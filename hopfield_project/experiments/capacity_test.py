"""
Capacity Test Experiment
========================
Determine network capacity: maximum patterns that can be reliably stored.
"""

import sys
sys.path.append('..')

import numpy as np
import matplotlib.pyplot as plt
from src.hopfield import HopfieldNetwork
from src.patterns import generate_random_patterns
from src.visualization import plot_capacity_experiment

# Set random seed
np.random.seed(42)

def test_capacity(n_neurons: int = 100, max_patterns: int = 30, 
                 noise_level: float = 0.1, n_trials: int = 10):
    """
    Test network capacity by varying number of stored patterns.
    
    Theoretical capacity for random patterns: ~0.138 * N
    For N=100, this is about 14 patterns.
    """
    print("=" * 60)
    print("HOPFIELD NETWORK: CAPACITY EXPERIMENT")
    print("=" * 60)
    print(f"Network size: {n_neurons} neurons")
    print(f"Theoretical capacity: ~{int(0.138 * n_neurons)} patterns")
    print(f"Testing up to {max_patterns} patterns")
    print()
    
    pattern_counts = range(1, max_patterns + 1)
    accuracies = []
    
    for n_patterns in pattern_counts:
        print(f"Testing with {n_patterns} patterns...", end=" ")
        
        trial_accuracies = []
        
        for trial in range(n_trials):
            # Generate random patterns
            patterns = generate_random_patterns(n_patterns, n_neurons)
            
            # Train network
            hopfield = HopfieldNetwork(n_neurons)
            hopfield.train(patterns)
            
            # Test retrieval for each pattern
            successes = 0
            for pattern in patterns:
                noisy = hopfield.add_noise(pattern, noise_level=noise_level)
                retrieved, _ = hopfield.retrieve(noisy, max_iter=50)
                
                if np.array_equal(retrieved, pattern):
                    successes += 1
            
            accuracy = successes / n_patterns
            trial_accuracies.append(accuracy)
        
        mean_accuracy = np.mean(trial_accuracies)
        std_accuracy = np.std(trial_accuracies)
        accuracies.append(mean_accuracy)
        
        print(f"Accuracy: {mean_accuracy:.2%} ± {std_accuracy:.2%}")
    
    print()
    print("=" * 60)
    print("RESULTS:")
    print("=" * 60)
    
    # Find practical capacity (where accuracy drops below 90%)
    practical_capacity = 0
    for i, acc in enumerate(accuracies):
        if acc >= 0.9:
            practical_capacity = i + 1
        else:
            break
    
    print(f"Practical capacity (≥90% accuracy): {practical_capacity} patterns")
    print(f"Theoretical capacity: ~{int(0.138 * n_neurons)} patterns")
    print()
    print("Brain Analogy:")
    print("  When too many memories are stored, the energy landscape")
    print("  becomes 'crowded' - valleys merge and the network starts")
    print("  to confuse memories or create 'false memories' (spurious attractors).")
    print()
    
    # Plot results
    fig = plot_capacity_experiment(list(pattern_counts), accuracies, 
                                  theoretical_capacity=0.138 * n_neurons)
    plt.savefig('../figures/capacity_experiment.png', dpi=150, bbox_inches='tight')
    print("Saved figure: capacity_experiment.png")
    
    return accuracies

if __name__ == "__main__":
    accuracies = test_capacity(n_neurons=100, max_patterns=30, 
                              noise_level=0.1, n_trials=10)
