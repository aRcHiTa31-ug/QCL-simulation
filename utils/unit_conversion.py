"""
Utility functions for unit conversion.
"""

from physics_engine.constants import ELECTRON_CHARGE


def nm_to_m(value):
    """Convert nanometers to meters."""
    return value * 1e-9


def m_to_nm(value):
    """Convert meters to nanometers."""
    return value * 1e9


def um_to_m(value):
    """Convert micrometers to meters."""
    return value * 1e-6


def m_to_um(value):
    """Convert meters to micrometers."""
    return value * 1e6


def ev_to_joule(value):
    """Convert electron volts to Joules."""
    return value * ELECTRON_CHARGE


def joule_to_ev(value):
    """Convert Joules to electron volts."""
    return value / ELECTRON_CHARGE


def celsius_to_kelvin(value):
    """Convert Celsius to Kelvin."""
    return value + 273.15


def kelvin_to_celsius(value):
    """Convert Kelvin to Celsius."""
    return value - 273.15