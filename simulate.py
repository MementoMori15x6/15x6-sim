import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.spatial.distance import euclidean

fixed_centres = np.array([
    [1.00, -1.00], [0.70, -0.60], [0.40, -0.30], [0.20, 0.00], [0.00, 0.00],
    [-0.30, 0.20], [-0.60, 0.50], [-0.80, 0.80], [-1.00, 1.00], [0.90, 0.90]
])

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
    if 'score' in df.columns:
        return df['score'].values.astype(float)
    else:
        # Fallback for bare metric,score or descriptive
        return df.iloc[:, -1].values.astype(float)  # last column = scores

def compute_coordinates(vector, y_multiplier=3.0, x_extra_weight=1.2):
    if len(vector) != 35:
        raise ValueError("Expected exactly 35 metric scores")
    
    # Non-linear penalty for extreme scores (>|8|)
    extreme = np.abs(vector) > 8
    penalty = extreme * (np.abs(vector) - 8) ** 2 * 0.5
    adjusted = vector + np.sign(vector) * penalty
    
    # Split: first 18 economic/replication → X, last 17 governance/cultural → Y
    x_raw = np.mean(adjusted[:18])
    y_raw = np.mean(adjusted[18:])
    
    X = (x_raw / 10) * x_extra_weight
    Y = (y_raw / 10) * y_multiplier
    
    point_2d = np.array([X, Y])
    
    # Splatter: inverse distance^10 → sharp concentration
    distances = np.array([euclidean(point_2d, centre) for centre in fixed_centres])
    distances = np.maximum(distances, 1e-8)
    inv_dist = 1 / (distances ** 10)
    weights = inv_dist / inv_dist.sum()
    splatter_percent = weights * 100
    
    # Debug prints (comment out when no longer needed)
    print(f"Raw X mean (first 18): {x_raw:.3f} → scaled X: {X:.3f}")
    print(f"Raw Y mean (last 17): {y_raw:.3f} → scaled Y: {Y:.3f}")
    
    return (X, Y), splatter_percent

def plot_filled_grid(splatter_percentages, title="Filled 15×6 Master Grid", output="filled_grid.png"):
    fig = plt.figure(figsize=(16, 13), dpi=300)
    ax = fig.add_axes([0.04, 0.09, 0.92, 0.80])
    ax.axis('off')

    # Grid lines
    for i in range(8):
        ax.axvline(i, color='black', linewidth=1.5)
    for i in range(17):
        ax.axhline(i, color='black', linewidth=1.5)

    # Move headers
    for col, label in enumerate(moves, start=1):
        ax.text(col + 0.5, 0.5, label, ha='center', va='center', fontsize=12.5, fontweight='bold', linespacing=1.2)

    # Rule labels
    for row, rule in enumerate(rules, start=1):
        ax.text(0.1, row + 0.5, rule, ha='left', va='center', fontsize=10.5, linespacing=1.1)

    # Fill cells based on dominant move (simplified from scores)
    # For ants: heavy Mutualism in rows 1-7, 11-15; Competition in row 9
    for row in range(1, 16):
        # Example: map high scores to Mutualism (green)
        # This is placeholder — in full version we'd calculate from vector
        if row in [1,2,3,4,5,6,7,10,11,12,13,14,15]:
            ax.add_patch(Rectangle((1, row), 1, 1, facecolor="#2ECC71", alpha=0.85))  # green Mutualism
            ax.text(1.5, row + 0.5, "80–95%", ha='center', va='center', fontsize=12, color='white')
        elif row == 9:
            ax.add_patch(Rectangle((4, row), 1, 1, facecolor="#F39C12", alpha=0.85))  # orange Competition
            ax.text(4.5, row + 0.5, "60%", ha='center', va='center', fontsize=12, color='white')
        else:
            ax.add_patch(Rectangle((6, row), 1, 1, facecolor="#95A5A6", alpha=0.85))  # gray Neutralism

    # Title with splatter info
    fig.suptitle(f"{title}\nTop splatter: {splatter_percentages.max():.1f}% in Zone {splatter_percentages.argmax()+1}", fontsize=21, y=0.96)

    ax.set_xlim(0, 7)
    ax.set_ylim(0, 16)
    ax.invert_yaxis()

    plt.savefig(output, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
                
if __name__ == "__main__":
    vector = load_metrics("examples/eusocial_ant_colony.csv")
    coord, splatter = compute_coordinates(vector)
    print(f"Ant Colony X,Y: {coord[0]:.2f}, {coord[1]:.2f}")
    print(f"Top zone splatter: {splatter.max():.1f}% in zone {splatter.argmax()+1}")
    plot_filled_grid(splatter, coord, title="Eusocial Ant Colony")
