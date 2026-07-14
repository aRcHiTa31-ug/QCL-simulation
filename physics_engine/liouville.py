"""
physics/liouville.py

Liouville-von Neumann Equation
for Quantum Cascade Lasers

Implements

    dρ/dt = -(i/ħ)[H,ρ]

where

H = Hamiltonian
ρ = Density Matrix
"""

import numpy as np

HBAR = 1.054571817e-34


class LiouvilleSolver:

    def __init__(self, hamiltonian):

        self.H = np.asarray(
            hamiltonian,
            dtype=np.complex128
        )

    # -----------------------------------------------------

    def commutator(
        self,
        rho
    ):
        """
        Calculate

            [H,ρ] = Hρ - ρH
        """

        rho = np.asarray(
            rho,
            dtype=np.complex128
        )

        return (

            self.H @ rho

            -

            rho @ self.H

        )

    # -----------------------------------------------------

    def time_derivative(
        self,
        rho
    ):
        """
        Liouville-von Neumann Equation

        dρ/dt = -(i/ħ)[H,ρ]
        """

        return (

            -1j / HBAR

        ) * self.commutator(rho)

    # -----------------------------------------------------

    def evolve(
        self,
        rho,
        dt
    ):
        """
        One Forward Euler Time Step
        """

        rho = np.asarray(
            rho,
            dtype=np.complex128
        )

        drho = self.time_derivative(
            rho
        )

        return rho + dt * drho


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    H = np.array([

        [1.0, 0.1],

        [0.1, 2.0]

    ], dtype=np.complex128)

    rho = np.array([

        [1.0, 0.0],

        [0.0, 0.0]

    ], dtype=np.complex128)

    solver = LiouvilleSolver(H)

    drho = solver.time_derivative(rho)

    print()

    print("dρ/dt")

    print(drho)

    print()

    rho_new = solver.evolve(

        rho,

        1e-15

    )

    print("Updated Density Matrix")

    print(rho_new)