"""
physics/gain.py

Optical Gain Calculations for Quantum Cascade Lasers

Includes:
1. Material Optical Gain
2. Lorentzian Broadening
3. Gain Spectrum
4. Peak Gain
5. Modal Gain
6. Gain Saturation
"""

import numpy as np

PI = np.pi


# ==========================================================
# Existing Equation
# ==========================================================

def calculate_optical_gain(
    sigma,
    upper_population,
    lower_population
):
    """
    Material Optical Gain

    g = σ(Nu - Nl)

    Parameters
    ----------
    sigma : float
        Stimulated emission cross-section

    upper_population : float
        Upper state carrier density

    lower_population : float
        Lower state carrier density

    Returns
    -------
    float
        Material optical gain
    """

    return sigma * (
        upper_population - lower_population
    )


# ==========================================================
# Lorentzian Broadening
# ==========================================================

def lorentzian_broadening(
    photon_energy,
    transition_energy,
    linewidth
):
    """
    Lorentzian Line Shape

    L(E) = (γ / 2π)
           -------------------------
           (E-E0)^2 + (γ/2)^2
    """

    gamma = linewidth

    numerator = gamma / (2 * PI)

    denominator = (
        (photon_energy - transition_energy) ** 2
        +
        (gamma / 2) ** 2
    )

    return numerator / denominator


# ==========================================================
# Gain Spectrum
# ==========================================================

def gain_spectrum(
    photon_energy,
    material_gain,
    transition_energy,
    linewidth
):
    """
    Optical Gain Spectrum
    """

    return (
        material_gain
        *
        lorentzian_broadening(
            photon_energy,
            transition_energy,
            linewidth
        )
    )


# ==========================================================
# Peak Gain
# ==========================================================

def peak_gain(
    spectrum
):
    """
    Maximum value of gain spectrum.
    """

    return np.max(spectrum)


# ==========================================================
# Modal Gain
# ==========================================================

def modal_gain(
    confinement_factor,
    material_gain
):
    """
    Modal Gain

    G = Γ g
    """

    return (
        confinement_factor
        * material_gain
    )


# ==========================================================
# Gain Saturation
# ==========================================================

def gain_saturation(
    small_signal_gain,
    optical_power,
    saturation_power
):
    """
    Gain Saturation

    g = g0 / (1 + P/Psat)
    """

    return (
        small_signal_gain
        /
        (
            1
            +
            optical_power
            / saturation_power
        )
    )


# ==========================================================
# Example
# ==========================================================

if __name__ == "__main__":

    Q = 1.602176634e-19

    photon_energy = np.linspace(
        0.20,
        0.35,
        1000
    ) * Q

    material_gain = calculate_optical_gain(
        sigma=2e-16,
        upper_population=5e22,
        lower_population=2e22
    )

    spectrum = gain_spectrum(
        photon_energy,
        material_gain,
        transition_energy=0.275 * Q,
        linewidth=0.008 * Q
    )

    print("Material Gain :", material_gain)

    print("Peak Gain :", peak_gain(spectrum))

    print("Modal Gain :", modal_gain(0.35, material_gain))

    print(
        "Saturated Gain :",
        gain_saturation(
            material_gain,
            optical_power=5,
            saturation_power=10
        )
    )