"""
Adding Additive Gaussian White Noise (AWGN) to a signal.
"""
import numpy as np

def awgn(signal, snr_db):
    """
    Input:
        'signal' - 1D numpy array to which an AWGN noise needs to be added.
        'snr_db' - given SNR (specified in dB).
    Output: 
        noise signal
    """
    signal = np.asanyarray(signal)
    
    snr_linear = 10**(snr_db/10)
    power = sum(signal*signal)/(signal.size)
    sigma = np.sqrt(power/snr_linear)
    noise = sigma*np.random.normal(0, 1, signal.size)
    return signal+noise
