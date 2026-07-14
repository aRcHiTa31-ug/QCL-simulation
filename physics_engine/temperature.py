"""
temperature.py

Contains equations related to thermal analysis
of Quantum Cascade Lasers (QCL).
"""

import math


# ==========================================================
# Thermal Resistance
# R_th = ΔT / P_diss
# ==========================================================

def calculate_thermal_resistance(
        temperature_rise,
        dissipated_power):
    """
    Calculate Thermal Resistance.

    Parameters:
        temperature_rise (float): Temperature Rise (K)
        dissipated_power (float): Dissipated Power (W)

    Returns:
        float: Thermal Resistance (K/W)
    """

    if dissipated_power <= 0:
        raise ValueError(
            "Dissipated Power must be greater than zero."
        )

    return temperature_rise / dissipated_power


# ==========================================================
# Temperature Rise
# ΔT = R_th × P_diss
# ==========================================================

def calculate_temperature_rise(
        thermal_resistance,
        dissipated_power):
    """
    Calculate Temperature Rise.

    Parameters:
        thermal_resistance (float): Thermal Resistance (K/W)
        dissipated_power (float): Dissipated Power (W)

    Returns:
        float: Temperature Rise (K)
    """

    if thermal_resistance < 0:
        raise ValueError(
            "Thermal Resistance cannot be negative."
        )

    return thermal_resistance * dissipated_power


# ==========================================================
# Dissipated Power
# P_diss = V × I − P_out
# ==========================================================

def calculate_dissipated_power(
        voltage,
        current,
        output_power):
    """
    Calculate Dissipated Power.

    Parameters:
        voltage (float): Applied Voltage (V)
        current (float): Operating Current (A)
        output_power (float): Optical Output Power (W)

    Returns:
        float: Dissipated Power (W)
    """

    return (voltage * current) - output_power


# ==========================================================
# Device Temperature
# T_device = T_ambient + ΔT
# ==========================================================

def calculate_device_temperature(
        ambient_temperature,
        temperature_rise):
    """
    Calculate Device Temperature.

    Parameters:
        ambient_temperature (float): Ambient Temperature (K)
        temperature_rise (float): Temperature Rise (K)

    Returns:
        float: Device Temperature (K)
    """

    return ambient_temperature + temperature_rise


# ==========================================================
# Thermal Conductivity
# k = (q × L) / ΔT
# ==========================================================

def calculate_thermal_conductivity(
        heat_flux,
        thickness,
        temperature_difference):
    """
    Calculate Thermal Conductivity.

    Parameters:
        heat_flux (float): Heat Flux (W/m²)
        thickness (float): Material Thickness (m)
        temperature_difference (float): Temperature Difference (K)

    Returns:
        float: Thermal Conductivity (W/mK)
    """

    if temperature_difference == 0:
        raise ValueError(
            "Temperature difference cannot be zero."
        )

    return (heat_flux * thickness) / temperature_difference


# ==========================================================
# Self Heating
# ΔT = T_device − T_ambient
# ==========================================================

def calculate_self_heating(
        device_temperature,
        ambient_temperature):
    """
    Calculate Self Heating.

    Parameters:
        device_temperature (float): Device Temperature (K)
        ambient_temperature (float): Ambient Temperature (K)

    Returns:
        float: Self Heating (K)
    """

    return device_temperature - ambient_temperature


# ==========================================================
# Threshold Current vs Temperature
# Ith(T)=Ith_ref*exp((T-Tref)/T0)
# ==========================================================

def calculate_threshold_current_temperature(
        threshold_current_reference,
        operating_temperature,
        reference_temperature,
        characteristic_temperature):
    """
    Calculate Threshold Current at a given temperature.

    Parameters:
        threshold_current_reference (float): Threshold Current at Tref (A)
        operating_temperature (float): Operating Temperature (K)
        reference_temperature (float): Reference Temperature (K)
        characteristic_temperature (float): Characteristic Temperature T0 (K)

    Returns:
        float: Threshold Current (A)
    """

    if characteristic_temperature <= 0:
        raise ValueError(
            "Characteristic temperature must be greater than zero."
        )

    exponent = (
        (operating_temperature - reference_temperature)
        / characteristic_temperature
    )

    return threshold_current_reference * math.exp(exponent)


# ==========================================================
# Wall-Plug Efficiency
# η = Pout / Pin
# ==========================================================

def calculate_wallplug_efficiency(
        output_power,
        voltage,
        current):
    """
    Calculate Wall-Plug Efficiency.

    Parameters:
        output_power (float): Optical Output Power (W)
        voltage (float): Voltage (V)
        current (float): Current (A)

    Returns:
        float: Wall-Plug Efficiency
    """

    electrical_power = voltage * current

    if electrical_power <= 0:
        raise ValueError(
            "Electrical power must be greater than zero."
        )

    return output_power / electrical_power