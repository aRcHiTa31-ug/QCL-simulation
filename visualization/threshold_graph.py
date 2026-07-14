"""
threshold_graph.py

Visualization of Threshold Characteristics
for the Quantum Cascade Laser Simulator.
"""

import numpy as np
import matplotlib.pyplot as plt

from physics_engine.physics_engine import PhysicsEngine


# ==========================================================
# Threshold Gain vs Mirror Loss
# ==========================================================

def plot_threshold_gain(
        internal_loss,
        mirror_loss_max,
        points=200):
    """
    Threshold Gain vs Mirror Loss.
    """

    mirror_loss = np.linspace(
        0,
        mirror_loss_max,
        points
    )

    threshold_gain = [
        PhysicsEngine.calculate_threshold_gain(
            internal_loss=internal_loss,
            mirror_loss=m
        )
        for m in mirror_loss
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        mirror_loss,
        threshold_gain,
        linewidth=2.5,
        color="royalblue",
        label="Threshold Gain"
    )

    ax.set_title("Threshold Gain vs Mirror Loss")

    ax.set_xlabel("Mirror Loss (cm⁻¹)")

    ax.set_ylabel("Threshold Gain (cm⁻¹)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Threshold Current Density vs Active Area
# ==========================================================

def plot_threshold_current_density(
        threshold_current,
        area_max,
        points=200):
    """
    Threshold Current Density vs Active Area.
    """

    area = np.linspace(
        area_max / points,
        area_max,
        points
    )

    current_density = [
        PhysicsEngine.calculate_threshold_current_density(
            threshold_current=threshold_current,
            area=a
        )
        for a in area
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        area,
        current_density,
        linewidth=2,
        color="crimson",
        label="Threshold Current Density"
    )

    ax.set_title("Threshold Current Density vs Active Area")

    ax.set_xlabel("Active Area (m²)")

    ax.set_ylabel("Current Density (A/m²)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Peak Threshold Gain Indicator
# ==========================================================

def calculate_peak_threshold_gain(
        internal_loss,
        mirror_loss_max,
        points=200):
    """
    Returns maximum threshold gain.
    """

    mirror_loss = np.linspace(
        0,
        mirror_loss_max,
        points
    )

    threshold_gain = [
        PhysicsEngine.calculate_threshold_gain(
            internal_loss=internal_loss,
            mirror_loss=m
        )
        for m in mirror_loss
    ]

    return np.max(threshold_gain)


# ==========================================================
# Peak Threshold Current Density Indicator
# ==========================================================

def calculate_peak_threshold_current_density(
        threshold_current,
        area_max,
        points=200):
    """
    Returns maximum threshold current density.
    """

    area = np.linspace(
        area_max / points,
        area_max,
        points
    )

    current_density = [
        PhysicsEngine.calculate_threshold_current_density(
            threshold_current=threshold_current,
            area=a
        )
        for a in area
    ]

    return np.max(current_density)