"""
physics/finite_quantum_well.py

Finite Quantum Well Energy Solver
for Quantum Cascade Lasers

Uses a transcendental equation to estimate
bound-state energies in a finite quantum well.
"""

import numpy as np
from scipy.optimize import brentq

# ---------------------------------------------------------
# Physical Constants
# ---------------------------------------------------------

HBAR = 1.054571817e-34      # J.s
M0 = 9.10938356e-31         # kg
Q = 1.602176634e-19         # C


class FiniteQuantumWell:

    def __init__(self, width, barrier_height, effective_mass):

        self.L = width
        self.V0 = barrier_height
        self.m = effective_mass

    # -----------------------------------------------------

    def k(self, E):

        return np.sqrt(2 * self.m * E) / HBAR

    def alpha(self, E):

        return np.sqrt(2 * self.m * (self.V0 - E)) / HBAR

    # -----------------------------------------------------

    def even_equation(self, E):

        if E <= 0 or E >= self.V0:
            return np.nan

        k = self.k(E)
        a = self.alpha(E)

        return k * np.tan(k * self.L / 2) - a

    # -----------------------------------------------------

    def odd_equation(self, E):

        if E <= 0 or E >= self.V0:
            return np.nan

        k = self.k(E)
        a = self.alpha(E)

        return -k / np.tan(k * self.L / 2) - a

    # -----------------------------------------------------

    def solve_even(self):

        energies = []

        scan = np.linspace(
            1e-6 * Q,
            self.V0 * 0.999,
            2000
        )

        for i in range(len(scan) - 1):

            try:

                f1 = self.even_equation(scan[i])
                f2 = self.even_equation(scan[i + 1])

                if np.isnan(f1) or np.isnan(f2):
                    continue

                if f1 * f2 < 0:

                    root = brentq(
                        self.even_equation,
                        scan[i],
                        scan[i + 1]
                    )

                    energies.append(root)

            except:
                pass

        return energies

    # -----------------------------------------------------

    def solve_odd(self):

        energies = []

        scan = np.linspace(
            1e-6 * Q,
            self.V0 * 0.999,
            2000
        )

        for i in range(len(scan) - 1):

            try:

                f1 = self.odd_equation(scan[i])
                f2 = self.odd_equation(scan[i + 1])

                if np.isnan(f1) or np.isnan(f2):
                    continue

                if f1 * f2 < 0:

                    root = brentq(
                        self.odd_equation,
                        scan[i],
                        scan[i + 1]
                    )

                    energies.append(root)

            except:
                pass

        return energies

    # -----------------------------------------------------

    def solve(self):

        even = self.solve_even()

        odd = self.solve_odd()

        energies = sorted(even + odd)

        return np.array(energies)


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    width = 5e-9

    barrier = 0.52 * Q

    m_eff = 0.043 * M0

    solver = FiniteQuantumWell(
        width,
        barrier,
        m_eff
    )

    energies = solver.solve()

    print("Finite Quantum Well Bound States")

    for i, E in enumerate(energies):

        print(f"Level {i+1}: {E/Q:.5f} eV")