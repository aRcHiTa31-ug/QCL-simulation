"""
physics/wavefunction.py

Wavefunction Utilities for Quantum Cascade Lasers

This module provides functions for

1. Wavefunction Normalization
2. Probability Density
"""

import numpy as np

# NumPy 2.0 removed `np.trapz` in favor of `np.trapezoid`. Support
# both so this module works on either NumPy 1.x or 2.x.
_trapezoid = getattr(np, "trapezoid", None) or np.trapz


def normalize_wavefunction(z, psi):
    """
    Normalize a wavefunction.

    Parameters
    ----------
    z : ndarray
        Position grid (m)

    psi : ndarray
        Wavefunction

    Returns
    -------
    ndarray
        Normalized wavefunction
    """

    z = np.asarray(z)
    psi = np.asarray(psi)

    norm = np.sqrt(_trapezoid(np.abs(psi) ** 2, z))

    if norm == 0:
        raise ValueError("Wavefunction norm is zero.")

    return psi / norm


def normalize_all_wavefunctions(z, wavefunctions):
    """
    Normalize all eigenstates.

    Parameters
    ----------
    z : ndarray

    wavefunctions : ndarray
        Matrix returned by numpy.linalg.eigh()

    Returns
    -------
    ndarray
        Normalized wavefunctions
    """

    normalized = np.zeros_like(wavefunctions)

    for i in range(wavefunctions.shape[1]):
        normalized[:, i] = normalize_wavefunction(
            z,
            wavefunctions[:, i]
        )

    return normalized


def probability_density(psi):
    """
    Compute probability density.

    Parameters
    ----------
    psi : ndarray

    Returns
    -------
    ndarray
        |psi|^2
    """

    return np.abs(psi) ** 2



