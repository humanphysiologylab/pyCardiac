from ..signal.processing.filtration import binning as binning_1d


def binning(data, kernel_size = 3, kernel_name = 'uniform', mask = None):
    return binning_1d(data, kernel_size, kernel_name, mask)