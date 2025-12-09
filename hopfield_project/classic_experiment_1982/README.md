# Classic Hopfield Network Experiment (1982)

## Historical Context

This reproduces John Hopfield's original 1982 experiment on associative memory with discrete binary neurons. The key innovation was showing that a simple network with symmetric weights could store and retrieve patterns through energy minimization.

**Original Paper**: Hopfield, J. J. (1982). "Neural networks and physical systems with emergent collective computational abilities". Proceedings of the National Academy of Sciences, 79(8), 2554-2558.

## The Experiment

### What Hopfield Showed

1. **Single Pattern Storage**: A network can store a pattern and retrieve it from partial/noisy input
2. **Energy Minimization**: The network dynamics guarantee convergence to stable states
3. **Associative Memory**: Given part of a pattern, the network completes it
4. **Biological Plausibility**: Simple local update rules, symmetric connections

### Classic Demo: Pattern Completion

- Store a single binary pattern (e.g., a letter or face)
- Present partial or corrupted version
- Watch network reconstruct the original
- Visualize the energy descent

## Our Reproduction

### Pattern Used
We use a 10x10 binary pattern (100 neurons) representing a simple shape or letter, similar to what Hopfield used.

### Experiments
1. **Complete Pattern Storage**: Store one clean pattern
2. **Partial Pattern Retrieval**: Present 25%, 50%, 75% of the pattern
3. **Noisy Pattern Retrieval**: Add 10%, 20%, 30% noise
4. **Energy Landscape**: Visualize how energy decreases during retrieval
5. **Update Dynamics**: Show step-by-step neuron updates

## Key Results

The network successfully:
- Stores a single pattern as a stable attractor
- Retrieves the full pattern from partial cues
- Corrects noisy inputs
- Converges in a few iterations (typically 2-5)
- Energy monotonically decreases (guaranteed by asynchronous updates)

## Historical Significance

This simple experiment demonstrated that:
- Collective computation emerges from simple local rules
- Memory is distributed across all connections
- Content-addressable memory is possible with neural networks
- Physical systems can perform computation

## Files

- `hopfield_1982_reproduction.py` - Main experiment script
- `figures/` - Generated visualizations
- `data/` - Stored patterns and results
- `RESULTS.md` - Detailed experimental results

## Running the Experiment

```bash
cd classic_experiment_1982
python hopfield_1982_reproduction.py
```

## Authors

Ingrid Corobana, Moise Irina, Cosmin Glod

**Date**: December 9, 2025
