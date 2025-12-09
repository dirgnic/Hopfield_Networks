# Modern Hopfield Networks - Comprehensive Theory Implementation

## Overview

This module provides a complete implementation and educational walkthrough of both classical (1982) and modern (2020) Hopfield Networks, with practical demonstrations using Simpsons character face recognition.

**Based on:** "Hopfield Networks is All You Need" (Ramsauer et al., 2020)

**Authors:** Ingrid Corobana, Cosmin Glod, Irina Moise

---

## Files

### Main Files

1. **`notebooks/hopfield_modern_theory.ipynb`**
   - Interactive Jupyter notebook with full theory
   - 11 comprehensive parts with visualizations
   - Works both locally and in Google Colab
   - Includes brain analogies throughout

2. **`hopfield_modern_theory.py`**
   - Standalone Python script version
   - Fully Colab-compatible
   - Generates 6 visualization figures
   - Can be run from command line

### Dataset

- **Synthetic Simpsons character faces** (10 characters)
  - Homer, Marge, Bart, Lisa, Maggie
  - Ned, Apu, Moe, Burns, Smithers
- **32x32 grayscale images** with distinctive features
- **Stored efficiently as numpy arrays**

---

## Theory Coverage

### Part 1: Classical Hopfield Networks (1982)
- Binary neurons {-1, +1}
- Hebbian learning rule
- Energy function and minimization
- Capacity limit: ~0.138N patterns

### Part 2: Modern Hopfield Networks (2020)
- Continuous states (real numbers)
- Exponential storage capacity
- Softmax attention mechanism
- Log-sum-exp energy function

### Part 3: Connection to Transformers
- Mathematical equivalence to attention
- Query-Key-Value correspondence
- Why Transformers are associative memory

### Part 4-11: Practical Implementation
- Modern Hopfield Network class
- Character face storage and retrieval
- Noise robustness testing (0-100%)
- Energy landscape visualization
- Classical vs Modern comparison

---

## Key Features

### Brain Analogies Throughout
- **Memory as valleys** in energy landscape
- **Retrieval as rolling downhill** to stable states
- **Attention weights** as memory activation
- **Beta parameter** as focus/concentration

### Demonstrations
1. **Noisy retrieval**: 40% noise, 90%+ accuracy
2. **Partial occlusion**: Reconstruct from 70% visible
3. **Energy minimization**: Watch convergence dynamics
4. **Multiple characters**: Test all 10 faces simultaneously
5. **Systematic robustness**: Accuracy vs noise curves
6. **Classical comparison**: Side-by-side with 1982 model

---

## Usage

### Option 1: Jupyter Notebook (Recommended)

```bash
cd hopfield_project
source venv/bin/activate
jupyter notebook notebooks/hopfield_modern_theory.ipynb
```

### Option 2: Python Script

```bash
cd hopfield_project
source venv/bin/activate
python hopfield_modern_theory.py
```

Generates 6 PNG figures:
- `simpsons_characters.png`
- `memory_retrieval_test.png`
- `energy_landscape.png`
- `multiple_character_recognition.png`
- `noise_robustness.png`
- `classical_vs_modern.png`

### Option 3: Google Colab

1. Upload `hopfield_modern_theory.ipynb` to Colab
2. Run all cells (automatic setup included)
3. All dependencies installed automatically

**Or run the Python script:**

```python
# In Colab
!wget https://raw.githubusercontent.com/dirgnic/Hopfield_Networks/main/hopfield_project/hopfield_modern_theory.py
!python hopfield_modern_theory.py
```

---

## Mathematical Highlights

### Classical Hopfield Update
```
s_i^(t+1) = sign(Σ w_ij * s_j^(t))
```

### Modern Hopfield Update
```
ξ^(t+1) = X · softmax(β X^T ξ^(t))
```

### Energy Functions

**Classical:**
```
E(s) = -1/2 Σ w_ij s_i s_j
```

**Modern:**
```
E(ξ) = -lse(β X^T ξ) + 1/2 ξ^T ξ + β^-1 log(M) + 1/2 M
```

---

## Results Summary

### Noise Robustness (β=5)
- **0% noise:** 100% accuracy
- **20% noise:** 100% accuracy
- **40% noise:** 90% accuracy
- **60% noise:** 70% accuracy
- **80% noise:** 50% accuracy

### Convergence Speed
- **Classical:** 20-50 iterations
- **Modern (β=1):** 5-10 iterations
- **Modern (β=5):** 3-5 iterations
- **Modern (β=10):** 2-3 iterations

### Storage Capacity
- **Classical:** ~138 patterns (for N=1000)
- **Modern:** 10^434 patterns (exponential)

---

## Key Insights

### Why Modern Hopfield Works Better

1. **Continuous states** allow gradual refinement
2. **Softmax attention** creates sharper attractor basins
3. **Higher beta** increases focus and robustness
4. **Energy function** guarantees convergence

### Connection to Deep Learning

- **Transformer attention IS modern Hopfield**
- Same math describes brains and AI systems
- Deep learning rediscovering neuroscience principles

### Brain Analogies

- **Energy landscape:** "Comfort" of current thought
- **Attention weights:** Which memories are activated
- **Convergence:** "Aha!" moment of recall
- **Beta parameter:** Concentration level

---

## Dependencies

```
numpy>=2.0.2
matplotlib>=3.9.4
scipy>=1.13.1
pillow>=10.4.0
scikit-learn>=1.5.1
```

All automatically installed in Colab.

---

## Integration with Project

This module **complements** the existing project:

### Existing (Classical Focus)
- `src/hopfield.py`: Classical discrete implementation
- `notebooks/exploration.ipynb`: Letter pattern demos
- `notebooks/image_retrieval.ipynb`: Geometric shapes
- `classic_experiment_1982/`: Historical reproduction

### New (Modern Focus)
- `notebooks/hopfield_modern_theory.ipynb`: Full theory
- `hopfield_modern_theory.py`: Standalone script
- Modern Hopfield class with attention
- Simpsons face recognition

### Together They Provide
- Complete historical context (1982 → 2020)
- Both discrete and continuous approaches
- Simple patterns AND realistic images
- Educational AND research-level content

---

## References

### Primary

1. **Hopfield, J.J. (1982).** "Neural networks and physical systems with emergent collective computational abilities." *Proceedings of the National Academy of Sciences*, 79(8), 2554-2558.

2. **Ramsauer, H., et al. (2020).** "Hopfield Networks is All You Need." *arXiv:2008.02217*
   - https://arxiv.org/abs/2008.02217

### Secondary

3. **Beren (2020).** "Walkthrough: Hopfield Networks is All You Need"
   - https://www.beren.io/2020-11-02-Walkthrough_Hopfield-Networks-Is-All-You-Need/

4. **Vaswani, A., et al. (2017).** "Attention is All You Need." *NeurIPS*.

---

## Educational Use

### Target Audiences

1. **Undergraduate students** - Clear explanations with analogies
2. **Graduate students** - Rigorous math and implementation
3. **Researchers** - Modern theory and connections to Transformers
4. **Practitioners** - Working code and practical demonstrations

### Learning Path

1. Start with classical Hopfield (`exploration.ipynb`)
2. See geometric patterns (`image_retrieval.ipynb`)
3. Understand historical context (`classic_experiment_1982/`)
4. **Learn modern theory** (`hopfield_modern_theory.ipynb`) ← This module
5. Read original papers for deeper understanding

### Key Takeaways

Students will learn:
- How associative memory works
- Why energy minimization guarantees convergence
- Connection between neuroscience and AI
- Modern attention mechanisms as memory retrieval
- Practical implementation techniques

---

## Future Extensions

### Possible Additions

1. **Real Simpsons dataset** - Download actual faces from simpsons-mnist
2. **More characters** - Test with 50+ patterns
3. **Video demos** - Animated convergence visualization
4. **Interactive widget** - Adjust beta in real-time
5. **Benchmark suite** - Compare with other architectures

### Research Directions

1. Sparse modern Hopfield networks
2. Hierarchical memory organization
3. Continual learning without catastrophic forgetting
4. Integration with modern transformer architectures

---

## Troubleshooting

### Common Issues

**Import errors:**
```bash
# Make sure virtual environment is active
source venv/bin/activate
pip install -r requirements.txt
```

**Matplotlib not showing plots:**
```python
# Add to notebook
%matplotlib inline
```

**Colab repository not found:**
```python
# Update repository URL in script
!git clone https://github.com/dirgnic/Hopfield_Networks.git
```

---

## License

Part of the Hopfield Networks project for the Archaeology of Intelligent Machines course.

---

## Contact

**Authors:**
- Ingrid Corobana
- Cosmin Glod
- Irina Moise

**Course:** Archaeology of Intelligent Machines - 2025

---

## Acknowledgments

- John Hopfield for the original 1982 network
- Hubert Ramsauer et al. for the 2020 modern formulation
- Beren for the excellent tutorial walkthrough
- The Simpsons creators for iconic characters

---

**Last Updated:** December 9, 2025
