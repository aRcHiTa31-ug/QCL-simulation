"""
schrodinger.py

Finite Difference Schrödinger Equation Solver
for Quantum Cascade Laser (QCL) simulations.
"""

import numpy as np
from scipy.linalg import eigh


class SchrodingerSolver:
    """
    1D Time-Independent Schrödinger Equation Solver.
    """

    def __init__(
            self,
            z,
            potential,
            effective_mass):

        self.z = np.asarray(z)

        self.V = np.asarray(potential)

        self.m = effective_mass

        self.hbar = 1.054571817e-34

        self.q = 1.602176634e-19

        self.m0 = 9.10938356e-31

        self.dz = self.z[1] - self.z[0]

    # ======================================================
    # Hamiltonian Matrix
    # ======================================================

    def build_hamiltonian(self):
        """
        Construct Hamiltonian matrix using
        finite difference approximation.
        """

        n = len(self.z)

        mass = self.m * self.m0

        t = (self.hbar ** 2) / (2 * mass * self.dz ** 2)

        H = np.zeros((n, n))

        for i in range(n):

            H[i, i] = 2 * t + self.V[i] * self.q

            if i > 0:
                H[i, i - 1] = -t

            if i < n - 1:
                H[i, i + 1] = -t

        return H

    # ======================================================
    # Solve Schrödinger Equation
    # ======================================================

    def solve(self):
        """
        Solve eigenvalue problem.

        Returns
        -------
        energies : ndarray
            Energy eigenvalues (eV)

        wavefunctions : ndarray
            Normalized eigenfunctions
        """

        H = self.build_hamiltonian()

        energies, psi = eigh(H)

        energies = energies / self.q

        # Normalize wavefunctions
        for i in range(psi.shape[1]):

            norm = np.sqrt(
                np.trapz(
                    np.abs(psi[:, i]) ** 2,
                    self.z
                )
            )

            if norm != 0:
                psi[:, i] /= norm

        return energies, psi

    # ======================================================
    # Ground State
    # ======================================================

    def ground_state(self):

        energies, psi = self.solve()

        return energies[0], psi[:, 0]

    # ======================================================
    # First Excited State
    # ======================================================

    def first_excited_state(self):

        energies, psi = self.solve()

        return energies[1], psi[:, 1]

    # ======================================================
    # Transition Energy
    # ======================================================

    def transition_energy(self):

        energies, _ = self.solve()

        if len(energies) < 2:
            return 0.0

        return energies[1] - energies[0]