"""
power_graph.py
Visualization of Output Power
for the Quantum Cascade Laser Simulator.
"""
import numpy as np
import matplotlib.pyplot as plt
from physics_engine.physics_engine import PhysicsEngine
# ==========================================================
# Output Power vs Operating Current
# ==========================================================
def plot_output_power(
        slope_efficiency,
        current_max,
        threshold_current,
        points=200):
    """
    Output Optical Power vs Operating Current.
    """
    current = np.linspace(
        0,
        current_max,
        points
    )
    power = [
        PhysicsEngine.calculate_output_power(
            slope_efficiency=slope_efficiency,
            current=i,
            threshold_current=threshold_current
        )
        for i in current
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        current,
        power,
        linewidth=2.5,
        color="royalblue"
    )
    ax.set_title("Output Optical Power")
    ax.set_xlabel("Operating Current (A)")
    ax.set_ylabel("Output Power (W)")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Dissipated Power vs Operating Current
# ==========================================================
def plot_dissipated_power(
        slope_efficiency,
        threshold_current,
        voltage,
        current_max,
        points=200):
    """
    Dissipated Power vs Operating Current.
    """
    current = np.linspace(
        0,
        current_max,
        points
    )
    dissipated = [
        PhysicsEngine.calculate_dissipated_power(
            voltage=voltage,
            current=i,
            output_power=PhysicsEngine.calculate_output_power(
                slope_efficiency=slope_efficiency,
                current=i,
                threshold_current=threshold_current
            )
        )
        for i in current
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        current,
        dissipated,
        linewidth=2,
        color="darkorange"
    )
    ax.set_title("Dissipated Power")
    ax.set_xlabel("Operating Current (A)")
    ax.set_ylabel("Dissipated Power (W)")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Power Density vs Emitting Area
# ==========================================================
def plot_power_density(
        output_power,
        area_max,
        points=100):
    """
    Power Density vs Emitting Area.
    """
    area = np.linspace(
        1e-12,
        area_max,
        points
    )
    density = [
        PhysicsEngine.calculate_power_density(
            output_power=output_power,
            emitting_area=a
        )
        for a in area
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        area,
        density,
        linewidth=2,
        color="darkgreen"
    )
    ax.set_title("Power Density")
    ax.set_xlabel("Emitting Area (m²)")
    ax.set_ylabel("Power Density (W/m²)")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Peak Power Density Indicator
# ==========================================================
def calculate_peak_power_density(
        output_power,
        area_max,
        points=100):
    """
    Returns the peak value of the power density curve.
    """
    area = np.linspace(
        0,
        area_max,
        points
    )
    density = [
        PhysicsEngine.calculate_power_density(
            output_power=output_power,
            emitting_area=a
        )
        for a in area
    ]
    return np.max(density)