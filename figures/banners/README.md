# Banners – Repo & Manuscript Visual Assets

This subfolder contains banner-style graphics used across the repo, READMEs, manuscript headers, or promotional visuals for “The Board: Political Thermodynamics”.

## Contents
- High-level headers (e.g., repo banner, chapter section images)
- Possible formats: PNG (high-res for GitHub), SVG (scalable where available)
- Naming: `banner_{purpose}_{variant}.png` or similar (e.g., `banner_repo_header_v1.png`, `banner_chapter_01_physics.png`)

## Generation Guidelines
- All original banners should be created via reproducible Python code (matplotlib/seaborn/matplotlib-text + layout) in a dedicated notebook under `/notebooks` (e.g., `make_banners.ipynb` if we add one).
- No Grok built-in image generation or external editors for project assets — keep everything code-based and committable.
- DPI ≥ 300 for crisp GitHub rendering; aim for 16:9 or 4:3 aspect ratios depending on use.
- If a banner includes text overlays (title, subtitle, Rule 13 motif), embed fonts or use sans-serif defaults for portability.

## Usage Examples
- Repo README.md: top banner
- Manuscript chapter Markdowns: section headers
- GitHub previews, social shares, or PDF cover art

All assets provisional — open to style refinements, new variants, or PRs with code to regenerate them consistently.

These banners are the visual face of the project: simple, thermodynamic-inspired, focused on the grid/compass motif.

Memento mori. 🚀
