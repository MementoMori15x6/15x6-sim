# -*- coding: utf-8 -*-
"""
fig_4x_entropy_export_curves.py

Purpose: Plot entropy export curves across multiple replicators (Chapter 4).

Part of The Board – Political Thermodynamics project
Repo: https://github.com/MementoMori15x6/15x6-sim
Co-authors: Memento & Mori
Last updated: March 2026
"""

import matplotlib.pyplot as plt
import numpy as np

years = np.linspace(0, 1200, 300)

# Rome: jagged descent
rome = 1.9 * np.exp(-years / 400) + 0.3 * np.sin(15 * years / 100) * np.exp(-years / 300)
rome = np.clip(rome, 0.2, 2.0)

# Venice: high plateau with small dips & late slow decline
venice = 1.65 + 0.08 * np.sin(2 * np.pi * years / 200) * np.exp(-years / 3000)
venice[-60:] -= np.linspace(0, 0.4, 60)  # graceful late decline after ~1000y

fig, ax = plt.subplots(figsize=(12, 7))  # slightly taller for annotations

ax.plot(years, rome, 'r--', linewidth=2.5, label='Rome: Conquest Metabolism (Jagged Descent)')
ax.plot(years, venice, 'b-', linewidth=2.5, label='Venice: Institutional Pheromones (High Plateau)')

# Kill-switch threshold
ax.axhline(1.1, color='gray', linestyle='--', alpha=0.7, linewidth=1.2)
ax.text(500, 1.13, 'Kill-Switch Threshold (ε = 1.1)', fontsize=10, color='gray')

# Shaded zones
ax.fill_between(years, 1.1, 2.6, color='green', alpha=0.08, label='Stability Zone')
ax.fill_between(years, 0, 1.09, color='red', alpha=0.08, label='Unstable Zone')

# Zone labels inside areas
ax.text(800, 2.1, 'Stability Zone', fontsize=12, color='darkgreen', ha='center', va='center', alpha=0.9)
ax.text(800, 0.55, 'Unstable Zone', fontsize=12, color='darkred', ha='center', va='center', alpha=0.9)

# Annotations - Rome (darkred/black)
ax.annotate('Conquest highs', xy=(50, 1.95), xytext=(180, 2.25),
            arrowprops=dict(facecolor='darkred', shrink=0.05, width=1.5, headwidth=8))
ax.annotate('Purge cycles', xy=(280, 1.35), xytext=(380, 1.8),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
ax.annotate('Kill-switch plunge', xy=(450, 0.9), xytext=(500, 0.8),
            arrowprops=dict(facecolor='darkred', shrink=0.05, width=1.5, headwidth=8))

# Annotations - Venice (blue)
ax.annotate('Pillar 1–3 onset', xy=(60, 1.45), xytext=(40, 1.1),
            arrowprops=dict(facecolor='blue', shrink=0.05, width=1.5, headwidth=8))
ax.annotate('Auto-correction dips\n(Plague, wars)', xy=(600, 1.58), xytext=(720, 1.85),
            arrowprops=dict(facecolor='blue', shrink=0.05, width=1.5, headwidth=8))
ax.annotate('Atlantic phase shift decline', xy=(1000, 1.42), xytext=(780, 1.2),
            arrowprops=dict(facecolor='blue', shrink=0.05, width=1.5, headwidth=8))

ax.set_xlim(0, 1200)
ax.set_ylim(0, 2.6)
ax.set_xlabel('Persistence Time (years, normalized)', fontsize=12)
ax.set_ylabel('Proxy Entropy-Export Ratio (ε)', fontsize=12)
ax.set_title('Figure 4.x: Comparative Stability States – Institutional Pheromones vs. Conquest Metabolism', fontsize=14, pad=15)

ax.legend(loc='upper right', fontsize=10, framealpha=0.95)
ax.grid(True, alpha=0.25, linestyle='--')

plt.tight_layout()

# Uncomment to save high-res for repo
# plt.savefig('figures/fig_4x_entropy_export_curves.png', dpi=300, bbox_inches='tight')

plt.show()

!python simulate.py
