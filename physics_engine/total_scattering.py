"""
physics/total_scattering.py

Total Scattering Rate
for Quantum Cascade Lasers
"""

import numpy as np


def total_scattering_rate(
    lo_rate,
    acoustic_rate,
    interface_rate,
    alloy_rate,
    impurity_rate,
    electron_rate
):
    """
    Total Scattering Rate

    Wtotal = Σ Wi
    """

    return (

        lo_rate

        +

        acoustic_rate

        +

        interface_rate

        +

        alloy_rate

        +

        impurity_rate

        +

        electron_rate

    )


def total_relaxation_time(
    total_rate
):
    """
    Overall Relaxation Time

    τ = 1/Wtotal
    """

    if total_rate <= 0:
        return np.inf

    return 1.0 / total_rate


if __name__ == "__main__":

    total = total_scattering_rate(

        lo_rate=2e12,

        acoustic_rate=1e11,

        interface_rate=5e10,

        alloy_rate=8e10,

        impurity_rate=3e10,

        electron_rate=2e10

    )

    print("Total Scattering Rate")

    print(total)

    print()

    print("Total Relaxation Time")

    print(
        total_relaxation_time(total)
    )