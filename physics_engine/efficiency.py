"""
efficiency.py

Contains efficiency equations for
Quantum Cascade Lasers (QCL).
"""

# ==========================================================
# Optical Efficiency
# η_opt = Pout / P_in
# ==========================================================

def calculate_optical_efficiency(
        optical_output_power,
        electrical_input_power):
    """
    Calculate Optical Efficiency.
    """

    if electrical_input_power <= 0:
        raise ValueError(
            "Electrical input power must be greater than zero."
        )

    return optical_output_power / electrical_input_power


# ==========================================================
# Wall-Plug Efficiency
# η_wp = Pout / (V × I)
# ==========================================================

def calculate_wallplug_efficiency(
        output_power,
        voltage,
        current):
    """
    Calculate Wall-Plug Efficiency.
    """

    electrical_power = voltage * current

    if electrical_power <= 0:
        raise ValueError(
            "Electrical power must be greater than zero."
        )

    return output_power / electrical_power


# ==========================================================
# Internal Quantum Efficiency
# η_int = Γg / (Γg + α_i)
# ==========================================================

def calculate_internal_quantum_efficiency(
        modal_gain,
        internal_loss):
    """
    Calculate Internal Quantum Efficiency.
    """

    denominator = modal_gain + internal_loss

    if denominator <= 0:
        raise ValueError(
            "Modal gain + internal loss must be greater than zero."
        )

    return modal_gain / denominator


# ==========================================================
# External Quantum Efficiency
# η_ext = α_m / (α_m + α_i)
# ==========================================================

def calculate_external_quantum_efficiency(
        mirror_loss,
        internal_loss):
    """
    Calculate External Quantum Efficiency.
    """

    denominator = mirror_loss + internal_loss

    if denominator <= 0:
        raise ValueError(
            "Mirror loss + internal loss must be greater than zero."
        )

    return mirror_loss / denominator


# ==========================================================
# Differential Quantum Efficiency
# η_d = ΔP / ΔI
# ==========================================================

def calculate_differential_quantum_efficiency(
        delta_output_power,
        delta_current):
    """
    Calculate Differential Quantum Efficiency.
    """

    if delta_current == 0:
        raise ValueError(
            "Change in current cannot be zero."
        )

    return delta_output_power / delta_current


# ==========================================================
# Injection Efficiency
# η_inj = Injected carriers / Total carriers
# ==========================================================

def calculate_injection_efficiency(
        injected_carriers,
        total_carriers):
    """
    Calculate Injection Efficiency.
    """

    if total_carriers <= 0:
        raise ValueError(
            "Total carriers must be greater than zero."
        )

    return injected_carriers / total_carriers


# ==========================================================
# Extraction Efficiency
# η_ext = Extracted photons / Generated photons
# ==========================================================

def calculate_extraction_efficiency(
        extracted_photons,
        generated_photons):
    """
    Calculate Extraction Efficiency.
    """

    if generated_photons <= 0:
        raise ValueError(
            "Generated photons must be greater than zero."
        )

    return extracted_photons / generated_photons