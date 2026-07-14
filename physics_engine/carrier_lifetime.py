"""
physics/carrier_lifetime.py

Carrier Lifetime Calculations
for Quantum Cascade Lasers

Implements

1. Carrier Lifetime
2. Upper State Lifetime
3. Lower State Lifetime
4. Effective Lifetime
5. Lifetime from Scattering Rates
"""

import numpy as np


def carrier_lifetime(
    recombination_rate
):
    """
    Carrier Lifetime

    τ = 1 / R
    """

    if recombination_rate <= 0:
        raise ValueError(
            "Recombination rate must be positive."
        )

    return 1.0 / recombination_rate


def upper_state_lifetime(
    scattering_rate
):
    """
    Upper State Lifetime
    """

    return carrier_lifetime(
        scattering_rate
    )


def lower_state_lifetime(
    scattering_rate
):
    """
    Lower State Lifetime
    """

    return carrier_lifetime(
        scattering_rate
    )


def effective_lifetime(
    lifetimes
):
    """
    Effective Lifetime

    1/τeff = Σ(1/τi)
    """

    lifetimes = np.asarray(
        lifetimes,
        dtype=float
    )

    if np.any(lifetimes <= 0):
        raise ValueError(
            "All lifetimes must be positive."
        )

    return 1.0 / np.sum(
        1.0 / lifetimes
    )


def lifetime_from_scattering(
    scattering_rates
):
    """
    Lifetime from multiple
    scattering mechanisms.
    """

    scattering_rates = np.asarray(
        scattering_rates,
        dtype=float
    )

    if np.any(scattering_rates < 0):
        raise ValueError(
            "Scattering rates cannot be negative."
        )

    total_rate = np.sum(
        scattering_rates
    )

    if total_rate == 0:
        return np.inf

    return 1.0 / total_rate


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    print()

    print(
        "Carrier Lifetime:"
    )

    print(
        carrier_lifetime(
            5e11
        )
    )

    print()

    print(
        "Upper Lifetime:"
    )

    print(
        upper_state_lifetime(
            3e11
        )
    )

    print()

    print(
        "Lower Lifetime:"
    )

    print(
        lower_state_lifetime(
            8e11
        )
    )

    print()

    print(
        "Effective Lifetime:"
    )

    print(
        effective_lifetime(
            [
                2e-12,
                3e-12,
                5e-12
            ]
        )
    )

    print()

    print(
        "Lifetime from Scattering:"
    )

    print(
        lifetime_from_scattering(
            [
                2e11,
                4e11,
                1e11
            ]
        )
    )