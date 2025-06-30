import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

from constants import mw, density
from units import mass_frac_calc, concentrate_calc, velocity_calc
from thermodynamics import density_calc, mw_calc
from solver import solve_pfr

# --- عنوان ---
st.title("PFR Reactor Simulator - EO to Glycols")

st.markdown("🔧 **Enter Process Parameters:**")

# --- دریافت ورودی از کاربر ---
inlet_temp = st.slider("Inlet Temperature (°C)", 150, 250, 220)
inlet_flow_mass = st.number_input("Inlet Mass Flow (kg/h)", value=393969.0)
reactor_length = st.number_input("Reactor Length (mm)", value=14300.0)
reactor_diameter = st.number_input("Reactor Diameter (inch)", value=18.0)

# ترکیب مولی
st.markdown("### Mole Fractions of Feed")
eo = st.number_input("Ethylene Oxide (EO)", value=0.03275464)
h2o = st.number_input("Water (H2O)", value=0.9560796)
meg = st.number_input("MEG", value=0.01097885)
deg = st.number_input("DEG", value=0.00018191)
teg = st.number_input("TEG", value=0.00000492)
inlet_molefrac = [eo, h2o, meg, deg, teg]

# --- بررسی مجموع کسر مولی ---
if round(sum(inlet_molefrac), 4) != 1.0:
    st.error("❗ Mole fractions must sum to 1.0")
    st.stop()

# --- اجرای شبیه‌سازی ---
if st.button("Run Simulation"):

    # تبدیل قطر راکتور
    diameter_m = reactor_diameter * 0.0254
    length_m = reactor_length / 1000

    # محاسبه ویژگی‌های مخلوط
    mass_frac = mass_frac_calc(inlet_molefrac, mw)
    density_mix = density_calc(mass_frac, density)
    mw_mix = mw_calc(inlet_molefrac, mw)
    inlet_flow_mol = inlet_flow_mass / mw_mix
    concent = concentrate_calc(inlet_molefrac, density_mix, mw)
    u = velocity_calc(inlet_flow_mol, density_mix, mw_mix, diameter_m)

    # حل معادلات
    x_vals, concentrations = solve_pfr(concent, inlet_temp, u, length_m)

    # --- نمودار غلظت واکنش‌دهنده‌ها ---
    st.subheader("🔹 Reactants Concentration Profile (EO, H2O)")
    fig1, ax1 = plt.subplots()
    ax1.plot(x_vals, concentrations[0], label="EO", color="blue")
    ax1.plot(x_vals, concentrations[1], label="H2O", color="red")
    ax1.set_xlabel("Reactor Length (m)")
    ax1.set_ylabel("Concentration (kmol/m³)")
    ax1.set_title("Reactants")
    ax1.grid(True)
    ax1.legend()
    st.pyplot(fig1)

    # --- نمودار غلظت محصولات ---
    st.subheader("🔹 Products Concentration Profile (MEG, DEG, TEG)")
    fig2, ax2 = plt.subplots()
    ax2.plot(x_vals, concentrations[2], label="MEG", color="green")
    ax2.plot(x_vals, concentrations[3], label="DEG", color="purple")
    ax2.plot(x_vals, concentrations[4], label="TEG", color="orange")
    ax2.set_xlabel("Reactor Length (m)")
    ax2.set_ylabel("Concentration (kmol/m³)")
    ax2.set_title("Products")
    ax2.grid(True)
    ax2.legend()
    st.pyplot(fig2)

    # --- ترکیب خروجی ---
    st.subheader("📊 Outlet Composition")

    # دبی حجمی
    area = math.pi * diameter_m**2 / 4
    Q = u * area # m³/s

    # دبی مولی و جرمی
    mol_flow_out = concentrations[:, -1] * Q
    mol_frac_out = mol_flow_out / np.sum(mol_flow_out)
    mass_flow_out = mol_flow_out * mw
    mass_frac_out = mass_flow_out / np.sum(mass_flow_out)

    st.markdown("**Mole Fraction (%)**")
    for comp, val in zip(["EO", "H2O", "MEG", "DEG", "TEG"], mol_frac_out):
        st.write(f"{comp}: {val*100:.2f} %")

    st.markdown("**Mass Fraction (%)**")
    for comp, val in zip(["EO", "H2O", "MEG", "DEG", "TEG"], mass_frac_out):
        st.write(f"{comp}: {val*100:.2f} %")