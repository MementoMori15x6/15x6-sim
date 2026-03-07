# Figures – Visual Diagnostics for The Board

This folder contains all generated figures for the manuscript “The Board: Political Thermodynamics” (December 2025 draft, ongoing).  
All images are created via reproducible Python code (matplotlib/seaborn) in the `/notebooks` directory — no external image generation tools used, per project policy.

## Contents Overview

- **Root files**: Primary manuscript figures, named `fig_{chapter}_{section}_{short_description}.png`  
  Examples:  
  - `fig_1_1_payoff_matrix_updated.png` → Chapter 1 payoff matrix  
  - `fig_2_1_late_republic_heatmap.png` → Roman Republic baseline heatmap  
  - `fig_7_3_usa_vs_prc_rc1_heatmap.png` → USA/PRC comparison (rc1 calibration)  
  - `master_blank_15×6_grid_v4.png` → Blank template for new grids  

- **Subfolders**:
  - `banners/` → Repo-wide banners, headers, or promotional visuals  
  - `old/` → Archived/deprecated figures (renamed or superseded versions moved here to keep root clean)

## Generation & Reproducibility

Each figure is produced by running the corresponding notebook in `/notebooks` (e.g., `fig_2_3_principate_heatmap.ipynb` → `fig_2_3_principate_heatmap.png`).  
- Core script: `../scripts/simulate.py`  
- Calibration: current toy version (X amp 1.2, Y amp 2.5, power-law **10 splatter, rigidity penalty banked)  
- To regenerate: Open notebook in Colab → Run all → Export/save PNG from plot cell  

If adding a new figure:
1. Create/extend a notebook in `/notebooks`  
2. Generate via `plt.savefig('fig_{ch}_{sec}_{desc}.png', dpi=300, bbox_inches='tight')`  
3. Commit to `/figures`  
4. Update this README if needed  

## Naming Convention (recommended)

- Use `fig_{chapter number}_{subsection}_{concise_description}.png`  
- Keep descriptions lowercase-with-underscores, avoid spaces  
- Include version if updated (e.g., `_updated`, `_v2`)  
- Special chars: Use `×` for 15×6, `–` for ranges (GitHub handles encoding)  

All figures provisional — tied to toy calibration and open to refinement via PRs (new attractors, shocks, ensembles, etc.).

These visuals are the microscope slides: heatmaps, drift curves, entropy exports, Rule-13 profiles — shining the light on persistence and fracture across scales.

Memento mori. 🚀
