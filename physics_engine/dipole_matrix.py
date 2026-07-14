"""
physics/dipole_matrix.py

Dipole Matrix Element Calculations
for Quantum Cascade Lasers

Implements

1. Dipole Matrix Element
2. Dipole Moment
3. Transition Dipole
"""

import numpy as np

# ---------------------------------------------------------
# Physical Constant
# ---------------------------------------------------------

Q = 1.602176634e-19  # Coulomb


def dipole_matrix_element(
    z,
    psi_upper,
    psi_lower
):
    """
    Dipole Matrix Element

        z_ul = ∫ ψu*(z) · z · ψl(z) dz

    Parameters
    ----------
    z : ndarray
        Position (m)

    psi_upper : ndarray
        Upper state wavefunction

    psi_lower : ndarray
        Lower state wavefunction

    Returns
    -------
    float
        Dipole matrix element (m)
    """

    z = np.asarray(z)
    psi_upper = np.asarray(psi_upper)
    psi_lower = np.asarray(psi_lower)

    integrand = (
        np.conjugate(psi_upper)
        * z
        * psi_lower
    )

    return np.real(
        np.trapz(
            integrand,
            z
        )
    )


def dipole_moment(
    z,
    psi_upper,
    psi_lower
):
    """
    Electric Dipole Moment

        p = q · z_ul

    Returns
    -------
    float
        Dipole moment (C·m)
    """

    z_ul = dipole_matrix_element(
        z,
        psi_upper,
        psi_lower
    )

    return Q * z_ul


def dipole_matrix_nm(
    z,
    psi_upper,
    psi_lower
):
    """
    Dipole Matrix Element in nm
    """

    return (
        dipole_matrix_element(
            z,
            psi_upper,
            psi_lower
        )
        * 1e9
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

    psi1 = np.sin(
        np.pi * z / z[-1]
    )

    psi2 = np.sin(
        2 * np.pi * z / z[-1]
    )

    psi1 /= np.sqrt(
        np.trapz(
            np.abs(psi1) ** 2,
            z
        )
    )

    psi2 /= np.sqrt(
        np.trapz(
            np.abs(psi2) ** 2,
            z
        )
    )

    print()

    print(
        "Dipole Matrix (nm):",
        dipole_matrix_nm(
            z,
            psi2,
            psi1
        )
    )

    print()

    print(
        "Dipole Moment:",
        dipole_moment(
            z,
            psi2,
            psi1
        )
    )