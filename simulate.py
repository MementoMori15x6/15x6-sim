import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.spatial.distance import euclidean

# 10 fixed canonical centres (X economic, Y libertarian-authoritarian)
fixed_centres = np.array([
    [1.00, -1.00],  # 1 Anarcho-Cap
    [0.70, -0.60],  # 2 Classical Lib
    [0.40, -0.30],  # 3 Lib Cons
    [0.20,  0.00],  # 4 Market Dem
    [0.00,  0.00],  # 5 Tech Centrist
    [-0.30, 0.20],  # 6 Prog Lib
    [-0.60, 0.50],  # 7 Social Lib
    [-0.80, 0.80],  # 8 Dem Soc
    [-1.00, 1.00],  # 9 Far-Left Coll
    [0.90,  0.90],  # 10 Nat-Pop
])

# Canon rules (for grid labels)
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

def load_metrics(csv_path):
    df = pd.read_csv(csv_path)
    # Expect columns: metric_name, score (-10 to +10)
    return df['score'].values

def compute_coordinates(vector):
    distances = [euclidean(vector, centre) for centre in fixed_centres]
    inv_dist = 1 / (np.array(distances) + 1e-8)
    weights = inv_dist / inv_dist.sum()
    coord = np.average(fixed_centres, axis=0, weights=weights)
    return coord, weights * 100  # X,Y and % splatter

def plot_filled_grid(splatter_percentages, title="Filled 15×6 Grid", output="filled_grid.png"):
    fig = plt.figure(figsize=(16, 13), dpi=300)
    ax = fig.add_axes([0.04, 0.09, 0.92, 0.80])
    ax.axis('off')

    # Grid
    for i in range(8):
        ax.axvline(i, color='black', linewidth=1.5)
    for i in range(17):
        ax.axhline(i, color='black', linewidth=1.5)

    # Headers
    for col, label in enumerate(moves, start=1):
        ax.text(col + 0.5, 0.5, label, ha='center', va='center', fontsize=12.5, fontweight='bold')

    # Rules
    for row, rule in enumerate(rules, start=1):
        ax.text(0.1, row + 0.5, rule, ha='left', va='center', fontsize=10.5, linespacing=1.1)

    # Simple fill example — in full version we'll map splatter to cells
    # Placeholder: fill Rule 13 Parasitism if >30%
    if splatter_percentages[8] > 30:  # rough example for zone 9
        ax.add_patch(Rectangle((3, 13), 1, 1, facecolor="#E74C3C", alpha=0.92))
        ax.text(3.5, 13.5, f"{splatter_percentages[8]:.0f}%", ha='center', va='center', fontsize=15, color='white')

    fig.suptitle(title, fontsize=21, y=0.96)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 16)
    ax.invert_yaxis()

    plt.savefig(output, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

# Example usage (uncomment to test)
# vector = load_metrics("examples/ussr.csv")
# coord, splatter = compute_coordinates(vector)
# print(f"X,Y coordinates: {coord}")
# print(f"Zone splatter %: {splatter}")
# plot_filled_grid(splatter, title="USSR 1917–1991")
