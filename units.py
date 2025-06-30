from config import inlet_flow_mol, diameter
from config import inlet_molefrac
from constants import mw, density
from thermodynamics import density_calc
import math



def mass_frac_calc( mole_frac: list, mw: list)->list:
    """" a function that convert molr fraction of stream to mass fraction"""
    mass_frac = []
    sigmaximwi = 0
    for i in range(len(mw)):
        ximwi = mw[i] * mole_frac[i]
        sigmaximwi += ximwi 
        #calculation of Xi * MWi and Sigma(Xi * MWi) for stream

    for i in range(len(mw)):
        ximwi = mw[i] * mole_frac[i]
        mass_frac_i = ximwi / sigmaximwi
        mass_frac.append(mass_frac_i)

    return mass_frac

#for test
#a = mass_frac_calc(mw, inlet_molefrac)
#print(a)           

def concentrate_calc(mole_frac: list, density_mix: float, mw: list)-> list:
    """" a function to convert mole fraction of species to molar concentration of components"""

    concentration = []
    for i in range(len(mole_frac)):
        concentration_i = (mole_frac[i] * density_mix) / mw[i]
        concentration.append(concentration_i)

    return concentration


def velocity_calc(mole_flow: float, density_mix: float, mw_mix: float, diameter: float)-> float:
    """" a funxtion to calculation of linear velocity of fluid in reactor"""
    area = (math.pi * diameter ** 2 ) / 4
    u = (mole_flow * mw_mix) / (3600 * (density_mix * area))

    return u





