import numpy as np
from ..routines import rescale as rescale_1d


def rescale(data, v_min = 0., v_max = 1.):
    return np.apply_along_axis(rescale_1d, -1, data, v_min, v_max)