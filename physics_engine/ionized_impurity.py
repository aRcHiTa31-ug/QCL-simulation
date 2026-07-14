"""
physics/ionized_impurity.py

Ionized Impurity Scattering
for Quantum Cascade Lasers
"""

import numpy as np


def ionized_impurity_rate(
    impurity_density,
    dielectric_constant,
    effective_mass
):
    """
    Ionized Impurity Scattering

    W ∝ Ni / (ε² m*)
    """

    return (
        impurity_density
        /
        (
            dielectric_constant**2
            * effective_mass
        )
    )


def impurity_relaxation_time(
    scattering_rate
):
    """
    τ = 1/W
    """

    if scattering_rate <= 0:
        return np.inf

    return 1.0 / scattering_rate


if __name__ == "__main__":

    rate = ionized_impurity_rate(
        impurity_density=1e22,
        dielectric_constant=13.9,
        effective_mass=0.043
    )

    print("Ionized Impurity Rate")

    print(rate)

    print()

    print("Relaxation Time")

    print(
        impurity_relaxation_time(rate)
    )