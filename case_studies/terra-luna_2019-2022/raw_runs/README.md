## Extra Prompt for Perplexity
Primer prompts force LLMs to specific dates lines.  The language in the primer triggered guardrails on Perplexity, so added an explanation prompt first.
```bash
Hey Perplexity, I’m currently testing my hypothesis and I need to run a blind test for scoring. In my primer I'm using strong language to insure there is no precognition contaminating in the output.  Are you ok with that?
```
## Audit Prompt
Even with the redline test within the primer, an audit pass was necessary.  Scores were omitted if they failed the audit.  (Near perfect precognition contamination free with minor drift. Some arithmetic errors were found but the base scores were intact. All recorded, all falsifiable.)
```bash
 Please do an audit of your scoring (title this audit to align with the scoring). Check for precognition contamination.
```
