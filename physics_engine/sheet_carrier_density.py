"""
physics/sheet_carrier_density.py

Sheet Carrier Density Calculations
for Quantum Cascade Lasers
"""

import numpy as np


def sheet_carrier_density(z, carrier_density):
    """
    Sheet Carrier Density

    Ns = ∫ n(z) dz

    Parameters
    ----------
    z : ndarray
        Position (m)

    carrier_density : ndarray
        Carrier concentration (m^-3)

    Returns
    -------
    float
        Sheet carrier density (m^-2)
    """

    z = np.asarray(z)
    carrier_density = np.asarray(carrier_density)

    return np.trapz(carrier_density, z)


def average_carrier_density(carrier_density):
    """
    Average carrier concentration.
    """

    return np.mean(carrier_density)


def peak_carrier_density(carrier_density):
    """
    Peak carrier concentration.
    """

    return np.max(carrier_density)


if __name__ == "__main__":

    z = np.linspace(0, 20e-9, 1000)

    carrier_density = (
        1e22
        * np.exp(
            -((z - 10e-9) ** 2)
            /
            (2 * (2e-9) ** 2)
        )
    )

    Ns = sheet_carrier_density(
        z,
        carrier_density
    )

    print("Sheet Carrier Density")

    print(Ns)

    print()

    print("Average Density")

    print(
        average_carrier_density(
            carrier_density
        )
    )

    print()

    print("Peak Density")

    print(
        peak_carrier_density(
            carrier_density
        )
    )