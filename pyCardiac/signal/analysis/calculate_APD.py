import numpy as np

def calculate_APD(time, signal, percentage = 80.):
    """ Calculate Action Potential Duration for "percentage" level repolarization."""

    time_copy, signal_copy = map(np.array, (time, signal))

    assert(0 < percentage < 100)
    assert(len(time_copy.shape) == len(signal_copy.shape))
    assert(time_copy.shape == signal_copy.shape)

    index = np.nonzero(signal_copy < signal_copy.min() + (1. - percentage / 100.) * signal_copy.ptp())
    index = index[0]
    spaces = time_copy[index[1:]] - time_copy[index[:-1]]
    APD = spaces.max()
    return APD
