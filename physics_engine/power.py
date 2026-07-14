"""
power.py

Contains equations related to Output Power.
"""


def calculate_output_power(slope_efficiency, current, threshold_current):
    """
    Calculate Output Optical Power.

    Parameters:
        slope_efficiency (float): Slope Efficiency (W/A)
        current (float): Operating Current (A)
        threshold_current (float): Threshold Current (A)

    Returns:
        float: Output Power (W)
    """

    if current <= threshold_current:
        return 0.0

    return slope_efficiency * (current - threshold_current)

def calculate_dissipated_power(voltage, current, output_power):
    """
    Calculate Dissipated Power.

    Parameters:
        voltage (float): Applied Voltage (V)
        current (float): Operating Current (A)
        output_power (float): Output Optical Power (W)

    Returns:
        float: Dissipated Power (W)
    """

    return (voltage * current) - output_power


def calculate_slope_efficiency(delta_power, delta_current):
    """
    Slope Efficiency (W/A)
    """
    if delta_current == 0:
        return 0.0
    return delta_power / delta_current

def calculate_power_density(output_power, area):
    """
    Power Density (W/m²)
    """
    if area == 0:
        return 0.0
    return output_power / area

def calculate_brightness(output_power, beam_area, solid_angle):
    """
    Brightness
    """
    if beam_area == 0 or solid_angle == 0:
        return 0.0
    return output_power / (beam_area * solid_angle)

def calculate_voltage_defect(photon_energy, electron_charge, voltage):
    """
    Voltage Defect
    """
    if voltage == 0:
        return 0.0
    return 1 - (photon_energy / (electron_charge * voltage))

def calculate_cascade_voltage(stages, transition_energy, electron_charge):
    """
    Cascade Voltage
    """
    return (stages * transition_energy) / electron_charge