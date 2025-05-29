"""
test_harmonics.py — THOR-FP Unit Test (Bloc 22)
Teste la fonction generate_harmonics du module harmonics.py.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import sys
import os
import numpy as np

# Pour importer src/thor_fp/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '../src/')))

from thor_fp.harmonics import generate_harmonics

def test_harmonic_n1_x0():
    n = 1
    x = 0.0
    expected = 0.0  # sin(1*0)/1 = 0
    result = generate_harmonics(n, x)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"

if _name_ == "_main_":
    test_harmonic_n1_x0()
    print("test_harmonic_n1_x0 PASSED")
