# -*- coding: utf-8 -*-
"""
fig_1_1_payoff_matrix_updated.py

Purpose: Render updated 2×2 payoff matrix (mutualism, exploitation, etc.) for Chapter 1.

Part of The Board – Political Thermodynamics project
Repo: https://github.com/MementoMori15x6/15x6-sim
Co-authors: Memento & Mori
Last updated: March 2026
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = [
    ['Mutualism (++)\nstable', 'Commensalism (+0)\nstable', 'Parasitism (+–)\nstable'],
    ['Commensalism (0+) = +0', 'Neutralism (00)\nstable', 'Amensalism (0–)\nstable'],
    ['Parasitism (–+) = +–', 'Competition (––)\nstable', 'Unstable / Impossible']
]

df = pd.DataFrame(data, index=['+', '0', '–'], columns=['+', '0', '–'])
df.index.name = 'Actor A \\ Actor B'
df.columns.name = 'Actor B \\ Actor A'

# Heatmap values: 1 for stable, 0 for unstable
heatmap_data = df.applymap(lambda x: 1 if 'stable' in str(x) else 0)

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(
    heatmap_data,
    annot=df,
    fmt='',
    cmap='RdYlGn',  # Green to red gradient
    cbar=False,
    linewidths=1,
    linecolor='white',
    ax=ax
)
ax.set_title('Figure 1.1 – Exhaustive 3×3 Payoff Matrix\nOnly Six Combinations Are Evolutionarily Stable')
plt.tight_layout()
plt.savefig('figures/fig_1_1_payoff_matrix_updated.png', dpi=300, bbox_inches='tight')
plt.show()
