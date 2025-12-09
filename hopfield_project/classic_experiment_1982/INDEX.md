# Index: Hopfield 1982 Classic Experiment

## Quick Navigation

### Start Here
- **README.md** - Historical context and experiment overview
- **QUICK_START.md** - Run the experiment in 30 seconds

### Results
- **RESULTS.md** - Comprehensive experimental results and analysis
- **figures/summary_hopfield_1982.png** - Main summary visualization

### Code
- **hopfield_1982_reproduction.py** - Complete experiment implementation

---

## Document Guide

### README.md
**Purpose**: Provides historical context for Hopfield's 1982 paper  
**Content**:
- Original paper reference
- What Hopfield demonstrated
- Significance of single-pattern experiment
- Our reproduction approach

**Read this if**: You want to understand the historical significance

---

### QUICK_START.md
**Purpose**: Get running immediately  
**Content**:
- How to run the experiment
- Expected results
- How to modify parameters
- Troubleshooting

**Read this if**: You want to run the experiment right now

---

### RESULTS.md
**Purpose**: Detailed experimental findings  
**Content**:
- 5 experiments with complete results
- Tables of metrics
- Theoretical analysis
- Comparison to original 1982 results

**Read this if**: You need detailed quantitative results

---

### hopfield_1982_reproduction.py
**Purpose**: Complete implementation  
**Content**:
- 5 experiment functions
- Visualization code
- Pattern creation utilities
- 672 lines, fully documented

**Read this if**: You want to understand or modify the code

---

## Figures Directory

### Main Summary
**summary_hopfield_1982.png** (181 KB)
- Comprehensive overview of all experiments
- 3×4 grid layout
- Shows: storage, weights, completion, correction
- **START HERE for visual understanding**

### Individual Experiments

**exp1_perfect_storage.png** (9.5 KB)
- Demonstrates single pattern storage
- Shows stored vs retrieved pattern

**exp2_partial_completion.png** (22 KB)
- Pattern completion from 75%, 50%, 25% input
- Shows how network fills in missing information

**exp3_noise_correction.png** (19 KB)
- Error correction from 10%, 20%, 30% noise
- Shows how network cleans corrupted input

**exp4_energy_dynamics.png** (89 KB)
- Energy descent during retrieval
- Shows "rolling downhill" dynamics

**exp5_step_by_step.png** (47 KB)
- Neuron-by-neuron update visualization
- Shows convergence process

---

## Experiment Overview

### Experiment 1: Perfect Storage
**Question**: Can we store and retrieve a pattern?  
**Result**: Yes, perfect retrieval in 1 iteration  
**Figure**: exp1_perfect_storage.png

### Experiment 2: Pattern Completion
**Question**: Can we retrieve from partial input?  
**Result**: Yes, even with 75% missing (25% visible)  
**Figure**: exp2_partial_completion.png

### Experiment 3: Noise Correction
**Question**: Can we correct errors?  
**Result**: Yes, perfect correction up to 30% noise  
**Figure**: exp3_noise_correction.png

### Experiment 4: Energy Dynamics
**Question**: Does energy always decrease?  
**Result**: Yes, monotonic descent guaranteed  
**Figure**: exp4_energy_dynamics.png

### Experiment 5: Step-by-Step
**Question**: How does retrieval work?  
**Result**: Fast convergence in 1-2 iterations  
**Figure**: exp5_step_by_step.png

---

## Key Concepts Explained

### Content-Addressable Memory
**What**: Access memory by content, not address  
**Example**: Hear a few notes → recall whole song  
**Experiment**: See experiment 2 (partial completion)

### Error Correction
**What**: Network corrects corrupted input  
**Example**: Recognize blurry photo  
**Experiment**: See experiment 3 (noise correction)

### Energy Minimization
**What**: Network "rolls downhill" to stable state  
**Example**: Ball rolling into valley  
**Experiment**: See experiment 4 (energy dynamics)

### Attractor States
**What**: Stable configurations network settles into  
**Example**: Stored memories are valleys in landscape  
**Experiment**: All experiments demonstrate this

---

## File Size Summary

```
Total: ~400 KB

Documentation:
  README.md          8 KB
  QUICK_START.md    11 KB  
  RESULTS.md        15 KB
  INDEX.md           5 KB

Code:
  hopfield_1982_reproduction.py    25 KB

Figures:
  exp1_perfect_storage.png          9.5 KB
  exp2_partial_completion.png      22 KB
  exp3_noise_correction.png        19 KB
  exp4_energy_dynamics.png         89 KB
  exp5_step_by_step.png            47 KB
  summary_hopfield_1982.png       181 KB
```

---

## Recommended Reading Order

### For Quick Understanding:
1. QUICK_START.md (2 min)
2. figures/summary_hopfield_1982.png (visual)
3. Run the experiment (5 sec)

### For Deep Understanding:
1. README.md (historical context)
2. QUICK_START.md (hands-on)
3. Run experiment and observe output
4. RESULTS.md (detailed analysis)
5. hopfield_1982_reproduction.py (implementation)

### For Presentation:
1. summary_hopfield_1982.png (main figure)
2. exp2_partial_completion.png (wow factor)
3. exp4_energy_dynamics.png (theory)
4. Key metrics from RESULTS.md

---

## Running the Experiment

```bash
# Navigate to folder
cd classic_experiment_1982

# Run experiment
python hopfield_1982_reproduction.py

# View results
open figures/summary_hopfield_1982.png
```

**Time**: ~5 seconds  
**Output**: 6 figures + terminal results

---

## Citation

If using this reproduction:

```
Corobana, I., Irina, M., & Glod, C. (2025).
Reproduction of Hopfield's 1982 Associative Memory Experiment.
Hopfield Networks Project, December 9, 2025.
```

Original paper:
```
Hopfield, J. J. (1982). 
Neural networks and physical systems with emergent 
collective computational abilities. 
Proceedings of the National Academy of Sciences, 79(8), 2554-2558.
```

---

## Status

- Experiments: COMPLETE ✓
- Documentation: COMPLETE ✓
- Figures: 6/6 generated ✓
- Results: Match theory ✓
- Code: Tested and working ✓

**Ready for**: Analysis, presentation, further experiments

---

**Authors**: Ingrid Corobana, Moise Irina, Cosmin Glod  
**Date**: December 9, 2025  
**Project**: Hopfield Networks - Archaeology of Intelligent Machines
