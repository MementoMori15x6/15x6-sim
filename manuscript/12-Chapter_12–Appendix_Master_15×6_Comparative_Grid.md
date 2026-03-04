# Chapter 12 – Appendix: Master 15×6 Comparative Grid (Living Ledger)
![](https://github.com/MementoMori15x6/15x6-sim/raw/main/figures/banners/banner_ch12_victorian_library.png)
Memento & Mori | December 2025 – ongoing

This is the extensible master ledger: scored replicators with baseline/shock proxies, longevity windows, Row-13 jumps, attractor zone splatter %, and key diagnostics.  
The ledger is living — updated via community PRs, new shocks, refined anchors, and ongoing scoring.

### Scoring & Update Protocol
- Use 35-metric compass → 15×6 grid mapping (simulate.py)
- Report: Rule-13 parasitism %, longevity estimate (Weibull/Gompertz), rigidity penalty, ε-ratio
- Shock: +10–15% delta on D1 parasitism / G1 detection (or custom)
- PR format: replicator name, baseline/post-shock metrics, longevity windows, notes, sources, CSV evidence
- Calibration: Use CRL anchors (Ch 9 / simulate.py) for reproducibility

### Master Ledger Table (Starter – Consensus Rows)

| Replicator                          | Baseline Rule-13 Proxy | Post-Shock Rule-13 Proxy | Baseline Longevity (years) | Post-Shock Longevity (years) | Baseline Row-13 Parasitism % | Post-Shock Row-13 Parasitism % | Attractor Zone / Splatter % | Notes / Calibration | Sources / PR Link |
|-------------------------------------|------------------------|--------------------------|-----------------------------|-------------------------------|------------------------------|--------------------------------|-----------------------------|---------------------|-------------------|
| **Late VOC (1780–1785)**            | 64.8%                 | — (acute collapse baseline) | ~60–160 (central ~1790–1800) | —                            | 62.1% (mean)                | —                              | Parasitism → Chaos Boundary drift | CRL hard-locked hinge (D1=9, G1=-8, F2=-8, E1=2); proxy tuned to 7-run consensus | Ch 5 case study; 7-run consensus CSV |
| Ethereum L1 (2026)                  | 24.0%                 | 50.0%                   | 697 ± 348                  | 458 ± 229                    | 21.1%                       | 71.4%                         | Heavy Competition/Parasitism post-shock | Stake concentration vulnerability | Public blockchain data, EIP governance records |
| Polkadot lattice (2026)             | 25.0%                 | 50.0%                   | 700 ± 350                  | 467 ± 233                    | 33.3%                       | 71.4%                         | Relay-chain vulnerability | Parachain modularity buffer | Polkadot whitepaper, on-chain metrics |
| AI-Hegemon Variant (G1=9.5)         | 19.0%                 | 50.0%                   | 743 ± 371                  | 458 ± 229                    | 18.6%                       | 71.4%                         | Tactical detection gain, structural shock fatal | Simulated from Ethereum base + G1 boost | Simulated delta |

(Add your rows here — PR format: replicator name, baseline/post-shock metrics, longevity windows, notes, sources, CSV evidence)

### Successor Criteria Reminder (from Ch. 08)
- Rule-13 proxy <20% baseline, <30% post-shock  
- C2 variation bandwidth >7 preserved  
- Low rigidity (Y near 0 or mildly positive)  
- ≥3 distributed entropy sinks  
- ε-Ratio <1.0 long-term  
- Longevity ≥500 years ±50%

### How to Add / Update a Row (PR Guide)
1. Score via 35-metric protocol (Ch 2) or simulate.py  
2. Enforce CRL anchors if applicable (Ch 9)  
3. Run baseline + shock(s) → compute proxy, longevity, grid dominance  
4. Export CSV: `data/15x6_[replicator]_[date].csv`  
5. Submit PR: add row to ledger table + CSV link + brief notes/sources  
6. Optional: propose new CRL anchor (centers + bands + evidence)

The ledger is living. Test variants in simulate.py. Submit PRs with new rows, refined columns, or shock scenarios.

Memento mori. 🚀
