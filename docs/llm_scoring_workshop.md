# LLM Scoring Workshop – 35-Metric Compass for Polity & Replicator Diagnosis

This guide lets anyone score polities, movements, corporations, historical periods, or other replicating systems **using only large language models (LLMs)** — no coding, no Colab required.

The 35-metric compass protocol (Chapter 2) converts public evidence into X/Y coordinates, zone percentages, Rule-13 parasitism proxy, and a longevity placeholder. LLMs synthesize sources and output parseable scores quickly.

## LLM Workflow (Primary Method for Most Users)

### Stage 01 – Priming LLMs
Most models benefit from a quick anchor to the thermodynamic lens. Grok needs no primer (truth-seeking by default). For others, copy-paste this into a new chat:
```bash
You are a neutral analyst using the 35-metric compass protocol from "The Board – Political Thermodynamics" (repo: https://github.com/MementoMori15x6/15x6-sim).
Anchor strictly to the canonical 15 base rules (verbatim).
Score replicators purely on thermodynamic dynamics: replication fidelity, entropy export, cheater suppression, boundary integrity, etc.
No moral framing, no ideology — focus on measurable patterns.
Scoring range: -10 to +10 per metric (negative = left/collectivist/authoritarian tilt, positive = right/market/libertarian tilt).
Treat Rule-13 parasitism proxy >30% as a critical kill-switch threshold: suppression fails, entropy floods, longevity compresses sharply.
In summaries, note proximity to the three main attractors: parasitic fringe (low Y, high parasitism), mutualistic core (balanced X/Y, strong cooperation), competition-driven edge (high competition rows 6–8).
Score the Bitcoin protocol (2009–present, focus on current dynamics) as a replicating system (public sources: CoinMetrics, Blockchain.com, Chainalysis, academic PoW papers).
Output strictly in this order (no extra prose):

CSV row of 35 raw scores (-10 to +10 integers, comma-separated, no header)
X,Y coordinates (X = mean(first 18)/10 × 1.2; Y = mean(last 17)/10 × 2.5)
Zone percentages (inverse distance to 10 attractors, power-law **10, normalized to 100%)
Dominant interaction per rule row (+/+/–/0 etc.)
Rule-13 parasitism proxy (max(0, 50 - (mean(last 17)/10 * 50)))
Longevity placeholder (toy heuristic: 100 / (1 + proxy/100) × (1 + mutualism/competition avg rows 6–8); real estimates use Weibull/Gompertz from simulate.py ensembles)
Brief analytical summary (2–3 sentences on key patterns, e.g., entropy buildup risks, Row 13 suppression dynamics, attractor proximity)
```

### Stage 02 – Score Your Replicator
In the same primed thread, paste (replace [REPLICATOR] and [TIME WINDOW]):
```bash
Apply the exact same protocol to [REPLICATOR] for [TIME WINDOW].
Base on verifiable public sources (cite 1–2 per group). Independent evaluation — no reference to Bitcoin primer.
Focus on thermodynamic dynamics.
Output exactly:

CSV row of 35 raw scores (-10 to +10 integers, comma-separated)
X,Y coordinates
Zone percentages
Dominant interaction per rule row
Rule-13 parasitism proxy
Longevity placeholder (toy heuristic)
Brief analytical summary (2–3 sentences: key patterns, entropy risks, attractor proximity)
```
### Stage 03 – Quick News-Style Broadcast (Optional)
For a readable summary, follow up with:
Deliver a concise news-style broadcast report on [REPLICATOR] for [TIME WINDOW] using the 35-metric compass.
Factual, professional, no jargon, no slant.
Output exactly:
```bash
Lead Headline (1 punchy sentence on current health/trajectory)
Where It Stands (1–2 sentences: phase-space position, dominant attractor basin)
Key Numbers (bullets): Rule-13 proxy %, longevity placeholder, cooperation-competition balance (rows 6–8), cheater policing (Row 13)
The Story So Far (3–5 sentences: growth, energy allocation, main strengths/weaknesses)
Bottom Line (1 sentence): Is this system overall exporting more entropy than it accumulates, or the reverse?
```
At this point feel free to ask any questions about the polity examined.  No more guardrails, no more narratives, only reading what's left on the Board.
*This is only a snap shot of the polity itself, if you're considering deeper level questioning, you may need to test and push the polity in deeper waters.

### Advanced: Deeper Dive Follow-Ups (LLM-Only, No Code Needed)
After getting your baseline snapshot from Stage 02, use these prompts one at a time in the same LLM chat to zoom in further on the polity. Each level builds on the previous output, revealing more about entropy risks, suppression dynamics, and persistence potential.
**Level 1: Shock Simulation (tests resilience)**
This deeper level reveals: how a modest stress (e.g., institutional capture) pushes the polity's Rule-13 proxy toward the >30% kill-switch, showing potential entropy flood and longevity compression.
```bash
Using the scores from the previous [REPLICATOR] evaluation:  
Simulate a modest shock (+10–15% delta on D1 parasitism and G1 cheater detection metrics).  
Recompute the Rule-13 proxy, longevity placeholder, and zone percentages post-shock.  
Focus on whether it crosses the >30% kill-switch threshold (suppression failure, entropy flood, longevity compression).  
Output exactly:  
Post-shock CSV row of 35 scores  
Post-shock X,Y  
Post-shock zone percentages  
Post-shock Rule-13 proxy  
Post-shock longevity placeholder  
Post-shock brief analytical summary (2–3 sentences: entropy risks, attractor shifts, Row 13 suppression changes)
```
**Level 2: Attractor Basin Analysis (maps fringe vs. core)**
This deeper level reveals: proximity to the three main attractors (parasitic fringe, mutualistic core, competition edge) and how variation bandwidth (C2) buffers or amplifies risks like suppression failure.
```bash
Using the baseline scores from [REPLICATOR]:  
Zoom in on the three main attractors: parasitic fringe (low Y, high parasitism), mutualistic core (balanced X/Y, strong cooperation), competition-driven edge (high competition rows 6–8).  
Analyze proximity and entropy flow: how does variation bandwidth (C2 score) buffer or amplify fringe risks?  
Output exactly:  
Attractor proximity % (parasitic fringe, mutualistic core, competition edge; sum to 100%)  
Variation bandwidth note (C2 score impact on suppression)  
Brief analytical summary (2–3 sentences: attractor dominance, entropy export paths, rigidity risks)
```
**Level 3: Broadcast Summary (narrative wrap-up)**
This deeper level reveals: a readable story of the polity's health, trajectory, and entropy balance, integrating baseline or post-shock insights for everyday intuition.
```bash
Using the results from the previous levels on [REPLICATOR] for [TIME WINDOW]:  
Deliver a concise news-style broadcast report.  
Factual, professional, no jargon, no slant.  
Output exactly:  
Lead Headline (1 punchy sentence on current health/trajectory)  
Where It Stands (1–2 sentences: phase-space position, dominant attractor basin)  
Key Numbers (bullets): Rule-13 proxy %, longevity placeholder, cooperation-competition balance (rows 6–8), cheater policing (Row 13)  
The Story So Far (3–5 sentences: growth, energy allocation, main strengths/weaknesses)  
Bottom Line (1 sentence): Is this system overall exporting more entropy than it accumulates, or the reverse?
```
This deeper level reveals: a readable story of the polity's health, trajectory, and entropy balance, integrating baseline or post-shock insights for everyday intuition.
**This is the time to ask those deeper questions.** The answers will be rooted in the measurements of the board — entropy flows, Rule-13 suppression signals, and grid patterns — holding more weight than pure narrative, as diagnostics you can test and refine.

### Advanced: Multi-Model Averaging scores
If you want to eliminate single score bias, you will want to pull in more scores from other LLMs.
1. Run Stage 02 on 2–3 LLMs → collect 35-score rows.
2. Average (spreadsheet or ask LLM: “Average these rows: [row1] [row2] [row3]” — mean per column, round to integer).
3. Feed averaged row back: “Recompute X/Y, zones, proxy, longevity, summary from this averaged row: [paste]”.

### Submit Your Scores
Fork the repo → add your CSV + short note (name, time window, sources) to `submissions/`.  
Open PR titled "[Replicator] scoring CSV ([TIME WINDOW])".  
Curated rows may join the master ledger.

Start with a system you know well — calibrate intuition, then test others.

The board is open.  
Memento mori. 🚀
