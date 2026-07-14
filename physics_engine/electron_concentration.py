"""
physics/electron_concentration.py

Electron Concentration Calculations
for Quantum Cascade Lasers

Implements

1. Effective Density of States
2. Electron Concentration
3. Intrinsic Carrier Concentration
"""

import numpy as np

# -------------------------------------------------------
# Physical Constants
# -------------------------------------------------------

K_B = 1.380649e-23          # J/K
HBAR = 1.054571817e-34      # J.s
M0 = 9.10938356e-31         # kg


def effective_density_of_states(
    effective_mass,
    temperature
):
    """
    Effective Density of States (Conduction Band)

    Nc = 2 * ((m*kT)/(2*pi*hbar²))^(3/2)

    Returns
    -------
    float
        Nc (m^-3)
    """

    return 2 * (
        (
            effective_mass
            * K_B
            * temperature
        )
        /
        (
            2
            * np.pi
            * HBAR**2
        )
    ) ** (3 / 2)


def electron_concentration(
    conduction_band_edge,
    fermi_level,
    effective_mass,
    temperature
):
    """
    Electron Concentration

    n = Nc exp(-(Ec-Ef)/kT)

    Returns
    -------
    float
        Electron concentration (m^-3)
    """

    Nc = effective_density_of_states(
        effective_mass,
        temperature
    )

    exponent = -(
        conduction_band_edge
        - fermi_level
    ) / (
        K_B
        * temperature
    )

    exponent = np.clip(
        exponent,
        -700,
        700
    )

    return Nc * np.exp(exponent)


def intrinsic_carrier_concentration(
    Nc,
    Nv,
    bandgap,
    temperature
):
    """
    Intrinsic Carrier Concentration

    ni = sqrt(Nc Nv) exp(-Eg/2kT)
    """

    exponent = -bandgap / (
        2
        * K_B
        * temperature
    )

    exponent = np.clip(
        exponent,
        -700,
        700
    )

    return np.sqrt(
        Nc * Nv
    ) * np.exp(exponent)


# -------------------------------------------------------
# Example
# -------------------------------------------------------

if __name__ == "__main__":

    temperature = 300

    effective_mass = 0.043 * M0

    Ec = 0.55 * 1.602176634e-19

    Ef = 0.50 * 1.602176634e-19

    Nc = effective_density_of_states(
        effective_mass,
        temperature
    )

    n = electron_concentration(
        Ec,
        Ef,
        effective_mass,
        temperature
    )

    print("Effective Density of States")

    print(Nc)

    print()

    print("Electron Concentration")

    print(n)