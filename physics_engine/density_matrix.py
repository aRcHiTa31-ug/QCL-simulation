"""
physics/density_matrix.py

Density Matrix Utilities
for Quantum Cascade Lasers

Implements

1. Density Matrix
2. Population Extraction
3. Coherence Extraction
4. Trace
5. Normalization
"""

import numpy as np


class DensityMatrix:

    def __init__(self, num_states):

        self.num_states = num_states

        self.rho = np.zeros(
            (num_states, num_states),
            dtype=np.complex128
        )

    # --------------------------------------------------

    def set_population(
        self,
        state,
        population
    ):

        self.rho[state, state] = population

    # --------------------------------------------------

    def set_coherence(
        self,
        state1,
        state2,
        coherence
    ):

        self.rho[state1, state2] = coherence

        self.rho[state2, state1] = np.conjugate(
            coherence
        )

    # --------------------------------------------------

    def population(
        self,
        state
    ):

        return np.real(
            self.rho[state, state]
        )

    # --------------------------------------------------

    def coherence(
        self,
        state1,
        state2
    ):

        return self.rho[state1, state2]

    # --------------------------------------------------

    def trace(self):

        return np.trace(
            self.rho
        )

    # --------------------------------------------------

    def normalize(self):

        tr = self.trace()

        if np.abs(tr) > 0:

            self.rho /= tr

    # --------------------------------------------------

    def matrix(self):

        return self.rho.copy()

    # --------------------------------------------------

    def clear(self):

        self.rho[:] = 0


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    dm = DensityMatrix(3)

    dm.set_population(0, 0.65)

    dm.set_population(1, 0.30)

    dm.set_population(2, 0.05)

    dm.set_coherence(
        0,
        1,
        0.02 + 0.01j
    )

    print()

    print("Density Matrix")

    print(dm.matrix())

    print()

    print("Trace")

    print(dm.trace())

    dm.normalize()

    print()

    print("Normalized Matrix")

    print(dm.matrix())