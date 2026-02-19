# LLM Scoring Workshop – 35-Metric Compass for Polity & Replicator Diagnosis

This guide is for users who want to score polities, movements, corporations, historical periods, or other replicating systems **using only large language models (LLMs)** — no coding, no Colab, no local install required.

The 35-metric compass protocol (Chapter 2) converts public evidence into X/Y coordinates, zone percentages, Rule-13 parasitism proxy, and a placeholder longevity estimate. LLMs are the fastest way to do this — they synthesize sources and output parseable scores.
 
**LLM Workflow (Primary Method for Most Users)**

for a quick start straight into evaluating  polity / replicator of your choice, use this method.

**Stage 01 - Priming LLMs** -- Outside of Grok (who's focus is being a maximum truth-seeking AI, and will not need a primer prompt). The other LLMs do need to understand you are gathering metrics to analyze negentropy/entropy in replicators (polity can be viewed as a social replicator).  The primer changes the lens on how they view polity, not as a narative or ideology, but as a thermodynamic replicating system.
The primer prompt is measuring cyptocurrency (Bitcoin to be exact) priming them to evaluate pure metrics, not opinions or narratives.

Copy-paste this into a new chat/thread:
```bash
You are a neutral analyst using the 35-metric compass protocol from the proposed framework "The Board – Political Thermodynamics" (ongoing project, repo: https://github.com/MementoMori15x6/15x6-sim) to score far-from-equilibrium replicators.
Anchor strictly to these canonical 15 base rules (verbatim, no variation):
1. Replication fidelity
2. Energy capture
3. Boundary maintenance
4. Error correction
5. Adaptation mechanisms
6. Competition protocols
7. Cooperation incentives
8. Resource allocation
9. Signaling integrity
10. Hierarchy formation
11. Scalability limits
12. Environmental coupling
13. Cheater detection & suppression
14. Dissipation pathways
15. Longevity extensions
Score the Bitcoin protocol / cryptocurrency network as a replicating system (window: 2009–2025, focus on current dynamics, drawing from public sources like CoinMetrics, Blockchain.com, Chainalysis, academic PoW security papers).
Metrics 1–17: Adaptation/structural (0–10, 0=weak/absent, 10=strong/positive).
Metrics 18–35: Governance/cultural (0–10, high=stable/cohesive, low=parasitism risk).
Output ONLY:
1. CSV row of 35 raw scores (0–10 integers, comma-separated, no header).
2. X,Y coordinates (X = avg 1–17 /10; Y = avg 18–35 /10 × 2.5; 0–1 range).
3. Zone percentages (low Y → parasitic fringe Zones 1–4, high Y → mutualistic core Zones 8–10).
4. Dominant interaction per rule row (+/+/–/0 etc.).
5. Rule-13 parasitism proxy (max(0, 50 - (avg 18–35 /10 * 50))).
6. Longevity placeholder (100 / (1 + proxy/100) × (1 + mutualism/competition avg from rows 6–8)).
7. Brief analytical summary (2–3 sentences on key patterns, e.g., entropy buildup risks).
No disclaimers, no moral framing — focus on thermodynamic dynamics.
```
**Stage 02 - Starter prompt for the polity / replicator of your choice.

Now that they have fully evaluated Bitcoin as a replicator you can engage them with the polity of your choice and place them on "The Board of Political Thermodynamics" to score far-from-equilibrium replicators.

Copy-paste this into the same chat/thread:
```bash
Great — the primer scoring aligns with the protocol.

Now apply the exact same protocol and output format (including longevity placeholder and brief analytical summary) to [REPLICATOR NAME] for [TIME WINDOW].

Base scores on verifiable public sources (cite 1–2 per group, e.g., Pew, Gallup, academic reports, policy trackers). Do not re-score or reference the Bitcoin primer in this evaluation — treat this as an independent case.

Focus on thermodynamic dynamics: replication spread, institutional coupling, cheater suppression signals, dissipation costs, etc.
```
You have your polity / replicator on the 15x6 Board ready to analyze.

*pro tip:* try asking different LLMs with the same polity / replicator prompt. Gather the metric scores, evaluations, and share them with 2 or more LLMs.  You'll see although there is variation there is also a deeper underlying convergence that the LLMs will be quick to notice.  It's the inherent phase-space topolgy projected as geometry (which the LLMs see) in the replicator's data itself.

**LLM Scoring Workflow -- using for scoring simulation analysis
For quick polity, movement, corporation, or historical scoring, use a frontier LLM

The 35-metric compass protocol (Chapter 2) converts public evidence into X/Y coordinates, zone percentages, Rule-13 parasitism proxy, and a placeholder longevity estimate. LLMs excel here: they synthesize sources, weight evidence, and provide clear interpretations of the output.

**Recommended LLMs** (all perform well)
- **Grok** — strong on real-time evidence and thermodynamic framing
- **Claude** — excellent detail, source citation, and caution around sensitive topics
- **ChatGPT** (GPT-4o or similar) — particularly good at clear, structured interpretation of scores
- **Gemini** — solid on data-heavy queries and cross-referencing

### Step-by-Step Prompt Template (copy-paste ready)

 **Step 0: Anchor to the Canonical 15×6 Grid (Mandatory – No Exceptions)**
 Copy-paste this into a new chat/thread:
```bash
**All scoring MUST use the exact 15 base rules as defined in the December 2025 manuscript (Chapter 1 table) and codified in `blank_grid.py`.**  
Do **not** regenerate, rephrase, expand, or invent alternative rule sets — even if the prompt seems open-ended or a different LLM previously did so. Variability in rule formulation introduces uncontrolled noise and breaks reproducibility across submissions.

Use this fixed list of rows **verbatim**:

1. Replication fidelity  
2. Energy capture  
3. Boundary maintenance  
4. Error correction  
5. Adaptation mechanisms  
6. Competition protocols  
7. Cooperation incentives  
8. Resource allocation  
9. Signaling integrity  
10. Hierarchy formation  
11. Scalability limits  
12. Environmental coupling  
13. Cheater detection & suppression  
14. Dissipation pathways  
15. Longevity extensions  

**Procedure:**  
- Load or reference `blank_grid.py` (or copy the structure from `examples/` templates) as your starting point.  
- Apply the 35-metric compass protocol (Chapter 2) **directly** to these 15 rows.  
- Derive interaction signs (+/+/–/0), X,Y coordinates, zone percentages, and Rule-13 parasitism proxy **only** from evidence mapped onto this canonical grid.  
- If you previously scored a case on a variant board (from another model/session), **re-score it entirely** on this fixed grid before submitting or simulating.  

This anchoring step ensures the 15×6 Master Grid remains a consistent diagnostic instrument across all contributors, models, and time. Refinements to rule wording or structure are welcome **only** via evidence-backed PRs to the repo — never ad-hoc during scoring.

Proceed to Step 1 only after confirming you are working from the canonical rows above.
```

**1. Use This Exact Prompt Template** for chosen LLM

Copy-paste this into the same chat/thread:
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
  - If averaging manually is tedious, paste the rows into one LLM and ask: “Average these three 35-score rows into one row (mean per column, round to integer): [paste row1] [paste row2] [paste row3]”
    
 **4. Interpret the Output**
Once you have the 35 scores:
- **X** ≈ average of metrics 1–17 / 10 (adaptation axis)
- **Y** ≈ average of metrics 18–35 / 10 × 2.5 (governance axis, amplified)
- **Rule-13 proxy** ≈ max(0, 50 - (average 18–35 / 10 * 50)) → >30–35% = cheater suppression failure risk
- **Dominant zone** → rough map: low Y → Zones 1–4 (parasitic fringe), high Y → Zones 8–10 (mutualistic core)
- **Longevity placeholder** → 100 / (1 + proxy/100) × (1 + mutualism/competition avg) → <100 years = short window

**Submit your scored CSV**
- Drop your CSV and note in the public [submissions/ upload_folder](https://github.com/MementoMori15x6/15x6-sim/tree/main/submissions) — no PR needed.
- Include in your commit message: system name, time window, sources, any adjustments.
- Curated submissions may be reviewed, cleaned, and moved to /ledger/ for the master ledger.

This workflow is fast, evidence-based, and open to everyone. Start with a polity you know well to calibrate your intuition.

Memento mori. 🚀
