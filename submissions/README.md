# /submissions/upload_folder – Community Contribution Drop Zone

This folder is the designated spot for provisional submissions from the community — new replicator scores, ledger row proposals, shock scenarios, alternative metric calibrations, or diagnostic runs.

Everything here is **unreviewed and provisional** until merged/reviewed into the canonical paths (`/data/`, `/tests/inputs/`, `/ledger/`, etc.).

## How to Submit
1. Fork the repo.
2. Place your file(s) here (preferred formats):
   - 35-metric CSV scores (use the exact column order from Chapter 2 / default scoring protocol)
   - Jupyter notebook (.ipynb) with compass run / heatmap / shock sim
   - Markdown table proposal for the master ledger (Seven Anchors or new row)
   - Python script snippet (if extending simulate.py)
3. Open a PR with a clear title/description (e.g., "Add 35-metric scores for [Entity] – baseline 2025").
4. Reference any public sources/evidence in your rationale column or PR notes.
5. We'll review, test against simulate.py, and merge if it fits the reproducibility standards.

**Guidelines**
- Use the standard 35-metric format (A1–M3 order, -10 to +10 scale, short evidence-based rationales).
- No speculation — stick to public historical/data.
- Keep files small (<1MB preferred); large ensembles go in a zip or linked Drive/Colab.
- All submissions provisional and open to community stress-testing.

This is how we grow the ledger collaboratively — new anchors, shocks, entities, refinements welcome.

Thanks for shining the light with us.

Memento mori. 🚀
