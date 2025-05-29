"""
test_model.py — THOR-FP Unit Test (Bloc 20)
Teste la classe THORModel du module model.py.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import sys
import os
import numpy as np

# Permet d'importer src/thor_fp/ même si le script est lancé depuis la racine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from thor_fp.model import THORModel

def test_scalar_invariant_basic():
    model = THORModel()
    theta = 0.0
    expected = 42 * np.pi * 1  # cos(0) = 1
    result = model.scalar_invariant(theta)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_scalar_invariant_basic()
    print("test_scalar_invariant_basic PASSED")
