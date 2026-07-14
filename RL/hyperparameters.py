"""
hyperparameters.py

Hyperparameters for the
QCL Reinforcement Learning module.
"""

# ==========================================================
# Q-Learning Parameters
# ==========================================================

LEARNING_RATE = 0.10

DISCOUNT_FACTOR = 0.95

EPSILON = 1.0

EPSILON_DECAY = 0.995

EPSILON_MIN = 0.01


# ==========================================================
# Training Parameters
# ==========================================================

NUM_EPISODES = 500

MAX_STEPS = 200


# ==========================================================
# Environment Parameters
# ==========================================================

CURRENT_MIN = 0.5
CURRENT_MAX = 2.0

VOLTAGE_MIN = 5.0
VOLTAGE_MAX = 15.0

TEMPERATURE_MIN = 280.0
TEMPERATURE_MAX = 380.0

CASCADE_STAGE_MIN = 10
CASCADE_STAGE_MAX = 40


# ==========================================================
# Action Step Sizes
# ==========================================================

CURRENT_STEP = 0.05

VOLTAGE_STEP = 0.10

TEMPERATURE_STEP = 2.0

STAGE_STEP = 1


# ==========================================================
# Reward Parameters
# ==========================================================

POWER_WEIGHT = 1.0

GAIN_WEIGHT = 0.8

EFFICIENCY_WEIGHT = 1.2

TEMPERATURE_PENALTY = 0.5

THRESHOLD_PENALTY = 0.5


# ==========================================================
# Random Seed
# ==========================================================

RANDOM_SEED = 42