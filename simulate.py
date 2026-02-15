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

def plot_filled_grid(splatter_percentages, coord, title="Filled 15×6 Grid", output="filled_grid.png"):
    fig = plt.figure(figsize=(12, 9.75), dpi=300)
    ax = fig.add_axes([0.04, 0.09, 0.92, 0.80])
    ax.axis('off')
    
    for i in range(8):
        ax.axvline(i, color='black', linewidth=1.5)
    for i in range(17):
        ax.axhline(i, color='black', linewidth=1.5)
    
    for col, label in enumerate(moves, start=1):
        ax.text(col + 0.5, 0.5, label, ha='center', va='center', fontsize=12.5, fontweight='bold')
    
    for row, rule in enumerate(rules, start=1):
        ax.text(0.1, row + 0.5, rule, ha='left', va='center', fontsize=10.5, linespacing=1.1)
    
    if splatter_percentages[8] > 30:  # Zone 9 index=8
        ax.add_patch(Rectangle((3, 13), 1, 1, facecolor="#E74C3C", alpha=0.92))
        ax.text(3.5, 13.5, f"{splatter_percentages[8]:.0f}%", ha='center', va='center', fontsize=15, color='white')
    
    fig.suptitle(title, fontsize=21, y=0.96)
    
      # Diagnostic text overlay
    ax.text(3.5, 15.5, f"X: {coord[0]:.2f}  Y: {coord[1]:.2f}", 
            ha='center', va='center', fontsize=14, color='blue')
    dom_zone = splatter_percentages.argmax() + 1
    ax.text(3.5, 15.0, f"Dominant: Zone {dom_zone} ({splatter_percentages[dom_zone-1]:.1f}%)", 
            ha='center', va='center', fontsize=12, color='darkgreen')
    
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
