import numpy as np
import math

def snr(*args):
    """
        Signal-to-noise ratio.
        b - clean signal
        a - noisy signal
        e = a - b, noise
        """
    if len(args) == 1:
        """
        This is old function from scipy.stats.
        """
        a = np.asanyarray(args[0])
        m = a.mean(0)
        sd = a.std(axis=0, ddof=0)
        ratio = np.where(sd == 0, 0, m/sd)
    
    elif len(args) == 2:
        a = np.asanyarray(args[0])
        b = np.asanyarray(args[1])
        e = a - b;
        
        rms_b = np.sqrt(np.mean(b**2));
        rms_e = np.sqrt(np.mean(e**2));
        
        ratio = 20*math.log10(rms_b/rms_e)
    else:
        print('TypeError: Number of arguments should be < 3')
        ratio = None
    return ratio




