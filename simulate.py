import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean

fixed_centres = np.array([
    [1.00, -1.00], [0.70, -0.60], [0.40, -0.30], [0.20, 0.00], [0.00, 0.00],
    [-0.30, 0.20], [-0.60, 0.50], [-0.80, 0.80], [-1.00, 1.00], [0.90, 0.50]  # lower Y for last point
])

def load_metrics(csv_path):
    df = pd.read_csv(csv_path)
    print("Loaded df shape:", df.shape)
    print(df.head())
    if df.shape[0] == 0:
        raise ValueError("No data rows found")
    vector = df.iloc[0].values.astype(float)
    print("Extracted vector length:", len(vector))
    if len(vector) != 35:
        raise ValueError(f"Expected 35 metrics, got {len(vector)}")
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
        Y = Y * 0.6  # amplify downward pull for fragile systems

    g_mean = np.mean(vector[18:])
    rule13_parasitism = max(0, 50 - (g_mean / 10 * 50))
    parasitism_penalty = (rule13_parasitism / 100) * 1.5
    Y = Y - parasitism_penalty
    
    X = (x_raw / 10) * x_extra_weight
    
    adaptation_penalty = max(0, (np.mean(vector[:18]) - 5.5) / 1.8)  # threshold 5.5, division 1.8
    X = X - adaptation_penalty

    # ← Add this block here (same indentation level as X = ...) ←
    if X > 0.6:
        Y = Y * 0.8  # dampen Y for high adaptation cases
    
    point_2d = np.array([X, Y])
    
    distances = np.array([euclidean(point_2d, c) for c in fixed_centres])
    distances = np.maximum(distances, 1e-8)
    inv_dist = 1 / (distances ** 10)
    weights = inv_dist / inv_dist.sum()
    splatter_percent = weights * 100
    
    return (X, Y), splatter_percent

def text_summary(vector, case_name="Unknown Case"):
    coord, splatter = compute_coordinates(vector)
    X, Y = coord
    dom_zone = splatter.argmax() + 1
    dom_pct = splatter[dom_zone - 1]
    
    print(f"\n{case_name}")
    print("-" * 50)
    print(f"X: {X:.2f}")
    print(f"Y: {Y:.2f}")
    print(f"Dominant Zone: {dom_zone} ({dom_pct:.1f}%)")
    
    # Move g_mean here – before the loop that uses it
    g_mean = np.mean(vector[18:])  # full governance block (18–35)
    rule13_parasitism = max(0, 50 - (g_mean / 10 * 50))
    print(f"Rule-13 parasitism proxy: ~{rule13_parasitism:.0f}%")
    
    print("\nRow dominance (heuristic):")
    for r in range(15):
        if r < 5:
            pct = 70 + (np.mean(vector[5:8]) / 10 * 20) if len(vector) > 8 else 50
            dom = "Parasitism" if np.mean(vector[5:8]) < 0 else "Mutualism"
        elif r < 8:
            pct = 70 + (vector[9] / 10 * 20) if len(vector) > 9 else 50
            dom = "Parasitism" if vector[9] > 5 else "Mutualism"
        elif r == 12:
            pct = 80 if g_mean > 5 else 40
            dom = "Mutualism" if g_mean > 5 else "Parasitism"
        else:
            pct = 70 if vector[16] > 5 else 60
            dom = "Mutualism" if vector[16] > 5 else "Neutralism"
        pct = round(min(max(pct, 0), 100))
        print(f"  Row {r+1}: ~{pct}% {dom}")

    # Longevity calculation
    mutual_comp_avg = np.mean(vector[[5,6,7,8,9,11,12]]) / 10
    longevity_estimate = 100 / (1 + rule13_parasitism / 100) * (1 + mutual_comp_avg)
    longevity_low = longevity_estimate * 0.7
    longevity_high = longevity_estimate * 1.3
    print(f"Estimated longevity window (placeholder): ~{int(longevity_low)}–{int(longevity_high)} years")
    print(f"  (Sensitivity: ±20% on parasitism would shift range to ~{int(longevity_low*0.8)}–{int(longevity_high*1.2)} years)")

# Batch runner (change y_multiplier here to test values)
examples = [
    'examples/eusocial_ant_colony.csv',
    'examples/influenza_molecular.csv',
    'examples/modern_north_korea.csv',
    'examples/ussr_1917_1991_lifetime.csv',
    'examples/united_states_west_1971-2025.csv'
]

for example in examples:
    base_name = example.split('/')[-1].replace('.csv', '').replace('_', ' ').title()
    vector = load_metrics(example)
    text_summary(vector, base_name)
