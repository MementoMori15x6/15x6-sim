# /scripts/ – Helper Tools & Extensions

This folder is reserved for utility scripts that extend the core `simulate.py` engine.

Current status (March 2026): empty / under development.

Planned contents (when ready):
- ensemble_runner.py — batch stochastic runs (n=100+ with Gaussian noise)
- bifurcation_scanner.py — metric sweeps (±20% increments, critical crossing detection)
- sensitivity_matrix.py — normalized delta impact on longevity/proxy/Row-13
- batch_anchors.py — run all triangulation anchors at once
- plot_utils.py — matplotlib helpers for phase-space scatter, drift paths, hazard curves

Contributions welcome:
- PR a new script with clear docstring + usage example
- Add tests or Colab notebook demo in /notebooks/
- Keep scripts modular and importable (use `if __name__ == "__main__":` for CLI)

Once populated, run examples will live here:
```bash
python scripts/ensemble_runner.py data/anchors/usa_1789_anchor.csv --n 100 --noise-std 0.1
