"""
physics/lindblad.py

Lindblad Master Equation
for Quantum Cascade Lasers

Implements

dρ/dt = -(i/ħ)[H,ρ] + Σ L(ρ)

where

L(ρ) is the Lindblad Dissipator
representing scattering and relaxation.
"""

import numpy as np

HBAR = 1.054571817e-34


class LindbladSolver:

    def __init__(self):

        pass

    # --------------------------------------------------

    @staticmethod
    def dagger(A):
        """
        Hermitian Conjugate
        """

        return np.conjugate(A.T)

    # --------------------------------------------------

    def dissipator(
        self,
        rho,
        L
    ):
        """
        Lindblad Dissipator

        D(ρ)=

        LρL†

        -

        1/2(L†Lρ + ρL†L)
        """

        rho = np.asarray(
            rho,
            dtype=np.complex128
        )

        L = np.asarray(
            L,
            dtype=np.complex128
        )

        Ld = self.dagger(L)

        term1 = L @ rho @ Ld

        term2 = Ld @ L @ rho

        term3 = rho @ Ld @ L

        return term1 - 0.5 * (term2 + term3)

    # --------------------------------------------------

    def total_dissipation(
        self,
        rho,
        operators
    ):
        """
        Sum of all Lindblad operators.
        """

        total = np.zeros_like(
            rho,
            dtype=np.complex128
        )

        for L in operators:

            total += self.dissipator(
                rho,
                L
            )

        return total

    # --------------------------------------------------

    def evolve(
        self,
        rho,
        liouville_term,
        operators,
        dt
    ):
        """
        One Euler Step

        ρ(t+dt)=ρ+dt(Liouville+Dissipation)
        """

        dissipation = self.total_dissipation(
            rho,
            operators
        )

        drho = (

            liouville_term

            +

            dissipation

        )

        return rho + dt * drho


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    rho = np.array(

        [

            [1.0, 0.0],

            [0.0, 0.0]

        ],

        dtype=np.complex128

    )

    gamma = 1e12

    L = np.sqrt(gamma) * np.array(

        [

            [0, 1],

            [0, 0]

        ],

        dtype=np.complex128

    )

    solver = LindbladSolver()

    D = solver.dissipator(

        rho,

        L

    )

    print()

    print("Lindblad Dissipator")

    print(D)

    rho2 = solver.evolve(

        rho,

        np.zeros_like(rho),

        [L],

        1e-15

    )

    print()

    print("Updated Density Matrix")

    print(rho2)