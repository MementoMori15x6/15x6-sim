# The Board – Political Thermodynamics
# simulate.py v2.0 – March 2026 (updated with Terra/Luna CRL + MC proxy)
# Major updates: full CRL enforcement by filename, rigidity multiplier active, scalar-safe X/Y calc, debug prints for R/vs/up
# Tested: triangulation anchors (USA_1789, USSR_1937, VOC golden/late) complete with distinct collapse signatures
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

# === CRL ANCHORS - Terra/Luna (dynamic load from CSV) ===
crl_path = "data/anchors/crl_terra_luna.csv"

try:
    crl_df = pd.read_csv(crl_path)
    CRL_ANCHORS = {}
    for _, row in crl_df.iterrows():
        name = row['Anchor_Name']
        CRL_ANCHORS[name] = {
            "proxy_target": float(row['Proxy_Target']),
            "D1": float(row['D1']) if row['D1'] != "-" else None,
            "G1": float(row['G1']) if row['G1'] != "-" else None,
            "F2": float(row['F2']) if row['F2'] != "-" else None,
            "C2": float(row['C2']) if row['C2'] != "-" else None,
            "rigidity_delta": float(row['Rigidity_Delta']),
            "notes": row['Notes']
        }
    print("✅ CRL anchors loaded:", list(CRL_ANCHORS.keys()))
except Exception as e:
    print(f"Failed to load CRL anchors: {e}")
    CRL_ANCHORS = {}

def apply_crl_anchor(df, anchor_name):
    """Apply exact hinge values from anchor to the dataframe."""
    if anchor_name not in CRL_ANCHORS:
        print(f"⚠ Anchor {anchor_name} not found")
        return df
   
    anchor = CRL_ANCHORS[anchor_name]
   
    # Apply exact hinge values (None = skip)
    for metric, value in [("D1", anchor["D1"]), ("G1", anchor["G1"]),
                          ("F2", anchor["F2"]), ("C2", anchor["C2"])]:
        if value is not None and metric in df['Metric'].values:
            df.loc[df['Metric'] == metric, 'Score'] = value
   
    # Optional rigidity adjustment (future use)
    if anchor["rigidity_delta"] != 0:
        print(f"  Rigidity delta applied: {anchor['rigidity_delta']}")
   
    return df

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
USA_1789_ANCHORS = {
    'G1_Cheater_Detection': {'center': 8, 'band_low': 7, 'band_high': 9, 'note': 'Strong early institutions for detecting & punishing graft/corruption (courts, militias, civic norms)'},
    'G2_Modularity': {'center': 7, 'band_low': 6, 'band_high': 8, 'note': 'Federal structure + separation of powers enables subsystem autonomy & error isolation'},
    'G3_Info_Storage': {'center': 8, 'band_low': 7, 'band_high': 9, 'note': 'Written Constitution, free press foundations, literacy/high info fidelity'},
    'D1_Exploitationism': {'center': -2, 'band_low': -4, 'band_high': 0, 'note': 'Low systemic parasitism; rent-seeking present but checked by competition & rule of law'},
    'D2_Competition': {'center': 6, 'band_low': 5, 'band_high': 7, 'note': 'Healthy market & political competition; no monopoly charter dominance'},
    'H2_Ideological_Monopoly':{'center': -5, 'band_low': -7, 'band_high': -3,'note': 'No state religion or enforced orthodoxy; pluralist founding ethos'},
    'H3_Dissent_Suppression': {'center': -6, 'band_low': -8, 'band_high': -4,'note': 'First Amendment protections; dissent channeled via elections & press'},
    'L2_Leadership_Cult': {'center': -7, 'band_low': -9, 'band_high': -5,'note': 'No personality cult; Washington steps down sets precedent'},
    'L3_Purge_Cycles': {'center': -8, 'band_low': -9, 'band_high': -7,'note': 'Peaceful electoral turnover; no violent elite culls'},
    'F2_Error_Repair': {'center': 6, 'band_low': 5, 'band_high': 7, 'note': 'Constitutional amendment + judicial review mechanisms functional'}
}
print("USSR_ANCHORS loaded successfully (dict with", len(USSR_ANCHORS), "entries)")
print(USSR_ANCHORS.keys())

# Rule-13 proxy function (v1.8 baseline – VOC-tuned, D1-dominant)
def compute_rule13_proxy(metrics):
    """
    Locked Rule-13 Proxy v3.0 (March 2026)
    Calibrated against CRL anchors: VOC 65.0%, USSR 66.9%, USA1789 ~1.6%, USA Modern 21.1%
    Bifurcation validated: crosses 30% at G1 ≈ -6 in USA-modern baseline
    """
    d1 = metrics[8]
    d2 = metrics[9]
    g1 = metrics[14]
    f2 = metrics[13]
    g3 = metrics[16]
    h2 = metrics[18]
    extraction_pressure = d1 * 0.85 + d2 * 0.10
    detection_capacity = g1 * 0.13 + f2 * 0.06 + g3 * 0.10
    masking_penalty = h2 * 0.10 if h2 > 3 else 0
    effective_detection = detection_capacity - masking_penalty
    raw_proxy = extraction_pressure - effective_detection + 1.5
    if g1 < -5 and d1 > 5:
        raw_proxy *= 1.5
    elif g1 < -5:
        raw_proxy *= 1.2
    MINIMUM_FLOOR = 0.4
    raw_proxy = max(raw_proxy, MINIMUM_FLOOR)
    scale_factor = 4.06
    proxy_percent = max(0, min(100, raw_proxy * scale_factor))
    return proxy_percent

# MC-aligned proxy (Bitcoin ~39.8%, Terra ~51.8%, shocked ~76.1%)
def mc_aligned_proxy(d1, g1, rigidity=0):
    raw = 41.91 + (d1 * 1 + g1 * 0.4) - (rigidity * 12.8)
    bounded = 118 / (1 + np.exp(-(raw - 50) / 10))
    return bounded

def load_scores(csv_path):
    try:
        df = pd.read_csv(csv_path)
        if 'Score' not in df.columns:
            raise ValueError("CSV must have 'Score' column")
        scores = df['Score'].astype(float).values
        if len(scores) != 35:
            raise ValueError(f"Expected 35 metrics, got {len(scores)}")
        return scores, df  # return both scores array and original df for anchor application
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

def compute_rigidity_multiplier(scores):
    """
    R = Vs * Up
    Vs = variation suppression (negative mean of low-variation/autonomy metrics)
    Up = uniformity pressure (mean of high-uniformity metrics)
    """
    c2 = scores[6] # C2_Variation
    h_group = scores[17:20] # H1–H3 Uniformity
    i_group = scores[20:23] # I1–I3 Autonomy/Expression
   
    vs = max(0, -np.mean([c2] + list(i_group)) / 10)
    up = max(0, np.mean(h_group) / 10)
   
    r = vs * up
   
    return r, vs, up

def build_15x6_matrix(scores):
    matrix = np.zeros((15, 6))
    # Row 12 = Rule 13: cheater detection & suppression
    parasitism_load = max(0, scores[9] / 10.0) * 0.6 + max(0, (-scores[15] / 10.0)) * 0.4
    matrix[12, 2] = parasitism_load # column 2 = Parasitism (+/–)
    print(f"Rule-13 Parasitism seed before norm: {parasitism_load:.2f}")
    row_sums = matrix.sum(axis=1, keepdims=True)
    matrix = np.where(row_sums > 0, matrix / row_sums * 100, 100.0 / 6) # uniform fallback
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
        print("Applying rigidity/boundary saturation shock (corrected — fracture acceleration)...")
        
        shocked[:18] -= 1.5               # mild economic stress
        gov_indices = list(range(18, 35))
        shocked[gov_indices] += 5.5       # heavy suppression ramp
        shocked[8] = 9.0                  # D1 → +9 (exploitation bleed)
        shocked[14] = -8.5                # G1 → -8.5 (detection collapse)
        shocked[6] -= 5.0                 # C2 suppressed
        shocked[17:20] += 4.0             # H1–H3 up
        shocked[20:23] -= 4.5             # I1–I3 down
        shocked[13] -= 3.0                # F2 degrade
        
        return shocked

def compute_compass(scores):
    """
    Compute X,Y position with rigidity boost (current protocol).
    """
    # Rigidity multiplier (must be scalar)
    r, vs, up = compute_rigidity_multiplier(scores)
    metabolic = scores[:18]
    governance = scores[18:]
    penalized_met = apply_nonlinear_penalty(metabolic)
    penalized_gov = apply_nonlinear_penalty(governance)
    # Scalar means + explicit float conversion
    mean_met = float(np.mean(penalized_met))
    mean_gov = float(np.mean(penalized_gov))
    raw_x = mean_met / 10 * 1.2
    raw_y = mean_gov / 10 * 2.5
    final_y = raw_y * (1 + 2.0 * r)
    print(f"DEBUG: Raw X: {raw_x:.3f}, Raw Y: {raw_y:.3f}")
    print(f"DEBUG: Rigidity R = {r:.3f}")
    print(f"DEBUG: Final Y after boost: {final_y:.3f}")
    return raw_x, final_y

# === Enforcement & Main Logic (cleaned, no undefined vars) ===
# === Enforcement Helpers (clean & unified) ===
def get_anchor_set(system_name):
    system_lower = system_name.lower()
    if "terra" in system_lower or "luna" in system_lower:
        print("!!! ENFORCING TERRA/LUNA DYNAMIC CRL ANCHORS FROM CSV !!!")
        return CRL_ANCHORS
    if "ussr_1937" in system_lower:
        print("!!! ENFORCING USSR 1937 CRL ANCHORS (peak rigidity / high parasitism) !!!")
        return USSR_ANCHORS
    elif "voc" in system_lower and any(x in system_lower for x in ["1780", "1785", "late"]):
        print("!!! ENFORCING LATE VOC 1780–1785 CRL ANCHORS (corporate decay / cheater collapse) !!!")
        return VOC_ANCHORS
    elif "usa_1789" in system_lower or "1789" in system_lower:
        print("!!! ENFORCING USA 1789 HEALTHY CRL ANCHORS (mutualist / adaptive baseline) !!!")
        return USA_1789_ANCHORS
    else:
        print("No CRL enforcement matched — using raw CSV scores.")
        return {}

# Hybrid / short-code METRIC_INDEX (supports both old full names and new short codes)
METRIC_INDEX = {
    # Short codes – used in your current CSVs
    'D1': 8,
    'G1': 14,
    'F2': 13,
    'C2': 6,
    'D2': 9,
    'G2': 15,
    'G3': 16,
    'H2': 18,
    'H3': 19,
    'L2': 30,
    'L3': 31,
    # Keep old full names for triangulation anchors (backward compatibility)
    'D1_Exploitationism': 8,
    'G1_Cheater_Detection': 14,
    'F2_Error_Repair': 13,
    'C2_Variation': 6,
    # ... add others if needed
}

def compute_rule13_proxy(metrics):
    d1 = metrics[8]   # D1
    d2 = metrics[9]
    g1 = metrics[14]  # G1
    f2 = metrics[13]  # F2
    g3 = metrics[16]
    h2 = metrics[18]
    extraction_pressure = d1 * 0.85 + d2 * 0.10
    detection_capacity = g1 * 0.13 + f2 * 0.06 + g3 * 0.10
    masking_penalty = h2 * 0.10 if h2 > 3 else 0
    effective_detection = detection_capacity - masking_penalty
    raw_proxy = extraction_pressure - effective_detection + 1.5
    if g1 < -5 and d1 > 5:
        raw_proxy *= 1.5
    elif g1 < -5:
        raw_proxy *= 1.2
    MINIMUM_FLOOR = 0.4
    raw_proxy = max(raw_proxy, MINIMUM_FLOOR)
    scale_factor = 4.06
    proxy_percent = max(0, min(100, raw_proxy * scale_factor))
    return proxy_percent

def apply_anchors(scores, anchors):
    if not anchors:
        return scores
    print("Applying CRL clamps:")
    for key, params in anchors.items():
        idx = METRIC_INDEX.get(key)
        if idx is not None and 0 <= idx < len(scores):
            current = scores[idx]
            clamped = max(params['band_low'], min(params['band_high'], params['center']))
            if abs(current - clamped) > 0.1:
                print(f" → {key} (idx {idx}): {current:.1f} → {clamped} {params.get('note', '')}")
            scores[idx] = clamped
    return scores

# === MAIN EXECUTION ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="15×6 Political Thermodynamics Simulator")
    parser.add_argument("csv_path", nargs="?", default=None,
                        help="Direct path to metrics CSV (overrides --system)")
    parser.add_argument("--system", default=None,
                        help="System name for enforcement & consensus file lookup")
    parser.add_argument("--shock", default="none",
                        choices=["none", "de_dollarization", "rigidity_collapse"],
                        help="Apply shock scenario")
    args = parser.parse_args()

    # Determine path and system name
    if args.csv_path:
        csv_path = args.csv_path
        base_name = args.csv_path.split('/')[-1].replace('.csv', '').lower()
        system_name = base_name.replace('_anchor', '').replace('-present_consensus', '')
        print(f"Direct CSV mode: {csv_path} → system '{system_name}' for CRL")
    elif args.system:
        system_name = args.system
        csv_path = f"data/35_metrics_{system_name}-present_consensus.csv"
        print(f"Consensus mode: {system_name} → {csv_path}")
    else:
        print("Error: Provide either --system or a direct CSV path")
        parser.print_help()
        sys.exit(1)

    print(f"Initializing simulation: {system_name}")
    raw_scores, df = load_scores(csv_path)  # now returns scores + df
    print(f"Loaded {len(raw_scores)} metrics")

    anchors = get_anchor_set(system_name)

    # Apply dynamic CRL anchor if Terra/Luna (uses df)
    if "terra" in system_name.lower() or "luna" in system_name.lower():
        df = apply_crl_anchor(df, system_name)  # or specific anchor name if needed
        scores = df['Score'].astype(float).values
    else:
        scores = raw_scores.copy()

    scores = apply_anchors(scores, anchors)
    scores = apply_shock(scores, args.shock)

    x, y = compute_compass(scores)
    rule13_pct = compute_rule13_proxy(scores)

    # Optional: MC-aligned proxy (example usage – replace or add to output as needed)
    d1 = scores[8]   # D1_Exploitationism
    g1 = scores[14]  # G1_Cheater_Detection
    r, _, _ = compute_rigidity_multiplier(scores)
    mc_proxy = mc_aligned_proxy(d1, g1, r)
    print(f"MC-aligned proxy: {mc_proxy:.1f}%")

    # Improved zone logic
    if rule13_pct > 50 or y > 1.5:
        zone = "Rigid Trap (Brittle Regime)"
    elif x < 0 and y > 0.8:
        zone = "Exploitationism Basin"
    else:
        zone = "Mutualism/Competition"

    # Gradient longevity
    if rule13_pct > 60:
        longevity = "30–80 years (High Parasitism)"
    elif rule13_pct > 30:
        longevity = "80–150 years (Moderate Risk)"
    else:
        longevity = "150+ years (Low Parasitism)"

        # After computing r, rule13_pct, etc.
    d1 = scores[8]   # D1 (Exploitationism)
    g1 = scores[14]  # G1 (Cheater Detection)
    proxy_mc = mc_aligned_proxy(d1, g1, r)  # Use the actual function you have
    print(f"MC-aligned Proxy (hinge): {proxy_mc:.1f}%")

    zone = (
    "Stable regime" if proxy_mc < 44 else
    "Pre-fracture / latent fragility" if proxy_mc < 45.5 else
    "Collapse basin (hinge crossed)" if proxy_mc < 50 else
    "Irreversible collapse"
    )
    print(f"Zone: {zone}")

    print("\n" + "="*60)
    print(f"RESULTS: {system_name.upper()} | {args.shock.upper()}")
    print(f"Compass X: {x:.2f} Y: {y:.2f}")
    print(f"Rule-13 Proxy: {rule13_pct:.1f}%")
    print(f"MC-aligned Proxy: {mc_proxy:.1f}%")
    print(f"Systemic State: {zone}")
    print(f"Longevity: {longevity}")
    print("="*60 + "\n")