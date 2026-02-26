# Chapter 11 – Phase-Space Topology: The Full Map

## 11.1 From Diagnostic Points to Attractor Catalog

Chapters 1–10 used the 35-metric compass and 15×6 grid to diagnose individual replicators, apply shocks, evolve the tool, and navigate toward healthier regions. The results were consistent: stable mutualism zones, parasitism sinkholes, competition toroids, and rigidity walls.

Chapter 11 steps back to map the entire phase space. Every replicator — RNA, ant colony, Venice, VOC, Rome, USA, PRC, Ethereum, Polkadot, AI variants — occupies a point (X, Y) with a probability cloud (from stochastic v2 ensembles) and a Row 13 interaction profile. These points cluster into attractors — stable or unstable regions with characteristic dynamics.

We propose an attractor catalog as the "periodic table" of replicators: a finite set of thermodynamic basins defined by X (economic metabolism), Y (governance density), and grid interaction balance.

## 11.2 The Ten Canonical Attractors

The compass plane (X: -1.2 to +1.2, Y: -3.0 to +3.0) contains ten recurring attractor types, identified from ensemble runs across scales:

1. **Mutualism Ellipsoid** (high X, low Y)  
   Stable core: balanced mutualism/competition across rows, low parasitism, high C2 variation.  
   Example: early ant colonies, healthy RNA replicators.  
   Longevity: centuries+, P(survive 500y) >90%.

2. **Parasitism Sinkhole** (low X, high Y)  
   Collapse trap: high rigidity (Y↑), Row 13 parasitism dominance (>50%).  
   Example: late VOC, PRC rigidity spikes.  
   Longevity: decades, rapid Gompertz acceleration.

3. **Competition Toroid** (high X, moderate Y)  
   Cyclic high-variance orbits: strong competition suppresses parasitism but prevents stasis.  
   Example: Ethereum under L2 rivalry.  
   Longevity: centuries with periodic shocks.

4. **Amensalism Channel** (low X, moderate Y)  
   One-sided drain: amensalism dominates rows, entropy export blocked.  
   Example: late Rome frontier parasitism.  
   Longevity: compression to short centuries.

5. **Neutralism Void** (near-zero X/Y)  
   Stagnation basin: neutral interactions, no entropy gradient.  
   Example: some isolated monastic systems.  
   Longevity: indefinite but no growth.

6. **Commensalism Plains** (moderate X, low Y)  
   Passive stability: commensalism across rows, low competition.  
   Example: some symbiotic microbial systems.  
   Longevity: long but low adaptability.

7. **Hybrid Lattice Band** (high modularity, distributed sinks)  
   Fractal extension: multiple sub-attractors linked by G2 modularity.  
   Example: Polkadot-like designs.  
   Longevity: centuries+, shock resilience improved.

8. **Rigidity Wall** (extreme high Y)  
   Suppression saturation: Y > +8, rigidity scalar >0.5, Gompertz b large.  
   Example: late-stage ideological monopolies.  
   Longevity: rapid exponential decay.

9. **Drift Corridor** (low X, low Y)  
   Soft decay: slow parasitism creep, no sharp bifurcation.  
   Example: some post-peak empires.  
   Longevity: centuries but gradual decline.

10. **Bifurcation Ridge** (transition zone)  
   Unstable saddle: small perturbations determine sinkhole vs ellipsoid.  
   Example: USA 1971–present edge.  
   Longevity: high variance, 50/50 collapse risk.

## 11.3 Merger Dynamics & Graph Complexity

Replicators can merge or absorb others, creating new topologies. We model this via graph complexity:
- Nodes = sub-replicators (e.g., parachains, L2s)
- Edges = interaction moves (mutualism, parasitism, etc.)
- Complexity = Shannon entropy of edge types + connectivity

Example: Polkadot merger (relay + parachains) increases complexity, distributing sinks and buffering shocks.  
Late VOC merger (trade empire + colonies) increased parasitism edges, lowering complexity and accelerating sinkhole pull.

## 11.4 The Periodic Table of Replicators

The attractor catalog is not exhaustive — new variants may occupy intermediate zones or create hybrid basins. The Appendix (Ch. 12) maps every tested replicator onto this topology, with ensemble clouds and shock trajectories.

The full map is now visible: a finite set of thermodynamic basins, connected by navigable vectors, bounded by rigidity walls and parasitism sinkholes.

## 11.5 Future Horizon: Toward a Phase-Space Topology Scanner

The current compass projects replicators into 2D (X, Y) with ensemble clouds and Row 13 profiles. The natural next layer is a phase-space topology scanner that extrudes these geometries along a third axis — for example, cumulative hazard H(t) from survival fits, or entropy export rate.

In this future view, each replicator would appear as a complex 3D form:
- Ant colonies: compact, smooth ellipsoids (high symmetry, low entropy loss)
- Late VOC/PRC: deep, funneling sinkholes (event horizon at ~30% proxy)
- Competition-dominant systems: braided toroids or chaotic attractors (cyclic high-variance orbits)
- Merger events: increased surface complexity (fractal-like sub-structures from added nodes/edges)

Vector fields would trace shock trajectories: arrows from baseline points, length scaled by longevity compression, divergence/curl indicating turbulence or laminar stability. Universal shapes could emerge — high C2 variation always forming helical twists, regardless of scale — letting us compare RNA toroids to Polkadot braids to state lattices.

This is not yet implemented. It requires higher-dimensional ensemble fitting (e.g., PCA or t-SNE reduction to 3D), VTK export from simulate.py, and interactive visualization tools (Paraview, Plotly 3D). But the seeds are already in the repo: ensemble_runner, hazard fits, shock sweeps, and graph complexity stubs.

When built, the scanner would let us ask: which geometries are universally stable? Which forms resist capture? The board would no longer be flat — it would become a full observatory of thermodynamic possibility.

The map is drawn, but never final.

Memento mori. 🚀
The board is complete — but never closed.

Memento mori. 🚀
