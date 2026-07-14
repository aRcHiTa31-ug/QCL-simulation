"""
physics/intersubband_transition.py

Intersubband Transition Calculations
for Quantum Cascade Lasers

Implements

1. Transition Energy
2. Transition Frequency
3. Transition Wavelength
4. Energy Difference
"""

import numpy as np

# -------------------------------------------------------
# Physical Constants
# -------------------------------------------------------

Q = 1.602176634e-19         # Coulomb
H = 6.62607015e-34          # J.s
C = 299792458               # m/s


def transition_energy(
    upper_energy,
    lower_energy
):
    """
    Transition Energy

        ΔE = Eu - El

    Parameters
    ----------
    upper_energy : float
        Upper state energy (J)

    lower_energy : float
        Lower state energy (J)

    Returns
    -------
    float
        Transition Energy (J)
    """

    return upper_energy - lower_energy


def transition_energy_ev(
    upper_energy,
    lower_energy
):
    """
    Transition Energy (eV)
    """

    return (
        transition_energy(
            upper_energy,
            lower_energy
        )
        / Q
    )


def transition_frequency(
    upper_energy,
    lower_energy
):
    """
    Transition Frequency

        f = ΔE / h
    """

    delta_e = transition_energy(
        upper_energy,
        lower_energy
    )

    return delta_e / H


def transition_wavelength(
    upper_energy,
    lower_energy
):
    """
    Transition Wavelength

        λ = hc / ΔE
    """

    delta_e = transition_energy(
        upper_energy,
        lower_energy
    )

    return (H * C) / delta_e


def transition_wavenumber(
    upper_energy,
    lower_energy
):
    """
    Transition Wavenumber

    Returns
    -------
    float
        cm^-1
    """

    wavelength = transition_wavelength(
        upper_energy,
        lower_energy
    )

    return 1 / (wavelength * 100)


# -------------------------------------------------------
# Example
# -------------------------------------------------------

if __name__ == "__main__":

    upper = 0.275 * Q

    lower = 0.120 * Q

    print()

    print(
        "Transition Energy (eV):",
        transition_energy_ev(
            upper,
            lower
        )
    )

    print()

    print(
        "Frequency (Hz):",
        transition_frequency(
            upper,
            lower
        )
    )

    print()

    print(
        "Wavelength (µm):",
        transition_wavelength(
            upper,
            lower
        ) * 1e6
    )

    print()

    print(
        "Wavenumber (cm⁻¹):",
        transition_wavenumber(
            upper,
            lower
        )
    )