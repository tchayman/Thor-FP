"""
metrics.py — Metrics and logging utilities for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

def accuracy(y_true, y_pred):
    """
    Compute simple accuracy between true and predicted values.

    Parameters
    ----------
    y_true : np.ndarray
        Ground truth values.
    y_pred : np.ndarray
        Predicted values.

    Returns
    -------
    float
        Accuracy score (between 0 and 1).
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    return float((y_true == y_pred).mean())

def log(msg):
    """
    Simple logger for the THOR-FP project.
    """
    print(f"[THOR-FP LOG] {msg}")
