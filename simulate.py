#!/usr/bin/env python3
import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output dir exists
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
        vector = df.iloc[:, 2].astype(float).values  # fallback
    
    print(f"Extracted {len(vector)} numeric scores")
    if len(vector) != 35:
        raise ValueError(f"Expected 35 scores, got {len(vector)}")
    
    return vector

def compute_coordinates(vector, y_multiplier=2.5, x_extra_weight=1.0):
    if len(vector) != 35:
        raise ValueError("Expected 35 metrics")
   
    extreme_pos = vector > 8
    extreme_neg = vector < -8
    penalty_pos = extreme_pos * (vector - 8) ** 2 * 0.8
    penalty_neg = extreme_neg * (vector + 8) ** 2 * 0.8
    adjusted = vector + penalty_pos + penalty_neg
   
    x_raw = np.mean(adjusted[:18])
    y_raw = np.mean(adjusted[18:])
   
    suppression_boost = (vector[14] + vector[16]) / 20 * 1.5
    central_boost = vector[15] / 10 * 0.75
    Y = (y_raw / 10) * y_multiplier + suppression_boost + central_boost
   
    if Y < 2.0:
        Y = Y * 0.6
    
    g_mean = np.mean(vector[18:])
    if g_mean < 0:
        rule13_parasitism = max(0, 5 + (g_mean / 10 * 5))  # biology tune: low parasitism for negative g_mean
    else:
        rule13_parasitism = max(0, 50 - (g_mean / 10 * 50))
    
    parasitism_penalty = (rule13_parasitism / 100) * 1.5
    Y = Y - parasitism_penalty
   
    X = (x_raw / 10) * x_extra_weight
   
    adaptation_penalty = max(0, (np.mean(vector[:18]) - 5.5) / 1.8)
    X = X - adaptation_penalty
    
    if X > 0.6:
        Y = Y * 0.8
    
    point_2d = np.array([X, Y])
    
    distances = np.array([euclidean(point_2d, c) for c in fixed_centres])
    distances = np.maximum(distances, 1e-8)
    inv_dist = 1 / (distances ** 10)
    weights = inv_dist / inv_dist.sum()
    splatter_percent = weights * 100
    
    return (X, Y), splatter_percent, rule13_parasitism

def text_summary(vector, case_name="Unknown Case"):
    coord, splatter, rule13_p = compute_coordinates(vector)
    X, Y = coord
    dom_zone = splatter.argmax() + 1
    print(f"\n--- {case_name} ---")
    print(f"X: {X:.2f} | Y: {Y:.2f} | Zone: {dom_zone}")
    print(f"Rule-13 Parasitism Proxy: {rule13_p:.1f}%")

    # Add longevity estimate
    mutual_comp_avg = np.mean(vector[[5,6,7,8,9,11,12]]) / 10
    longevity_estimate = 120 + (vector[2] * 2) + (-vector[18] * 4)  # base + C3 persistence bonus + G1 cheater detection bonus
    longevity_estimate = longevity_estimate / (1 + rule13_parasitism / 100)
    longevity_low = longevity_estimate * 0.7
    longevity_high = longevity_estimate * 1.3
    print(f"Estimated longevity window: ~{int(longevity_low)}–{int(longevity_high)} years")
    print(f" (Sensitivity: ±20% on parasitism would shift range to ~{int(longevity_low*0.8)}–{int(longevity_high*1.2)} years)")
    
# Run ants only
try:
    csv_file = "examples/eusocial_ant_colony.csv"
    scores = load_metrics(csv_file)
    text_summary(scores, "Ants Consensus Baseline")

    # Heatmap Generation
    dominance = np.zeros((15, 6))
    dominance[:, 0] = 95  # Perfect lattice mutualism
    dominance[12, 0] = 98 # Rule 13 strong suppression
    dominance[12, 2] = 2  # Residual parasitism
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(dominance, annot=True, cmap="YlGnBu")
    plt.title("Figure 3.1: The Perfect Lattice (Ant Baseline)")
    plt.ylabel("Base Rules (1–15)")
    plt.xlabel("Mutualism | Commensalism | Parasitism | Competition | Amensalism | Neutralism")
    plt.tight_layout()
    plt.savefig("tests/outputs/ants_consensus_lattice.png")
    plt.close()
    print("Success: Grid saved to tests/outputs/ants_consensus_lattice.png")
except Exception as e:
    print(f"Error: {e}")
