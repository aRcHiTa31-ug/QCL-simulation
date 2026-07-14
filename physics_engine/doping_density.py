"""
physics/doping_density.py

Doping Density Utilities
for Quantum Cascade Lasers
"""

import numpy as np


def donor_density(profile):
    """
    Donor Density Profile
    """

    return np.asarray(profile)


def acceptor_density(profile):
    """
    Acceptor Density Profile
    """

    return np.asarray(profile)


def net_doping(
    donor,
    acceptor
):
    """
    Net Doping

    ND - NA
    """

    donor = np.asarray(donor)
    acceptor = np.asarray(acceptor)

    return donor - acceptor


def uniform_doping(
    z,
    concentration
):
    """
    Uniform Doping Profile
    """

    return np.ones_like(z) * concentration


def gaussian_doping(
    z,
    peak,
    center,
    sigma
):
    """
    Gaussian Doping Profile
    """

    return peak * np.exp(
        -((z - center) ** 2)
        /
        (2 * sigma ** 2)
    )


if __name__ == "__main__":

    z = np.linspace(
        0,
        20e-9,
        1000
    )

    profile = gaussian_doping(
        z,
        5e22,
        10e-9,
        2e-9
    )

    print()

    print("Maximum Doping")

    print(np.max(profile))