from mass_balance import mass_balance_calc
import numpy as np
from scipy.integrate import solve_ivp

def solve_pfr(conc0, temp: float, u: float, length: float, n_points: int = 500):
    def ode_system(x, C):
        return mass_balance_calc(C, x, temp, u)
    
    x_span = (0, length)
    x_eval = np.linspace(0, length, n_points)

    sol = solve_ivp(ode_system, x_span, conc0, t_eval = x_eval, method = "RK45")

    return sol.t, sol.y    # x_vals & concentration

