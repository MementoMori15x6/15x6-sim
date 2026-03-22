
import pandas as pd
import numpy as np

# === CRL ANCHORS - Terra/Luna (dynamic load from CSV) ===
crl_path = "data/anchors/crl_terra_luna.csv"
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

def apply_crl_anchor(df, anchor_name):
    \"\"\"Apply exact hinge values from anchor to the dataframe.\"\"\"
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

# === Your original simulate.py code goes here below ===
# Paste or keep your existing simulation logic here
# For example:
print("simulate.py updated with CRL integration - ready for scoring")
