"""
metrics.py — Metrics and logging utilities for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

def calculate_metrics(y_true, y_pred, threshold=1e-6):
    """
    Compute metrics between true and predicted values.

    Parameters
    ----------
    y_true : np.ndarray
        Ground truth values.
    y_pred : np.ndarray
        Predicted values.
    threshold : float, optional
        Threshold for considering values equal (default: 1e-6).

    Returns
    -------
    dict
        Dictionary containing various metrics:
        - accuracy: Proportion of values within threshold
        - mse: Mean Squared Error
        - mae: Mean Absolute Error
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # Accuracy (proportion of values within threshold)
    accuracy = float(np.mean(np.abs(y_true - y_pred) < threshold))
    
    # Mean Squared Error
    mse = float(np.mean((y_true - y_pred) ** 2))
    
    # Mean Absolute Error
    mae = float(np.mean(np.abs(y_true - y_pred)))
    
    return {
        "accuracy": accuracy,
        "mse": mse,
        "mae": mae
    }

def log(msg):
    """
    Simple logger for the THOR-FP project.
    """
    print(f"[THOR-FP LOG] {msg}")
