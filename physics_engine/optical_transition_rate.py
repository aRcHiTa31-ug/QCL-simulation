"""
physics/optical_transition_rate.py

Optical Transition Rate
for Quantum Cascade Lasers

Implements

1. Spontaneous Transition Rate
2. Stimulated Transition Rate
"""

import numpy as np

from physics_engine.oscillator_strength import oscillator_strength
from physics_engine.intersubband_transition import transition_energy

# ---------------------------------------------------------
# Physical Constants
# ---------------------------------------------------------

Q = 1.602176634e-19
HBAR = 1.054571817e-34
EPSILON0 = 8.854187817e-12
C = 299792458


def spontaneous_transition_rate(
    z,
    psi_upper,
    psi_lower,
    upper_energy,
    lower_energy,
    effective_mass,
    refractive_index=3.2
):
    """
    Simplified spontaneous emission rate.
    """

    delta_e = transition_energy(
        upper_energy,
        lower_energy
    )

    omega = delta_e / HBAR

    f = oscillator_strength(

        z,

        psi_upper,

        psi_lower,

        upper_energy,

        lower_energy,

        effective_mass

    )

    return (
        (f * omega**2)
        /
        (
            3
            * np.pi
            * EPSILON0
            * refractive_index
            * C**3
        )
    )


def stimulated_transition_rate(
    spontaneous_rate,
    photon_density
):
    """
    Stimulated Transition Rate
    """

    return spontaneous_rate * photon_density


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    from physics.schrodinger import Q, M0

    z = np.linspace(
        0,
        10e-9,
        1000
    )

    psi1 = np.sin(
        np.pi * z / z[-1]
    )

    psi2 = np.sin(
        2 * np.pi * z / z[-1]
    )

    psi1 /= np.sqrt(
        np.trapz(
            np.abs(psi1)**2,
            z
        )
    )

    psi2 /= np.sqrt(
        np.trapz(
            np.abs(psi2)**2,
            z
        )
    )

    rate = spontaneous_transition_rate(

        z,

        psi2,

        psi1,

        0.275 * Q,

        0.120 * Q,

        0.043 * M0

    )

    print()

    print("Spontaneous Transition Rate")

    print(rate)

    print()

    print("Stimulated Transition Rate")

    print(
        stimulated_transition_rate(
            rate,
            1e20
        )
    )