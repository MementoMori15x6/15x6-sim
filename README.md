# 15×6 Simulator – Replicator Thermodynamic Scorecard

Toy v0.1: text-first baseline output (X/Y coordinates, dominant zone, Rule-13 parasitism proxy, simple row heuristic).

Quick Start in Colab:
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MementoMori15x6/15x6-sim/blob/main/quick_start.ipynb)

Or locally:

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

### Calibration Note: Governance Amplification
The simulation applies a moderate amplification (Y multiplier = 2.5) to the governance/cultural metrics (second half of the 35) to reproduce the qualitative extreme Zone 9 pull described for early Bolshevik USSR in Chapter 3.1.

Simple averaging dilutes this signal due to the balanced nature of the 35-metric protocol. The multiplier is explicit in `simulate.py` and open to refinement — fork the repo and adjust it to see how splatter changes.

This keeps scoring single-column and human-friendly while matching manuscript claims.

All code is pure matplotlib/numpy/pandas — no dependencies beyond basics.

Contributions welcome: bug fixes, new example cases, alternative weighting schemes, or visualisation improvements.

Memento mori. 🚀
