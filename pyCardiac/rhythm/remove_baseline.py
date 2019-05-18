from ..signal.processing import remove_baseline as remove_baseline_1d


def remove_baseline(data, method_name = "linear", **kwargs):
    return remove_baseline_1d(data, method_name, **kwargs)