"""
reproducibility_check.py — THOR-FP Reproducibility Test (Bloc 24)
Vérifie que tous les modules et notebooks principaux sont importables/exécutables.
Author: Alexandre ICHAÏ (www.thor.love)
"""

import sys
import os

def check_module_imports():
    print("Checking module imports...")
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '../src/')))
    try:
        from thor_fp.model import THORModel
        from thor_fp.harmonics import generate_harmonics
        from thor_fp.encoder import FractalEncoder
        from thor_fp.decoder import DeltaPhiDecoder
        from thor_fp.utils import seed_everything, device
        from thor_fp.config import load_config
        from thor_fp.metrics import accuracy, log
        print("All module imports PASSED")
    except Exception as e:
        print(f"Module import FAILED: {e}")
        return False
    return True

def check_notebooks_exist():
    print("Checking notebooks existence...")
    notebook_list = [
        '../notebooks/demo_model.ipynb',
        '../notebooks/demo_encoder.ipynb',
        '../notebooks/demo_harmonics.ipynb',
        '../notebooks/demo_decoder.ipynb'
    ]
    missing = [nb for nb in notebook_list if not os.path.exists(nb)]
    if missing:
        print(f"Missing notebooks: {missing}")
        return False
    print("All notebooks found")
    return True

if _name_ == "_main_":
    ok = check_module_imports() and check_notebooks_exist()
    if ok:
        print("✅ Reproducibility check PASSED")
    else:
        print("❌ Reproducibility check FAILED")
