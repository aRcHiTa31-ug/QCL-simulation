"""
wavelength.py

Contains equations related to wavelength and photon energy.
"""

from physics_engine.constants import PLANCK, SPEED_OF_LIGHT


def calculate_wavelength(transition_energy):
    """
    Calculate Wavelength.

    Parameters:
        transition_energy (float): Transition Energy (J)

    Returns:
        float: Wavelength (m)
    """

    if transition_energy <= 0:
        raise ValueError("Transition Energy must be greater than zero.")

    return (PLANCK * SPEED_OF_LIGHT) / transition_energy

def calculate_frequency(wavelength):
    """
    Calculate Photon Frequency.

    Parameters:
        wavelength (float): Wavelength (m)

    Returns:
        float: Frequency (Hz)
    """

    if wavelength <= 0:
        raise ValueError("Wavelength must be greater than zero.")

    return SPEED_OF_LIGHT / wavelength

def calculate_wavenumber(wavelength):
    """
    Calculate Wavenumber.

    Parameters
    ----------
    wavelength : float
        Wavelength (m)

    Returns
    -------
    float
        Wavenumber (m^-1)
    """

    if wavelength <= 0:
        raise ValueError("Wavelength must be greater than zero.")

    return 1 / wavelength

def calculate_photon_momentum(wavelength):
    """
    Calculate Photon Momentum.

    Parameters
    ----------
    wavelength : float
        Wavelength (m)

    Returns
    -------
    float
        Photon Momentum (kg·m/s)
    """

    if wavelength <= 0:
        raise ValueError("Wavelength must be greater than zero.")

    return PLANCK / wavelength