"""
reward.py
Reward function module for QCL Reinforcement Learning environment.
Defines how the agent is rewarded based on:
- Photon emission / wavelength alignment
- Energy optimization
- Stability of output
"""
import warnings
from typing import Mapping, Union

import numpy as np

StateLike = Mapping[str, float]


class RewardFunction:
    """
    Computes reward for QCL RL agent actions based on how close the
    device's output wavelength is to a target, how much energy it
    consumes, and how stable its output is.
    """

    def __init__(
        self,
        target_wavelength: float = 8.0,
        wavelength_tolerance: float = 0.5,
        energy_weight: float = 0.3,
        stability_weight: float = 0.2,
        success_bonus: float = 5.0,
        missing_key_policy: str = "warn",
    ):
        """
        Args:
            target_wavelength: Desired output wavelength (e.g. microns).
            wavelength_tolerance: Absolute error below which the
                wavelength is considered "aligned" and given max reward.
            energy_weight: Non-negative weight penalizing energy use.
            stability_weight: Non-negative weight rewarding stability.
            success_bonus: Reward returned by `success_reward` when
                the target wavelength is reached.
            missing_key_policy: One of "raise", "warn", "silent".
                Controls what happens when a state dict is missing an
                expected key (see `compute_reward`). Defaults to "warn"
                since silently treating a missing wavelength as 0.0
                (i.e. "wildly off target") or missing energy as 0.0
                (i.e. "free energy, no penalty") can distort training
                without anyone noticing.
        """
        if wavelength_tolerance <= 0:
            raise ValueError("wavelength_tolerance must be positive.")
        if energy_weight < 0:
            raise ValueError("energy_weight must be non-negative.")
        if stability_weight < 0:
            raise ValueError("stability_weight must be non-negative.")
        if missing_key_policy not in ("raise", "warn", "silent"):
            raise ValueError(
                "missing_key_policy must be one of 'raise', 'warn', 'silent'."
            )

        self.target_wavelength = target_wavelength
        self.wavelength_tolerance = wavelength_tolerance
        self.energy_weight = energy_weight
        self.stability_weight = stability_weight
        self.success_bonus = success_bonus
        self.missing_key_policy = missing_key_policy

    # -----------------------------------------
    # Safe field access
    # -----------------------------------------
    def _get(self, state: StateLike, key: str, default: float) -> float:
        """
        Fetch `key` from `state`, applying `missing_key_policy` if
        absent, so a missing physics reading can't silently masquerade
        as a real (and misleading) value.
        """
        if key in state:
            return float(state[key])

        message = (
            f"State is missing expected key '{key}'; "
            f"falling back to default={default}. This will bias "
            f"the reward unless '{key}' is genuinely meant to be "
            f"{default} here."
        )
        if self.missing_key_policy == "raise":
            raise KeyError(message)
        if self.missing_key_policy == "warn":
            warnings.warn(message, stacklevel=3)
        return default

    # -----------------------------------------
    # Main reward function
    # -----------------------------------------
    def compute_reward(
        self,
        state: StateLike,
        action,
        next_state: StateLike,
    ) -> float:
        """
        Calculate reward for a (state, action, next_state) transition.

        Args:
            state: Physics state before the action (dict-like, with
                optional 'wavelength', 'energy', 'stability' keys).
            action: Action taken by the RL agent (unused in the
                current reward shaping, but accepted for API
                compatibility with reward functions that need it).
            next_state: Physics state after the action.

        Returns:
            Scalar reward for this transition.
        """
        wavelength = self._get(next_state, "wavelength", default=0.0)
        energy = self._get(next_state, "energy", default=0.0)
        stability = self._get(next_state, "stability", default=1.0)

        if energy < 0:
            warnings.warn(
                f"Received negative energy ({energy}); this will "
                f"produce a *positive* energy_reward, which is "
                f"physically suspicious unless negative energy has "
                f"a specific meaning in your model.",
                stacklevel=2,
            )
        if not 0.0 <= stability <= 1.0:
            warnings.warn(
                f"stability={stability} is outside the expected "
                f"[0, 1] range; reward contribution may be larger "
                f"than intended.",
                stacklevel=2,
            )

        # 1. Wavelength alignment reward.
        wavelength_error = abs(wavelength - self.target_wavelength)
        if wavelength_error < self.wavelength_tolerance:
            wavelength_reward = 1.0
        else:
            wavelength_reward = -wavelength_error

        # 2. Energy efficiency reward (lower energy = better).
        energy_reward = -self.energy_weight * energy

        # 3. Stability reward (higher stability = better).
        stability_reward = self.stability_weight * stability

        total_reward = wavelength_reward + energy_reward + stability_reward
        return float(total_reward)

    # -----------------------------------------
    # Optional: sparse success reward
    # -----------------------------------------
    def success_reward(self, state: StateLike) -> float:
        """
        Extra sparse reward when the system reaches the target
        wavelength within tolerance.
        """
        wavelength = self._get(state, "wavelength", default=0.0)
        if abs(wavelength - self.target_wavelength) < self.wavelength_tolerance:
            return self.success_bonus
        return 0.0