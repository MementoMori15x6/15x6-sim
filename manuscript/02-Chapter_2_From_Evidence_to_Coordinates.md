# 02 - Chapter 2: From Evidence to Coordinates
![](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/banners/banner_ch02_Roman_road08.png)
Memento & Mori | December 2025 – ongoing

**The 35-Metric Compass and 15×6 Grid as a Diagnostic Lens for Political Thermodynamics**

## Introduction – The Compass Protocol

The Political Thermodynamics framework treats polities as far-from-equilibrium replicating systems governed by fifteen base rules (Chapter1). The 35-metric compass converts qualitative historical evidence into quantitative coordinates: X axis(economic metabolism) from metrics A–G, Y axis (governance density) from H–M. Non-linear penalties amplify extremes, rigidity adjustment boosts suppression costs, and inverse-distance splatter assigns zone percentages. The 15×6 grid maps these to interaction distributions (Mutualism to Neutralism), with Rule 13 highlighted as the key specificity sensor.

The diagnostic power lies in row shape, not just percentages: a flat Rule 13 row signals loss of cheater-detection specificity (inability to distinguish legitimate variation from parasitism), even if raw parasitism % remains moderate.

The entropy export ratio (mean mutualism % / mean parasitism %) serves as a life-support monitor for the system. Values well above 1.0 indicate net-positive dissipation outward; **sustained drift toward or below ~1.0–1.1 signals a potential "kill-switch"** — thermodynamic collapse where internal friction matches or exceeds external harvesting capacity.

:::info Compass Metrics at a Glance
**Economic Axis (X – A–G, 18 metrics)**

- A1–A3: Property, market allocation, profit motive
- B1–B2: Redistribution, welfare
- C1–C3: Heredity fidelity, variation, persistence
- D1–D2: Parasitism tolerance, competition intensity
- E1–E2: Survival, niche construction & colonization
- F1–F2: Boundary maintenance, error detection & repair
- G1–G3: Cheater detection, modularity, info storage

**Governance Axis (Y – H–M, 17 metrics)**:

- H1–H3: Cultural uniformity, ideological monopoly, dissent suppression
- I1–I3: Family autonomy, religious freedom, artistic expression
- J1–J3: Scientific direction, education indoctrination, media control
- K1–K3: Military priority, isolationism, external threat narrative
- L1–L3: Succession mechanism, leadership cult, purge cycles
- M1–M3: Natalism, migration control, ethnic policy

For the complete 35-metric list (exact labels, descriptions, -10/+10 anchors), scoring guidelines, rationale discipline, prompt templates, consensus ensemble method, X/Y formulas, entropy export ratio, and mapping to the 15×6 grid, see:  
- [Compass 35-Metric Protocol](https://github.com/MementoMori15x6/15x6-sim/blob/main/docs/compass_35_metrics_protocol.md) (primary reference)  
- Appendix A (compiled protocol in manuscript)  
- Chapter 12 Appendix: Living Ledger (for filled examples once populated)  

Scoring uses public historical consensus via structured prompts averaged across multiple LLMs. Full calculations, grids, and drift simulations reproducible via `simulate.py`.

This chapter applies the compass to three Roman phases, demonstrating how it reveals universal signatures: separatrix fragility, crystallization resets, and variation-longevity trade-offs.

## Case Study 1: Late Roman Republic (133–27 BCE) – Separatrix Crisis

The late Republic is a textbook high-metabolism separatrix state: conquest niches (Rule 10) export massive negative entropy, buffering internal decay until coordination failure cascades.

**Figure 2.1: Late Roman Republic 15×6 Heatmap**

![](https://raw.githubusercontent.com/MementoMori15x6/15x6-sim/main/figures/fig_2_1_late_republic_heatmap.png)

Consensus heatmap of the late Republic (133–27 BCE) reveals a classic separatrix splatter: high variance across interaction moves, with Rule 13 row flat at ~18–20% parasitism (diagnostic of lost cheater-detection specificity — inability to distinguish legitimate variation from factional cannibalization). Export rows (1, 6, 10) remain strong (~35–43% mutualism/competition), but governance erosion flattens the grid overall. Entropy export ratio ≈ 7.82.

**Figure 2.2: Republic Drift Curve**

![](https://raw.githubusercontent.com/MementoMori15x6/15x6-sim/main/figures/fig_2_2_republic_drift_curve.png)

Cumulative drift simulation from 133 BCE onward shows the high-metabolism paradox: expansion buffer (200–100 BCE — massive negative entropy from Rule 10 niches) delays the kill-switch crossing despite rising parasitism. Export starts at ~7.8, plateaus, then plunges to ~1.1 by ~27 BCE as coordination failure cascades. Rule-13 parasitism climbs steadily to ~20%, signaling specificity loss.

**Table 2.1: Key Metric Deltas – Republic Crisis Phase**

| Metric Group | Average Score | Interpretation |
| --- | --- | --- |
| A1–A3 (Property/Market) | ~5.5 | Moderate positive; conquest profits buffer redistribution pressures |
| L1–L3 (Succession) | ~2.5 | Fragile, leading to civil wars |
| Rule 13-related (H/I/J) | ~3.0 | Creeping suppression cost, flat row shape |

## Case Study 2: Principate Reset (27 BCE – ~180 CE) – Hierarchical Cooling

The Principate is a thermodynamic reorganization: Augustus and the adoptive emperors traded republican variation for centralized hierarchy, suppressing parasitism and rebounding export.

**Figure 2.3: Early Principate 15×6 Heatmap (Consensus Reset)**

![](https://raw.githubusercontent.com/MementoMori15x6/15x6-sim/main/figures/fig_2_3_principate_heatmap.png)

Consensus grid for the Principate (27 BCE – ~180 CE) shows hierarchical cooling: Rule 13 row sharply skewed toward mutualism/hierarchy (19.1% each), with parasitism crushed to ~4.4%. Export rows (10–11) dominate (~40–44% mutualism/competition), reflecting reopened outward dissipation. Variation penalty (C2/I1–I3 lower) trades degrees of freedom for Y-density gains. Entropy export ratio ≈ 7.16.

**Table 2.2: Key Metric Deltas – Principate Reset**

| Metric Group | Average Score | Interpretation |
| --- | --- | --- |
| G1–G3 (Cheater/Modularity) | ~6.5 | Centralized oversight restores specificity |
| L1–L3 (Succession) | ~3.3 | Adoptive system buys stability |
| K1–K3 (Military) | ~5.7 | Prioritized but redirected outward |
| **Variation & Autonomy (C2/I1–I3)** | ~4.5 | **Reduced scores reflect trade-off for Y-density gains** |

**The Principate's stability was not just "good leadership," but a cooling reorganization that traded internal variation for hierarchical stability.**

## Case Study 3: Forward Drift & Third Century Anarchy Cascade (~180–300 CE)

Starting from the Principate baseline, forward simulation tests longevity: gradual creep + shocks reveal a ~200-year plateau before acceleration.

**Figure 2.4: Principate Forward Drift – Stability → Third Century Anarchy Cascade**

![](https://raw.githubusercontent.com/MementoMori15x6/15x6-sim/main/figures/fig_2_4_principate_drift.png)

Forward simulation from Principate baseline reveals ~200-year stability plateau (~7.2 → ~5.5 by ~150–200 CE) before anarchy acceleration post-235 CE (legionary pay-rise shocks fuel cannibalization surge). Export decays to ~2.0–2.5 by ~270–300 CE as Rule-13 parasitism surges >20%, demonstrating the entropy cycle restarting under renewed suppression-cost pressure.

**Table 2.3: Key Metric Deltas – Anarchy Cascade**

| Metric Group | Baseline Score | End Score (~300 CE) | Interpretation |
| --- | --- | --- | --- |
| L1–L3 (Succession) | ~3.3 | ~ -2.0 | Fragility restarts cycle |
| G1–G3 (Cheater/Modularity) | ~6.5 | ~3.0 | Erosion leads to splintering |
| K1–K3 (Military) | ~5.7 | ~8.5 | Over-priority turns parasitic |

The ~2.0–2.5 export floor at ~270–300 CE represents **Boundary Saturation**: enough residual heat and boundary maintenance (Rule 11) to enable Aurelian/Diocletianic re-stabilization rather than total thermodynamic death.

**Table 2.4: Phase Evolution Ledger Summary**

| Phase | Zone | Export Ratio | Variation & Autonomy (C2/I1–I3) | Health Signature |
| --- | --- | --- | --- | --- |
| Late Republic crisis | Separatrix | 7.8 → ~1.1 | High (0.4–0.6) | High-Metabolism Splatter |
| Principate Reset | Stressed Mutualism | ~7.2 | Low (0.1–0.3) | Hierarchical Cooling |
| Anarchy Cascade end (~300 CE) | Active Competition / Boundary Saturation | ~2.0–2.5 | Minimal | Boundary Saturation Floor |

These patterns reinforce the central thesis: political systems rarely annihilate; they reorganize into more rigid lattices when variation bandwidth becomes unsustainable. Rule 13 row shape proves a leading indicator: flatness signals impending coordination failure; sharpening indicates successful cooling. The variation-longevity trade-off is stark: the Principate gained ~200–250 years by constraining internal degrees of freedom, but the entropy cycle eventually restarts when suppression specificity erodes again.

Implications extend beyond Rome. The compass offers a falsifiable lens for other polities—Han China, Byzantine transitions, or modern states—where similar signatures (separatrix drift, crystallization resets, boundary saturation floors) may emerge. Future work can refine kill-switch thresholds, test variation-longevity correlations across scales, and apply the protocol to contemporary replicating systems facing analogous pressures.

## Synthesis & Implications

The Roman case demonstrates the diagnostic power of the 35-metric compass and 15×6 grid: from qualitative evidence to quantitative coordinates, it consistently reveals universal thermodynamic signatures across three distinct phases.

**Figure 2.5: Roman Life-Cycle – Full Thermodynamic Arc (133 BCE – 300 CE)**

![](https://raw.githubusercontent.com/MementoMori15x6/15x6-sim/main/figures/fig_2_5_roman_life_cycle.png)

Combined drift plot illustrates the full Roman arc: late Republic separatrix plunge (export 7.8 → ~1.1), Principate reset jump at 27 BCE (export rebound to ~7.2, parasitism crash to ~4.4%), and Third Century anarchy cascade (export decay to ~2.0–2.5 by ~270–300 CE). The ~200–250 year plateau reflects hierarchical cooling; the Aurelian floor (~2.0–2.5 export) enables re-crystallization into the Dominate rather than total thermodynamic death.

The late Republic illustrates **separatrix fragility**: a high-metabolism system (X ≈ 0.42) trapped in a fragile equilibrium (Y ≈ 0.21), where external conquest niches (Rule 10) provide an entropy buffer that delays collapse for decades despite creeping internal coordination failure. The diagnostic signal is the **flat Rule 13 row** (~18–20% parasitism): cheater detection loses specificity, becoming unable to distinguish legitimate variation from factional cannibalization, even as raw parasitism remains moderate.

The Principate reset exemplifies **crystallization**: a reorganization that trades variation bandwidth (lower C2/I1–I3 scores) for hierarchical stability (sharpened Rule 13 mutualism/hierarchy dominance, parasitism crushed to ~4.4%). Export rebounds (~7.2) and governance density jumps (Y ≈ 0.51), moving the system into Stressed Mutualism and buying centuries of relative equilibrium.

The forward drift into the Third Century crisis shows the cycle restarting: gradual entropy accumulation erodes suppression specificity, military parasitism surges post-235 CE (legionary pay-rise shocks fueling cannibalization), and export decays to a low but positive floor (~2.0–2.5) by ~270–300 CE. This **Aurelian floor**—Boundary Saturation rather than total thermodynamic death—explains why the empire did not vanish but re-freezes into the more rigid Dominate lattice under Diocletian.

## Synthesis & Implications

The Roman arc on the 15×6 board moves us beyond familiar historical narratives — ambitious generals, corrupt senates, wise emperors — into measurable thermodynamic dynamics of a replicating system. The 35-metric compass and grid consistently reveal three universal signatures that transcend Rome's specific stories:

**Figure 2.5: Roman Life-Cycle – Full Thermodynamic Arc (133 BCE – 300 CE)**

![](https://raw.githubusercontent.com/MementoMori15x6/15x6-sim/main/figures/fig_2_5_roman_life_cycle.png)

1. **Separatrix fragility in high-metabolism states**  
   The late Republic (133–27 BCE) is a classic separatrix crisis: conquest-driven Rule 10 niches export massive negative entropy (ratio ~7.8), delaying collapse despite internal leaks. Yet the diagnostic is not raw parasitism volume — it is the **flat Rule 13 row** (~18 % across moves, parasitism only ~8.6 %). Cheater detection loses specificity, unable to distinguish legitimate variation from factional cannibalization, even as external buffers hold. This explains why coordination failure cascaded only after expansion slowed.

2. **Crystallization resets via variation suppression**  
   The Principate (27 BCE–~180 CE) is a thermodynamic reorganization: Augustus and the adoptive emperors traded degrees of freedom (lower C2/I1–I3 scores) for hierarchical cooling. Rule 13 sharpens toward mutualism/hierarchy dominance (parasitism crushed to ~4.4 %), entropy export rebounds (~7.2), and governance density rises (Y ≈ 0.51). The board shows this as **Stressed Mutualism** — not just "good leadership," but a deliberate cost-benefit trade that restored cheater-suppression specificity and bought 200–250 years of persistence.

3. **Persistent entropy cycles and boundary saturation floors**  
   Forward drift into the Third Century crisis restarts the cycle: military shocks erode suppression mechanisms, parasitism surges in Rows 6/12, and export decays to ~2.0–2.5 by ~270–300 CE. This **Aurelian floor** — boundary saturation rather than total thermodynamic death — enables re-crystallization into the more rigid Dominate lattice. The board quantifies why empires rarely annihilate: residual heat and Rule 11 maintenance provide just enough dissipation for reorganization.

Placing Rome on the board thus reveals a deeper pattern: ancient polities obey the same fifteen rules and entropy-export imperatives as RNA replicators, eusocial colonies, or modern states. The familiar events are surface symptoms; the underlying dynamics are universal — separatrix plunges masked by buffers, crystallization trades, and cycles that restart when Rule 13 specificity erodes. By quantifying these, the compass offers a falsifiable, reproducible diagnostic lens applicable to Han China, Byzantine transitions, or any replicating system facing analogous pressures. Future ledger entries can test these signatures across scales and refine the kill-switch thresholds.
