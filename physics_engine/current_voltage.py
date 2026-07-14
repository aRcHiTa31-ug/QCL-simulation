"""
current_voltage.py

Contains equations related to:
1. Current Density
2. Electric Field (to be added later)
"""


def calculate_current_density(current, area):
    """
    Calculate Current Density.

    Parameters:
        current (float): Current in Amperes (A)
        area (float): Cross-sectional Area in square meters (m²)

    Returns:
        float: Current Density in A/m²
    """

    if area <= 0:
        raise ValueError("Area must be greater than zero.")

    return current / area

def calculate_electric_field(voltage, distance):
    """
    Calculate Electric Field.

    Parameters:
        voltage (float): Applied Voltage in Volts (V)
        distance (float): Active Region Thickness in meters (m)

    Returns:
        float: Electric Field in V/m
    """

    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")

    return voltage / distance