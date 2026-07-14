"""
performance.py

Performance metrics for Quantum Cascade Laser (QCL)
"""

import math


def calculate_brightness(output_power, beam_area, solid_angle):
    """
    Brightness (W/m²/sr)
    """
    if beam_area <= 0 or solid_angle <= 0:
        return 0.0
    return output_power / (beam_area * solid_angle)


def calculate_beam_divergence(wavelength, aperture_width):
    """
    Beam Divergence (radians)
    θ ≈ λ / D
    """
    if aperture_width <= 0:
        return 0.0
    return wavelength / aperture_width


def calculate_power_density(output_power, emitting_area):
    """
    Power Density (W/m²)
    """
    if emitting_area <= 0:
        return 0.0
    return output_power / emitting_area


def calculate_spectral_linewidth(center_wavelength, quality_factor):
    """
    Spectral Linewidth (m)
    Δλ = λ / Q
    """
    if quality_factor <= 0:
        return 0.0
    return center_wavelength / quality_factor


def calculate_characteristic_temperature(I1, I2, T1, T2):
    """
    Characteristic Temperature T0 (K)
    """
    if I1 <= 0 or I2 <= 0 or T1 == T2:
        return 0.0

    denominator = math.log(I2 / I1)

    if denominator == 0:
        return 0.0

    return (T2 - T1) / denominator


def calculate_voltage_defect(photon_energy, electron_charge, voltage):
    """
    Voltage Defect
    """
    if voltage <= 0:
        return 0.0
    return 1 - photon_energy / (electron_charge * voltage)


def calculate_optical_frequency(speed_of_light, wavelength):
    """
    Optical Frequency (Hz)
    """
    if wavelength <= 0:
        return 0.0
    return speed_of_light / wavelength


def calculate_cascade_voltage(number_of_cascades, stage_voltage):
    """
    Cascade Voltage (V)
    """
    return number_of_cascades * stage_voltage


def calculate_active_region_thickness(number_of_cascades, stage_length):
    """
    Active Region Thickness (m)
    """
    return number_of_cascades * stage_length


def calculate_figure_of_merit(output_power, threshold_current, linewidth):
    """
    Overall Device Figure of Merit
    """
    if threshold_current <= 0 or linewidth <= 0:
        return 0.0

    return output_power / (threshold_current * linewidth)