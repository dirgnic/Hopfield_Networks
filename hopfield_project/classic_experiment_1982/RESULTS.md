# Experimental Results: Hopfield 1982 Reproduction

**Date**: December 9, 2025  
**Authors**: Ingrid Corobana, Cosmin Glod, Irina Moise

## Summary

This document presents the results of reproducing John Hopfield's seminal 1982 experiment on associative memory with discrete binary neurons. We successfully demonstrated all key properties of the Hopfield network with a single stored pattern.

## Experiment 1: Single Pattern Storage

**Objective**: Verify that a pattern can be stored and retrieved perfectly.

**Setup**:
- Pattern: Letter 'H' (10×10 grid = 100 neurons)
- Network: 100 neurons, 9,900 connections
- Storage: Hebbian learning rule

**Results**:
- Pattern stored successfully
- Weight matrix: 100×100, average |weight| = 0.0099
- Perfect retrieval: 1 iteration to convergence
- Energy of stored pattern: -49.50
- Overlap with original: 1.0000 (perfect match)

**Conclusion**: The stored pattern is a stable fixed point (attractor) in the network dynamics.

---

## Experiment 2: Pattern Completion from Partial Input

**Objective**: Demonstrate content-addressable memory - retrieve full pattern from partial information.

**Setup**:
- Test with 75%, 50%, and 25% of pattern visible
- Remaining neurons initialized randomly
- Maximum 20 iterations allowed

**Results**:

| % Visible | Known Neurons | Convergence | Iterations | Final Overlap | Hamming Distance |
|-----------|--------------|-------------|------------|---------------|------------------|
| 75%       | 81/100       | YES         | 2          | 1.0000        | 0                |
| 50%       | 46/100       | YES         | 2          | 1.0000        | 0                |
| 25%       | 23/100       | YES         | 2          | 1.0000        | 0                |

**Key Findings**:
1. **Perfect completion**: All cases achieved 100% retrieval
2. **Fast convergence**: Only 2 iterations needed
3. **Robust to missing data**: Even with 75% missing (25% visible), full pattern reconstructed
4. **Content-addressability**: Any part of the pattern can retrieve the whole

**Biological Analogy**: Like recalling a full song from hearing just a few notes, or recognizing a face from seeing just the eyes.

---

## Experiment 3: Noise Correction

**Objective**: Test error-correction capability - retrieve clean pattern from corrupted input.

**Setup**:
- Add noise by randomly flipping 10%, 20%, and 30% of bits
- Maximum 20 iterations allowed

**Results**:

| Noise Level | Flipped Bits | Convergence | Iterations | Correction | Energy Change |
|-------------|--------------|-------------|------------|------------|---------------|
| 10%         | 10/100       | YES         | 2          | PERFECT    | -31.50 → -49.50 (Δ=18.00) |
| 20%         | 20/100       | YES         | 2          | PERFECT    | -17.50 → -49.50 (Δ=32.00) |
| 30%         | 30/100       | YES         | 2          | PERFECT    | -7.50 → -49.50 (Δ=42.00)  |

**Key Findings**:
1. **Perfect error correction**: All noise completely removed
2. **Energy minimization**: Higher noise → larger energy decrease
3. **Monotonic descent**: Energy decreased or stayed constant at each step
4. **Rapid correction**: All cases converged in 2 iterations

**Physical Interpretation**: The network "rolls downhill" in the energy landscape, from high-energy noisy states to the low-energy stored pattern.

---

## Experiment 4: Energy Minimization Dynamics

**Objective**: Visualize energy descent during pattern retrieval.

**Setup**:
- Three test cases: 20% noise, 50% partial, 30% noise
- Record energy at each iteration

**Results**:

| Test Case   | Initial Energy | Final Energy | Energy Decrease | Iterations |
|-------------|----------------|--------------|-----------------|------------|
| 20% Noise   | -17.50         | -49.50       | 32.00           | 2          |
| 50% Partial | -13.02         | -49.50       | 36.48           | 2          |
| 30% Noise   | -7.50          | -49.50       | 42.00           | 2          |

**Energy Trajectory Observations**:
1. Energy NEVER increases (guaranteed by asynchronous updates)
2. Steeper descent for more corrupted inputs
3. All trajectories end at same minimum (stored pattern energy)
4. Convergence is rapid (2 iterations)

**Mathematical Guarantee**: Asynchronous update rule ensures ΔE ≤ 0 at every step.

---

## Experiment 5: Step-by-Step Update Dynamics

**Objective**: Visualize how individual neuron updates lead to pattern reconstruction.

**Setup**:
- Start with 25% noise (25 flipped bits)
- Record state after each iteration
- Visualize first 8 steps

**Results**:

| Step | Energy  | Errors | Description |
|------|---------|--------|-------------|
| 0    | -12.00  | 25/100 | Initial noisy state |
| 1    | -49.50  | 0/100  | CONVERGED - all errors corrected |
| 2    | -49.50  | 0/100  | Stable (no further changes) |

**Observations**:
1. **Single iteration correction**: All 25 errors fixed in one sweep
2. **Immediate convergence**: Network reached stable state after first update
3. **Stability**: Once converged, state remains unchanged
4. **Local computation**: Each neuron updated based only on its weighted inputs

---

## Overall Conclusions

### What We Successfully Demonstrated

1. **Associative Memory**: 
   - Store a pattern and retrieve it from partial/corrupted input
   - Content-addressable: any part retrieves the whole

2. **Error Correction**:
   - Perfect correction of up to 30% noise
   - Network acts as error-correcting code

3. **Energy Minimization**:
   - Dynamics guaranteed to decrease energy
   - Stored patterns are local energy minima (attractors)

4. **Computational Emergence**:
   - Complex memory retrieval from simple local rules
   - No central controller - collective computation

5. **Biological Plausibility**:
   - Symmetric connections (reciprocal synapses)
   - Local update rules (each neuron "listens" to neighbors)
   - Hebbian learning ("fire together, wire together")

### Historical Significance

Hopfield's 1982 paper showed that:
- Simple physics-inspired networks can perform computation
- Memory is distributed across connections, not stored in specific neurons
- Content-addressable memory emerges from energy minimization
- Neural networks can be analyzed using statistical mechanics

### Performance Metrics

| Metric | Value | Comment |
|--------|-------|---------|
| Storage capacity | 1 pattern | Single pattern demonstration |
| Retrieval accuracy | 100% | Perfect in all tests |
| Convergence speed | 1-2 iterations | Very fast |
| Noise tolerance | >30% | Excellent robustness |
| Partial input tolerance | >75% missing | Excellent completion |

### Comparison to Original 1982 Results

Our reproduction matches Hopfield's original findings:
- ✓ Single pattern storage works perfectly
- ✓ Pattern completion from partial input
- ✓ Error correction from noisy input
- ✓ Energy minimization dynamics
- ✓ Fast convergence (few iterations)
- ✓ Stable attractor states

---

## Theoretical Foundation

### Hebbian Learning Rule

**Mathematical Form**:
```
w_ij = (1/N) × ξ_i × ξ_j  for i ≠ j
w_ii = 0
```

Where:
- w_ij: weight between neurons i and j
- ξ_i: state of neuron i in stored pattern
- N: number of neurons

**Interpretation**: Neurons that are co-active in the pattern develop strong connections.

### Energy Function

**Mathematical Form**:
```
E = -1/2 × Σ_ij w_ij × s_i × s_j
```

**Properties**:
- Stored patterns have low (negative) energy
- Energy decreases during asynchronous updates
- Local minima correspond to attractor states

### Update Rule

**Asynchronous Update**:
```
s_i^(t+1) = sign(Σ_j w_ij × s_j^(t))
```

**Guarantee**: E^(t+1) ≤ E^(t) (energy never increases)

---

## Technical Details

### Network Architecture
- Neurons: 100 (arranged in 10×10 grid)
- Connections: 9,900 (fully connected, excluding self-connections)
- Activation: Binary {-1, +1}
- Learning: Single-shot Hebbian rule

### Implementation
- Language: Python 3.9
- Libraries: NumPy, Matplotlib, Seaborn
- Visualization: High-resolution PNG (150 DPI)
- Random seed: 42 (for reproducibility)

### Computational Requirements
- Memory: <10 MB
- Time: <5 seconds for all experiments
- CPU: Standard laptop processor

---

## Figures Generated

1. **exp1_perfect_storage.png** - Demonstrates single pattern storage
2. **exp2_partial_completion.png** - Pattern completion from 25%, 50%, 75% input
3. **exp3_noise_correction.png** - Error correction from 10%, 20%, 30% noise
4. **exp4_energy_dynamics.png** - Energy descent trajectories
5. **exp5_step_by_step.png** - Neuron-by-neuron update visualization
6. **summary_hopfield_1982.png** - Comprehensive summary figure

---

## References

1. **Hopfield, J. J. (1982)**. "Neural networks and physical systems with emergent collective computational abilities". *Proceedings of the National Academy of Sciences*, 79(8), 2554-2558.

2. **Hebb, D. O. (1949)**. *The Organization of Behavior*. New York: Wiley.

3. **Amit, D. J., Gutfreund, H., & Sompolinsky, H. (1985)**. "Storing infinite numbers of patterns in a spin-glass model of neural networks". *Physical Review Letters*, 55(14), 1530.

---

## Reproduction Notes

This reproduction was created on December 9, 2025 by:
- Ingrid Corobana
- Cosmin Glod
- Irina Moise

The code is available in: `classic_experiment_1982/hopfield_1982_reproduction.py`

All experiments were successful and results match the theoretical predictions and original 1982 findings.

**Status**: COMPLETE AND VERIFIED ✓
