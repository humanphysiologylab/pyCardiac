import numpy as np

def calculate_alternance(time, signal, percentage = 80., APD_min = 10.):
    """Calculate Action Potential alternance for "percentage" level repolarization."""

    time_copy, signal_copy = map(np.array, (time, signal))

    assert(0 < percentage < 100)
    assert(len(time_copy.shape) == len(signal_copy.shape))
    assert(time_copy.shape == signal_copy.shape)

    index = np.nonzero(signal_copy < signal_copy.min() + (1. - percentage / 100.) * signal_copy.ptp())
    index = index[0]
    spaces = time_copy[index[1:]] - time_copy[index[:-1]]

    try:
        max_first = np.argmax(spaces > APD_min)
        max_second = max_first + 1 + np.argmax(spaces[max_first + 1: ] > APD_min)
        alternance_value = spaces[max_first] - spaces[max_second]
    except:
        alternance_value = np.NaN
    return alternance_value
