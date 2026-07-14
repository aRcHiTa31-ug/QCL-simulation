"""
wavelength_graph.py

Visualization of Wavelength Characteristics
for the Quantum Cascade Laser Simulator.
"""

import numpy as np
import matplotlib.pyplot as plt

from physics_engine.physics_engine import PhysicsEngine


# ==========================================================
# Wavelength vs Transition Energy
# ==========================================================

def plot_wavelength(
        transition_energy_min,
        transition_energy_max,
        points=200):
    """
    Wavelength vs Transition Energy.
    """

    transition_energy = np.linspace(
        transition_energy_min,
        transition_energy_max,
        points
    )

    wavelength = [
        PhysicsEngine.calculate_wavelength(
            transition_energy=e
        )
        for e in transition_energy
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        transition_energy,
        wavelength,
        linewidth=2.5,
        color="royalblue",
        label="Wavelength"
    )

    ax.set_title("Wavelength vs Transition Energy")

    ax.set_xlabel("Transition Energy (J)")

    ax.set_ylabel("Wavelength (m)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Frequency vs Wavelength
# ==========================================================

def plot_frequency(
        wavelength_min,
        wavelength_max,
        points=200):
    """
    Frequency vs Wavelength.
    """

    wavelength = np.linspace(
        wavelength_min,
        wavelength_max,
        points
    )

    frequency = [
        PhysicsEngine.calculate_frequency(
            wavelength=w
        )
        for w in wavelength
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        wavelength,
        frequency,
        linewidth=2,
        color="crimson",
        label="Frequency"
    )

    ax.set_title("Frequency vs Wavelength")

    ax.set_xlabel("Wavelength (m)")

    ax.set_ylabel("Frequency (Hz)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Wavenumber vs Wavelength
# ==========================================================

def plot_wavenumber(
        wavelength_min,
        wavelength_max,
        points=200):
    """
    Wavenumber vs Wavelength.
    """

    wavelength = np.linspace(
        wavelength_min,
        wavelength_max,
        points
    )

    wavenumber = [
        PhysicsEngine.calculate_wavenumber(
            wavelength=w
        )
        for w in wavelength
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        wavelength,
        wavenumber,
        linewidth=2,
        color="darkgreen",
        label="Wavenumber"
    )

    ax.set_title("Wavenumber vs Wavelength")

    ax.set_xlabel("Wavelength (m)")

    ax.set_ylabel("Wavenumber (m⁻¹)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Photon Momentum vs Wavelength
# ==========================================================

def plot_photon_momentum(
        wavelength_min,
        wavelength_max,
        points=200):
    """
    Photon Momentum vs Wavelength.
    """

    wavelength = np.linspace(
        wavelength_min,
        wavelength_max,
        points
    )

    momentum = [
        PhysicsEngine.calculate_photon_momentum(
            wavelength=w
        )
        for w in wavelength
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        wavelength,
        momentum,
        linewidth=2,
        color="darkorange",
        label="Photon Momentum"
    )

    ax.set_title("Photon Momentum vs Wavelength")

    ax.set_xlabel("Wavelength (m)")

    ax.set_ylabel("Photon Momentum (kg·m/s)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Peak Frequency Indicator
# ==========================================================

def calculate_peak_frequency(
        wavelength_min,
        wavelength_max,
        points=200):
    """
    Returns maximum photon frequency.
    """

    wavelength = np.linspace(
        wavelength_min,
        wavelength_max,
        points
    )

    frequency = [
        PhysicsEngine.calculate_frequency(
            wavelength=w
        )
        for w in wavelength
    ]

    return np.max(frequency)