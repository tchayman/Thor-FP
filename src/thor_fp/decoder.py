"""
decoder.py — DeltaPhiDecoder for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class DeltaPhiDecoder:
    def _init_(self, delta_phi=0.1):
        self.delta_phi = delta_phi

    def decode(self, y):
        """
        Example decoding function (to be customized).
        """
        return y / self.delta_phi
