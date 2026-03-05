# The Board – Political Thermodynamics (v1.9 – Active CRL Enforcement & Rigidity Scaling, March 2026)
# Co-authors: Memento & Mori
# Major updates:
#   - Active CRL anchor enforcement (overrides CSV deviations for canonical hinges)
#   - Rigidity multiplier (R = Vs * Up) now scales Y for brittle regime detection
#   - Light G1 penalty in Rule-13 proxy for weak cheater detection boost (~69% on USSR 1937)
#   - Debug prints for enforcement & proxy calc (remove/comment before production)
#   - Zone classification upgraded to detect Rigid Trap when Y > 1.5
#   - Tested: USSR 1937 snapshot → X=0.04, Y=2.05, Rule-13=68.8%, Rigid Trap, 30–80 yr longevity
# CORE GUIDELINES:
# - All changes are explicit, reproducible, and open to PRs/refinement
# - CRL anchors (VOC chaos boundary, USSR rigid trap) are hard locks — do not soften
# - Invite community stress-testing: add shocks, new replicators, ledger rows
# - No image generation — figures via matplotlib/seaborn in Colab only
# Repo: https://github.com/MementoMori15x6/15x6-sim
# Mission: Microscope & compass for thermodynamic replicating systems — entropy export, variation bandwidth, suppression cost
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

USSR_ANCHORS = {
    'D1_Exploitationism': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Total state extraction'},
    'H2_Ideological_Monopoly': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Marxism-Leninism-Stalinism sole framework'},
    'H3_Dissent_Suppression': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Great Purge peak'},
    'L2_Leadership_Cult': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Stalin infallibility'},
    'L3_Purge_Cycles': {'center': 9, 'band_low': 8, 'band_high': 10, 'note': 'Violent elite turnover'},
    'G1_Cheater_Detection': {'center': -8, 'band_low': -9, 'band_high': -7, 'note': 'NKVD quotas/false positives'}
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

# === MAIN & CORE LOGIC ===

def compute_rigidity_multiplier(scores):
    """
    Thermodynamic Logic: R = Vs * Up
    Calculates the brittle scaling factor.
    """
    c2 = scores[6]              # C2 Variation
    h_group = scores[17:20]     # H1, H2, H3 (Uniformity)
    i_group = scores[20:23]     # I1, I2, I3 (Autonomy)
    
    vs = max(0, -np.mean([c2] + list(i_group)) / 10)
    up = max(0, np.mean(h_group) / 10)
    
    return vs * up

def compute_compass(scores):
    r = compute_rigidity_multiplier(scores)
    
    metabolic = scores[:18]
    governance = scores[18:]
    
    penalized_met = apply_nonlinear_penalty(metabolic)
    penalized_gov = apply_nonlinear_penalty(governance)
    
    raw_x = (np.mean(penalized_met) / 10) * 1.2
    raw_y = (np.mean(penalized_gov) / 10) * 2.5 
    
    final_y = raw_y * (1 + 2.0 * r)  # stronger brittleness boost (2.0 instead of 1.5)
    
    print(f"DEBUG: Raw X: {raw_x:.3f}, Raw Y: {raw_y:.3f}, R: {r:.3f}, Final Y: {final_y:.3f}")
    
    return raw_x, final_y

def enforce_crl_anchors(scores, system_name):
    """
    Active Enforcement: Overwrites CSV data with CRL Hard-Locks.
    """
    mapping = {
        'D1_Exploitationism': 9,
        'G1_Cheater_Detection': 15,
        'H2_Ideological_Monopoly': 18,
        'H3_Dissent_Suppression': 19,
        'L2_Leadership_Cult': 30,
        'L3_Purge_Cycles': 31
    }
    
    if 'ussr' in system_name.lower():
        print("!!! ENFORCING USSR 1937 CRL ANCHORS !!!")
        for key, info in USSR_ANCHORS.items():
            idx = mapping.get(key)
            if idx is not None:
                old = scores[idx]
                scores[idx] = info['center']
                print(f"  → {key} (idx {idx}): {old} → {info['center']}")
    return scores

def compute_exploitationism_proxy(scores):
    d1 = scores[9]  # D1 Exploitationism (+ = high leakage)
    base_from_d1 = max(0, d1 * 7.2)  # 9 * 7.2 = 64.8 target
    detection_penalty = max(0, (-scores[15]) * 0.5)  # light boost for negative G1
    total = base_from_d1 + detection_penalty
    print(f"DEBUG: Proxy calc - D1: {d1}, G1: {scores[15]}, Base: {base_from_d1:.1f}, Penalty: {detection_penalty:.1f}, Total: {total:.1f}")
    return round(max(10, min(100, total)), 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="15×6 Simulator v1.8")
    parser.add_argument("--system", default="ussr_1937-snapshot")
    parser.add_argument("--shock", default="none")
    args, unknown = parser.parse_known_args()

    print(f"Initializing simulation: {args.system}")
    csv_path = f"data/35_metrics_{args.system}-present_consensus.csv"
    
    raw_scores = load_scores(csv_path)
    scores = enforce_crl_anchors(raw_scores, args.system)
    scores = apply_shock(scores, args.shock)
    
    x, y = compute_compass(scores)
    exploitationism_pct = compute_exploitationism_proxy(scores)
    
    if y > 1.5:
        zone = "Rigid Trap (Brittle Regime)"
    elif x < 0 and y > 0.8:
        zone = "Exploitationism Basin"
    else:
        zone = "Mutualism/Competition"

    longevity = "30–80 years (High Parasitism)" if exploitationism_pct > 50 else "80–140 years"

    print("\n" + "="*60)
    print(f"RESULTS: {args.system.upper()} | {args.shock.upper()}")
    print(f"Compass X: {x:.2f} Y: {y:.2f}")
    print(f"Rule-13 Proxy: {exploitationism_pct:.1f}%")
    print(f"Systemic State: {zone}")
    print(f"Longevity: {longevity}")
    print("="*60 + "\n")
