"""
encoder.py — FractalEncoder for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class FractalEncoder:
    """
    FractalEncoder applies fractal encoding using π and φ.
    """

    def _init_(self, pi=np.pi, phi=(1 + 5 ** 0.5) / 2):
        self.pi = pi
        self.phi = phi

    def encode(self, x):
        """
        Encode input x using fractal/harmonic structure.

        Parameters
        ----------
        x : float or np.ndarray
            Input value(s).

        Returns
        -------
        float or np.ndarray
            Encoded value(s).
        """
        return np.sin(self.pi * x) + np.cos(self.phi * x)
