import numpy as np

def snr(a, b = None):
    """
    Signal-to-noise ratio.
    a - noisy signal
    b - clean signal
    """
    
    if b is None:
        """
        This is old function from scipy.stats.
        """
        m = a.mean(0)
        sd = a.std(axis = 0, ddof = 0)
        ratio = np.where(sd == 0, 0, m / sd)
    
    else:
        e = a - b # noise
        rms_b = np.sqrt(np.mean(b**2))
        rms_e = np.sqrt(np.mean(e**2))
        ratio = 20 * np.log10(rms_b / rms_e)

    return ratio



