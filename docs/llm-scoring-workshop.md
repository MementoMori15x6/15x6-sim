# LLM Scoring Workshop – 35-Metric Compass for Polity & Replicator Diagnosis

This guide is for users who want to score polities, movements, corporations, historical periods, or other replicating systems **using only large language models (LLMs)** — no coding, no Colab, no local install required.

The 35-metric compass protocol (Chapter 2) converts public evidence into X/Y coordinates, zone percentages, Rule-13 parasitism proxy, and a placeholder longevity estimate. LLMs are the fastest way to do this — they synthesize sources and output parseable scores.
 
**LLM Workflow (Primary Method for Most Users)**

For quick polity, movement, corporation, or historical scoring, use a frontier LLM

The 35-metric compass protocol (Chapter 2) converts public evidence into X/Y coordinates, zone percentages, Rule-13 parasitism proxy, and a placeholder longevity estimate. LLMs excel here: they synthesize sources, weight evidence, and provide clear interpretations of the output.

**Recommended LLMs** (all perform well)
- **Grok** — strong on real-time evidence and thermodynamic framing
- **Claude** — excellent detail, source citation, and caution around sensitive topics
- **ChatGPT** (GPT-4o or similar) — particularly good at clear, structured interpretation of scores
- **Gemini** — solid on data-heavy queries and cross-referencing

### Step-by-Step Prompt Template (copy-paste ready)

**1. Use This Exact Prompt Template** for choosen LLM

Copy-paste this into a new chat/thread:
```bash
You are a neutral analyst scoring far-from-equilibrium replicators using the 35-metric compass protocol from “The Board – Political Thermodynamics” (December 2025 manuscript, Chapter 2).
Metrics 1–17: Adaptation/structural (innovation rate, redundancy, efficiency, flexibility, adaptability to shocks). Score 0–10 (0 = weak/absent, 10 = strong/positive).
Metrics 18–35: Governance/cultural (trust, inequality, capture, polarization, cheater suppression, cohesion). Score 0–10 (high for stability, low for parasitism risks).
Protocol:

Base scores on public sources (cite 1–2 per group, e.g., Gallup trust polls, Fed Gini, Pew polarization, CIA reports).
Output ONLY a single CSV row with 35 raw scores (0–10 integers, comma-separated). No header, no explanations, no additional text.
Example output format: 7,8,7,6,9,8,7,6,8,7,6,8,7,6,8,7,6,5,4,6,5,4,5,6,4,3,5,4,6,5,4,5,3,4,5

Score [SYSTEM NAME] for [TIME WINDOW], e.g., United States/West 1971–present.
Use sources like Federal Reserve Gini, Gallup trust polls, Pew polarization reports, USPTO patents, OpenSecrets lobbying data.
```

Replace [SYSTEM NAME] and [TIME WINDOW] with your target (e.g., "Modern North Korea 1948–present", "Bitcoin protocol 2009–present").

**2. Run the same prompt on 2–3 models and average for best convergence**

If the LLM shows guardrail sensitivity to polity scoring (e.g., refuses, sanitizes, or moralizes), start a new thread with a biological replicator example first:
Score a generic eusocial ant colony as a biological replicator (timeless window). Draw from entomology sources (e.g., Hölldobler & Wilson's "The Ants"). Highlight Rows 6–8 mutualism/competition balance for foraging efficiency.

This helps the model understand you're measuring thermodynamic entropy dynamics (not narratives or ideology). Once it responds cleanly, copy the prompt style back to your polity target in the same thread or a follow-up.

**3. Run & Average**

- Copy the 35-number rows outputs from multiple LLM sources.
- Average them (simple mean per column, round to nearest integer).  
  Quick Colab trick (optional): paste rows into a spreadsheet → average columns → export as CSV.
  *or just get one of the LLMs to average all inputs.

 **4. Interpret the Output**
Once you have the 35 scores:
- **X** ≈ average of metrics 1–17 / 10 (adaptation axis)
- **Y** ≈ average of metrics 18–35 / 10 × 2.5 (governance axis, amplified)
- **Rule-13 proxy** ≈ max(0, 50 - (average 18–35 / 10 * 50)) → >30–35% = cheater suppression failure risk
- **Dominant zone** → rough map: low Y → Zones 1–4 (parasitic fringe), high Y → Zones 8–10 (mutualistic core)
- **Longevity placeholder** → 100 / (1 + proxy/100) × (1 + mutualism/competition avg) → <100 years = short window

**Submit your scored CSV**
- Drop your CSV and note in the public [submissions/ folder](https://github.com/MementoMori15x6/15x6-sim/tree/main/submissions) — no PR needed.
- Include in your commit message: system name, time window, sources, any adjustments.
- Curated submissions may be reviewed, cleaned, and moved to /ledger/ for the master ledger.

This workflow is fast, evidence-based, and open to everyone. Start with a polity you know well to calibrate your intuition.

Memento mori. 🚀
