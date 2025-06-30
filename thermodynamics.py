
#from units import mass_frac_calc
#from config import inlet_molefrac
#from constants import density
#from constants import mw



def density_calc(mass_frac: list, density: list)-> float:
    """" A function for calculation of mixture density from density of components at fixed temperature """
    
    density_mix = 0
    for i in range(5):
        density_mix += mass_frac[i] * density[i]

    return density_mix



def mw_calc(mole_frac: list, mw: list) -> float:
    """"A function for calculation of mixture Molecular weight (MW) """

    mw_mix = 0
    for i in range(len(mw)):
        mw_i = mole_frac[i] * mw[i]
        mw_mix += mw_i

    return mw_mix