"""
physics/fermi_dirac.py

Fermi-Dirac Statistics for Quantum Cascade Lasers

Implements

1. Fermi-Dirac Distribution
2. Maxwell-Boltzmann Approximation
3. Fermi Occupation
"""

import numpy as np

# -------------------------------------------------------
# Physical Constants
# -------------------------------------------------------

K_B = 1.380649e-23          # J/K
Q = 1.602176634e-19         # Coulomb


def fermi_dirac(
    energy,
    fermi_level,
    temperature
):
    """
    Fermi-Dirac Distribution

        f(E)=1/(1+exp((E-Ef)/kT))

    Parameters
    ----------
    energy : ndarray or float
        Energy (J)

    fermi_level : float
        Fermi Energy (J)

    temperature : float
        Temperature (K)

    Returns
    -------
    ndarray or float
        Occupation Probability
    """

    energy = np.asarray(energy)

    exponent = (
        (energy - fermi_level)
        /
        (K_B * temperature)
    )

    exponent = np.clip(
        exponent,
        -700,
        700
    )

    return 1.0 / (
        1.0 + np.exp(exponent)
    )


def maxwell_boltzmann(
    energy,
    fermi_level,
    temperature
):
    """
    Maxwell-Boltzmann Approximation

    Valid when

        E - Ef >> kT
    """

    exponent = (
        -(energy - fermi_level)
        /
        (K_B * temperature)
    )

    exponent = np.clip(
        exponent,
        -700,
        700
    )

    return np.exp(exponent)


def occupation_probability(
    energy,
    fermi_level,
    temperature
):
    """
    Alias for Fermi-Dirac Distribution
    """

    return fermi_dirac(
        energy,
        fermi_level,
        temperature
    )


# -------------------------------------------------------
# Example
# -------------------------------------------------------

if __name__ == "__main__":

    energy = np.linspace(
        0,
        0.5 * Q,
        500
    )

    Ef = 0.25 * Q

    T = 300

    f = fermi_dirac(
        energy,
        Ef,
        T
    )

    print()

    print("Occupation at Ef")

    print(
        fermi_dirac(
            Ef,
            Ef,
            T
        )
    )

    print()

    print("Maximum Occupation")

    print(np.max(f))

    print()

    print("Minimum Occupation")

    print(np.min(f))