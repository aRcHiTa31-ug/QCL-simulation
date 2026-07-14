"""
physics/mirror_loss.py

Mirror Loss Calculations
for Quantum Cascade Lasers
"""

import numpy as np


def mirror_loss(
    cavity_length,
    reflectivity_front,
    reflectivity_back
):
    """
    Mirror Loss

    αm = (1/2L) ln(1/(R1R2))

    Parameters
    ----------
    cavity_length : float
        Cavity length (m)

    reflectivity_front : float

    reflectivity_back : float

    Returns
    -------
    float
        Mirror loss (m^-1)
    """

    return (
        1
        /
        (2 * cavity_length)
    ) * np.log(
        1
        /
        (
            reflectivity_front
            * reflectivity_back
        )
    )


if __name__ == "__main__":

    loss = mirror_loss(

        cavity_length=3e-3,

        reflectivity_front=0.27,

        reflectivity_back=0.95

    )

    print()

    print("Mirror Loss")

    print(loss)