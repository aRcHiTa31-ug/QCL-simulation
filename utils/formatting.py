"""
Formatting helper functions.
"""


def format_energy(value):
    return f"{value:.4f} eV"


def format_voltage(value):
    return f"{value:.2f} V"


def format_current(value):
    return f"{value:.3f} A"


def format_temperature(value):
    return f"{value:.1f} K"


def format_wavelength(value):
    return f"{value:.2f} μm"


def format_percentage(value):
    return f"{value:.2f} %"