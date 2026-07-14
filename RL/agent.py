"""
agent.py
Q-Learning Agent for the
QCL Reinforcement Learning module.
"""
import pickle
import random
from typing import Sequence, Tuple, Union

import numpy as np
from RL.action import Action

class QLearningAgent:
    """
    Tabular Q-Learning Agent with epsilon-greedy exploration.
    """

    def __init__(
        self,
        state_size: int,
        action_size: int,
        learning_rate: float = 0.1,
        discount_factor: float = 0.95,
        epsilon: float = 1.0,
        epsilon_decay: float = 0.995,
        epsilon_min: float = 0.01,
        state_precision: int = 4,
        seed: int = None,
    ):
        """
        Args:
            state_size: Number of features in a state vector.
            action_size: Number of discrete actions available.
            learning_rate: Q-value update step size, in [0, 1].
            discount_factor: Future reward discount, in [0, 1].
            epsilon: Initial exploration probability, in [0, 1].
            epsilon_decay: Multiplicative decay applied per episode/step.
            epsilon_min: Floor for epsilon after decay.
            state_precision: Decimal places to round continuous state
                values to before using them as a dict key. This matters
                a lot for physical/continuous states (e.g. current,
                voltage, temperature) - without rounding, two states
                that differ by floating point noise are treated as
                completely unrelated entries in the Q-table, so the
                agent effectively never revisits a state and never
                really learns. Set to None to disable rounding.
            seed: Optional random seed for reproducibility.
        """
        if state_size <= 0:
            raise ValueError("state_size must be a positive integer.")
        if action_size <= 0:
            raise ValueError("action_size must be a positive integer.")
        if not 0 < learning_rate <= 1:
            raise ValueError("learning_rate must be in (0, 1].")
        if not 0 <= discount_factor <= 1:
            raise ValueError("discount_factor must be in [0, 1].")
        if not 0 <= epsilon <= 1:
            raise ValueError("epsilon must be in [0, 1].")
        if not 0 < epsilon_decay <= 1:
            raise ValueError("epsilon_decay must be in (0, 1].")
        if not 0 <= epsilon_min <= 1:
            raise ValueError("epsilon_min must be in [0, 1].")

        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.initial_epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.state_precision = state_precision

        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

        # Q-table: maps state tuple -> np.ndarray of shape (action_size)
        self.q_table = {}

    # ---------------------------------------------------
    # Normalize + register state
    # ---------------------------------------------------
    def _check_state(self, state: Sequence[float]) -> Tuple[float, ...]:
        """
        Convert a state vector into a hashable, precision-limited
        tuple key, and ensure it has an entry in the Q-table.
        """
        if len(state) != self.state_size:
            raise ValueError(
                f"Expected state of length {self.state_size}, "
                f"got {len(state)}."
            )

        if self.state_precision is not None:
            state = tuple(round(float(s), self.state_precision) for s in state)
        else:
            state = tuple(state)

        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.action_size, dtype=float)
        return state

    def _check_action(self, action: int) -> int:
        """Validate that an action index is within bounds."""
        action = int(action)
        if not 0 <= action < self.action_size:
            raise ValueError(
                f"action {action} is out of range "
                f"[0, {self.action_size - 1}]."
            )
        return action

    # ---------------------------------------------------
    # Select Action (epsilon-Greedy)
    # ---------------------------------------------------
    def choose_action(self, state: Sequence[float]) -> int:
        """
        Select an action using epsilon-greedy exploration.
        """
        state = self._check_state(state)
        if random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)
        return int(np.argmax(self.q_table[state]))

    # ---------------------------------------------------
    # Learn
    # ---------------------------------------------------
    def learn(
        self,
        state: Sequence[float],
        action: Union[int, "Action"],
        reward: float,
        next_state: Sequence[float],
        done: bool,
    ) -> None:
        """
        Update the Q-value for (state, action) using the observed
        reward and next state.
        """
        state = self._check_state(state)
        action = self._check_action(action)
        next_state = self._check_state(next_state)

        current_q = self.q_table[state][action]
        if done:
            target = reward
        else:
            target = reward + self.discount_factor * np.max(
                self.q_table[next_state]
            )

        self.q_table[state][action] += self.learning_rate * (target - current_q)

    # ---------------------------------------------------
    # Update Exploration Rate
    # ---------------------------------------------------
    def decay_epsilon(self) -> None:
        """Decay epsilon toward epsilon_min."""
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    # ---------------------------------------------------
    # Predict Best Action (no exploration)
    # ---------------------------------------------------
    def predict(self, state: Sequence[float]) -> int:
        """
        Return the greedy (best known) action for a state,
        with no exploration.
        """
        state = self._check_state(state)
        return int(np.argmax(self.q_table[state]))

    # ---------------------------------------------------
    # Q-value inspection
    # ---------------------------------------------------
    def get_q_values(self, state: Sequence[float]) -> np.ndarray:
        """Return a copy of the Q-values for a given state."""
        state = self._check_state(state)
        return self.q_table[state].copy()

    # ---------------------------------------------------
    # Persistence
    # ---------------------------------------------------
    def save(self, filepath: str) -> None:
        """Save the Q-table and hyperparameters to disk."""
        with open(filepath, "wb") as f:
            pickle.dump(
                {
                    "q_table": self.q_table,
                    "epsilon": self.epsilon,
                    "state_size": self.state_size,
                    "action_size": self.action_size,
                },
                f,
            )

    def load(self, filepath: str) -> None:
        """Load a previously saved Q-table and hyperparameters."""
        with open(filepath, "rb") as f:
            data = pickle.load(f)

        if data["state_size"] != self.state_size:
            raise ValueError(
                f"Loaded state_size ({data['state_size']}) does not "
                f"match agent's state_size ({self.state_size})."
            )
        if data["action_size"] != self.action_size:
            raise ValueError(
                f"Loaded action_size ({data['action_size']}) does not "
                f"match agent's action_size ({self.action_size})."
            )

        self.q_table = data["q_table"]
        self.epsilon = data["epsilon"]

    # ---------------------------------------------------
    # Reset
    # ---------------------------------------------------
    def reset(self) -> None:
        """Clear the Q-table and restore initial epsilon."""
        self.q_table.clear()
        self.epsilon = self.initial_epsilon