# united_states_west_1971-2025.csv – Scoring Metadata

**Time window**: 1971–present (post-Nixon shock, end of gold standard; financialization, inequality rise, institutional drift, sustained tech/market adaptability).

**Input format**: 15×6 grid of row-normalized percentages (0–100 per row, derived from 35-metric compass protocol raw scores).  
**Y-multiplier applied**: 2.5 on governance/cultural metrics (columns 18–35 in raw 35-input, aggregated here).

**Key diagnostic signals**:
- Rows 6–8 (core adaptation/competition): Mutualism + Competition combined ~70–80% → strong health indicator (innovation ecosystems, market flexibility).
- Rule 13 (cheater detection & suppression): Parasitism ~38% (>30% threshold flagged as collapse risk; driven by regulatory capture, lobbying entrenchment, elite networks).
- Zone estimate: ~8–11 (competitive/mutualistic core dominant; parasitic fringe expanding but not yet terminal).
- Longevity heuristic (placeholder): Median 220–450+ years (ongoing system with wide error bars; potential tipping if Rule-13 parasitism crosses 45%).

**Evidence sources / rationale**:
- Economic inequality: Federal Reserve Gini coefficient trends, Piketty/Saez data on top 1% share.
- Institutional trust erosion: Gallup confidence in institutions polls (1970s peak to 2020s lows).
- Polarization & capture: Pew Research polarization reports, studies on revolving-door lobbying.
- Adaptation/innovation: USPTO patent filings, tech sector growth metrics.
- Mapping process: Raw 35-metric scores (0–10 scale) aggregated and normalized per rule to 15×6; open to refinement via LLM averaging or primary source updates.

**Notes for simulation**:
- Run: `python simulate.py examples/united_states_west_1971-2025.csv`
- Compare output zones / Rule-13 proxy to these priors.
- If distortions appear (e.g., over-conservative longevity), consider scoping Y-multiplier or forking to type-specific weights.

PRs welcome for evidence updates or alternative scorings.
