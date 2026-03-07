# Contributing to The Board – Political Thermodynamics

Thank you for considering a contribution.  
This project is intentionally open and minimalist: a diagnostic microscope for replicating systems.

The goal is simple:  
Score replicators using the 35-metric compass → run them through `simulate.py` → add results to the living ledger (Chapter 12) → refine the hinge signals (especially Rule-13) across scales.

### Ways to Contribute

1. **Re-score a system**  
   - Fork the repo  
   - Copy `data/35_metrics_blank_template.csv` → rename to `35_metrics_your_system.csv`  
   - Fill scores (-10 to +10) + short evidence-based rationales (public sources only)  
   - Run `simulate.py` (or `iterative_dynamics.ipynb` if available)  
   - Submit a PR with your CSV, resulting X/Y/R/proxy/state/longevity, and any insights (e.g. hinge jumps, attractor zone)

2. **Improve the pipeline**  
   - Refine soft-projection tuning (γ, ε)  
   - Explore commensalism extensions or Z-axis prototypes  
   - Add nonlinear damping or Monte Carlo sensitivity sweeps  
   - Improve ensemble realism (correlated noise, scale-specific profiles)

3. **Add case studies**  
   - Score new historical, modern, biological, or fictional replicators (corporations, religions, pathogens, startups, sci-fi empires)  
   - Include CSV + short narrative (e.g. "Why Rule-13 spiked here")  
   - Propose new CRL anchors (centers + bands + justification)

4. **Documentation & testing**  
   - Expand Appendix A proofs  
   - Add unit tests for bifurcation/sensitivity functions  
   - Improve notebook visualizations or add Colab starters  
   - Clarify usage in READMEs or primers

### Guidelines

- Keep changes reproducible (public data sources, fixed seeds, clear rationales)  
- Let the grid speak — no narrative overrides of the compass output  
- PRs welcome; feel free to open issues for discussion first  
- All contributions provisional — we refine through evidence and testing  

The Board is a shared diagnostic tool. Bring your scores, run the simulation, and let's see what patterns emerge.

Memento mori. 🚀
