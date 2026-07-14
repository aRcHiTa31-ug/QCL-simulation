"""
physics/interface_roughness.py

Interface Roughness Scattering
for Quantum Cascade Lasers
"""

import numpy as np


def interface_roughness_rate(
    roughness_height,
    correlation_length,
    wavefunction_overlap
):
    """
    Interface Roughness Scattering

    W ∝ Δ² Λ² |Overlap|²
    """

    return (
        roughness_height**2
        * correlation_length**2
        * wavefunction_overlap**2
    )


def interface_relaxation_time(
    scattering_rate
):
    """
    τ = 1/W
    """

    if scattering_rate <= 0:
        return np.inf

    return 1.0 / scattering_rate


if __name__ == "__main__":

    rate = interface_roughness_rate(
        roughness_height=0.2e-9,
        correlation_length=8e-9,
        wavefunction_overlap=0.75
    )

    print("Interface Roughness Rate")

    print(rate)

    print()

    print("Relaxation Time")

    print(interface_relaxation_time(rate))