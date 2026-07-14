def calculate_intersubband_transition(
    upper_energy,
    lower_energy
):
    """
    Calculates the intersubband transition energy.

    ΔE = E_upper - E_lower

    Parameters
    ----------
    upper_energy : float
        Upper energy level (eV)

    lower_energy : float
        Lower energy level (eV)

    Returns
    -------
    float
        Transition energy (eV)
    """

    return upper_energy - lower_energy