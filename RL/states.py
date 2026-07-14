"""
states.py

Defines the state representation used by the
QCL Reinforcement Learning module.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class QCLState:
    """
    Represents the state of the Quantum Cascade Laser.

    Parameters
    ----------
    current : float
        Injection current (A)

    voltage : float
        Device voltage (V)

    temperature : float
        Device temperature (K)

    wavelength : float
        Output wavelength (µm)

    optical_power : float
        Optical output power (W)
    """

    current: float
    voltage: float
    temperature: float
    wavelength: float
    optical_power: float

    def to_tuple(self) -> Tuple:
        """
        Convert state into a tuple.

        Useful for tabular Q-Learning where tuples are
        used as dictionary keys.
        """
        return (
            round(self.current, 2),
            round(self.voltage, 2),
            round(self.temperature, 2),
            round(self.wavelength, 2),
            round(self.optical_power, 2),
        )

    def to_list(self):
        """
        Convert state to a list.

        Useful for neural-network based agents (DQN).
        """
        return [
            self.current,
            self.voltage,
            self.temperature,
            self.wavelength,
            self.optical_power,
        ]

    @classmethod
    def from_dict(cls, data):
        """
        Create a QCLState from a dictionary.
        """
        return cls(
            current=data.get("current", 0.0),
            voltage=data.get("voltage", 0.0),
            temperature=data.get("temperature", 300.0),
            wavelength=data.get("wavelength", 0.0),
            optical_power=data.get("optical_power", 0.0),
        )

    def copy(self):
        """
        Return a copy of the current state.
        """
        return QCLState(
            current=self.current,
            voltage=self.voltage,
            temperature=self.temperature,
            wavelength=self.wavelength,
            optical_power=self.optical_power,
        )

    def __str__(self):
        return (
            f"QCLState("
            f"I={self.current:.2f} A, "
            f"V={self.voltage:.2f} V, "
            f"T={self.temperature:.2f} K, "
            f"λ={self.wavelength:.2f} µm, "
            f"P={self.optical_power:.2f} W)"
        )