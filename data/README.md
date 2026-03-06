# /data/ — 35-Metric Compass Score Files

###Provisional Mutualism Anchor (USA 1787–1789)
This consensus gives us a strong, evidence-based "healthy replicator" reference:

Rule-13 leakage ~24% (low parasitism, strong cheater detection via checks/balances)
Positive X (market/property tilt), low-moderate Y (decentralized governance, no brittleness)
High modularity/variation (federalism), robust error repair (separation of powers)
Zone: Dynamic Mutualism
Longevity: 200–400+ years (matches observed persistence)

This completes the triangulation beautifully: VOC chaos (high parasitism), USSR rigid trap (high suppression), USA mutualism (balanced +/+ dominance, low leakage). The golden path signal is now measurable — win-win interactions, robust detection, adaptive variation → extended persistence.

### USSR 1937 Snapshot (Rigid Trap Canonical)
Run: `python simulate.py --system ussr_1937-snapshot --shock none`
Expected (v1.9 with enforcement): X≈0.04, Y≈2.05, Rule-13 proxy≈68.8%, Zone=Rigid Trap, Longevity=30–80 years (compressed)
CSV: data/35_metrics_ussr_1937-snapshot-present_consensus.csv (median scores from 6 LLM runs)

This folder contains all input CSVs for the 35-metric compass protocol (Chapter 2). Each file scores a replicating system (biological, institutional, algorithmic) in baseline or shock state, following the exact column structure:

- **Metric** (A1–M3 order)
- **Description** (short label)
- **Score** (-10 to +10; negative = collectivist/authoritarian tilt, positive = market/libertarian tilt)
- **Rationale** (1–2 sentences, evidence-based only, public sources)

These CSVs feed directly into `simulate.py` to compute:
- X (economic metabolism), Y (governance density)
- Zone splatter % across 10 attractors
- Rule-13 parasitism % (key hinge for stability)
- Longevity proxy / ε estimates

All scores are provisional — community-refined via PRs. Rationales should cite verifiable public data only.

## Naming Convention
- `35_metrics_{system-or-context}_{variant-or-phase-or-shock}_consensus.csv`
- `_consensus` suffix = converged/community/iterative scoring
- `_shock_{event/year}` or `_phase_{n}` for perturbations
- Blank starter: `35_metrics_blank_template.csv`

## Current Files (as of March 2026)

### Biological / Superorganism Baselines
- `35_metrics_eusocial_ant_colony.csv` — Healthy eusocial ant colony (thermodynamic ceiling, low parasitism, high mutualism)
- `35_metrics_ants_queen_death_shock.csv` — Queen-death shock proxy (Rule-13 failure test)

### Historical Polities / Phases
- `35_metrics_roman_republic_133_27_bce.csv` — Late Roman Republic (133–27 BCE) crisis phase
- `35_metrics_agustus_baseline.csv` — Augustan Principate baseline (post-Republic stabilization)
- `35_metrics_venice_pre_serrata_drift.csv` — Venice pre-Serrata drift (early merchant republic stress)
- `35_metrics_venice_republic_697-1797_v2_consensus.csv` — Full Venetian Republic arc (697–1797, longevity benchmark)
- `35_metrics_voc_ensemble_consensus.csv` — Dutch East India Company (VOC) baseline ensemble
- `35_metrics_voc_shock_1780s.csv` — VOC 1780s fracture shock

### Modern / Contemporary Hegemons
- `35_metrics_usa_1971-present_consensus.csv` — USA post-1971 baseline (stressed mutualism era)
- `35_metrics_usa_dedollarization_shock_dominance.csv` — USA dedollarization shock variant
- `35_metrics_prc_1978-present_consensus.csv` — PRC 1978–present consensus (high-suppression centralized)
- `35_metrics_prc_rigidity_collapse_shock.csv` — PRC rigidity-collapse shock test

### Algorithmic / Millisecond-Lag Replicators
- `35_metrics_bitcoin_consensus.csv` — Bitcoin physics-enforced baseline
- `35_metrics_ethereum_consensus.csv` — Ethereum baseline
- `35_metrics_ethereum_aihegemon_variant.csv` — Ethereum AI-hegemon variant (G1 boosted to 9.5)
- `35_metrics_makerdao_consensus.csv` — MakerDAO governance-capture baseline
- `35_metrics_polkadot_consensus.csv` — Polkadot modular consensus (fractal-sink proxy)

### Helpers & Templates
- `35_metrics_blank_template.csv` — Empty starter for new scorings
- `35_metrics_placeholders.csv` — Demo/filled placeholders for testing

## Subfolder Notes
- `shocks/` — Legacy / intermediate shock matrices (most have been renamed and moved to root for flat access)

## How to Contribute
1. Fork and copy `35_metrics_blank_template.csv`
2. Fill scores + evidence-based rationales
3. PR with filename following convention + brief commit message (e.g., "Add scored CSV: ancient Athens baseline")
4. Reference in ledger discussions or Ch 12 appendix updates

These files are the living ledger backbone — every new CSV helps test the Rule-13 hinge (>30% parasitism collapse signal) and fractal-sink / kill-switch hypotheses across scales.

Questions? Open an issue or PR. Let's keep refining the microscope.

Memento mori. 🚀
