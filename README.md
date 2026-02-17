# 15×6 Simulator – Replicator Thermodynamic Scorecard

Toy v0.1: text-first baseline output (X/Y coordinates, dominant zone, Rule-13 parasitism proxy, simple row heuristic).

Quick Start in Colab:
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MementoMori15x6/15x6-sim/blob/main/quick_start.ipynb)

Or locally: git clone https://github.com/MementoMori15x6/15x6-sim.git
cd 15x6-sim
pip install -r requirements.txt
python simulate.py examples/eusocial_ant_colony.csv

For nuanced scoring: prompt 2–4 LLMs with the evidence packet + protocol → average grids for convergence.

See quick_start.ipynb for examples.

# 15×6 Simulation Script

Reproducible Python tools for the 15×6 Master Grid proposed in “The Board – Political Thermodynamics”.

This repo contains:
- `blank_grid.py` — generates the canonical blank grid (page 99 style)
- `simulate.py` — core engine: 35-metric CSV → X,Y coordinates → zone splatter → filled grid PNG + entropy curve (placeholder)
- `examples/` — CSVs for the four illustrative case studies
- `notebooks/quick_start.ipynb` — step-by-step demo

**Purpose**  
The script lets anyone take raw evidence, score the 35 metrics, and produce the same grid heat-maps and entropy curves used in the manuscript. It is deliberately minimal and open — fork, improve, test new cases, or refine the protocol.

**Quick Start**
1. Clone the repo
2. `pip install -r requirements.txt`
3. Open `notebooks/quick_start.ipynb` and run the cells
4. Try your own polity CSV!

### Governance Amplification Calibration
The simulation applies a moderate amplification (Y multiplier = 2.5) to the governance/cultural metrics (second half of the 35) to reproduce the qualitative extreme Zone 9 pull described for early Bolshevik USSR in Chapter 3.1.

Simple averaging dilutes this signal due to the balanced nature of the 35-metric protocol. The multiplier is explicit in `simulate.py` and open to refinement — fork the repo and adjust it to see how splatter changes.

This keeps scoring single-column and human-friendly while matching manuscript claims.

All code is pure matplotlib/numpy/pandas — no dependencies beyond basics.

Contributions welcome: bug fixes, new example cases, alternative weighting schemes, or visualisation improvements.

### Calibration & Example Notes

The toy simulator (`simulate.py` v0.1) is a deterministic baseline: it processes a 15×6 CSV (row-normalized percentages) via the 35-metric compass protocol, applies the governance Y-multiplier (currently 2.5 on cultural/governance metrics), computes zone percentages, a Rule-13 parasitism proxy, and placeholder entropy/longevity curves. Outputs are text-first (console + optional PNG) for reproducibility.

**Why these examples need careful interpretation and potential tuning:**

- **eusocial_ant_colony.csv** (biological replicator, canon scoring v1.6.2b)  
  Heavy mutualism expected in Rows 6–8 (foraging/adaptation efficiency), low Rule-13 parasitism (~10% or less). As a persistent equilibrium case, it should land in Zone ~9–11 with extended longevity (100+ generations). Apply minimal or no additional amplification beyond the default Y-multiplier; over-weighting parasitism (e.g., from political bleed) can flatten it unrealistically. Use as health benchmark.

- **modern_north_korea.csv** (political replicator, ongoing)  
  High institutional fragility and Rule-13 parasitism (~35–45% expected). Targets Zone ~4–6 and median longevity ~60–80 years (aligns with observed persistence under stress but collapse risk). The Y-multiplier helps pull governance metrics, but fragile cases may still show conservative estimates—tune by increasing parasitism sensitivity if needed in forks.

- **ussr_1917_1991_lifetime.csv** (political lifetime span, placeholder)  
  Rough seed only; not fully refined via 35-metric protocol. Expect high early parasitism drift, collapse around ~70–74 years (historical match). Use as collapsed-system control; refine grid with LLM prompting for accurate curves.

- **united_states_west_1971-2025** (political/western drift, placeholder)  
  Placeholder data; captures post-1971 institutional evolution with moderate Rule-13 rise (~20–30%). Targets Zone ~8–12 and median 150–300+ years (ongoing drift, no terminal collapse yet). Refine via evidence-based scoring; current outputs are illustrative.

- **influenza_molecular.csv** (molecular/viral replicator, recently updated)  
  Fast-entropy parasitic spikes; low longevity baseline (short cycles). Use as control for rapid-decay replicators. Minimal Y-multiplier impact expected due to non-governance nature.

**General guidance:**  
- Batch-style testing (run examples sequentially and compare) reveals cross-case distortions (e.g., political fragility over-correcting biological persistence).  
- The Y-multiplier=2.5 is global and explicit in `simulate.py`—fork and adjust (or scope per replicator type) to better align zones/med longevity with priors.  
- These are "good enough" starting points tuned empirically from manuscript claims and early runs. Placeholders (USA/USSR) await full 35-metric refinement.  
- For polity-focused tests, LLM + 35-metric scoring (see future Prompting Guide) remains primary; the toy is best for builders exploring entropy mechanics. PRs with evidence-backed tweaks welcome.

This section complements the Governance Amplification note and invites collaboration on calibration.

### Raw 35-Metric CSV Input (Recommended for Accurate Diagnostics)

The simulator reads a CSV with **35 columns** (one per metric from Chapter 2 compass protocol). Each row is a replicator case (or time slice); values are raw scores (e.g., 0–10 Likert-like or 0–100 normalized evidence scale).

- Columns 1–17: Adaptation/structural metrics
- Columns 18–35: Governance/cultural metrics (amplified ×2.5 by default)

No row normalization required—the protocol aggregates to X/Y coordinates directly.

**Template CSV Header** (use blank_35metric.csv or generate via extension of blank_grid.py):
Metric1,Metric2,...,Metric35
[case_name or empty],value1,value2,...,value35

**How to Create Scores**
- Use the 35-metric protocol: Map public evidence to each metric (e.g., inequality Gini → specific metric; trust polls → cultural metric).
- For quick starts: Prompt LLMs with "Score [system] on the 35-metric compass using public sources. Output as CSV with 35 columns of 0–10 raw scores, cite 1–2 sources per metric."
- Average 2–3 LLM runs for convergence.
- Save as e.g., examples/united_states_west_1971-2025.csv

This raw format preserves signal strength and allows precise entropy modeling—preferred for research forks. For simple 15×6 % grids (if desired), use LLM to convert raw → row-normalized percentages post-scoring.

Memento mori. 🚀
