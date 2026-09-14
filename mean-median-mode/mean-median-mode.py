from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x.sort()
    mean = float(sum(x)/len(x))
    median = float(x[int(len(x)/2)] if len(x) % 2 == 1 else (x[int(len(x)/2)] + x[int(len(x)/2 - 1)])/2)
    tmp = float(max(x.count(i) for i in x))
    mode = 0
    for i in x:
        if x.count(i) == tmp: 
            mode = i
            break
    return {'mean': mean, 'median': median, 'mode': float(mode)}