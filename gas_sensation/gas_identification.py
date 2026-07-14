"""
gas_identification.py

Gas identification module
for the QCL Gas Sensing Simulator.
"""

from gas_sensation.gas_database import GAS_DATABASE


# ==========================================================
# Identify Gas by Peak Wavelength
# ==========================================================

def identify_gas(
        measured_wavelength,
        tolerance=0.10):
    """
    Identify gas using measured absorption wavelength.

    Parameters
    ----------
    measured_wavelength : float
        Measured wavelength (µm)

    tolerance : float
        Allowed wavelength deviation (µm)

    Returns
    -------
    dict
        Identified gas information
    """

    if measured_wavelength <= 0:
        raise ValueError(
            "Measured wavelength must be greater than zero."
        )

    best_match = None
    smallest_error = float("inf")

    for gas_id, gas in GAS_DATABASE.items():

        error = abs(
            measured_wavelength -
            gas["peak_wavelength"]
        )

        if error < smallest_error:

            smallest_error = error
            best_match = gas

    if (
        best_match is not None and
        smallest_error <= tolerance
    ):
        return best_match

    return None


# ==========================================================
# Search Gas by Name
# ==========================================================

def search_gas(gas_name):
    """
    Search gas by its ID.

    Example:
        CH4
        CO2
        NH3
    """

    gas_name = gas_name.upper()

    if gas_name not in GAS_DATABASE:
        raise ValueError(
            f"{gas_name} not found in database."
        )

    return GAS_DATABASE[gas_name]


# ==========================================================
# List Available Gases
# ==========================================================

def list_available_gases():
    """
    Return list of available gases.
    """

    return list(GAS_DATABASE.keys())


# ==========================================================
# Check Gas Availability
# ==========================================================

def gas_exists(gas_name):
    """
    Check whether gas exists.
    """

    return gas_name.upper() in GAS_DATABASE


# ==========================================================
# Get Peak Wavelength
# ==========================================================

def get_peak_wavelength(gas_name):
    """
    Return peak absorption wavelength.
    """

    gas = search_gas(gas_name)

    return gas["peak_wavelength"]


# ==========================================================
# Get Absorption Coefficient
# ==========================================================

def get_absorption_coefficient(gas_name):
    """
    Return absorption coefficient.
    """

    gas = search_gas(gas_name)

    return gas["absorption_coefficient"]