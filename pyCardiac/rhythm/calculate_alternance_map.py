import numpy as np
from ..signal.analysis import calculate_alternance


def calculate_alternance_map(data, t_start, t_end, apd_min = 10.):
    time = np.arange(t_start, t_end)
    alt_map = np.apply_along_axis(lambda x: calculate_alternance(time, x[t_start: t_end], apd_min), -1, data)
    return alt_map
