"""
utils.py — Utility functions for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np
import random
import os

def seed_everything(seed=42):
    """
    Set random seed for reproducibility (numpy and random).
    """
    np.random.seed(seed)
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)

def normalize_data(data, min_val=None, max_val=None):
    """
    Normalize data to [0, 1] range.

    Parameters
    ----------
    data : np.ndarray
        Input data to normalize.
    min_val : float, optional
        Minimum value for normalization. If None, uses data.min().
    max_val : float, optional
        Maximum value for normalization. If None, uses data.max().

    Returns
    -------
    np.ndarray
        Normalized data in [0, 1] range.
    """
    data = np.asarray(data)
    if min_val is None:
        min_val = data.min()
    if max_val is None:
        max_val = data.max()
    return (data - min_val) / (max_val - min_val)
