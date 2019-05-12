import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.signal import detrend as detrend


def remove_baseline(signal, method_name = "linear", **kwargs):
    
    if (method_name == "linear"):
        signal_detrended = detrend(signal, **kwargs)
    elif (method_name == "least_squares"):
        trend = baseline_als(signal, **kwargs)
        signal_detrended = signal - trend
    else:
        raise Exception("method_name may be 'linear' or 'least_squares' but {} given".format(method_name))
    
    return signal_detrended
    

def baseline_als(signal, lam = 1e6, p = 0.01, niter = 10):    
    """
    returns baseline of the signal
    
    Baseline Correction with Asymmetric Least Squares Smoothing
    Paul H. C. EilersHans F.M. Boelens, October 21, 2005

    Explanation from the article:
        There are two parameters: p for asymmetry and lam for smoothness.
        Both have to be tuned to the data at hand.
        We found that generally 0.001 < p < 0.1 is a good choice (for a signal with positive peaks)
        and 10^2 < lam < 10^9, but exceptions may occur.
        In any case one should vary lam on a grid that is approximately linear for log(lam).
        Often visual inspection is sufficient to get good parameter values.
    """
    L = len(signal)
    D = sparse.diags([1, -2, 1],
                     [0, -1, -2],
                     shape = (L, L - 2))
    weights = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(weights, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        baseline = spsolve(Z, weights * signal)
        weights = p * (signal > baseline) + (1 - p) * (signal < baseline)
        
    return baseline
