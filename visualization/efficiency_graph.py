"""
efficiency_graph.py
Visualization of Efficiency Metrics
for the Quantum Cascade Laser Simulator.
"""
import numpy as np
import matplotlib.pyplot as plt
from physics_engine.physics_engine import PhysicsEngine
# ==========================================================
# Wall-Plug Efficiency vs Operating Current
# ==========================================================
def plot_wallplug_efficiency(
        output_power,
        voltage,
        current_max,
        points=200):
    """
    Wall-Plug Efficiency vs Operating Current.
    """
    current = np.linspace(
        current_max / points,
        current_max,
        points
    )
    efficiency = [
        PhysicsEngine.calculate_wallplug_efficiency(
            output_power=output_power,
            voltage=voltage,
            current=i
        )
        for i in current
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        current,
        efficiency,
        linewidth=2.5,
        color="royalblue"
    )
    ax.legend()
    ax.set_title("Wall-Plug Efficiency")
    ax.set_xlabel("Operating Current (A)")
    ax.set_ylabel("Wall-Plug Efficiency")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Internal Quantum Efficiency vs Modal Gain
# ==========================================================
def plot_internal_quantum_efficiency(
        modal_gain_max,
        internal_loss,
        points=200):
    """
    Internal Quantum Efficiency vs Modal Gain.
    """
    modal_gain = np.linspace(
        1e-6,
        modal_gain_max,
        points
    )
    efficiency = [
        PhysicsEngine.calculate_internal_quantum_efficiency(
            modal_gain=g,
            internal_loss=internal_loss
        )
        for g in modal_gain
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        modal_gain,
        efficiency,
        linewidth=2,
        color="darkgreen"
    )
    ax.legend()
    ax.set_title("Internal Quantum Efficiency")
    ax.set_xlabel("Modal Gain")
    ax.set_ylabel("Internal Quantum Efficiency")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# External Quantum Efficiency vs Mirror Loss
# ==========================================================
def plot_external_quantum_efficiency(
        mirror_loss_max,
        internal_loss,
        points=200):
    """
    External Quantum Efficiency vs Mirror Loss.
    """
    mirror_loss = np.linspace(
        1e-6,
        mirror_loss_max,
        points
    )
    efficiency = [
        PhysicsEngine.calculate_external_quantum_efficiency(
            mirror_loss=m,
            internal_loss=internal_loss
        )
        for m in mirror_loss
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        mirror_loss,
        efficiency,
        linewidth=2,
        color="crimson"
    )
    ax.legend()
    ax.set_title("External Quantum Efficiency")
    ax.set_xlabel("Mirror Loss")
    ax.set_ylabel("External Quantum Efficiency")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Peak Wall-Plug Efficiency Indicator
# ==========================================================
def calculate_peak_wallplug_efficiency(
        output_power,
        voltage,
        current_max,
        points=200):
    """
    Returns the peak value of the wall-plug efficiency curve.
    """
    current = np.linspace(
        current_max / points,
        current_max,
        points
    )
    efficiency = [
        PhysicsEngine.calculate_wallplug_efficiency(
            output_power=output_power,
            voltage=voltage,
            current=i
        )
        for i in current
    ]
    return np.max(efficiency)