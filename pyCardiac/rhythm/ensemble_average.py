import numpy as np
from ..signal.processing import ensemble_average as ensemble_average_1d


def ensemble_average(data, cycle_length):
    """
    returns averaged data
    """
    time = np.arange(data.shape[-1])
    return np.apply_along_axis(lambda signal: ensemble_average_1d(time, signal, cycle_length)[1], -1, data)