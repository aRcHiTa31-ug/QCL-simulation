"""
gas_database.py

Database of gases for the
QCL Gas Sensing module.
"""

# ==========================================================
# Gas Database
#
# Values are approximate and can be updated later with
# experimental/spectroscopic data.
# ==========================================================

GAS_DATABASE = {

    "CH4": {
        "name": "Methane",
        "formula": "CH₄",
        "absorption_coefficient": 0.82,
        "peak_wavelength": 7.66,      # μm
        "molecular_weight": 16.04,
        "color": "orange"
    },

    "CO2": {
        "name": "Carbon Dioxide",
        "formula": "CO₂",
        "absorption_coefficient": 1.12,
        "peak_wavelength": 4.26,
        "molecular_weight": 44.01,
        "color": "green"
    },

    "CO": {
        "name": "Carbon Monoxide",
        "formula": "CO",
        "absorption_coefficient": 0.73,
        "peak_wavelength": 4.67,
        "molecular_weight": 28.01,
        "color": "red"
    },

    "NH3": {
        "name": "Ammonia",
        "formula": "NH₃",
        "absorption_coefficient": 0.94,
        "peak_wavelength": 10.34,
        "molecular_weight": 17.03,
        "color": "blue"
    },

    "NO2": {
        "name": "Nitrogen Dioxide",
        "formula": "NO₂",
        "absorption_coefficient": 0.88,
        "peak_wavelength": 6.20,
        "molecular_weight": 46.01,
        "color": "purple"
    },

    "SO2": {
        "name": "Sulfur Dioxide",
        "formula": "SO₂",
        "absorption_coefficient": 1.05,
        "peak_wavelength": 7.34,
        "molecular_weight": 64.07,
        "color": "brown"
    },

    "N2O": {
        "name": "Nitrous Oxide",
        "formula": "N₂O",
        "absorption_coefficient": 0.91,
        "peak_wavelength": 4.52,
        "molecular_weight": 44.01,
        "color": "cyan"
    }

}


# ==========================================================
# Get Gas Information
# ==========================================================

def get_gas(gas_name):
    """
    Return gas properties.
    """

    if gas_name not in GAS_DATABASE:
        raise ValueError(
            f"Gas '{gas_name}' not found in database."
        )

    return GAS_DATABASE[gas_name]


# ==========================================================
# List Available Gases
# ==========================================================

def list_gases():
    """
    Return all available gases.
    """

    return list(GAS_DATABASE.keys())


# ==========================================================
# Check Gas Availability
# ==========================================================

def gas_exists(gas_name):
    """
    Check whether a gas exists.
    """

    return gas_name in GAS_DATABASE