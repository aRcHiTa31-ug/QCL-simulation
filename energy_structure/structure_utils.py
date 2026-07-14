"""
energy_structure/structure_utils.py

Utility functions for Quantum Cascade Laser
energy structure visualization.

These functions provide common helpers used by
band_alignment.py, cascade_plot.py and
transition_diagram.py.
"""

from physics_engine.physics_engine import PhysicsEngine


def stage_length(
        well_width,
        barrier_width):
    """
    Return the length of one cascade stage.

    Parameters
    ----------
    well_width : float
        Quantum well width (nm or m).

    barrier_width : float
        Barrier width (nm or m).

    Returns
    -------
    float
        Total stage length.
    """

    return well_width + barrier_width


def total_structure_length(
        well_width,
        barrier_width,
        cascade_stages):
    """
    Calculate total device length.

    Returns
    -------
    float
    """

    return (
        stage_length(
            well_width,
            barrier_width
        )
        * cascade_stages
    )


def stage_position(
        stage_number,
        well_width,
        barrier_width):
    """
    Return the starting position of a stage.

    Parameters
    ----------
    stage_number : int

    Returns
    -------
    float
    """

    return (
        stage_number
        * stage_length(
            well_width,
            barrier_width
        )
    )


def calculate_conduction_band_energy(
        voltage,
        temperature,
        doping_concentration,
        barrier_height=0.25):
    """
    Calculate well and barrier energies.

    Returns
    -------
    tuple
        (well_energy, barrier_energy)
    """

    well_energy = PhysicsEngine.calculate_energy_level(
        voltage=voltage,
        temperature=temperature,
        doping_density=doping_concentration
    )

    barrier_energy = (
        well_energy
        + barrier_height
    )

    return well_energy, barrier_energy


def stage_labels(cascade_stages):
    """
    Generate stage labels.

    Returns
    -------
    list
    """

    return [
        f"Stage {i + 1}"
        for i in range(cascade_stages)
    ]


def validate_structure_inputs(
        well_width,
        barrier_width,
        cascade_stages):
    """
    Validate energy structure inputs.
    """

    if well_width <= 0:
        raise ValueError(
            "Well width must be positive."
        )

    if barrier_width <= 0:
        raise ValueError(
            "Barrier width must be positive."
        )

    if cascade_stages <= 0:
        raise ValueError(
            "Cascade stages must be positive."
        )