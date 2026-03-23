##Update simulate.py to v3.2 calibration:
- MC-aligned proxy tuned for Terra trajectory (Stage 1 38.3% → Stage 4 96.3%)
- ETH S3 at 55.4% (pre-fracture signal – historically plausible 2018–2021 stress)
- Rigidity buildup visible in Terra (R 0.00 → 0.32)
- Full ledger table generated with baselines + 4 stages


# Terra/Luna Case Study (2019–2022) – Monte Carlo Sensitivity Analysis

This folder contains all derived outputs from the Monte Carlo perturbation of the 35-metric consensus scores across the key stages of Terra/Luna, with contrast runs on Bitcoin and Ethereum baselines.

The goal was to test how stable the Fracture Meter (Rule-13 hinge proxy) is under realistic scoring noise — and whether the system crosses the collapse threshold (>45%) in perturbed versions.

## Monte Carlo Setup
- 5,000 iterations per stage
- Gaussian noise: σ=1.0 on main hinges (D1, G1, F2), σ=0.5 on secondary (H3, L2, C2), σ=0.3 on others
- Collapse flag: Fracture Meter >45% = collapse-prone under uncertainty
- Notebook: `notebooks/terra-luna_mc_sensitivity.ipynb`

## Terra/Luna Results – Baseline Noise

| Stage                                      | Mean Fracture Meter | 95% CI          | % >45% | % >50% | % >55% | Collapse Prob (>45%) | Raw CSV                                      | Converted CSV (35-metric)                    |
|--------------------------------------------|----------------------|-----------------|--------|--------|--------|----------------------|----------------------------------------------|----------------------------------------------|
| Stage 1 (2019 Genesis)                     | 39.8%               | 34.0–45.5%      | 3.8%   | 0.0%   | 0.0%   | 3.8%                 | raw_terra-luna_mc_results_stage1.csv         | terra-luna_mc_converted_stage1.csv           |
| Stage 2 (2020 Anchor Launch)               | 37.3%               | 31.3–43.1%      | 0.4%   | 0.0%   | 0.0%   | 0.4%                 | raw_terra-luna_mc_results_stage2.csv         | terra-luna_mc_converted_stage2.csv           |
| Stage 3 (2021 Parabolic)                   | 51.2%               | 45.5–56.9%      | 98.3%  | 66.3%  | 9.3%   | 98.3%                | raw_terra-luna_mc_results_stage3.csv         | terra-luna_mc_converted_stage3.csv           |
| Stage 3 + Combined Shock (+1 D1 & -1 G1)   | 55.1%               | 49.5–60.6%      | 100.0% | 96.1%  | 52.9%  | 100.0%               | (shock variant – not yet raw-exported)       | (shock variant – not yet converted)          |

**Key Insight**  
Only Stage 3 consistently crosses the fracture threshold under realistic uncertainty. Earlier stages remain robust. The combined shock pushes Stage 3 to certain collapse — showing zero margin for error once the parabolic phase is reached.

## Bitcoin & Ethereum Contrast – Baseline Noise

| Stage                                      | Mean Fracture Meter | 95% CI          | % >45% | % >50% | % >55% | Collapse Prob (>45%) | Raw CSV                                      | Converted CSV (35-metric)                    |
|--------------------------------------------|----------------------|-----------------|--------|--------|--------|----------------------|----------------------------------------------|----------------------------------------------|
| Bitcoin Stage 1 (2009 Genesis)             | 36.8%               | 31.1–42.6%      | 0.3%   | 0.0%   | 0.0%   | 0.3%                 | raw_bitcoin_mc_results_stage1.csv            | bitcoin_mc_converted_stage1.csv              |
| Ethereum Stage 1 (2015 Genesis)            | 39.2%               | 33.5–45.0%      | 2.5%   | 0.0%   | 0.0%   | 2.5%                 | raw_ethereum_mc_results_stage1.csv           | ethereum_mc_converted_stage1.csv             |
| Bitcoin Stage 3 (2015–2017 Scaling Wars)   | 38.4%               | 32.6–44.1%      | 1.3%   | 0.0%   | 0.0%   | 1.3%                 | raw_bitcoin_mc_results_stage3.csv            | bitcoin_mc_converted_stage3.csv              |
| Ethereum Stage 3 (post-DAO / pre-merge)    | 43.8%               | 38.1–49.6%      | 33.9%  | 1.8%   | 0.0%   | 33.9%                | raw_ethereum_mc_results_stage3.csv           | ethereum_mc_converted_stage3.csv             |

**Key Insight**  
All BTC & ETH stages remain robust under the same noise applied to Terra. Even Ethereum Stage 3 (high TVL/DeFi growth period) shows only moderate elevation (33.9%) — far safer than Terra Stage 3 (98.3%). The hinge selectively identifies fragility.

## Files Overview
- `raw_*.csv` — raw 5,000 iteration Fracture Meter values (one file per stage)
- `*_mc_converted_*.csv` — recalibrated 35-metric consensus scores that produce the ensemble mean Fracture Meter (ready for simulate.py / compass protocol)
- `notebooks/terra-luna_mc_sensitivity.ipynb` — full MC code, baseline arrays, and export logic

## How to Reproduce
1. Open `notebooks/terra-luna_mc_sensitivity.ipynb` in Colab
2. Run all cells top-to-bottom
3. Outputs appear in `results/` (raw CSVs + printed summaries)
4. Converted CSVs can be re-generated by perturbing hinges to match printed means

All scores provisional and open to community review/testing/PRs.

Memento mori. 🚀
