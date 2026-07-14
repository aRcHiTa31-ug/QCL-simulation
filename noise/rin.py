"""
rin.py

Relative Intensity Noise (RIN)
calculations for the QCL Simulator.
"""

import math
import numpy as np


# ==========================================================
# Relative Intensity Noise (Linear)
#
#           <(ΔP)²>
# RIN = ----------------
#             P²
# ==========================================================

def calculate_rin(
        signal):
    """
    Calculate Relative Intensity Noise (Linear).

    Parameters
    ----------
    signal : array-like
        Optical power measurements

    Returns
    -------
    float
        Relative Intensity Noise
    """

    signal = np.asarray(signal)

    if signal.size == 0:
        raise ValueError(
            "Signal cannot be empty."
        )

    mean_power = np.mean(signal)

    if mean_power <= 0:
        raise ValueError(
            "Mean optical power must be greater than zero."
        )

    variance = np.var(signal)

    return variance / (mean_power ** 2)


# ==========================================================
# Relative Intensity Noise (dB/Hz)
#
# RIN(dB/Hz) = 10 log10(RIN)
# ==========================================================

def calculate_rin_db(
        signal):
    """
    Calculate Relative Intensity Noise
    in dB/Hz.
    """

    rin = calculate_rin(signal)

    return 10 * math.log10(rin)


# ==========================================================
# Mean Optical Power
# ==========================================================

def calculate_mean_power(
        signal):
    """
    Calculate mean optical power.
    """

    signal = np.asarray(signal)

    if signal.size == 0:
        raise ValueError(
            "Signal cannot be empty."
        )

    return float(np.mean(signal))


# ==========================================================
# Power Variance
# ==========================================================

def calculate_power_variance(
        signal):
    """
    Calculate variance of optical power.
    """

    signal = np.asarray(signal)

    if signal.size == 0:
        raise ValueError(
            "Signal cannot be empty."
        )

    return float(np.var(signal))


# ==========================================================
# Power Standard Deviation
# ==========================================================

def calculate_power_std(
        signal):
    """
    Calculate standard deviation
    of optical power.
    """

    signal = np.asarray(signal)

    if signal.size == 0:
        raise ValueError(
            "Signal cannot be empty."
        )

    return float(np.std(signal))