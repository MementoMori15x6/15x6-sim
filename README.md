# 15×6 Simulator – Replicator Thermodynamic Scorecard

Toy v1 — deterministic baseline that processes a 35-metric raw CSV to compute X/Y coordinates, zone percentages, Rule-13 parasitism proxy, row dominance heuristics, and a placeholder longevity estimate.

The project is a microscope for diagnosing health in far-from-equilibrium replicating systems (RNA → polities). The 15×6 Master Grid and 35-metric compass protocol are proposed tools for reproducibility and open testing.

## Quick Start
For LLM-only scoring (no code required): see the [LLM Scoring Workshop Guide](docs/llm-scoring-workshop.md)

### In Colab (recommended)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MementoMori15x6/15x6-sim/blob/main/notebooks/the_board_rc1_diagnostic.ipynb)
[![Release v1.1-RC1](https://img.shields.io/github/v/release/MementoMori15x6/15x6-sim?color=brightgreen)](https://github.com/MementoMori15x6/15x6-sim/releases)

1. Open the notebook above
2. Run cells to clone repo + install deps
3. Try an example: `!python simulate.py examples/united_states_west_1971-2025.csv`

**Resouce**: Generate blank grid: python scripts/master_blank_15x6_grid_v3.py → outputs → figures/master_blank_grid_15x6.png

## Default Metric Scoring Guidelines or Default LLM Scoring Format.

When generating or requesting 35-metric compass scores for any polity, historical period, corporation, or replicating system:

**Always output exactly as CSV** with these columns only (no extra text outside the CSV):

Use the **full 35 metrics** in this exact order and grouping:

- A1–A3: property, market allocation, profit motive  
- B1–B2: redistribution, welfare  
- C1–C3: heredity fidelity, variation, persistence  
- D1–D2: parasitism, competition  
- E1–E2: survival, niche construction  
- F1–F2: boundary, error repair  
- G1–G3: cheater detection, modularity, info storage  
- H1–H3: cultural uniformity, ideological monopoly, dissent suppression  
- I1–I3: family autonomy, religious freedom, artistic expression  
- J1–J3: scientific direction, education indoctrination, media control  
- K1–K3: military priority, isolationism, external threat narrative  
- L1–L3: succession mechanism, leadership cult, purge cycles  
- M1–M3: natalism, migration control, ethnic policy  

**Rules for scoring**:
- Range: -10 to +10 per metric  
  - negative = left/collectivist/authoritarian tilt  
  - positive = right/market/libertarian tilt  
- Rationale: 1–2 sentences only, evidence-based (public historical/public data only), no speculation  
- Wrap any rationale containing commas in double quotes `"..."` to ensure CSV integrity  
- After the CSV, output nothing else unless explicitly asked  

All scores are provisional and open to empirical stress-testing on the 15×6 Master Grid.
 
### Locally
```bash
git clone https://github.com/MementoMori15x6/15x6-sim.git
cd 15x6-sim
pip install -r requirements.txt
python simulate.py examples/eusocial_ant_colony.csv
```
Purpose & Limitations
This toy is a minimal, deterministic scaffold for testing the 15×6 Master Grid and 35-metric compass protocol. It produces flat or spiked curves based on raw inputs — no LLM judgment, no stochastic noise, no adaptive weighting.
Use cases

R&D / builders: fork and extend (add noise, ML modulators, custom entropy decay)
Community testing: generate 35-metric CSVs via LLM prompts, pipe to toy for baseline projections

### Known Limitations

Deterministic curves only — flat baselines or spikes; no probabilistic noise or real-world variability.
Placeholder longevity estimate — simple heuristic (base 100 years modulated by parasitism proxy and mutualism/competition average); not empirically validated, ±20% ranges only.
Tuned on 5 canonical cases — results reflect these examples (ants, influenza, NK, USSR, USA 1971–present); performance on other replicators untested.
No built-in 35-metric scoring — users must generate raw scores via LLM prompts or manual evidence mapping.
Fixed centres array and heuristics are static — zone assignment and dominance logic may over-anchor to Zone 10 for moderate-high adaptation.

The toy is a scaffold for extensions. For polity-specific or nuanced scoring, LLM-driven 35-metric workflows remain the primary diagnostic tool.
Input Format (locked v1)
CSV with:

Header row: Metric1,Metric2,...,Metric35 (dummy labels)
Single data row: 35 comma-separated numbers (0–10 scale, averaged from LLM ensemble)
No trailing commas, no strings, no extra rows

Example (USA 1971–present):
```bash
textMetric1,Metric2,Metric3,...,Metric35
8,7,7,7,8,7,7,7,8,7,7,8,7,8,8,6,7,3,2,4,3,2,2,3,3,2,3,3,4,4,2,3,1,3,3
```
 **Current Calibration (v1 – February 2026)**
Tuned on canonical cases to expose political fragility while preserving biological persistence.
Key parameters

y_multiplier = 2.5 (reduced to show governance drift)
Parasitism penalty on Y: (Rule-13 proxy / 100) * 1.5
Adaptation penalty on X: max(0, (mean(metrics 1–17) - 6.0) / 2.0)
Rule-13 proxy: max(0, 50 - (mean(metrics 18–35) / 10 * 50))
Longevity placeholder: 100 / (1 + proxy/100) * (1 + mutual_comp_avg), ±20% ranges

**Batch output example (5 canonical replicators)**

| Replicator                        | X     | Y     | Dominant Zone      | Rule-13 Proxy | Longevity Range       |
|-----------------------------------|-------|-------|--------------------|---------------|-----------------------|
| Eusocial Ant Colony               | 0.49  | 0.86  | 10 (98.8%)         | ~45%          | ~77–144 years         |
| Influenza Molecular               | 0.00  | -0.75 | 3 (72.5%)          | ~50%          | ~46–86 years          |
| Modern North Korea                | 0.00  | -0.75 | 3 (72.5%)          | ~50%          | ~46–86 years          |
| USSR 1917-1991                    | 0.43  | 0.50  | 10 (78.5%)         | ~41%          | ~72–134 years         |
| United States West 1971-2025      | -0.16 | 1.72  | 9 (46.1%)          | ~36%          | ~88–165 years         |


 **Interpretation keys**

Zone 1–4: Parasitic fringe dominant → high collapse risk
Zone 8–10: Mutualistic/competitive core dominant → persistence / health
Rule-13 proxy >30–35%: Cheater suppression failure signal
Longevity <100 years: Short window (collapse imminent)
Longevity >150 years: Extended stability (with error bars)

 **Recommended Workflows**
Quick polity test (most users)
Use an LLM (Grok, Claude, Gemini) with the 35-metric prompt guide. Average outputs, save as CSV, interpret zones/proxy/longevity manually or pipe to toy.
Advanced / reproducible testing

Generate 35-metric CSV via LLM ensemble
Run python simulate.py your_file.csv
Compare to priors and submit PRs with evidence-backed refinements

  **Contributing**

Bug fixes, new examples, alternative weighting schemes, visualisation improvements welcome.
Fork and experiment: add noise, ML modulators, or custom entropy decay.
PRs: evidence-based tuning or new cases (corporate, crypto protocols, etc.).

This project is open for discourse, testing, and refinement. The toy is a scaffold — the real value lies in community extensions and LLM-hybrid scoring.
Memento mori. 🚀

