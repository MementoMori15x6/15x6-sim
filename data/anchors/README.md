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
## VOC Pair – Golden Age vs. Late Decay

- voc_golden_age_anchor.csv
  → Raw consensus (zenith phase)
  → X: 0.29 Y: -0.43 | Rule-13: 18.0% | Mutualism/Competition | 150+ yrs (Low Parasitism)
  → Rigidity R: 0.0000

- voc_late_golden_age_anchor.csv (or voc_late_1780-1785_anchor.csv)
  → Same consensus, enforced with VOC_ANCHORS (1780–1785 decay calibration)
  → X: 0.10 Y: -0.43 | Rule-13: 64.8% | Rigid Trap (Brittle Regime) | 30–80 yrs (High Parasitism)
  → Rigidity R: 0.0000
  → Key: Cheater detection collapse + exploitation ramp (no Y density spike)
# VOC Anchor Pair – Golden Age vs Late Decay (as of March 2026 local runs)

**Golden Age** (raw, no enforcement)  
X: 0.29 | Y: -0.43 | R: 0.0000 | Rule-13: 18.0%  
State: Mutualism/Competition | Longevity: 150+ yrs (Low Parasitism)

**Late Decay** (enforced via filename trigger "late")  
X: 0.10 | Y: -0.43 | R: 0.0000 | Rule-13: 64.8%  
State: Rigid Trap (Brittle Regime) | Longevity: 30–80 yrs (High Parasitism)

Key clamps: D1 +9, G1 -8, F2 -8, E1 +2, D2 -8  
Insight: Rule-13 overload alone compresses longevity dramatically, even with Y remaining low/negative (no rigidity boost). Distinct from USSR-style high-Y traps.
