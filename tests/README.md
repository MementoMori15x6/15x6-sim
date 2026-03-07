# /tests/ – Diagnostic Workbench

This directory contains **validation, diagnostic, and calibration artifacts** for the 15×6 simulation pipeline in "The Board – Political Thermodynamics".

## Purpose

The files here are **not** part of the canonical baselines, manuscript figures, or core examples. Instead, they serve to:

- Test and verify `simulate.py` behavior across diverse cases
- Calibrate Rule-13 parasitism proxy, zone splatter logic, X/Y amplifiers, and longevity estimates
- Compare pairwise or multi-case diagnostics (e.g., high-trust foil vs high-suppression polity)
- Preserve ad-hoc / exploratory runs (historical probes, modern contrasts) without cluttering `/examples/`, `/figures/`, or `/data/`
- Support reproducibility when tweaking penalties, rigidity factors, or biology-specific adjustments

Everything in `/tests/` is provisional and open to refinement — treat it as a workbench, not gospel.

## Subfolders (current or planned)

- **outputs/**  
  Generated visuals: 15×6 Master Grids, heatmaps, compass scatter plots, etc.  
  Examples: `nk_vs_ants_rc1_diagnostic.png`, `usa_vs_prc_rc1_heatmap_v3.png`, `historical_venice_consensus_rc1.png`

- **inputs/** (optional / future)  
  Provisional or raw input CSVs used only for testing (e.g., multi-rater raw scores before consensus averaging, temp files from notebook experiments).

- **comparatives/** (optional / future)  
  If `/outputs/` gets crowded, move pairwise diagnostic PNGs here for clearer organization.

- **notebooks/**  
  Exploratory Jupyter notebooks for test runs and validation.

- **scripts/**  
  Helper or variant Python scripts for isolated testing.

## Root files

- `blank_grid.py`: Quick template runner for blank 15×6 grids.
- `requirements.txt`: Local deps for test env isolation.
- `simulate.py`: Scratch/test copy (canonical version in `/scripts/`).

## How these files are created

Most content is generated via:
```bash
python simulate.py --input examples/eusocial_ant_colony.csv --mode grid --output tests/outputs/ants_baseline_rc1.png
