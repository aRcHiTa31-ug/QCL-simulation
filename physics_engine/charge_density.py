"""
physics/charge_density.py

Charge Density Calculations
for Quantum Cascade Lasers

Implements:

1. Electron Charge Density
2. Net Charge Density
3. Sheet Charge Density
"""

import numpy as np

# ---------------------------------------------------------
# Physical Constants
# ---------------------------------------------------------

Q = 1.602176634e-19  # Coulomb


def electron_charge_density(psi, electron_density):
    """
    Electron Charge Density

        ρ = -q n |ψ|²

    Parameters
    ----------
    psi : ndarray
        Normalized wavefunction

    electron_density : float
        Electron concentration (m^-3)

    Returns
    -------
    ndarray
        Charge density (C/m³)
    """

    psi = np.asarray(psi)

    probability = np.abs(psi) ** 2

    return -Q * electron_density * probability


def net_charge_density(
    electron_density,
    donor_density,
    acceptor_density=0.0
):
    """
    Net Charge Density

        ρ = q(ND - NA - n)

    Parameters
    ----------
    electron_density : ndarray or float

    donor_density : ndarray or float

    acceptor_density : ndarray or float

    Returns
    -------
    ndarray
        Net charge density (C/m³)
    """

    return Q * (
        donor_density
        - acceptor_density
        - electron_density
    )


def sheet_charge_density(
    charge_density,
    z
):
    """
    Sheet Charge Density

        Ns = ∫ ρ(z)/q dz

    Parameters
    ----------
    charge_density : ndarray

    z : ndarray

    Returns
    -------
    float
        Sheet Density (m^-2)
    """

    return np.trapz(
        charge_density / Q,
        z
    )


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

    rho = electron_charge_density(
        psi,
        1e22
    )

    print("Maximum Charge Density")

    print(np.max(np.abs(rho)))

    print(
        "Sheet Density =",
        sheet_charge_density(
            rho,
            z
        )
    )