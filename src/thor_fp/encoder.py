"""
encoder.py — FractalEncoder for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class FractalEncoder:
    """
    FractalEncoder encode les entrées selon une fonction fractale.
    """

    def __init__(self):
        # On pourrait définir des paramètres ici si nécessaire
        pass

    def encode(self, x):
        """
        Encode l'entrée x avec une combinaison sinusoïdale.

        Paramètres
        ----------
        x : float ou np.ndarray
            Entrée(s) à encoder.

        Retourne
        --------
        float ou np.ndarray
            Valeur(s) encodée(s).
        """
        phi = (1 + np.sqrt(5)) / 2
        return np.sin(np.pi * x) + np.cos(phi * x)
