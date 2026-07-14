"""
optical_intensity.py

Optical Intensity equations
for the QCL Gas Sensing module.
"""

# ==========================================================
# Optical Intensity
#
#        P
# I = -------
#        A
#
# where
# I = Optical intensity (W/m²)
# P = Optical power (W)
# A = Beam area (m²)
# ==========================================================

def calculate_optical_intensity(
        optical_power,
        beam_area):
    """
    Calculate optical intensity.

    Parameters
    ----------
    optical_power : float
        Optical power (W)

    beam_area : float
        Beam area (m²)

    Returns
    -------
    float
        Optical intensity (W/m²)
    """

    if optical_power < 0:
        raise ValueError(
            "Optical power cannot be negative."
        )

    if beam_area <= 0:
        raise ValueError(
            "Beam area must be greater than zero."
        )

    return optical_power / beam_area


# ==========================================================
# Incident Optical Intensity
#
#        P₀
# I₀ = ------
#        A
# ==========================================================

def calculate_incident_intensity(
        incident_power,
        beam_area):
    """
    Calculate incident optical intensity.
    """

    if incident_power < 0:
        raise ValueError(
            "Incident power cannot be negative."
        )

    if beam_area <= 0:
        raise ValueError(
            "Beam area must be greater than zero."
        )

    return incident_power / beam_area


# ==========================================================
# Transmitted Optical Intensity
#
#        Pₜ
# Iₜ = ------
#        A
# ==========================================================

def calculate_transmitted_intensity(
        transmitted_power,
        beam_area):
    """
    Calculate transmitted optical intensity.
    """

    if transmitted_power < 0:
        raise ValueError(
            "Transmitted power cannot be negative."
        )

    if beam_area <= 0:
        raise ValueError(
            "Beam area must be greater than zero."
        )

    return transmitted_power / beam_area