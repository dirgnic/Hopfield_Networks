"""
Quick Demo Script
=================
Demonstrates all components of the Hopfield network project.
"""

import sys
sys.path.append('.')

import numpy as np
import matplotlib.pyplot as plt
from src.hopfield import HopfieldNetwork
from src.patterns import generate_letters, compute_pattern_similarity_matrix
from src.visualization import (plot_retrieval_sequence, plot_energy_trajectory,
                                plot_multiple_patterns, plot_pattern_similarity_matrix)

def main():
    print("=" * 70)
    print(" " * 15 + "HOPFIELD NETWORK DEMONSTRATION")
    print(" " * 10 + "A Brain-Inspired Model for Associative Memory")
    print("=" * 70)
    print()
    
    # 1. Generate patterns
    print("1. GENERATING PATTERNS")
    print("-" * 70)
    patterns = generate_letters(['A', 'B', 'C'], size=10)
    print(f"   Created {len(patterns)} letter patterns (10x10 = 100 neurons each)")
    print()
    
    # Visualize patterns
    fig = plot_multiple_patterns(patterns, (10, 10), 
                                titles=['Letter A', 'Letter B', 'Letter C'],
                                n_cols=3)
    plt.savefig('figures/demo_patterns.png', dpi=150, bbox_inches='tight')
    print("   ✓ Saved: figures/demo_patterns.png")
    plt.close()
    
    # 2. Compute similarity
    print()
    print("2. EXPLORATORY DATA ANALYSIS")
    print("-" * 70)
    similarity = compute_pattern_similarity_matrix(patterns)
    print("   Pattern Similarity Matrix (normalized overlap):")
    print("   ", similarity)
    print()
    print("   Interpretation: Low similarity → patterns are distinct")
    print("                   → easier to store without interference")
    print()
    
    fig = plot_pattern_similarity_matrix(similarity, ['A', 'B', 'C'])
    plt.savefig('figures/demo_similarity.png', dpi=150, bbox_inches='tight')
    print("   ✓ Saved: figures/demo_similarity.png")
    plt.close()
    
    # 3. Train network
    print()
    print("3. TRAINING NETWORK (HEBBIAN LEARNING)")
    print("-" * 70)
    hopfield = HopfieldNetwork(n_neurons=100)
    hopfield.train(patterns)
    print(f"   Network trained with {hopfield.weights.shape[0]}x{hopfield.weights.shape[1]} weight matrix")
    print(f"   Average synaptic strength: {np.mean(np.abs(hopfield.weights)):.4f}")
    print()
    print("   Brain Analogy: 'Neurons that fire together, wire together'")
    print("   → Synapses strengthen for co-active neurons across patterns")
    print()
    
    # 4. Test retrieval
    print()
    print("4. MEMORY RETRIEVAL TEST")
    print("-" * 70)
    
    # Test with Letter A
    original = patterns[0]
    noise_level = 0.25
    noisy = hopfield.add_noise(original, noise_level=noise_level)
    
    print(f"   Adding {int(noise_level*100)}% noise to Letter A...")
    hamming_before = hopfield.hamming_distance(noisy, original)
    print(f"   → {hamming_before} bits flipped (out of 100)")
    print()
    
    print("   Running network dynamics (energy minimization)...")
    retrieved, info = hopfield.retrieve(noisy, max_iter=50, record_trajectory=True)
    
    hamming_after = hopfield.hamming_distance(retrieved, original)
    success = np.array_equal(retrieved, original)
    
    print(f"   → Converged in {info['iterations']} iterations")
    print(f"   → Final Hamming distance: {hamming_after}")
    print(f"   → Retrieval: {'SUCCESS ✓' if success else 'FAILED ✗'}")
    print()
    
    if success:
        print("   Brain Analogy: Like hearing a few notes and recalling the whole song!")
        print("   → Network 'filled in' the missing/corrupted information")
    print()
    
    # Visualize retrieval
    fig = plot_retrieval_sequence(original, noisy, retrieved, (10, 10),
                                  hamming_before, hamming_after)
    fig.suptitle(f"Memory Retrieval: Letter A with {int(noise_level*100)}% Noise", 
                fontsize=14, y=1.02)
    plt.savefig('figures/demo_retrieval.png', dpi=150, bbox_inches='tight')
    print("   ✓ Saved: figures/demo_retrieval.png")
    plt.close()
    
    # Plot energy
    fig = plot_energy_trajectory(info['energy_trajectory'], 
                                "Energy Landscape: Rolling Downhill to Memory")
    plt.savefig('figures/demo_energy.png', dpi=150, bbox_inches='tight')
    print("   ✓ Saved: figures/demo_energy.png")
    plt.close()
    
    # 5. Summary
    print()
    print("=" * 70)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 70)
    print()
    print("Key Takeaways:")
    print("  1. Simple binary neurons + Hebbian learning = associative memory")
    print("  2. Energy minimization drives retrieval (rolling downhill)")
    print("  3. Network can recall complete memories from partial cues")
    print("  4. All inspired by brain dynamics and protein folding!")
    print()
    print("Next Steps:")
    print("  → Run experiments/capacity_test.py for capacity analysis")
    print("  → Run experiments/noise_robustness.py for noise tolerance")
    print("  → Run experiments/spurious_attractors.py for false memories")
    print()
    print("See figures/ directory for all generated plots!")
    print()

if __name__ == "__main__":
    main()
