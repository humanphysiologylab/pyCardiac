""" 
Autoscaling technique implementation. 
Based on the method of least squares (link: https://en.wikipedia.org/wiki/Least_squares)
Date: 17.05.2019
"""
import numpy as np
from ...metrics import sd

def scalar_multiplications(a, b):
    a, b = map(np.array, (a, b))
    coefficients = np.array([0., 0., 0., 0., 0.])
    coefficients[0] = np.sum(a * b)
    coefficients[1] = sum(a)
    coefficients[2] = sum(b)
    coefficients[3] = np.sum(a * a)
    coefficients[4] = sum(np.ones(len(a)))
    return coefficients

def autoscaling(signal_to_scale, signal_reference):
    """
    Input:
        'signal_to_scale' - signal we want to scale.
        'signal_reference' - target signal.
        Both are 1D numpy arrays same length.
    Output:
        'signal_scaled'  - scaled signal, 1d array.
        variance - standart distance (error between two signals)
    """
    c = scalar_multiplications(signal_to_scale, signal_reference)
    
    if c[1] == 0 or c[1] * c[1] - c[4] * c[3] == 0:
        alpha = 0
        beta = 0
    else:
        beta = (c[0]*c[1] - c[2]*c[3])/(c[1]*c[1] - c[4]*c[3])
        alpha = (c[2] - beta*c[4])/c[1]
    
    signal_scaled = signal_to_scale * alpha + beta
    variance = sd(signal_scaled, signal_reference)
    
    return signal_scaled, variance
