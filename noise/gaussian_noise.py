"""
gaussian_noise.py

Gaussian Noise model
for the QCL Simulator.
"""

import numpy as np


# ==========================================================
# Gaussian Noise
#
# y_noise = y + N(0, σ²)
# ==========================================================

def add_gaussian_noise(
        signal,
        noise_std=0.01):
    """
    Add Gaussian noise to a signal.

    Parameters
    ----------
    signal : array-like
        Original signal

    noise_std : float
        Standard deviation of Gaussian noise

    Returns
    -------
    numpy.ndarray
        Noisy signal
    """

    if noise_std < 0:
        raise ValueError(
            "Noise standard deviation cannot be negative."
        )

    signal = np.asarray(signal)

    noise = np.random.normal(
        loc=0.0,
        scale=noise_std,
        size=signal.shape
    )

    return signal + noise


# ==========================================================
# Generate Gaussian Noise Only
# ==========================================================

def generate_gaussian_noise(
        size,
        noise_std=0.01):
    """
    Generate Gaussian noise.

    Parameters
    ----------
    size : int

    noise_std : float

    Returns
    -------
    numpy.ndarray
    """

    if size <= 0:
        raise ValueError(
            "Size must be greater than zero."
        )

    if noise_std < 0:
        raise ValueError(
            "Noise standard deviation cannot be negative."
        )

    return np.random.normal(
        loc=0.0,
        scale=noise_std,
        size=size
    )


# ==========================================================
# Noise Mean
# ==========================================================

def calculate_noise_mean(noise):
    """
    Calculate mean of noise.
    """

    return float(np.mean(noise))


# ==========================================================
# Noise Standard Deviation
# ==========================================================

def calculate_noise_std(noise):
    """
    Calculate standard deviation of noise.
    """

    return float(np.std(noise))


# ==========================================================
# Noise Variance
# ==========================================================

def calculate_noise_variance(noise):
    """
    Calculate variance of noise.
    """

    return float(np.var(noise))