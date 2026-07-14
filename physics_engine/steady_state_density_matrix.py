"""
physics/steady_state_density_matrix.py

Steady-State Density Matrix Solver
for Quantum Cascade Lasers

Uses

- Liouville Equation
- Lindblad Dissipation

to iteratively obtain the steady-state
density matrix.
"""

import numpy as np

from physics_engine.liouville import LiouvilleSolver
from physics_engine.lindblad import LindbladSolver


class SteadyStateDensityMatrix:

    def __init__(
        self,
        hamiltonian,
        lindblad_operators
    ):

        self.H = np.asarray(
            hamiltonian,
            dtype=np.complex128
        )

        self.operators = lindblad_operators

        self.liouville = LiouvilleSolver(
            self.H
        )

        self.lindblad = LindbladSolver()

    # ------------------------------------------------------

    def solve(
        self,
        rho0,
        dt=1e-15,
        tolerance=1e-12,
        max_iterations=10000
    ):
        """
        Solve steady-state density matrix.

        Returns
        -------
        rho
            Steady-state density matrix
        """

        rho = np.asarray(
            rho0,
            dtype=np.complex128
        )

        for iteration in range(max_iterations):

            liouville_term = self.liouville.time_derivative(
                rho
            )

            rho_new = self.lindblad.evolve(

                rho,

                liouville_term,

                self.operators,

                dt

            )

            error = np.max(
                np.abs(rho_new - rho)
            )

            rho = rho_new

            if error < tolerance:

                print(
                    f"Steady state reached in {iteration+1} iterations."
                )

                break

        trace = np.trace(rho)

        if np.abs(trace) > 0:

            rho /= trace

        return rho


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    H = np.array(

        [

            [1.0, 0.1],

            [0.1, 2.0]

        ],

        dtype=np.complex128

    )

    rho0 = np.array(

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

    solver = SteadyStateDensityMatrix(

        H,

        [L]

    )

    rho = solver.solve(rho0)

    print()

    print("Steady-State Density Matrix")

    print(rho)