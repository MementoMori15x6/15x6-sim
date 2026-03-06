# Canonical Anchors for Triangulation & Comparison

These are fixed, numeric-only CSV configurations (35 metrics, -10..+10 scale) derived from consensus scores in ../.  
Use them as reference points in simulate.py for:

- Phase-space distance / drift tracking
- Splatter % relative to healthy vs. rigid attractors
- Shock delta testing (copy → perturb → compare)

Naming convention: {system}_{phase-or-era}_anchor.csv

Current set:
- usa_1789_anchor.csv          → Founding constitutional baseline (high mutualism, balanced Rule-13)
- ussr_1937_anchor.csv         → Peak centralized command (high Y density, suppression)
- voc_golden_age_anchor.csv    → Dutch VOC commercial zenith
- usa_1971-present_anchor.csv  → Modern US late-stage drift
- prc_1978-present_anchor.csv  → Post-reform PRC hybrid
- venice_republic_anchor.csv   → Longevity-max Venetian case

To run: python simulate.py data/anchors/usa_1789_anchor.csv
All provisional — welcome PRs for new anchors or refinements.
## Quick Reference Diagnostics (from latest simulate.py run)

| Anchor                  | X     | Y     | Dominant Zone | Rule-13 Expl % | Longevity Est. |
|-------------------------|-------|-------|---------------|----------------|----------------|
| usa_1789_anchor        | ~?   | ~?   | Healthy Mutualist? | <20%?         | High (200+ yrs?) |
| ussr_1937_anchor       | ~?   | high | Rigid Trap?   | >30%?         | Medium-low     |
| voc_golden_age_anchor  | pos  | mod  | Exploitation Sink? | mid-high?    | Medium         |

(Fill from your runs — provisional!)
