"""
beer_lambert.py

Beer-Lambert Law equations for
QCL Gas Sensing Module.
"""

import math


# ==========================================================
# Beer-Lambert Law
#
# I = I0 * exp(-αCL)
# ==========================================================

def calculate_beer_lambert(
        incident_intensity,
        absorption_coefficient,
        gas_concentration,
        optical_path_length):
    """
    Calculate transmitted intensity using
    Beer-Lambert Law.

    Parameters
    ----------
    incident_intensity : float
        Incident optical intensity (W/m²)

    absorption_coefficient : float
        Absorption coefficient (m²/mol or cm⁻¹)

    gas_concentration : float
        Gas concentration

    optical_path_length : float
        Optical path length (m)

    Returns
    -------
    float
        Transmitted optical intensity
    """

    if incident_intensity <= 0:
        raise ValueError(
            "Incident intensity must be greater than zero."
        )

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

    return (
        incident_intensity
        * math.exp(
            -absorption_coefficient
            * gas_concentration
            * optical_path_length
        )
    )


# ==========================================================
# Absorbance
#
# A = αCL
# ==========================================================

def calculate_absorbance(
        absorption_coefficient,
        gas_concentration,
        optical_path_length):
    """
    Calculate absorbance.

    Parameters
    ----------
    absorption_coefficient : float

    gas_concentration : float

    optical_path_length : float

    Returns
    -------
    float
        Absorbance
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

    return (
        absorption_coefficient
        * gas_concentration
        * optical_path_length
    )