"""
decoder.py — DeltaPhiDecoder for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class DeltaPhiDecoder:
    """
    DeltaPhiDecoder applies a decoding operation based on ΔΦ.
    """

    def __init__(self, delta_phi=0.1):  # ✅ constructeur Python valide
        self.delta_phi = delta_phi

    def decode(self, y):
        """
        Decode input y using ΔΦ.
        """
        return y / self.delta_phi  # logique : division par delta_phi
