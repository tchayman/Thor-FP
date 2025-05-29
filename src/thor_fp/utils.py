"""
utils.py — Utility functions for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

def seed_everything(seed=42):
    np.random.seed(seed)

def device():
    return "cpu"  # Update if GPU available or with torch
