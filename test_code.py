"""
============================================================
Quantum Cascade Laser Simulator

DRDO Internship Project

Integrated Application Entry Point

This file connects all modules of the simulator.

DO NOT MODIFY THE SCIENTIFIC MODULES.

============================================================
"""

import traceback
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# ==========================================================
# Dashboard
# ==========================================================

from dashboard.theme import apply_theme
from dashboard.sidebar import render_sidebar

from dashboard.layout import render_layout

# ==========================================================
# Physics Engine
# ==========================================================

from physics_engine.physics_engine import PhysicsEngine
# ==========================================================
# Visualization
# ==========================================================

from visualization.gain_graph import *
from visualization.power_graph import *
from visualization.thermal_graph import *
from visualization.threshold_graph import *
from visualization.wavelength_graph import *
from visualization.population_graph import *
from visualization.efficiency_graph import *
from visualization.reliability_graph import *
from visualization.heatmap import *
from visualization.spectrum import *

# ==========================================================
# Reinforcement Learning
# ==========================================================

from RL.environment import QCLPhysicsEnv
from RL.agent import QLearningAgent
from RL.train import train
from RL.evaluate import evaluate_agent
from RL.metrics import Metrics
from RL.action import number_of_actions

# ==========================================================
# Gas Sensing
# ==========================================================

from gas_sensation.gas_engine import GasEngine

# ==========================================================
# Noise
# ==========================================================

from noise.noise_engine import NoiseEngine
# ==========================================================
# Energy Structure
# ==========================================================

from energy_structure.energy_band import (
    build_cascade_energy_structure,
    calculate_well_energy_levels,
    calculate_transition_energies,
    calculate_lasing_wavelength_um,
)

from energy_structure.structure_utils import (
    total_structure_length
)

from energy_structure.band_alignment import (
    plot_band_alignment
)

from energy_structure.wavefunction import (
    plot_wavefunctions
)

from energy_structure.transition_diagram import (
    plot_transition_diagram
)

from energy_structure.cascade_plot import (
    plot_cascade_structure
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Quantum Cascade Laser Simulator",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_theme()

st.title("⚛️ Quantum Cascade Laser Simulator")

st.caption(
    "Physics-Based Quantum Cascade Laser Research Platform"
)

# ==========================================================
# Sidebar
# ==========================================================

inputs = render_sidebar()

# ==========================================================
# Physics Engine Object
# ==========================================================

engine = PhysicsEngine()
gas_engine = GasEngine()
noise_engine = NoiseEngine()

# ==========================================================
# Global Results Dictionary
# ==========================================================

simulation_results = {}
# ==========================================================
# Run Simulation
# ==========================================================

if inputs["run_simulation"]:

    try:

        with st.spinner("Running Quantum Cascade Laser Simulation..."):

            # --------------------------------------------------
            # Read Sidebar Inputs
            # --------------------------------------------------

            current = inputs["current"]
            voltage = inputs["voltage"]
            temperature = inputs["temperature"]

            well_width = inputs["well_width"]
            barrier_width = inputs["barrier_width"]

            cascade_stages = inputs["cascade_stages"]
            doping = inputs["doping"]
            cavity_length = inputs["cavity_length"]

            enable_noise = inputs["enable_noise"]
            noise_level = inputs["noise_level"]
            noise_type = inputs["noise_type"]

            rl_algorithm = inputs["rl_algorithm"]
            episodes = inputs["episodes"]
            learning_rate = inputs["learning_rate"]
            gamma = inputs["gamma"]

            # --------------------------------------------------
            # Save Inputs
            # --------------------------------------------------

            simulation_results["inputs"] = inputs

            # --------------------------------------------------
            # Physics Results Container
            # --------------------------------------------------

            physics_results = {}

            simulation_results["physics"] = physics_results

            # ==========================================================
            # Unit Conversion
            # ==========================================================

            current_A = current / 1000.0  # mA -> A
            well_width_m = well_width * 1e-9  # nm -> m
            barrier_width_m = barrier_width * 1e-9
            cavity_length_m = cavity_length * 1e-6

            # Default ridge dimensions
            ridge_width = 15e-6  # 15 µm
            active_region = 2e-6  # 2 µm

            device_area = ridge_width * active_region

            # ==========================================================
            # Electrical Calculations
            # ==========================================================

            current_density = engine.calculate_current_density(
                current=current_A,
                area=device_area
            )

            electric_field = engine.calculate_electric_field(
                voltage=voltage,
                distance=active_region
            )

            physics_results["current_density"] = current_density
            physics_results["electric_field"] = electric_field

            # ==========================================================
            # Population Inversion
            # ==========================================================

            # Temporary carrier populations.
            # These will later be replaced by the Energy Structure module.
            upper_population = doping
            lower_population = 0.4 * doping

            population_inversion = engine.calculate_population_inversion(
                upper_population,
                lower_population
            )

            physics_results["population_inversion"] = population_inversion

            # ==========================================================
            # Optical Gain
            # ==========================================================

            # Stimulated emission cross-section
            sigma = 2.5e-16

            optical_gain = engine.calculate_optical_gain(
                sigma,
                upper_population,
                lower_population
            )

            physics_results["optical_gain"] = optical_gain

            # ==========================================================
            # Threshold
            # ==========================================================

            internal_loss = 8.0
            mirror_loss = 5.0

            threshold_gain = engine.calculate_threshold_gain(
                internal_loss,
                mirror_loss
            )

            physics_results["threshold_gain"] = threshold_gain

            # ==========================================================
            # Power Calculations
            # ==========================================================

            # Temporary threshold current (A)
            # This will later come from the threshold module.
            threshold_current = 0.10

            # Temporary slope efficiency (W/A)
            # Later this will be computed from measured/simulated data.
            slope_efficiency = 0.80

            output_power = engine.calculate_output_power(
                slope_efficiency,
                current_A,
                threshold_current
            )

            dissipated_power = engine.calculate_dissipated_power(
                voltage,
                current_A,
                output_power
            )

            power_density = engine.calculate_power_density(
                output_power,
                device_area
            )

            physics_results["output_power"] = output_power
            physics_results["dissipated_power"] = dissipated_power
            physics_results["power_density"] = power_density

            # ==========================================================
            # Efficiency Calculations
            # ==========================================================

            electrical_input_power = voltage * current_A

            optical_efficiency = engine.calculate_optical_efficiency(
                output_power,
                electrical_input_power
            )
            st.write("Voltage:", voltage)
            st.write("Current:", current_A)
            st.write("Output Power:", output_power)

            wallplug_efficiency = engine.calculate_wallplug_efficiency(
                output_power,
                voltage,
                current_A
            )

            internal_quantum_efficiency = (
                engine.calculate_internal_quantum_efficiency(
                    optical_gain,
                    internal_loss
                )
            )

            external_quantum_efficiency = (
                engine.calculate_external_quantum_efficiency(
                    mirror_loss,
                    internal_loss
                )
            )

            physics_results["optical_efficiency"] = optical_efficiency
            physics_results["wallplug_efficiency"] = wallplug_efficiency
            physics_results["internal_quantum_efficiency"] = (
                internal_quantum_efficiency
            )
            physics_results["external_quantum_efficiency"] = (
                external_quantum_efficiency
            )

            # ==========================================================
            # Thermal Analysis
            # ==========================================================

            # Initial thermal parameters
            ambient_temperature = temperature
            thermal_resistance = 8.0  # K/W (temporary, will later come from the thermal module)

            temperature_rise = engine.calculate_temperature_rise(
                thermal_resistance,
                dissipated_power
            )

            device_temperature = engine.calculate_device_temperature(
                ambient_temperature,
                temperature_rise
            )

            self_heating = engine.calculate_self_heating(
                thermal_resistance,
                dissipated_power
            )

            physics_results["temperature_rise"] = temperature_rise
            physics_results["device_temperature"] = device_temperature
            physics_results["self_heating"] = self_heating

            # ==========================================================
            # Optical Properties
            # ==========================================================

            # Temporary photon energy (eV)
            # Later this will come from the Energy Structure module.
            photon_energy = 0.27
            photon_energy_joule = photon_energy * 1.602176634e-19
            # st.write("Photon Energy:", photon_energy)

            wavelength = engine.calculate_wavelength(
                photon_energy_joule
            )
            st.write("Calculated Wavelength:", wavelength)

            frequency = engine.calculate_frequency(
                wavelength
            )

            wavenumber = engine.calculate_wavenumber(
                wavelength
            )

            photon_momentum = engine.calculate_photon_momentum(
                wavelength
            )

            physics_results["photon_energy"] = photon_energy
            physics_results["wavelength"] = wavelength
            physics_results["frequency"] = frequency
            physics_results["wavenumber"] = wavenumber
            physics_results["photon_momentum"] = photon_momentum

            # ==========================================================
            # Reliability Analysis
            # ==========================================================

            activation_energy = 0.35  # eV
            operating_temperature = device_temperature
            reference_temperature = 300.0

            arrhenius_factor = engine.calculate_arrhenius_factor(
                activation_energy,
                operating_temperature,
                reference_temperature
            )

            current_density_cm2 = current_density / 1e4

            mttf = engine.calculate_mttf(
                current_density_cm2,
                operating_temperature
            )

            operating_time = 1000

            reliability = engine.calculate_reliability_function(
                operating_time,
                mttf
            )

            operating_time = 1000  # hours (example operating time)

            failure_probability = engine.calculate_failure_probability(
                operating_time,
                mttf
            )

            physics_results["arrhenius_factor"] = arrhenius_factor
            physics_results["mttf"] = mttf
            physics_results["reliability"] = reliability
            physics_results["failure_probability"] = failure_probability

            # ===========================================================
            # Validation Status
            # ==========================================================

            validation_status = "Pending"
            validation_score = 0

            wavelength_um = wavelength * 1e6
            # -------- Wavelength Validation --------
            if 4.4 <= wavelength_um <= 4.8:
                validation_score += 1

            # -------- Temperature Validation --------
            if 300 <= device_temperature <= 380:
                validation_score += 1

            # -------- Cascade Stage Validation --------
            if 35 <= cascade_stages <= 45:
                validation_score += 1

            # -------- Wall Plug Efficiency --------
            if wallplug_efficiency >= 0.05:
                validation_score += 1

            st.write("Wavelength:", wavelength)
            st.write("Temperature:", device_temperature)
            st.write("Cascade Stages:", cascade_stages)
            st.write("Wall Plug Efficiency:", wallplug_efficiency)
            st.write("Validation Score:", validation_score)

            # Final Decision
            if validation_score >= 4:
                validation_status = "Completed"
            else:
                validation_status = "Pending"

            # ==========================================================
            # Gas Sensing (computed early so dashboard_metrics below
            # has real values from the start, instead of None
            # placeholders that render_metrics would display before
            # this ever ran further down the script)
            # ==========================================================

            gas_name = "CO2"
            gas = gas_engine.get_gas(gas_name)

            beam_area = 1e-6
            optical_path = 0.10

            # NOTE: 100 ppm (1e-4 as a mole-fraction) is a realistic
            # trace-gas concentration for a leak/ambient-sensing demo.
            # The previous value of 0.20 meant 20% - it round-tripped
            # through Beer-Lambert and back out as exactly 200,000 ppm
            # every time, which is both physically implausible for a
            # gas sensor and not really "detecting" anything since the
            # forward and inverse calculations perfectly cancel out.
            gas_concentration = 100e-6

            # The QCL may be below threshold for some slider settings
            # (output_power == 0), and calculate_optical_intensity /
            # calculate_beer_lambert both raise ValueError on a
            # zero-or-negative incident intensity. Guard this so a low
            # current setting doesn't crash the whole app.
            gas_sensing_available = output_power > 0

            if gas_sensing_available:

                incident_intensity = gas_engine.calculate_optical_intensity(
                    output_power,
                    beam_area
                )

                transmitted_intensity = gas_engine.calculate_beer_lambert(
                    incident_intensity,
                    gas["absorption_coefficient"],
                    gas_concentration,
                    optical_path
                )

                transmission = gas_engine.calculate_transmission(
                    incident_intensity,
                    transmitted_intensity
                )

                absorption = gas_engine.calculate_optical_absorption(
                    incident_intensity,
                    transmitted_intensity,
                    optical_path
                )

                concentration = gas_engine.calculate_gas_concentration(
                    incident_intensity,
                    transmitted_intensity,
                    gas["absorption_coefficient"],
                    optical_path
                )

                concentration_ppm = gas_engine.concentration_to_ppm(
                    concentration
                )

                # Identify the gas from the QCL's actual simulated
                # emission wavelength, not from the pre-selected gas's
                # own database entry - identifying "gas" using its own
                # peak_wavelength is a tautology that always just
                # returns "gas" again regardless of the real physics.
                detected_gas = gas_engine.identify_gas(
                    wavelength * 1e6
                )
                if detected_gas is None:
                    detected_gas = {
                        "name": "No Match",
                        "formula": "-",
                        "peak_wavelength": wavelength * 1e6,
                    }

                snr_linear = gas_engine.calculate_transmission(
                    incident_intensity,
                    transmitted_intensity
                ) * 100

                # No dedicated detection-limit formula exists in
                # gas_sensation yet. Standard analytical-chemistry
                # convention: LOD ~ 3 * (measured concentration / SNR).
                # This is an approximation, not a calibrated instrument
                # spec - replace with a real LOD model if one becomes
                # available.
                detection_limit = (
                    3 * concentration_ppm / snr_linear
                    if snr_linear > 0 else float("nan")
                )

            else:
                incident_intensity = 0.0
                transmitted_intensity = 0.0
                transmission = 0.0
                absorption = 0.0
                concentration = 0.0
                concentration_ppm = 0.0
                detected_gas = {
                    "name": "N/A (below threshold)",
                    "formula": "-",
                    "peak_wavelength": None,
                }
                detection_limit = float("nan")

            # Dashboard Metrics
            # ==========================================================

            dashboard_metrics = {

                "output_power": output_power * 1000,

                "optical_gain": optical_gain,

                "threshold_current": threshold_current * 1000,

                "wavelength": wavelength * 1e6,

                "efficiency": wallplug_efficiency * 100,

                "temperature": device_temperature,

                "gas_status": detected_gas["name"],

                "rl_status": "Idle",

                "validation_status": validation_status,

                "simulation_status": "Completed",

                "absorbance": absorption,

                "gas_concentration": concentration_ppm,

                "snr": transmission * 100,

                "detection_limit": detection_limit,

            }



            # render_layout(dashboard_metrics)

            # ==========================================================
            # Visualization Inputs
            # ==========================================================
            # The values below feed the Visualization tabs. Where a
            # quantity is already computed above, it's reused directly
            # (e.g. material_gain = optical_gain). Where no upstream
            # module computes it yet, an illustrative literature-typical
            # constant is used instead and clearly marked - these are
            # placeholders, not measured/simulated values, and should be
            # replaced once the corresponding physics module exists.

            # ---- Gain tab ----
            material_gain = optical_gain
            transition_energy = photon_energy_joule
            linewidth = 0.01 * 1.602176634e-19  # ~10 meV, illustrative

            # ---- Thermal tab ----
            characteristic_temperature = 150.0  # K (T0, typical QCL literature value)
            max_temperature = device_temperature + 100.0
            heat_flux = dissipated_power / device_area  # W/m^2
            thickness = active_region
            max_temperature_difference = max(temperature_rise * 2, 20.0)

            # ---- Reliability tab ----
            stress_temperature_max = device_temperature + 100.0
            blacks_constant_a = 1e6  # illustrative Black's-equation constant
            blacks_exponent_n = 2.0  # typical electromigration exponent
            current_density_max = current_density * 10

            # ---- Wavelength & Spectrum tab ----
            wavelength_min = wavelength * 0.9
            wavelength_max = wavelength * 1.1
            spectrum_fwhm = 0.05  # µm, illustrative

            # ---- Efficiency tab ----
            modal_gain_max = optical_gain * 2

            # ---- Energy Structure section (below, outside Visualization) ----
            effective_mass = 0.067 * 9.1093837015e-31  # GaAs-like conduction-band mass
            barrier_height = 0.3 * 1.602176634e-19  # 0.3 eV -> Joules
            number_of_levels = 3
            stage_thickness = well_width_m + barrier_width_m
            stage_voltage = voltage / cascade_stages
            gain_per_stage = optical_gain / cascade_stages
            power_per_stage = output_power / cascade_stages

            # ==========================================================
            # Visualization
            # ==========================================================
            st.header("📈 Physics Visualizations")
            st.caption(
                "Explore the QCL's simulated behavior across gain, power, "
                "thermal, reliability, spectral, and efficiency domains."
            )

            (
                viz_tab_gain,
                viz_tab_power,
                viz_tab_thermal,
                viz_tab_reliability,
                viz_tab_threshold,
                viz_tab_wavelength,
                viz_tab_efficiency,
                viz_tab_heatmap,
                viz_tab_noise,
            ) = st.tabs(
                [
                    "🔬 Gain & Population",
                    "⚡ Power",
                    "🌡️ Thermal",
                    "🛠️ Reliability",
                    "📉 Threshold",
                    "🌈 Wavelength & Spectrum",
                    "🔋 Efficiency",
                    "🗺️ Heatmaps",
                    "🎛️ Noise",
                ]
            )

            # ----------------------------------------------------------
            # Gain & Population
            # ----------------------------------------------------------
            with viz_tab_gain:
                st.subheader("Material Gain vs. Population Inversion")
                col1, col2 = st.columns(2)
                with col1:
                    fig = plot_material_gain(
                        sigma=sigma,
                        upper_population_max=upper_population,
                        lower_population=lower_population,
                    )
                    st.pyplot(fig)
                with col2:
                    fig = plot_population_inversion(
                        upper_population_max=upper_population,
                        lower_population=lower_population,
                    )
                    st.pyplot(fig)

                st.divider()
                st.subheader("Gain Spectrum & Modal Gain")
                col3, col4 = st.columns(2)
                with col3:
                    fig = plot_gain_spectrum(
                        material_gain=material_gain,
                        transition_energy=transition_energy,
                        linewidth=linewidth,
                    )
                    st.pyplot(fig)
                with col4:
                    fig = plot_modal_gain(
                        material_gain=material_gain,
                    )
                    st.pyplot(fig)

                st.divider()
                st.subheader("Population Ratio")
                col5, col6 = st.columns([2, 1])
                with col5:
                    fig = plot_population_ratio(
                        upper_population_max=upper_population,
                        lower_population=lower_population,
                    )
                    st.pyplot(fig)
                with col6:
                    peak_ratio = calculate_peak_population_ratio(
                        upper_population_max=upper_population,
                        lower_population=lower_population,
                    )
                    st.metric("Peak Population Ratio", f"{peak_ratio:.2f}")
                    peak_gain_val = calculate_peak_gain(
                        material_gain=material_gain,
                        transition_energy=transition_energy,
                        linewidth=linewidth,
                    )
                    st.metric("Peak Gain", f"{peak_gain_val:.4g}")

            # ----------------------------------------------------------
            # Power
            # ----------------------------------------------------------
            with viz_tab_power:
                st.subheader("Output Power & Density")
                col1, col2 = st.columns(2)
                with col1:
                    fig = plot_output_power(
                        slope_efficiency=slope_efficiency,
                        current_max=current_A * 2,
                        threshold_current=threshold_current,
                    )
                    st.pyplot(fig)
                with col2:
                    fig = plot_power_density(
                        output_power=output_power,
                        area_max=device_area,
                    )
                    st.pyplot(fig)

                st.divider()
                st.subheader("Dissipated Power")
                col3, col4 = st.columns([2, 1])
                with col3:
                    fig = plot_dissipated_power(
                        slope_efficiency=slope_efficiency,
                        threshold_current=threshold_current,
                        voltage=voltage,
                        current_max=current_A * 2,
                    )
                    st.pyplot(fig)
                with col4:
                    peak_density = calculate_peak_power_density(
                        output_power=output_power,
                        area_max=device_area,
                    )
                    st.metric("Peak Power Density", f"{peak_density:.4g} W/m²")

            # ----------------------------------------------------------
            # Thermal
            # ----------------------------------------------------------
            with viz_tab_thermal:
                st.subheader("Temperature Rise & Device Temperature")
                col1, col2 = st.columns(2)
                with col1:
                    fig = plot_temperature_rise(
                        thermal_resistance=thermal_resistance,
                        max_dissipated_power=dissipated_power,
                    )
                    st.pyplot(fig)
                with col2:
                    fig = plot_device_temperature(
                        ambient_temperature=ambient_temperature,
                        thermal_resistance=thermal_resistance,
                        max_dissipated_power=dissipated_power,
                    )
                    st.pyplot(fig)

                st.divider()
                st.subheader("Threshold Current vs. Temperature & Thermal Conductivity")
                col3, col4 = st.columns(2)
                with col3:
                    fig = plot_threshold_current_temperature(
                        threshold_current_reference=threshold_current,
                        reference_temperature=ambient_temperature,
                        characteristic_temperature=characteristic_temperature,
                        max_temperature=max_temperature,
                    )
                    st.pyplot(fig)
                with col4:
                    fig = plot_thermal_conductivity(
                        heat_flux=heat_flux,
                        thickness=thickness,
                        max_temperature_difference=max_temperature_difference,
                    )
                    st.pyplot(fig)

                peak_temp = calculate_peak_device_temperature(
                    ambient_temperature=ambient_temperature,
                    thermal_resistance=thermal_resistance,
                    max_dissipated_power=dissipated_power,
                )
                st.metric("Peak Device Temperature", f"{peak_temp:.2f} K")

            # ----------------------------------------------------------
            # Reliability
            # ----------------------------------------------------------
            with viz_tab_reliability:
                st.subheader("Reliability & Failure Probability")
                col1, col2 = st.columns(2)
                with col1:
                    fig = plot_reliability(
                        mean_time_to_failure=mttf,
                        max_time=10000,
                    )
                    st.pyplot(fig)
                with col2:
                    fig = plot_failure_probability(
                        mean_time_to_failure=mttf,
                        max_time=10000,
                    )
                    st.pyplot(fig)

                st.divider()
                st.subheader("Arrhenius Acceleration & Black's Equation")
                col3, col4 = st.columns(2)
                with col3:
                    fig = plot_arrhenius_factor(
                        activation_energy=activation_energy,
                        use_temperature=ambient_temperature,
                        stress_temperature_max=stress_temperature_max,
                    )
                    st.pyplot(fig)
                with col4:
                    fig = plot_blacks_equation(
                        constant_A=blacks_constant_a,
                        exponent_n=blacks_exponent_n,
                        activation_energy=activation_energy,
                        temperature=ambient_temperature,
                        current_density_max=current_density_max,
                    )
                    st.pyplot(fig)

                peak_reliability = calculate_peak_reliability(
                    mean_time_to_failure=mttf,
                    max_time=10000,
                )
                st.metric("Peak Reliability", f"{peak_reliability:.4f}")

            # ----------------------------------------------------------
            # Threshold
            # ----------------------------------------------------------
            with viz_tab_threshold:
                st.subheader("Threshold Gain & Current Density")
                col1, col2 = st.columns(2)
                with col1:
                    fig = plot_threshold_gain(
                        internal_loss=internal_loss,
                        mirror_loss_max=20,
                    )
                    st.pyplot(fig)
                with col2:
                    fig = plot_threshold_current_density(
                        threshold_current=threshold_current,
                        area_max=device_area,
                    )
                    st.pyplot(fig)

                col3, col4 = st.columns(2)
                with col3:
                    peak_threshold_gain = calculate_peak_threshold_gain(
                        internal_loss=internal_loss,
                        mirror_loss_max=20,
                    )
                    st.metric("Peak Threshold Gain", f"{peak_threshold_gain:.4g}")
                with col4:
                    peak_threshold_j = calculate_peak_threshold_current_density(
                        threshold_current=threshold_current,
                        area_max=device_area,
                    )
                    st.metric("Peak Threshold Current Density", f"{peak_threshold_j:.4g} A/m²")

            # ----------------------------------------------------------
            # Wavelength & Spectrum
            # ----------------------------------------------------------
            with viz_tab_wavelength:
                st.subheader("Emission Wavelength & Spectrum")
                col1, col2 = st.columns(2)
                with col1:
                    fig = plot_wavelength(
                        transition_energy_min=0.15,
                        transition_energy_max=0.40,
                    )
                    st.pyplot(fig)
                with col2:
                    fig = plot_gaussian_spectrum(
                        center_wavelength=wavelength * 1e6,
                    )
                    st.pyplot(fig)

                st.divider()
                st.subheader("Frequency, Wavenumber & Photon Momentum")
                col3, col4, col5 = st.columns(3)
                with col3:
                    fig = plot_frequency(
                        wavelength_min=wavelength_min,
                        wavelength_max=wavelength_max,
                    )
                    st.pyplot(fig)
                with col4:
                    fig = plot_wavenumber(
                        wavelength_min=wavelength_min,
                        wavelength_max=wavelength_max,
                    )
                    st.pyplot(fig)
                with col5:
                    fig = plot_photon_momentum(
                        wavelength_min=wavelength_min,
                        wavelength_max=wavelength_max,
                    )
                    st.pyplot(fig)

                peak_frequency = calculate_peak_frequency(
                    wavelength_min=wavelength_min,
                    wavelength_max=wavelength_max,
                )
                st.metric("Peak Frequency", f"{peak_frequency:.4g} Hz")

                st.divider()
                st.subheader("Custom Spectrum")
                wl, intensity = generate_gaussian_spectrum(
                    center_wavelength=wavelength * 1e6,
                    fwhm=spectrum_fwhm,
                )
                fig = plot_spectrum(wl, intensity, normalize=True, title="Normalized Emission Spectrum")
                st.pyplot(fig)

            # ----------------------------------------------------------
            # Efficiency
            # ----------------------------------------------------------
            with viz_tab_efficiency:
                st.subheader("Wall-Plug & Quantum Efficiency")
                col1, col2 = st.columns(2)
                with col1:
                    fig = plot_wallplug_efficiency(
                        output_power=output_power,
                        voltage=voltage,
                        current_max=current_A * 2,
                    )
                    st.pyplot(fig)
                with col2:
                    peak_wallplug = calculate_peak_wallplug_efficiency(
                        output_power=output_power,
                        voltage=voltage,
                        current_max=current_A * 2,
                    )
                    st.metric("Peak Wall-Plug Efficiency", f"{peak_wallplug:.2%}")

                st.divider()
                col3, col4 = st.columns(2)
                with col3:
                    fig = plot_internal_quantum_efficiency(
                        modal_gain_max=modal_gain_max,
                        internal_loss=internal_loss,
                    )
                    st.pyplot(fig)
                with col4:
                    fig = plot_external_quantum_efficiency(
                        mirror_loss_max=20,
                        internal_loss=internal_loss,
                    )
                    st.pyplot(fig)

            # ----------------------------------------------------------
            # Heatmaps
            # ----------------------------------------------------------
            with viz_tab_heatmap:
                st.subheader("Output Power vs. Current & Temperature")
                fig = plot_output_power_heatmap(
                    slope_efficiency=slope_efficiency,
                    threshold_current_reference=threshold_current,
                    reference_temperature=ambient_temperature,
                    characteristic_temperature=characteristic_temperature,
                    current_max=current_A * 2,
                    temperature_max=max_temperature,
                )
                st.pyplot(fig)
                peak_power_heatmap = calculate_peak_output_power(
                    slope_efficiency=slope_efficiency,
                    threshold_current_reference=threshold_current,
                    reference_temperature=ambient_temperature,
                    characteristic_temperature=characteristic_temperature,
                    current_max=current_A * 2,
                    temperature_max=max_temperature,
                )
                st.metric("Peak Output Power (over sweep)", f"{peak_power_heatmap:.4g} W")

                st.divider()
                st.subheader("Wall-Plug Efficiency vs. Current & Voltage")
                fig = plot_wallplug_efficiency_heatmap(
                    slope_efficiency=slope_efficiency,
                    threshold_current=threshold_current,
                    current_max=current_A * 2,
                    voltage_max=voltage * 2,
                )
                st.pyplot(fig)

            # ----------------------------------------------------------
            # Noise
            # ----------------------------------------------------------
            with viz_tab_noise:
                st.subheader("Gaussian Noise on Output Power")

                noise_std = output_power * noise_level if enable_noise else output_power * 0.05
                clean_signal = np.full(200, output_power)
                noisy_signal = noise_engine.add_gaussian_noise(clean_signal, noise_std)

                col1, col2 = st.columns([2, 1])
                with col1:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    ax.plot(noisy_signal, linewidth=1.2, color="royalblue", label="Noisy Power")
                    ax.axhline(output_power, color="crimson", linestyle="--", linewidth=1, label="Clean Power")
                    ax.set_xlabel("Sample")
                    ax.set_ylabel("Power (W)")
                    ax.set_title("Output Power with Gaussian Noise")
                    ax.legend()
                    ax.grid(True, alpha=0.3)
                    st.pyplot(fig)
                    plt.close(fig)
                with col2:
                    st.metric("Noise Mean", f"{noise_engine.calculate_noise_mean(noisy_signal - output_power):.4g} W")
                    st.metric("Noise Std Dev", f"{noise_engine.calculate_noise_std(noisy_signal - output_power):.4g} W")
                    st.metric("Noise Variance", f"{noise_engine.calculate_noise_variance(noisy_signal - output_power):.4g} W²")

                st.divider()
                st.subheader("Relative Intensity Noise (RIN)")
                col3, col4 = st.columns([2, 1])
                with col3:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    ax.plot(noisy_signal, linewidth=1.2, color="darkorange")
                    ax.set_xlabel("Sample")
                    ax.set_ylabel("Power (W)")
                    ax.set_title("Signal Used for RIN Calculation")
                    ax.grid(True, alpha=0.3)
                    st.pyplot(fig)
                    plt.close(fig)
                with col4:
                    st.metric("RIN", f"{noise_engine.calculate_rin(noisy_signal):.3e}")
                    st.metric("RIN (dB)", f"{noise_engine.calculate_rin_db(noisy_signal):.2f} dB")
                    st.metric("Mean Power", f"{noise_engine.calculate_mean_power(noisy_signal):.4g} W")

                st.divider()
                st.subheader("Signal-to-Noise Ratio (SNR)")
                noise_component = noisy_signal - output_power
                signal_power = noise_engine.calculate_signal_power(noisy_signal)
                noise_power = noise_engine.calculate_noise_power(noise_component)

                col5, col6 = st.columns([2, 1])
                with col5:
                    fig, ax = plt.subplots(figsize=(8, 4))
                    ax.plot(noise_component, linewidth=1.2, color="seagreen")
                    ax.set_xlabel("Sample")
                    ax.set_ylabel("Deviation (W)")
                    ax.set_title("Noise Component")
                    ax.grid(True, alpha=0.3)
                    st.pyplot(fig)
                    plt.close(fig)
                with col6:
                    st.metric("SNR", f"{noise_engine.calculate_snr(signal_power, noise_power):.4g}")
                    st.metric("SNR (dB)", f"{noise_engine.calculate_snr_db(signal_power, noise_power):.2f} dB")

            # ==========================================================
            # ==========================================================
            # Reinforcement Learning
            # ==========================================================

            import matplotlib.pyplot as plt

            st.header("🤖 Reinforcement Learning")

            rl_tab1, rl_tab2 = st.tabs([
                "Training",
                "Visualization"
            ])

            rl_environment = QCLPhysicsEnv()

            rl_agent = QLearningAgent(
                state_size=rl_environment.state_size,
                action_size=number_of_actions(),
                learning_rate=learning_rate,
                discount_factor=gamma,
            )

            if "training_results" not in st.session_state:
                st.session_state.training_results = None

            # ==========================================================
            # Training Tab
            # ==========================================================

            with rl_tab1:

                st.success("RL Environment Initialized")

                col1, col2 = st.columns(2)

                with col1:
                    st.write("State Size :", rl_environment.state_size)
                    st.write("Action Size :", rl_environment.action_size)

                with col2:
                    st.write("Episodes :", episodes)
                    st.write("Learning Rate :", learning_rate)
                    st.write("Discount Factor :", gamma)

                if st.button("🚀 Train RL Agent"):
                    with st.spinner("Training Reinforcement Learning Agent..."):
                        st.session_state.training_results = train(
                            num_episodes=episodes
                        )

                    st.success("Training Completed!")

                if st.button("📊 Evaluate RL Agent"):
                    with st.spinner("Evaluating Agent..."):
                        evaluation_results = evaluate_agent(
                            rl_environment,
                            rl_agent,
                            episodes=5
                        )

                    st.success("Evaluation Completed")
                    st.json(evaluation_results)

            # ==========================================================
            # Visualization Tab
            # ==========================================================

            with rl_tab2:

                st.subheader("RL Training Dashboard")

                if st.session_state.training_results is None:

                    st.info("Train the RL Agent first.")

                else:

                    results = st.session_state.training_results

                    col1, col2, col3, col4 = st.columns(4)

                    col1.metric(
                        "Episodes",
                        results["episodes"]
                    )

                    col2.metric(
                        "Average Reward",
                        f"{results['average_reward']:.2f}"
                    )

                    col3.metric(
                        "Best Reward",
                        f"{results['best_reward']:.2f}"
                    )

                    col4.metric(
                        "Final Epsilon",
                        f"{results['final_epsilon']:.3f}"
                    )

                    st.markdown("---")

                    # Reward Curve
                    st.subheader("📈 Reward Curve")

                    fig, ax = plt.subplots(figsize=(8, 4))

                    ax.plot(results["rewards"], linewidth=2)

                    ax.set_xlabel("Episode")
                    ax.set_ylabel("Reward")
                    ax.grid(True)

                    st.pyplot(fig)

                    plt.close(fig)

                    # Epsilon Curve
                    st.subheader("📉 Epsilon Decay")

                    fig, ax = plt.subplots(figsize=(8, 4))

                    ax.plot(results["epsilon_history"], linewidth=2)

                    ax.set_xlabel("Episode")
                    ax.set_ylabel("Epsilon")
                    ax.grid(True)

                    st.pyplot(fig)

                    plt.close(fig)


                # ==========================================================
            # Gas Sensing Module
            # ==========================================================

            st.header("🧪 Gas Sensing")

            # gas_name, gas, incident_intensity, transmitted_intensity,
            # transmission, absorption, concentration, concentration_ppm,
            # and detected_gas were already computed earlier (before
            # dashboard_metrics was built) - reused here, not recomputed.
            st.write(detected_gas)
            st.write(gas["peak_wavelength"])

            st.subheader("Gas Detection Results")

            st.metric(
                "Detected Gas",
                detected_gas["name"]
            )

            st.metric(
                "Peak Wavelength (µm)",
                detected_gas["peak_wavelength"]
            )

            st.metric(
                "Transmission",
                f"{transmission:.4f}"
            )

            st.metric(
                "Absorption",
                f"{absorption:.4f}"
            )

            st.metric(
                "Estimated Concentration",
                f"{concentration_ppm:.2f} ppm"
            )

            # ==========================================================
            # Energy Structure
            # ==========================================================

            st.header("⚛️ Energy Structure")

            energy_structure = build_cascade_energy_structure(
                well_width=well_width_m,
                effective_mass=effective_mass,
                cascade_stages=cascade_stages,
                number_of_levels=3
            )

            simulation_results["energy_structure"] = energy_structure

            st.success("Energy Structure Calculated")

            st.write(
                f"Number of Cascade Stages : {cascade_stages}"
            )

            st.write(
                f"Dominant Lasing Wavelength : "
                f"{energy_structure[0]['lasing_wavelength_um']:.3f} µm"
            )

            energy_tab1, energy_tab2 = st.tabs(
                [
                    "Band Structure",
                    "Wavefunctions"
                ]
            )

            with energy_tab1:

                fig = plot_band_alignment(
                    well_width=well_width,
                    barrier_width=barrier_width,
                    cascade_stages=cascade_stages,
                    effective_mass=effective_mass
                )

                st.pyplot(fig)

                stage_thickness = (
                        (well_width + barrier_width)
                        * 1e-9
                )

                fig = plot_cascade_structure(
                    number_of_stages=cascade_stages,
                    stage_thickness=stage_thickness,
                    stage_voltage=voltage / cascade_stages,
                    gain_per_stage=optical_gain / cascade_stages,
                    power_per_stage=output_power / cascade_stages
                )

                st.pyplot(fig)

            with energy_tab2:

                fig = plot_wavefunctions(
                    well_width=well_width_m,
                    effective_mass=effective_mass
                )

                st.pyplot(fig)

                fig = plot_transition_diagram(
                    well_width=well_width_m,
                    effective_mass=effective_mass
                )

                st.pyplot(fig)

                # ==========================================================
            # Validation
            # ==========================================================

            st.header("✅ ErwinJr2 Validation")

            import json
            import os
            import pandas as pd

            validation_rows = []

            json_files = [

                "assets/erwin_validation1.json",
                "assets/erwin_validation2.json",
                "assets/erwin_validation3.json",
                "assets/erwin_validation4.json"

            ]

            simulator_layer_width = well_width + barrier_width

            simulator_wavelength = wavelength * 1e6

            simulator_temperature = device_temperature

            simulator_states = 3

            for file in json_files:

                if not os.path.exists(file):
                    continue

                with open(file, "r") as f:

                    erwin = json.load(f)

                qcl = erwin["QCLayers"]

                erwin_layer_width = sum(qcl["Width"])

                erwin_wavelength = qcl["Wavelength"]

                erwin_temperature = qcl["Temperature"]

                erwin_states = qcl["No of states"]

                validation_rows.append({

                    "File":

                        os.path.basename(file),

                    "Simulator λ (µm)":

                        round(simulator_wavelength, 3),

                    "Erwin λ (µm)":

                        erwin_wavelength,

                    "Simulator Temp":

                        simulator_temperature,

                    "Erwin Temp":

                        erwin_temperature,

                    "Simulator States":

                        simulator_states,

                    "Erwin States":

                        erwin_states,

                    "Simulator Layer Width":

                        simulator_layer_width,

                    "Erwin Layer Width":

                        erwin_layer_width

                })

            validation_df = pd.DataFrame(validation_rows)

            st.dataframe(
                validation_df,
                use_container_width=True
            )

            # dashboard_metrics["validation_status"] = "Completed"
            # render_metrics(dashboard_metrics)
            # render_layout(dashboard_metrics)
            if validation_status == "Completed":
                dashboard_metrics["validation_status"] = "Completed"
            else:
                dashboard_metrics["validation_status"] = "Pending"

            # render_layout(dashboard_metrics)
            # Update the dashboard after all values are ready

            render_layout(dashboard_metrics)
            st.success(
                "Validation Completed Successfully"
            )



    except Exception as e:
        st.error(f"Simulation failed: {e}")
        st.exception(e)
        st.code(traceback.format_exc())