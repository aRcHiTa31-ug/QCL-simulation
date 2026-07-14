"""
threshold.py

Contains equations related to Threshold Gain and
Threshold Current Density.
"""


def calculate_threshold_gain(internal_loss, mirror_loss):
    """
    Calculate Threshold Gain.

    Parameters:
        internal_loss (float): Internal Loss (αi)
        mirror_loss (float): Mirror Loss (αm)

    Returns:
        float: Threshold Gain
    """

    return internal_loss + mirror_loss

def calculate_threshold_current_density(threshold_current, area):
    """
    Calculate Threshold Current Density.

    Parameters:
        threshold_current (float): Threshold Current (A)
        area (float): Active Area (m²)

    Returns:
        float: Threshold Current Density (A/m²)
    """

    if area <= 0:
        raise ValueError("Area must be greater than zero.")

    return threshold_current / area