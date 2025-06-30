# Glycol PFR Simulator

**Simulation of an Industrial Plug Flow Reactor (PFR) for Ethylene Oxide Conversion to Glycols**

---

## 📌 Project Overview

This Python-based simulator models the conversion of Ethylene Oxide (EO) into glycols (MEG, DEG, TEG) through a multi-step reaction in a plug flow reactor (PFR).  
All feed and reactor specifications are based on actual data from an industrial production unit.

---

## 📊 Technical Features

- Multi-step reaction kinetics:
  - EO + H₂O → MEG  
  - EO + MEG → DEG  
  - EO + DEG → TEG  
- Plug flow reactor modeling using mass balance differential equations
- Thermophysical property modules
- Modular code structure with clean separation of functionality
- Interactive graphical interface built with Streamlit
- Visualization of:
  - Reactant concentration profiles
  - Product concentration profiles
  - Outlet composition (mol% and wt%)

---

## ⚙️ User Inputs via GUI

- Feed temperature (°C)
- Mass flow rate (kg/h)
- Mole fractions of EO, H₂O, MEG, DEG, TEG
- Reactor length (mm)
- Reactor diameter (inch)

*Velocity and residence time are calculated automatically.*

---

## 🚀 How to Run

1. Clone the repository  
2. Install dependencies:

```bash
pip install -r requirements.txt

3. Launch the simulator:



streamlit run gui.py


---

📈 Output Features

Dynamic concentration profile vs. reactor length

Final outlet stream composition in mole percent and weight percent

Graphs for both reactants and products



---

🏗️ Project Structure

.
├── gui.py # Streamlit graphical interface
├── config.py # Feed and reactor specifications
├── constants.py # Physical properties (MW, density)
├── kinetics.py # Reaction rate models
├── thermodynamics.py # Density and MW mixing rules
├── units.py # Unit conversions and calculations
├── mass_balance.py # Differential equations (dC/dx)
├── solver.py # ODE solver integration
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

📦 Future Extensions

🔄 Integration with Aspen HYSYS for automatic feed input

🌡️ Non-isothermal reactor modeling (energy balance)

🧪 By-product formation and parallel reactions

📤 Export of simulation results to Excel or database



---

👨‍💻 Author

Ali Nademi
Process Engineer | Python Developer
📧 alinademi1371@gmail.com


---

⚖️ License

MIT License – see LICENSE file for full terms.
