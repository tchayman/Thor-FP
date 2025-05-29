"""
test_encoder.py — THOR-FP Unit Test (Bloc 21)
Teste la classe FractalEncoder du module encoder.py.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import sys
import os
import numpy as np

# Pour importer src/thor_fp/ même si lancé depuis la racine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '../src/')))

from thor_fp.encoder import FractalEncoder

def test_encode_scalar():
    encoder = FractalEncoder()
    x = 0.0
    expected = np.sin(np.pi * x) + np.cos((1 + 5**0.5) / 2 * x)  # = 0 + 1 = 1
    result = encoder.encode(x)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

if _name_ == "_main_":
    test_encode_scalar()
    print("test_encode_scalar PASSED")
