"""
model.py — THOR-FP Unified Scalar Topological Physics
Implements the core THORModel and main scalar law (θ₀ = 42π).
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class THORModel:
    def _init_(self, theta0=42 * np.pi):
        self.theta0 = theta0

    def scalar_invariant(self, theta):
        """
        Compute the scalar invariant for an input angle theta.
        """
        return self.theta0 * np.cos(theta)
