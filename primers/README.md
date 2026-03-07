# /primers/ — LLM Prompt Templates for The Board

This folder contains lightweight, reusable system prompt templates for loading the Board framework into LLMs.

All primers are provisional and open to refinement/PRs. Use them as starting points for scoring, analysis, or deep dives.

## Current Primers (v1.7 – March 2026)

1. **board_scoring_primer_v1.7_baseline.md**  
   Lightweight scoring primer — no repo fetches, no heavy context loading.  
   Purpose: Quickly gather 35-metric scores for any entity/replicator/polity using only the prompt and basic knowledge.  
   Ideal for:  
   - Fast manual/LLM scoring sessions  
   - Initial drafts or exploratory placements  
   - When you want minimal overhead and no external dependencies  

   Usage: Paste as system prompt → ask to score a polity (e.g. "Score the Spacing Guild from Dune using the 35-metric protocol").

2. **llm_full_access_primer_v1.7.md**  
   Full-access / deep-context primer — fetches and internalizes Ch 9–11 + repo README.  
   Purpose: Gives the LLM complete, up-to-date access to the diagnostic protocol, CRL anchors, navigation, phase-space topology, and project status.  
   Ideal for:  
   - AI alignment research (testing attractor wells, golden path navigation, +/+ mutualism)  
   - Direct comparative studies of replicating systems  
   - Diagnostic R&D and nuanced mechanics analysis  
   - Deep curiosity / "opening the Board" explorations  

   Usage: Paste as system prompt in a fresh chat. Wait for "Primer verified and loaded" confirmation before asking questions.

## How to Use
- Copy the desired primer text into a new LLM conversation as the system prompt.
- For scoring: Use the lightweight version first (baseline) to get quick 35-metric CSV output.
- For deeper analysis/placement: Switch to full-access version to leverage Ch 9–11 context.
- Check Verify Protocols on loading (on full-access) — models sometimes skip fetches so reload Prompt if Verification fails.

## Naming Convention
- `board_scoring_primer_vX.X_[variant].md` → lightweight scoring templates
- `llm_full_access_primer_vX.X.md` → deep-context / repo-loading templates

Questions? PRs welcome — add variants, test cases, or scoring examples.  
Memento mori. 🚀
