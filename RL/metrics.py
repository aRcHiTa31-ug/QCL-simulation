"""
metrics.py
Evaluation metrics for QCL Reinforcement Learning system.
Used for:
- training evaluation
- inference analysis
- physics performance tracking
"""
from typing import List, Optional, Sequence

import numpy as np


class Metrics:
    """
    Tracks episode-level RL metrics and step-level QCL physics
    metrics (current, voltage, temperature, optical power).
    """

    def __init__(self):
        self.episode_rewards: List[float] = []
        self.episode_lengths: List[int] = []
        # QCL-specific metrics
        self.optical_power_history: List[float] = []
        self.voltage_history: List[float] = []
        self.current_history: List[float] = []
        self.temperature_history: List[float] = []

    # ---------------------------------------------------
    # Episode tracking
    # ---------------------------------------------------
    def log_episode(self, reward: float, length: int) -> None:
        """Record the outcome of one completed episode."""
        if length < 0:
            raise ValueError("length must be >= 0.")
        self.episode_rewards.append(float(reward))
        self.episode_lengths.append(int(length))

    # ---------------------------------------------------
    # Step-level physics logging
    # ---------------------------------------------------
    def log_step(
        self,
        current: float,
        voltage: float,
        temperature: float,
        optical_power: float,
    ) -> None:
        """
        Record one step's physics readings.

        NOTE: This takes explicit named values rather than a raw
        state vector on purpose. Environment state layouts change
        (e.g. inserting a `num_stages` field shifts every index
        after it), and unpacking by position silently logs the
        wrong quantity under the wrong name with no error. Pass
        values explicitly, e.g.:

            metrics.log_step(
                current=state[0],
                voltage=state[1],
                temperature=state[2],
                optical_power=state[4],  # index depends on your env!
            )
        """
        self.current_history.append(float(current))
        self.voltage_history.append(float(voltage))
        self.temperature_history.append(float(temperature))
        self.optical_power_history.append(float(optical_power))

    def log_step_from_state(
        self,
        state: Sequence[float],
        current_idx: int = 0,
        voltage_idx: int = 1,
        temperature_idx: int = 2,
        optical_power_idx: int = 4,
    ) -> None:
        """
        Convenience wrapper for logging directly from a raw state
        vector, with explicit (overridable) indices.

        Defaults match a state layout of:
            [current, voltage, temperature, num_stages, optical_power]
        as produced by QCLPhysicsEnv. If your environment's state
        layout differs, pass the correct indices explicitly.
        """
        required = max(current_idx, voltage_idx, temperature_idx, optical_power_idx)
        if len(state) <= required:
            raise ValueError(
                f"state has length {len(state)}, but index {required} "
                f"was requested. Check your index arguments."
            )
        self.log_step(
            current=state[current_idx],
            voltage=state[voltage_idx],
            temperature=state[temperature_idx],
            optical_power=state[optical_power_idx],
        )

    # ---------------------------------------------------
    # Basic statistics
    # ---------------------------------------------------
    def mean_reward(self) -> float:
        return float(np.mean(self.episode_rewards)) if self.episode_rewards else 0.0

    def std_reward(self) -> float:
        return float(np.std(self.episode_rewards)) if self.episode_rewards else 0.0

    def best_episode(self) -> Optional[int]:
        """Index of the episode with the highest reward, or None if empty."""
        if not self.episode_rewards:
            return None
        return int(np.argmax(self.episode_rewards))

    def best_reward(self) -> Optional[float]:
        """Highest recorded episode reward, or None if empty."""
        if not self.episode_rewards:
            return None
        return float(np.max(self.episode_rewards))

    def mean_episode_length(self) -> float:
        return float(np.mean(self.episode_lengths)) if self.episode_lengths else 0.0

    # ---------------------------------------------------
    # QCL-specific metrics
    # ---------------------------------------------------
    def max_optical_power(self) -> float:
        return float(max(self.optical_power_history)) if self.optical_power_history else 0.0

    def avg_optical_power(self) -> float:
        return float(np.mean(self.optical_power_history)) if self.optical_power_history else 0.0

    def efficiency(self) -> float:
        """
        Simple physics-inspired efficiency metric:
        optical power out per unit electrical power in
        (optical_power / (current * voltage)).

        NOTE: units matter here. If current is logged in mA and
        voltage in V, this returns mW(optical) per mW*1000... i.e.
        the numerator and denominator won't be in consistent units
        unless you convert current to Amps first. Pass
        `current_in_milliamps=True` (default) if your current
        history is in mA, and it will be converted to A internally
        so the result is a dimensionless ratio of optical mW to
        electrical W.
        """
        return self._efficiency(current_in_milliamps=True)

    def _efficiency(self, current_in_milliamps: bool = True) -> float:
        if not self.current_history or not self.voltage_history or not self.optical_power_history:
            return 0.0

        lengths = {
            len(self.current_history),
            len(self.voltage_history),
            len(self.optical_power_history),
        }
        if len(lengths) != 1:
            raise ValueError(
                "current_history, voltage_history, and "
                "optical_power_history have mismatched lengths "
                f"({lengths}); metrics were logged inconsistently."
            )

        current = np.array(self.current_history, dtype=float)
        if current_in_milliamps:
            current = current / 1000.0  # mA -> A

        voltage = np.array(self.voltage_history, dtype=float)
        optical = np.array(self.optical_power_history, dtype=float)

        power_in_w = current * voltage
        # Avoid division by zero for near-zero drive power without
        # silently producing huge/misleading efficiency spikes.
        valid = power_in_w > 1e-6
        if not np.any(valid):
            return 0.0

        return float(np.mean(optical[valid] / power_in_w[valid]))

    # ---------------------------------------------------
    # Summary
    # ---------------------------------------------------
    def summary(self) -> dict:
        """Return all key metrics as a single dict."""
        return {
            "num_episodes": len(self.episode_rewards),
            "mean_reward": self.mean_reward(),
            "std_reward": self.std_reward(),
            "best_episode": self.best_episode(),
            "best_reward": self.best_reward(),
            "mean_episode_length": self.mean_episode_length(),
            "max_optical_power": self.max_optical_power(),
            "avg_optical_power": self.avg_optical_power(),
            "efficiency": self.efficiency(),
        }

    def print_summary(self) -> None:
        """Pretty-print the metrics summary."""
        s = self.summary()
        print("\n========== QCL RL Metrics ==========")
        print(f"Episodes           : {s['num_episodes']}")
        print(f"Mean Reward        : {s['mean_reward']:.3f}")
        print(f"Std Reward         : {s['std_reward']:.3f}")
        print(f"Best Episode       : {s['best_episode']}")
        print(f"Best Reward        : {s['best_reward']}")
        print(f"Mean Ep. Length    : {s['mean_episode_length']:.2f}")
        print(f"Max Optical Power  : {s['max_optical_power']:.3f} mW")
        print(f"Avg Optical Power  : {s['avg_optical_power']:.3f} mW")
        print(f"Efficiency         : {s['efficiency']:.5f}")
        print("=====================================\n")

    # ---------------------------------------------------
    # Reset
    # ---------------------------------------------------
    def reset(self) -> None:
        """Clear all recorded metrics."""
        self.__init__()