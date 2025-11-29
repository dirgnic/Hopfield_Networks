# Project Setup and Execution Guide

## Complete Hopfield Networks Project
**Archaeology of Intelligent Machines - 2025**

This guide walks you through setting up and running the entire project.

---

## Step 1: Install Dependencies

```bash
cd hopfield_project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install required packages
pip install -r requirements.txt
```

---

## Step 2: Run Quick Demo

```bash
# Run the demonstration script
python demo.py
```

This will:
- Generate letter patterns (A, B, C)
- Train a Hopfield network
- Test memory retrieval with noise
- Create figures showing the process
- Save results to `figures/` directory

**Expected output files:**
- `figures/demo_patterns.png` - Stored letter patterns
- `figures/demo_similarity.png` - Pattern similarity analysis
- `figures/demo_retrieval.png` - Before/after retrieval visualization
- `figures/demo_energy.png` - Energy minimization trajectory

---

## Step 3: Run Full Experiments

### Experiment 1: Basic Retrieval
```bash
cd experiments
python basic_retrieval.py
```
Tests memory recall with 10%, 20%, and 30% noise levels.

**Generates:**
- `figures/retrieval_noise_10.png`
- `figures/retrieval_noise_20.png`
- `figures/retrieval_noise_30.png`
- `figures/energy_noise_*.png`

### Experiment 2: Capacity Test
```bash
python capacity_test.py
```
Determines maximum number of patterns the network can store reliably.

**Generates:**
- `figures/capacity_experiment.png`

### Experiment 3: Noise Robustness
```bash
python noise_robustness.py
```
Tests how accuracy degrades with increasing noise (0-50%).

**Generates:**
- `figures/noise_robustness.png`

### Experiment 4: Spurious Attractors
```bash
python spurious_attractors.py
```
Searches for "false memories" that emerge when too many patterns are stored.

**Generates:**
- `figures/stored_patterns.png`
- `figures/spurious_attractors.png`
- `figures/pattern_similarity.png`

---

## Step 4: Compile LaTeX Documents

### Mid-Term Project Description
```bash
cd latex_presentation

# Compile project description
pdflatex project_description.tex
pdflatex project_description.tex  # Run twice for references

# Open PDF
open project_description.pdf  # macOS
```

### Beamer Presentation
```bash
# Compile presentation
pdflatex presentation.tex
pdflatex presentation.tex  # Run twice for navigation

# Open PDF
open presentation.pdf  # macOS
```

**Note:** Before compiling the presentation, copy your generated figures from `../figures/` to the LaTeX directory, or update the `\includegraphics` paths in `presentation.tex`.

---

## Step 5: Customize and Extend

### Add Your Own Patterns
Edit `src/patterns.py` to add custom letter templates or load images:

```python
from src.patterns import generate_letters

# Add more letters
patterns = generate_letters(['A', 'B', 'C', 'D', 'E', 'F'], size=10)
```

### Adjust Network Parameters
Modify experiments to test different configurations:

```python
# In any experiment file
hopfield = HopfieldNetwork(n_neurons=100)  # Change size
hopfield.train(patterns)

# Test with different noise levels
noisy = hopfield.add_noise(pattern, noise_level=0.4)  # 40% noise
```

### Create Custom Visualizations
Use the visualization tools in `src/visualization.py`:

```python
from src.visualization import (
    plot_energy_landscape_2d,
    animate_retrieval,
    plot_weight_matrix
)

# Visualize weight matrix
fig = plot_weight_matrix(hopfield.weights)
plt.savefig('my_weights.png')
```

---

## Project Structure Overview

```
hopfield_project/
├── README.md                    # Project overview
├── GUIDE.md                     # This file
├── requirements.txt             # Python dependencies
├── demo.py                      # Quick demonstration
│
├── src/                         # Core implementation
│   ├── __init__.py
│   ├── hopfield.py             # Hopfield network class
│   ├── patterns.py             # Pattern generation utilities
│   └── visualization.py        # Plotting functions
│
├── experiments/                 # All experiments
│   ├── basic_retrieval.py      # Memory recall tests
│   ├── capacity_test.py        # Storage capacity analysis
│   ├── noise_robustness.py     # Noise tolerance evaluation
│   └── spurious_attractors.py  # False memory detection
│
├── figures/                     # Generated plots (created by scripts)
│
├── latex_presentation/          # LaTeX documents
│   ├── presentation.tex        # Beamer slides
│   └── project_description.tex # Mid-term report
│
└── data/                        # (Optional) Custom datasets
```

---

## Understanding the Three-Act Structure

### Act I: From Proteins to Energy Landscapes
**Concept:** Nature solves optimization by energy minimization
- Protein folding analogy
- Energy valleys = stable states
- Transition to neural systems

### Act II: Building from Simple Rules
**Implementation with brain analogies:**
1. **Neurons & Patterns** → Brain states
2. **Hebbian Learning** → Synaptic plasticity
3. **Network Dynamics** → Energy minimization
4. **Memory Retrieval** → Associative recall

### Act III: Experiments & Modern Connections
**Validation and insights:**
- Capacity limits (~0.138N)
- Noise robustness (up to ~30%)
- Spurious attractors (false memories)
- Connection to transformers

---

## Troubleshooting

### Import errors when running experiments
```bash
# Make sure you're in the right directory
cd experiments
python basic_retrieval.py

# Or use absolute imports
cd hopfield_project
python -m experiments.basic_retrieval
```

### Figures not displaying
```bash
# Check if matplotlib backend is set correctly
python -c "import matplotlib; print(matplotlib.get_backend())"

# If using remote SSH, use Agg backend
export MPLBACKEND=Agg
```

### LaTeX compilation errors
- Ensure you have a LaTeX distribution installed (TeX Live, MiKTeX)
- Install missing packages: `tlmgr install <package-name>`
- For Beamer: `tlmgr install beamer`

---

## Expected Results Summary

### Basic Retrieval
- **10% noise:** 100% accuracy
- **20% noise:** 95-100% accuracy
- **30% noise:** 80-90% accuracy
- **Convergence:** 5-15 iterations

### Capacity Test
- **Theoretical:** ~14 patterns (for N=100)
- **Measured:** ~12 patterns at 90% accuracy
- **Beyond capacity:** Rapid degradation

### Noise Robustness
- **Excellent:** 0-25% noise
- **Degrading:** 25-40% noise
- **Failure:** >40% noise

### Spurious Attractors
- **Below capacity:** None or very few
- **At capacity:** Several emerge
- **Above capacity:** Many spurious states

---

## Citation and References

If you use this code for your project, cite:

```bibtex
@misc{hopfield_ami_2025,
  author = {Corobana, Ingrid},
  title = {Hopfield Networks: A Brain-Inspired Model for Associative Memory},
  year = {2025},
  note = {Archaeology of Intelligent Machines, Final Project}
}
```

**Key References:**
1. Hopfield, J. J. (1982). "Neural networks and physical systems..." PNAS
2. "A Brain-Inspired Algorithm For Memory" (YouTube)
3. "Hopfield Networks is All You Need" (Ramsauer et al., 2020)

---

## Next Steps for Your Presentation

1. **Run all experiments** and collect figures
2. **Copy figures** to `latex_presentation/figures/`
3. **Update presentation.tex** with actual figure paths:
   ```latex
   \includegraphics[width=0.8\textwidth]{figures/capacity_experiment.png}
   ```
4. **Compile presentation** and review
5. **Practice** the three-act narrative
6. **Prepare** to discuss brain analogies

---

## Questions?

This project demonstrates:
✓ Classical Hopfield networks from scratch  
✓ Brain-inspired analogies throughout  
✓ Comprehensive experiments with visualizations  
✓ Connection to modern AI (transformers)  
✓ Complete LaTeX presentation and report  

Enjoy exploring how simple rules create complex memory systems! 🧠✨
