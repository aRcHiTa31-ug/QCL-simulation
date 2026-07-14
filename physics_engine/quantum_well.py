"""
physics/quantum_well.py

Quantum Well Energy Calculations
for Quantum Cascade Lasers

Implements:

1. Infinite Quantum Well Energy
2. Finite Quantum Well Approximation
"""

import numpy as np

# ---------------------------------------------------------
# Physical Constants
# ---------------------------------------------------------

HBAR = 1.054571817e-34      # J.s
M0 = 9.10938356e-31         # kg
Q = 1.602176634e-19         # C


def infinite_well_energy(level, width, effective_mass):
    """
    Infinite Quantum Well Energy

        En = (n²π²ħ²)/(2mL²)

    Parameters
    ----------
    level : int
        Quantum number (1,2,3...)

    width : float
        Well width (m)

    effective_mass : float
        Effective mass (kg)

    Returns
    -------
    float
        Energy (J)
    """

    n = level

    return (
        n ** 2
        * np.pi ** 2
        * HBAR ** 2
        / (2 * effective_mass * width ** 2)
    )


def infinite_well_energy_ev(level, width, effective_mass):
    """
    Energy in eV
    """

    return infinite_well_energy(
        level,
        width,
        effective_mass
    ) / Q


def finite_well_correction(
    energy,
    barrier_height
):
    """
    Simple finite well approximation.

    Energy cannot exceed barrier height.
    """

    return min(
        energy,
        0.99 * barrier_height
    )


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    width = 5e-9

    m_eff = 0.043 * M0

    barrier = 0.52 * Q

    for n in range(1, 6):

        E = infinite_well_energy(
            n,
            width,
            m_eff
        )

        Ef = finite_well_correction(
            E,
            barrier
        )

        print(
            f"Level {n}: "
            f"{E/Q:.4f} eV "
            f"(Finite: {Ef/Q:.4f} eV)"
        )