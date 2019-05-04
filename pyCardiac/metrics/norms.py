import numpy as np
"""
Metrics below may be used to compare goodness of fit between Action Potentials via Genetic Algorithm.
4.05.2019
"""

def ssd(a, b):
    """
    Sum Of Squared Differences (SSD) implementation.
    a, b - arrays with the same length
    """
    A = np.array(a)
    B = np.array(b)
    return float(np.sum((A-B)*(A-B)))


def sd(a,b):
    """
    Standard deviation (SD) implementation.
    a, b - arrays with the same length
    """
    A = np.array(a)
    B = np.array(b)
    summation = float(np.sum((A-B)*(A-B)))/A.size
    return np.sqrt(summation)

