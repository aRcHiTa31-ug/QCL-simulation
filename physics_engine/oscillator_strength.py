"""
physics/oscillator_strength.py

Oscillator Strength Calculations
for Quantum Cascade Lasers

Implements

1. Oscillator Strength
2. Normalized Oscillator Strength
"""

import numpy as np

from physics_engine.intersubband_transition import transition_energy
from physics_engine.dipole_matrix import dipole_matrix_element

# ---------------------------------------------------------
# Physical Constants
# ---------------------------------------------------------

HBAR = 1.054571817e-34      # J.s
M0 = 9.10938356e-31         # kg


def oscillator_strength(
    z,
    psi_upper,
    psi_lower,
    upper_energy,
    lower_energy,
    effective_mass
):
    """
    Oscillator Strength

    f = (2m*ΔE|z_ul|²)/ħ²

    Parameters
    ----------
    z : ndarray

    psi_upper : ndarray

    psi_lower : ndarray

    upper_energy : float
        J

    lower_energy : float
        J

    effective_mass : float
        kg

    Returns
    -------
    float
    """

    delta_e = transition_energy(
        upper_energy,
        lower_energy
    )

    z_ul = dipole_matrix_element(
        z,
        psi_upper,
        psi_lower
    )

    return (
        2
        * effective_mass
        * delta_e
        * z_ul**2
    ) / (HBAR**2)


def normalized_oscillator_strength(
    *args,
    **kwargs
):
    """
    Clamp oscillator strength
    between 0 and 1.
    """

    f = oscillator_strength(
        *args,
        **kwargs
    )

    return np.clip(
        f,
        0,
        1
    )


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    from physics.schrodinger import Q

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

    f = oscillator_strength(

        z,

        psi2,

        psi1,

        0.275 * Q,

        0.120 * Q,

        0.043 * M0

    )

    print()

    print("Oscillator Strength")

    print(f)