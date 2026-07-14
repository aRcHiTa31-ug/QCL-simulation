"""
physics/rate_equations.py

Carrier Rate Equations
for Quantum Cascade Lasers

Implements

1. Upper State Rate Equation
2. Lower State Rate Equation
3. Generic Multi-Level Rate Equation
"""

import numpy as np


def upper_state_rate(
    injection_rate,
    upper_population,
    upper_lifetime,
    stimulated_emission_rate
):
    """
    dNu/dt

    Parameters
    ----------
    injection_rate : float

    upper_population : float

    upper_lifetime : float

    stimulated_emission_rate : float

    Returns
    -------
    float
    """

    return (
        injection_rate
        -
        upper_population / upper_lifetime
        -
        stimulated_emission_rate
    )


def lower_state_rate(
    stimulated_emission_rate,
    lower_population,
    lower_lifetime,
    extraction_rate
):
    """
    dNl/dt
    """

    return (
        stimulated_emission_rate
        -
        lower_population / lower_lifetime
        -
        extraction_rate
    )


def rate_equation(
    population,
    inflow_rates,
    outflow_rates
):
    """
    Generic Carrier Rate Equation

    dN/dt = Σ(inflow) − Σ(outflow)
    """

    inflow = np.sum(inflow_rates)

    outflow = np.sum(outflow_rates)

    return inflow - outflow


def steady_state_population(
    injection_rate,
    lifetime
):
    """
    Steady-State Population

    N = Rτ
    """

    return injection_rate * lifetime


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    Nu = upper_state_rate(

        injection_rate=5e26,

        upper_population=1e22,

        upper_lifetime=2e-12,

        stimulated_emission_rate=3e25

    )

    Nl = lower_state_rate(

        stimulated_emission_rate=3e25,

        lower_population=5e21,

        lower_lifetime=0.4e-12,

        extraction_rate=1e25

    )

    print()

    print("Upper State Rate")

    print(Nu)

    print()

    print("Lower State Rate")

    print(Nl)

    print()

    print("Steady Population")

    print(

        steady_state_population(

            5e26,

            2e-12

        )

    )