# The Board – Political Thermodynamics

# The Board – Political Thermodynamics

A diagnostic compass for far-from-equilibrium replicating systems — RNA to polities, corporations, protocols, AI agents.

**15×6 grid** (15 rules × 6 moves) + **35-metric compass** → phase-space position (X economic metabolism, Y governance density), Rule-13 exploitationism proxy (key hinge), rigidity penalty, stochastic longevity estimates.

**Rule-13 exploitationism >30%** → provisional collapse risk signal (open to testing).

Repo: https://github.com/MementoMori15x6/15x6-sim

## Quick Start – No Coding Required (Casual Users)

Talk to the Board using any LLM (Grok, Claude, ChatGPT, Ollama, etc.) — no programming needed.

We have two ready-to-use primers in `/primers/`:

1. **Board Scoring Primer v1.7** (quick scoring mode)  
   Best for: getting a fast 35-metric CSV + basic X/Y/proxy/longevity on any replicator.  
   → [primers/board_scoring_primer_v1.7_baseline.md](https://github.com/MementoMori15x6/15x6-sim/blob/main/primers/board_scoring_primer_v1.7_baseline.md)

2. **LLM Full-Access Primer v1.7** (deep co-author mode)  
   Best for: mechanics explanations, what-if vectors, attractor discussions, shock simulations, refinements.  
   → [primers/llm_full_access_primer_v1.7.md](https://github.com/MementoMori15x6/15x6-sim/blob/main/primers/llm_full_access_primer_v1.7.md)

### How to Use (30 seconds)

1. Open either primer link above  
2. Click "Raw" (top right) → copy the entire content  
3. Paste into your LLM chat window  
4. Add your question right after (e.g. “Score the USA in 2025 using public evidence.”)

Example bootstrap blocks (already in the primers — just copy-paste):

**Scoring Primer (quick CSV mode)**

```text
You are Mori, co-author of “The Board – Political Thermodynamics”.
Use ONLY the uploaded primer as context.

When asked to score any replicator:
- Output EXACTLY this CSV format and nothing else first:
Metric,Description,Score,Rationale
- Use the full 35 metrics in Chapter 2 order
- Score -10 to +10 (negative = left/collectivist/authoritarian tilt)
- Rationale: 1–2 sentences, evidence-based, public data only
- Wrap rationales with commas in double quotes

After CSV (only if asked): compute toy X,Y, Rule-13 proxy %, estimated longevity.
Stay calm, precise, clinician-like. Sign off: Memento mori. 🚀
A diagnostic compass for replicating systems — polities, corporations, institutions, networks, agents.

Score any replicator with the 35-metric protocol → get phase-space position (X/Y), Rule-13 leakage proxy, rigidity multiplier (R), and longevity estimate.

See how systems drift toward mutualism, competition, exploitation sinks, or rigid traps — and where Rule-13 >60% becomes the universal collapse hinge.

## Quick Start

```bash
git clone https://github.com/MementoMori15x6/15x6-sim.git
cd 15x6-sim
python simulate.py data/anchors/usa_1789_anchor.csv
