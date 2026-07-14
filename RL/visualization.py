"""
visualization.py
Visualization utilities for the
QCL Reinforcement Learning module.
"""
import os
from typing import Optional, Sequence

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from typing import Optional

class TrainingVisualizer:
    """
    Visualize RL training statistics and QCL physics metrics.

    All plotting methods accept an optional `save_path`. If given,
    the figure is saved to disk instead of (or in addition to)
    being shown interactively — this matters because calling
    `plt.show()` in a headless environment (a remote server, CI,
    or a script run without a display) will either hang or raise,
    depending on the matplotlib backend.
    """

    @staticmethod
    def _finalize(fig, save_path: Optional[str], show: bool) -> None:
        """
        Save and/or display a figure, then always close it to avoid
        leaking memory across many calls (matplotlib keeps closed-
        over figures alive until explicitly closed).
        """
        if save_path:
            directory = os.path.dirname(save_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            fig.savefig(save_path, dpi=150, bbox_inches="tight")
            print(f"[TrainingVisualizer] Saved plot to: {save_path}")

        if show:
            try:
                plt.show()
            except Exception as exc:
                # Typically happens in headless environments with no
                # display backend configured. Don't crash the whole
                # training/analysis run over a plotting issue.
                print(
                    f"[TrainingVisualizer] Could not display plot "
                    f"interactively ({exc}). "
                    f"{'Use save_path to save it instead.' if not save_path else ''}"
                )

        plt.close(fig)

    @staticmethod
    def plot_rewards(
        rewards: Sequence[float],
        window: int = 20,
        save_path: Optional[str] = None,
        show: bool = True,
    ) -> Optional[Figure]:
        """
        Plot episode rewards and a moving average.
        """
        if len(rewards) == 0:
            print("No rewards available.")
            return

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(rewards, label="Episode Reward", linewidth=1.2)

        if len(rewards) >= window:
            moving_avg = np.convolve(
                rewards, np.ones(window) / window, mode="valid"
            )
            ax.plot(
                range(window - 1, len(rewards)),
                moving_avg,
                linewidth=2,
                label=f"{window}-Episode Average",
            )
        elif window > 0:
            print(
                f"Note: only {len(rewards)} episode(s) available, fewer "
                f"than window={window}; skipping moving average."
            )

        ax.set_title("Training Reward")
        ax.set_xlabel("Episode")
        ax.set_ylabel("Reward")
        ax.grid(True)
        ax.legend()
        fig.tight_layout()

        if show or save_path:
            TrainingVisualizer._finalize(fig, save_path, show)
        else:
            return fig

    @staticmethod
    def plot_epsilon(
        epsilon_history: Sequence[float],
        save_path: Optional[str] = None,
        show: bool = True,
    ) -> Optional[Figure]:
        """
        Plot epsilon decay over training.
        """
        if len(epsilon_history) == 0:
            print("No epsilon history available.")
            return

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(epsilon_history, linewidth=2)
        ax.set_title("Exploration Rate (Epsilon)")
        ax.set_xlabel("Episode")
        ax.set_ylabel("Epsilon")
        ax.set_ylim(bottom=0)
        ax.grid(True)
        fig.tight_layout()

        if show or save_path:
            TrainingVisualizer._finalize(fig, save_path, show)
        else:
            return fig

    @staticmethod
    def plot_physics(
        current_history: Sequence[float],
        voltage_history: Sequence[float],
        temperature_history: Sequence[float],
        optical_power_history: Sequence[float],
        save_path: Optional[str] = None,
        show: bool = True,
    ) -> Optional[Figure]:
        """
        Plot QCL step-level physics traces (current, voltage,
        temperature, optical power) as a 2x2 grid of subplots.

        Expects the four history lists from `metrics.Metrics`
        (current_history, voltage_history, temperature_history,
        optical_power_history). They must all be the same length.
        """
        lengths = {
            len(current_history),
            len(voltage_history),
            len(temperature_history),
            len(optical_power_history),
        }
        if lengths == {0}:
            print("No physics history available.")
            return
        if len(lengths) != 1:
            raise ValueError(
                f"Physics history arrays have mismatched lengths: "
                f"current={len(current_history)}, "
                f"voltage={len(voltage_history)}, "
                f"temperature={len(temperature_history)}, "
                f"optical_power={len(optical_power_history)}. "
                f"They should all be logged together, one entry per step."
            )

        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        panels = [
            (axes[0, 0], current_history, "Current", "mA", "tab:blue"),
            (axes[0, 1], voltage_history, "Voltage", "V", "tab:orange"),
            (axes[1, 0], temperature_history, "Temperature", "K", "tab:red"),
            (axes[1, 1], optical_power_history, "Optical Power", "mW", "tab:green"),
        ]
        for ax, data, title, unit, color in panels:
            ax.plot(data, linewidth=1.2, color=color)
            ax.set_title(title)
            ax.set_xlabel("Step")
            ax.set_ylabel(unit)
            ax.grid(True)

        fig.suptitle("QCL Physics Traces")
        fig.tight_layout()

        if show or save_path:
            TrainingVisualizer._finalize(fig, save_path, show)
        else:
            return fig

    @staticmethod
    def plot_training(
        rewards: Sequence[float],
        epsilon_history: Sequence[float],
        save_dir: Optional[str] = None,
        show: bool = True,
    ) -> None:
        """
        Plot both reward and epsilon curves.

        If `save_dir` is given, saves each plot as a separate PNG
        inside that directory (rewards.png, epsilon.png) rather than
        requiring a single combined save path, since these are two
        logically independent figures.
        """
        reward_path = os.path.join(save_dir, "rewards.png") if save_dir else None
        epsilon_path = os.path.join(save_dir, "epsilon.png") if save_dir else None

        TrainingVisualizer.plot_rewards(rewards, save_path=reward_path, show=show)
        TrainingVisualizer.plot_epsilon(epsilon_history, save_path=epsilon_path, show=show)