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

def device():
    """
    Return the default computation device.
    Update this function if GPU/torch support is added.
    """
    return "cpu"
