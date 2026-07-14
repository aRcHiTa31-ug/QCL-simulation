"""
gain_graph.py
Visualization of Optical Gain
for the Quantum Cascade Laser Simulator.
"""
import numpy as np
import matplotlib.pyplot as plt
from physics_engine.physics_engine import PhysicsEngine
# ==========================================================
# Material Gain vs Population Inversion
# ==========================================================
def plot_material_gain(
        sigma,
        upper_population_max,
        lower_population,
        points=200):
    """
    Material Gain vs Upper State Population.
    """
    upper_population = np.linspace(
        lower_population,
        upper_population_max,
        points
    )
    gain = [
        PhysicsEngine.calculate_optical_gain(
            sigma=sigma,
            upper_population=up,
            lower_population=lower_population
        )
        for up in upper_population
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        upper_population,
        gain,
        linewidth=2.5,
        color="royalblue"
    )
    ax.legend(["Material Gain"])
    ax.set_title("Material Optical Gain")
    ax.set_xlabel("Upper State Population (m⁻³)")
    ax.set_ylabel("Material Gain (m⁻¹)")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Optical Gain Spectrum
# ==========================================================
def plot_gain_spectrum(
        material_gain,
        transition_energy,
        linewidth):
    """
    Optical Gain Spectrum.
    """
    q = 1.602176634e-19
    photon_energy = np.linspace(
        transition_energy - 0.05 * q,
        transition_energy + 0.05 * q,
        500
    )
    spectrum = [
        PhysicsEngine.gain_spectrum(
            photon_energy=e,
            material_gain=material_gain,
            transition_energy=transition_energy,
            linewidth=linewidth
        )
        for e in photon_energy
    ]
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(
        photon_energy / q,
        spectrum,
        linewidth=2,
        color="darkgreen"
    )
    ax.legend(["Gain Spectrum"])
    ax.set_title("Optical Gain Spectrum")
    ax.set_xlabel("Photon Energy (eV)")
    ax.set_ylabel("Spectral Gain")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Modal Gain
# ==========================================================
def plot_modal_gain(
        material_gain,
        max_confinement=1.0,
        points=100):
    """
    Modal Gain vs Optical Confinement Factor.
    """
    confinement = np.linspace(
        0,
        max_confinement,
        points
    )
    modal_gain = [
        PhysicsEngine.modal_gain(
            confinement_factor=gamma,
            material_gain=material_gain
        )
        for gamma in confinement
    ]
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(
        confinement,
        modal_gain,
        linewidth=2,
        color="crimson"
    )
    ax.legend(["Modal Gain"])
    ax.set_title("Modal Gain")
    ax.set_xlabel("Optical Confinement Factor")
    ax.set_ylabel("Modal Gain (m⁻¹)")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Peak Gain Indicator
# ==========================================================
def calculate_peak_gain(
        material_gain,
        transition_energy,
        linewidth):
    """
    Returns the peak value of the gain spectrum.
    """
    q = 1.602176634e-19
    photon_energy = np.linspace(
        transition_energy - 0.05 * q,
        transition_energy + 0.05 * q,
        500
    )
    spectrum = [
        PhysicsEngine.gain_spectrum(
            photon_energy=e,
            material_gain=material_gain,
            transition_energy=transition_energy,
            linewidth=linewidth
        )
        for e in photon_energy
    ]
    return PhysicsEngine.peak_gain(np.array(spectrum))