# dashboard/sidebar.py

import streamlit as st
from typing import TypedDict


# Defaults tuned for a 4.5 µm mid-IR QCL, based on:
#   - Pierscinska et al., Materials 14, 7352 (2021)   [4.5 µm, primary source]
#   - Lyakh et al., Appl. Phys. Lett. 92, 111110 (2008) [4.6 µm, strain-balanced]
#   - Soleimanikahnoj et al., arXiv:1710.08870          [4.6 µm density-matrix sim]
DEFAULTS = {
    "current": 1000.0,         # mA — above derived threshold of ~830-960 mA
                                # (Materials 2021: Jth 2.75-3.20 kA/cm^2, ~15 um x 2 mm ridge)
    "voltage": 13.0,           # V — read from L-I-V curve near 1 A (Materials 2021, Fig. 2)
    "temperature": 300,        # K — room-temperature operation (all sources)
    "well_width": 4.3,         # nm — widest well in the 11-pair sequence (Materials 2021)
    "barrier_width": 3.8,      # nm — injection barrier, thickest in sequence (Materials 2021)
    "cascade_stages": 50,      # Nc — 11 pairs x 50 repeats (Materials 2021)
                                # NOTE: Lyakh 2008 and Go et al. 2018 both use 40 stages
                                # for their 4.6 um designs -- 40 is a valid alternative.
    "doping": 4.0e17,          # cm^-3 — doped barrier layers (Materials 2021)
    "cavity_length": 2000,     # µm — 2 mm as-cleaved devices (Materials 2021)
    "enable_noise": False,
    "noise_level": 0.05,
    "noise_type": "Gaussian",
    "rl_algorithm": "PPO",
    "episodes": 1000,
    "learning_rate": 0.001,
    "gamma": 0.99,
}


class SidebarInputs(TypedDict):
    current: float
    voltage: float
    temperature: int
    well_width: float
    barrier_width: float
    cascade_stages: int
    doping: float
    cavity_length: int
    enable_noise: bool
    noise_level: float
    noise_type: str
    rl_algorithm: str
    episodes: int
    learning_rate: float
    gamma: float
    run_simulation: bool
    train_rl: bool
    export_results: bool
    reset_parameters: bool


def _reset_defaults():
    """Reset all widget values back to the 4.5 µm QCL literature defaults."""
    for key, value in DEFAULTS.items():
        st.session_state[key] = value


def render_sidebar() -> SidebarInputs:
    """Renders the left control panel and returns all user-selected inputs."""

    st.sidebar.title("⚛️ QCL Control Panel")
    st.sidebar.caption(
        "Defaults from Pierścińska et al. (Materials 2021, 4.5 µm) "
        "and Lyakh et al. (APL 2008, 4.6 µm)"
    )
    st.sidebar.markdown("---")

    # ==============================
    # Simulation Parameters
    # ==============================
    with st.sidebar.expander("Simulation Inputs", expanded=True):
        current = st.slider(
            "Current (mA)", 0.0, 1000.0, key="current", step=1.0,
            help="Derived threshold ~830-960 mA for a 2 mm x 15 µm ridge "
                 "(Materials 2021, Jth = 2.75-3.20 kA/cm^2).",
        )
        voltage = st.slider(
            "Voltage (V)", 0.0, 20.0, key="voltage", step=0.1,
            help="~13 V near 1 A operating point (Materials 2021, Fig. 2 L-I-V).",
        )
        temperature = st.slider(
            "Temperature (K)", 77, 500, key="temperature", step=1,
            help="Heat-sink / operating temperature.",
        )
        well_width = st.slider(
            "Quantum Well Width (nm)", 1.0, 20.0, key="well_width", step=0.1,
            help="4.3 nm = widest well in the Materials 2021 layer sequence.",
        )
        barrier_width = st.slider(
            "Barrier Width (nm)", 1.0, 15.0, key="barrier_width", step=0.1,
            help="3.8 nm = injection barrier thickness (Materials 2021).",
        )
        cascade_stages = st.slider(
            "Cascade Stages (Nc)", 5, 100, key="cascade_stages", step=1,
            help="50 stages (Materials 2021); 40 stages used in Lyakh 2008 / Go 2018.",
        )
        doping = st.number_input(
            "Doping Concentration (cm⁻³)",
            min_value=1e14, max_value=1e19, step=1e15,
            key="doping", format="%.2e",
            help="4.0e17 cm^-3 doped barrier layers (Materials 2021).",
        )
        cavity_length = st.number_input(
            "Cavity Length (µm)",
            min_value=100, max_value=10000, step=100,
            key="cavity_length",
            help="2 mm as-cleaved devices (Materials 2021).",
        )

    # ==============================
    # Noise Settings
    # ==============================
    with st.sidebar.expander("Noise Settings"):
        enable_noise = st.checkbox("Enable Noise", key="enable_noise")
        noise_level = st.slider(
            "Noise Level", 0.0, 1.0, step=0.01,
            key="noise_level", disabled=not enable_noise,
        )
        noise_type = st.selectbox(
            "Noise Type",
            ["Gaussian"],
            key="noise_type",
            disabled=not enable_noise
        )

    # ==============================
    # Reinforcement Learning
    # ==============================
    with st.sidebar.expander("RL Settings"):
        rl_algorithm = st.selectbox(
            "RL Algorithm",
            ["Q-Learning"],
            key="rl_algorithm",
        )
        episodes = st.number_input(
            "Episodes", min_value=100, max_value=100000, step=100,
            key="episodes",
        )
        learning_rate = st.number_input(
            "Learning Rate",
            min_value=0.00001, max_value=0.1, step=0.00001,
            key="learning_rate", format="%.5f",
        )
        gamma = st.slider(
            "Discount Factor (γ)", 0.80, 0.999, step=0.001, key="gamma",
        )

    st.sidebar.markdown("---")

    # ==============================
    # Action Buttons
    # ==============================
    # ==============================
    # Action Buttons
    # ==============================
    st.sidebar.subheader("Simulation Controls")

    # Persistent Run Simulation State
    if "run_simulation" not in st.session_state:
        st.session_state.run_simulation = False

    if st.sidebar.button("▶ Run Simulation", use_container_width=True):
        st.session_state.run_simulation = True

    run_simulation = st.session_state.run_simulation

    # Optional: Stop Simulation Button
    if run_simulation:
        if st.sidebar.button("⏹ Stop Simulation", use_container_width=True):
            st.session_state.run_simulation = False
            st.rerun()

    train_rl = st.sidebar.button(
        "🤖 Train RL Agent",
        use_container_width=True
    )

    export_results = st.sidebar.button(
        "📤 Export Results",
        use_container_width=True
    )

    reset_parameters = st.sidebar.button(
        "🔄 Reset Parameters",
        use_container_width=True,
        on_click=_reset_defaults,
    )

    st.sidebar.markdown("---")

    # ==============================
    # About
    # ==============================
    st.sidebar.subheader("About")
    st.sidebar.info(
        """
        **Quantum Cascade Laser Simulator**

        Physics-based QCL simulation with
        Reinforcement Learning optimization,
        thermal analysis, energy band
        visualization and benchmark validation.
        """
    )

    return {
        "current": current,
        "voltage": voltage,
        "temperature": temperature,
        "well_width": well_width,
        "barrier_width": barrier_width,
        "cascade_stages": cascade_stages,
        "doping": doping,
        "cavity_length": cavity_length,
        "enable_noise": enable_noise,
        "noise_level": noise_level,
        "noise_type": noise_type,
        "rl_algorithm": rl_algorithm,
        "episodes": episodes,
        "learning_rate": learning_rate,
        "gamma": gamma,
        "run_simulation": st.session_state.run_simulation,
        "train_rl": train_rl,
        "export_results": export_results,
        "reset_parameters": reset_parameters,
    }