"""
equations.py

Noise equations for the
QCL Simulator Dashboard.
"""

NOISE_EQUATIONS = {

# ==========================================================
# Gaussian Noise
# ==========================================================

"Gaussian Noise":
r"""
y_{noise}=y+\mathcal{N}(0,\sigma^2)
""",


# ==========================================================
# Signal-to-Noise Ratio (Linear)
# ==========================================================

"Signal-to-Noise Ratio":
r"""
SNR=\frac{P_{signal}}{P_{noise}}
""",


# ==========================================================
# Signal-to-Noise Ratio (dB)
# ==========================================================

"Signal-to-Noise Ratio (dB)":
r"""
SNR_{dB}=10\log_{10}
\left(
\frac{P_{signal}}
{P_{noise}}
\right)
""",


# ==========================================================
# Relative Intensity Noise (Linear)
# ==========================================================

"Relative Intensity Noise":
r"""
RIN=
\frac{
\langle(\Delta P)^2\rangle
}
{P^2}
""",


# ==========================================================
# Relative Intensity Noise (dB/Hz)
# ==========================================================

"Relative Intensity Noise (dB/Hz)":
r"""
RIN_{dB/Hz}
=
10\log_{10}(RIN)
""",


# ==========================================================
# Noise Power
# ==========================================================

"Noise Power":
r"""
P_{noise}=P_{signal}-P_{ideal}
""",


# ==========================================================
# Standard Deviation
# ==========================================================

"Noise Standard Deviation":
r"""
\sigma=
\sqrt{
\frac{
\sum(x_i-\mu)^2
}
{N}
}
""",


# ==========================================================
# Noise Variance
# ==========================================================

"Noise Variance":
r"""
\sigma^2=
\frac{
\sum(x_i-\mu)^2
}
{N}
"""

}