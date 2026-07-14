"""
noise_engine.py

Central Noise Engine
for the QCL Simulator.
"""

# Gaussian Noise
from noise.gaussian_noise import (
    add_gaussian_noise,
    generate_gaussian_noise,
    calculate_noise_mean,
    calculate_noise_std,
    calculate_noise_variance
)

# Signal-to-Noise Ratio
from noise.snr import (
    calculate_snr,
    calculate_snr_db,
    calculate_signal_power,
    calculate_noise_power,
    calculate_snr_from_arrays,
    calculate_snr_db_from_arrays
)

# Relative Intensity Noise
from noise.rin import (
    calculate_rin,
    calculate_rin_db,
    calculate_mean_power,
    calculate_power_variance,
    calculate_power_std
)


class NoiseEngine:
    """
    Central Noise Engine
    for the QCL Simulator.
    """

    # =====================================================
    # Gaussian Noise
    # =====================================================

    add_gaussian_noise = staticmethod(
        add_gaussian_noise
    )

    generate_gaussian_noise = staticmethod(
        generate_gaussian_noise
    )

    calculate_noise_mean = staticmethod(
        calculate_noise_mean
    )

    calculate_noise_std = staticmethod(
        calculate_noise_std
    )

    calculate_noise_variance = staticmethod(
        calculate_noise_variance
    )

    # =====================================================
    # Signal-to-Noise Ratio
    # =====================================================

    calculate_snr = staticmethod(
        calculate_snr
    )

    calculate_snr_db = staticmethod(
        calculate_snr_db
    )

    calculate_signal_power = staticmethod(
        calculate_signal_power
    )

    calculate_noise_power = staticmethod(
        calculate_noise_power
    )

    calculate_snr_from_arrays = staticmethod(
        calculate_snr_from_arrays
    )

    calculate_snr_db_from_arrays = staticmethod(
        calculate_snr_db_from_arrays
    )

    # =====================================================
    # Relative Intensity Noise
    # =====================================================

    calculate_rin = staticmethod(
        calculate_rin
    )

    calculate_rin_db = staticmethod(
        calculate_rin_db
    )

    calculate_mean_power = staticmethod(
        calculate_mean_power
    )

    calculate_power_variance = staticmethod(
        calculate_power_variance
    )

    calculate_power_std = staticmethod(
        calculate_power_std
    )