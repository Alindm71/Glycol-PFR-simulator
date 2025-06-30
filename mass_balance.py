from config import inlet_temp
from kinetics import reaction_rate1_calc, reaction_rate2_calc, reaction_rate3_calc
from units import concentrate_calc
import numpy as np


def mass_balance_calc(concentrate: list, x, temp: float, u:float ):
    """" a function for calculation of mass balance in reactor PFR 
        input arguments:   
        output arguments: dC / dx """
    
    r1 = reaction_rate1_calc(concentrate, temp)
    r2 = reaction_rate2_calc(concentrate, temp)
    r3 = reaction_rate3_calc(concentrate, temp)

    C_EO, C_H20, C_MEG, C_DEG, C_TEG = concentrate

    dC_EO_dx = (-r1 -r2 -r3) / u
    dC_H2O_dx = (-r1) / u
    dC_MEG_dx = (r1 - r2) / u
    dC_DEG_dx = (r2 - r3) / u
    dC_TEG_dx = r3 / u 

    dC_dx = np.array([dC_EO_dx, dC_H2O_dx, dC_MEG_dx, dC_DEG_dx, dC_TEG_dx])

    return dC_dx




