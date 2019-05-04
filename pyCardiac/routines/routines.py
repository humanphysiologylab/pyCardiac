import numpy as np

def rescale(signal, v_min = 0., v_max = 1.):
    """Rescale signal to [v_min, v_max]."""

    # rescaling to [0, 1]
    result = np.array(signal, dtype = float)
    result -= np.nanmin(result)
    result /= np.nanmax(result)

    # rescaling to [v_min, v_max] 
    v_ptp = v_max - v_min
    result *= v_ptp
    result -= v_min

    return result
    

def moving_average(a, n = 3) :
    """Source: https://stackoverflow.com/a/14314054"""

    ret = np.cumsum(a, dtype = float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

