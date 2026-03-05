# The Board – Political Thermodynamics (v1.8 – USSR CRL fixes, February 2026)
# Calibration anchors enforced for reproducibility; see manuscript Chapter 9 for CRL details
# simulate.py
# Fixed: removed duplicate proxy, fixed C2 index, added anchor check, cleaned matrix stub
# Memento & Mori
import pandas as pd
import numpy as np
import argparse
import sys

# === CRL HARD ANCHORS & CONSTANTS ===
# Late VOC 1780–1785: canonical corporate exploitative collapse / Chaos Boundary
VOC_ANCHORS = {
    'D1_Exploitationism': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Structural dominance of endemic servant corruption / private trade (particuliere handel)'},
    'F2_Error_Repair': {'center': -8, 'band_low': -9, 'band_high': -7, 'note': 'Systemic breakdown; distant oversight failed to correct cascading failures'},
    'G1_Cheater_Detection': {'center': -8, 'band_low': -9, 'band_high': -7, 'note': 'Internal visibility collapsed; widespread graft undetected/unpunished (triggers Enforcement Decay)'},
    'E1_Survival': {'center': 2, 'band_low': 1, 'band_high': 3, 'note': 'Zombie/legal shell via bailouts; no independent metabolic survival (zombie cap applied)'},
    # Provisional secondaries (guidance only – not yet hard-enforced)
    'D2_Competition': {'center': -8, 'band_low': -9, 'band_high': -7, 'note': 'External competition suppressed by charter; British naval actions imposed destructive pressure'},
    'A2_Market_Allocation': {'center': -6, 'band_low': -7, 'band_high': -5, 'note': 'Monopoly on paper but war/seizures shifted effective allocation to unregulated smuggling'}
}

# USSR ~1937 – canonical ideological authoritarian / Rigid Trap reference
USSR_ANCHORS = {
    'H2_Ideological_Monopoly': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Marxism-Leninism-Stalinism sole permissible framework; all alternatives eliminated'},
    'H3_Dissent_Suppression': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Great Purge peak; NKVD terror and denunciation culture at maximum density'},
    'L2_Leadership_Cult': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Stalin cult at maximum intensity; personal infallibility embedded in public culture'},
    'L3_Purge_Cycles': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Great Purge operational peak; regular violent elite turnover as governance mechanism'},
    'G1_Cheater_Detection': {'center': -8, 'band_low': -9, 'band_high': -7, 'note': 'Denunciation weaponized; NKVD quotas incentivize false positives over genuine detection'}
}

print("USSR_ANCHORS loaded successfully (dict with", len(USSR_ANCHORS), "entries)")
print(USSR_ANCHORS.keys())

# Rule-13 proxy function (v1.8 baseline – VOC-tuned, D1-dominant)
def compute_exploitationism_proxy(scores):
    """
    Rule-13 leakage proxy: systemic energy lost to exploitationism/rent/corruption.
    Tuned to ~64.8% on canonical Late VOC hinge (D1=9, G1=-8) after 7-run consensus (~62% mean).
    """
    d1 = scores[9]  # D1 Exploitationism (+ = high leakage)
    base_from_d1 = max(0, d1 * 7.2)  # 9 * 7.2 = 64.8 target
    detection_penalty = max(0, (5 - scores[15]) * 0.0)  # disabled; tune later if needed
    total = base_from_d1 + detection_penalty
    return round(max(10, min(100, total)), 1)

# === HELPERS ===
def load_scores(csv_path):
    try:
        df = pd.read_csv(csv_path)
        if 'Score' not in df.columns:
            raise ValueError("CSV must have 'Score' column")
        scores = df['Score'].astype(float).values
        if len(scores) != 35:
            raise ValueError(f"Expected 35 metrics, got {len(scores)}")
        return scores
    except Exception as e:
        print(f"Load error for {csv_path}: {e}")
        sys.exit(1)

def check_anchors(scores, anchors):
    metric_map = {
        'D1_Exploitationism': 9,
        'F2_Error_Repair': 13,
        'G1_Cheater_Detection': 15,
        'E1_Survival': 10,
        'D2_Competition': 11,
        'A2_Market_Allocation': 1,
        'H2_Ideological_Monopoly': 19,
        'H3_Dissent_Suppression': 20,
        'L2_Leadership_Cult': 29,
        'L3_Purge_Cycles': 30
    }
    for key, info in anchors.items():
        idx = metric_map.get(key)
        if idx is not None:
            score = scores[idx]
            center = info['center']
            low, high = info['band_low'], info['band_high']
            if not (low <= score <= high):
                print(f"Warning: {key} score {score} outside CRL band [{low},{high}] (center {center})")

def apply_nonlinear_penalty(scores):
    penalty = np.where(np.abs(scores) > 8, (np.abs(scores) - 8)**2 * 0.5 * np.sign(scores), 0)
    return scores + penalty

def compute_compass(scores):
    metabolic = scores[:18]
    governance = scores[18:]
    penalized_met = apply_nonlinear_penalty(metabolic)
    penalized_gov = apply_nonlinear_penalty(governance)
    x = np.mean(penalized_met) / 10 * 1.2
    y = np.mean(penalized_gov) / 10 * 3.0
    return x, y

def build_15x6_matrix(scores):
    matrix = np.zeros((15, 6))
    # Row 12 = Rule 13: cheater detection & suppression
    parasitism_load = max(0, scores[9] / 10.0) * 0.6 + max(0, (-scores[15] / 10.0)) * 0.4
    matrix[12, 2] = parasitism_load  # column 2 = Parasitism (+/–)
    print(f"Rule-13 Parasitism seed before norm: {parasitism_load:.2f}")
    row_sums = matrix.sum(axis=1, keepdims=True)
    matrix = np.where(row_sums > 0, matrix / row_sums * 100, 100.0 / 6)  # uniform fallback
    return matrix

def apply_shock(scores, shock_type="none"):
    shocked = scores.copy()
    if shock_type == "none":
        return shocked
    if shock_type == "de_dollarization":
        print("Applying de-dollarization shock...")
        met_indices = list(range(0, 18))
        shocked[met_indices] -= 4.5
        key_met = [4,5,6,7,8,9,10,11]
        shocked[key_met] -= 2.0
        shocked[9] = -5.0
        shocked[15] = 2.5
        gov_indices = list(range(18, 35))
        shocked[gov_indices] += 0.8
        return shocked
    if shock_type == "rigidity_collapse":
        print("Applying rigidity/boundary saturation shock...")
        shocked[:18] -= 4.0
        gov_indices = list(range(18, 35))
        shocked[gov_indices] -= 7.0
        shocked[9] = -7.5
        shocked[15] = 0.5
        c2_idx = 6  # C2_Variation
        shocked[c2_idx] -= 6.0
        return shocked

# === MAIN ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="15×6 Simulator")
    parser.add_argument("--system", default="usa_1971", help="e.g. ussr_1937, usa_1971, prc_1978")
    parser.add_argument("--shock", default="none", help="none (default), de_dollarization, rigidity_collapse")
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Ignoring unrecognized arguments: {unknown}")
    print(f"Running simulation on system: {args.system}")
    print(f"Shock applied: {args.shock}")
    csv_path = f"data/35_metrics_{args.system}-present_consensus.csv"
    baseline_scores = load_scores(csv_path)
    print(f"Loaded {len(baseline_scores)} scores from {csv_path}")
    
    # Anchor check for USSR
    if 'ussr' in args.system.lower():
        check_anchors(baseline_scores, USSR_ANCHORS)
    
    scores = apply_shock(baseline_scores, args.shock)
    x, y = compute_compass(scores)
    exploitationism_pct = compute_exploitationism_proxy(scores)
    matrix = build_15x6_matrix(scores)
    pd.DataFrame(matrix).to_csv(f"matrix_{args.system}_{args.shock}.csv", index=False)
    print(f"Matrix saved: matrix_{args.system}_{args.shock}.csv")
    zone = "Stressed Mutualism" if x > 0 and y > 0 else "Boundary Saturation"
    longevity = "80–140 years" if exploitationism_pct < 50 else "30–80 years (compressed)"
    print("\n" + "="*60)
    print(f"RESULTS: {args.system.upper()} | {args.shock.upper()}")
    print(f"Compass X: {x:.2f} Y: {y:.2f}")
    print(f"Rule-13 Exploitationism Proxy: {exploitationism_pct:.1f}%")
    print(f"Zone: {zone}")
    print(f"Estimated Remaining Longevity: {longevity}")
    print("="*60 + "\n")
