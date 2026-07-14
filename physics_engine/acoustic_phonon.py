"""
physics/acoustic_phonon.py

Acoustic Phonon Scattering
for Quantum Cascade Lasers
"""

import numpy as np

K_B = 1.380649e-23


def acoustic_scattering_rate(
    deformation_potential,
    temperature,
    density_of_states
):
    """
    Acoustic Phonon Scattering

    W ∝ D² kT g(E)
    """

    return (
        deformation_potential**2
        * K_B
        * temperature
        * density_of_states
    )


def acoustic_relaxation_time(
    scattering_rate
):
    """
    τ = 1/W
    """

    if scattering_rate <= 0:
        return np.inf

    return 1.0 / scattering_rate


if __name__ == "__main__":

    rate = acoustic_scattering_rate(
        deformation_potential=8.0,
        temperature=300,
        density_of_states=1e45
    )

    print("Acoustic Scattering Rate")

    print(rate)

    print()

    print("Relaxation Time")

    print(acoustic_relaxation_time(rate))