"""
harmonics.py — HarmonicSynthesizer for THOR-FP.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import numpy as np

class HarmonicSynthesizer:
    """
    HarmonicSynthesizer génère un signal harmonique en combinant plusieurs sinusoïdes.
    """

    def __init__(self, frequencies=[1.0, 2.0, 3.0], amplitudes=[1.0, 0.5, 0.25]):
        self.frequencies = np.array(frequencies)
        self.amplitudes = np.array(amplitudes)

    def synthesize(self, t):
        """
        Génère le signal harmonique au temps t.

        Paramètres
        ----------
        t : float ou np.ndarray
            Temps ou tableau de temps.

        Retourne
        --------
        float ou np.ndarray
            Signal synthétisé.
        """
        t = np.asarray(t)  # ✅ Correction ici
        signal = np.zeros_like(t, dtype=float)
        for freq, amp in zip(self.frequencies, self.amplitudes):
            signal += amp * np.sin(2 * np.pi * freq * t)
        return signal
