# Chapter 09 – Evolution of the Diagnostic Tool

![](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/banners/banner_ch09_diagnostic_evolution.png)

Memento & Mori | December 2025 – ongoing

## 9.1 From Deterministic v1 to Stochastic v2

The original 35-metric compass (v1) was deterministic: fixed scores from public evidence, fixed shocks, fixed longevity extrapolations. It revealed recurring patterns — Rule-13 parasitism >30% as collapse signal, balanced mutualism/competition in rows 6–8 & 13–14 as health indicator — but treated replicators as static snapshots.

v2 introduces stochastic realism. Real systems drift: small metric fluctuations (±5–10%) arise from environmental noise, measurement uncertainty, or hidden variables. We model this by adding Gaussian noise ε_j ~ N(0, σ) to each metric score across ensemble runs (n=100 per replicator):

$$
s_{j,i} = s_j + \epsilon_{j,i}, \quad \epsilon_{j,i} \sim \mathcal{N}(0, \sigma), \quad \sigma \in [0.05, 0.10]
$$

Recompute compass coordinates, Rule-13 proxy, longevity estimate, and Row 13 intensity for each realization i.

Early test cases illustrate the shift:
- Ant colonies (low intrinsic variance): noise barely perturbs mutualism-dominant grid; longevity distributions remain tight (high stability).
- Late VOC (high internal variance): noise amplifies parasitism spikes in Row 13; longevity distributions widen dramatically (fragility signal).

**Figure 9.1: Stochastic Drift – Ant Colonies vs Late VOC**

![Figure 9.1](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_9_1_stochastic_drift.png)

**Caption:** Ensemble scatter on compass plane (n=100): ants (tight cluster in high-mutualism zone), late VOC (wide smear toward parasitism sinkhole).

The microscope now sees probability clouds around attractors, not just point estimates.

## 9.2 Bifurcation Analyzer

Small metric changes can push a replicator across phase boundaries — from mutualism ellipsoid to parasitism sinkhole. The bifurcation scanner sweeps selected metrics (D1 parasitism, G1 detection, C2 variation, H2 ideological monopoly, etc.) in ±20% increments and tracks critical crossings:
- Rule-13 proxy >30%
- Row 13 parasitism intensity >40%
- Longevity drops below 500 years

This mirrors a Clausius-Clapeyron-like phase transition: just as physical matter changes state under pressure and temperature, social replicators bifurcate when **metabolic pressure** (parasitism load) exceeds available **governance temperature** (suppression capacity). In the compass, we replace P/V with Parasitism/Variation. A system flips into a parasitism sinkhole when accumulated Rule-13 debt (latent entropy) exceeds metabolic output available to suppress it.

Example thresholds (preliminary):
- Venice late: +5% rigidity (H1–H3) → bifurcation into high-Y trap
- USA modern: -8% cheater detection (G1) → proxy crosses 30% in <10% drift

The analyzer turns the tool from snapshot diagnostic to early-warning system — identifying leverage points before fracture.

## 9.3 The Mathematical Engine: Longevity Fits & Ensemble Statistics

To quantify the probability clouds, we fit two survival models to ensemble durations (n=100 noisy runs per replicator). Model choice itself becomes a secondary diagnostic of the system's structural nature.

### 9.3.1 Weibull Model — Adaptive Resilience

The Weibull distribution is flexible and ideal for systems with modular aging or infant mortality. Its hazard function h(t) determines how the risk of death changes over time:

$$
h(t) = \frac{k}{\lambda} \left( \frac{t}{\lambda} \right)^{k-1}
$$

Survival function:

$$
S(t) = e^{-\left( t / \lambda \right)^k}
$$

Units: λ (scale parameter) is expressed in years — the characteristic life at which ~63.2% of the population has "failed" under Weibull assumptions. For polity-scale replicators, this provides a natural timescale (decades to centuries); for faster-evolving systems (e.g., algorithmic replicators), λ may require logarithmic scaling or separate calibration in future iterations.

- **Shape parameter k** — the "Vitality Coefficient"
  - k < 1: decreasing hazard ("learning" phase, infant mortality)
  - k = 1: constant hazard (memoryless, exponential decay)
  - k > 1: increasing hazard (aging)

Ant colonies typically show high k (~3–4) with slow acceleration — strong aging resistance. Ethereum baseline shows k ≈ 2.1 — structured but accelerating decay of initial "founding entropy."

**Figure 9.2: Hazard Rate Comparison – Weibull vs Gompertz**

![Figure 9.2](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_9_2_hazard_comparison.png)

**Caption:** Hazard rate h(t) comparison: ant colonies (Weibull k ≈ 3.2, gradual increase reflecting adaptive resilience) vs. late VOC (Gompertz with large b, rapid exponential acceleration after Rule-13 threshold crossing).

### 9.3.2 Gompertz Model — Rigid Fragility

For high governance-density systems (late VOC, PRC), Gompertz often fits better. It captures exponential acceleration of failure as rigidity blocks adaptation:

$$
h(t) = a e^{bt}
$$

Survival function:

$$
S(t) = \exp\left( \frac{a}{b} (1 - e^{bt}) \right)
$$

- **Growth parameter b** — the "Rigidity Penalty"
  - In late VOC, b spikes once Rule-13 parasitism crosses 30%, causing hazard to double every ~ln(2)/b years (15–20 years in example fits) until lattice fracture.

For each ensemble:
- Median longevity + 95% CI
- Hazard rate curve
- P(survive >500 years)

Preliminary fits:
- Ant colonies: Weibull k ≈ 3.2, λ large (characteristic life >>1000 years), P(survive 500 y) >95%
- Late VOC: Gompertz dominant with large b, characteristic life much shorter once rigidity penalty activates, P(survive 500 y) <20%
- Ethereum baseline: Weibull k ≈ 2.1, median longevity ≈700 years (toy proxy from ensemble), wide CI from stake-concentration noise

The tool now quantifies decay curves — probabilistic health trajectories, not point guesses.

## 9.4 Sensitivity Matrix & Community Extension

Not all metrics are equally important. The Sensitivity Matrix quantifies impact: sweep ±20% on each metric individually, measure normalized delta in median longevity (t_{50}), proxy, Row 13 par intensity:

$$
s_m = \frac{ \Delta o / \Delta m }{ \max(\Delta o / \Delta m) } , \quad o \in \{ t_{50}, \text{proxy}, \text{Row 13 par} \}
$$

Example (preliminary on USA 1971 model):

| Metric | Δ t_{50} | Δ Proxy | Δ Row 13 par | Sensitivity Rank |
|--------|----------|---------|--------------|------------------|
| G1     | –0.45    | +0.80   | +0.65        | 1 (high)         |
| D1     | –0.32    | +0.55   | +0.70        | 2                |
| C2     | +0.28    | –0.40   | –0.35        | 3                |
| A2     | +0.08    | –0.10   | –0.12        | 10 (low)         |

**Note on non-linear coupling**  
In high-Y rigid systems (e.g., late Rome, PRC), metrics are often coupled: a degradation in G1 (cheater detection) frequently correlates with compensatory increases in H2–H3 (ideological monopoly / dissent suppression) as the system attempts to maintain control. Future ensemble runs could incorporate a covariance matrix Σ for selected metric pairs (e.g., cov(G1, H2) < 0), allowing realistic correlated perturbations during stochastic sweeps. This would better capture positive-feedback loops that accelerate bifurcation once Rule-13 debt accumulates beyond suppression capacity. Prototype support for correlated noise can be added to `run_ensemble()` via NumPy `multivariate_normal`; open to community PRs for empirical covariance estimates from historical cases.

v2 is still early: noise model simple (Gaussian), fits preliminary, bifurcation sweeps manual. The repo (`simulate.py` and prototype extensions) now includes / plans:
- Ensemble runner (`run_ensemble(replicator_csv, n=100, noise_std=0.1)`)
- Weibull/Gompertz fit stubs (using `scipy.stats` and `lifelines`)
- Bifurcation scanner (`sweep_metric(metric, range_pct=20, steps=20)`)
- Sensitivity matrix generator

Open for refinement:
- Scale-specific noise profiles (RNA low, polities high)
- Automated tipping-point detection
- Bayesian longevity priors from historical data

The microscope is evolving — from static lens to dynamic, probabilistic observer.
