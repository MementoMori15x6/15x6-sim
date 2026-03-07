# /scripts/bifurcation_scanner.py
# Stub for metric sweep & critical crossing detection
# Planned: ±20% sweep on selected metrics, track Rule-13 >30%, longevity <500y crossings

def sweep_metric(csv_path, metric_name, range_pct=20, steps=20):
    """Sweep a single metric ±range_pct in steps, recompute compass & proxy."""
    # TODO: load CSV, apply perturbations, run simulate.py core, collect outputs
    print(f"Stub: Sweeping {metric_name} on {csv_path}")
    # Future: return list of (delta, X, Y, proxy, longevity)
    pass

if __name__ == "__main__":
    print("Bifurcation scanner stub – implement sweep logic here")

