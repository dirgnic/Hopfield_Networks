"""
Spurious Attractors Experiment
==============================
Detect and visualize spurious attractors (false memories).
"""

import sys
sys.path.append('..')

import numpy as np
import matplotlib.pyplot as plt
from src.hopfield import HopfieldNetwork
from src.patterns import generate_letters, compute_pattern_similarity_matrix
from src.visualization import plot_multiple_patterns, plot_pattern_similarity_matrix

# Set random seed
np.random.seed(42)

def find_spurious_attractors():
    """
    Store many patterns and search for spurious attractors.
    
    Spurious attractors are stable states that weren't explicitly stored.
    They emerge from interference between stored patterns.
    """
    print("=" * 60)
    print("HOPFIELD NETWORK: SPURIOUS ATTRACTORS EXPERIMENT")
    print("=" * 60)
    print()
    
    # Generate patterns (store more than capacity to induce spurious states)
    print("Generating patterns...")
    patterns = generate_letters(['A', 'B', 'C', 'D', 'E'], size=10)
    n_neurons = patterns.shape[1]
    
    print(f"Stored {patterns.shape[0]} patterns ({patterns.shape[1]} neurons)")
    print(f"Theoretical capacity: ~{int(0.138 * n_neurons)} patterns")
    print("(We're near/above capacity, so spurious attractors likely)")
    print()
    
    # Train network
    print("Training network...")
    hopfield = HopfieldNetwork(n_neurons)
    hopfield.train(patterns)
    print()
    
    # Analyze pattern similarity
    print("Computing pattern similarity...")
    similarity = compute_pattern_similarity_matrix(patterns)
    print("Pattern similarity matrix:")
    print(similarity)
    print()
    
    # Search for spurious attractors
    print("Searching for spurious attractors (100 random initializations)...")
    spurious = hopfield.check_spurious_attractors(n_tests=100)
    print(f"Found {len(spurious)} spurious attractors")
    print()
    
    if len(spurious) > 0:
        print("=" * 60)
        print("ANALYSIS OF SPURIOUS ATTRACTORS:")
        print("=" * 60)
        
        for i, sp in enumerate(spurious[:5]):  # Show first 5
            print(f"\nSpurious Attractor {i+1}:")
            
            # Compute overlap with each stored pattern
            overlaps = [hopfield.compute_overlap(sp, p) for p in patterns]
            print(f"  Overlaps with stored patterns: {[f'{o:.2f}' for o in overlaps]}")
            
            # Find which patterns it's closest to
            max_overlap_idx = np.argmax(np.abs(overlaps))
            print(f"  Closest to pattern {max_overlap_idx+1} (overlap: {overlaps[max_overlap_idx]:.2f})")
            
            # Compute energy
            energy = hopfield.energy(sp)
            stored_energies = [hopfield.energy(p) for p in patterns]
            print(f"  Energy: {energy:.2f}")
            print(f"  Stored pattern energies: {[f'{e:.2f}' for e in stored_energies]}")
        
        print()
        print("Brain Analogy:")
        print("  Spurious attractors are like 'false memories' or confabulations.")
        print("  The brain creates stable but incorrect memories by blending")
        print("  real experiences. In Hopfield networks, these emerge when")
        print("  too many patterns are stored - the energy landscape creates")
        print("  unexpected valleys that weren't explicitly programmed.")
        print()
        
        # Visualize stored patterns
        fig = plot_multiple_patterns(patterns, (10, 10), 
                                     titles=[f'Stored {chr(65+i)}' for i in range(len(patterns))],
                                     n_cols=5)
        fig.suptitle("Stored Patterns", fontsize=16, y=1.02)
        plt.savefig('../figures/stored_patterns.png', dpi=150, bbox_inches='tight')
        print("Saved figure: stored_patterns.png")
        
        # Visualize spurious attractors
        if len(spurious) > 0:
            spurious_array = np.array(spurious[:min(5, len(spurious))])
            fig = plot_multiple_patterns(spurious_array, (10, 10),
                                        titles=[f'Spurious {i+1}' for i in range(len(spurious_array))],
                                        n_cols=5)
            fig.suptitle("Spurious Attractors (False Memories)", fontsize=16, y=1.02)
            plt.savefig('../figures/spurious_attractors.png', dpi=150, bbox_inches='tight')
            print("Saved figure: spurious_attractors.png")
        
        # Plot similarity matrix
        fig = plot_pattern_similarity_matrix(similarity, 
                                            pattern_names=[chr(65+i) for i in range(len(patterns))])
        plt.savefig('../figures/pattern_similarity.png', dpi=150, bbox_inches='tight')
        print("Saved figure: pattern_similarity.png")
        
    else:
        print("No spurious attractors found! Network is operating below capacity.")
    
    print()
    print("=" * 60)
    print("EXPERIMENT COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    find_spurious_attractors()
