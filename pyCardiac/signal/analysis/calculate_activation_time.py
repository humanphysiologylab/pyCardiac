import numpy as np


def calculate_activation_time(time, signal, percentage = 90.):
    try:
        index_act = np.argmax(signal > signal.max() * percentage / 100.)
        t_act = time[index_act]
    except:
        t_act = np.NaN
    return t_act
