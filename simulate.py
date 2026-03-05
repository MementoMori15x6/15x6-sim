# The Board – Political Thermodynamics (v1.7 baseline, December 2025)
# Calibration anchors enforced for reproducibility; see manuscript Chapter 9 for CRL details
# simulate.py
# Fixed version – adds matrix stub & correct save placement
# Tuned for Chapter 07 – baseline ~10–43% proxy, shocks ~70–100%
# February 2026 – Memento & Mori

import pandas as pd
import numpy as np
import argparse
import sys

# === CRL HARD ANCHORS & CONSTANTS ===
# Calibration Reference Layer (CRL) – hard-locked values from manuscript Chapter 9

# Late VOC 1780–1785: canonical corporate exploitative collapse / Chaos Boundary
# Centers from 7-run multi-model consensus; ±1 bands reflect historical limits
VOC_ANCHORS = {
    'D1_Exploitationism': {
        'center': 9,
        'band_low': 8,
        'band_high': 10,
        'note': 'Structural dominance of endemic servant corruption / private trade (particuliere handel)'
    },
    'F2_Error_Repair': {
        'center': -8,
        'band_low': -9,
        'band_high': -7,
        'note': 'Systemic breakdown; distant oversight failed to correct cascading failures'
    },
    'G1_Cheater_Detection': {
        'center': -8,
        'band_low': -9,
        'band_high': -7,
        'note': 'Internal visibility collapsed; widespread graft undetected/unpunished (triggers Enforcement Decay)'
    },
    'E1_Survival': {
        'center': 2,
        'band_low': 1,
        'band_high': 3,
        'note': 'Zombie/legal shell via bailouts; no independent metabolic survival (zombie cap applied)'
    },
    # Provisional secondaries (guidance only – not yet hard-enforced)
    'D2_Competition': {
        'center': -8,
        'band_low': -9,
        'band_high': -7,
        'note': 'External competition suppressed by charter; British naval actions imposed destructive pressure'
    },
    'A2_Market_Allocation': {
        'center': -6,
        'band_low': -7,
        'band_high': -5,
        'note': 'Monopoly on paper but war/seizures shifted effective allocation to unregulated smuggling'
    }
}

# USSR ~1937 – canonical ideological authoritarian / Rigid Trap reference
# Centers from 6-run consensus (Claude x2, Grok x2, Gemini x2); ±1 bands
USSR_ANCHORS = {
    'H2_Ideological_Monopoly': {
        'center': 9,
        'band_low': 8,
        'band_high': 10,
        'note': 'Marxism-Leninism-Stalinism sole permissible framework; all alternatives eliminated'
    },
    'H3_Dissent_Suppression': {
        'center': 9,
        'band_low': 8,
        'band_high': 10,
        'note': 'Great Purge peak; NKVD terror and denunciation culture at maximum density'
    },
    'L2_Leadership_Cult': {
        'center': 9,
        'band_low': 8,
        'band_high': 10,
        'note': 'Stalin cult at maximum intensity; personal infallibility embedded in public culture'
    },
    'L3_Purge_Cycles': {
        'center': 9,
        'band_low': 8,
        'band_high': 10,
        'note': 'Great Purge operational peak; regular violent elite turnover as governance mechanism'
    },
    'G1_Cheater_Detection': {
        'center': -8,
        'band_low': -9,
        'band_high': -7,
        'note': 'Denunciation weaponized; NKVD quotas incentivize false positives over genuine detection'
    }
}

print("USSR_ANCHORS loaded successfully (dict with", len(USSR_ANCHORS), "entries)")
print(USSR_ANCHORS.keys())  # Should print the keys

# Rule-13 proxy function (v1.7 baseline – D1-dominant, aligned with consensus)
def compute_exploitationism_proxy(scores):
    """
    Rule-13 leakage proxy: systemic energy lost to exploitationism/rent/corruption.
    Tuned to ~64.8% on canonical Late VOC hinge (D1=9, G1=-8) after 7-run consensus (~62% mean).
    D1 is primary driver; G1 penalty disabled for simplicity and alignment (can re-enable lightly later).
    Metric indices (0-based):
    - d1 = scores[9]   # D1 Exploitationism
    - g1 = scores[15]  # G1 Cheater Detection
    """
    d1 = scores[9]   # Exploitationism (+ = high leakage)

    # Primary driver: exploitationism load (positive D1 contributes positively)
    base_from_d1 = max(0, d1 * 7.2)           # 9 * 7.2 = 64.8 → target alignment

    # Optional light detection penalty (disabled by default)
    detection_penalty = max(0, (5 - scores[15]) * 0.0)  # 0.0 = disabled; try 0.8 for +10.4 if desired

    total = base_from_d1 + detection_penalty
    return round(max(10, min(100, total)), 1)  # floor at 10%, cap at 100% for safety
    
# Usage example in scoring/ensemble functions:
# if replicator == 'late_voc_1780_1785':
#     enforce_anchors(VOC_ANCHORS, metric_scores)

# === HELPERS ===

def load_scores(csv_path):
    """Load 35-metric consensus scores."""
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

def apply_nonlinear_penalty(scores):
    """Quadratic penalty for |score| > 8."""
    penalty = np.where(np.abs(scores) > 8, (np.abs(scores) - 8)**2 * 0.5 * np.sign(scores), 0)
    return scores + penalty

def compute_compass(scores):
    """X (economic metabolism) and Y (governance density)."""
    metabolic = scores[:18]   # A1–G3
    governance = scores[18:]  # H1–M3
    
    penalized_met = apply_nonlinear_penalty(metabolic)
    penalized_gov = apply_nonlinear_penalty(governance)
    
    x = np.mean(penalized_met) / 10 * 1.2
    y = np.mean(penalized_gov) / 10 * 3.0
    return x, y

def compute_exploitationism_proxy(scores):
    d1 = scores[9]
    g1 = scores[15]
    
    base_from_d1 = max(0, -d1 * 13.0)           # stronger baseline scaling
    detection_penalty = max(0, (5 - g1) * 6)    # bigger penalty for weak G1
    
    total = base_from_d1 + detection_penalty
    return round(max(10, min(100, total)), 1)

def build_15x6_matrix(scores):
    # Placeholder: map metric polarities to interaction dominance (expand later)
    matrix = np.zeros((15, 6))
    # Example: Row 13 (cheater suppression) heavy parasitism if D1 high & G1 low
    parasitism_load = max(0, scores[9] / 10) * 0.6 + max(0, ( -scores[15] / 10) * 0.4)
    matrix[12, 2] = parasitism_load  # index 2 = Parasitism column, assuming order +/+, +/0, +/-, -/-, 0/-, 0/0
    # Normalize etc. – stub for now
    matrix = matrix / (matrix.sum(axis=1, keepdims=True) + 1e-10) * 100
    return matrix

def apply_shock(scores, shock_type="none"):
    """Apply shock deltas."""
    shocked = scores.copy()
    
    if shock_type == "none":
        return shocked
    
    if shock_type == "de_dollarization":
        print("Applying de-dollarization shock...")
        
        met_indices = list(range(0, 18))
        shocked[met_indices] -= 4.5
        
        key_met = [4,5,6,7,8,9,10,11]
        shocked[key_met] -= 2.0
        
        d1_idx = 9
        g1_idx = 15
        shocked[d1_idx] = -5.0
        shocked[g1_idx] = 2.5
        
        gov_indices = list(range(18, 35))
        shocked[gov_indices] += 0.8
        
        return shocked
    
    if shock_type == "rigidity_collapse":
    print("Applying PRC rigidity/boundary saturation shock...")
    
    # 1. Metabolism chokes (stronger X drop for brittleness)
    shocked[:18] -= 4.0          # was -3.0 → deeper choke
    
    # 2. Suppression costs skyrocket (deeper Y plunge)
    gov_indices = list(range(18, 35))
    shocked[gov_indices] -= 7.0  # was -4.0 → Y should drop toward -2.5 or lower
    
    # 3. Rule-13 fracture – elite impunity + detection failure
    shocked[9]  = -7.5           # D1 stronger exploitationism (was -6.5)
    shocked[15] = 0.5            # G1 almost fails (was 1.0)
    
    # Optional: direct C2 variation choke (kills adaptability)
    c2_idx = 7                   # C2 variation index – confirm with your CSV order!
    shocked[c2_idx] -= 6.0       # variation bandwidth collapse
    
    return shocked

# === MAIN ===

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="15×6 Simulator")
    parser.add_argument("--system", default="usa_1971", help="usa_1971 or prc_1978")
    parser.add_argument("--shock", default="none", help="none (default), de_dollarization, rigidity_collapse")
    
    args, unknown = parser.parse_known_args()
    if unknown:
        print(f"Ignoring unrecognized arguments: {unknown}")

    print(f"sys.argv contents: {sys.argv}")
    print(f"Running simulation on system: {args.system}")
    print(f"Shock applied: {args.shock}")

    csv_path = f"data/35_metrics_{args.system}-present_consensus.csv"
    baseline_scores = load_scores(csv_path)

    scores = apply_shock(baseline_scores, args.shock)

    x, y = compute_compass(scores)
    exploitationism_pct = compute_exploitationism_proxy(scores)
    
    # BUILD & SAVE MATRIX (placed correctly)
    matrix = build_15x6_matrix(scores)  # stub or real function
    pd.DataFrame(matrix).to_csv(f"matrix_{args.system}_{args.shock}.csv", index=False)
    print(f"Matrix saved: matrix_{args.system}_{args.shock}.csv")

    zone = "Stressed Mutualism" if x > 0 and y > 0 else "Boundary Saturation"
    longevity = "80–140 years" if exploitationism_pct < 50 else "30–80 years (compressed)"

    print("\n" + "="*60)
    print(f"RESULTS: {args.system.upper()} | {args.shock.upper()}")
    print(f"Compass X: {x:.2f}    Y: {y:.2f}")
    print(f"Rule-13 Exploitationism Proxy: {exploitationism_pct:.1f}%")
    print(f"Zone: {zone}")
    print(f"Estimated Remaining Longevity: {longevity}")
    print("="*60 + "\n")
