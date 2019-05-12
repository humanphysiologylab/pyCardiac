from ..signal.processing.filtration import binning as binning_


def binning(data, kernel_size = 3, kernel_name = 'uniform', mask = None):
    return binning_(data, kernel_size = 3, kernel_name = 'uniform', mask = None)