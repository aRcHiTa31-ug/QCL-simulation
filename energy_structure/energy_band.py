"""
energy_structure/energy_band.py

Quantum Well Energy Level and Transition calculations for the
QCL cascade structure. This module sits above physics_engine's
own low-level equations (raw formulas) and organizes them into
per-well and per-stage results that band_alignment.py,
cascade_plot.py, and transition_diagram.py can reuse, instead of
each recomputing quantum levels inline.
"""
from typing import Dict, List

from physics_engine.constants import ELECTRON_CHARGE
from physics_engine.physics_engine import PhysicsEngine


# ==========================================================
# Single Quantum Well Energy Levels
# ==========================================================
def calculate_well_energy_levels(
        well_width,
        effective_mass,
        number_of_levels=3):
    """
    Calculate the first `number_of_levels` quantum well energy
    levels, in eV.

    Parameters
    ----------
    well_width : float
        Quantum well width (m).

    effective_mass : float
        Electron effective mass (kg).

    number_of_levels : int
        Number of quantum levels to compute (must be >= 1).

    Returns
    -------
    list of float
        Energy levels in eV, ordered E1, E2, E3, ...
    """
    if number_of_levels < 1:
        raise ValueError(
            f"number_of_levels must be >= 1, got {number_of_levels}."
        )

    levels_ev = []
    for n in range(1, number_of_levels + 1):
        energy_joule = PhysicsEngine.calculate_energy_level(
            quantum_number=n,
            effective_mass=effective_mass,
            well_width=well_width
        )
        levels_ev.append(energy_joule / ELECTRON_CHARGE)

    return levels_ev


# ==========================================================
# Transition Energies Between Levels
# ==========================================================
def calculate_transition_energies(levels_ev):
    """
    Calculate transition energies between all pairs of levels
    where the upper level has a higher index (and therefore
    higher energy) than the lower level.

    Parameters
    ----------
    levels_ev : list of float
        Energy levels in eV, ordered E1, E2, E3, ... (as returned
        by `calculate_well_energy_levels`).

    Returns
    -------
    dict
        Keys are f"E{upper}->E{lower}" (1-indexed), values are
        the transition energy in eV.
    """
    if len(levels_ev) < 2:
        raise ValueError(
            "At least two energy levels are required to compute "
            "a transition."
        )

    transitions: Dict[str, float] = {}
    for upper_idx in range(len(levels_ev)):
        for lower_idx in range(upper_idx):
            upper_energy_j = levels_ev[upper_idx] * ELECTRON_CHARGE
            lower_energy_j = levels_ev[lower_idx] * ELECTRON_CHARGE

            transition_energy_j = PhysicsEngine.calculate_transition_energy(
                upper_energy=upper_energy_j,
                lower_energy=lower_energy_j
            )

            key = f"E{upper_idx + 1}->E{lower_idx + 1}"
            transitions[key] = transition_energy_j / ELECTRON_CHARGE

    return transitions


# ==========================================================
# Lasing Wavelength From a Transition
# ==========================================================
def calculate_lasing_wavelength_um(
        upper_energy_ev,
        lower_energy_ev):
    """
    Calculate the lasing wavelength (in micrometers) for a
    transition between two energy levels.

    Parameters
    ----------
    upper_energy_ev : float
        Upper energy level (eV).

    lower_energy_ev : float
        Lower energy level (eV).

    Returns
    -------
    float
        Wavelength (micrometers).
    """
    upper_energy_j = upper_energy_ev * ELECTRON_CHARGE
    lower_energy_j = lower_energy_ev * ELECTRON_CHARGE

    transition_energy_j = PhysicsEngine.calculate_transition_energy(
        upper_energy=upper_energy_j,
        lower_energy=lower_energy_j
    )

    wavelength_m = PhysicsEngine.calculate_transition_wavelength(
        transition_energy=transition_energy_j
    )

    return wavelength_m * 1e6


# ==========================================================
# Full Cascade Energy Structure
# ==========================================================
def build_cascade_energy_structure(
        well_width,
        effective_mass,
        cascade_stages,
        number_of_levels=3):
    """
    Build the full per-stage energy band structure for a QCL
    cascade: quantum levels, all pairwise transitions, and the
    lasing wavelength for the dominant (highest-to-lowest)
    transition, repeated identically for every stage (since each
    stage is assumed structurally identical).

    Parameters
    ----------
    well_width : float
        Quantum well width (m).

    effective_mass : float
        Electron effective mass (kg).

    cascade_stages : int
        Number of QCL stages (must be >= 1).

    number_of_levels : int
        Number of quantum levels per well.

    Returns
    -------
    list of dict
        One dict per stage, each containing:
            "stage": int (0-indexed)
            "levels_ev": list of float
            "transitions_ev": dict
            "lasing_wavelength_um": float
    """
    if cascade_stages < 1:
        raise ValueError(
            f"cascade_stages must be >= 1, got {cascade_stages}."
        )

    levels_ev = calculate_well_energy_levels(
        well_width=well_width,
        effective_mass=effective_mass,
        number_of_levels=number_of_levels
    )
    transitions_ev = calculate_transition_energies(levels_ev)

    lasing_wavelength_um = calculate_lasing_wavelength_um(
        upper_energy_ev=levels_ev[2],  # E3
        lower_energy_ev=levels_ev[1]  # E2
    )

    structure:List[Dict] = []
    for stage in range(cascade_stages):
        structure.append({
            "stage": stage,
            "levels_ev": levels_ev,
            "transitions_ev": transitions_ev,
            "lasing_wavelength_um": lasing_wavelength_um,
        })

    return structure