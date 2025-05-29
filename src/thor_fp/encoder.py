"""
encoder.py — FractalEncoder for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class FractalEncoder:
    def _init_(self, pi=np.pi, phi=(1 + 5 ** 0.5) / 2):
        self.pi = pi
        self.phi = phi

    def encode(self, x):
        """
        Example encoding function (to be customized).
        """
        return np.sin(self.pi * x) + np.cos(self.phi * x)
