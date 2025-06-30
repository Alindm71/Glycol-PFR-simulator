from config import inlet_flow_mol, inlet_molefrac, inlet_temp, diameter, reactor_lenght
import numpy as np
import scipy.integrate as sp
from units import mass_frac_calc, concentrate_calc, velocity_calc
from constants import mw, density
from thermodynamics import density_calc, mw_calc
from kinetics import reaction_rate1_calc, reaction_rate2_calc, reaction_rate3_calc
from mass_balance import mass_balance_calc
from solver import solve_pfr
import matplotlib.pyplot as plt 
import math

mole_flow = inlet_flow_mol
mole_frac = inlet_molefrac

mass_frac = mass_frac_calc(mole_frac, mw)

rho_mix = density_calc(mass_frac, density)

concent = concentrate_calc(mole_frac, rho_mix, mw)

temp = inlet_temp
r1 = reaction_rate1_calc(concent, temp)
r2 = reaction_rate2_calc(concent, temp)
r3 = reaction_rate3_calc(concent, temp)

rates = [r1, r2, r3]
#print(r1, r2, r3)

mw_mix = mw_calc(mole_frac, mw)

u = velocity_calc(mole_flow, rho_mix, mw_mix, diameter)
length = reactor_lenght / 1000
x = np.linspace(0, length, 500)

dC_dx = mass_balance_calc(concent, x, temp, u)
#print(dC_dx)


residence_time = (length / u) / 60
print(residence_time)


x_vals, concentration = solve_pfr(concent, temp, u, length)


labels = ["EO", "H2O", "MEG", "DEG", "TEG"]
for i in range(2, len(labels)):
    plt.plot(x_vals, concentration[i], label = labels[i])

plt.xlabel("reactor length (m)")
plt.ylabel("concentration (kmol/m3)")
plt.legend()
plt.grid()
plt.show()    

c_outlet = concentration[:, -1]

area = (math.pi / 4) * diameter ** 2 
vol_flow = u * area 

mol_flow_out = c_outlet * vol_flow
mol_frac_out = mol_flow_out / mol_flow_out.sum()

mass_frac_out = mass_frac_calc(mol_frac_out.tolist(), mw)

print(mol_flow_out) 
print(mol_frac_out) 
print(mass_frac_out) 


#print(type(dC_dx))
#print(dC_dx)
#print(mass_frac)
#print(rho_mix)
#print(concent)
#print(rates)
#print(mw_mix)
#print(u)
