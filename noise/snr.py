"""
snr.py

Signal-to-Noise Ratio (SNR)
calculations for the QCL Simulator.
"""

import math
import numpy as np


# ==========================================================
# Signal-to-Noise Ratio (Linear)
#
# SNR = P_signal / P_noise
# ==========================================================

def calculate_snr(
        signal_power,
        noise_power):
    """
    Calculate Signal-to-Noise Ratio (Linear).

    Parameters
    ----------
    signal_power : float

    noise_power : float

    Returns
    -------
    float
    """

    if signal_power <= 0:
        raise ValueError(
            "Signal power must be greater than zero."
        )

    if noise_power <= 0:
        raise ValueError(
            "Noise power must be greater than zero."
        )

    return signal_power / noise_power


# ==========================================================
# Signal-to-Noise Ratio (dB)
#
# SNR(dB) = 10 log10(P_signal / P_noise)
# ==========================================================

def calculate_snr_db(
        signal_power,
        noise_power):
    """
    Calculate Signal-to-Noise Ratio in dB.
    """

    snr = calculate_snr(
        signal_power,
        noise_power
    )

    return 10 * math.log10(snr)


# ==========================================================
# Signal Power
#
# P_signal = mean(signal²)
# ==========================================================

def calculate_signal_power(signal):
    """
    Calculate average signal power.
    """

    signal = np.asarray(signal)

    return float(np.mean(signal ** 2))


# ==========================================================
# Noise Power
#
# P_noise = mean(noise²)
# ==========================================================

def calculate_noise_power(noise):
    """
    Calculate average noise power.
    """

    noise = np.asarray(noise)

    return float(np.mean(noise ** 2))


# ==========================================================
# SNR from Signal and Noise Arrays
# ==========================================================

def calculate_snr_from_arrays(
        signal,
        noise):
    """
    Calculate SNR directly from
    signal and noise arrays.

    Returns
    -------
    float
        SNR (Linear)
    """

    signal_power = calculate_signal_power(signal)
    noise_power = calculate_noise_power(noise)

    return calculate_snr(
        signal_power,
        noise_power
    )


# ==========================================================
# SNR (dB) from Signal and Noise Arrays
# ==========================================================

def calculate_snr_db_from_arrays(
        signal,
        noise):
    """
    Calculate SNR in dB directly
    from arrays.
    """

    signal_power = calculate_signal_power(signal)
    noise_power = calculate_noise_power(noise)

    return calculate_snr_db(
        signal_power,
        noise_power
    )