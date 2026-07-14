"""
physics/schrodinger_poisson.py

Self-Consistent Schrödinger-Poisson Solver
for Quantum Cascade Lasers

Workflow

Potential
      ↓
Schrödinger Solver
      ↓
Wavefunctions
      ↓
Charge Density
      ↓
Poisson Solver
      ↓
Updated Potential
      ↓
Repeat until convergence
"""

import numpy as np

from physics_engine.schrodinger import SchrodingerSolver
from physics_engine.poisson import PoissonSolver
from physics_engine.charge_density import electron_charge_density


class SchrodingerPoissonSolver:

    def __init__(
        self,
        z,
        initial_potential,
        effective_mass,
        relative_permittivity,
        electron_density,
        tolerance=1e-6,
        max_iterations=100
    ):

        self.z = np.asarray(z)

        self.potential = np.asarray(initial_potential)

        self.mass = np.asarray(effective_mass)

        self.er = np.asarray(relative_permittivity)

        self.n = electron_density

        self.tolerance = tolerance

        self.max_iterations = max_iterations

    # ------------------------------------------------------

    def solve(self):

        previous = self.potential.copy()

        for iteration in range(self.max_iterations):

            # -------------------------------
            # Schrödinger Equation
            # -------------------------------

            sch = SchrodingerSolver(
                self.z,
                previous,
                self.mass
            )

            energies, wavefunctions = sch.solve()

            ground_state = wavefunctions[:, 0]

            # -------------------------------
            # Charge Density
            # -------------------------------

            rho = electron_charge_density(
                ground_state,
                self.n
            )

            # -------------------------------
            # Poisson Equation
            # -------------------------------

            poi = PoissonSolver(
                self.z,
                rho,
                self.er
            )

            updated = poi.solve()

            error = np.max(
                np.abs(updated - previous)
            )

            previous = updated.copy()

            if error < self.tolerance:

                print(
                    f"Converged in {iteration+1} iterations."
                )

                break

        return {

            "potential": updated,

            "charge_density": rho,

            "energies": energies,

            "wavefunctions": wavefunctions,

            "iterations": iteration + 1,

            "error": error
        }


# ----------------------------------------------------------
# Example
# ----------------------------------------------------------

if __name__ == "__main__":

    from physics_engine.schrodinger import M0, Q

    z = np.linspace(
        0,
        20e-9,
        500
    )

    potential = np.zeros_like(z)

    barrier = 0.52 * Q

    potential[180:320] = barrier

    effective_mass = np.where(

        potential < barrier,

        0.043 * M0,

        0.075 * M0

    )

    relative_permittivity = np.ones_like(z) * 13.9

    solver = SchrodingerPoissonSolver(

        z,

        potential,

        effective_mass,

        relative_permittivity,

        electron_density=1e22

    )

    result = solver.solve()

    print()

    print("Iterations :", result["iterations"])

    print("Final Error :", result["error"])

    print()

    print("Lowest Energy (eV) :")

    print(result["energies"][0] / Q)