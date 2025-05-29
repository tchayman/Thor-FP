"""
metrics.py — Metrics and logging utilities for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

def accuracy(y_true, y_pred):
    return float((y_true == y_pred).mean())

def log(msg):
    print(f"[THOR-FP LOG] {msg}")
