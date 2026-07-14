"""
absorption.py

Optical Absorption equations
for the QCL Gas Sensing module.
"""

import math


# ==========================================================
# Equation 80
# Optical Absorption
#
# α = -(1/L) ln(I/I₀)
#
# where
# α  = Absorption coefficient
# I  = Transmitted intensity
# I₀ = Incident intensity
# L  = Optical path length
# ==========================================================

def calculate_optical_absorption(
        incident_intensity,
        transmitted_intensity,
        optical_path_length):
    """
    Calculate the absorption coefficient.

    Parameters
    ----------
    incident_intensity : float
        Incident optical intensity

    transmitted_intensity : float
        Transmitted optical intensity

    optical_path_length : float
        Optical path length (m)

    Returns
    -------
    float
        Absorption coefficient
    """

    if incident_intensity <= 0:
        raise ValueError(
            "Incident intensity must be greater than zero."
        )

    if transmitted_intensity <= 0:
        raise ValueError(
            "Transmitted intensity must be greater than zero."
        )

    if optical_path_length <= 0:
        raise ValueError(
            "Optical path length must be greater than zero."
        )

    absorption_coefficient = (
        -math.log(
            transmitted_intensity /
            incident_intensity
        ) / optical_path_length
    )

    return absorption_coefficient


# ==========================================================
# Absorbed Optical Power
#
# P_abs = P₀ − P_t
#
# where
# P_abs = Absorbed power
# P₀    = Incident power
# P_t   = Transmitted power
# ==========================================================

def calculate_absorbed_power(
        incident_power,
        transmitted_power):
    """
    Calculate absorbed optical power.
    """

    if incident_power < 0:
        raise ValueError(
            "Incident power cannot be negative."
        )

    if transmitted_power < 0:
        raise ValueError(
            "Transmitted power cannot be negative."
        )

    if transmitted_power > incident_power:
        raise ValueError(
            "Transmitted power cannot exceed incident power."
        )

    return incident_power - transmitted_power