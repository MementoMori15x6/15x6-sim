# 11 - Chapter 11 – Phase-Space Topology: The Full Map
![](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/banners/banner_ch11_phase-space02.png)
Memento & Mori | December 2025 – ongoing

## 11.1 From Diagnostic Points to Attractor Catalog

Chapters 1–10 used the 35-metric compass and 15×6 grid to diagnose individual replicators, apply shocks, evolve the tool, and navigate toward healthier regions. The results were consistent: stable mutualism zones, exploitationism sinkholes, competition toroids, and rigidity walls.

Chapter 11 steps back to map the entire phase space. Every replicator — RNA, ant colony, Venice, VOC, Rome, USA, PRC, Ethereum, Polkadot, AI variants — occupies a point (X, Y) with a probability cloud (from stochastic v2 ensembles) and a Row 13 interaction profile. These points cluster into attractors — stable or unstable regions with characteristic dynamics.

We propose an attractor catalog as the "periodic table" of replicators: a finite set of thermodynamic basins defined by X (economic metabolism), Y (governance density), and grid interaction balance.

**Figure 11.1: Phase-Space Attractor Catalog**  
Ensemble clouds (n=50 per replicator, σ=0.07) on the compass plane, colored by Rule-13 proxy (%). Canonical attractors shown as shaded basins. Ethereum, Polkadot, and AI-hegemon variant occupy distinct regions, with drift visible toward exploitationism/rigidity under noise.

The central band — labeled the **Stable Corridor** — is the thermodynamically preferred operating zone for long-persistence replicators. Systems whose ensemble clouds remain anchored here exhibit balanced Mutualism (+/+) dominance in harvest and functional rows combined with calibrated Competition (–/–) in adaptation, boundary maintenance, and suppression rows (6–8, 13–14). Variation bandwidth remains high (C2 >7), rigidity penalty stays low, and Row-13 exploitationism bleed is suppressed below 20–25% baseline. This corridor is the topological expression of the healthy baseline observed in ant colonies, Venice plateau, Bitcoin PoW, and Polkadot/Cosmos fractal designs: the narrow path where entropy export outpaces accumulation without requiring extreme suppression or metabolic overload.

![Figure 11.1: Phase-Space Attractor Catalog](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_11_1_final_clean.png)  
*Note: The (+/–) move is now formally termed **Exploitationism** (systemic extraction); “Parasitism” is retained in legacy figures until updated.*
**Caption:** Ensemble clouds (n=50 per replicator, σ=0.07) on the compass plane, colored by Rule-13 proxy (%). Canonical attractors shown as shaded basins. Ethereum, Polkadot, and AI-hegemon variant occupy distinct regions, with drift visible toward exploitationism/rigidity under noise.

## 11.2 The Ten Canonical Attractors

The compass plane (X: -1.2 to +1.2, Y: -3.0 to +3.0) contains ten recurring attractor types, identified from ensemble runs across scales:

1. **Mutualism Ellipsoid** (high X, low Y)  
   Stable core: balanced mutualism/competition across rows, low exploitationism, high C2 variation.  
   Longevity: centuries+, P(survive 500y) >90%.

2. **Exploitationism Sinkhole** (low X, high Y)  
   Collapse trap: high rigidity (Y↑), Row 13 exploitationism dominance (>50%).  
   Longevity: decades, rapid Gompertz acceleration.

3. **Competition Toroid** (high X, moderate Y)  
   Cyclic high-variance orbits: strong competition suppresses exploitationism but prevents stasis.  
   Longevity: centuries with periodic shocks.

4. **Amensalism Channel** (low X, moderate Y)  
   One-sided drain: amensalism dominates rows, entropy export blocked.  
   Longevity: compression to short centuries.

5. **Neutralism Void** (near-zero X/Y)  
   Stagnation basin: neutral interactions, no entropy gradient.  
   Longevity: indefinite but no growth.

6. **Commensalism Plains** (moderate X, low Y)  
   Passive stability: commensalism across rows, low competition.  
   Longevity: moderate centuries.

7. **Rigid Trap** (moderate X, high negative Y)  
   Suppression overload: high governance density, low variation bandwidth.  
   Longevity: decades under rigidity penalty.

8. **Boundary Saturation** (low X, high negative Y)  
   Frontier exhaustion: boundary maintenance saturates, export fails.  
   Longevity: compression to short centuries.

9. **Chaos Boundary** (extreme X/Y swings)  
   High turbulence: unstable orbits between sinkholes.  
   Longevity: short, unpredictable.

10. **Stable Corridor** (moderate X, low-to-mild Y)  
    Preferred resilience zone: balanced mutualism/competition, high C2, low rigidity.  
    Longevity: centuries+, shock-absorbing.

![Figure 11.2: Row 13 Interaction Profiles by Canonical Attractor](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_11_2_row13_profiles_updated.png)  
*Note: The (+/–) move is now formally termed **Exploitationism** (systemic extraction); “Parasitism” is retained in legacy figures until updated.*
**Caption:** Average move intensities in Row 13 for each attractor. Mutualism/competition balance defines stable cores; exploitationism dominance defines sinkholes.

## 11.3 Merger Dynamics – Graph Complexity

Mergers and modular expansions increase graph complexity, distributing entropy sinks and buffering shocks.

- Nodes = sub-replicators (e.g., relay + parachains)  
- Edges = interaction moves (mutualism, exploitationism, etc.)  
- Complexity = Shannon entropy of edge types + connectivity  

Mergers increase complexity, distributing sinks and buffering shocks.

**Figure 11.3: Four Primary Attractor Wells & Kill-Switch Bifurcation**  
![](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_11_3_four_wells_kill_switch_ridge.png)
*Note: The (+/–) move is now formally termed **Exploitationism** (systemic extraction); “Parasitism” is retained in legacy figures until updated.*
Phase-space map showing the four dominant basins: Stressed Mutualism (green), Hierarchical Cooling (blue), Boundary Saturation (gold), and Exploitationism-dominated Terminal Descent (red). The dashed red line at ε ≈ 1.1 marks the bifurcation threshold where the exploitationism well becomes dominant.

1. **Stressed Mutualism** — high entropy export with moderate suppression cost (broad, shallow basin; resilient under shocks)  
2. **Hierarchical Cooling** — variation bandwidth traded for sharpened Rule-13 suppression (deep, stable well; longevity extended via rigidity)  
3. **Boundary Saturation** — low but positive export floor enabling re-crystallization (narrow ledge; escape possible via external reset)  
4. **Exploitationism-dominated Terminal Descent** — internal friction equals or exceeds harvesting capacity (sinkhole; irreversible cascade)

The entropy-export ratio ε ≈ 1.1 acts as the empirical bifurcation threshold: above ~1.1, trajectories remain trapped in one of the first three wells (net export > internal friction); at or below ~1.1, the exploitationism well becomes dominant — suppression costs consume the entire surplus, triggering irreversible cascade into terminal descent. This threshold emerged from iterating the 15×6 grid across stochastic ensembles (see notebooks/attractor_ensemble.py) and serves as the kill-switch diagnostic used throughout the ledger. Full phase-space topology and vector fields are still in development.

**Figure 11.4: Merger Dynamics – Graph Complexity**  
Network representation of interaction moves before and after merger. Increased complexity (more edges) distributes sinks and buffers shocks.

## 11.4 The Periodic Table of Replicators

The attractor catalog is not exhaustive — new variants may occupy intermediate zones or create hybrid basins. The Appendix (Ch. 12) maps every tested replicator onto this topology, with ensemble clouds and shock trajectories.

The full map is now visible: a finite set of thermodynamic basins, connected by navigable vectors, bounded by rigidity walls and exploitationism sinkholes.
![Figure 11.4: Merger Dynamics – Graph Complexity](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_11_4_merger_dynamics.png)  
**Caption:** Network representation of interaction moves before and after merger. Increased complexity (more edges) distributes sinks and buffers shocks.

## 11.5 Future Horizon: Toward a Phase-Space Topology Scanner

The current compass projects replicators into 2D (X, Y) with ensemble clouds and Row 13 profiles. The natural next layer is a phase-space topology scanner that extrudes these geometries along a third axis — for example, cumulative hazard H(t) from survival fits, or entropy export rate.

In this future view, each replicator would appear as a complex 3D form:  
- Ant colonies: compact, smooth ellipsoids (high symmetry, low entropy loss)  
- Late VOC/PRC: deep, funneling sinkholes (event horizon at ~30% proxy)  
- Competition-dominant systems: braided toroids or chaotic attractors (cyclic high-variance orbits)  
- Merger events: increased surface complexity (fractal-like sub-structures from added nodes/edges)  

Vector fields would trace shock trajectories: arrows from baseline points, length scaled by longevity compression, divergence/curl indicating turbulence or laminar stability. Universal shapes could emerge — high C2 variation always forming helical twists, regardless of scale — letting us compare RNA toroids to Polkadot braids to state lattices.

This is not yet implemented. It requires higher-dimensional ensemble fitting (e.g., PCA or t-SNE reduction to 3D), VTK export from simulate.py, and interactive visualization tools (Paraview, Plotly 3D). But the seeds are already in the repo: ensemble_runner, hazard fits, shock sweeps, and graph complexity stubs.

![Figure 11.6: Complexity Surface – Merger Resilience Illustration](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/fig_11_5_complexity_surface_updated.png)  

**Caption:** Illustrative 3D surface of graph complexity across the compass plane (X, Y). Complexity peaks in hybrid lattice bands (resilience zone) and dips toward exploitationism/rigidity traps. Real replicators plotted as points on the surface.

When built, the scanner would let us ask: which geometries are universally stable? Which forms resist capture? The board would no longer be flat — it would become a full observatory of thermodynamic possibility.

The map is drawn, but never final.

