# Hopfield Networks: A Brain-Inspired Memory Model
## Archaeology of Intelligent Machines - Final Project

### Overview
This project explores Hopfield Networks through the lens of biological and physical analogies, presenting them as artificial "energy landscapes" where memories are stable valleys, mirroring protein folding dynamics and brain attractor states.

### Project Structure
```
hopfield_project/
├── src/
│   ├── hopfield.py          # Core Hopfield network implementation
│   ├── patterns.py          # Pattern generation utilities
│   └── visualization.py     # Plotting and animation tools
├── experiments/
│   ├── basic_retrieval.py   # Simple memory recall experiments
│   ├── capacity_test.py     # Network capacity analysis
│   └── noise_robustness.py  # Noise tolerance evaluation
├── data/
│   └── patterns/            # Stored pattern examples
├── figures/                 # Generated plots and animations
├── latex_presentation/      # LaTeX beamer presentation
└── notebooks/               # Jupyter notebooks for exploration

```

### Three-Act Narrative Structure

#### Act I: From Proteins to Energy Landscapes
- **Analogy**: Protein folding in energy landscapes
- **Connection**: How nature solves optimization problems
- **Bridge**: From molecules to neural networks

#### Act II: Building Intelligence from Simple Rules
- **Step 1**: Neurons and patterns (brain states)
- **Step 2**: Hebbian learning (synaptic plasticity)
- **Step 3**: Network dynamics (energy minimization)
- **Step 4**: Memory retrieval (associative recall)

#### Act III: Experiments and Modern Connections
- **Experiments**: Capacity, noise robustness, spurious attractors
- **Metrics**: Retrieval accuracy, Hamming distances
- **Modern angle**: Connection to transformers and attention

### Installation

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install numpy matplotlib scipy scikit-learn pillow
```

### Quick Start

```python
from src.hopfield import HopfieldNetwork
from src.patterns import generate_letters

# Generate patterns (e.g., letter "A" and "B")
patterns = generate_letters(['A', 'B'], size=10)

# Create and train network
hopfield = HopfieldNetwork(n_neurons=100)
hopfield.train(patterns)

# Add noise and retrieve
noisy = hopfield.add_noise(patterns[0], noise_level=0.2)
retrieved = hopfield.retrieve(noisy, max_iter=20)
```

### Key References

1. **Video**: [A Brain-Inspired Algorithm For Memory](https://www.youtube.com/watch?v=1WPJdAW-sFo)
2. **Video**: [Hopfield Networks Explained](https://www.youtube.com/watch?v=piF6D6CQxUw)
3. **Wikipedia**: [Hopfield Network](https://en.wikipedia.org/wiki/Hopfield_network)
4. **Modern Extensions**: [Hopfield Networks is All You Need](https://www.youtube.com/watch?v=nv6oFDp6rNQ)

### Authors
Ingrid Corobana
Archaeology of Intelligent Machines - 2025
