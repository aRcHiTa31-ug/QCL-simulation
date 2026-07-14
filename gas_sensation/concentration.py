"""
concentration.py

Gas concentration calculations
for the QCL Gas Sensing module.
"""

import math


# ==========================================================
# Gas Concentration
#
#            -ln(I / I₀)
# C = -----------------------------
#      α × L
#
# where
# C  = Gas concentration
# α  = Absorption coefficient
# L  = Optical path length
# I₀ = Incident intensity
# I  = Transmitted intensity
# ==========================================================

def calculate_gas_concentration(
        incident_intensity,
        transmitted_intensity,
        absorption_coefficient,
        optical_path_length):
    """
    Calculate gas concentration using the
    Beer-Lambert Law.

    Parameters
    ----------
    incident_intensity : float
        Incident optical intensity

    transmitted_intensity : float
        Transmitted optical intensity

    absorption_coefficient : float
        Absorption coefficient

    optical_path_length : float
        Optical path length (m)

    Returns
    -------
    float
        Gas concentration
    """

    if incident_intensity <= 0:
        raise ValueError(
            "Incident intensity must be greater than zero."
        )

    if transmitted_intensity <= 0:
        raise ValueError(
            "Transmitted intensity must be greater than zero."
        )

    if absorption_coefficient <= 0:
        raise ValueError(
            "Absorption coefficient must be greater than zero."
        )

    if optical_path_length <= 0:
        raise ValueError(
            "Optical path length must be greater than zero."
        )

    concentration = (
        -math.log(
            transmitted_intensity /
            incident_intensity
        )
        /
        (
            absorption_coefficient *
            optical_path_length
        )
    )

    return concentration


# ==========================================================
# Concentration in ppm
#
# ppm = C × 10⁶
# ==========================================================

def concentration_to_ppm(concentration):
    """
    Convert concentration to ppm.
    """

    if concentration < 0:
        raise ValueError(
            "Concentration cannot be negative."
        )

    return concentration * 1e6


# ==========================================================
# Concentration in %
#
# % = C × 100
# ==========================================================

def concentration_to_percent(concentration):
    """
    Convert concentration to percentage.
    """

    if concentration < 0:
        raise ValueError(
            "Concentration cannot be negative."
        )

    return concentration * 100