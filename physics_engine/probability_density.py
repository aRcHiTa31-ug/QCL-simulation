"""
physics/probability_density.py

Probability Density calculations for Quantum Cascade Lasers.

Equation:

P(z) = |ψ(z)|²
"""

import numpy as np


def probability_density(psi):
    """
    Calculate probability density.

    Parameters
    ----------
    psi : ndarray
        Wavefunction

    Returns
    -------
    ndarray
        Probability density |ψ|²
    """
    psi = np.asarray(psi)

    return np.abs(psi) ** 2


def probability_between(z, psi, z_min, z_max):
    """
    Probability of finding the electron
    between z_min and z_max.

    Parameters
    ----------
    z : ndarray
    psi : ndarray
    z_min : float
    z_max : float

    Returns
    -------
    float
    """

    rho = probability_density(psi)

    mask = (z >= z_min) & (z <= z_max)

    return np.trapz(rho[mask], z[mask])


def expectation_position(z, psi):
    """
    Calculate <z>

    Parameters
    ----------
    z : ndarray
    psi : ndarray

    Returns
    -------
    float
    """

    rho = probability_density(psi)

    numerator = np.trapz(z * rho, z)

    denominator = np.trapz(rho, z)

    return numerator / denominator


if __name__ == "__main__":

    z = np.linspace(0, 10e-9, 1000)

    psi = np.sin(np.pi * z / z[-1])

    psi /= np.sqrt(np.trapz(np.abs(psi) ** 2, z))

    rho = probability_density(psi)

    print("Integral =", np.trapz(rho, z))

    print("Mean Position =", expectation_position(z, psi))

    print(
        "Probability in first half =",
        probability_between(
            z,
            psi,
            0,
            5e-9
        )
    )