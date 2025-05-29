"""
decoder.py — DeltaPhiDecoder for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class DeltaPhiDecoder:
    """
    DeltaPhiDecoder applies a decoding operation based on ΔΦ.
    """

    def _init_(self, delta_phi=0.1):
        self.delta_phi = delta_phi

    def decode(self, y):
        """
        Decode input y using ΔΦ.

        Parameters
        ----------
        y : float or np.ndarray
            Input value(s).

        Returns
        -------
        float or np.ndarray
            Decoded value(s).
        """
        return y / self.delta_phi
