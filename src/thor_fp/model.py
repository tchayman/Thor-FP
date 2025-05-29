"""
model.py — THORModel for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class THORModel:
    """
    THORModel computes scalar invariants based on input theta.
    """

    def __init__(self):
        self.constant = 42

    def scalar_invariant(self, theta):
        """
        Compute the scalar invariant for a given angle theta.

        Parameters
        ----------
        theta : float
            Angle in radians.

        Returns
        -------
        float
            The computed invariant.
        """
        return self.constant * np.pi * np.cos(theta)
