"""
physics/electrostatic_field.py

Electrostatic Electric Field Utilities
for Quantum Cascade Lasers

Computes electric field from
electrostatic potential.

E = -dV/dz
"""

import numpy as np


def electric_field(z, potential):
    """
    Calculate electric field from potential.

    Parameters
    ----------
    z : ndarray
        Position grid (m)

    potential : ndarray
        Electrostatic potential (V)

    Returns
    -------
    ndarray
        Electric field (V/m)
    """

    z = np.asarray(z)
    potential = np.asarray(potential)

    return -np.gradient(potential, z)


def field_magnitude(field):
    """
    Electric field magnitude.
    """

    return np.abs(field)


def maximum_field(field):
    """
    Maximum electric field.
    """

    return np.max(np.abs(field))


def average_field(field):
    """
    Average electric field.
    """

    return np.mean(field)


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    z = np.linspace(
        0,
        20e-9,
        500
    )

    potential = np.linspace(
        0,
        5,
        len(z)
    )

    field = electric_field(
        z,
        potential
    )

    print("Maximum Field (V/m):")

    print(maximum_field(field))

    print()

    print("Average Field (V/m):")

    print(average_field(field))