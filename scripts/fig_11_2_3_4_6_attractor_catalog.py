# -*- coding: utf-8 -*-
"""
fig_11_2_3_4_6_attractor_catalog.py

Purpose: Generate attractor catalog variants (figs 11.2, 11.3, 11.4, 11.6) for Chapter 11.

Part of The Board – Political Thermodynamics project
Repo: https://github.com/MementoMori15x6/15x6-sim
Co-authors: Memento & Mori
Last updated: March 2026
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import os

# Non-linear penalty function (from compass protocol)
def apply_penalty(s):
    if abs(s) > 8:
        excess = abs(s) - 8
        return s - np.sign(s) * (excess ** 2 * 0.5)
    return s

plt.switch_backend('agg')
plt.close('all')

# CONFIG
CSV_FILES = [
    "data/35_metrics_ethereum_consensus.csv",
    "data/35_metrics_polkadot_consensus.csv",
    "data/35_metrics_ethereum_aihegemon_variant.csv"
]
REPLICATOR_NAMES = ["Ethereum", "Polkadot", "AI-Hegemon Variant"]
ENSEMBLE_N = 50
NOISE_STD = 0.07

# Attractor zones (rough illustrative boundaries)
ATTRACTORS = [
    {"name": "Mutualism Ellipsoid", "xy": (0.8, 0.5), "width": 0.6, "height": 1.0, "color": "limegreen", "alpha": 0.15},
    {"name": "Parasitism Sinkhole", "xy": (-0.6, 2.5), "width": 0.8, "height": 1.5, "color": "darkred", "alpha": 0.15},
    {"name": "Competition Toroid", "xy": (0.9, 1.8), "width": 0.5, "height": 0.8, "color": "orange", "alpha": 0.15},
    {"name": "Amensalism Channel", "xy": (-0.5, 1.0), "width": 0.7, "height": 1.2, "color": "gray", "alpha": 0.15},
    {"name": "Neutralism Void", "xy": (0.0, 0.0), "width": 0.4, "height": 0.6, "color": "lightgray", "alpha": 0.15},
    {"name": "Commensalism Plains", "xy": (0.4, 0.3), "width": 0.8, "height": 0.8, "color": "lightgreen", "alpha": 0.15},
    {"name": "Hybrid Lattice Band", "xy": (0.7, 1.2), "width": 1.0, "height": 0.8, "color": "cyan", "alpha": 0.15},
    {"name": "Rigidity Wall", "xy": (0.2, 2.8), "width": 0.4, "height": 0.6, "color": "purple", "alpha": 0.15},
    {"name": "Drift Corridor", "xy": (-0.3, -0.5), "width": 0.6, "height": 1.0, "color": "lightblue", "alpha": 0.15},
    {"name": "Bifurcation Ridge", "xy": (0.0, 1.5), "width": 0.5, "height": 0.8, "color": "yellow", "alpha": 0.15},
]

def rule13_proxy(s):
    g1 = s['G1']
    d1 = s['D1']
    return max(0, min(50, 50 - (g1 * 2 + (10 - abs(d1)) * 1.5)))

# Load & Generate Ensembles
all_points = []
all_proxies = []
all_labels = []

for csv_path, name in zip(CSV_FILES, REPLICATOR_NAMES):
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found")
        continue

    df = pd.read_csv(csv_path)
    scores = dict(zip(df['Metric'], df['Score']))

    # Base (penalized) X/Y
    x_metrics = [scores[m] for m in df['Metric'][:18]]
    y_metrics = [scores[m] for m in df['Metric'][18:]]
    base_x = np.mean([apply_penalty(s) for s in x_metrics]) / 10 * 1.2
    base_y = np.mean([apply_penalty(s) for s in y_metrics]) / 10 * 3.0

    # Noisy cloud
    x_cloud = []
    y_cloud = []
    proxy_cloud = []
    for _ in range(ENSEMBLE_N):
        noisy_scores = {m: s + np.random.normal(0, NOISE_STD) for m, s in scores.items()}
        noisy_x = np.mean([apply_penalty(noisy_scores[m]) for m in df['Metric'][:18]]) / 10 * 1.2
        noisy_y = np.mean([apply_penalty(noisy_scores[m]) for m in df['Metric'][18:]]) / 10 * 3.0
        proxy = rule13_proxy(noisy_scores)  # assuming rule13_proxy defined earlier

        x_cloud.append(noisy_x)
        y_cloud.append(noisy_y)
        proxy_cloud.append(proxy)

    all_points.append((x_cloud, y_cloud))
    all_proxies.append(proxy_cloud)
    all_labels.append(name)

# Plot
fig, ax = plt.subplots(figsize=(10, 8))

for (x_c, y_c), proxies, label in zip(all_points, all_proxies, all_labels):
    sc = ax.scatter(x_c, y_c, c=proxies, cmap='viridis', alpha=0.7, s=40, label=label)
    ax.scatter(np.mean(x_c), np.mean(y_c), color='black', marker='*', s=200, edgecolor='white', zorder=10)

ax.set_xlabel('X – Economic Metabolism')
ax.set_ylabel('Y – Governance Density')
ax.set_title('Figure 11.1: Phase-Space Attractor Catalog\nEnsemble Clouds (n=50 per replicator, σ=0.07)')

# Shaded zones
for zone in ATTRACTORS:
    patch = Ellipse(zone['xy'], zone['width'], zone['height'],
                    color=zone['color'], alpha=zone['alpha'], fill=True)
    ax.add_patch(patch)
    ax.text(zone['xy'][0], zone['xy'][1], zone['name'], fontsize=8, ha='center', va='center', color='black', alpha=0.8)

cbar = fig.colorbar(sc, ax=ax, label='Rule-13 Proxy (%)')
cbar.set_ticks([0, 10, 20, 30, 40, 50])
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(True, alpha=0.3)

# Save
os.makedirs('figures', exist_ok=True)
save_path = 'figures/fig_11_1_attractor_catalog.png'
fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Figure saved to: {save_path}")

plt.show()

!git add figures/fig_11_1_attractor_catalog.png
!git commit -m "Add Figure 11.1: Phase-Space Attractor Catalog for Ch. 11"
!git push origin main

import numpy as np
import matplotlib.pyplot as plt
import os

plt.switch_backend('agg')
plt.close('all')

# Typical Row 13 intensities per attractor (illustrative, 0–10 scale)
# Order: Mut, Comm, Par, Comp, Amen, Neut
profiles = {
    "Mutualism Ellipsoid":      [8.0, 2.0, 2.0, 8.0, 1.0, 1.0],
    "Parasitism Sinkhole":      [1.0, 1.0, 9.0, 2.0, 3.0, 2.0],
    "Competition Toroid":       [6.0, 3.0, 4.0, 9.0, 2.0, 1.0],
    "Amensalism Channel":       [2.0, 1.0, 7.0, 3.0, 8.0, 2.0],
    "Neutralism Void":          [1.0, 1.0, 1.0, 1.0, 1.0, 9.0],
    "Commensalism Plains":      [4.0, 8.0, 2.0, 3.0, 1.0, 2.0],
    "Hybrid Lattice Band":      [7.0, 4.0, 3.0, 7.0, 2.0, 3.0],
    "Rigidity Wall":            [3.0, 2.0, 5.0, 2.0, 4.0, 4.0],
    "Drift Corridor":           [2.0, 3.0, 6.0, 3.0, 3.0, 5.0],
    "Bifurcation Ridge":        [5.0, 4.0, 5.0, 5.0, 3.0, 3.0],
}

moves = ['Mut', 'Comm', 'Par', 'Comp', 'Amen', 'Neut']
fig, axes = plt.subplots(2, 5, figsize=(14, 6), sharey=True)
axes = axes.flatten()

for i, (name, values) in enumerate(profiles.items()):
    ax = axes[i]
    ax.bar(moves, values, color='skyblue')
    ax.set_title(name, fontsize=9)
    ax.set_ylim(0, 10)
    ax.tick_params(axis='x', rotation=45, labelsize=8)
    ax.tick_params(axis='y', labelsize=8)

fig.suptitle('Figure 11.2: Row 13 Interaction Profiles by Canonical Attractor')
fig.tight_layout(rect=[0, 0, 1, 0.96])

save_path = 'figures/fig_11_2_row13_profiles.png'
os.makedirs('figures', exist_ok=True)
fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Figure saved to: {save_path}")

plt.show()

import networkx as nx
import matplotlib.pyplot as plt
import os

plt.switch_backend('agg')
plt.close('all')

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Before merger: simple chain
G_before = nx.Graph()
G_before.add_edges_from([('Relay', 'Chain1'), ('Relay', 'Chain2')])
pos_before = nx.spring_layout(G_before)
nx.draw(G_before, pos_before, ax=axes[0], with_labels=True, node_color='lightblue',
        edge_color='gray', node_size=800, font_size=10)
axes[0].set_title('Before Merger')

# After merger: lattice with mutualism (green) and some parasitism (red)
G_after = nx.Graph()
G_after.add_edges_from([
    ('Relay', 'Para1'), ('Relay', 'Para2'), ('Relay', 'Para3'),
    ('Para1', 'Para2'), ('Para2', 'Para3')
])
edge_colors = ['green'] * 5  # all mutualism for simplicity
pos_after = nx.spring_layout(G_after)
nx.draw(G_after, pos_after, ax=axes[1], with_labels=True, node_color='lightblue',
        edge_color=edge_colors, node_size=800, font_size=10)
axes[1].set_title('After Merger (Lattice)')

fig.suptitle('Figure 11.3: Merger Dynamics – Graph Complexity')
fig.tight_layout()

save_path = 'figures/fig_11_3_merger_dynamics.png'
os.makedirs('figures', exist_ok=True)
fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Figure saved to: {save_path}")

plt.show()

!git add figures/fig_11_2_row13_profiles.png figures/fig_11_3_merger_dynamics.png
!git commit -m "Add Ch. 11 figures: Row 13 profiles and merger dynamics network"
!git push origin main

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

plt.switch_backend('agg')
plt.close('all')

# Dummy complexity values for our three replicators (higher = more distributed sinks)
# Based on G2 modularity + interaction diversity (illustrative)
replicators = {
    "Ethereum":         {"x": 0.80, "y": 1.63, "z": 6.5, "proxy": 24.0},
    "Polkadot":         {"x": 0.84, "y": 2.14, "z": 8.5, "proxy": 25.0},
    "AI-Hegemon Var":   {"x": 0.76, "y": 1.63, "z": 7.5, "proxy": 19.0},
}

# Grid for surface (illustrative complexity landscape)
x = np.linspace(-1.2, 1.2, 50)
y = np.linspace(-3.0, 3.0, 50)
X, Y = np.meshgrid(x, y)

# Dummy surface: complexity peaks in hybrid lattice band, dips in sinkholes
Z = 5 + 4 * np.exp(-((X - 0.7)**2 + (Y - 1.2)**2) / 0.5)  # peak around lattice
Z -= 3 * np.exp(-((X + 0.6)**2 + (Y - 2.5)**2) / 0.8)     # dip in parasitism sinkhole
Z -= 2 * np.exp(-((X - 0.2)**2 + (Y - 2.8)**2) / 0.4)     # dip in rigidity wall

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')

# Replicator points
for name, data in replicators.items():
    ax.scatter(data['x'], data['y'], data['z'], color='red', s=100, label=name,
               edgecolor='black', zorder=10)
    ax.text(data['x'], data['y'], data['z'] + 0.5, name, fontsize=9)

ax.set_xlabel('X – Economic Metabolism')
ax.set_ylabel('Y – Governance Density')
#ax.set_zlabel('Graph Complexity (illustrative)')
ax.set_title('Figure 11.5: Complexity Surface – Merger Resilience Illustration')
fig.colorbar(surf, ax=ax, label='Complexity Index')

ax.legend()
ax.view_init(elev=25, azim=135)  # nice angle

save_path = 'figures/fig_11_5_complexity_surface.png'
os.makedirs('figures', exist_ok=True)
fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Figure saved to: {save_path}")

plt.show()

!git add figures/fig_11_5_complexity_surface.png
!git commit -m "Add Figure 11.5: Complexity Surface for Ch. 11 (illustrative merger resilience)"
!git push origin main
