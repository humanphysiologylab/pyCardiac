import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


def extract_baseline(y, lam, p, niter = 10):
    """
    Baseline Correction with Asymmetric Least SquaresSmoothing
    Paul H. C. EilersHans F.M. Boelens, October 21, 2005

    Explanation from the article:
        There are two parameters: p for asymmetry and lam for smoothness.
        Both have to be tuned to the data at hand.
        We found that generally 0.001 < p < 0.1 is a good choice (for a signal with positive peaks)
        and 10^2 < lam < 10^9, but exceptions may occur.
        In any case one should vary lam on a grid that is approximately linear for log(lam).
        Often visual inspection is sufficient to get good parameter values.
    """
    L = len(y)
    D = sparse.diags([1, -2, 1],
                     [0, -1, -2],
                     shape = (L, L - 2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w * y)
        w = p * (y > z) + (1 - p) * (y < z)
    return z
