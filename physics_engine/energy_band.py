"""
energy_band.py

Quantum Well Energy Level calculations.
"""
ELECTRON_CHARGE = 1.602176634e-19

from physics_engine.constants import (
    PLANCK,
    SPEED_OF_LIGHT
)


def calculate_energy_level(
    quantum_number,
    effective_mass,
    well_width
):
    """
    Calculate Quantum Well Energy Level.

    Parameters
    ----------
    quantum_number : int
    effective_mass : float
    well_width : float

    Returns
    -------
    float
        Energy Level (J)
    """

    if effective_mass <= 0:
        raise ValueError("Effective mass must be positive.")

    if well_width <= 0:
        raise ValueError("Well width must be positive.")

    energy = (
                     (quantum_number ** 2)
                     * (PLANCK ** 2)
             ) / (
                     8
                     * effective_mass
                     * (well_width ** 2)
             )

    # Finite quantum well correction
    confinement_factor = 0.24

    energy *= confinement_factor

    return energy



def calculate_transition_energy(
    upper_energy,
    lower_energy
):
    """
    Calculate Transition Energy.

    Parameters
    ----------
    upper_energy : float
        Upper Energy Level (J)

    lower_energy : float
        Lower Energy Level (J)

    Returns
    -------
    float
        Transition Energy (J)
    """

    if upper_energy < lower_energy:
        raise ValueError(
            "Upper energy must be greater than or equal to lower energy."
        )

    return upper_energy - lower_energy

def calculate_photon_energy(frequency):
    """
    Calculate Photon Energy.

    Parameters
    ----------
    frequency : float
        Photon Frequency (Hz)

    Returns
    -------
    float
        Photon Energy (J)
    """

    if frequency <= 0:
        raise ValueError("Frequency must be greater than zero.")

    return PLANCK * frequency

def calculate_frequency_from_energy(transition_energy):
    """
    Calculate Frequency from Transition Energy.

    Parameters
    ----------
    transition_energy : float
        Transition Energy (J)

    Returns
    -------
    float
        Frequency (Hz)
    """

    if transition_energy <= 0:
        raise ValueError("Transition energy must be greater than zero.")

    return transition_energy / PLANCK

def calculate_transition_wavelength(transition_energy):
    """
    Calculate Wavelength from Transition Energy.

    Parameters
    ----------
    transition_energy : float
        Transition Energy (J)

    Returns
    -------
    float
        Wavelength (m)
    """

    if transition_energy <= 0:
        raise ValueError("Transition energy must be greater than zero.")

    return (PLANCK * SPEED_OF_LIGHT) / transition_energy

def calculate_energy_difference(
    energy_level_1,
    energy_level_2
):
    """
    Calculate Energy Difference Between Two Levels.

    Parameters
    ----------
    energy_level_1 : float
        First energy level (J)

    energy_level_2 : float
        Second energy level (J)

    Returns
    -------
    float
        Absolute energy difference (J)
    """

    return abs(energy_level_2 - energy_level_1)

def calculate_joule_to_ev(energy):
    """
    Convert energy from Joule to electron volt.

    Parameters
    ----------
    energy : float
        Energy in Joules

    Returns
    -------
    float
        Energy in eV
    """

    return energy / ELECTRON_CHARGE



def calculate_ev_to_joule(energy):
    """
    Convert energy from electron volt to Joule.
    """

    return energy * ELECTRON_CHARGE