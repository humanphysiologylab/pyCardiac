import numpy as np
from ..signal.processing.filtration import fourier_filter as fourier_filt


def fourier_filter(data, Fs, *args):
    return np.apply_along_axis(fourier_filt, -1, data, Fs, *args)