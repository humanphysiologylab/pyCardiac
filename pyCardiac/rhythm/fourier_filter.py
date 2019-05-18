import numpy as np
from ..signal.processing.filtration import fourier_filter as fourier_filter_1d


def fourier_filter(data, Fs, *args):
    return np.apply_along_axis(fourier_filter_1d, -1, data, Fs, *args)