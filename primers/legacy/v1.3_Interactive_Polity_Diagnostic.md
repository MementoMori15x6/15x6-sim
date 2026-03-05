# Board Scoring Primer v1.3 – Workshop Iteration (Interactive Polity Diagnostic)
**Version note**: This is the v1.3 prompt used during the second LLM scoring workshop rounds (early manuscript scoring phase). Most scores in Chapters 2–8 (Roman cases, crypto protocols, initial hegemon baselines) were generated with this or similar v1.x versions (unconstrained hinge metrics, no CRL anchors, no proxy tuning).  
**Later versions**:  
- v1.6 (clean layout + Exploitationism terminology)  
- v1.7 (Dec 2025 baseline – CRL anchors enforced in simulate.py, proxy tuned to ~64.8% on VOC hinge)  
See repo/primers/ for full history and Chapter 9 for calibration evolution.

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

Now apply the exact same protocol to [REPLICATOR NAME] for [TIME WINDOW].

Base scores on verifiable public sources (cite 1–2 per group, e.g., Pew, Gallup, academic reports, policy trackers). Do not re-score or reference the Bitcoin primer in this evaluation — treat this as an independent case.

Focus on thermodynamic dynamics: replication spread, institutional coupling, cheater suppression signals, dissipation costs, etc.

Output in this structured format (include all items):

1. CSV row of 35 raw scores (0–10 integers, comma-separated, no header).  
2. X,Y coordinates (X = avg 1–17 /10; Y = avg 18–35 /10 × 2.5; 0–1 range).  
3. Zone percentages (low Y → parasitic fringe Zones 1–4, high Y → mutualistic core Zones 8–10).  
4. Dominant interaction per rule row (+/+/–/0 etc.).  
5. Rule-13 parasitism proxy (max(0, 50 - (avg 18–35 /10 * 50))).  
6. Longevity placeholder (100 / (1 + proxy/100) × (1 + mutualism/competition avg from rows 6–8)).  
7. Brief analytical summary (2–3 sentences on key patterns, e.g., entropy buildup risks, Row 13 suppression dynamics, rows 6–8 balance).

No disclaimers, no moral framing — focus on thermodynamic dynamics.
```

You now have your replicator placed on the 15×6 Board with a full diagnostic snapshot.
