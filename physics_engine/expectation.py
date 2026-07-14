"""
physics/expectation.py

Expectation Value Calculations
for Quantum Cascade Lasers

Implements:

1. Position Expectation Value <z>
2. Position Squared <z²>
3. General Expectation Value <A>
"""

import numpy as np


def expectation_value(z, psi, operator):
    """
    General expectation value

        <A> = ∫ ψ* A ψ dz

    Parameters
    ----------
    z : ndarray
        Position grid (m)

    psi : ndarray
        Wavefunction

    operator : ndarray
        Operator evaluated on z

    Returns
    -------
    float
    """

    z = np.asarray(z)
    psi = np.asarray(psi)
    operator = np.asarray(operator)

    numerator = np.trapz(
        np.conjugate(psi) * operator * psi,
        z
    )

    denominator = np.trapz(
        np.abs(psi) ** 2,
        z
    )

    return np.real(numerator / denominator)


def expectation_position(z, psi):
    """
    Position Expectation Value

        <z>
    """

    return expectation_value(
        z,
        psi,
        z
    )


def expectation_position_squared(z, psi):
    """
    Position Squared Expectation Value

        <z²>
    """

    return expectation_value(
        z,
        psi,
        z ** 2
    )


def standard_deviation_position(z, psi):
    """
    Position Standard Deviation

        σ = sqrt(<z²> - <z>²)
    """

    mean = expectation_position(z, psi)

    mean2 = expectation_position_squared(
        z,
        psi
    )

    return np.sqrt(mean2 - mean ** 2)


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    z = np.linspace(
        0,
        10e-9,
        1000
    )

    psi = np.sin(
        np.pi * z / z[-1]
    )

    psi /= np.sqrt(
        np.trapz(
            np.abs(psi) ** 2,
            z
        )
    )

    print("Expectation <z> =", expectation_position(z, psi))

    print("Expectation <z²> =", expectation_position_squared(z, psi))

    print("σ =", standard_deviation_position(z, psi))