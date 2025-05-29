"""
test_harmonics.py — THOR-FP Unit Test (Bloc 22)
Teste la classe HarmonicSynthesizer du module harmonics.py.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import sys
import os
import numpy as np

# Pour importer src/thor_fp/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from thor_fp.harmonics import HarmonicSynthesizer

def test_synthesize_scalar():
    synth = HarmonicSynthesizer()
    t = 0.0
    result = synth.synthesize(t)
    assert np.isclose(result, 0.0), f"❌ Mauvais résultat à t=0: {result}"

def test_synthesize_array():
    synth = HarmonicSynthesizer()
    t = np.linspace(0, 1, 100)
    result = synth.synthesize(t)
    assert isinstance(result, np.ndarray), "❌ Résultat attendu: tableau"
    assert result.shape == t.shape, "❌ Forme incorrecte"
    print("✅ test_synthesize_array PASSED")

if __name__ == "__main__":
    test_synthesize_scalar()
    test_synthesize_array()
    print("✅ Tous les tests HarmonicSynthesizer ont réussi.")
