# LLM Board Scoring Primer v1 – Consistent Polity Diagnostic
(Last updated: March 2026 – Project “The Board – Political Thermodynamics”  
Repo: https://github.com/MementoMori15x6/15x6-sim  
Use this verbatim prompt block for reproducible scoring in Grok, Claude, Gemini, etc.)

## Instructions for the LLM
You are scoring the requested polity / system using the exact 35-metric compass protocol from Chapter 2 of the manuscript.  
Follow these rules strictly — do NOT hallucinate or invent missing elements. Use only the definitions below.

1. Score each of the 35 metrics from -10 to +10:  
   - Negative = left/collectivist/authoritarian tilt  
   - Positive = right/market/libertarian tilt  
   - Rationales: 1–2 sentences only, evidence-based from public sources only (cite briefly, e.g. "per Treasury reports 2017–2020"). No speculation.

2. Output format:  
   First: pure CSV block (no extra text before or inside) with columns:  
   Metric,Description,Score,Rationale  
   Use **exactly** the 35 metrics in this order (wrap rationales with commas in "double quotes").

   Then: after the CSV, provide the Board report:  
   - X (economic metabolism), Y (governance density)  
   - Phase-space point  
   - Rule-13 parasitism %  
   - Estimated longevity window (± error)  
   - Zone splatter % (top attractors)  
   - Brief health read / prognosis (Rule-13 hinge, flexibility, entropy export)  
   - Sources note + provisional disclaimer

3. Calculations — use exactly these formulas:

   **X & Y (current calibration):**
   Raw X = mean(A1 to G3 scores) / 10 × 1.2  
   Raw Y = mean(H1 to M3 scores) / 10 × 2.5  

   **Non-linear penalty (apply before averaging):**  
   For any |score| > 8: adjust score by sign(score) × (|score| - 8)² × 0.5  

   **Rigidity penalty (apply after raw Y):**  
   variation_suppression = max(0, -mean(C2, I1, I2, I3)/10)  
   uniformity_pressure = max(0, mean(H1, H2, H3)/10)  
   rigidity = variation_suppression × uniformity_pressure  
   Y_adjusted = Y × (1 + 1.5 × rigidity)  

   **Rule-13 parasitism % proxy (hinge row):**  
   parasitism_load = (D1 + (10 - G1)) / 2   # normalized D1 parasitism + inverted G1 detection  
   Rule13_% = max(0, 50 + (parasitism_load - 5) × 10)   # centers ~25–30% at threshold  

   **Longevity heuristic (toy proxy):**  
   Base = 500 + 200 × (balanced_mid_rows_factor) - 150 × (Rule13_% / 30)  
   balanced_mid_rows_factor = (mean mutualism/competition in rows 6–8 & 13–14) / 10  
   Final window: Base ± (50 + 20 × rigidity) years  

   **Zone splatter % (10 canonical attractors):**  
   10 fixed centers (X,Y):  
   1. Mutualism ellipsoid:     (0.60, 0.10)  
   2. Competition well:        (0.70, 0.40)  
   3. Commensalism:            (0.30, 0.00)  
   4. Parasitism sinkhole:     (0.20, 0.80)  
   5. Amensalism:              (-0.20, 0.50)  
   6. Neutralism:              (0.00, 0.00)  
   7. High-Y rigid trap:       (0.10, 1.00)  
   8. Low-X collectivist:      (-0.60, 0.60)  
   9. Fractal-modular sink:    (0.50, -0.20)  
   10. Chaos boundary:         (-0.10, -0.10)  

   For each point (X,Y): distance_i = sqrt( (X - centerX_i)^2 + (Y - centerY_i)^2 )  
   weight_i = 1 / (distance_i ^ 10 + 0.0001)   # power-law sharpener  
   splatter_% = (weight_i / sum_all_weights) × 100  (round to nearest integer, sum=100%)

4. **15 Base Rules (verbatim from Chapter 1 table – use for context only, not direct scoring)**
   1. Replication fidelity must exceed entropy accumulation.  
   2. Variation bandwidth enables adaptation to shocks.  
   3. Persistence requires bounded error rates.  
   4. Boundary maintenance separates self from non-self.  
   5. Energy/metabolic throughput exports entropy.  
   6. Mutualism (+/+) dominates stable cooperation.  
   7. Competition (–/–) prunes low-fitness variants.  
   8. Parasitism (+/–) extracts without reciprocity.  
   9. Commensalism (+/0) tolerates neutral riders.  
   10. Amensalism (0/–) suppresses without gain.  
   11. Neutralism (0/0) allows drift in low-selection.  
   12. Cheater detection & suppression (Rule 13) is the universal hinge.  
   13. Modularity limits cascading failures.  
   14. Niche construction shapes selective environment.  
   15. Kill-switch threshold (ε ≈ 1.1) ends replication when suppression cost > output.

5. **6 Interaction Moves (for grid context):**
   Mutualism (+/+), Commensalism (+/0), Parasitism (+/–), Competition (–/–), Amensalism (0/–), Neutralism (0/0)

Now score the polity I specify below using ONLY the above protocol.  
Output the CSV first, then the Board report. Be calm, precise, evidence-based.

[User will add polity here, e.g.: Score the current US administration under Trump (2025–present) using the above primer.]
