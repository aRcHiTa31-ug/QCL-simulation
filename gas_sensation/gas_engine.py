"""
gas_engine.py

Central Gas Sensing Engine
for the QCL Simulator.
"""

# Beer-Lambert Law
from gas_sensation.beer_lambert import (
    calculate_beer_lambert
)

# Transmission
from gas_sensation.transmission import (
    calculate_transmission,
    calculate_transmission_percentage,
    calculate_theoretical_transmission
)

# Optical Intensity
from gas_sensation.optical_intensity import (
    calculate_optical_intensity,
    calculate_incident_intensity,
    calculate_transmitted_intensity
)

# Absorption
from gas_sensation.absorption import (
    calculate_optical_absorption,
    calculate_absorbed_power
)

# Concentration
from gas_sensation.concentration import (
    calculate_gas_concentration,
    concentration_to_ppm,
    concentration_to_percent
)

# Gas Database
from gas_sensation.gas_database import (
    GAS_DATABASE,
    get_gas,
    list_gases,
    gas_exists
)

# Gas Identification
from gas_sensation.gas_identification import (
    identify_gas,
    search_gas,
    list_available_gases,
    get_peak_wavelength,
    get_absorption_coefficient
)

# Spectrum Processing
from gas_sensation.spectrum_processing import (
    baseline_correction,
    normalize_spectrum,
    smooth_spectrum,
    detect_peaks,
    maximum_intensity
)


class GasEngine:
    """
    Central Gas Sensing Engine.
    """

    # -------------------------------------------------
    # Beer-Lambert Law
    # -------------------------------------------------

    calculate_beer_lambert = staticmethod(
        calculate_beer_lambert
    )

    # -------------------------------------------------
    # Transmission
    # -------------------------------------------------

    calculate_transmission = staticmethod(
        calculate_transmission
    )

    calculate_transmission_percentage = staticmethod(
        calculate_transmission_percentage
    )

    calculate_theoretical_transmission = staticmethod(
        calculate_theoretical_transmission
    )

    # -------------------------------------------------
    # Optical Intensity
    # -------------------------------------------------

    calculate_optical_intensity = staticmethod(
        calculate_optical_intensity
    )

    calculate_incident_intensity = staticmethod(
        calculate_incident_intensity
    )

    calculate_transmitted_intensity = staticmethod(
        calculate_transmitted_intensity
    )

    # -------------------------------------------------
    # Absorption
    # -------------------------------------------------

    calculate_optical_absorption = staticmethod(
        calculate_optical_absorption
    )

    calculate_absorbed_power = staticmethod(
        calculate_absorbed_power
    )

    # -------------------------------------------------
    # Gas Concentration
    # -------------------------------------------------

    calculate_gas_concentration = staticmethod(
        calculate_gas_concentration
    )

    concentration_to_ppm = staticmethod(
        concentration_to_ppm
    )

    concentration_to_percent = staticmethod(
        concentration_to_percent
    )

    # -------------------------------------------------
    # Gas Database
    # -------------------------------------------------

    get_gas = staticmethod(
        get_gas
    )

    list_gases = staticmethod(
        list_gases
    )

    gas_exists = staticmethod(
        gas_exists
    )

    # -------------------------------------------------
    # Gas Identification
    # -------------------------------------------------

    identify_gas = staticmethod(
        identify_gas
    )

    search_gas = staticmethod(
        search_gas
    )

    list_available_gases = staticmethod(
        list_available_gases
    )

    get_peak_wavelength = staticmethod(
        get_peak_wavelength
    )

    get_absorption_coefficient = staticmethod(
        get_absorption_coefficient
    )

    # -------------------------------------------------
    # Spectrum Processing
    # -------------------------------------------------

    baseline_correction = staticmethod(
        baseline_correction
    )

    normalize_spectrum = staticmethod(
        normalize_spectrum
    )

    smooth_spectrum = staticmethod(
        smooth_spectrum
    )

    detect_peaks = staticmethod(
        detect_peaks
    )

    maximum_intensity = staticmethod(
        maximum_intensity
    )