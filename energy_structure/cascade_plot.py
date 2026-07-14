"""
energy_structure/cascade_plot.py

Cascade stage visualization for
Quantum Cascade Laser Simulator.
"""

import numpy as np
import matplotlib.pyplot as plt

from physics_engine.physics_engine import PhysicsEngine



def plot_cascade_structure(
        number_of_stages,
        stage_thickness,
        stage_voltage,
        gain_per_stage,
        power_per_stage
):
    """
    Plot Quantum Cascade Laser stage structure.

    Parameters
    ----------
    number_of_stages : int
        Number of cascade stages.

    stage_thickness : float
        Thickness of one stage (m).

    stage_voltage : float
        Voltage drop per stage (V).

    gain_per_stage : float
        Gain contribution of one stage.

    power_per_stage : float
        Output power per stage (W).

    Returns
    -------
    matplotlib Figure
    """

    # -----------------------------
    # Physics calculations
    # -----------------------------

    total_thickness = PhysicsEngine.calculate_total_active_region(
        number_of_stages,
        stage_thickness
    )


    total_voltage = PhysicsEngine.calculate_total_voltage(
        number_of_stages,
        stage_voltage
    )


    total_gain = PhysicsEngine.calculate_total_gain(
        number_of_stages,
        gain_per_stage
    )


    total_power = PhysicsEngine.calculate_total_output_power(
        number_of_stages,
        power_per_stage
    )


    # -----------------------------
    # Generate cascade positions
    # -----------------------------

    stage_positions = np.arange(
        number_of_stages
    ) * stage_thickness



    stage_height = np.ones(
        number_of_stages
    )



    # -----------------------------
    # Plot
    # -----------------------------

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )


    ax.bar(
        stage_positions,
        stage_height,
        width=stage_thickness * 0.8
    )


    # Stage labels

    for i, position in enumerate(stage_positions):

        ax.text(
            position,
            1.05,
            f"S{i+1}",
            ha="center"
        )



    ax.set_title(
        "Quantum Cascade Laser Stage Structure",
        fontsize=14
    )


    ax.set_xlabel(
        "Position (m)"
    )


    ax.set_ylabel(
        "Cascade Stage"
    )


    ax.set_ylim(
        0,
        1.5
    )


    ax.grid(
        True,
        alpha=0.3
    )



    # Display calculated values

    info = (
        f"Stages: {number_of_stages}\n"
        f"Total thickness: {total_thickness:.2e} m\n"
        f"Total voltage: {total_voltage:.2f} V\n"
        f"Total gain: {total_gain:.2f}\n"
        f"Output power: {total_power:.2e} W"
    )


    ax.text(
        1.02,
        0.5,
        info,
        transform=ax.transAxes,
        verticalalignment="center"
    )


    fig.tight_layout()


    return fig