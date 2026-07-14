"""
physics/alloy_disorder.py

Alloy Disorder Scattering
for Quantum Cascade Lasers
"""

import numpy as np


def alloy_scattering_rate(
    alloy_fraction,
    scattering_potential,
    density_of_states
):
    """
    Alloy Disorder Scattering

    W ∝ x(1-x)V²g(E)
    """

    x = alloy_fraction

    return (
        x
        * (1 - x)
        * scattering_potential**2
        * density_of_states
    )


def alloy_relaxation_time(
    scattering_rate
):
    """
    τ = 1/W
    """

    if scattering_rate <= 0:
        return np.inf

    return 1.0 / scattering_rate


if __name__ == "__main__":

    rate = alloy_scattering_rate(
        alloy_fraction=0.53,
        scattering_potential=0.15,
        density_of_states=1e45
    )

    print("Alloy Disorder Rate")

    print(rate)

    print()

    print("Relaxation Time")

    print(alloy_relaxation_time(rate))