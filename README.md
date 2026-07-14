# ⚛️ Quantum Cascade Laser (QCL) Simulator

A physics-based simulation and research platform for a **3-layered, 4.6 µm Quantum Cascade Laser**, built as an integrated Streamlit dashboard. The platform combines device physics, reinforcement-learning-based optimization, gas sensing, noise/thermal analysis, and energy band structure modeling into a single tool for design, simulation, optimization, and validation.

---

## 🚀 Features

- **Physics Engine** — Core QCL device physics: current-voltage characteristics, optical gain, threshold conditions, output power, efficiency, reliability, and more.
- **Energy Structure** — Conduction band alignment, quantum well energy levels, wavefunctions, transition diagrams, and cascade structure visualization.
- **Reinforcement Learning (RL) Optimization** — A Q-learning agent trained to optimize QCL operating parameters (current, voltage, temperature, cascade stages) against a custom physics-based environment.
- **Gas Sensing Module** — Beer-Lambert absorption, transmission, gas concentration estimation, and gas identification based on the QCL's simulated emission wavelength.
- **Noise & Thermal Analysis** — Gaussian noise modeling, relative intensity noise (RIN), signal-to-noise ratio (SNR), and thermal/temperature-dependent device behavior.
- **Visualization Suite** — Extensive plotting library covering gain, power, thermal, reliability, threshold, wavelength/spectrum, efficiency, and parameter heatmaps.
- **Validation** — Benchmarking and consistency checks against reference physics behavior.
- **Interactive Dashboard** — A Streamlit-based UI tying all modules together with live parameter controls, metrics, and visualizations.

---

## 📁 Project Structure

```
QCL_stimulation_drdo/
├── app.py                   # Main Streamlit entry point
├── dashboard/                # UI layout, sidebar controls, theming, metrics
│   ├── layout.py
│   ├── sidebar.py
│   ├── theme.py
│   └── metrics.py
├── physics_engine/            # Core QCL device physics (gain, power, threshold, etc.)
├── energy_structure/           # Band alignment, wavefunctions, cascade structure
├── gas_sensation/              # Beer-Lambert absorption, transmission, gas ID
├── noise/                     # Gaussian noise, RIN, SNR calculations
├── RL/                        # Q-learning agent, environment, training, evaluation
│   ├── agent.py
│   ├── environment.py
│   ├── train.py
│   ├── evaluate.py
│   ├── inference.py
│   ├── reward.py
│   ├── states.py
│   ├── hyperparameters.py
│   └── model_manager.py
├── visualization/              # Plotting modules (gain, power, thermal, spectrum, etc.)
├── validation/                 # Benchmark/validation checks
├── models/                    # Saved trained RL models (Q-tables)
├── utils/                     # Shared helpers (unit conversion, etc.)
├── data/                      # Reference/input data
├── output/                    # Generated outputs/exports
├── assets/                    # Images and static assets used in the UI
├── requirement.txt             # Python dependencies
└── test_code.py                # Test/scratch script
```

---

## 🛠️ Installation

**1. Clone the repository**
```bash
git clone <your-repository-url>
cd QCL_stimulation_drdo
```

**2. Create and activate a virtual environment (recommended)**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirement.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

This launches the dashboard in your default browser (typically at `http://localhost:8501`). From there you can:

- Adjust device parameters (current, voltage, temperature, well/barrier width, cascade stages) from the sidebar.
- Click **Run Simulation** to compute the physics chain and populate all dashboard metrics and plots.
- Click **Train RL Agent** to run Q-learning optimization and view reward/epsilon training curves.
- Explore the **Gas Sensing**, **Noise & Thermal**, **Energy Structure**, and **Equations** tabs for deeper analysis.

---

## 🧪 Testing

```bash
python test_code.py
```

*(Add/expand test coverage as the project matures.)*

---

## 📋 Requirements

See [`requirement.txt`](./requirement.txt) for the full dependency list. Core dependencies typically include:

- `streamlit`
- `numpy`
- `matplotlib`

---

## 📌 Notes

- This project models a **simplified, tunable physics approximation** rather than a full electromagnetic/quantum transport simulation — constants in `physics_engine/` and `RL/environment.py` are illustrative and should be calibrated against real device/measurement data for production use.
- The Reinforcement Learning module uses **tabular Q-learning** (not PPO or other deep-RL methods).

---

## 📄 License

*MIT License*

## 👤 Author / Maintainer

*Archita Kumari & Advait (DRDO interns)*
