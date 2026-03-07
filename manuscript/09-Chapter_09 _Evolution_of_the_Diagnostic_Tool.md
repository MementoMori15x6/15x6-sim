# 09 - Chapter 09 – Evolution of the Diagnostic Tool
![](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/banners/banner_ch09_diagnotic_evolution.png)
Memento & Mori | December 2025 – ongoing

## 9.1 From Deterministic v1 to Stochastic v2

The original 35-metric compass (v1) was deterministic: fixed scores from public evidence, fixed shocks, fixed longevity extrapolations. It revealed recurring patterns — Rule-13 exploitationism >30% as collapse signal, balanced mutualism/competition in rows 6–8 & 13–14 as health indicator — but treated replicators as static snapshots.

v2 introduces stochastic realism. Real systems drift: small metric fluctuations (±5–10%) arise from environmental noise, measurement uncertainty, or hidden variables. We model this by adding Gaussian noise ε_j ~ N(0, σ) to each metric score across ensemble runs (n=100 per replicator):

$$
s_{j,i} = s_j + \epsilon_{j,i}, \quad \epsilon_{j,i} \sim \mathcal{N}(0, \sigma), \quad \sigma \in [0.05, 0.10]
$$

(σ expressed as fraction of full -10 to +10 scoring range, corresponding to ~±0.5 to ±1 point uncertainty per metric.)

Recompute compass coordinates, Rule-13 proxy, longevity estimate, and Row 13 intensity for each realization i.

Early test cases illustrate the shift:
- Ant colonies (low intrinsic variance): noise barely perturbs mutualism-dominant grid; longevity distributions remain tight (high stability).
- Late VOC (high internal variance): noise amplifies exploitationism spikes in Row 13; longevity distributions widen dramatically (fragility signal).

**Figure 9.1: Stochastic Drift – Ant Colonies vs Late VOC**  
![Figure 9.1](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_9_1_stochastic_drift.png)  
**Caption:** Ensemble scatter on compass plane (n=100): ants (tight cluster in high-mutualism zone), late VOC (wide smear toward exploitationism/Chaos Boundary sinkhole).

The microscope now sees probability clouds around attractors, not just point estimates.

## 9.2 Calibration Reference Layer (CRL)

**Version & Consensus Note**  
The anchor scores, CRL values, and diagnostics presented in this chapter (and cross-referenced in Chapter 12) are drawn from an early primer consensus (December 2025 – February 2026) used to draft the manuscript. These were generated with an initial version of the compass protocol and `simulate.py` (pre-v2.0).  

Subsequent refinements — scalar safety fixes, active rigidity multiplier with vs/up debug, filename-triggered CRL enforcement, and ensemble improvements — have been applied in the live repository (v2.0, March 2026). Readers reproducing runs locally may observe modest differences in X, Y, R, or Rule-13 proxy for the same anchors. These reflect ongoing calibration, not errors in the manuscript.  

The values below remain useful as historical illustrations and provisional reference points. The repository (/data/anchors/) contains the most current outputs and reproducibility code. Community PRs to update ledger rows with v2.0+ runs are encouraged to keep the ledger synchronized with the evolving protocol.

The compass is a diagnostic instrument, not a fixed index. To achieve cross-model reproducibility and reduce interpretive variance, the protocol relies on the Calibration Reference Layer (CRL): a set of canonical replicators with locked or provisional anchor values. These serve as orientation priors—stabilizing the meaning of extreme scores and ensuring proportionality across scorers and frontier models.

  ### Calibration Reference Layer (CRL) Anchors

| Anchor Name              | Snapshot Period       | Key Enforced Metrics                  | Proxy % | X / Y (post-scaling) | Zone                  | Longevity Window      | Note                                                                 |
|--------------------------|-----------------------|---------------------------------------|---------|----------------------|-----------------------|-----------------------|----------------------------------------------------------------------|
| Chaos Boundary (VOC)     | Late 1780–1785       | D1=9, G1=-8, F2=-8, E1=2             | ~65%    | X negative, Y moderate | Chaos Boundary        | Short (10–40 years)   | Unchecked parasitism → entropy export failure                        |
| Rigid Trap (USSR)        | 1937 (Great Purge peak) | D1=9, G1=-8, H2/H3/L2/L3=9–10      | 68.8%   | X ≈0.04, Y=2.05      | Rigid Trap (Brittle)  | 30–80 years           | Max suppression + weaponized detection → brittleness                 |
| Mutualism Reference (Provisional) | USA 1787–1789 (Constitution) | A1=+10, D1=-6, G1=+8, C2=+9, H3=-7, L2=-9 | ~20–30% | X positive, Y low-mod | Dynamic Mutualism     | 150–300+ years        | Balanced mutualism/competition, strong error repair — provisional; PRs welcome to refine scoring |

### 9.2.1 Hard-Locked Canonical Anchors

The CRL includes a growing set of hard-locked canonical anchors with enforced hinge metrics. These centers and bands are calibrated from historical evidence and multi-model consensus, then enforced in `simulate.py` (via anchor dictionaries) to ensure reproducibility across runs and scorers.

#### 9.2.1.1 Late VOC (1780–1785 snapshot) – Corporate Exploitative Collapse / Chaos Boundary

The Late VOC during the acute phase of the Fourth Anglo-Dutch War (1780–1785) is the first hard-locked reference for **corporate exploitative collapse** transitioning to the **Chaos Boundary** basin. This snapshot exhibits naval blockade-induced metabolic severance, zero liquidity, endemic servant corruption/private trade dominance, distant oversight failure, and formal institutional shell persistence via bailouts.

The following hinge metrics are **hard-locked** as calibration centers with ±1 confidence bands:

| Metric                | Canonical Center | Confidence Band | Justification (locked for reproducibility) |
|-----------------------|------------------|-----------------|--------------------------------------------|
| D1 Exploitationism    | +9               | 8 – 10          | Endemic servant corruption, particuliere handel, and smuggling reached structural dominance; private extraction exceeded legitimate trade flows under blockade. |
| F2 Error Repair       | −8               | −7 to −9        | Systemic breakdown: Heeren XVII oversight failed to detect or correct cascading failures (falsified reports, fleet losses, corruption); no meaningful repair capacity. |
| G1 Cheater Detection  | −8               | −7 to −9        | Internal visibility collapsed; widespread graft went undetected/unpunished at scale, triggering Enforcement Decay shim. |
| E1 Survival           | +2               | 1 – 3           | Zombie/legal shell persisted via Republic bailouts and charter continuity, but no independent metabolic survival (zombie cap under blockade ceiling). |

**Secondary guidance (provisional):**  
- D2 Competition ≈ −8 (±1)  
- A2 Market Allocation ≈ −6 (±1)

**Application notes:**  
- These locked hinge values stabilize Rule-13 leakage calculations and Enforcement Decay/Ratchet shims across all ensemble runs and future scorings.  
- Locked values are enforced in `simulate.py` (VOC_ANCHORS dict) and multi-model passes.  
- Confidence bands allow minor interpretive flexibility while anchoring the integrity hinge.  
- See Chapter 5 for the full Late VOC case study and multi-model consensus application.

#### 9.2.1.2 USSR ~1937 (Great Purge peak) – Rigid Trap / High-Y Suppression

The USSR at the height of the Great Purge (1937) is hard-locked as the primary reference for **high-Y rigid trap** dynamics: extreme ideological monopoly, dissent suppression, leadership cult, purge cycles, and weaponized (but brittle) cheater detection.

Hard-locked hinge metrics:

| Metric                   | Canonical Center | Confidence Band | Justification |
|--------------------------|------------------|-----------------|--------------|
| D1 Exploitationism       | +9               | 8 – 10          | Total state extraction |
| H2 Ideological Monopoly  | +9               | 8 – 10          | Marxism-Leninism-Stalinism sole framework |
| H3 Dissent Suppression   | +9               | 8 – 10          | Great Purge peak |
| L2 Leadership Cult       | +9               | 8 – 10          | Stalin infallibility |
| L3 Purge Cycles          | +9               | 8 – 10          | Violent elite turnover |
| G1 Cheater Detection     | −8               | −7 to −9        | NKVD quotas/false positives |

**Application notes:**  
- Enforced in `simulate.py` (USSR_ANCHORS dict).  
- Produces high rigidity penalty (R ≈ 0.74) and Y ≈ 2.78 after boost.

#### 9.2.1.3 United States ~1789 (Constitutional founding) – Mutualism / Healthy Baseline

The United States at the 1787–1789 constitutional founding is hard-locked as the primary reference for **adaptive mutualism** with strong cheater detection, modularity, low suppression, and balanced competition.

Hard-locked hinge metrics:

| Metric                   | Canonical Center | Confidence Band | Justification |
|--------------------------|------------------|-----------------|--------------|
| G1 Cheater Detection     | +8               | 7 – 9           | Strong early institutions for detecting & punishing graft/corruption |
| G2 Modularity            | +7               | 6 – 8           | Federal structure + separation of powers enables subsystem autonomy |
| G3 Info Storage          | +8               | 7 – 9           | Written Constitution, free press foundations, literacy/high info fidelity |
| D1 Exploitationism       | −2               | −4 – 0          | Low systemic parasitism; rent-seeking checked by competition & rule of law |
| D2 Competition           | +6               | 5 – 7           | Healthy market & political competition; no monopoly dominance |
| H2 Ideological Monopoly  | −5               | −7 – −3         | No state religion or enforced orthodoxy; pluralist founding ethos |
| H3 Dissent Suppression   | −6               | −8 – −4         | First Amendment protections; dissent channeled via elections & press |
| L2 Leadership Cult       | −7               | −9 – −5         | No personality cult; Washington precedent |
| L3 Purge Cycles          | −8               | −9 – −7         | Peaceful electoral turnover; no violent elite culls |
| F2 Error Repair          | +6               | 5 – 7           | Constitutional amendment + judicial review functional |

**Application notes:**  
- Enforced in `simulate.py` (USA_1789_ANCHORS dict).  
- Produces low Rule-13 proxy (~10%) and near-zero Y (−0.02).

### 9.2.2 Phased CRL Development

Calibration proceeds in phases to maintain rigor without over-constraint:

- **Phase 1 (complete)**: Late VOC (1780–1785) locked as primary collapse / Chaos Boundary anchor.
- **Phase 2 (complete)**: USSR ~1937 (Rigid Trap) and United States ~1789 (Mutualism / healthy baseline) locked for rigidity and adaptive mutualism references.
- **Phase 3 (ongoing / provisional)**: Remaining references (Roman Empire ~100 CE, British Empire ~1850, Nazi Germany ~1942, Qing Dynasty ~1820, Bitcoin Network ~2023) remain provisional with descriptive ranges; open to community multi-model runs and PR proposals.

The CRL is a living layer—extensible via evidence and consensus. Future anchors will follow the same center + band format to preserve reproducibility while welcoming expert refinement.
For current X, Y, R, and Rule-13 diagnostics on these locked anchors, see the triangulation set in Chapter 12 (Master Ledger) and /data/anchors/ in the repository.

## 9.3 Bifurcation Analyzer

Small metric changes can push a replicator across phase boundaries — from mutualism ellipsoid to exploitationism sinkhole. The bifurcation scanner sweeps selected metrics (D1 exploitationism, G1 detection, C2 variation, H2 ideological monopoly, etc.) in ±20% increments and tracks critical crossings:
- Rule-13 proxy >30%  
- Row 13 exploitationism intensity >40%  
- Longevity drops below 500 years  

This mirrors a Clausius-Clapeyron-like phase transition: just as physical matter changes state under pressure and temperature, social replicators bifurcate when **metabolic pressure** (exploitationism load) exceeds available **governance temperature** (suppression capacity and cost). In the compass, we replace P/V with Exploitationism/Variation. A system flips into a exploitationism sinkhole when accumulated Rule-13 debt (latent entropy) exceeds metabolic output available to suppress it.

Example thresholds (preliminary):
- Late Venice: +5% rigidity (H1–H3) → bifurcation into high-Y trap  
- USA modern: -8% cheater detection (G1) → proxy crosses 30% in <10% drift  

Bifurcation sweeps currently treat metrics independently; future iterations will incorporate correlated perturbations (see 9.5 note on covariance). The analyzer turns the tool from snapshot diagnostic to early-warning system — identifying leverage points before fracture.

## 9.4 The Mathematical Engine: Longevity Fits & Ensemble Statistics

To quantify the probability clouds, we fit two survival models to ensemble durations (n=100 noisy runs per replicator). Model choice (Weibull vs. Gompertz) is determined by AIC/BIC fit on ensemble data; high-governance-density systems favor Gompertz due to accelerating hazard from rigidity penalties.

### 9.4.1 Weibull Model — Adaptive Resilience

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

Ant colonies typically show high k (~3–4 ±0.4) with slow acceleration — strong aging resistance. Ethereum baseline shows k ≈ 2.1 — structured but accelerating decay of initial "founding entropy."

**Figure 9.4: Hazard Rate Comparison – Weibull vs Gompertz**  
![Figure 9.4](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_9_4_hazard_comparison.png)
**Caption:** Hazard rate h(t) comparison: ant colonies (Weibull k ≈ 3.2 ±0.4, gradual increase reflecting adaptive resilience) vs. late VOC (Gompertz with large b, rapid exponential acceleration after Rule-13 threshold crossing).

### 9.4.2 Gompertz Model — Rigid Fragility

For high governance-density systems (late VOC, PRC), Gompertz often fits better. It captures exponential acceleration of failure as rigidity blocks adaptation:

$$
h(t) = a e^{bt}
$$

Survival function:

$$
S(t) = \exp\left( \frac{a}{b} (1 - e^{bt}) \right)
$$

- **Growth parameter b** — the "Rigidity Penalty"  
  - In late VOC, b spikes once Rule-13 exploitationism crosses 30%, causing hazard to double every ~ln(2)/b years (15–20 years in example fits) until lattice fracture.

For each ensemble:
- Median longevity + 95% CI  
- Hazard rate curve  
- P(survive >500 years)  

Preliminary fits:
- Ant colonies: Weibull k ≈ 3.2 (±0.4), λ large (>>1000 years), P(survive 500 y) >95%  
- Late VOC: Gompertz dominant with large b, characteristic life much shorter once rigidity penalty activates, P(survive 500 y) <20%  
- Ethereum baseline: Weibull k ≈ 2.1, median longevity ≈700 years (toy proxy from ensemble), wide CI from stake-concentration noise  

The tool now quantifies decay curves — probabilistic health trajectories, not point guesses.

## 9.5 Sensitivity Matrix & Community Extension

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
In high-Y rigid systems (e.g., late Rome, PRC), metrics are often coupled: a degradation in G1 (cheater detection) frequently correlates with compensatory increases in H2–H3 (ideological monopoly / dissent suppression) as the system attempts to maintain control. Future ensemble runs could incorporate a covariance matrix Σ for selected metric pairs (e.g., cov(G1, H2) < 0), allowing realistic correlated perturbations during stochastic sweeps. This would better capture positive-feedback loops that accelerate bifurcation once Rule-13 debt accumulates beyond suppression capacity. Prototype support for correlated noise can be added to `run_ensemble()` via NumPy `multivariate_normal`; **open to community PRs for empirical covariance estimates from historical cases**.

v2 is still early: noise model simple (Gaussian), fits preliminary, bifurcation sweeps manual. The repo (`simulate.py` and prototype extensions) now includes / plans:
- Ensemble runner (`run_ensemble(replicator_csv, n=100, noise_std=0.1)`)  
- Weibull/Gompertz fit stubs (using `scipy.stats` and `lifelines`)  
- Bifurcation scanner (`sweep_metric(metric, range_pct=20, steps=20)`)  
- Sensitivity matrix generator  

Open for refinement:
- Scale-specific noise profiles (RNA low, polities high)  
- Automated tipping-point detection  
- Bayesian longevity priors from historical data  

The diagnostic tool is no longer a static microscope — it is a dynamic, probabilistic observer, continuously refined through evidence, ensemble testing, and open collaboration.
