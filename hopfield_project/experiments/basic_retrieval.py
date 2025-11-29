"""
Basic Retrieval Experiment
==========================
Demonstrate core memory retrieval with letters.
"""

import sys
sys.path.append('..')

import numpy as np
import matplotlib.pyplot as plt
from src.hopfield import HopfieldNetwork
from src.patterns import generate_letters
from src.visualization import plot_retrieval_sequence, plot_energy_trajectory

# Set random seed for reproducibility
np.random.seed(42)

def main():
    print("=" * 60)
    print("HOPFIELD NETWORK: BASIC RETRIEVAL EXPERIMENT")
    print("=" * 60)
    print()
    
    # Step 1: Generate patterns
    print("Step 1: Generating letter patterns (A, B, C)...")
    patterns = generate_letters(['A', 'B', 'C'], size=10)
    print(f"  Created {patterns.shape[0]} patterns, each with {patterns.shape[1]} neurons")
    print()
    
    # Step 2: Create and train network
    print("Step 2: Training Hopfield network (Hebbian learning)...")
    hopfield = HopfieldNetwork(n_neurons=100)
    hopfield.train(patterns)
    print(f"  Network trained with weight matrix: {hopfield.weights.shape}")
    print(f"  Average synaptic weight: {np.mean(np.abs(hopfield.weights)):.4f}")
    print()
    
    # Step 3: Test retrieval with noise
    noise_levels = [0.1, 0.2, 0.3]
    
    for i, noise_level in enumerate(noise_levels):
        print(f"Step 3.{i+1}: Testing retrieval with {int(noise_level*100)}% noise...")
        
        # Choose pattern A
        original = patterns[0]
        noisy = hopfield.add_noise(original, noise_level=noise_level)
        
        # Retrieve
        retrieved, info = hopfield.retrieve(noisy, max_iter=50, record_trajectory=True)
        
        # Compute metrics
        hamming_original = hopfield.hamming_distance(noisy, original)
        hamming_retrieved = hopfield.hamming_distance(retrieved, original)
        success = np.array_equal(retrieved, original)
        
        print(f"  Noisy pattern: {hamming_original} bits different from original")
        print(f"  Retrieved pattern: {hamming_retrieved} bits different from original")
        print(f"  Converged in {info['iterations']} iterations")
        print(f"  Retrieval {'SUCCESS' if success else 'FAILED'}")
        print()
        
        # Plot retrieval
        fig = plot_retrieval_sequence(original, noisy, retrieved, (10, 10),
                                     hamming_original, hamming_retrieved)
        fig.suptitle(f"Retrieval with {int(noise_level*100)}% Noise - Letter A", 
                    fontsize=16, y=1.02)
        plt.savefig(f'../figures/retrieval_noise_{int(noise_level*100)}.png', 
                   dpi=150, bbox_inches='tight')
        print(f"  Saved figure: retrieval_noise_{int(noise_level*100)}.png")
        
        # Plot energy trajectory
        fig_energy = plot_energy_trajectory(info['energy_trajectory'],
                                           f"Energy Minimization ({int(noise_level*100)}% Noise)")
        plt.savefig(f'../figures/energy_noise_{int(noise_level*100)}.png', 
                   dpi=150, bbox_inches='tight')
        print(f"  Saved figure: energy_noise_{int(noise_level*100)}.png")
        print()
    
    print("=" * 60)
    print("EXPERIMENT COMPLETE!")
    print("=" * 60)
    print()
    print("Brain Analogy Summary:")
    print("  - Stored patterns = familiar memories (stable brain states)")
    print("  - Noisy input = partial/corrupted sensory information")
    print("  - Retrieval = brain 'filling in' missing details")
    print("  - Energy decrease = system settling into stable configuration")
    print()

if __name__ == "__main__":
    main()
