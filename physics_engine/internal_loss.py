"""
physics/internal_loss.py

Internal Optical Loss
"""

import numpy as np


def internal_loss(

    waveguide_loss,

    free_carrier_loss,

    scattering_loss

):
    """
    Total Internal Loss
    """

    return (

        waveguide_loss

        +

        free_carrier_loss

        +

        scattering_loss

    )


if __name__ == "__main__":

    print(

        internal_loss(

            4,

            1,

            0.5

        )

    )