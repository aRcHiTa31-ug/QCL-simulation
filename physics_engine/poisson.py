"""
physics/poisson.py

One-Dimensional Poisson Equation Solver
for Quantum Cascade Lasers

Equation:

d²V/dz² = -ρ(z) / ε

Finite Difference Method
"""

import numpy as np

# ----------------------------------------------------------
# Physical Constants
# ----------------------------------------------------------

EPSILON_0 = 8.854187817e-12  # F/m


class PoissonSolver:

    def __init__(
        self,
        z,
        charge_density,
        relative_permittivity
    ):

        self.z = np.asarray(z)

        self.rho = np.asarray(charge_density)

        self.er = np.asarray(relative_permittivity)

    # ------------------------------------------------------

    def solve(self):

        n = len(self.z)

        dz = self.z[1] - self.z[0]

        epsilon = EPSILON_0 * self.er

        A = np.zeros((n, n))

        b = np.zeros(n)

        # Boundary Conditions
        A[0, 0] = 1
        A[-1, -1] = 1

        b[0] = 0
        b[-1] = 0

        for i in range(1, n - 1):

            A[i, i - 1] = 1

            A[i, i] = -2

            A[i, i + 1] = 1

            b[i] = -(
                self.rho[i]
                * dz ** 2
                / epsilon[i]
            )

        potential = np.linalg.solve(A, b)

        return potential


# ----------------------------------------------------------
# Example
# ----------------------------------------------------------

if __name__ == "__main__":

    z = np.linspace(
        0,
        20e-9,
        500
    )

    charge = np.zeros_like(z)

    charge[200:300] = -1e5

    er = np.ones_like(z) * 13.9

    solver = PoissonSolver(
        z,
        charge,
        er
    )

    V = solver.solve()

    print("Potential calculated.")

    print(V[:10])