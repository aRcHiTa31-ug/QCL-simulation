"""
equations.py

Stores all QCL Physics Engine equations in LaTeX format.
Used by the Dashboard -> Equations tab.
"""

PHYSICS_EQUATIONS = {

# =====================================================
# CURRENT & VOLTAGE
# =====================================================

"Current Density":
r"J=\frac{I}{A}",

"Electric Field":
r"E=\frac{V}{L}",


# =====================================================
# GAIN
# =====================================================

"Optical Gain":
r"g=\Gamma g_0 (N-N_{tr})",


# =====================================================
# POPULATION
# =====================================================

"Population Inversion":
r"\Delta N=N_2-N_1",


# =====================================================
# THRESHOLD
# =====================================================

"Threshold Gain":
r"g_{th}=\frac{\alpha_i+\alpha_m}{\Gamma}",

"Threshold Current Density":
r"J_{th}=J_0e^{T/T_0}",


# =====================================================
# POWER
# =====================================================

"Output Power":
r"P_{out}=\eta_s(I-I_{th})",

"Dissipated Power":
r"P_{diss}=VI-P_{out}",

"Slope Efficiency":
r"\eta_s=\frac{\Delta P}{\Delta I}",

"Power Density":
r"PD=\frac{P}{A}",

"Brightness":
r"B=\frac{P}{A\Omega}",

"Voltage Defect":
r"V_{def}=\frac{E_{ph}}{qV}",

"Cascade Voltage":
r"V_{cascade}=N_{stage}V_{stage}",


# =====================================================
# EFFICIENCY
# =====================================================

"Optical Efficiency":
r"\eta_{opt}=\frac{P_{out}}{P_{in}}",

"Wall Plug Efficiency":
r"\eta_{wp}=\frac{P_{out}}{VI}",

"Internal Quantum Efficiency":
r"\eta_i=\frac{g}{g+\alpha_i}",

"External Quantum Efficiency":
r"\eta_{ext}=\eta_i\frac{\alpha_m}{\alpha_i+\alpha_m}",

"Differential Quantum Efficiency":
r"\eta_d=\frac{dP}{dI}",

"Injection Efficiency":
r"\eta_{inj}=\frac{I_{active}}{I_{total}}",

"Extraction Efficiency":
r"\eta_{extract}=\frac{P_{out}}{P_{generated}}",


# =====================================================
# TEMPERATURE
# =====================================================

"Thermal Resistance":
r"R_{th}=\frac{\Delta T}{P_{diss}}",

"Temperature Rise":
r"\Delta T=P_{diss}R_{th}",

"Device Temperature":
r"T_{device}=T_{ambient}+\Delta T",

"Thermal Conductivity":
r"k=\frac{QL}{A\Delta T}",

"Self Heating":
r"P_{heat}=VI-P_{out}",

"Temperature Dependent Threshold":
r"I_{th}(T)=I_0e^{T/T_0}",


# =====================================================
# WAVELENGTH
# =====================================================

"Wavelength":
r"\lambda=\frac{hc}{E}",

"Frequency":
r"f=\frac{c}{\lambda}",

"Wavenumber":
r"\tilde{\nu}=\frac1{\lambda}",

"Photon Momentum":
r"p=\frac{h}{\lambda}",


# =====================================================
# ENERGY BAND
# =====================================================

"Energy Level":
r"E_n=\frac{n^2h^2}{8mL^2}",

"Transition Energy":
r"\Delta E=E_u-E_l",

"Photon Energy":
r"E=hf",

"Frequency from Energy":
r"f=\frac{E}{h}",

"Transition Wavelength":
r"\lambda=\frac{hc}{\Delta E}",

"Energy Difference":
r"\Delta E=E_2-E_1",


# =====================================================
# CASCADE STAGE
# =====================================================

"Total Active Region Thickness":
r"L=N_{stage}L_{stage}",

"Total Cascade Voltage":
r"V=N_{stage}V_{stage}",

"Total Gain":
r"G=N_{stage}g_{stage}",

"Total Output Power":
r"P=N_{stage}P_{stage}",


# =====================================================
# PERFORMANCE
# =====================================================

"Beam Divergence":
r"\theta=\frac{\lambda}{\pi w_0}",

"Spectral Linewidth":
r"\Delta\nu=\frac1{2\pi\tau}",

"Characteristic Temperature":
r"I_{th}=I_0e^{T/T_0}",

"Optical Frequency":
r"f=\frac{c}{\lambda}",

"Active Region Thickness":
r"d=N_{stage}d_{stage}",

"Figure of Merit":
r"FOM=\frac{P_{out}}{P_{diss}}",


# =====================================================
# RELIABILITY
# =====================================================

"Arrhenius Factor":
r"AF=e^{-E_a/(kT)}",

"Mean Time To Failure":
r"MTTF=Ae^{E_a/(kT)}",

"Black's Equation":
r"MTTF=AJ^{-n}e^{E_a/(kT)}",

"Reliability Function":
r"R(t)=e^{-t/MTTF}",

"Failure Probability":
r"F(t)=1-R(t)"

}