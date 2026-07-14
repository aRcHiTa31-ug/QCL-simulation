"""
physics/optical_confinement.py

Optical Confinement Factor
"""

import numpy as np


def confinement_factor(

    active_region_intensity,

    total_intensity

):
    """
    Optical Confinement Factor

    Γ = Active / Total
    """

    return (

        active_region_intensity

        /

        total_intensity

    )


if __name__ == "__main__":

    print(

        confinement_factor(

            0.42,

            1.0

        )

    )