# Chapter 01 – The Board: Rules, Moves, and the Physics of Persistence

> “The game is played whether we understand the rules or not.”  
> —Memento

![Alchemical Entropy Lab Teaser](figures/fig_1_0_alchemical_entropy_lab.png)  
*Harvesting order from chaos: an entropy pump in alchemical form — bottles, books, swirling motifs on a checkerboard floor. The replicator's eternal struggle visualized.*

Every organization—from a strand of RNA to the bureaucracy of a global hegemon—is an entropy pump. It must continuously harvest free energy from its environment to maintain internal order. Where that flow falters, decay begins.

Rises and collapses are still commonly attributed to luck, great leaders, or historical cycles. Yet patterns across scales suggest something more structural: a physics of persistence that precedes ideology. This chapter introduces the Board—a 15×6 master grid—not as a metaphor, but as a navigational framework. It formalizes the constraints that govern durable systems and tests whether those constraints repeat across scales.

The framework has been stress-tested across diverse cases: RNA replicators, ant colonies, the Republic of Venice, the Dutch East India Company (VOC), modern polities, and cryptographic protocols. The signals recur. If persistence obeys common constraints, then diagnosis—and perhaps foresight—may be possible before collapse renders the lesson obvious.

## 1.1 Why Existing Theories Miss the Substrate

Liberalism, Marxism, Realism, and Constructivism understandably begin at the human level. Their units of analysis are actors, classes, institutions, and norms. Biology and physics appear only distantly, if at all. Yet the mechanisms governing replicating systems operate beneath culture and ideology.

These theories often describe symptoms—inequality, revolution, hegemony—but have struggled to consistently predict systemic collapse or engineer durable stability. Few anticipated the implosion of the Soviet Union. Demographic theory underestimated the speed and depth of fertility collapse across parts of East Asia. Contemporary institutional rigidities in parts of the West remain poorly modeled by standard frameworks.

The deeper substrate is replication under thermodynamic constraint. Life—and by extension politics—is an emergent subset of chemical systems that maintain local order by exporting entropy to their environment, consistent with the Second Law of Thermodynamics. Add imperfect replication, heredity, and differential persistence under finite resources, and Darwinian evolution follows inevitably.

Genes, memes, firms, and nations participate in the same underlying dynamic: producing more viable copies tomorrow than their rivals. To persist across time, such systems converge on a constrained set of structural rules. The remainder of this chapter outlines those constraints and examines whether they are derivable from first principles and observable across scales.

## 1.2 The Six Legal Moves: A Grammar of Interaction

If persistence requires replication under constraint, then interactions between replicators must also obey structural limits.

The fifteen rules introduced below define the board. Interactions played upon that board resolve into six evolutionarily stable sign combinations:  
Mutualism (+/+), Commensalism (+/0), Parasitism (+/–), Competition (–/–), Amensalism (0/–), Neutralism (0/0).

Under finite resources and thermodynamic constraint, the space of stable interactions reduces to these six classes. No additional stable sign configuration survives evolutionary filtering.

### Why Only Six?

From evolutionary game theory (Maynard Smith 1982; Nowak 2006), three conditions constrain interactions: payoff asymmetry, thermodynamic limits (no infinite gain without cost), and ESS criteria (no rare mutant invasion).

Enumerating the 3×3 sign combinations (+, 0, –) yields nine logical possibilities. Accounting for symmetry and stability reduces them to six:

- ++ Mutualism: reciprocal gain, stabilized by shared defense mechanisms
- +0 Commensalism: one benefits, the other unaffected, stable under boundary integrity
- +– Parasitism: exploitation persists until countermeasures evolve
- –– Competition: mutual harm under scarcity, driving adaptive escalation
- 0– Amensalism: incidental harm without direct benefit
- 00 Neutralism: non-overlapping niches or negligible interaction

The remaining permutations collapse under relabeling or violate stability. These six align with generalized Lotka–Volterra dynamics: competition, predator–prey, and mutualism variants.

Across scales, the grammar repeats:  
- Molecular: viral parasitism; polymerase cooperation  
- Organismal: mycorrhizal mutualism; canopy competition  
- Institutional: trade mutualism; extractive parasitism; geopolitical competition  

Most complex systems mix moves. Durable constitutions bias toward mutualism and regulated competition while suppressing unchecked parasitism. Where parasitism outpaces detection and suppression, cooperative equilibria degrade toward system-wide competition.

**Figure 1.1 – Exhaustive 3×3 Payoff Matrix**  
Stable cells green; unstable red/strikethrough. (Reproducible code below — run in Colab, commit PNG.)

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

matrix = [
    ['Mutualism (++)\nstable', 'Commensalism (+0)\nstable', 'Parasitism (+–)\nstable'],
    ['Commensalism (0+) = +0', 'Neutralism (00)\nstable', 'Amensalism (0–)\nstable'],
    ['Parasitism (–+) = +–', 'Competition (––)\nstable', 'Unstable / Impossible']
]
df = pd.DataFrame(matrix, index=['+', '0', '–'], columns=['+', '0', '–'])
df.index.name = 'Actor B \\ Actor A'

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df.applymap(lambda x: 1 if 'stable' in str(x) else 0), annot=df, fmt='', cmap='RdYlGn_r', cbar=False, ax=ax, linewidths=1)
ax.set_title('Payoff Matrix: Only Six Stable Equilibria')
plt.tight_layout()
plt.savefig('figures/fig_1_1_payoff_matrix.png')
plt.show()
### 1.3 The Fifteen Universal Rules: Constraints on Persistence

If the six moves define the grammar of interaction, the fifteen rules define the structural constraints under which all entropy-harvesting replicators operate.

These rules are not moral prescriptions. They are physical and evolutionary constraints inferred from thermodynamics, replication theory, and comparative observation. Across tested scales—from prebiotic chemistry to algorithmic governance structures—systems that violate them degrade.

| #  | Rule                                      | One-Sentence Proof                                      | Signal (Observable / Predictive Power) |
|----|-------------------------------------------|---------------------------------------------------------|----------------------------------------|
| 1  | Harvest negative entropy                  | If you don’t, you disassemble                           | Metabolic ceiling and throughput limits (fuel starvation under 2nd Law for open systems) |
| 2  | Replicate with heredity                   | If the pattern is not copied faithfully, replication ceases (proposed as definitional). | Persistence fidelity thresholds (H1) |
| 3  | Allow heritable variation                 | Perfect copying → no evolution → extinction when environment shifts | Adaptive bandwidth (C2) and shock resilience |
| 4  | Differential persistence                  | Some variants must out-replicate others or nothing happens | Selection efficiency (D2 competition) |
| 5  | Individual survival until replication     | Dead carriers don’t copy                                | Baseline durability and friction |
| 6  | Resource acquisition & defense            | You lose if competitors take them first                 | Scarcity vulnerability |
| 7  | Reproductive success (direct or inclusive)| Patterns that don’t get copied disappear                | Demographic and expansion metrics (natalism M1–M3) |
| 8  | Adaptation to change                      | Static strategies lose                                  | Rigidity thresholds |
| 9  | Diversity maintenance                     | Monoculture = single-point failure                      | Diversity sinks and resilience gradients |
| 10 | Niche construction & colonization         | If you don’t take them, someone else will               | Expansion into adjacent possibility space (ε-ratio gains) |
| 11 | Boundary maintenance                      | No membrane/identity → dissipation                      | Identity coherence (F1) |
| 12 | Error detection & repair                  | Unrepaired errors → error catastrophe                   | Decay rates and modular repair capacity |
| 13 | Cheater detection & suppression           | Without immune system, mutualism collapses to parasitism| Parasitic load thresholds and fracture risk (>30% = collapse signal) |
| 14 | Hierarchical / modular organization       | Flat systems cannot scale                               | Governance density vs. scale (Y-axis) |
| 15 | Information storage separated from execution | Somatic suicide is the norm; germline (or constitution) survives | Reset capacity and longevity curves |

These constraints are testable. If a durable system systematically violates them, it should degrade measurably. If counterexamples exist, the framework must adapt. A physics-grounded political theory gains strength precisely because it is falsifiable.

### 1.4 The 15×6 Grid: From Constraints to Instrument

The Board combines the fifteen rules (rows) with the six interaction classes (columns), forming a 90-cell grid that maps entropy dynamics across systems.

Chapter 02 introduces a 35-metric compass used to populate this grid: measuring metabolic throughput (X-axis), governance density (Y-axis), parasitic load (Rule 13 proxy), attractor drift, and projected longevity windows.

The aim is not metaphorical elegance but instrumentation. If rules and moves are real, they should leave measurable traces. Public data in, diagnostics out.

**Figure 1.2 – Blank 15×6 Grid Teaser**  
(From blank_grid.py — run in Colab, commit output PNG to figures/.)

```python
# Example stub for blank grid (expand from repo's blank_grid.py)
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 12))
ax.imshow(np.zeros((15, 6)), cmap='Greys', interpolation='none')
ax.set_xticks(np.arange(6))
ax.set_yticks(np.arange(15))
ax.set_xticklabels(['Mutualism', 'Commensalism', 'Parasitism', 'Competition', 'Amensalism', 'Neutralism'], rotation=45)
ax.set_yticklabels([f'Rule {i+1}' for i in range(15)])
ax.grid(True, color='white', linewidth=0.5)
plt.title('Blank 15×6 Master Grid – Scorecard for Replicators')
plt.tight_layout()
plt.savefig('figures/fig_1_2_blank_grid.png')
plt.show()
### 1.5 The Six and Only Six Legal Moves

Once the fifteen base rules are in place—forming the immutable “board” upon which all replicating systems must play—the next logical question arises: what interactions are possible between two or more such replicators in a shared environment? The answer, derived from first principles of game theory and ecology, is both elegant and exhaustive: there are exactly six possible outcomes, no more and no less. These six “legal moves” correspond to the classic categories of ecological interactions: mutualism (+/+), commensalism (+/0), parasitism (+/–), competition (–/–), amensalism (0/–), and neutralism (0/0). No seventh category is physically or logically possible, as any interaction between entities constrained by finite resources and differential persistence must resolve into one of these payoff matrices.

This classification is not an arbitrary taxonomy but a direct consequence of the board’s core imperatives. Consider two replicators, A and B, each pursuing Rules 1–15 in a zero-sum thermodynamic arena (finite negative entropy). Their interaction cannot be neutral to the board’s logic: A’s actions either enhance, hinder, or ignore B’s replication, and vice versa. The resulting dyad must fit a 2×2 payoff grid where each axis represents net fitness impact (positive: increased replication probability; negative: decreased; zero: negligible effect). Expanding to zero-sum or asymmetric cases yields precisely the six stable equilibria observed across scales—from molecular quorum sensing to interstate alliances.

#### 1.5.1 Formal Proof: Why Only Six?

To derive this exhaustively, begin with the minimal assumptions of replicator dynamics (Maynard Smith, 1982; Nowak, 2006):

1. **Payoff Asymmetry**: Each replicator’s “fitness” (Rule 4: differential persistence) is a scalar function of its strategy and the opponent’s. Let ( f_A(s_A, s_B) ) be A’s fitness under strategies ( s_A ) and ( s_B ). By symmetry, ( f_B(s_A, s_B) = f_B(s_B, s_A) ), but interactions are dyadic.

2. **Thermodynamic Constraint**: Total entropy in the system is conserved locally (Rule 1). Thus, ( f_A + f_B ) in zero-sum niches (e.g., shared resources), but gains can occur via niche construction (Rule 10) if one exports entropy externally.

3. **Stability Requirement**: Equilibria must be evolutionarily stable strategies (ESS): no mutant strategy invades if rare (Hamilton, 1964). Transient states (e.g., temporary symbiosis) resolve into one of the six.

Enumerating all 3^2 = 9 possible sign combinations (+, 0, − for each actor) and discarding unstable or impossible ones:

- ++ (Mutualism): Stable if both benefit (e.g., via reciprocal exchange). Possible under Rule 6 (shared resource defense).
- +0 (Commensalism): Stable if A gains without costing B (e.g., spillover benefits). Rule 11 (boundaries) allows this without leakage.
- +– (Parasitism/Predation): Stable if A exploits B asymmetrically. Rule 13 evolves countermeasures, but the dyad persists until host collapse.
- -- (Competition): Stable zero-sum rivalry (e.g., scramble for Rule 6 resources). Drives Rule 8 adaptation.
- 0– (Amensalism): Stable if B suffers without A gaining (e.g., byproduct harm). Rare but stable under Rule 12 (unrepaired errors).
- 00 (Neutralism): Stable indifference (e.g., non-overlapping niches, Rule 9).

Impossible/Discarded:
- –+: Identical to +– (asymmetry relabeling).
- –0: Unstable—negative payoff without counter drives extinction (violates Rule 4).
- 0+: Identical to +0.

Thus, six stable categories emerge, invariant across scales. This is no coincidence: it mirrors the Lotka-Volterra equations for predator-prey (+/–) or Lotka-Volterra-Leslie for mutualism (++), generalized to zero effects (Roughgarden, 1979).

**Figure 1.5.1 – Exhaustive Payoff Matrix (3×3)**  
Only Six Combinations Are Evolutionarily Stable

| Actor A \ Actor B | +                          | 0                          | –                          |
|-------------------|----------------------------|----------------------------|----------------------------|
| +                 | Mutualism (++)\nstable     | Commensalism (+0)\nstable  | Parasitism (+–)\nstable    |
| 0                 | Commensalism (0+ = +0)     | Neutralism (00)\nstable    | Amensalism (0–)\nstable    |
| –                 | Parasitism (–+ = +–)       | Competition (––)\nstable   | Unstable / Impossible      |

Only six combinations are evolutionarily stable. Impossible/unstable cells struck through in red. Source: Author’s derivation.

#### 1.5.2 Examples Across Scales: From Molecules to Politics

The six moves manifest identically at every level, underscoring the board’s universality:

- **Molecular Scale (Rules 1–4 dominant):** RNA polymerase enzymes exhibit mutualism (++) with DNA templates, catalyzing replication for both. Commensalism (+/0) appears in chaperone proteins aiding folding without cost. Parasitism (+/–) in viral RNA hijacking host ribosomes; competition (–/–) between alleles for polymerase access.

- **Organismal Scale (Rules 5–10):** Mycorrhizal fungi and plants form mutualism (++), trading phosphorus for sugars (Rule 6). Barnacles on whales are commensal (+/0), gaining mobility gratis. Ticks on hosts are parasitic (+/–); lions-zebras, predatory (+/–). Oak-pine canopy wars are competition (–/–); penicillin’s bacterial inhibition, amensalism (0/–).

- **Societal Scale (Rules 11–15):** Trade alliances (EU single market) as mutualism (++). Startups on AWS infrastructure as commensalism (+/0). Crony NGOs siphoning grants as parasitism (+/–). U.S.-China chip wars as competition (–/–). Algorithmic radicalization (unintended echo chambers) as amensalism (0/–). Distant strangers pre-internet as neutralism (0/0).

In politics, these moves are rarely pure; they form dynamic mixtures. The U.S. Constitution engineers a bias toward mutualism/competition (Federalist 51: “ambition counteracting ambition”) while suppressing parasitism via Rule 13. Communism, by centralizing Rule 13, invites elite parasitism (+/–) at scale. The board enforces mixtures: unchecked parasitism cascades to system-wide competition (–/–), eroding mutualism.

The Board is not destiny. It is an attempt at cartography.

If it succeeds, it should clarify where systems drift toward brittleness or resilience. If it fails, it should fail visibly under empirical scrutiny.

The game is played regardless. The question is whether we can learn its geometry in time to navigate it.

### Road Map

- Ch02: The Compass — 35 Metrics for Mapping the Lattice  
- Ch03: Ant Colonies as Upper Bound  
- Ch04–07: Venice, VOC, Crypto Protocols, Hegemons  
- Ch08–09: Algorithmic Hypothesis and Tool Evolution  
- Ch10: From Diagnosis to Prescription  
- Ch11: Topology of Persistence  
- Ch12: Master Grid Appendix  
- Ch13: Rule 13 and Systemic Fracture  

Toward resilient futures.

Memento mori. 🚀
