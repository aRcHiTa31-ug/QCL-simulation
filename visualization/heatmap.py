"""
heatmap.py
2D Parameter Sweep Heatmaps
for the Quantum Cascade Laser Simulator.
"""
import numpy as np
import matplotlib.pyplot as plt
from physics_engine.physics_engine import PhysicsEngine
# ==========================================================
# Output Power vs Current & Temperature
# ==========================================================
def plot_output_power_heatmap(
        slope_efficiency,
        threshold_current_reference,
        reference_temperature,
        characteristic_temperature,
        current_max,
        temperature_max,
        points=100):
    """
    Output Power Heatmap over Current and Temperature.

    At each temperature, the threshold current is first
    computed via calculate_threshold_current_temperature,
    then output power is computed via calculate_output_power
    using that temperature-shifted threshold.
    """
    current = np.linspace(
        1e-6,
        current_max,
        points
    )
    temperature = np.linspace(
        reference_temperature,
        temperature_max,
        points
    )
    power_grid = np.zeros((points, points))
    for t_idx, t in enumerate(temperature):
        threshold_current = PhysicsEngine.calculate_threshold_current_temperature(
            threshold_current_reference=threshold_current_reference,
            operating_temperature=t,
            reference_temperature=reference_temperature,
            characteristic_temperature=characteristic_temperature
        )
        for c_idx, i in enumerate(current):
            power_grid[t_idx, c_idx] = PhysicsEngine.calculate_output_power(
                slope_efficiency=slope_efficiency,
                current=i,
                threshold_current=threshold_current
            )
    fig, ax = plt.subplots(figsize=(8, 6))
    mesh = ax.pcolormesh(
        current,
        temperature,
        power_grid,
        shading="auto",
        cmap="inferno"
    )
    fig.colorbar(mesh, ax=ax, label="Output Power (W)")
    ax.set_title("Output Power Heatmap")
    ax.set_xlabel("Operating Current (A)")
    ax.set_ylabel("Temperature (K)")
    ax.set_aspect("auto")
    fig.tight_layout()
    return fig
# ==========================================================
# Wall-Plug Efficiency vs Current & Voltage
# ==========================================================
def plot_wallplug_efficiency_heatmap(
        slope_efficiency,
        threshold_current,
        current_max,
        voltage_max,
        points=100):
    """
    Wall-Plug Efficiency Heatmap over Current and Voltage.
    """
    current = np.linspace(
        current_max / points,
        current_max,
        points
    )
    voltage = np.linspace(
        voltage_max / points,
        voltage_max,
        points
    )
    efficiency_grid = np.zeros((points, points))
    for v_idx, v in enumerate(voltage):
        for c_idx, i in enumerate(current):
            output_power = PhysicsEngine.calculate_output_power(
                slope_efficiency=slope_efficiency,
                current=i,
                threshold_current=threshold_current
            )
            efficiency_grid[v_idx, c_idx] = PhysicsEngine.calculate_wallplug_efficiency(
                output_power=output_power,
                voltage=v,
                current=i
            )
    fig, ax = plt.subplots(figsize=(8, 6))
    mesh = ax.pcolormesh(
        current,
        voltage,
        efficiency_grid,
        shading="auto",
        cmap="viridis"
    )
    fig.colorbar(mesh, ax=ax, label="Wall-Plug Efficiency")
    ax.set_title("Wall-Plug Efficiency Heatmap")
    ax.set_xlabel("Operating Current (A)")
    ax.set_ylabel("Voltage (V)")
    ax.set_aspect("auto")
    fig.tight_layout()
    return fig
# ==========================================================
# Peak Output Power Indicator
# ==========================================================
def calculate_peak_output_power(
        slope_efficiency,
        threshold_current_reference,
        reference_temperature,
        characteristic_temperature,
        current_max,
        temperature_max,
        points=100):
    """
    Returns the peak output power across the swept
    Current x Temperature grid.
    """
    current = np.linspace(
        0,
        current_max,
        points
    )
    temperature = np.linspace(
        reference_temperature,
        temperature_max,
        points
    )
    power_grid = np.zeros((points, points))
    for t_idx, t in enumerate(temperature):
        threshold_current = PhysicsEngine.calculate_threshold_current_temperature(
            threshold_current_reference=threshold_current_reference,
            operating_temperature=t,
            reference_temperature=reference_temperature,
            characteristic_temperature=characteristic_temperature
        )
        for c_idx, i in enumerate(current):
            power_grid[t_idx, c_idx] = PhysicsEngine.calculate_output_power(
                slope_efficiency=slope_efficiency,
                current=i,
                threshold_current=threshold_current
            )
    return np.max(power_grid)