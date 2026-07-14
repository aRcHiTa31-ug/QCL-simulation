"""
environment.py
Physics-based simulation environment for a Quantum Cascade Laser
(QCL), used by the QCL Reinforcement Learning module.

Wires together:
- RL.action           (discrete action space)
- RL.states           (QCLState observation representation)
- RL.hyperparameters  (operating bounds and step sizes)
- RL.reward           (RewardFunction)

This is a simplified, tunable physics approximation, not a full
electromagnetic/quantum transport simulation. Constants below are
placeholders - calibrate them to your actual device/simulation.
"""
from typing import List, Optional, Tuple

import numpy as np

from RL.action import Action, number_of_actions
from RL.states import QCLState
from RL.reward import RewardFunction
from RL.hyperparameters import (
    CURRENT_MIN,
    CURRENT_MAX,
    VOLTAGE_MIN,
    VOLTAGE_MAX,
    TEMPERATURE_MIN,
    TEMPERATURE_MAX,
    CASCADE_STAGE_MIN,
    CASCADE_STAGE_MAX,
    CURRENT_STEP,
    VOLTAGE_STEP,
    TEMPERATURE_STEP,
    STAGE_STEP,
)


class QCLPhysicsEnv:
    """
    Simplified QCL operating-point environment.

    Observation (via QCLState.to_list(), 5 values):
        [current, voltage, temperature, wavelength, optical_power]

    IMPORTANT - PARTIAL OBSERVABILITY NOTE:
    action.py defines INCREASE_STAGE / DECREASE_STAGE actions, and
    hyperparameters.py defines CASCADE_STAGE_MIN/MAX + STAGE_STEP
    for them - but states.QCLState has no `num_stages` field. The
    cascade stage count is therefore tracked *internally* by this
    environment (self._num_stages) and still affects the physics
    (it scales optical power), but it is NOT part of the state
    vector returned to the agent. The agent can only observe the
    downstream effect on optical_power, not the stage count itself.
    If you want the agent to fully observe this, add a
    `num_stages` field to QCLState and extend `to_list()` /
    `to_tuple()` accordingly - this file would then need a small
    update to include it.
    """

    # ---- Device physics constants (approximate - tune to your device) ----
    THRESHOLD_CURRENT_A = 0.9
    SLOPE_EFFICIENCY = 4.0        # W per A above threshold, per stage-normalized
    REFERENCE_STAGES = 25
    THERMAL_ROLLOVER_K = 340.0
    ROLLOVER_STRENGTH = 0.05

    BASE_WAVELENGTH_UM = 4.6
    WAVELENGTH_TEMP_COEFF_UM_PER_K = 0.0008   # small redshift with heating

    def __init__(
        self,
        reward_function: Optional[RewardFunction] = None,
        ambient_temperature: float = 300.0,
        seed: Optional[int] = None,
    ):
        self.reward_function = reward_function or RewardFunction(
            target_wavelength=self.BASE_WAVELENGTH_UM
        )
        self.ambient_temperature = ambient_temperature
        self._rng = np.random.default_rng(seed)

        self.state_size = 5
        self.action_size = number_of_actions()

        self._state: Optional[QCLState] = None
        self._num_stages: int = self.REFERENCE_STAGES
        self._step_count = 0

    # ---------------------------------------------------
    # Physics helpers
    # ---------------------------------------------------
    def _compute_optical_power(self, current, temperature, num_stages) -> float:
        """
        Lasing only above threshold current; power scales with
        stage count and degrades past a thermal rollover point.
        """
        if current <= self.THRESHOLD_CURRENT_A:
            return 0.0

        above_threshold = current - self.THRESHOLD_CURRENT_A
        stage_factor = num_stages / self.REFERENCE_STAGES
        power = self.SLOPE_EFFICIENCY * above_threshold * stage_factor

        if temperature > self.THERMAL_ROLLOVER_K:
            overheat = temperature - self.THERMAL_ROLLOVER_K
            power *= np.exp(-self.ROLLOVER_STRENGTH * overheat)

        noise = self._rng.normal(loc=0.0, scale=0.01)
        return max(0.0, power + noise)

    def _compute_wavelength(self, temperature) -> float:
        """
        Small temperature-dependent wavelength redshift, on top of
        the device's designed base wavelength.
        """
        return (
            self.BASE_WAVELENGTH_UM
            + self.WAVELENGTH_TEMP_COEFF_UM_PER_K
            * (temperature - self.ambient_temperature)
        )

    def _joule_heating_update(self, temperature, current, voltage) -> float:
        """
        Passive self-heating: temperature relaxes toward an
        equilibrium set by electrical dissipation, independent of
        any INCREASE/DECREASE_TEMPERATURE action taken this step.
        """
        dissipation = current * voltage  # Watts
        equilibrium_temp = self.ambient_temperature + dissipation * 2.0
        relaxation = 0.1
        return temperature + relaxation * (equilibrium_temp - temperature)

    def _state_to_reward_dict(self, state: QCLState, previous_power: float) -> dict:
        """
        Bridge QCLState -> the dict shape RewardFunction expects
        ('wavelength', 'energy', 'stability'). QCLState has no
        'energy' or 'stability' fields, so they are derived here:

          - energy    = electrical power drawn (voltage * current),
                        used as a proxy for energy cost.
          - stability = 1 / (1 + relative change in optical power
                        since the previous step); closer to 1.0
                        means output power is steady step-to-step.

        NOTE: this is a modeling choice, not something reward.py
        or states.py define themselves - reconsider these mappings
        if you want a different notion of "energy"/"stability".
        """
        electrical_power = state.voltage * state.current
        power_delta = abs(state.optical_power - previous_power)
        relative_change = power_delta / max(previous_power, 1e-6)
        stability = 1.0 / (1.0 + relative_change)

        return {
            "wavelength": state.wavelength,
            "energy": electrical_power,
            "stability": stability,
        }

    # ---------------------------------------------------
    # Gym-like interface
    # ---------------------------------------------------
    def reset(self) -> List[float]:
        """
        Reset the device to a safe, sub-threshold starting point.
        """
        current = self._rng.uniform(CURRENT_MIN, self.THRESHOLD_CURRENT_A)
        voltage = self._rng.uniform(
            VOLTAGE_MIN, VOLTAGE_MIN + (VOLTAGE_MAX - VOLTAGE_MIN) * 0.3
        )
        temperature = self.ambient_temperature
        self._num_stages = int(
            self._rng.integers(CASCADE_STAGE_MIN, CASCADE_STAGE_MAX + 1)
        )

        wavelength = self._compute_wavelength(temperature)
        optical_power = self._compute_optical_power(
            current, temperature, self._num_stages
        )

        self._state = QCLState(
            current=current,
            voltage=voltage,
            temperature=temperature,
            wavelength=wavelength,
            optical_power=optical_power,
        )
        self._step_count = 0
        return self._state.to_list()

    def step(self, action) -> Tuple[List[float], float, bool, dict]:
        """
        Apply an action, update device state, and compute reward.
        """
        action = Action(int(action)) if not isinstance(action, Action) else action
        previous_state = self._state.copy()

        current = self._state.current
        voltage = self._state.voltage
        temperature = self._state.temperature
        num_stages = self._num_stages

        if action == Action.INCREASE_CURRENT:
            current += CURRENT_STEP
        elif action == Action.DECREASE_CURRENT:
            current -= CURRENT_STEP
        elif action == Action.INCREASE_VOLTAGE:
            voltage += VOLTAGE_STEP
        elif action == Action.DECREASE_VOLTAGE:
            voltage -= VOLTAGE_STEP
        elif action == Action.INCREASE_TEMPERATURE:
            temperature += TEMPERATURE_STEP
        elif action == Action.DECREASE_TEMPERATURE:
            temperature -= TEMPERATURE_STEP
        elif action == Action.INCREASE_STAGE:
            num_stages += STAGE_STEP
        elif action == Action.DECREASE_STAGE:
            num_stages -= STAGE_STEP
        elif action == Action.HOLD:
            pass
        else:
            raise ValueError(f"Unrecognized action: {action}")

        # Passive Joule heating, independent of the temperature action.
        temperature = self._joule_heating_update(temperature, current, voltage)

        # Clamp to physical/operational bounds.
        current = float(np.clip(current, CURRENT_MIN, CURRENT_MAX))
        voltage = float(np.clip(voltage, VOLTAGE_MIN, VOLTAGE_MAX))
        temperature = float(np.clip(temperature, TEMPERATURE_MIN, TEMPERATURE_MAX))
        num_stages = int(np.clip(num_stages, CASCADE_STAGE_MIN, CASCADE_STAGE_MAX))
        self._num_stages = num_stages

        wavelength = self._compute_wavelength(temperature)
        optical_power = self._compute_optical_power(current, temperature, num_stages)

        self._state = QCLState(
            current=current,
            voltage=voltage,
            temperature=temperature,
            wavelength=wavelength,
            optical_power=optical_power,
        )
        self._step_count += 1

        reward, done, info = self._compute_reward_and_done(previous_state)

        return self._state.to_list(), reward, done, info

    # ---------------------------------------------------
    # Reward / termination
    # ---------------------------------------------------
    def _compute_reward_and_done(self, previous_state: QCLState) -> Tuple[float, bool, dict]:
        info = {}

        # Hard safety bounds -> destructive condition, end episode.
        if self._state.temperature >= TEMPERATURE_MAX:
            info["termination_reason"] = "over_temperature"
            return -100.0, True, info
        if self._state.current >= CURRENT_MAX:
            info["termination_reason"] = "over_current"
            return -100.0, True, info
        if self._state.voltage >= VOLTAGE_MAX:
            info["termination_reason"] = "over_voltage"
            return -100.0, True, info

        previous_dict = self._state_to_reward_dict(
            previous_state, previous_state.optical_power
        )
        next_dict = self._state_to_reward_dict(
            self._state, previous_state.optical_power
        )

        reward = self.reward_function.compute_reward(
            state=previous_dict,
            action=None,
            next_state=next_dict,
        )
        reward += self.reward_function.success_reward(next_dict)

        wavelength_error = abs(
            self._state.wavelength - self.reward_function.target_wavelength
        )
        if wavelength_error < self.reward_function.wavelength_tolerance:
            info["termination_reason"] = "target_wavelength_reached"
            return float(reward), True, info

        return float(reward), False, info

    # ---------------------------------------------------
    # Rendering / cleanup
    # ---------------------------------------------------
    def render(self) -> None:
        """Print the current device operating point."""
        print(
            f"Step {self._step_count:4d} | {self._state} | "
            f"Stages={self._num_stages}"
        )

    def close(self) -> None:
        """No external resources held; provided for interface parity."""
        pass