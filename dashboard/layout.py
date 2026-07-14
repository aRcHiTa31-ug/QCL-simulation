# dashboard/layout.py

import streamlit as st


def render_layout(metrics: dict):

    tabs = st.tabs(["📚 Equations"])

    with tabs[0]:

        st.title("📚 Quantum Cascade Laser Simulator Equations")
        st.caption("Reference equations used throughout the simulator.")

        col1, col2, col3 = st.columns(3)

        # =====================================================
        # COLUMN 1
        # =====================================================

        with col1:

            st.subheader("⚡ Electrical")

            st.latex(r"J=\frac{I}{A}")

            st.latex(r"E=\frac{V}{L}")

            st.latex(r"P_{elec}=VI")

            st.latex(r"P_{diss}=VI-P_{opt}")

            st.latex(r"P_{density}=\frac{P}{A}")

            st.divider()

            st.subheader("🔬 Optical Gain")

            st.latex(r"\Delta N=N_u-N_l")

            st.latex(r"g=\sigma(N_u-N_l)")

            st.latex(r"g_{th}=\alpha_i+\alpha_m")

            st.latex(r"P_{out}=\eta_s(I-I_{th})")

            st.latex(r"\eta_o=\frac{P_{out}}{P_{elec}}")

            st.latex(r"\eta_{wp}=\frac{P_{out}}{VI}")

            st.latex(r"\eta_i=\frac{g}{g+\alpha_i}")

            st.latex(r"\eta_e=\frac{\alpha_m}{\alpha_i+\alpha_m}")

            st.divider()

            st.subheader("🌡 Thermal")

            st.latex(r"\Delta T=R_{th}P_{diss}")

            st.latex(r"T_{device}=T_{ambient}+\Delta T")

            st.latex(r"G_{th}=\frac{1}{R_{th}}")

            st.latex(r"Q=mc\Delta T")

            st.latex(r"q=-k\nabla T")

        # =====================================================
        # COLUMN 2
        # =====================================================

        with col2:

            st.subheader("🌈 Optical Properties")

            st.latex(r"E=\frac{hc}{\lambda}")

            st.latex(r"\lambda=\frac{hc}{E}")

            st.latex(r"f=\frac{c}{\lambda}")

            st.latex(r"k=\frac{2\pi}{\lambda}")

            st.latex(r"p=\frac{h}{\lambda}")

            st.divider()

            st.subheader("🧪 Gas Sensing")

            st.latex(r"I=I_0e^{-\alpha cL}")

            st.latex(r"T=\frac{I}{I_0}")

            st.latex(r"A=-\log_{10}(T)")

            st.latex(r"c=\frac{A}{\alpha L}")

            st.latex(r"LOD=\frac{3\sigma}{\alpha L}")

            st.latex(r"P=\frac{Power}{Area}")

            st.divider()

            st.subheader("📈 Noise")

            st.latex(r"i_n=\sqrt{2qI\Delta f}")

            st.latex(r"v_n=\sqrt{4kTR\Delta f}")

            st.latex(r"RIN=\frac{\delta P^2}{P^2\Delta f}")

            st.latex(r"SNR=\frac{P_{signal}}{\sigma}")

            st.latex(r"\sigma=\sqrt{\sigma_1^2+\sigma_2^2+\sigma_3^2}")

            st.latex(r"N(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}")

        # =====================================================
        # COLUMN 3
        # =====================================================

        with col3:

            st.subheader("⚛ Energy Structure")

            st.latex(r"-\frac{\hbar^2}{2m}\nabla^2\psi+V\psi=E\psi")

            st.latex(r"E_n=\frac{n^2h^2}{8mL^2}")

            st.latex(r"\Delta E=E_u-E_l")

            st.latex(r"\lambda=\frac{hc}{\Delta E}")

            st.latex(r"\int |\psi|^2dx=1")

            st.latex(r"T=e^{-2\kappa L}")

            st.divider()

            st.subheader("📊 Reliability")

            st.latex(r"AF=e^{\frac{E_a}{k}\left(\frac1{T_r}-\frac1T\right)}")

            st.latex(r"MTTF=\frac{A}{J^n}e^{\frac{E_a}{kT}}")

            st.latex(r"R(t)=e^{-t/MTTF}")

            st.latex(r"F(t)=1-e^{-t/MTTF}")

            st.divider()

            st.subheader("🤖 Reinforcement Learning")

            st.latex(r"G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}")

            st.latex(r"V(s)=\mathbb{E}[R+\gamma V(s')]")

            st.latex(r"Q(s,a)=R+\gamma\max Q(s',a')")

            st.latex(r"Q\leftarrow Q+\alpha[r+\gamma\max Q'-Q]")

            st.latex(r"\delta=r+\gamma\max Q'-Q")

            st.latex(r"\epsilon\text{-Greedy}")

            st.latex(r"A(s,a)=Q(s,a)-V(s)")

            st.latex(r"L=(y-Q)^2")

            st.latex(r"\nabla_\theta J=\mathbb{E}[\nabla_\theta\log\pi(a|s)G_t]")

            st.latex(r"L^{CLIP}=E[\min(rA,\mathrm{clip}(r)A)]")