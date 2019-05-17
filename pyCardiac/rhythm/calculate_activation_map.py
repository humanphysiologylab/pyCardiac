import numpy as np
from ..signal.analysis import calculate_activation_time


def calculate_activation_map(data, t_start, t_end, percentage = 90.):
    time = np.arange(t_start, t_end)
    act_map = np.apply_along_axis(lambda x: calculate_activation_time(time, x[t_start: t_end], percentage), -1, data)
    return act_map
