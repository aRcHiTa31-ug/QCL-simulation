"""
Input validation utilities.
"""


def validate_positive(value, name):
    """
    Ensure a value is positive.
    """

    if value <= 0:
        raise ValueError(f"{name} must be positive.")

    return value


def validate_non_negative(value, name):
    """
    Ensure a value is non-negative.
    """

    if value < 0:
        raise ValueError(f"{name} cannot be negative.")

    return value


def validate_probability(value):
    """
    Validate probability.
    """

    if value < 0 or value > 1:
        raise ValueError(
            "Probability must be between 0 and 1."
        )

    return value