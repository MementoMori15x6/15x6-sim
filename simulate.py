#!/usr/bin/env python3
import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

print("sys.argv contents:", sys.argv)

# 1. SETUP
if len(sys.argv) > 1:
    csv_file = sys.argv[1]
    label = os.path.basename(csv_file).replace('.csv', '').replace('_', ' ').title()
    print(f"Running simulation on: {csv_file}")
    print(f"Label: {label}")
else:
    csv_file = "examples/eusocial_ant_colony.csv"
    label = "Ants Consensus Baseline"
    print("No CSV path provided — falling back to ants baseline")

os.makedirs("tests/outputs", exist_ok=True)

fixed_centres = np.array([
    [1.00, -1.00], [0.70, -0.60], [0.40, -0.30], [0.20, 0.00], [0.00, 0.00],
    [-0.30, 0.20], [-0.60, 0.50], [-0.80, 0.80], [-1.00, 1.00], [0.90, 0.50]
])

def load_metrics(csv_path):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Missing file: {csv_path}")
    df = pd.read_csv(csv_path)
    print("Loading CSV:", csv_path)
    print("DF shape:", df.shape)
    print("DF columns:", df.columns.tolist())
    print(df.head(2))
    
    if 'Score' in df.columns:
        vector = df['Score'].astype(float).values
    else:
        vector = df.iloc[:, 2].astype(float).values
    
    print(f"Extracted {len(vector)} numeric scores")
    if len(vector) != 35:
        raise ValueError(f"Expected 35 scores, got {len(vector)}")
    
    return vector

def compute_coordinates(vector, y_multiplier=5.0, x_extra_weight=1.0):
    extreme_pos = vector > 8
    extreme_neg = vector < -8
    penalty_pos = extreme_pos * (vector - 8) ** 2 * 0.8
    penalty_neg = extreme_neg * (vector + 8) ** 2 * 0.8
    adjusted = vector + penalty_pos + penalty_neg
  
    x_raw = np.mean(adjusted[:18])
    y_raw = np.mean(adjusted[18:])
  
    suppression_boost = (vector[14] + vector[16] + vector[17]) / 30 * 3.0  # stronger, includes H3
    central_boost = vector[15] / 10 * 0.75
    Y = (y_raw / 10) * y_multiplier + suppression_boost + central_boost
  
    if Y < 2.0:
        Y = Y * 0.6
   
    g_mean = np.mean(vector[18:])
    if g_mean < -1.0:
        rule13_parasitism = max(0, 30 + (-g_mean * 10))
    else:
        rule13_parasitism = max(0, 5 + (g_mean / 10 * 5))
   
    parasitism_penalty = (rule13_parasitism / 100) * 1.5
    Y = Y - parasitism_penalty
   
    X = (x_raw / 10) * x_extra_weight - max(0, (np.mean(vector[:18]) - 5.5) / 1.8)
   
    if X > 0.6:
        Y = Y * 0.8
   
    point_2d = np.array([X, Y])
    distances = np.array([euclidean(point_2d, c) for c in fixed_centres])
    inv_dist = 1 / (np.maximum(distances, 1e-8) ** 10)
    splatter_percent = (inv_dist / inv_dist.sum()) * 100
   
    return (X, Y), splatter_percent, rule13_parasitism

def run_full_simulation(vector, case_name):
    coord, splatter, rule13_p = compute_coordinates(vector)
    X, Y = coord
    dom_zone = splatter.argmax() + 1
   
    print(f"\n--- {case_name} ---")
    print(f"X: {X:.2f} | Y: {Y:.2f} | Zone: {dom_zone}")
    print(f"Rule-13 Parasitism Proxy: {rule13_p:.1f}%")
   
    longevity = 160 + (vector[2] * 2) + (-vector[18] * 4)  # higher base for historical bracket
    longevity = longevity / (1 + rule13_p / 300)  # softened penalty
    print(f"Estimated longevity window: ~{int(longevity*0.7)}–{int(longevity*1.3)} years")
    print(f" (Sensitivity: ±20% on parasitism would shift range to ~{int(longevity*0.7*0.8)}–{int(longevity*1.3*1.2)} years)")
   
    # Lattice
    dominance = np.zeros((15, 6))
    dominance[:, 0] = 95  # baseline mutualism
   
    # Rule-13 row mapping
    dominance[12, 0] = max(0, 100 - rule13_p - 5)
    dominance[12, 2] = rule13_p
   
    # Normalize Row 13
    row_sum = dominance[12, :].sum()
    if row_sum > 0:
        dominance[12, :] = (dominance[12, :] / row_sum) * 100
   
    # Tweak 3: D1 parasitism bump in Row 3 (D1 row, assuming Row 3 maps to D1)
    dominance[3, 2] = 35  # parasitism leak from high D1 -7.2
    dominance[3, 0] = 60
    row_sum_d1 = dominance[3, :].sum()
    if row_sum_d1 > 0:
        dominance[3, :] = (dominance[3, :] / row_sum_d1) * 100
   
    plt.figure(figsize=(12, 9))
    sns.heatmap(dominance, annot=True, cmap="YlGnBu", fmt=".1f", cbar_kws={'label': '% Dominance'})
    plt.title(f"15×6 Master Grid: {case_name}\n(X: {X:.2f}, Y: {Y:.2f}, Rule-13: {rule13_p:.1f}%)")
    plt.ylabel("Base Rules (1–15)")
    plt.xlabel("Mutualism | Commensalism | Parasitism | Competition | Amensalism | Neutralism")
    plt.tight_layout()
   
    file_safe = case_name.lower().replace(" ", "_")[:40]
    output_path = f"tests/outputs/{file_safe}_lattice.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Success: Lattice saved to {output_path}")

# 4. EXECUTION
try:
    scores = load_metrics(csv_file)
    run_full_simulation(scores, label)
except Exception as e:
    print(f"Error during simulation: {e}")
