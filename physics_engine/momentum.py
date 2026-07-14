"""
physics/momentum.py

Momentum Expectation Value Calculations
for Quantum Cascade Lasers

Implements:

1. Momentum Expectation Value <p>
2. Momentum Squared <p²>
3. Kinetic Energy
"""

import numpy as np

# ---------------------------------------------------------
# Physical Constant
# ---------------------------------------------------------

HBAR = 1.054571817e-34  # J.s


def momentum_expectation(z, psi):
    """
    Calculate

        <p> = ∫ ψ*(-iħ d/dz)ψ dz
    """

    z = np.asarray(z)
    psi = np.asarray(psi)

    dpsi = np.gradient(psi, z)

    numerator = np.trapz(
        np.conjugate(psi) *
        (-1j * HBAR * dpsi),
        z
    )

    denominator = np.trapz(
        np.abs(psi) ** 2,
        z
    )

    return np.real(numerator / denominator)


def momentum_squared(z, psi):
    """
    Calculate

        <p²> = ∫ ψ*(-ħ² d²/dz²)ψ dz
    """

    z = np.asarray(z)
    psi = np.asarray(psi)

    dpsi = np.gradient(psi, z)
    d2psi = np.gradient(dpsi, z)

    numerator = np.trapz(
        np.conjugate(psi) *
        (-HBAR ** 2 * d2psi),
        z
    )

    denominator = np.trapz(
        np.abs(psi) ** 2,
        z
    )

    return np.real(numerator / denominator)


def kinetic_energy(z, psi, effective_mass):
    """
    Calculate kinetic energy

        KE = <p²> / (2m*)
    """

    p2 = momentum_squared(z, psi)

    return p2 / (2 * effective_mass)


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

    m_eff = 0.043 * 9.10938356e-31

    print("Momentum <p> =", momentum_expectation(z, psi))

    print("Momentum² =", momentum_squared(z, psi))

    print("Kinetic Energy =", kinetic_energy(z, psi, m_eff))