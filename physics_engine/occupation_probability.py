"""
physics/occupation_probability.py

Occupation Probability Utilities
for Quantum Cascade Lasers
"""

import numpy as np

from physics_engine.fermi_dirac import (
    fermi_dirac
)


def occupation(
    energy,
    fermi_level,
    temperature
):
    """
    Occupation Probability
    """

    return fermi_dirac(
        energy,
        fermi_level,
        temperature
    )


def empty_state_probability(
    energy,
    fermi_level,
    temperature
):
    """
    Empty State Probability

    1 - f(E)
    """

    return (
        1
        - occupation(
            energy,
            fermi_level,
            temperature
        )
    )


def transition_probability(
    upper_energy,
    lower_energy,
    fermi_level,
    temperature
):
    """
    Transition Probability

    f(lower) × [1 - f(upper)]
    """

    lower = occupation(
        lower_energy,
        fermi_level,
        temperature
    )

    upper = occupation(
        upper_energy,
        fermi_level,
        temperature
    )

    return lower * (1 - upper)


if __name__ == "__main__":

    Q = 1.602176634e-19

    Ef = 0.25 * Q

    T = 300

    E1 = 0.15 * Q

    E2 = 0.30 * Q

    print()

    print(
        "Lower Occupation:",
        occupation(E1, Ef, T)
    )

    print()

    print(
        "Upper Occupation:",
        occupation(E2, Ef, T)
    )

    print()

    print(
        "Transition Probability:",
        transition_probability(
            E2,
            E1,
            Ef,
            T
        )
    )