"""
population_graph.py
Visualization of Population Inversion
for the Quantum Cascade Laser Simulator.
"""
import numpy as np
import matplotlib.pyplot as plt
from physics_engine.physics_engine import PhysicsEngine
# ==========================================================
# Classical Population Inversion vs Upper State Population
# ==========================================================
def plot_population_inversion(
        upper_population_max,
        lower_population,
        points=200):
    """
    Population Inversion (ΔN = Nu - Nl) vs Upper State Population.
    """
    upper_population = np.linspace(
        lower_population,
        upper_population_max,
        points
    )
    inversion = [
        PhysicsEngine.calculate_population_inversion(
            upper_population=up,
            lower_population=lower_population
        )
        for up in upper_population
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        upper_population,
        inversion,
        linewidth=2.5,
        color="royalblue"
    )
    ax.legend()
    ax.axhline(0, color="gray", linewidth=1, linestyle="--")
    ax.set_title("Population Inversion")
    ax.set_xlabel("Upper State Population (m⁻³)")
    ax.set_ylabel("Population Inversion ΔN (m⁻³)")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Population Ratio vs Upper State Population
# ==========================================================
def plot_population_ratio(
        upper_population_max,
        lower_population,
        points=200):
    """
    Population Ratio (Nu / Nl) vs Upper State Population.
    """
    upper_population = np.linspace(
        0,
        upper_population_max,
        points
    )
    ratio = [
        PhysicsEngine.population_ratio(
            upper_population=up,
            lower_population=lower_population
        )
        for up in upper_population
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        upper_population,
        ratio,
        linewidth=2,
        color="darkgreen"
    )
    ax.legend()
    ax.axhline(1, color="gray", linewidth=1, linestyle="--")
    ax.set_title("Population Ratio")
    ax.set_xlabel("Upper State Population (m⁻³)")
    ax.set_ylabel("Nu / Nl")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Quantum Population Inversion vs Diagonal Density Matrix Element
# ==========================================================
def plot_quantum_population_inversion(
        coherence=0.02,
        points=100):
    """
    Quantum Population Inversion (ρuu - ρll) vs the upper-state
    diagonal density matrix element, for a simple two-level
    system where ρuu + ρll = 1.
    """
    rho_uu_values = np.linspace(
        0,
        1,
        points
    )
    inversion = []
    for rho_uu in rho_uu_values:
        rho_ll = 1 - rho_uu
        density_matrix = np.array(
            [
                [rho_ll, coherence],
                [coherence, rho_uu]
            ],
            dtype=np.complex128
        )
        inversion.append(
            PhysicsEngine.quantum_population_inversion(
                density_matrix=density_matrix,
                upper_state=1,
                lower_state=0
            )
        )
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        rho_uu_values,
        inversion,
        linewidth=2,
        color="crimson"
    )
    ax.legend()
    ax.axhline(0, color="gray", linewidth=1, linestyle="--")
    ax.set_title("Quantum Population Inversion")
    ax.set_xlabel("Upper State Diagonal Element (ρuu)")
    ax.set_ylabel("Population Inversion (ρuu - ρll)")
    ax.grid(True)
    fig.tight_layout()
    return fig
# ==========================================================
# Peak Population Ratio Indicator
# ==========================================================
def calculate_peak_population_ratio(
        upper_population_max,
        lower_population,
        points=200):
    """
    Returns the peak value of the population ratio curve.
    """
    upper_population = np.linspace(
        1e-12,
        upper_population_max,
        points
    )
    ratio = [
        PhysicsEngine.population_ratio(
            upper_population=up,
            lower_population=lower_population
        )
        for up in upper_population
    ]
    return np.max(ratio)