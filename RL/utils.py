"""
utils.py

Utility functions for the
QCL Reinforcement Learning module.
"""

import os
import random
import numpy as np


# ==========================================================
# Random Seed
# ==========================================================

def set_random_seed(seed: int):
    """
    Set random seed for reproducibility.
    """
    random.seed(seed)
    np.random.seed(seed)


# ==========================================================
# Create Directory
# ==========================================================

def create_directory(path: str):
    """
    Create a directory if it does not exist.
    """
    os.makedirs(path, exist_ok=True)


# ==========================================================
# Normalize Value
# ==========================================================

def normalize(value, minimum, maximum):
    """
    Normalize a value between 0 and 1.
    """
    if maximum == minimum:
        return 0.0

    return (value - minimum) / (maximum - minimum)


# ==========================================================
# Clip Value
# ==========================================================

def clip(value, minimum, maximum):
    """
    Restrict a value to a specified range.
    """
    return max(minimum, min(value, maximum))


# ==========================================================
# Moving Average
# ==========================================================

def moving_average(values, window=10):
    """
    Compute moving average.
    """
    if len(values) < window:
        return np.array(values)

    return np.convolve(
        values,
        np.ones(window) / window,
        mode="valid"
    )


# ==========================================================
# Training Statistics
# ==========================================================

def print_training_summary(rewards):
    """
    Print summary statistics after training.
    """
    if len(rewards) == 0:
        print("No training statistics available.")
        return

    print("\n========== Training Summary ==========")
    print(f"Episodes      : {len(rewards)}")
    print(f"Average Reward: {np.mean(rewards):.2f}")
    print(f"Best Reward   : {np.max(rewards):.2f}")
    print(f"Worst Reward  : {np.min(rewards):.2f}")
    print("======================================")