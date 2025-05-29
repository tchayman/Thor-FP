"""
run_benchmarks.py — THOR-FP Benchmark runner (Bloc 19)
Author: Alexandre ICHAÏ (www.thor.love)

Ce script charge le tableau benchmarks/benchmark_table.csv et affiche les résultats.
À étendre avec de vrais tests/benchmarks si besoin.
"""

import pandas as pd
import os

def main():
    csv_path = os.path.join(os.path.dirname(_file_), "benchmark_table.csv")
    if not os.path.exists(csv_path):
        print(f"Benchmark file not found: {csv_path}")
        return
    df = pd.read_csv(csv_path)
    print("=== Benchmark Results ===")
    print(df.to_markdown(index=False))

if _name_ == "_main_":
    main()
