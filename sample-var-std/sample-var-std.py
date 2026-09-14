import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    mean = float(sum(x) / len(x))
    var = float(sum((i - mean)**2 for i in x) / (len(x) - 1))
    return {'variance': var, 'standard_deviation': var**0.5}