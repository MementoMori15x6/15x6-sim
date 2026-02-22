import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

# ────────────────────────────────────────────────
# 1. CANONICAL LABELS
# ────────────────────────────────────────────────
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

# ────────────────────────────────────────────────
# 2. BASELINE VENICE MATRIX (your locked v1 values)
# ────────────────────────────────────────────────
baseline_matrix = np.array([
    [75.0, 10.0,  5.0, 10.0,  0.0,  0.0],
    [70.0, 15.0,  5.0, 10.0,  0.0,  0.0],
    [65.0, 10.0,  5.0, 20.0,  0.0,  0.0],
    [60.0, 15.0,  5.0, 20.0,  0.0,  0.0],
    [70.0, 10.0,  5.0, 15.0,  0.0,  0.0],
    [75.0, 15.0,  5.0,  5.0,  0.0,  0.0],
    [80.0, 10.0,  5.0,  5.0,  0.0,  0.0],
    [70.0, 15.0,  5.0, 10.0,  0.0,  0.0],
    [65.0, 10.0,  5.0, 20.0,  0.0,  0.0],
    [60.0, 15.0,  5.0, 20.0,  0.0,  0.0],
    [55.0, 10.0,  5.0, 30.0,  0.0,  0.0],
    [50.0, 15.0,  5.0, 30.0,  0.0,  0.0],
    [45.0, 10.0,  5.0, 40.0,  0.0,  0.0],
    [60.0, 15.0,  5.0, 20.0,  0.0,  0.0],
    [70.0, 10.0,  5.0, 15.0,  0.0,  0.0]
])

# ────────────────────────────────────────────────
# 3. SERRATA SHIFT (Pre vs Post)
# Adjustments applied only to targeted metrics (row indices 0-based)
# G1 = Cheater detection (row 12, column 0)
# C1 = Heredity fidelity (row 4, column 0)
# C2 = Variation allowance (row 5, column 0)
# D1 = Parasitism tolerance (row 9, column 0)
# ────────────────────────────────────────────────
pre_serrata = baseline_matrix.copy()

# Pre-Serrata: Higher parasitism tolerance, lower cheater detection, reduced heredity, increased variation
pre_serrata[12, 0] -= 1.5  # G1: Cheater detection down
pre_serrata[4, 0]  -= 2.0  # C1: Heredity fidelity down
pre_serrata[5, 0]  += 2.0  # C2: Variation allowance up
pre_serrata[9, 0]  += 1.0  # D1: Parasitism tolerance up

# Post-Serrata: Baseline (already locked with Serrata effects baked in)
post_serrata = baseline_matrix.copy()

# Create DataFrames
pre_df = pd.DataFrame(pre_serrata, index=rules, columns=moves)
post_df = pd.DataFrame(post_serrata, index=rules, columns=moves)

# ────────────────────────────────────────────────
# 4. STYLING
# ────────────────────────────────────────────────
viridis_base = mpl.colormaps["viridis"]
newcolors = viridis_base(np.linspace(0, 1, 256))
newcolors[0, :] = [1, 1, 1, 1]
custom_map = LinearSegmentedColormap.from_list('WhiteViridis', newcolors)
oxford_red = "#8B0000"

# ────────────────────────────────────────────────
# 5. DUAL-PANE PLOT
# ────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(28, 12), sharey=True)
cbar_ax = fig.add_axes([0.94, 0.15, 0.015, 0.7])

fig.suptitle("Venice Serrata Shift (Pre- vs Post-1297) – RC1 Diagnostic", fontsize=24, fontweight='bold', y=0.98)

for ax, df, title in zip([ax1, ax2], [pre_df, post_df], ["Pre-Serrata (Drift)", "Post-Serrata (Recovery)"]):
    sns.heatmap(df, annot=True, fmt=".1f", cmap=custom_map, vmin=0, vmax=100,
                linewidths=1, linecolor="#eeeeee", cbar_kws={'label': '% Dominance', 'pad': 0.08}, ax=ax,
                cbar_ax=cbar_ax if ax == ax2 else None, cbar=(ax == ax2))

    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')
    ax.set_xticklabels(moves, rotation=45, ha="left", fontsize=10)
    ax.set_yticklabels(rules, rotation=0, fontsize=10)
    ax.tick_params(axis='y', which='major', pad=10)

    ax.set_title(title, fontsize=20, pad=80, fontweight='bold')

    # Rule 13 red border
    ax.add_patch(plt.Rectangle((0, 12), 6, 1, fill=False, edgecolor=oxford_red, lw=4, clip_on=False))

    # Provisional note
    ax.text(0.5, 12.2, ">30 % Parasitism → Potential Collapse Risk",
            fontsize=9, color=oxford_red, ha='left', va='top', fontweight='bold')

plt.subplots_adjust(wspace=0.45, left=0.08, right=0.92, top=0.88, bottom=0.08)
plt.savefig("venice_serrata_shift_v1.png", dpi=300, bbox_inches="tight")
plt.show()

print("Saved: venice_serrata_shift_v1.png")
