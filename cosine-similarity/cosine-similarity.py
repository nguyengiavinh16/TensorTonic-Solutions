import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    if sum(a) == 0 or sum(b) == 0: return 0.0
    dot_prod = float(sum(a[i] * b[i] for i in range(len(a))))
    return dot_prod / (sum(a[i]**2 for i in range(len(a))) * sum(b[i]**2 for i in range(len(b))))**0.5