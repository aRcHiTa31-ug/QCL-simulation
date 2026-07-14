"""
physics/lo_phonon.py

Longitudinal Optical (LO) Phonon Scattering
for Quantum Cascade Lasers

Implements

1. LO Phonon Occupation Number
2. LO Phonon Emission Rate
3. LO Phonon Absorption Rate
4. Total LO Phonon Scattering Rate
"""

import numpy as np

# ---------------------------------------------------------
# Physical Constants
# ---------------------------------------------------------

HBAR = 1.054571817e-34      # J.s
K_B = 1.380649e-23          # J/K


def phonon_occupation(
    phonon_energy,
    temperature
):
    """
    Bose-Einstein Occupation Number

    N = 1 / (exp(Eph/kT)-1)
    """

    exponent = phonon_energy / (
        K_B * temperature
    )

    exponent = np.clip(
        exponent,
        -700,
        700
    )

    return 1.0 / (
        np.exp(exponent) - 1
    )


def emission_rate(
    coupling_constant,
    phonon_energy,
    temperature
):
    """
    LO Phonon Emission

    W ∝ (N + 1)
    """

    N = phonon_occupation(
        phonon_energy,
        temperature
    )

    return coupling_constant * (N + 1)


def absorption_rate(
    coupling_constant,
    phonon_energy,
    temperature
):
    """
    LO Phonon Absorption

    W ∝ N
    """

    N = phonon_occupation(
        phonon_energy,
        temperature
    )

    return coupling_constant * N


def total_lo_scattering(
    coupling_constant,
    phonon_energy,
    temperature
):
    """
    Total LO Phonon Scattering
    """

    return (

        emission_rate(

            coupling_constant,

            phonon_energy,

            temperature

        )

        +

        absorption_rate(

            coupling_constant,

            phonon_energy,

            temperature

        )

    )


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    Q = 1.602176634e-19

    Eph = 0.036 * Q

    rate = total_lo_scattering(

        2e11,

        Eph,

        300

    )

    print("LO Scattering Rate")

    print(rate)