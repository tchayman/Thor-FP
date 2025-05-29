"""
test_decoder.py — THOR-FP Unit Test (Bloc 23)
Teste la classe DeltaPhiDecoder du module decoder.py.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import sys
import os
import numpy as np

# Pour importer src/thor_fp/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from thor_fp.decoder import DeltaPhiDecoder

def test_decode_basic():
    decoder = DeltaPhiDecoder(delta_phi=2.0)
    y = 10.0
    expected = 5.0
    result = decoder.decode(y)
    assert np.isclose(result, expected), f"❌ Échec: attendu {expected}, obtenu {result}"

if __name__ == "__main__":
    test_decode_basic()
    print("✅ test_decode_basic PASSED")
