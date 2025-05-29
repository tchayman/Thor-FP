"""
test_encoder.py — THOR-FP Unit Test (Bloc 21)
Teste la classe FractalEncoder du module encoder.py.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import sys
import os
import numpy as np

# Pour importer src/thor_fp/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from thor_fp.encoder import FractalEncoder

def test_encode_scalar():
    encoder = FractalEncoder()
    x = 0.0
    expected = np.sin(np.pi * x) + np.cos((1 + 5**0.5) / 2 * x)
    result = encoder.encode(x)
    assert np.isclose(result, expected), f"❌ Échec: attendu {expected}, obtenu {result}"

def test_encode_vector():
    encoder = FractalEncoder()
    x = np.array([0.0, 1.0])
    result = encoder.encode(x)
    assert isinstance(result, np.ndarray), "❌ Résultat non-vectoriel"
    assert result.shape == x.shape, f"❌ Mauvaise forme: {result.shape}"
    print("✅ test_encode_vector PASSED")

if __name__ == "__main__":
    test_encode_scalar()
    test_encode_vector()
    print("✅ Tous les tests FractalEncoder ont réussi.")
