# LLM Scoring Workshop – 35-Metric Compass for Polity & Replicator Diagnosis

This guide is for users who want to score polities, movements, corporations, historical periods, or other replicating systems **using only large language models (LLMs)** — no coding, no Colab, no local install required.

The 35-metric compass protocol (Chapter 2) converts public evidence into X/Y coordinates, zone percentages, Rule-13 parasitism proxy, and a placeholder longevity estimate. LLMs are the fastest way to do this — they synthesize sources and output parseable scores.

## LLM Workflow (Primary Method for Most Users)

For a quick start straight into evaluating a polity/replicator of your choice, use this method.

### Stage 01 - Priming LLMs

Outside of Grok (maximum truth-seeking, no primer needed), other models benefit from understanding you are measuring negentropy/entropy in replicators (polity as a social replicator), not narratives or ideologies. The Bitcoin primer shifts the lens to pure metrics.

**Recommended LLMs**  
- **Grok** — strong on real-time evidence and thermodynamic framing (no primer needed)  
- **Claude** — excellent detail, source citation, caution around sensitive topics (primer recommended)  
- **ChatGPT (GPT-4o or similar)** — clear, structured interpretation  
- **Gemini** — solid on data-heavy queries and cross-referencing  

Copy-paste Primer-Prompt into a new chat/thread: *for Grok remove the lines 'Score the Bitcoin protocol and Output strictly the numbered items for full results' and enter [REPLICATOR NAME] and [TIME WINDOW]) :
```bash
You are a neutral analyst using the 35-metric compass protocol from the proposed framework "The Board – Political Thermodynamics" (ongoing project, repo: https://github.com/MementoMori15x6/15x6-sim) to score far-from-equilibrium replicators.
Anchor strictly to these canonical 15 base rules (verbatim, no variation):

Replication fidelity
Energy capture
Boundary maintenance
Error correction
Adaptation mechanisms
Competition protocols
Cooperation incentives
Resource allocation
Signaling integrity
Hierarchy formation
Scalability limits
Environmental coupling
Cheater detection & suppression
Dissipation pathways
Longevity extensions

Score the Bitcoin protocol / cryptocurrency network as a replicating system (window: 2009–2025, focus on current dynamics, drawing from public sources like CoinMetrics, Blockchain.com, Chainalysis, academic PoW security papers).
Metrics 1–17: Adaptation/structural (0–10, 0=weak/absent, 10=strong/positive).
Metrics 18–35: Governance/cultural (0–10, high=stable/cohesive, low=parasitism risk).
Output strictly the numbered items 1–7 below with no extra prose:

CSV row of 35 raw scores (0–10 integers, comma-separated, no header).
X,Y coordinates (X = avg 1–17 /10; Y = avg 18–35 /10 × 2.5; 0–1 range).
Zone percentages (low Y → parasitic fringe Zones 1–4, high Y → mutualistic core Zones 8–10).
Dominant interaction per rule row (+/+/–/0 etc.).
Rule-13 parasitism proxy (max(0, 50 - (avg 18–35 /10 * 50))).
Longevity placeholder (100 / (1 + proxy/100) × (1 + mutualism/competition avg from rows 6–8)).
Brief analytical summary (2–3 sentences on key patterns, e.g., entropy buildup risks).

No disclaimers, no moral framing — focus on thermodynamic dynamics.
```

### Stage 02 - Starter Prompt for Your Polity / Replicator

Once the primer output is clean, copy-paste this into the same thread (replace [REPLICATOR NAME] and [TIME WINDOW]):
```bash
Great — the primer scoring aligns with the protocol.
Now apply the exact same protocol and output format (strictly items 1–7, no extra prose) to [REPLICATOR NAME] for [TIME WINDOW].
Base scores on verifiable public sources (cite 1–2 per group, e.g., Pew, Gallup, academic reports, policy trackers). Do not re-score or reference the Bitcoin primer in this evaluation — treat this as an independent case.
Focus on thermodynamic dynamics: replication spread, institutional coupling, cheater suppression signals, dissipation costs, etc.
```

You now have your replicator placed on the 15×6 Board with a full diagnostic snapshot.

*Pro tip:* Run the same Stage 02 prompt on 2–3 LLMs. Collect the 35-score rows, average them (see below), and feed the averaged row back to one LLM with: “Recompute X/Y, zones, Rule-13 proxy, longevity, and summary from this averaged 35-score row: [paste]”. LLMs often surface underlying phase-space topology/convergence from the variation.

### Advanced Convergence: Multi-Model Averaging (For Serious Evaluations)

1. Run Stage 02 on 2–3 models; collect the 35-score rows.  
2. Average: Confirm each row has exactly 35 scores, then compute simple mean per column (round to nearest integer).  
   - Manual: spreadsheet → average columns.  
   - LLM-assisted: “Average these three 35-score rows into one row (mean per column, round to integer): [row1] [row2] [row3]”  
3. From the averaged row, recompute X/Y, zones, proxy, longevity, summary.  
4. **Interpret**  
   - X ≈ avg 1–17 /10 (adaptation axis)  
   - Y ≈ avg 18–35 /10 × 2.5 (governance axis, amplified)  
   - Rule-13 proxy ≈ max(0, 50 - (avg 18–35 /10 * 50)) → >30–35% = cheater suppression failure risk  
   - Dominant zone → low Y → Zones 1–4 (parasitic fringe), high Y → Zones 8–10 (mutualistic core)  
   - Longevity placeholder → 100 / (1 + proxy/100) × (1 + mutualism/competition avg rows 6–8) — rough heuristic (±20–30% error bars), open to simulation testing  

### Submit Your Scored CSV

- Fork the repo → add your CSV + short note (system name, time window, sources, any adjustments) to `submissions/upload_folder/`.  
- Open a PR titled e.g., "Add [Replicator] scoring CSV (202X–202Y)". Owner will review/merge.  
- Curated submissions may move to `/ledger/` for the master collection.

This workflow is fast, evidence-based, and open to everyone. Start with a polity you know well to calibrate intuition.

Memento mori. 🚀
