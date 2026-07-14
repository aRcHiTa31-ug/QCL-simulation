"""
transmission.py

Transmission equations
for the QCL Gas Sensing module.
"""

import math


# ==========================================================
# Optical Transmission
#
#        I
# T = -------
#       I₀
#
# where
# T  = Transmission
# I  = Transmitted intensity
# I₀ = Incident intensity
# ==========================================================

def calculate_transmission(
        incident_intensity,
        transmitted_intensity):
    """
    Calculate optical transmission.
    """

    if incident_intensity <= 0:
        raise ValueError(
            "Incident intensity must be greater than zero."
        )

    if transmitted_intensity < 0:
        raise ValueError(
            "Transmitted intensity cannot be negative."
        )

    if transmitted_intensity > incident_intensity:
        raise ValueError(
            "Transmitted intensity cannot exceed incident intensity."
        )

    return (
        transmitted_intensity /
        incident_intensity
    )


# ==========================================================
# Transmission Percentage
#
# T(%) = T × 100
# ==========================================================

def calculate_transmission_percentage(
        incident_intensity,
        transmitted_intensity):
    """
    Calculate transmission percentage.
    """

    transmission = calculate_transmission(
        incident_intensity,
        transmitted_intensity
    )

    return transmission * 100


# ==========================================================
# Beer-Lambert Transmission
#
# T = exp(-αCL)
#
# where
# α = Absorption coefficient
# C = Gas concentration
# L = Optical path length
# ==========================================================

def calculate_theoretical_transmission(
        absorption_coefficient,
        gas_concentration,
        optical_path_length):
    """
    Calculate theoretical transmission
    using Beer-Lambert law.
    """

    if absorption_coefficient < 0:
        raise ValueError(
            "Absorption coefficient cannot be negative."
        )

    if gas_concentration < 0:
        raise ValueError(
            "Gas concentration cannot be negative."
        )

    if optical_path_length < 0:
        raise ValueError(
            "Optical path length cannot be negative."
        )

    return math.exp(
        -absorption_coefficient
        * gas_concentration
        * optical_path_length
    )