"""
Noise Robustness Experiment
===========================
Test how network performance degrades with increasing noise.
"""

import sys
sys.path.append('..')

import numpy as np
import matplotlib.pyplot as plt
from src.hopfield import HopfieldNetwork
from src.patterns import generate_letters
from src.visualization import plot_noise_robustness

# Set random seed
np.random.seed(42)

def test_noise_robustness(n_trials: int = 20):
    """
    Test retrieval accuracy as noise increases from 0% to 50%.
    """
    print("=" * 60)
    print("HOPFIELD NETWORK: NOISE ROBUSTNESS EXPERIMENT")
    print("=" * 60)
    print()
    
    # Generate and train network
    print("Generating patterns and training network...")
    patterns = generate_letters(['A', 'B', 'C', 'D', 'E'], size=10)
    hopfield = HopfieldNetwork(n_neurons=100)
    hopfield.train(patterns)
    print(f"Trained on {patterns.shape[0]} patterns")
    print()
    
    # Test different noise levels
    noise_levels = np.arange(0.0, 0.55, 0.05)
    accuracies = []
    
    for noise_level in noise_levels:
        print(f"Testing noise level: {int(noise_level*100)}%...", end=" ")
        
        successes = 0
        total_tests = n_trials * len(patterns)
        
        for _ in range(n_trials):
            for pattern in patterns:
                # Add noise
                noisy = hopfield.add_noise(pattern, noise_level=noise_level)
                
                # Retrieve
                retrieved, _ = hopfield.retrieve(noisy, max_iter=50)
                
                # Check success
                if np.array_equal(retrieved, pattern):
                    successes += 1
        
        accuracy = successes / total_tests
        accuracies.append(accuracy)
        print(f"Accuracy: {accuracy:.2%}")
    
    print()
    print("=" * 60)
    print("RESULTS:")
    print("=" * 60)
    
    # Find breaking point (where accuracy drops below 50%)
    breaking_point = None
    for i, acc in enumerate(accuracies):
        if acc < 0.5 and breaking_point is None:
            breaking_point = noise_levels[i]
            break
    
    if breaking_point:
        print(f"Breaking point: ~{int(breaking_point*100)}% noise")
    else:
        print("Network remained robust across all tested noise levels!")
    
    print()
    print("Brain Analogy:")
    print("  Like human memory, the network can reconstruct complete")
    print("  memories from partial cues, but only up to a point.")
    print("  Beyond ~30-40% corruption, retrieval becomes unreliable -")
    print("  similar to how we can't recall a song from just 1-2 random notes.")
    print()
    
    # Plot results
    fig = plot_noise_robustness(noise_levels, accuracies)
    plt.savefig('../figures/noise_robustness.png', dpi=150, bbox_inches='tight')
    print("Saved figure: noise_robustness.png")
    
    return noise_levels, accuracies

if __name__ == "__main__":
    noise_levels, accuracies = test_noise_robustness(n_trials=20)
