"""
config.py — Configuration loader for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import yaml
import os

DEFAULT_CONFIG = {
    "model": {
        "theta0": 42 * 3.141592653589793,
        "delta_phi": 0.1
    },
    "encoder": {
        "pi": 3.141592653589793,
        "phi": 1.618033988749895
    },
    "training": {
        "seed": 42,
        "batch_size": 32,
        "learning_rate": 0.001
    }
}

def load_config(config_path="config.yaml"):
    """
    Load configuration from a YAML file.

    Parameters
    ----------
    config_path : str
        Path to the YAML configuration file.

    Returns
    -------
    dict
        Configuration dictionary.
    """
    if not os.path.exists(config_path):
        return DEFAULT_CONFIG
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config
