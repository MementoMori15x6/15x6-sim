# Monte Carlo Sensitivity Analysis – Terra/Luna Stages (2019–2021)

**Purpose**: Test Fracture Meter robustness under realistic scoring noise (Gaussian, σ=1.0 on main hinges, σ=0.5 on secondary, σ=0.3 on others).  
**Iterations**: 5,000 per stage  
**Collapse flag**: >45% = collapse-prone under uncertainty  
**Notebook**: notebooks/terra-luna_mc_sensitivity.ipynb

## Summary Table

| Stage                        | Mean Fracture Meter | 95% CI         | % >45% | % >50% | Collapse Prob (>45%) |
|------------------------------|----------------------|----------------|--------|--------|----------------------|
| Stage 1 (2019 Genesis)       | 39.8%               | 34.0–45.5%     | 3.8%   | 0.0%   | 3.8%                 |
| Stage 2 (2020 Anchor Launch) | 37.3%               | 31.3–43.1%     | 0.4%   | 0.0%   | 0.4%                 |
| Stage 3 (2021 Parabolic)     | 51.2%               | 45.5–56.9%     | 98.3%  | 66.3%  | 98.3%                |
| Stage 3 + Combined Shock     | 55.1%               | 49.5–60.6%     | 100.0% | 96.1%  | 100.0%               |

**Key Insight**: Only Stage 3 consistently crosses the fracture threshold under noise. Earlier stages remain robust. The combined shock (+1 D1, -1 G1) pushes Stage 3 to 100% collapse probability — showing zero margin for error.

See notebooks/ for full code and raw outputs.
