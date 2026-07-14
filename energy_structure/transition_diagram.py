"""
energy_structure/transition_diagram.py

Quantum Level Transition Diagram visualization for the
QCL Simulator. Shows the energy levels of a single quantum
well and the transitions between them, annotated with
transition energy and lasing wavelength.
"""
import matplotlib.pyplot as plt

from energy_structure.energy_band import (
    calculate_well_energy_levels,
    calculate_transition_energies,
    calculate_lasing_wavelength_um,
)


def plot_transition_diagram(
        well_width,
        effective_mass,
        number_of_levels=3,
        highlight_transition=None):
    """
    Plot a quantum level transition diagram for a single well.

    Parameters
    ----------
    well_width : float
        Quantum well width (m).

    effective_mass : float
        Electron effective mass (kg).

    number_of_levels : int
        Number of quantum levels to display (must be >= 2).

    highlight_transition : str, optional
        Key of the transition to highlight (e.g. "E3->E1"), as
        returned by `calculate_transition_energies`. If None,
        the transition between the highest and lowest level is
        highlighted (the dominant lasing transition).

    Returns
    -------
    matplotlib Figure
    """
    if number_of_levels < 2:
        raise ValueError(
            f"number_of_levels must be >= 2 to show a transition, "
            f"got {number_of_levels}."
        )

    levels_ev = calculate_well_energy_levels(
        well_width=well_width,
        effective_mass=effective_mass,
        number_of_levels=number_of_levels
    )
    transitions_ev = calculate_transition_energies(levels_ev)

    if highlight_transition is None:
        highlight_transition = f"E{number_of_levels}->E2"
    if highlight_transition not in transitions_ev:
        raise ValueError(
            f"'{highlight_transition}' is not a valid transition; "
            f"available transitions are: {list(transitions_ev.keys())}."
        )

    fig, ax = plt.subplots(figsize=(8, 7))

    line_x_min, line_x_max = 0.3, 0.7
    label_x = line_x_max + 0.05

    # Draw each energy level as a horizontal line.
    for index, energy in enumerate(levels_ev):
        ax.hlines(
            energy,
            line_x_min,
            line_x_max,
            linewidth=2.5,
            color="black"
        )
        ax.text(
            label_x,
            energy,
            f"E{index + 1} = {energy:.4f} eV",
            va="center",
            fontsize=10
        )

    # Draw an arrow for every transition, highlighting the
    # requested one and dimming the rest.
    arrow_x = (line_x_min + line_x_max) / 2
    for key, energy in transitions_ev.items():
        upper_idx = int(key.split("->")[0][1:]) - 1
        lower_idx = int(key.split("->")[1][1:]) - 1

        is_highlighted = key == highlight_transition
        ax.annotate(
            "",
            xy=(arrow_x, levels_ev[lower_idx]),
            xytext=(arrow_x, levels_ev[upper_idx]),
            arrowprops=dict(
                arrowstyle="->",
                linewidth=2.2 if is_highlighted else 1.0,
                color="crimson" if is_highlighted else "gray",
                alpha=1.0 if is_highlighted else 0.4
            )
        )

    highlighted_energy = transitions_ev[highlight_transition]
    wavelength_um = calculate_lasing_wavelength_um(
        upper_energy_ev=levels_ev[
            int(highlight_transition.split("->")[0][1:]) - 1
        ],
        lower_energy_ev=levels_ev[
            int(highlight_transition.split("->")[1][1:]) - 1
        ]
    )

    ax.set_title(
        f"Quantum Level Transition Diagram\n"
        f"{highlight_transition}: {highlighted_energy:.4f} eV "
        f"({wavelength_um:.2f} µm)",
        fontsize=13
    )
    ax.set_ylabel("Energy (eV)")
    ax.set_xlim(0, 1.4)
    ax.get_xaxis().set_visible(False)
    for spine in ("top", "right", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()

    return fig