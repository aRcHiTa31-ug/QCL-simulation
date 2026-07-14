"""
thermal_graph.py

Visualization of Thermal Characteristics
for the Quantum Cascade Laser Simulator.
"""

import numpy as np
import matplotlib.pyplot as plt

from physics_engine.physics_engine import PhysicsEngine


# ==========================================================
# Temperature Rise vs Dissipated Power
# ==========================================================

def plot_temperature_rise(
        thermal_resistance,
        max_dissipated_power,
        points=200):
    """
    Temperature Rise vs Dissipated Power.
    """

    dissipated_power = np.linspace(
        0,
        max_dissipated_power,
        points
    )

    temperature_rise = [
        PhysicsEngine.calculate_temperature_rise(
            thermal_resistance=thermal_resistance,
            dissipated_power=p
        )
        for p in dissipated_power
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        dissipated_power,
        temperature_rise,
        linewidth=2.5,
        color="royalblue",
        label="Temperature Rise"
    )

    ax.set_title("Temperature Rise vs Dissipated Power")

    ax.set_xlabel("Dissipated Power (W)")

    ax.set_ylabel("Temperature Rise (K)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Device Temperature vs Dissipated Power
# ==========================================================

def plot_device_temperature(
        ambient_temperature,
        thermal_resistance,
        max_dissipated_power,
        points=200):
    """
    Device Temperature vs Dissipated Power.
    """

    dissipated_power = np.linspace(
        0,
        max_dissipated_power,
        points
    )

    device_temperature = []

    for p in dissipated_power:

        delta_t = PhysicsEngine.calculate_temperature_rise(
            thermal_resistance=thermal_resistance,
            dissipated_power=p
        )

        device_temperature.append(
            PhysicsEngine.calculate_device_temperature(
                ambient_temperature=ambient_temperature,
                temperature_rise=delta_t
            )
        )

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        dissipated_power,
        device_temperature,
        linewidth=2,
        color="crimson",
        label="Device Temperature"
    )

    ax.set_title("Device Temperature")

    ax.set_xlabel("Dissipated Power (W)")

    ax.set_ylabel("Temperature (K)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Threshold Current vs Temperature
# ==========================================================

def plot_threshold_current_temperature(
        threshold_current_reference,
        reference_temperature,
        characteristic_temperature,
        max_temperature,
        points=200):
    """
    Threshold Current vs Temperature.
    """

    temperature = np.linspace(
        reference_temperature,
        max_temperature,
        points
    )

    threshold_current = [
        PhysicsEngine.calculate_threshold_current_temperature(
            threshold_current_reference=threshold_current_reference,
            operating_temperature=t,
            reference_temperature=reference_temperature,
            characteristic_temperature=characteristic_temperature
        )
        for t in temperature
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        temperature,
        threshold_current,
        linewidth=2,
        color="darkgreen",
        label="Threshold Current"
    )

    ax.set_title("Threshold Current vs Temperature")

    ax.set_xlabel("Temperature (K)")

    ax.set_ylabel("Threshold Current (A)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Thermal Conductivity vs Temperature Difference
# ==========================================================

def plot_thermal_conductivity(
        heat_flux,
        thickness,
        max_temperature_difference,
        points=200):
    """
    Thermal Conductivity vs Temperature Difference.
    """

    temperature_difference = np.linspace(
        1,
        max_temperature_difference,
        points
    )

    conductivity = [
        PhysicsEngine.calculate_thermal_conductivity(
            heat_flux=heat_flux,
            thickness=thickness,
            temperature_difference=d
        )
        for d in temperature_difference
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        temperature_difference,
        conductivity,
        linewidth=2,
        color="darkorange",
        label="Thermal Conductivity"
    )

    ax.set_title("Thermal Conductivity")

    ax.set_xlabel("Temperature Difference (K)")

    ax.set_ylabel("Thermal Conductivity (W/m·K)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Peak Device Temperature Indicator
# ==========================================================

def calculate_peak_device_temperature(
        ambient_temperature,
        thermal_resistance,
        max_dissipated_power,
        points=200):
    """
    Returns the peak device temperature.
    """

    dissipated_power = np.linspace(
        0,
        max_dissipated_power,
        points
    )

    temperature = []

    for p in dissipated_power:

        delta_t = PhysicsEngine.calculate_temperature_rise(
            thermal_resistance=thermal_resistance,
            dissipated_power=p
        )

        temperature.append(
            PhysicsEngine.calculate_device_temperature(
                ambient_temperature=ambient_temperature,
                temperature_rise=delta_t
            )
        )

    return np.max(temperature)