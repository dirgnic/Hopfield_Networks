# Quick Reference Card
## Hopfield Networks Project

###  Quick Start
```bash
cd hopfield_project
chmod +x setup.sh
./setup.sh
```

###  File Structure
```
hopfield_project/
├── src/               # Core implementation
│   ├── hopfield.py   # Main network class
│   ├── patterns.py   # Pattern generation
│   └── visualization.py  # Plotting tools
├── experiments/       # All experiments
├── figures/          # Generated plots
├── latex_presentation/  # Slides & report
└── notebooks/        # Jupyter notebook
```

###  Run Experiments
```bash
# Quick demo
python demo.py

# Full experiments
cd experiments
python basic_retrieval.py      # Memory recall
python capacity_test.py        # Storage limits
python noise_robustness.py     # Noise tolerance
python spurious_attractors.py  # False memories
```

###  Key Results
- **Capacity**: ~14 patterns (0.138 × 100 neurons)
- **Noise tolerance**: Up to 25-30% corruption
- **Convergence**: 5-15 iterations typical
- **Spurious attractors**: Emerge above capacity

###  Brain Analogies Cheat Sheet
| Component | Math | Brain Analogy |
|-----------|------|---------------|
| Neuron state | s_i ∈ {-1,+1} | Firing (+1) or silent (-1) |
| Pattern | ξ = (s₁,...,sₙ) | Brain state snapshot |
| Weights | w_ij | Synaptic connections |
| Learning | w_ij = Σ ξᵢ·ξⱼ | "Fire together, wire together" |
| Energy | E = -½Σw_ij·s_i·s_j | Stability landscape |
| Update | s_i = sign(Σw_ij·s_j) | Neuron listens to inputs |
| Retrieval | Noisy → Original | "Hear notes → recall song" |

###  LaTeX Commands
```bash
cd latex_presentation

# Compile project description
pdflatex project_description.tex
pdflatex project_description.tex

# Compile presentation
pdflatex presentation.tex
pdflatex presentation.tex
```

###  Three-Act Structure
**Act I**: Protein folding → Energy landscapes → Brain dynamics

**Act II**: Implementation with analogies
1. Neurons & patterns → Brain states
2. Hebbian learning → Synaptic plasticity  
3. Dynamics → Energy minimization
4. Retrieval → Associative memory

**Act III**: Experiments → Capacity → Spurious attractors → Transformers

###  Key Equations
**Hebbian learning:**
```
w_ij = (1/N) Σ_μ ξ_i^μ · ξ_j^μ  (i≠j)
```

**Update rule:**
```
s_i^(t+1) = sign(Σ_j w_ij · s_j^(t))
```

**Energy:**
```
E(s) = -½ Σ_ij w_ij · s_i · s_j
```

###  Troubleshooting
```bash
# Can't run experiments?
cd experiments
python basic_retrieval.py

# Import errors?
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# No plots showing?
export MPLBACKEND=TkAgg
```

###  References
1. Hopfield (1982) - PNAS original paper
2. YouTube: "A Brain-Inspired Algorithm For Memory"
3. Ramsauer et al. (2020) - "Hopfield Networks is All You Need"

###  Checklist for Presentation
- [ ] Run all experiments
- [ ] Generate all figures
- [ ] Copy figures to latex_presentation/
- [ ] Update figure paths in presentation.tex
- [ ] Compile LaTeX documents
- [ ] Practice three-act narrative
- [ ] Prepare brain analogy examples
- [ ] Test demo on presentation machine

---
**2024 Nobel Prize in Physics** 
John Hopfield & Geoffrey Hinton
