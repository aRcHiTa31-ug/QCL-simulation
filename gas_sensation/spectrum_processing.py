"""
spectrum_processing.py

Spectrum processing functions
for the QCL Gas Sensing module.
"""

# ==========================================================
# Baseline Correction
#
# Corrected = Measured - Baseline
# ==========================================================

def baseline_correction(
        measured_spectrum,
        baseline):
    """
    Perform baseline correction.

    Parameters
    ----------
    measured_spectrum : list[float]

    baseline : list[float]

    Returns
    -------
    list[float]
    """

    if len(measured_spectrum) != len(baseline):
        raise ValueError(
            "Spectrum and baseline must have the same length."
        )

    return [
        measured - base
        for measured, base in zip(
            measured_spectrum,
            baseline
        )
    ]


# ==========================================================
# Normalize Spectrum
#
# S_norm = S / max(S)
# ==========================================================

def normalize_spectrum(spectrum):
    """
    Normalize spectrum between 0 and 1.
    """

    if len(spectrum) == 0:
        raise ValueError(
            "Spectrum cannot be empty."
        )

    maximum = max(spectrum)

    if maximum == 0:
        raise ValueError(
            "Maximum spectrum value cannot be zero."
        )

    return [
        value / maximum
        for value in spectrum
    ]


# ==========================================================
# Moving Average Smoothing
# ==========================================================

def smooth_spectrum(
        spectrum,
        window_size=3):
    """
    Smooth spectrum using moving average.
    """

    if window_size < 1:
        raise ValueError(
            "Window size must be at least 1."
        )

    smoothed = []

    for i in range(len(spectrum)):

        start = max(
            0,
            i - window_size // 2
        )

        end = min(
            len(spectrum),
            i + window_size // 2 + 1
        )

        average = (
            sum(spectrum[start:end])
            /
            (end - start)
        )

        smoothed.append(average)

    return smoothed


# ==========================================================
# Peak Detection
# ==========================================================

def detect_peaks(
        spectrum,
        threshold=0.5):
    """
    Detect spectrum peaks.

    Returns
    -------
    list
        List of peak indices.
    """

    peaks = []

    for i in range(
            1,
            len(spectrum) - 1):

        if (
            spectrum[i] > spectrum[i - 1]
            and
            spectrum[i] > spectrum[i + 1]
            and
            spectrum[i] >= threshold
        ):
            peaks.append(i)

    return peaks


# ==========================================================
# Maximum Intensity
# ==========================================================

def maximum_intensity(spectrum):
    """
    Return maximum intensity.
    """

    if len(spectrum) == 0:
        raise ValueError(
            "Spectrum cannot be empty."
        )

    return max(spectrum)