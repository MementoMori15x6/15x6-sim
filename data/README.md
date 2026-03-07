# /data/ — 35-Metric Compass Score Files

This folder contains all input CSVs for the 35-metric compass protocol (Chapter 2). Each file scores a replicating system (biological, institutional, algorithmic) in baseline or shock state.

**Format (locked v1)**  
CSV with:
- Header row: Metric,Description,Score,Rationale  
- Single data row: 35 comma-separated scores (-10 to +10)  
- No trailing commas, no strings, no extra rows

**Naming Convention**  
`35_metrics_{system-or-context}_{variant-or-phase-or-shock}_consensus.csv`  
Examples:  
- `35_metrics_voc_golden_age_consensus.csv`  
- `35_metrics_voc_shock_1780s.csv`  
- `35_metrics_blank_template.csv` (starter for new scorings)

## Current Files (as of March 2026)

### Triangulation Anchors (core reference set)
- `usa_1789_anchor.csv` — Founding constitutional baseline (healthy mutualism)  
- `ussr_1937_anchor.csv` — Peak centralized command (high-Y rigid trap)  
- `voc_golden_age_anchor.csv` — Dutch VOC commercial zenith (raw consensus)  
- `voc_late_golden_age_anchor.csv` — VOC late decay (enforced 1780–1785 calibration)

### Biological / Superorganism Baselines
- `35_metrics_eusocial_ant_colony.csv` — Healthy eusocial ant colony  
- `35_metrics_ants_queen_death_shock.csv` — Queen-death shock proxy (Rule-13 failure test)

### Historical Polities / Phases
- `35_metrics_roman_republic_133_27_bce.csv` — Late Roman Republic crisis phase  
- `35_metrics_augustus_baseline.csv` — Augustan Principate baseline  
- `35_metrics_venice_pre_serrata_drift.csv` — Venice pre-Serrata drift  
- `35_metrics_venice_republic_697-1797_v2_consensus.csv` — Full Venetian Republic arc  
- `35_metrics_voc_ensemble_consensus.csv` — VOC baseline ensemble  
- `35_metrics_voc_shock_1780s.csv` — VOC 1780s fracture shock

### Modern / Contemporary Hegemons
- `35_metrics_usa_1971-present_consensus.csv` — USA post-1971 baseline  
- `35_metrics_usa_dedollarization_shock_dominance.csv` — USA dedollarization shock  
- `35_metrics_prc_1978-present_consensus.csv` — PRC 1978–present consensus  
- `35_metrics_prc_rigidity_collapse_shock.csv` — PRC rigidity-collapse shock

### Algorithmic / Millisecond-Lag Replicators
- `35_metrics_bitcoin_consensus.csv` — Bitcoin baseline  
- `35_metrics_ethereum_consensus.csv` — Ethereum baseline  
- `35_metrics_ethereum_aihegemon_variant.csv` — Ethereum AI-hegemon variant  
- `35_metrics_makerdao_consensus.csv` — MakerDAO governance baseline  
- `35_metrics_polkadot_consensus.csv` — Polkadot modular consensus

### Helpers & Templates
- `35_metrics_blank_template.csv` — Empty starter  
- `35_metrics_placeholders.csv` — Demo/filled placeholders for testing

## Subfolder Notes
- `shocks/` — Legacy shock matrices (most moved to root for flat access)

## How to Contribute
1. Copy `35_metrics_blank_template.csv`  
2. Fill scores + evidence-based rationales (public sources only)  
3. PR with filename following convention + brief message  
4. Reference in ledger discussions or Ch 12 appendix updates  

These files are the living ledger backbone — every new CSV helps test the Rule-13 hinge (>30% exploitationism collapse signal) and fractal-sink / kill-switch hypotheses across scales.

Questions? Open an issue or PR. Let's keep refining the microscope.  
Memento mori. 🚀
