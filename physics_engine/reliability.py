"""
reliability.py

Reliability equations for Quantum Cascade Lasers (QCL).
"""

import math


# ==========================================================
# Arrhenius Acceleration Factor
#
# AF = exp[(Ea/k) * (1/Tuse - 1/Tstress)]
# ==========================================================

def calculate_arrhenius_factor(
        activation_energy,
        use_temperature,
        stress_temperature):
    """
    Calculate Arrhenius Acceleration Factor.

    Parameters
    ----------
    activation_energy : float
        Activation Energy (eV)

    use_temperature : float
        Normal operating temperature (K)

    stress_temperature : float
        Accelerated test temperature (K)

    Returns
    -------
    float
        Acceleration Factor
    """

    if use_temperature <= 0:
        raise ValueError(
            "Use temperature must be greater than zero."
        )

    if stress_temperature <= 0:
        raise ValueError(
            "Stress temperature must be greater than zero."
        )

    BOLTZMANN_EV = 8.617333262145e-5

    exponent = (
        activation_energy / BOLTZMANN_EV
    ) * (
        (1 / use_temperature)
        - (1 / stress_temperature)
    )

    return math.exp(exponent)


# ==========================================================
# Mean Time To Failure (MTTF)
#
# MTTF = Total Operating Time / Number of Failures
# ==========================================================

def calculate_mttf(
        total_operating_time,
        number_of_failures):
    """
    Calculate Mean Time To Failure.
    """

    if number_of_failures <= 0:
        raise ValueError(
            "Number of failures must be greater than zero."
        )

    return total_operating_time / number_of_failures


# ==========================================================
# Black's Equation
#
# MTTF = A * J^(-n) * exp(Ea / kT)
# ==========================================================

def calculate_blacks_equation(
        constant_A,
        current_density,
        exponent_n,
        activation_energy,
        temperature):
    """
    Calculate Black's Equation.
    """

    if current_density <= 0:
        raise ValueError(
            "Current density must be greater than zero."
        )

    if temperature <= 0:
        raise ValueError(
            "Temperature must be greater than zero."
        )

    BOLTZMANN_EV = 8.617333262145e-5

    return (
        constant_A
        * (current_density ** (-exponent_n))
        * math.exp(
            activation_energy /
            (BOLTZMANN_EV * temperature)
        )
    )


# ==========================================================
# Reliability Function
#
# R(t) = exp(-t / MTTF)
# ==========================================================

def calculate_reliability_function(
        operating_time,
        mean_time_to_failure):
    """
    Calculate Reliability Function.
    """

    if mean_time_to_failure <= 0:
        raise ValueError(
            "MTTF must be greater than zero."
        )

    return math.exp(
        -operating_time / mean_time_to_failure
    )


# ==========================================================
# Failure Probability
#
# F(t) = 1 - R(t)
# ==========================================================

def calculate_failure_probability(
        operating_time,
        mean_time_to_failure):
    """
    Calculate Failure Probability.
    """

    reliability = calculate_reliability_function(
        operating_time,
        mean_time_to_failure
    )

    return 1 - reliability