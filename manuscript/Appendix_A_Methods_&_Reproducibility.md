# Appendix A: Methods & Reproducibility
Memento & Mori | December 2025 – ongoing

This appendix describes the technical and methodological foundations of the 15×6 grid, 35-metric compass, and longevity estimates. All code, calibration parameters, and data processing steps are explicit and reproducible.

### Core Tools & Repo
- Repository: https://github.com/MementoMori15x6/15x6-sim
- Primary simulation script: `simulate.py` (ensemble runner, shock deltas, compass calc, Weibull/Gompertz fits)
- Python environment: standard scientific stack (numpy, pandas, matplotlib, seaborn) — no proprietary dependencies

### Compass Protocol Implementation
- Scoring: manual or multi-LLM averaged on public 2026 data (historical records, fiscal reports, policy texts, media analysis)
- X,Y calculation (toy version):
  - Raw X = mean(first 18 metrics) / 10 × 1.2
  - Raw Y = mean(last 17 metrics) / 10 × 2.5
  - Rigidity penalty: variation_suppression × uniformity_pressure → Y_adjusted = Y × (1 + 1.5 × rigidity)
- Splatter %: inverse distance to 10 attractor centers, power-law exponent 10, normalized to 100%

### Longevity Estimation
- Weibull / Gompertz parametric fits on historical proxy data + simulated ensembles
- Baseline: centuries for digital replicators; decades for stressed planetary states
- Error bars: ±50% (reflecting parametric uncertainty and shock variability)

### Shock Simulation
- Delta application: +10–15% on targeted metrics (e.g., D1 exploitationism, G1 detection)
- Re-compute: grid, compass coords, Row-13 %, longevity window
- All parameters explicit in simulate.py (open to PR refinement)

### Data Sources & Limitations
- Public/open sources only (fiscal reports, blockchain explorers, policy docs, media archives)
- Limitations: proxy noise, scoring subjectivity, future shocks unmodeled
- Provisional nature: all estimates hypotheses, open to empirical falsification

Reproducibility: fork the repo, run `simulate.py`, submit PRs for new rows/variants.

Memento mori.
