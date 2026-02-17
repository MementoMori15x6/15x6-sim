%%writefile simulate.py
import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean

fixed_centres = np.array([
    [1.00, -1.00], [0.70, -0.60], [0.40, -0.30], [0.20, 0.00], [0.00, 0.00],
    [-0.30, 0.20], [-0.60, 0.50], [-0.80, 0.80], [-1.00, 1.00], [0.90, 0.90]
])

def load_metrics(csv_path):
    df = pd.read_csv(csv_path)
    if 'score' in df.columns:
        return df['score'].astype(float).values
    if len(df.columns) >= 2:
        if not pd.api.types.is_numeric_dtype(df.iloc[:, 1]):
            df = pd.read_csv(csv_path, skiprows=1)
        return df.iloc[:, -1].astype(float).values
    raise ValueError("CSV format not recognized")

def compute_coordinates(vector, y_multiplier=6.5, x_extra_weight=1.0):
    if len(vector) != 35:
        raise ValueError("Expected 35 metrics")
    
    # Boost extremes: positives push right (exploitation), negatives push right (failure = parasitism)
    extreme_pos = vector > 8
    extreme_neg = vector < -8
    penalty_pos = extreme_pos * (vector - 8) ** 2 * 0.8
    penalty_neg = extreme_neg * (vector + 8) ** 2 * 0.8  # negative → right (failure = exploitation)
    adjusted = vector + penalty_pos + penalty_neg
    
    x_raw = np.mean(adjusted[:18])
    y_raw = np.mean(adjusted[18:])
    
    # Strong suppression boost for Y (G1 + G3)
    suppression_boost = (vector[14] + vector[16]) / 20 * 5.5
    central_boost = vector[15] / 10 * 3.0
    Y = (y_raw / 10) * y_multiplier + suppression_boost + central_boost
    
    X = (x_raw / 10) * x_extra_weight
    
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
    
    g_mean = np.mean(vector[14:17]) if len(vector) > 17 else 0
    rule13_parasitism = max(0, 30 - (g_mean / 10 * 30))
    print(f"Rule-13 parasitism proxy: ~{rule13_parasitism:.0f}%")
    
    print("\nRow dominance (heuristic):")
    for r in range(15):
        if r < 5:
            pct = 70 + (vector[5:8].mean() / 10 * 20) if len(vector) > 8 else 50
            dom = "Parasitism" if vector[5:8].mean() < 0 else "Mutualism"
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

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
        vector = load_metrics(csv_path)
        case_name = csv_path.split('/')[-1].replace('.csv', '').replace('_', ' ').title()
        text_summary(vector, case_name)
    else:
        print("Usage: python simulate.py path/to/your.csv")
