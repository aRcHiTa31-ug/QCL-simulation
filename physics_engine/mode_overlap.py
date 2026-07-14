"""
physics/mode_overlap.py

Optical Mode Overlap
"""

import numpy as np


def mode_overlap(

    optical_field,

    gain_region

):
    """
    Mode Overlap Integral
    """

    numerator = np.trapz(

        optical_field

        * gain_region

    )

    denominator = np.trapz(

        optical_field

    )

    return numerator / denominator


if __name__ == "__main__":

    field = np.linspace(

        0,

        1,

        1000

    )

    gain = np.ones(1000)

    print(

        mode_overlap(

            field,

            gain

        )

    )