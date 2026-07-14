"""
visualization/spectrum.py

Optical spectrum visualization for the
Quantum Cascade Laser Simulator.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_spectrum(
        wavelength,
        intensity,
        normalize=False,
        title="QCL Emission Spectrum"):
    """
    Plot the optical emission spectrum.

    Parameters
    ----------
    wavelength : array-like
        Wavelength values (µm)

    intensity : array-like
        Optical intensity values

    normalize : bool
        Normalize intensity to unity.

    title : str
        Plot title.

    Returns
    -------
    matplotlib.figure.Figure
    """

    wavelength = np.asarray(wavelength)
    intensity = np.asarray(intensity)

    if wavelength.size != intensity.size:
        raise ValueError(
            "wavelength and intensity must have the same length."
        )

    if normalize:
        maximum = np.max(intensity)
        if maximum > 0:
            intensity = intensity / maximum

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        wavelength,
        intensity,
        color="navy",
        linewidth=2.5
    )

    peak_index = np.argmax(intensity)
    peak_wavelength = wavelength[peak_index]
    peak_intensity = intensity[peak_index]

    ax.scatter(
        peak_wavelength,
        peak_intensity,
        color="red",
        zorder=5,
        s=40,
    )

    # Give the plot headroom above the peak. Previously the y-axis
    # topped out at exactly the peak value (1.0 when normalized), so
    # the peak sat flush against the title with no room for the
    # annotation - this is what caused the label to visually collide
    # with the title in the original plot.
    y_max = np.max(intensity)
    y_min = min(np.min(intensity), 0)
    headroom = (y_max - y_min) * 0.30
    ax.set_ylim(y_min, y_max + headroom)

    ax.annotate(
        f"Peak: {peak_wavelength:.2f} μm",
        xy=(peak_wavelength, peak_intensity),
        xytext=(0, 40),
        textcoords="offset points",
        fontsize=11,
        fontweight="bold",
        ha="center",
        arrowprops=dict(
            arrowstyle="->",
            color="black",
            linewidth=1.3,
        ),
        bbox=dict(
            boxstyle="round,pad=0.35",
            facecolor="white",
            edgecolor="red",
            linewidth=1.2,
            alpha=0.95,
        ),
    )

    ax.set_title(title, fontsize=13, fontweight="bold", pad=14)
    ax.set_xlabel("Wavelength (μm)", fontsize=11)
    ax.set_ylabel("Intensity (a.u.)", fontsize=11)
    ax.tick_params(axis="both", labelsize=10)

    ax.grid(alpha=0.3)

    fig.tight_layout()

    return fig


def generate_gaussian_spectrum(
        center_wavelength,
        fwhm,
        wavelength_min=None,
        wavelength_max=None,
        points=1000):
    """
    Generate a Gaussian emission spectrum.

    Parameters
    ----------
    center_wavelength : float
        Peak wavelength (µm)

    fwhm : float
        Full Width at Half Maximum (µm)

    wavelength_min : float, optional

    wavelength_max : float, optional

    points : int

    Returns
    -------
    tuple
        wavelength, intensity
    """

    if wavelength_min is None:
        wavelength_min = center_wavelength - 1.0

    if wavelength_max is None:
        wavelength_max = center_wavelength + 1.0

    wavelength = np.linspace(
        wavelength_min,
        wavelength_max,
        points
    )

    sigma = fwhm / 2.355

    intensity = np.exp(
        -((wavelength - center_wavelength) ** 2) /
        (2 * sigma ** 2)
    )

    return wavelength, intensity


def plot_gaussian_spectrum(
        center_wavelength,
        fwhm=0.20):
    """
    Convenience function for plotting a
    Gaussian QCL spectrum.

    Parameters
    ----------
    center_wavelength : float
        Peak wavelength (µm)

    fwhm : float
        Spectral width (µm)

    Returns
    -------
    matplotlib.figure.Figure
    """

    wavelength, intensity = generate_gaussian_spectrum(
        center_wavelength=center_wavelength,
        fwhm=fwhm
    )

    return plot_spectrum(
        wavelength,
        intensity,
        normalize=True,
        title=f"QCL Spectrum ({center_wavelength:.2f} μm)"
    )