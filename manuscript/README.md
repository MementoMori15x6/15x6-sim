# Manuscript – The Board: Political Thermodynamics

Source Markdown files for the full manuscript (December 2025 draft, ongoing refinements).  
Co-authors: Memento & Mori.  

This directory holds the chapter-by-chapter breakdown in plain Markdown — reproducible, diff-friendly, and ready for conversion to PDF/LaTeX/HTML via pandoc or similar. All figures referenced here are generated via `/notebooks` or `/scripts` in the parent repo (pure matplotlib/seaborn, no external image gen).

## Structure Overview

- **0.1–0.2**: Title page, preface, authorship note  
- **00**: Introduction – Measuring Replicating Systems  
- **01**: Chapter 1 – The Board: Rules, Moves, and the Physics of Persistence  
- **02**: Chapter 2 – From Evidence to Coordinates (35-metric compass protocol)  
- **03**: Chapter 3 – The Superorganism Baseline: Ants as Thermodynamic Ceiling  
- **04**: Chapter 4 – Artificial Pheromones: Venice Engineered Approximation  
- **05**: Chapter 5 – VOC: The Dutch East India Company  
- **06**: Chapter 6 – Bitcoin vs MakerDAO: Millisecond-Lag Replicators  
- **07**: Chapter 7 – The Hegemon Test: USA vs PRC  
- **08**: Chapter 8 – Algorithmic Hegemon Hypothesis  
- **09**: Chapter 9 – Evolution of the Diagnostic Tool  
- **10**: Chapter 10 – Navigation: From Diagnosis to Prescription  
- **11**: Chapter 11 – Phase-Space Topology: The Full Map  
- **12**: Chapter 12 – Appendix: Master 15×6 Comparative Grid (ledger starter)  
- **13**: Chapter 13 – Conclusion: Rule 13 – The Universal Fracture  
- **Appendix_A**: Methods & Reproducibility  

Backup drafts live in `/manuscript/backup` and `/old_drafts`. Tables, figures, data anchors in sibling dirs (`/tables`, `/figures`, `/data`).

## How to Build / Render

Example pandoc one-liner for full draft PDF (from repo root):  
```bash
pandoc manuscript/*.md -o the_board_political_thermodynamics.pdf --toc --number-sections --pdf-engine=xelatex
