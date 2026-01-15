# Hopfield Networks: From Classic to Modern
## Archaeology of Intelligent Machines - Final Project

**Authors:** Ingrid Corobana, Cosmin Glod, Irina Moise  
**Course:** Archaeology of Intelligent Machines, 2025

---

## 1. Literature Review: What Exists on This Topic

### Foundational Work

| Paper | Year | Key Contribution |
|-------|------|------------------|
| **Hopfield, J.J.** - "Neural networks and physical systems with emergent collective computational abilities" | 1982 | Original formulation of associative memory using energy-based neural networks |
| **Amit, D.J.** - "Modeling Brain Function" | 1989 | Theoretical analysis of storage capacity (~0.138N patterns) |
| **Ramsauer et al.** - "Hopfield Networks is All You Need" | 2020 | Modern Hopfield with exponential capacity, connection to Transformers |
| **Sahoo & Pradhan** - "Behavior of Learning Rules in Hopfield Neural Network" | 2020 | Comparison of Hebbian vs Pseudo-Inverse learning rules |

### Key Concepts from Literature

1. **Energy-Based Models**: Hopfield networks minimize an energy function:
   $$E = -\frac{1}{2}\sum_{i,j} w_{ij} s_i s_j$$
   
2. **Hebbian Learning**: "Neurons that fire together, wire together"
   $$W = \frac{1}{N}\sum_{\mu} \xi^{\mu} (\xi^{\mu})^T$$

3. **Capacity Limit**: Classical networks can store ~0.138N patterns reliably

4. **Modern Hopfield**: Uses softmax attention, achieving exponential capacity:
   $$\xi^{new} = X \cdot \text{softmax}(\beta X^T \xi)$$

### What We Add

- **Comparative analysis** of three approaches: Hebbian, Pseudo-Inverse, and Modern Hopfield
- **Visual demonstrations** of why similar patterns fail with Hebbian learning
- **Energy landscape visualizations** comparing learning rules
- **Practical implementation** with reproducible experiments

---

## 2. Data and Exploratory Data Analysis (EDA)

### Datasets Used

We use **synthetic pattern datasets** to ensure controlled experiments:

| Dataset | Size | Neurons | Description |
|---------|------|---------|-------------|
| **Letter Patterns** | 3 patterns (A, B, C) | 100 (10×10) | Introduction/teaching examples |
| **Geometric Patterns** | 5 patterns | 576 (24×24) | Orthogonal patterns (low correlation) |
| **Simpsons Characters** | 5 patterns | 576 (24×24) | Similar patterns (high correlation ~46%) |

### Exploratory Data Analysis

#### Pattern Correlation Analysis

We analyze pattern similarity using the correlation matrix:

```
Pattern Similarity (Simpsons):
         Homer  Marge  Bart   Lisa   Maggie
Homer    1.00   0.42   0.48   0.45   0.41
Marge    0.42   1.00   0.39   0.52   0.38
Bart     0.48   0.39   1.00   0.47   0.44
Lisa     0.45   0.52   0.47   1.00   0.43
Maggie   0.41   0.38   0.44   0.43   1.00

Average off-diagonal correlation: ~46%
```

**Key Finding:** High pattern correlation (>40%) causes interference in Hebbian learning.

#### Pattern Orthogonality (Geometric)

```
Geometric patterns have near-zero correlation:
Average off-diagonal correlation: <5%
```

This explains why geometric patterns work well with standard Hebbian learning.

### Visualization: Patterns Stored in Memory

*All visualizations are generated in the notebook `image_retrieval_3.ipynb`*

---

## 3. Models and Computational Requirements

### Models Implemented

#### 3.1 Classical Hopfield Network (Hebbian)
```python
class HopfieldNetwork:
    def train(self, patterns):
        W = (1/N) * sum(ξ @ ξ.T for ξ in patterns)
```
- **Learning Rule:** Hebbian (outer product)
- **Capacity:** ~0.138N patterns
- **Limitation:** Fails on correlated patterns

#### 3.2 Pseudo-Inverse Hopfield Network
```python
class PseudoInverseHopfield:
    def train(self, patterns):
        X = patterns.T
        W = X @ inv(X.T @ X) @ X.T  # Moore-Penrose pseudoinverse
```
- **Learning Rule:** Pseudo-Inverse
- **Advantage:** Orthogonalizes weight matrix, eliminates cross-talk
- **Result:** 100% accuracy on similar patterns

#### 3.3 Modern Hopfield Network
```python
class ModernHopfieldNetwork:
    def retrieve(self, query):
        attention = softmax(β * X.T @ query)
        return X @ attention
```
- **Mechanism:** Softmax attention (identical to Transformer attention!)
- **Capacity:** Exponential in N
- **Advantage:** No matrix inversion, naturally handles similar patterns

### Computational Requirements

| Component | Requirement |
|-----------|-------------|
| **Hardware** | CPU only (no GPU required) |
| **Memory** | <1 GB RAM |
| **Python** | 3.8+ |
| **Dependencies** | NumPy, Matplotlib, SciPy, scikit-learn |
| **Runtime** | ~30 seconds for full notebook execution |

### Why No GPU?

Hopfield networks are computationally lightweight:
- Weight matrix: 576×576 = 331,776 parameters (for 24×24 images)
- No backpropagation or gradient descent
- Single matrix multiplication for retrieval

This is in stark contrast to modern deep learning models (millions of parameters).

---

## 4. Evaluation Methods and Model Comparison

### Evaluation Metrics

#### 4.1 Retrieval Accuracy
```python
def accuracy(original, retrieved):
    return 1.0 if np.array_equal(original, retrieved) else 0.0
```
Binary success/failure based on exact pattern match.

#### 4.2 Pattern Correlation
```python
def correlation(original, retrieved):
    return np.corrcoef(original.flatten(), retrieved.flatten())[0, 1]
```
Measures similarity (1.0 = perfect, 0.0 = random).

#### 4.3 Hamming Distance
```python
def hamming_distance(a, b):
    return np.sum(a != b)
```
Counts number of differing bits.

### Experimental Protocol

1. **Train** network on P patterns
2. **Corrupt** each pattern with noise (0% to 40%)
3. **Retrieve** using network dynamics
4. **Measure** accuracy over 30 trials per noise level

### Results Summary

#### Geometric Patterns (Low Correlation ~5%)

| Noise Level | Hebbian | Pseudo-Inverse | Modern |
|-------------|---------|----------------|--------|
| 10% | 100% | 100% | 100% |
| 20% | 95% | 100% | 100% |
| 25% | 90% | 100% | 100% |
| 30% | 75% | 100% | 100% |

**Conclusion:** All methods work well on orthogonal patterns.

#### Simpsons Characters (High Correlation ~46%)

| Noise Level | Hebbian | Pseudo-Inverse | Modern |
|-------------|---------|----------------|--------|
| 10% | 20% | 100% | 100% |
| 20% | 0% | 100% | 100% |
| 30% | 0% | **100%** | **100%** |
| 40% | 0% | 90% | 95% |

**Key Finding:** Hebbian fails completely (0%) on similar patterns, while Pseudo-Inverse and Modern achieve near-perfect accuracy.

### Visualization: Energy Landscape Comparison

We use PCA to project the high-dimensional state space to 2D and visualize energy landscapes:

| Hebbian Learning | Pseudo-Inverse Learning |
|------------------|-------------------------|
| Shallow, merged basins | Sharp, separated wells |
| Patterns blend together | Each pattern has distinct attractor |
| Cross-talk causes failures | Orthogonalization prevents interference |

---

## Preliminary Results

### Main Findings

1. **Pattern Similarity Matters:** Classical Hopfield with Hebbian learning fails when patterns share >30% correlation

2. **Learning Rule is Key:** The limitation is NOT the Hopfield architecture, but the learning rule:
   - Hebbian: 0% on similar patterns
   - Pseudo-Inverse: 100% on same patterns

3. **Modern Hopfield = Attention:** The update rule $\xi^{new} = X \cdot \text{softmax}(\beta X^T \xi)$ is identical to Transformer self-attention

4. **Energy Landscape Insight:** Pseudo-Inverse creates deeper, more separated energy wells, preventing spurious attractors

### Visualizations Generated

- Weight matrix structure and interpretation
- 3D energy landscape with pattern attractors
- Retrieval accuracy vs. noise level curves
- Side-by-side Hebbian vs Pseudo-Inverse energy landscapes
- Classical vs Modern Hopfield comparison on Simpsons

---

## Future Work

1. **Real Image Data:** Test on MNIST digits or celebrity faces
2. **Capacity Experiments:** Systematically measure capacity limits for each approach
3. **Biological Plausibility:** Compare with neuroscience literature on memory formation
4. **Transformer Connection:** Explicit demonstration of Hopfield ↔ Attention equivalence

---

## Project Structure

```
hopfield_project/
├── src/
│   ├── hopfield.py          # Classical Hopfield implementation
│   ├── patterns.py          # Pattern generation (letters, geometric)
│   └── visualization.py     # Plotting utilities
├── notebooks/
│   └── image_retrieval_3.ipynb  # Main demonstration notebook
├── figures/                 # Generated visualizations
├── latex_presentation/      # Presentation slides
└── requirements.txt         # Dependencies
```

---

## Quick Start

```bash
# Clone and setup
cd hopfield_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the main notebook
jupyter notebook notebooks/image_retrieval_3.ipynb
```

---

## References

1. Hopfield, J.J. (1982). "Neural networks and physical systems with emergent collective computational abilities". *PNAS*, 79(8), 2554-2558.

2. Ramsauer, H., et al. (2020). "Hopfield Networks is All You Need". *ICLR 2021*.

3. Sahoo, S. & Pradhan, P. (2020). "Behavior of Learning Rules in Hopfield Neural Network for Odia Script". *IJACSA*, Vol. 11, No. 1.

4. Amit, D.J. (1989). "Modeling Brain Function: The World of Attractor Neural Networks". Cambridge University Press.

5. Youtube: https://www.youtube.com/watch?v=1WPJdAW-sFo

6. Youtube: https://www.youtube.com/watch?v=piF6D6CQxUw


---

*Archaeology of Intelligent Machines - University of Bucharest, 2025*
