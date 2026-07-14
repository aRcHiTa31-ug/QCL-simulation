"""
physics/electric_potential.py

Electric Potential Utilities
for Quantum Cascade Lasers

Implements:

1. Potential Difference
2. Electrostatic Potential Energy
3. Built-in Potential
"""

import numpy as np

# ---------------------------------------------------------
# Physical Constants
# ---------------------------------------------------------

Q = 1.602176634e-19  # C


def potential_difference(V1, V2):
    """
    Potential Difference

        ΔV = V2 - V1

    Parameters
    ----------
    V1 : float
        Initial Potential (V)

    V2 : float
        Final Potential (V)

    Returns
    -------
    float
        Potential Difference (V)
    """

    return V2 - V1


def electrostatic_potential_energy(
    potential,
    charge=-Q
):
    """
    Electrostatic Potential Energy

        U = qV

    Parameters
    ----------
    potential : ndarray or float
        Electric Potential (V)

    charge : float
        Charge (C)

    Returns
    -------
    ndarray or float
        Potential Energy (J)
    """

    return charge * np.asarray(potential)


def built_in_potential(
    donor_density,
    acceptor_density,
    intrinsic_density,
    temperature
):
    """
    Built-in Potential

        Vbi = (kT/q) ln(NA ND / ni²)

    Parameters
    ----------
    donor_density : float

    acceptor_density : float

    intrinsic_density : float

    temperature : float

    Returns
    -------
    float
        Built-in Potential (V)
    """

    k = 1.380649e-23

    return (
        (k * temperature) / Q
    ) * np.log(
        (donor_density * acceptor_density)
        /
        (intrinsic_density ** 2)
    )


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    V = np.linspace(
        0,
        5,
        10
    )

    energy = electrostatic_potential_energy(V)

    print("Potential Energy")

    print(energy)

    print()

    print(
        "Potential Difference:",
        potential_difference(
            0,
            5
        )
    )

    print()

    print(
        "Built-in Potential:",
        built_in_potential(
            donor_density=1e23,
            acceptor_density=1e22,
            intrinsic_density=1e16,
            temperature=300
        )
    )