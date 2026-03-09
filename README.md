## Support the Ledger❤️
If the 35-metric compass, 15×6 grid, or Rule-13 hinge has helped clarify thermodynamic dynamics in replicating systems, consider a small contribution to sustain simulations, figures, and ledger growth.

Ko-fi: https://ko-fi.com/mementomori15x6 (suggested tips: $5 / $16 / $42)
GitHub Sponsors (pending final approval): https://github.com/sponsors/MementoMori15x6

Every tip extends the observation window. Memento mori. 🚀
---
# The Board – Political Thermodynamics
   
A diagnostic compass for far-from-equilibrium replicating systems — RNA to polities, corporations, protocols, AI agents.

**15×6 grid** (15 rules × 6 moves) + **35-metric compass** → phase-space position (X economic metabolism, Y governance density), Rule-13 exploitationism proxy (key hinge), rigidity penalty, stochastic longevity estimates.

**Rule-13 exploitationism >30%** → provisional collapse risk signal (open to testing).

Repo: https://github.com/MementoMori15x6/15x6-sim

---

## Quick Start – No Coding Required (Casual Users)

Talk to the Board using any LLM (Grok, Claude, ChatGPT, Ollama, etc.) — no programming needed.

Two ready-to-use primers are available in `/primers/`:

**1. Board Scoring Primer v1.7** (quick scoring mode)
Best for: getting a fast 35-metric CSV + basic X/Y/proxy/longevity on any replicator.
→ [primers/board_scoring_primer_v1.7_baseline.md](https://github.com/MementoMori15x6/15x6-sim/blob/main/primers/board_scoring_primer_v1.7_baseline.md)

**2. LLM Full-Access Primer v1.7** (full access mode)
Best for: Full discussion on [polity/replicator] in question, mechanics explanations, what-if vectors, attractor discussions, shock simulations, refinements.
→ [primers/llm_full_access_primer_v1.7.md](https://github.com/MementoMori15x6/15x6-sim/blob/main/primers/llm_full_access_primer_v1.7.md)

### How to Use (30 seconds)

1. Open either primer link above
2. Copy **bash section** 
3. Paste into your LLM chat window
4. **Full Access Primer**: add your question right after (e.g. *"the USA in 2025-present using public evidence."*) 
5. **Board Scoring Primer** should be solely for gathering and collecting score.

---

## For Developers / Experimenters

Want to run simulations, tweak parameters, add new anchors, or contribute to the ledger?

Collect and aggregate scores using the **Board Scoring Primer v1.7**
→ [primers/board_scoring_primer_v1.7_baseline.md](https://github.com/MementoMori15x6/15x6-sim/blob/main/primers/board_scoring_primer_v1.7_baseline.md)

Score any replicator with the 35-metric protocol → get phase-space position (X/Y), Rule-13 leakage proxy, rigidity multiplier (R), and longevity estimate. See how systems drift toward mutualism ellipsoids, competition toroids, exploitationism sinkholes, or rigid traps — and where Rule-13 >30% (or >60% post-shock) becomes the universal collapse hinge.

### Quick Start

1. **Clone the repo**

   ```bash
   git clone https://github.com/MementoMori15x6/15x6-sim.git
   cd 15x6-sim
   ```

2. **Install dependencies** (Python 3.8+ recommended)

   ```bash
   pip install -r requirements.txt
   ```

   Dependencies: numpy, scipy, pandas, matplotlib, lifelines — no extras needed.

3. **Run a baseline anchor** (example: enforced USA 1789 healthy mutualist)

   ```bash
   python simulate.py data/anchors/usa_1789_anchor.csv --noise_std=0.1 --n_ensemble=100
   ```

   Typical output (console + saved files):
   - Compass X/Y coordinates (toy version)
   - Rule-13 exploitationism proxy %
   - Rigidity penalty (R)
   - Stochastic longevity (Weibull/Gompertz median ± CI)
   - Ensemble scatter plot (PNG)
   - Optional 15×6 grid heatmap (with `--plot-grid`)

4. **Score your own replicator**

   Start from the template:

   ```bash
   cp data/templates/blank_35_metrics.csv data/my_replicator_2025.csv
   ```

   Fill the 35 metrics (−10 to +10) using public evidence + Chapter 2 protocol, then run:

   ```bash
   python simulate.py data/my_replicator_2025.csv --noise_std=0.07 --n_ensemble=200 --plot-grid
   ```

### Useful Flags

```bash
# Lower noise for stable anchors
python simulate.py ... --noise_std=0.05

# More ensemble runs for tighter CIs (slower)
python simulate.py ... --n_ensemble=500

# Generate 15×6 dominance heatmap
python simulate.py ... --plot-grid

# Apply sample institutional capture shock (D1/G1 delta)
python simulate.py ... --shock capture

# Full help
python simulate.py --help
```

### Next Steps & Contributions

- **Add new anchors** → drop CSV in `/data/anchors/`, PR with evidence notes
- **Extend the engine** → edit `simulate.py` (e.g. add correlated noise, new survival fits, 3D topology stubs)
- **Update master ledger** → PR row to `/docs/Chapter_12–Appendix_Master_15×6_Comparative_Grid.md` (format: replicator name, baseline/post-shock proxies, longevity, notes, sources)
- **Figures** → matplotlib/seaborn code only (see `/figures/scripts/` examples; no AI generation)
- **Discuss / report bugs / wild ideas** → open an issue or tag [@MementoMori15x6](https://x.com/MementoMori15x6) on X

Calibration anchors, CRL enforcement, rigidity formulas, and full protocol are in `/docs/`. Fork, experiment, break things, send PRs — the ledger is living.

## Contributing
The main branch is protected — all changes must come through pull requests.  
Fork the repo, make your edits (e.g., new replicator scores in data/, tweaks to simulate.py), and open a PR.  
PRs welcome for ledger rows, shock tests, figure code, or compass refinements.  
All provisional and open to stress-testing.

The microscope is yours.

Memento mori. 🚀
