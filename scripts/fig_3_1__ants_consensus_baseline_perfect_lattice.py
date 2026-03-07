# -*- coding: utf-8 -*-
"""
fig_3_1__ants_consensus_baseline_perfect_lattice.py

Purpose: Baseline heatmap of perfect eusocial ant colony lattice (Chapter 3).

Part of The Board – Political Thermodynamics project
Repo: https://github.com/MementoMori15x6/15x6-sim
Co-authors: Memento & Mori
Last updated: March 2026
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap
from google.colab import files

# Load scores
df = pd.read_csv("examples/eusocial_ant_colony.csv")
scores = df['Score'].astype(float).values

# Your canonical labels
rules = [
    "1. Harvest negative entropy",
    "2. Replicate with heredity",
    "3. Allow heritable variation",
    "4. Differential persistence",
    "5. Individual survival until replication",
    "6. Resource acquisition & defense",
    "7. Reproductive success",
    "8. Adaptation to change",
    "9. Diversity maintenance",
    "10. Niche construction & colonization",
    "11. Boundary maintenance",
    "12. Error detection & repair",
    "13. Cheater detection & suppression (KEY RULE)",
    "14. Hierarchical/modular organization",
    "15. Info storage separated from execution"
]
moves = [
    "Mutualism (+/+)",
    "Commensalism (+/0)",
    "Parasitism (+/–)",
    "Competition (–/–)",
    "Amensalism (0/–)",
    "Neutralism (0/0)"
]

# Refined dominance mapping (max mutualism, min bleed)
dominance = np.zeros((15, 6))
for r in range(15):
    score = scores[r]
    mutual = max(0, score * 8 + 80)  # baseline 80 + score boost
    mutual = min(100, mutual)
    dominance[r, 0] = mutual

    parasit = max(0, -score * 3) if score < -3 else 0
    dominance[r, 2] = min(10, parasit)  # cap bleed low

# Lock Rule-13 suppression
dominance[12, 0] = 98
dominance[12, 2] = 2

# Your style
viridis_base = mpl.colormaps["viridis"]
newcolors = viridis_base(np.linspace(0, 1, 256))
newcolors[0, :] = [0.98, 0.98, 1, 1]
custom_map = LinearSegmentedColormap.from_list('FullSaturation', newcolors)
oxford_red = "#8B0000"

fig, ax = plt.subplots(figsize=(14, 10))
sns.heatmap(dominance, annot=True, fmt=".0f", cmap=custom_map, vmin=0, vmax=100,
            linewidths=0.5, linecolor="#dddddd", cbar_kws={'label': '% Dominance', 'pad': 0.05}, ax=ax,
            xticklabels=moves, yticklabels=rules)

ax.set_title("15×6 Master Grid – Ants Consensus Baseline (Perfect Lattice)", fontsize=18, pad=50, fontweight='bold')
ax.set_ylabel("Base Rules (Dec 2025 Canon)", fontsize=12)
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
plt.xticks(rotation=45, ha="left", fontsize=10)
plt.yticks(rotation=0, fontsize=10)
ax.tick_params(axis='y', which='major', pad=10)

# Red Rule-13 border
ax.add_patch(plt.Rectangle((0, 12), 6, 1, fill=False, edgecolor=oxford_red, lw=5, clip_on=False))

# Critical note
ax.text(0, 15.5, "Critical Rule 13: >30 % Parasitism → Potential Collapse Risk",
        fontsize=10, color=oxford_red, ha='left', va='top', fontweight='bold',
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))

plt.tight_layout()
plt.savefig("tests/outputs/ants_consensus_lattice_v5.png", dpi=300, bbox_inches="tight")
plt.show()

files.download("tests/outputs/ants_consensus_lattice_v5.png")

!python simulate.py
