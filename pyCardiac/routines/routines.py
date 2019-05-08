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


def add_borders(matrix,
                left_border_size,
                right_border_size,
                top_border_size,
                bottom_border_size,
                value = 0.):
    """Adds borders with given sizes and filled with given value to matrix"""
    
    n, m = matrix.shape

    A = np.full((n + top_border_size + bottom_border_size,
                 m + left_border_size + right_border_size),
                fill_value = value)

    top = top_border_size
    bottom = top_border_size + n
    left = left_border_size
    right = left_border_size + m

    A[top : bottom, left : right] = matrix  

    return A


def phase_difference(a, b):
    
    if np.abs(a - b) <= np.pi:
        return a - b
    
    elif (a - b) > 0:
        return a - b - 2 * np.pi
    
    else:
        return a - b + 2 * np.pi
    

def char_to_float(c, f_min = -100., f_max = 50.):

    f = f_min + (f_max - f_min) * (c + 128.) / 255.
    return f

def float_to_char(f, f_min = -100., f_max = 50.):

    c = -128. + 255. * (f - f_min) / (f_max - f_min)
    return c