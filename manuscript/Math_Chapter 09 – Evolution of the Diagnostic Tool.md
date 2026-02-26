# Chapter 09 – Evolution of the Diagnostic Tool

## 9.1 From Deterministic v1 to Stochastic v2

The original 35-metric compass (v1) was deterministic: fixed scores s_j from public evidence, fixed shocks, fixed longevity extrapolations. It revealed recurring patterns — Rule-13 parasitism >30% as collapse signal, balanced mutualism/competition in rows 6–8 & 13–14 as health indicator — but treated replicators as static snapshots.

v2 introduces stochastic realism. Real systems drift: small metric fluctuations (±5–10%) arise from environmental noise, measurement uncertainty, or hidden variables. We model this by adding Gaussian noise ε_j ~ N(0, σ) to each metric score across ensemble runs (n=100 per replicator):

$$
s_{j,i} = s_j + \epsilon_{j,i}, \quad \epsilon_{j,i} \sim \mathcal{N}(0, \sigma), \quad \sigma = 0.05-0.10
$$

Then recompute compass coordinates, Rule-13 proxy, longevity estimate, and Row 13 intensity for each realization i.

Early test cases illustrate the shift:
- Ant colonies (low intrinsic variance): noise barely perturbs mutualism-dominant grid; longevity distributions remain tight (high stability).
- Late VOC (high internal variance): noise amplifies parasitism spikes in Row 13; longevity distributions widen dramatically (fragility signal).

The microscope now sees probability clouds around attractors, not just point estimates.

## 9.2 Bifurcation Analyzer

Small metric changes can push a replicator across phase boundaries — from mutualism ellipsoid to parasitism sinkhole. The bifurcation scanner sweeps selected metrics m ∈ {D1, G1, C2, H2, …} over range [s_m (1-r), s_m (1+r)], r=0.2, steps=20.

For each value m_k:
- Recompute ensemble (n=100) with fixed m_k + noise on others
- Record fraction of runs where proxy >30%, Row 13 par >40%, longevity <500y

Tipping threshold: first m_k where fraction >0.5.

This mirrors a Clausius-Clapeyron-like phase transition: just as physical matter changes state under pressure and temperature, social replicators bifurcate when **metabolic pressure** (parasitism load) exceeds available **governance temperature** (suppression capacity). In the compass, we replace P/V with Parasitism/Variation. A system flips into a parasitism sinkhole when accumulated Rule-13 debt (latent entropy) exceeds metabolic output available to suppress it.

Example thresholds (preliminary):
- Venice late: +5% rigidity (H1–H3) → bifurcation into high-Y trap
- USA modern: -8% cheater detection (G1) → proxy crosses 30% in <10% drift

The analyzer turns the tool from snapshot diagnostic to early-warning system — identifying leverage points before fracture.

## 9.3 The Mathematical Engine: Longevity Fits & Ensemble Statistics

To quantify the probability clouds, we fit two survival models to ensemble durations (n=100 noisy runs per replicator). Model choice itself becomes a secondary diagnostic.

### 9.3.1 Weibull Model — Adaptive Resilience
The Weibull distribution is flexible and ideal for systems with modular aging or infant mortality. Its hazard function is:

$$
h(t) = \frac{k}{\lambda} \left( \frac{t}{\lambda} \right)^{k-1}, \quad k>0, \lambda>0
$$

Survival function:

$$
S(t) = e^{-\left( t / \lambda \right)^k}
$$

Cumulative hazard:

$$
H(t) = \left( t / \lambda \right)^k
$$

- **Shape parameter k** — the "Vitality Coefficient"
  - k < 1: decreasing hazard ("learning" phase, infant mortality)
  - k = 1: constant hazard (memoryless, exponential decay)
  - k > 1: increasing hazard (aging)

Ant colonies typically show high k (~3–4) with slow acceleration — strong aging resistance. Ethereum baseline shows k ≈ 2.1 — structured but accelerating decay of initial "founding entropy."

### 9.3.2 Gompertz Model — Rigid Fragility
For high governance-density systems (late VOC, PRC), Gompertz often fits better. It captures exponential acceleration of failure as rigidity blocks adaptation:

$$
h(t) = a e^{bt}, \quad a>0, b>0
$$

Survival function:

$$
S(t) = e^{a/b (1 - e^{bt})}
$$

Cumulative hazard:

$$
H(t) = \frac{a}{b} (e^{bt} - 1)
$$

- **Growth parameter b** — the "Rigidity Penalty"
  - In late VOC, b spikes once Rule-13 parasitism crosses 30%, causing hazard to double every 15–20 years until lattice fracture.

Fit via maximum likelihood (`scipy.stats` or `lifelines`). For each ensemble:
- Median longevity + 95% CI
- Hazard rate curve
- P(survive >500 years)

Preliminary fits:
- Ant colonies: Weibull k ≈ 3.2, P(survive 500y) >95%
- Late VOC: Gompertz dominant, hazard accelerates sharply, P(survive 500y) <20%
- Ethereum baseline: Weibull k ≈ 2.1, median ~700y, wide CI from stake-concentration noise

The tool now quantifies decay curves — probabilistic health trajectories, not point guesses.

## 9.4 Sensitivity Matrix & Community Extension

Not all metrics are equally important. The Sensitivity Matrix quantifies impact: for each metric m, sweep ±20% and measure normalized delta in median longevity (t_{50}), proxy, Row 13 par intensity:

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

v2 is still early: noise model simple (Gaussian), fits preliminary, bifurcation sweeps manual. The repo (`simulate.py`) now includes:

- Ensemble runner (`run_ensemble(replicator_csv, n=100, noise_std=0.1)`)
- Weibull/Gompertz fit stubs (using `scipy.stats` and `lifelines`)
- Bifurcation scanner (`sweep_metric(metric, range_pct=20, steps=20)`)
- Sensitivity matrix generator

Open for refinement:
- Scale-specific noise profiles (RNA low, polities high)
- Automated tipping-point detection
- Bayesian longevity priors from historical data

The microscope is evolving — from static lens to dynamic, probabilistic observer.

Memento mori. 🚀
