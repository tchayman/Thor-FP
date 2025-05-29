"""
harmonics.py — Harmonic functions and fractal structures for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

def generate_harmonics(n, x):
    """
    Generate the n-th harmonic at point(s) x.
    """
    return np.sin(n * x) / n
