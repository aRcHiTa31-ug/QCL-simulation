"""
carrier_density.py

Carrier Density Calculations
for the Quantum Cascade Laser Simulator.
"""

import numpy as np


class CarrierDensity:

    @staticmethod
    def calculate_carrier_density(
            current,
            active_region_volume,
            electron_lifetime,
            electron_charge=1.602176634e-19):
        """
        Carrier Density

        n = (I * tau) / (q * V)

        Parameters
        ----------
        current : float
            Injection current (A)

        active_region_volume : float
            Active region volume (m³)

        electron_lifetime : float
            Carrier lifetime (s)

        electron_charge : float
            Electron charge (C)

        Returns
        -------
        float
            Carrier density (m⁻³)
        """

        if active_region_volume <= 0:
            raise ValueError("Active region volume must be positive.")

        return (
            current
            * electron_lifetime
            /
            (electron_charge * active_region_volume)
        )

    @staticmethod
    def calculate_sheet_carrier_density(
            carrier_density,
            active_region_thickness):
        """
        Sheet Carrier Density

        Ns = n × L
        """

        return carrier_density * active_region_thickness

    @staticmethod
    def average_carrier_density(
            carrier_density_array):
        """
        Average Carrier Density.
        """

        return np.mean(carrier_density_array)

    @staticmethod
    def peak_carrier_density(
            carrier_density_array):
        """
        Peak Carrier Density.
        """

        return np.max(carrier_density_array)