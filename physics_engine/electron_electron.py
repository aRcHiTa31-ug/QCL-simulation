"""
physics/electron_electron.py

Electron-Electron Scattering
for Quantum Cascade Lasers
"""

import numpy as np


def electron_electron_rate(
    carrier_density,
    temperature
):
    """
    Electron-Electron Scattering

    Simplified

    W ∝ n √T
    """

    return (
        carrier_density
        * np.sqrt(temperature)
    )


def electron_electron_lifetime(
    scattering_rate
):
    """
    τ = 1/W
    """

    if scattering_rate <= 0:
        return np.inf

    return 1.0 / scattering_rate


if __name__ == "__main__":

    rate = electron_electron_rate(
        carrier_density=5e22,
        temperature=300
    )

    print("Electron-Electron Rate")

    print(rate)

    print()

    print("Lifetime")

    print(
        electron_electron_lifetime(rate)
    )