"""
physics/facet_reflectivity.py

Facet Reflectivity
"""

import numpy as np


def facet_reflectivity(
    refractive_index
):
    """
    Fresnel Reflectivity

    R=((n-1)/(n+1))²
    """

    n = refractive_index

    return (

        (n - 1)

        /

        (n + 1)

    ) ** 2


if __name__ == "__main__":

    print(

        facet_reflectivity(

            3.2

        )

    )