import math

def reaction_rate1_calc(concentration: list, temp: float):
    """"a function for calculation the rate of reaction NO. 1
        reaction:
                    EO + H2O --> MEG 
                    r1 = K1 * [EO] * [H2O]
                    K1 = exp(13.62 - 8220/T) 
                    """
    
    k1 = math.exp(13.62 - (8220/(temp+273.15)))
    r1 = (k1 * concentration[0] * concentration[1]) / 60
    # dimention of reaction ratr (r1) is kmol/s

    return r1


def reaction_rate2_calc(concentration: list, temp: float):
    """"a function for calculation the rate of reaction NO. 2
        reaction:
                    EO + MEG --> DEG 
                    r2 = K2 * [EO] * [MEG]
                    K2 = exp(15.57 - 8700/T) 
                    """
    
    k2 = math.exp(15.57 - (8700 / (temp + 273.15)))
    r2 = (k2 * concentration[0] * concentration[2]) / 60
    # dimention of reaction ratr (r2) is kmol/s

    return r2



def reaction_rate3_calc(concentration: list, temp: float):
    """"a function for calculation the rate of reaction NO. 3
        reaction:
                    EO + DEG --> TEG 
                    r3 = K3 * [EO] * [DEG]
                    K3 = exp(16.06 - 8900/T) 
                    """
    
    k3 = math.exp(13.62 - (8220/(temp+273.15)))
    r3 = (k3 * concentration[0] * concentration[3]) / 60
    # dimention of reaction ratr (r3) is kmol/s

    return r3