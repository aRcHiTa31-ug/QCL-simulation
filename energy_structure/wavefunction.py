"""
energy_structure/wavefunction.py

Quantum Well Wavefunction calculations and visualization for
the QCL Simulator. Solves the infinite-square-well
wavefunctions consistent with the energy levels computed in
energy_band.py (both assume the same infinite well model:
E_n = n^2 h^2 / (8 m L^2)), normalizes them via PhysicsEngine,
and plots them alongside their probability densities.
"""
import numpy as np
import matplotlib.pyplot as plt

from physics_engine.physics_engine import PhysicsEngine
from energy_structure.energy_band import calculate_well_energy_levels


# ==========================================================
# Analytic Infinite-Well Wavefunction (unnormalized)
# ==========================================================
def _infinite_well_wavefunction(z, well_width, quantum_number):
    """
    Unnormalized infinite-square-well wavefunction.

    psi_n(z) = sin(n * pi * z / L) for 0 <= z <= L, 0 elsewhere.
    """
    psi = np.sin(quantum_number * np.pi * z / well_width)
    psi = np.where((z >= 0) & (z <= well_width), psi, 0.0)
    return psi


# ==========================================================
# Compute Normalized Wavefunctions + Probability Densities
# ==========================================================
def calculate_well_wavefunctions(
        well_width,
        number_of_levels=3,
        points=500):
    """
    Compute normalized wavefunctions and probability densities
    for the first `number_of_levels` states of an infinite
    quantum well.

    Returns
    -------
    tuple
        (z, wavefunctions, densities)
    """
    if number_of_levels < 1:
        raise ValueError(
            f"number_of_levels must be >= 1, got {number_of_levels}."
        )
    if well_width <= 0:
        raise ValueError(f"well_width must be positive, got {well_width}.")

    z = np.linspace(0, well_width, points)

    wavefunctions = []
    densities = []
    for n in range(1, number_of_levels + 1):
        psi_raw = _infinite_well_wavefunction(z, well_width, n)
        psi_normalized = PhysicsEngine.normalize_wavefunction(z=z, psi=psi_raw)
        density = PhysicsEngine.calculate_probability_density(psi_normalized)

        wavefunctions.append(psi_normalized)
        densities.append(density)

    return z, wavefunctions, densities


# ==========================================================
# Plot Wavefunctions + Probability Densities
# ==========================================================
def plot_wavefunctions(
        well_width,
        effective_mass,
        number_of_levels=3,
        points=500):
    """
    Plot quantum well wavefunctions and probability densities,
    each offset vertically by its energy level (in eV).
    """
    z, wavefunctions, densities = calculate_well_wavefunctions(
        well_width=well_width,
        number_of_levels=number_of_levels,
        points=points
    )
    levels_ev = calculate_well_energy_levels(
        well_width=well_width,
        effective_mass=effective_mass,
        number_of_levels=number_of_levels
    )

    z_nm = z * 1e9

    fig, (ax_psi, ax_density) = plt.subplots(
        1, 2, figsize=(12, 6), sharey=False
    )

    scale = (
        (max(levels_ev) - min(levels_ev)) / number_of_levels
        if number_of_levels > 1 else 1.0
    )

    for n, (psi, density, energy) in enumerate(
            zip(wavefunctions, densities, levels_ev), start=1):
        ax_psi.plot(
            z_nm,
            energy + scale * psi / np.max(np.abs(psi)),
            linewidth=2,
            label=f"ψ{n} (E={energy:.4f} eV)"
        )
        ax_psi.hlines(
            energy, z_nm[0], z_nm[-1],
            linestyle="--", linewidth=0.8, color="gray"
        )

        ax_density.plot(
            z_nm,
            energy + scale * density / np.max(density),
            linewidth=2,
            label=f"|ψ{n}|² (E={energy:.4f} eV)"
        )
        ax_density.hlines(
            energy, z_nm[0], z_nm[-1],
            linestyle="--", linewidth=0.8, color="gray"
        )

    ax_psi.set_title("Wavefunctions")
    ax_psi.set_xlabel("Position (nm)")
    ax_psi.set_ylabel("Energy (eV) + scaled ψ")
    ax_psi.grid(True, alpha=0.3)
    ax_psi.legend(fontsize=8)

    ax_density.set_title("Probability Densities")
    ax_density.set_xlabel("Position (nm)")
    ax_density.set_ylabel("Energy (eV) + scaled |ψ|²")
    ax_density.grid(True, alpha=0.3)
    ax_density.legend(fontsize=8)

    fig.suptitle("Quantum Well Wavefunctions and Probability Densities")
    fig.tight_layout()

    return fig