# Quick Start Guide: Hopfield 1982 Experiment

## Overview

This folder contains a complete reproduction of John Hopfield's 1982 experiment demonstrating associative memory with a discrete binary neural network using a **single stored pattern**.

## What This Demonstrates

The classic Hopfield experiment shows three key capabilities:

1. **Pattern Completion**: Given 25%-75% of a pattern, the network reconstructs 100%
2. **Error Correction**: Noisy inputs (10-30% corruption) are cleaned perfectly  
3. **Energy Minimization**: Network dynamics guarantee convergence to stored memories

## Quick Start

### Run the Experiment

```bash
cd classic_experiment_1982
python hopfield_1982_reproduction.py
```

This will:
- Train a 100-neuron network on letter 'H'
- Test pattern completion from partial input
- Test noise correction
- Visualize energy dynamics
- Generate 6 publication-quality figures

**Runtime**: ~5 seconds

### View Results

All figures are saved in `figures/` directory:

```bash
open figures/summary_hopfield_1982.png     # Comprehensive overview
open figures/exp2_partial_completion.png   # Pattern completion demo
open figures/exp3_noise_correction.png     # Error correction demo
open figures/exp4_energy_dynamics.png      # Energy descent
```

## Expected Results

### Pattern Completion
- **75% visible** → 100% retrieved in 2 iterations ✓
- **50% visible** → 100% retrieved in 2 iterations ✓
- **25% visible** → 100% retrieved in 2 iterations ✓

### Error Correction
- **10% noise** → Perfectly corrected in 2 iterations ✓
- **20% noise** → Perfectly corrected in 2 iterations ✓
- **30% noise** → Perfectly corrected in 2 iterations ✓

### Performance
- Convergence: 1-2 iterations
- Accuracy: 100% in all tests
- Energy: Monotonically decreasing (guaranteed)

## Files

```
classic_experiment_1982/
├── README.md                          # Historical context
├── RESULTS.md                         # Detailed experimental results
├── QUICK_START.md                     # This file
├── hopfield_1982_reproduction.py      # Main experiment script
├── figures/                           # Generated visualizations (6 files)
│   ├── exp1_perfect_storage.png
│   ├── exp2_partial_completion.png
│   ├── exp3_noise_correction.png
│   ├── exp4_energy_dynamics.png
│   ├── exp5_step_by_step.png
│   └── summary_hopfield_1982.png
└── data/                              # (empty, for future use)
```

## The Network

**Architecture**:
- 100 neurons (10×10 grid)
- 9,900 symmetric connections
- Binary states: {-1, +1}

**Learning**:
- Hebbian rule: w_ij = (1/N) × ξ_i × ξ_j
- Single-shot learning (no iterations)

**Dynamics**:
- Asynchronous updates (one neuron at a time)
- Energy always decreases or stays constant
- Guaranteed convergence to local minimum

## Understanding the Results

### What to Look For

1. **Pattern Grid**: Black = +1 (active), White = -1 (inactive)
2. **Energy Values**: More negative = more stable
3. **Convergence**: Network reaches stable state in 1-2 steps
4. **Perfect Retrieval**: Hamming distance = 0 (no errors)

### Key Insights

**Pattern Completion**: 
- Network fills in missing information
- Works like content-addressable memory
- "Hear a few notes, recall the whole song"

**Error Correction**:
- Network cleans up noisy input
- Acts as error-correcting code
- Robust to significant corruption (>30%)

**Energy Minimization**:
- Network "rolls downhill" to stored pattern
- Physical analogy: ball rolling to valley bottom
- Stored patterns = energy minima (attractors)

## Modifying the Experiment

### Try Different Patterns

Edit `create_letter_H()` function to create different 10×10 patterns:

```python
def create_custom_pattern():
    pattern = np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        # ... define your pattern
    ])
    return np.where(pattern == 1, 1, -1).flatten()
```

### Test Different Noise Levels

Modify `noise_levels` in `experiment_3_noise_correction()`:

```python
noise_levels = [0.1, 0.2, 0.3, 0.4, 0.5]  # Test up to 50% noise
```

### Increase Network Size

Change to larger patterns:

```python
def create_large_pattern():
    # 20×20 = 400 neurons
    pattern = create_your_20x20_pattern()
    return pattern.flatten()

net = HopfieldNetwork(n_neurons=400)
```

## Theoretical Background

### Hebbian Learning
"Neurons that fire together, wire together" - Donald Hebb

When two neurons are both active in a stored pattern, their connection strengthens. This creates an "attractor" in the network's state space.

### Energy Function
```
E = -1/2 × Σ_ij w_ij × s_i × s_j
```

- Stored patterns have **low energy** (deep valleys)
- Random states have **high energy** (hills)
- Network dynamics **minimize energy** (roll downhill)

### Update Rule
```
s_i^(t+1) = sign(Σ_j w_ij × s_j^(t))
```

Each neuron "listens" to weighted input from all other neurons and updates its state accordingly.

## Common Questions

**Q: Why only one pattern?**  
A: This is the classic 1982 demonstration. Single pattern shows core principles most clearly. For multiple patterns, see the main experiments.

**Q: Why does it converge so fast?**  
A: With one pattern, the energy landscape is simple - one deep valley. Network quickly finds it.

**Q: What if I use synchronous updates?**  
A: May oscillate! Asynchronous updates guarantee energy decrease. See Hopfield (1982) for mathematical proof.

**Q: Why {-1, +1} instead of {0, 1}?**  
A: Makes the math cleaner and connects to spin glass physics (Ising model).

## Troubleshooting

**Import errors?**
```bash
pip install numpy matplotlib seaborn
```

**Module 'src' not found?**
```bash
export PYTHONPATH=/path/to/hopfield_project:$PYTHONPATH
```

**Figures not displaying?**
```bash
# Check they were created
ls -l figures/

# Open manually
open figures/summary_hopfield_1982.png
```

## Next Steps

After understanding this single-pattern experiment:

1. **Multiple patterns**: See `../experiments/capacity_test.py`
2. **Spurious attractors**: See `../experiments/spurious_attractors.py`
3. **Noise robustness**: See `../experiments/noise_robustness.py`

## Historical Context

**1982**: Hopfield publishes seminal paper  
**Impact**: Revived interest in neural networks  
**Innovation**: Showed connection between neural computation and statistical mechanics  
**Legacy**: Foundation for modern deep learning

## References

**Main Paper**:
- Hopfield, J. J. (1982). PNAS, 79(8), 2554-2558.

**Related Work**:
- Hebb, D. O. (1949). The Organization of Behavior.
- Amit et al. (1985). Spin glass models of neural networks.

## Authors

Ingrid Corobana, Cosmin Glod, Irina Moise

**Date**: December 9, 2025

---

**Status**: Experiment completed successfully ✓  
**Runtime**: ~5 seconds  
**Figures**: 6 high-quality visualizations  
**Accuracy**: 100% in all tests
