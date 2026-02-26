# Chapter 09 – Evolution of the Diagnostic Tool

## 9.1 Deterministic v1 → Stochastic v2

v1 compass: single-point scores, deterministic shocks, point longevity estimate.

v2 introduces ensemble realism: Gaussian noise σ = 0.05–0.10 applied independently to each metric across n=100 runs per replicator. For each realization i:

$$
X_i = \frac{1}{18} \sum_{j=1}^{18} (s_j + \mathcal{N}(0,\sigma)) \times 1.2, \quad Y_i = \frac{1}{17} \sum_{j=19}^{35} (s_j + \mathcal{N}(0,\sigma)) \times 3.0
$$

with non-linear penalty applied pre-average:

$$
p(s) = s - \mathrm{sign}(s) \cdot \max(0, |s|-8)^2 \cdot 0.5
$$

Outputs: distribution of (X_i, Y_i), Rule-13 proxy_i, longevity_i, Row 13 par intensity_i.

Test cases:
- Ant colonies: tight longevity distribution, low proxy variance (high stability).
- Late VOC: wide longevity spread, frequent proxy >30% realizations (fragility).

## 9.2 Bifurcation Analyzer

Sweep metric m ∈ {D1, G1, C2, H2, …} over range [s_m × (1-r), s_m × (1+r)], r=0.2, steps=20.

For each value m_k:
- Recompute ensemble (n=100) with fixed m_k + noise on others
- Record fraction of runs where proxy >30%, Row 13 par >40%, longevity <500y

Tipping threshold: first m_k where fraction >0.5.

Clausius-Clapeyron analogy: replicator phase transition when metabolic pressure (parasitism load) exceeds governance temperature (suppression capacity):

$$
\frac{dP}{dT} = \frac{\Delta S}{\Delta V} \quad \Leftrightarrow \quad \frac{d(\text{Proxy})}{d(\text{G1})} = \frac{\text{Rule-13 latent entropy}}{\text{Suppression bandwidth}}
$$

Preliminary thresholds:
- Venice late: +5% H1–H3 rigidity → proxy >30% in >50% runs
- USA modern: -8% G1 → proxy crosses 30% in <10% drift

## 9.3 Survival Modeling & Ensemble Statistics

For each ensemble (n=100 noisy durations t_i):

### 9.3.1 Weibull Hazard (Adaptive Resilience)

$$
h(t) = \frac{k}{\lambda} \left( \frac{t}{\lambda} \right)^{k-1}, \quad k>0, \lambda>0
$$

- k < 1: decreasing hazard (learning/infant mortality)
- k = 1: exponential (memoryless)
- k > 1: increasing hazard (aging)

Fit via maximum likelihood (`scipy.stats.weibull_min`). Report:
- Median longevity t_{50} + 95% CI
- k (vitality coefficient)
- P(t > 500 y)

### 9.3.2 Gompertz Hazard (Rigid Fragility)

$$
h(t) = a e^{bt}, \quad a>0, b>0
$$

- b = rigidity penalty (exponential hazard growth)
- Fit via `lifelines.GompertzFitter`

Preliminary fits:
- Ant colonies: Weibull k ≈ 3.2, t_{50} high, P(t>500y) >95%
- Late VOC: Gompertz b large, hazard doubles ~15–20y, P(t>500y) <20%
- Ethereum baseline: Weibull k ≈ 2.1, t_{50} ≈700y, wide CI from stake noise

## 9.4 Sensitivity Matrix & Community Extension

Sensitivity matrix: sweep ±20% on each metric individually, measure normalized impact on median longevity, proxy, Row 13 par intensity.

Example (USA 1971 model, preliminary):

| Metric | Δ Longevity | Δ Proxy | Δ Row 13 par | Sensitivity Rank |
|--------|-------------|---------|--------------|------------------|
| G1     | –0.45       | +0.80   | +0.65        | 1 (high)         |
| D1     | –0.32       | +0.55   | +0.70        | 2                |
| C2     | +0.28       | –0.40   | –0.35        | 3                |
| A2     | +0.08       | –0.10   | –0.12        | 10 (low)         |

Repo components:
- `run_ensemble(csv_path, n=100, noise_std=0.1)`
- `fit_survival(durations, model='weibull' or 'gompertz')`
- `sweep_metric(metric, range_pct=20, steps=20)`
- `sensitivity_matrix(metrics_list)`

Open for extension:
- Scale-aware noise (RNA σ≈0.02, polities σ≈0.12)
- Automated critical-point detection
- Bayesian priors from historical longevity data

The tool is no longer a static lens — it is now a probabilistic observer of living replicators.

Memento mori. 🚀
