"""
reliability_graph.py

Visualization of Reliability
for the Quantum Cascade Laser Simulator.
"""

import numpy as np
import matplotlib.pyplot as plt

from physics_engine.physics_engine import PhysicsEngine


# ==========================================================
# Reliability Function vs Operating Time
# ==========================================================

def plot_reliability(
        mean_time_to_failure,
        max_time,
        points=200):
    """
    Reliability Function R(t) vs Operating Time.
    """

    operating_time = np.linspace(
        0,
        max_time,
        points
    )

    reliability = [
        PhysicsEngine.calculate_reliability_function(
            operating_time=t,
            mean_time_to_failure=mean_time_to_failure
        )
        for t in operating_time
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        operating_time,
        reliability,
        linewidth=2.5,
        color="royalblue",
        label="Reliability"
    )

    ax.set_title("Reliability Function")

    ax.set_xlabel("Operating Time (hours)")

    ax.set_ylabel("Reliability R(t)")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Failure Probability vs Operating Time
# ==========================================================

def plot_failure_probability(
        mean_time_to_failure,
        max_time,
        points=200):
    """
    Failure Probability F(t) vs Operating Time.
    """

    operating_time = np.linspace(
        0,
        max_time,
        points
    )

    failure_probability = [
        PhysicsEngine.calculate_failure_probability(
            operating_time=t,
            mean_time_to_failure=mean_time_to_failure
        )
        for t in operating_time
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        operating_time,
        failure_probability,
        linewidth=2,
        color="crimson",
        label="Failure Probability"
    )

    ax.set_title("Failure Probability")

    ax.set_xlabel("Operating Time (hours)")

    ax.set_ylabel("Failure Probability")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Arrhenius Acceleration Factor
# ==========================================================

def plot_arrhenius_factor(
        activation_energy,
        use_temperature,
        stress_temperature_max,
        points=200):
    """
    Arrhenius Acceleration Factor vs Stress Temperature.
    """

    stress_temperature = np.linspace(
        use_temperature + 1,
        stress_temperature_max,
        points
    )

    acceleration_factor = [
        PhysicsEngine.calculate_arrhenius_factor(
            activation_energy=activation_energy,
            use_temperature=use_temperature,
            stress_temperature=t
        )
        for t in stress_temperature
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        stress_temperature,
        acceleration_factor,
        linewidth=2,
        color="darkgreen",
        label="Acceleration Factor"
    )

    ax.set_title("Arrhenius Acceleration Factor")

    ax.set_xlabel("Stress Temperature (K)")

    ax.set_ylabel("Acceleration Factor")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Black's Equation
# ==========================================================

def plot_blacks_equation(
        constant_A,
        exponent_n,
        activation_energy,
        temperature,
        current_density_max,
        points=200):
    """
    Black's Equation vs Current Density.
    """

    current_density = np.linspace(
        1e3,
        current_density_max,
        points
    )

    mttf = [
        PhysicsEngine.calculate_blacks_equation(
            constant_A=constant_A,
            current_density=j,
            exponent_n=exponent_n,
            activation_energy=activation_energy,
            temperature=temperature
        )
        for j in current_density
    ]

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        current_density,
        mttf,
        linewidth=2,
        color="darkorange",
        label="Black's Equation"
    )

    ax.set_title("Mean Time To Failure (Black's Equation)")

    ax.set_xlabel("Current Density (A/m²)")

    ax.set_ylabel("MTTF")

    ax.grid(True)

    ax.legend()

    fig.tight_layout()

    return fig


# ==========================================================
# Peak Reliability
# ==========================================================

def calculate_peak_reliability(
        mean_time_to_failure,
        max_time,
        points=200):
    """
    Returns maximum reliability.
    """

    operating_time = np.linspace(
        0,
        max_time,
        points
    )

    reliability = [
        PhysicsEngine.calculate_reliability_function(
            operating_time=t,
            mean_time_to_failure=mean_time_to_failure
        )
        for t in operating_time
    ]

    return np.max(reliability)