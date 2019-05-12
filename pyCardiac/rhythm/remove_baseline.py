from ..signal.processing import remove_baseline as rm_baseline

def remove_baseline(data, method_name = "linear", **kwargs):
    return rm_baseline(data, method_name, **kwargs)