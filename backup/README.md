# backup – Archived Versions of simulate.py

This root-level folder archives historical iterations of the core simulation script `simulate.py` — the engine for 35-metric compass calculations, 15×6 grid heatmaps, X,Y positioning, splatter %, Rule-13 exploitationism %, rigidity penalties, and shock simulations.

**Do not use or run files from here for active work** — the current canonical version lives in `/scripts/simulate.py`.

## Purpose
- Preserve the evolutionary history of calibration parameters, functions, and logic (e.g., amp factors, power-law splatter, non-linear penalties, rigidity banked features).
- Allow diffing/regression checks: compare old vs current to trace changes (e.g., pre-VOC lattice tweaks, PRC shock additions).
- Enable recovery if a major refactor goes sideways.

## Naming Patterns (historical)
- Timestamped: `simulate_YYYYMMDD_HH:MM.py` — snapshots from specific sessions.
- Versioned: `simulate_vX.Y_*.py` — milestone releases (e.g., v0.4 for VOC lattice support, v1.7 baseline).
- Descriptive: e.g., `simulate_pre_prc_shock_*.py`, `simulate_1.9_CRL_enforce.py` — feature/branch indicators.

All archived content is provisional and historical — superseded by the active script. Calibration details in current `simulate.py` are the source of truth for manuscript figures, ledger scores, and diagnostics.

If a specific old version inspires a change, copy relevant snippets to the active file and note the origin in comments.

Memento mori. 🚀
