# Canonical Anchors for Triangulation & Comparison

These are fixed, numeric-only CSV configurations (35 metrics, -10..+10 scale) derived from consensus scores in `../`.  
Use them as reference points in `simulate.py` for:

- Phase-space distance / drift tracking
- Splatter % relative to healthy vs. rigid attractors
- Shock delta testing (copy → perturb → compare)

## Current Status – simulate.py v2.0 (March 2026)

- Filename-triggered CRL enforcement (e.g. "late" → VOC decay clamps, "ussr_1937" → peak rigidity)
- Rigidity multiplier (R = Vs × Up) active with debug (vs/up shown)
- Scalar-safe compass calculations (no sequence/float errors)
- Triangulation set complete: USA_1789, USSR_1937, VOC golden/late

Run example:
```bash
python simulate.py data/anchors/voc_late_golden_age_anchor.csv

All provisional — welcome PRs for new anchors, refinements, or shocks.
Naming Convention
{system}_{phase-or-era}_anchor.csv
Current Set

usa_1789_anchor.csv → Founding constitutional baseline (high mutualism, balanced Rule-13)
ussr_1937_anchor.csv → Peak centralized command (high Y density, suppression)
voc_golden_age_anchor.csv → Dutch VOC commercial zenith (raw consensus)
voc_late_golden_age_anchor.csv → VOC late decay (enforced 1780–1785 calibration)
usa_1971-present_anchor.csv → Modern US late-stage drift (pending full run)
prc_1978-present_anchor.csv → Post-reform PRC hybrid (pending)
venice_republic_anchor.csv → Longevity-max Venetian case (pending)

AnchorXYRRule-13 %Systemic StateLongevity EstimatePath / Hinge SignatureUSA_1789 (enforced)0.59-0.02~0.0010.0%Mutualism/Competition150+ yrs (Low Parasitism)Healthy baseline: balanced mutualism, strong G rows, minimal suppression costVOC Golden Age (raw)0.29-0.430.000018.0%Mutualism/Competition150+ yrs (Low Parasitism)Commercial zenith: low governance density, functional cheater detectionVOC Late Decay (enforced)0.10-0.430.000064.8%Rigid Trap (Brittle Regime)30–80 yrs (High Parasitism)Low-Y decay path: pure metabolic/exploitation overload (D1↑, G1/F2↓), no rigidity boostUSSR_1937 (enforced)0.042.780.742564.8%Rigid Trap (Brittle Regime)30–80 yrs (High Parasitism)High-Y suppression path: governance density overload (H/L maxed), strong rigidity penalty
Key Observations

Two distinct collapse paths to same Rule-13 % / longevity: low-Y exploitation sink (VOC late) vs high-Y suppression trap (USSR).
Rule-13 >60% → brittle regime, regardless of Y density.
Rigidity R=0 on VOC decay → confirms cheater detection failure alone can collapse a system without governance overload.
Health indicator: USA_1789 and VOC golden cluster in low-proxy, low-R, near-neutral/negative Y zone → extended persistence correlates with balanced mutualism/competition and minimal rigidity.

VOC Pair – Golden Age vs Late Decay
Golden Age (raw, no enforcement)
X: 0.29 | Y: -0.43 | R: 0.0000 | Rule-13: 18.0%
State: Mutualism/Competition | Longevity: 150+ yrs (Low Parasitism)
Late Decay (enforced via "late" trigger)
X: 0.10 | Y: -0.43 | R: 0.0000 | Rule-13: 64.8%
State: Rigid Trap (Brittle Regime) | Longevity: 30–80 yrs (High Parasitism)
Key clamps: D1 +9, G1 -8, F2 -8, E1 +2, D2 -8
Insight: Rule-13 overload alone compresses longevity dramatically, even with Y remaining low/negative (no rigidity boost). Distinct from USSR-style high-Y traps.
All scores provisional — open to empirical testing, shocks, and PRs for new anchors or refinements
