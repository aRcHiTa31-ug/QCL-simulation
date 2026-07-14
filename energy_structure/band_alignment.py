"""
energy_structure/band_alignment.py

Quantum Cascade Laser Band Alignment Visualization
for Desktop Simulator.
"""

import numpy as np
import matplotlib.pyplot as plt

from physics_engine.physics_engine import PhysicsEngine



def plot_band_alignment(
        well_width,
        barrier_width,
        cascade_stages,
        effective_mass,
        barrier_height=0.25,
        number_of_levels=3
):
    """
    Plot QCL conduction band alignment
    with quantum well energy levels.

    Parameters
    ----------
    well_width : float
        Quantum well width (nm)

    barrier_width : float
        Barrier width (nm)

    cascade_stages : int
        Number of QCL stages

    effective_mass : float
        Electron effective mass (kg)

    barrier_height : float
        Barrier height (eV)

    number_of_levels : int
        Number of quantum levels

    Returns
    -------
    matplotlib Figure
    """

    # Convert nm to meter
    well_width_m = well_width * 1e-9


    # -----------------------------
    # Calculate quantum energy levels
    # using Physics Engine
    # -----------------------------

    quantum_levels = []


    for n in range(1, number_of_levels + 1):

        energy_joule = PhysicsEngine.calculate_energy_level(
            quantum_number=n,
            effective_mass=effective_mass,
            well_width=well_width_m
        )


        energy_ev = PhysicsEngine.calculate_joule_to_ev(
            energy_joule
        )


        quantum_levels.append(
            energy_ev
        )



    # -----------------------------
    # Generate band structure
    # -----------------------------

    period = well_width + barrier_width

    total_length = period * cascade_stages


    position = np.linspace(
        0,
        total_length,
        2000
    )


    conduction_band = []


    for x in position:

        local_position = x % period


        if local_position <= well_width:

            energy = 0


        else:

            energy = barrier_height


        conduction_band.append(
            energy
        )



    conduction_band = np.array(
        conduction_band
    )



    # -----------------------------
    # Plot
    # -----------------------------

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )


    # Conduction band

    ax.plot(
        position,
        conduction_band,
        linewidth=2.5,
        label="Conduction Band"
    )



    # Quantum levels inside wells

    for stage in range(cascade_stages):

        start = stage * period


        for index, level in enumerate(quantum_levels):

            ax.hlines(
                level,
                start,
                start + well_width,
                linewidth=2,
                label=f"E{index+1}" if stage == 0 else ""
            )



    # Stage boundaries

    for stage in range(cascade_stages + 1):

        ax.axvline(
            stage * period,
            linestyle="--",
            linewidth=0.8
        )



    ax.set_title(
        "Quantum Cascade Laser Band Alignment",
        fontsize=14
    )


    ax.set_xlabel(
        "Position (nm)"
    )


    ax.set_ylabel(
        "Energy (eV)"
    )


    ax.grid(
        True,
        alpha=0.3
    )


    ax.legend()


    fig.tight_layout()


    return fig