"""
physics/population.py

Population Inversion Calculations
for Quantum Cascade Lasers

Implements

1. Classical Population Inversion
2. Quantum Population Inversion
3. Population Ratio
4. Population Difference
5. Inversion Check
"""

import numpy as np


# ==========================================================
# Classical Population Inversion
# ==========================================================

def calculate_population_inversion(
    upper_population,
    lower_population
):
    """
    Classical Population Inversion

    ΔN = Nu - Nl
    """

    return (
        upper_population
        - lower_population
    )


# ==========================================================
# Quantum Population Inversion
# ==========================================================

def quantum_population_inversion(
    density_matrix,
    upper_state,
    lower_state
):
    """
    Population inversion obtained from
    the diagonal elements of the density matrix.

    ΔN = ρuu - ρll
    """

    rho = np.asarray(
        density_matrix,
        dtype=np.complex128
    )

    return np.real(

        rho[upper_state, upper_state]

        -

        rho[lower_state, lower_state]

    )


# ==========================================================
# Population Ratio
# ==========================================================

def population_ratio(
    upper_population,
    lower_population
):
    """
    Population Ratio

    Nu/Nl
    """

    if lower_population == 0:
        return np.inf

    return (

        upper_population

        /

        lower_population

    )


# ==========================================================
# Population Difference
# ==========================================================

def population_difference(
    populations
):
    """
    Population Difference

    Highest Population
        -
    Lowest Population
    """

    populations = np.asarray(
        populations
    )

    return (

        np.max(populations)

        -

        np.min(populations)

    )


# ==========================================================
# Check Population Inversion
# ==========================================================

def has_population_inversion(
    upper_population,
    lower_population
):
    """
    Returns True if

    Nu > Nl
    """

    return (

        upper_population

        >

        lower_population

    )


# ==========================================================
# Example
# ==========================================================

if __name__ == "__main__":

    upper = 5e22

    lower = 2e22

    print()

    print("Classical Population Inversion")

    print(

        calculate_population_inversion(

            upper,

            lower

        )

    )

    rho = np.array(

        [

            [0.25, 0.02],

            [0.02, 0.75]

        ],

        dtype=np.complex128

    )

    print()

    print("Quantum Population Inversion")

    print(

        quantum_population_inversion(

            rho,

            upper_state=1,

            lower_state=0

        )

    )

    print()

    print("Population Ratio")

    print(

        population_ratio(

            upper,

            lower

        )

    )

    print()

    print("Population Difference")

    print(

        population_difference(

            [

                upper,

                lower,

                3e22

            ]

        )

    )

    print()

    print("Has Population Inversion?")

    print(

        has_population_inversion(

            upper,

            lower

        )

    )