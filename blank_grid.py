import matplotlib.pyplot as plt

rules = [
    "1. Harvest negative\nentropy",
    "2. Replicate with\nheredity",
    "3. Allow heritable\nvariation",
    "4. Differential\npersistence",
    "5. Individual survival\nuntil replication",
    "6. Resource\nacquisition &\ndefense",
    "7. Reproductive\nsuccess",
    "8. Adaptation to\nchange",
    "9. Diversity\nmaintenance",
    "10. Niche\nconstruction &\ncolonization",
    "11. Boundary\nmaintenance",
    "12. Error detection &\nrepair",
    "13. Cheater\ndetection &\nsuppression",
    "14. Modularity",
    "15. Info storage"
]

moves = [
    "Mutualism\n(+/+)", "Commensalism\n(+/0)", "Parasitism\n(+/–)",
    "Competition\n(–/–)", "Amensalism\n(0/–)", "Neutralism\n(0/0)"
]

fig = plt.figure(figsize=(16, 13), dpi=300)
ax = fig.add_axes([0.04, 0.09, 0.92, 0.80])
ax.axis('off')

# Grid: header + 15 rules
for i in range(8):
    ax.axvline(i, color='black', linewidth=1.5)
for i in range(17):
    ax.axhline(i, color='black', linewidth=1.5)

# Move headers in row 0
for col, label in enumerate(moves, start=1):
    ax.text(col + 0.5, 0.5, label, ha='center', va='center',
            fontsize=12.5, fontweight='bold', linespacing=1.2)

# Rule labels starting at row 1
for row, rule in enumerate(rules, start=1):
    ax.text(0.1, row + 0.5, rule, ha='left', va='center',
            fontsize=10.5, linespacing=1.1)

# Title
fig.suptitle("The Board – 15×6 Master Grid\nUniversal Scorecard for Replicating Systems", fontsize=21, y=0.96)

ax.set_xlim(0, 7)
ax.set_ylim(0, 16)
ax.invert_yaxis()

plt.savefig('blank_master_grid.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
