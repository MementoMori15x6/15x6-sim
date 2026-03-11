# /primers/ — LLM Prompt Templates for The Board

**The Board** is designed to be usable even if you never touch Python or the repo. It functions as a **computational diagnostic instrument** with the use of algorithmic simulation (AI) that explores trajectories across the phase space.

Use your favorite LLM (Grok, Claude, ChatGPT, Gemini, etc.) as the Board’s operator and diagnostic assistant — just copy & paste one of the two primer prompts below into a LLM prompt window to access the Board. Once loaded start asking about your [entity/polity/replicator] in question. e.g.[Political figure -present date /or/ Roman Republic circa 100 BCE /or/ Western honey bee colony-current]

**Quick 30-Second Start**
1. Open one of the primer links above
2. Click "Raw" (top right) → copy the entire text
3. Open your LLM chat window
4. Paste the primer text—wait for load verification
5. Add your question right after (example below)

e.g. "Score the United States in 2025 using public evidence."

**Tips for Best Results**
*Reminder you loaded the Board onto your favourite LLM, it will default to the Board’s diagnostic terms with its findings, but feel free to ask for a more digestible output.

e.g. Explain the findings like you are the weather channel, explicit details on rule 13 output.

* Use the Scoring Primer first if you just want a quick diagnostic or to aggregate concensus scores.
* Switch to Full-Access when you want deeper mechanics or counterfactuals.
* If the LLM asks for clarification, point it back to the primer or repo link.
* Share your sessions / insights in repo issues or on X — we're open to community refinements.
The primers are lightweight starters. For deepest fidelity, upload more chapters from /docs/ later.
No code, no setup — just paste and diagnose.

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
   Purpose: Gives the LLM complete up-to-date access to the diagnostic protocol, Full discussion on [polity/replicator] in question, CRL anchors, navigation, phase-space topology, and project status.  
   Ideal for:  
   - AI alignment research (testing attractor wells, golden path navigation, +/+ mutualism)  
   - Direct comparative studies of replicating systems  
   - Diagnostic R&D and nuanced mechanics analysis  
   - Deep curiosity / "opening the Board" explorations  

   Usage: Paste as system prompt in a fresh chat. Wait for "Primer verified and loaded" confirmation before asking questions.

## Collecting Consensus Scoring
- Copy the desired primer text into a new LLM conversation as the system prompt.
- For scoring: Use the lightweight version first (baseline) to get quick 35-metric CSV output.  Collect 4+ metric score from various LLMs, and aggregate scoring into a concensus.
- For deeper analysis/placement: Switch to full-access version to leverage Ch 9–11 context.
- Check Verify Protocols on loading (on full-access) — models sometimes skip fetches so reload Prompt if Verification fails.

## Naming Convention
- `board_scoring_primer_vX.X_[variant].md` → lightweight scoring templates
- `llm_full_access_primer_vX.X.md` → deep-context / repo-loading templates

Questions? PRs welcome — add variants, test cases, or scoring examples.  
Memento mori. 🚀
