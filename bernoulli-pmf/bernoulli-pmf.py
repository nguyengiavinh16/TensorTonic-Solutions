import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf = [1-p if x[i] == 0 else p for i in range(len(x))]
    return {'pmf': np.array(pmf), 'mean': float(p), 'variance': float(p * (1 - p))}