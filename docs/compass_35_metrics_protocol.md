# 35-Metric Compass Protocol – Detailed Mapping & Scoring Guidelines

(Current version as of December 2025 manuscript. Open to empirical testing, refinement, and PRs.)

The 35-metric compass converts public evidence into a 2D phase-space position:
- **X**: Economic metabolism (left/collectivist to right/market tilt)
- **Y**: Governance density (libertarian/low-suppression to authoritarian/high-suppression)

**Scoring Range per metric**: -10 to +10  
- Negative values: tilt toward collectivist/authoritarian/left  
- Positive values: tilt toward market/libertarian/right  

Scores derived from public historical/data consensus, averaged via structured LLM prompts (see llm_scoring_workshop.md for template/examples).

## Economic Axis (X) – First 18 metrics (A–G groups)
A1: Property rights strength & enforcement norms  
A2: Market allocation vs. central planning dominance  
A3: Profit motive & incentive alignment  

B1: Redistribution scale & mechanisms  
B2: Welfare universality, conditionality, & dependency  

C1: Heredity fidelity (copying accuracy)  
C2: Heritable variation bandwidth  
C3: Persistence of variants under selection  

D1: Parasitism tolerance / exploitation prevalence  
D2: Competition intensity & zero-sum dynamics  

E1: Individual survival probability until replication  
E2: Niche construction & colonization capability  

F1: Boundary maintenance & identity defense  
F2: Error detection & repair efficiency  

G1: Cheater detection mechanisms  
G2: Modularity & hierarchical sub-unit stability  
G3: Information storage separated from execution  

## Governance Axis (Y) – Last 17 metrics (H–M groups)
H1: Cultural uniformity pressure  
H2: Ideological monopoly strength  
H3: Dissent suppression intensity  

I1: Family autonomy & kinship structures  
I2: Religious freedom & pluralism  
I3: Artistic expression & creative liberty  

J1: Scientific direction & funding independence  
J2: Education system indoctrination level  
J3: Media control & narrative monopoly  

K1: Military priority & resource allocation  
K2: Isolationism vs. openness  
K3: External threat narrative dominance  

L1: Succession mechanism predictability  
L2: Leadership cult / personality centrality  
L3: Purge cycles & elite turnover violence  

M1: Natalism policies & fertility incentives  
M2: Migration control strictness  
M3: Ethnic / identity policy framing  

## Key Calculations & Diagnostics
- **Raw X** = mean(A1–G3 scores) / 10 × 1.2  
- **Raw Y** = mean(H1–M3 scores) / 10 × 2.5  
- **Final point**: (X, Y) in phase space  
- **Splatter %**: Inverse distance to 10 canonical attractor centers, power-law **10, normalized to 100%  
- **Non-linear penalty**: For |score| > 8, quadratic amplification ( (|score| - 8)² × 0.5 ) in sign direction  
- **Entropy export ratio** (life-support monitor): mean mutualism % / mean parasitism % across grid  
  → Well >1.0: net-positive dissipation outward (healthy)  
  → Sustained drift toward or below ~1.0–1.1: potential thermodynamic kill-switch (friction ≥ harvesting)  

All parameters explicit in `simulate.py`. See notebooks/ for ensemble examples, shocks, and CSV outputs.

Mapping to 15×6 Master Grid: Metrics primarily load into specific rows (e.g., G1–G3 → Row 13 cheater detection; full cross-mapping in 15x6_master_grid.md).
## Blank CSV Template for Scoring
Start with this clean blank template (all scores at 0.0, ready for your evidence-based fills):

[Download/View blank template: 35_metrics_blank_template.csv](https://github.com/MementoMori15x6/15x6-sim/blob/main/data/35_metrics_blank_template.csv)

- **Columns**: Metric (A1 etc.), Description (short label), Score (-10 to +10), Rationale (1–2 sentences evidence).
- Fill Scores and Rationales from public sources.
- Average per axis → run through `simulate.py` for X,Y point, splatter %, entropy export ratio, etc.
- For a filled example (USA/PRC comparison), see: [35_metrics_placeholders.csv](https://github.com/MementoMori15x6/15x6-sim/blob/main/data/35_metrics_placeholders.csv)

Future ledger entries and case studies will use this format.

Scores provisional — encourage community stress-testing and PRs for ledger entries.

Memento mori. 🚀
