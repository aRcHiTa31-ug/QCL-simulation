"""
physics_engine.py

Central Physics Engine for the QCL Simulator.
This file combines all physics modules into one class.
"""

# Current & Voltage
from physics_engine.current_voltage import(
    calculate_current_density,
    calculate_electric_field
)

# ==========================================================
# Wavefunction
# ==========================================================

from physics_engine.wavefunction import (
    normalize_wavefunction,
    normalize_all_wavefunctions
)




# reliability

from physics_engine.reliability import (
     calculate_arrhenius_factor,
     calculate_mttf,
     calculate_blacks_equation,
     calculate_reliability_function,
     calculate_failure_probability
 )


# Gain
from physics_engine.gain import (
    calculate_optical_gain,
    lorentzian_broadening,
    gain_spectrum,
    peak_gain,
    modal_gain,
    gain_saturation
)

# Population
from physics_engine.population import (
    calculate_population_inversion,
    quantum_population_inversion,
    population_ratio,
    population_difference,
    has_population_inversion
)

# Threshold
from physics_engine.threshold import (
    calculate_threshold_gain,
    calculate_threshold_current_density
)

# power
from physics_engine.power import (
    calculate_output_power,
    calculate_dissipated_power,
    calculate_slope_efficiency,
    calculate_power_density,
    calculate_brightness,
    calculate_voltage_defect,
    calculate_cascade_voltage
)

# Efficiency

from physics_engine.efficiency import (
    calculate_optical_efficiency,
    calculate_wallplug_efficiency,
    calculate_internal_quantum_efficiency,
    calculate_external_quantum_efficiency,
    calculate_differential_quantum_efficiency,
    calculate_injection_efficiency,
    calculate_extraction_efficiency
)
# Temperature
from physics_engine.temperature import (
    calculate_thermal_resistance,
    calculate_temperature_rise,
    calculate_device_temperature,
    calculate_thermal_conductivity,
    calculate_self_heating,
    calculate_threshold_current_temperature
)

# ==========================================================
# Threshold Condition
# ==========================================================

from physics_engine.threshold_condition import (
    threshold_condition,
    threshold_margin
)

# ==========================================================
# Total Scattering
# ==========================================================

from physics_engine.total_scattering import (
    total_scattering_rate,
    total_relaxation_time
)

# ==========================================================
# Mirror Loss
# ==========================================================

from physics_engine.mirror_loss import (
    mirror_loss
)

# ==========================================================
# Optical Confinement
# ==========================================================

from physics_engine.optical_confinement import (
    confinement_factor
)

 # Momentum
# ==========================================================

from physics_engine.momentum import (
    momentum_expectation,
    momentum_squared,
    kinetic_energy
)



# ==========================================================
# Mode Overlap
# ==========================================================

from physics_engine.mode_overlap import (
    mode_overlap
)

# ==========================================================
# Occupation Probability
# ==========================================================

from physics_engine.occupation_probability import (
    occupation,
    empty_state_probability,
    transition_probability
)




# Wavelength
from physics_engine.wavelength import (
    calculate_wavelength,
    calculate_frequency,
    calculate_wavenumber,
    calculate_photon_momentum
)

# Energy Band
from physics_engine.energy_band import (
    calculate_energy_level,
    calculate_transition_energy,
    calculate_photon_energy,
    calculate_frequency_from_energy,
    calculate_transition_wavelength,
    calculate_energy_difference,
    calculate_joule_to_ev
)
# performance
from physics_engine.performance import (
    calculate_brightness,
    calculate_beam_divergence,
    calculate_power_density,
    calculate_spectral_linewidth,
    calculate_characteristic_temperature,
    calculate_voltage_defect,
    calculate_optical_frequency,
    calculate_cascade_voltage,
    calculate_active_region_thickness,
    calculate_figure_of_merit
)

# Cascade Stage
from physics_engine.cascade_stage import (
    calculate_total_active_region,
    calculate_total_voltage,
    calculate_total_gain,
    calculate_total_output_power
)

# quantum wall
from physics_engine.quantum_well import (
    infinite_well_energy,
    infinite_well_energy_ev,
    finite_well_correction
)

#  probability density
from physics_engine.probability_density import (
    probability_density,
    probability_between,
    expectation_position
)

# ==========================================================
# Rate Equations
# ==========================================================

from physics_engine.rate_equations import (
    upper_state_rate,
    lower_state_rate,
    rate_equation,
    steady_state_population
)

# ==========================================================
# Oscillator Strength
# ==========================================================

from physics_engine.oscillator_strength import (
    oscillator_strength,
    normalized_oscillator_strength
)

# ==========================================================
# Optical Transition Rate
# ==========================================================

from physics_engine.optical_transition_rate import (
    spontaneous_transition_rate,
    stimulated_transition_rate
)

# ==========================================================
# LO Phonon
# ==========================================================

from physics_engine.lo_phonon import (
    phonon_occupation,
    emission_rate,
    absorption_rate,
    total_lo_scattering
)




class PhysicsEngine:
    """
    Central Physics Engine for the QCL Simulator.
    """

    # -----------------------
    # Current & Voltage
    # -----------------------

    calculate_current_density = staticmethod(calculate_current_density)
    calculate_electric_field = staticmethod(calculate_electric_field)

    # -----------------------
    # Gain
    # -----------------------


    calculate_optical_gain = staticmethod(calculate_optical_gain)
    lorentzian_broadening = staticmethod(lorentzian_broadening)
    gain_spectrum = staticmethod(gain_spectrum)
    peak_gain = staticmethod(peak_gain)
    modal_gain = staticmethod(modal_gain)
    gain_saturation = staticmethod(gain_saturation)

    # -----------------------
    # Population
    # -----------------------

    calculate_population_inversion = staticmethod(
        calculate_population_inversion
    )
    quantum_population_inversion = staticmethod(
        quantum_population_inversion
    )

    population_ratio = staticmethod(
        population_ratio
    )

    population_difference = staticmethod(
        population_difference
    )

    has_population_inversion = staticmethod(
        has_population_inversion
    )

    # -----------------------
    # Threshold
    # -----------------------

    calculate_threshold_gain = staticmethod(
        calculate_threshold_gain
    )

    calculate_threshold_current_density = staticmethod(
        calculate_threshold_current_density
    )

    # -----------------------
    # Reliability
    # -----------------------

    calculate_arrhenius_factor = staticmethod(
        calculate_arrhenius_factor
    )

    calculate_mttf = staticmethod(
        calculate_mttf
    )

    calculate_blacks_equation = staticmethod(
        calculate_blacks_equation
    )

    calculate_reliability_function = staticmethod(
        calculate_reliability_function
    )

    calculate_failure_probability = staticmethod(
        calculate_failure_probability
    )

    # -----------------------
    # Power
    # -----------------------

    calculate_slope_efficiency = staticmethod(
        calculate_slope_efficiency
    )

    calculate_power_density = staticmethod(
        calculate_power_density
    )

    calculate_brightness = staticmethod(
        calculate_brightness
    )

    calculate_voltage_defect = staticmethod(
        calculate_voltage_defect
    )

    calculate_cascade_voltage = staticmethod(
        calculate_cascade_voltage
    )
    calculate_output_power = staticmethod(
        calculate_output_power
    )
    calculate_dissipated_power=staticmethod(
        calculate_dissipated_power
    )

    # -----------------------
    # Efficiency
    # -----------------------

    calculate_optical_efficiency = staticmethod(
        calculate_optical_efficiency
    )

    calculate_wallplug_efficiency = staticmethod(
        calculate_wallplug_efficiency
    )

    calculate_internal_quantum_efficiency = staticmethod(
        calculate_internal_quantum_efficiency
    )

    calculate_external_quantum_efficiency = staticmethod(
        calculate_external_quantum_efficiency
    )

    calculate_differential_quantum_efficiency = staticmethod(
        calculate_differential_quantum_efficiency
    )

    calculate_injection_efficiency = staticmethod(
        calculate_injection_efficiency
    )

    calculate_extraction_efficiency = staticmethod(
        calculate_extraction_efficiency
    )

    # -----------------------
    # Temperature
    # -----------------------

    calculate_thermal_resistance = staticmethod(
        calculate_thermal_resistance
    )

    calculate_threshold_current_temperature = staticmethod(
        calculate_threshold_current_temperature
    )

    calculate_temperature_rise = staticmethod(
        calculate_temperature_rise
    )

    calculate_device_temperature = staticmethod(
        calculate_device_temperature
    )

    calculate_thermal_conductivity = staticmethod(
        calculate_thermal_conductivity
    )

    calculate_self_heating = staticmethod(
        calculate_self_heating
    )


    # -----------------------
    # Wavelength
    # -----------------------

    calculate_wavelength = staticmethod(
        calculate_wavelength
    )

    calculate_frequency = staticmethod(
        calculate_frequency
    )

    calculate_wavenumber = staticmethod(
        calculate_wavenumber
    )

    calculate_photon_momentum = staticmethod(
        calculate_photon_momentum
    )

    # -----------------------
    # Energy Band
    # -----------------------

    calculate_energy_level = staticmethod(
        calculate_energy_level
    )

    calculate_joule_to_ev = staticmethod(
        calculate_joule_to_ev
    )

    calculate_transition_energy = staticmethod(
        calculate_transition_energy
    )

    calculate_photon_energy = staticmethod(
        calculate_photon_energy
    )

    calculate_frequency_from_energy = staticmethod(
        calculate_frequency_from_energy
    )

    calculate_transition_wavelength = staticmethod(
        calculate_transition_wavelength
    )

    calculate_energy_difference = staticmethod(
        calculate_energy_difference
    )

    # -----------------------
    # Cascade Stage
    # -----------------------

    calculate_total_active_region = staticmethod(
        calculate_total_active_region
    )

    calculate_total_voltage = staticmethod(
        calculate_total_voltage
    )

    calculate_total_gain = staticmethod(
        calculate_total_gain
    )

    calculate_total_output_power = staticmethod(
        calculate_total_output_power
    )

    # performance

    calculate_brightness = staticmethod(
        calculate_brightness
    )

    calculate_beam_divergence = staticmethod(
        calculate_beam_divergence
    )

    calculate_power_density = staticmethod(
        calculate_power_density
    )

    calculate_spectral_linewidth = staticmethod(
        calculate_spectral_linewidth
    )

    calculate_characteristic_temperature = staticmethod(
        calculate_characteristic_temperature
    )

    calculate_voltage_defect = staticmethod(
        calculate_voltage_defect
    )

    calculate_optical_frequency = staticmethod(
        calculate_optical_frequency
    )

    calculate_cascade_voltage = staticmethod(
        calculate_cascade_voltage
    )

    calculate_active_region_thickness = staticmethod(
        calculate_active_region_thickness
    )

    calculate_figure_of_merit = staticmethod(
        calculate_figure_of_merit
    )

    # ======================================================
    # Quantum Well
    # ======================================================

    calculate_infinite_well_energy = staticmethod(
        infinite_well_energy
    )

    calculate_infinite_well_energy_ev = staticmethod(
        infinite_well_energy_ev
    )

    calculate_finite_well_correction = staticmethod(
        finite_well_correction
    )

    # ======================================================
    # Probability Density
    # ======================================================

    calculate_probability_density = staticmethod(
        probability_density
    )

    calculate_probability_between = staticmethod(
        probability_between
    )

    calculate_expectation_position = staticmethod(
        expectation_position
    )

    # ======================================================
    # Wavefunction
    # ======================================================

    normalize_wavefunction = staticmethod(
        normalize_wavefunction
    )

    normalize_all_wavefunctions = staticmethod(
        normalize_all_wavefunctions
    )

    # ======================================================
    # Momentum
    # ======================================================

    momentum_expectation = staticmethod(
        momentum_expectation
    )

    momentum_squared = staticmethod(
        momentum_squared
    )

    kinetic_energy = staticmethod(
        kinetic_energy
    )


    # ======================================================
    # Rate Equations
    # ======================================================

    upper_state_rate = staticmethod(
        upper_state_rate
    )

    lower_state_rate = staticmethod(
        lower_state_rate
    )

    rate_equation = staticmethod(
        rate_equation
    )

    steady_state_population = staticmethod(
        steady_state_population
    )

    # ======================================================
    # Oscillator Strength
    # ======================================================

    oscillator_strength = staticmethod(
        oscillator_strength
    )

    normalized_oscillator_strength = staticmethod(
        normalized_oscillator_strength
    )

    # ======================================================
    # Optical Transition Rate
    # ======================================================

    spontaneous_transition_rate = staticmethod(
        spontaneous_transition_rate
    )

    stimulated_transition_rate = staticmethod(
        stimulated_transition_rate
    )

    # ======================================================
    # LO Phonon
    # ======================================================

    phonon_occupation = staticmethod(
        phonon_occupation
    )

    emission_rate = staticmethod(
        emission_rate
    )

    absorption_rate = staticmethod(
        absorption_rate
    )

    total_lo_scattering = staticmethod(
        total_lo_scattering
    )

    # ======================================================
    # Threshold Condition
    # ======================================================

    threshold_condition = staticmethod(
        threshold_condition
    )

    threshold_margin = staticmethod(
        threshold_margin
    )

    # ======================================================
    # Total Scattering
    # ======================================================

    total_scattering_rate = staticmethod(
        total_scattering_rate
    )

    total_relaxation_time = staticmethod(
        total_relaxation_time
    )

    # ======================================================
    # Mirror Loss
    # ======================================================

    mirror_loss = staticmethod(
        mirror_loss
    )

    # ======================================================
    # Optical Confinement
    # ======================================================

    confinement_factor = staticmethod(
        confinement_factor
    )

    # ======================================================
    # Mode Overlap
    # ======================================================

    mode_overlap = staticmethod(
        mode_overlap
    )

    # ======================================================
    # Occupation Probability
    # ======================================================

    occupation = staticmethod(
        occupation
    )

    empty_state_probability = staticmethod(
        empty_state_probability
    )

    transition_probability = staticmethod(
        transition_probability
    )
