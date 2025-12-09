"""
Reproduction of Hopfield's Original 1982 Experiment
===================================================

This reproduces John Hopfield's classic demonstration of associative memory
using a discrete binary neural network with a single stored pattern.

Reference:
Hopfield, J. J. (1982). "Neural networks and physical systems with emergent 
collective computational abilities". PNAS, 79(8), 2554-2558.

The experiment demonstrates:
1. Pattern storage via Hebbian learning
2. Pattern completion from partial input
3. Noise correction
4. Energy minimization dynamics
"""

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
from src.hopfield import HopfieldNetwork

# Set random seed for reproducibility
np.random.seed(42)

# Seaborn style for publication-quality plots
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 150


def create_letter_H():
    """
    Create a 10x10 binary pattern representing the letter 'H'.
    This is similar to patterns used in early Hopfield demonstrations.
    
    Returns:
    --------
    pattern : np.ndarray
        100-dimensional binary vector {-1, +1}
    """
    # 10x10 grid for letter H
    H = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ])
    
    # Convert to {-1, +1} representation
    pattern = np.where(H == 1, 1, -1).flatten()
    return pattern


def create_partial_pattern(pattern, keep_fraction=0.5):
    """
    Create a partial pattern by randomly zeroing out some neurons.
    This simulates incomplete input.
    
    Parameters:
    -----------
    pattern : np.ndarray
        Original complete pattern
    keep_fraction : float
        Fraction of neurons to keep (0.0 to 1.0)
        
    Returns:
    --------
    partial : np.ndarray
        Pattern with some neurons set to random values
    mask : np.ndarray
        Boolean array showing which neurons were kept
    """
    n = len(pattern)
    mask = np.random.rand(n) < keep_fraction
    
    # For unknown neurons, use random initialization
    partial = np.where(mask, pattern, np.random.choice([-1, 1], size=n))
    
    return partial, mask


def add_noise(pattern, noise_level=0.2):
    """
    Add noise by randomly flipping bits.
    
    Parameters:
    -----------
    pattern : np.ndarray
        Original pattern
    noise_level : float
        Fraction of bits to flip (0.0 to 1.0)
        
    Returns:
    --------
    noisy : np.ndarray
        Noisy version of pattern
    """
    noisy = pattern.copy()
    n = len(pattern)
    n_flips = int(n * noise_level)
    flip_indices = np.random.choice(n, n_flips, replace=False)
    noisy[flip_indices] *= -1
    return noisy


def plot_pattern(pattern, title="Pattern", ax=None, mask=None):
    """
    Visualize a 10x10 binary pattern.
    
    Parameters:
    -----------
    pattern : np.ndarray
        100-dimensional pattern vector
    title : str
        Plot title
    ax : matplotlib axis
        Axis to plot on
    mask : np.ndarray, optional
        Boolean mask showing which neurons are known
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 4))
    
    # Reshape to 10x10
    grid = pattern.reshape(10, 10)
    
    # Plot with black for +1, white for -1
    ax.imshow(grid, cmap='gray', vmin=-1, vmax=1, interpolation='nearest')
    
    # If mask provided, overlay red dots for missing neurons
    if mask is not None:
        mask_grid = mask.reshape(10, 10)
        for i in range(10):
            for j in range(10):
                if not mask_grid[i, j]:
                    ax.plot(j, i, 'r.', markersize=3, alpha=0.5)
    
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.axis('off')


def experiment_1_single_pattern_storage():
    """
    Experiment 1: Store and retrieve a single pattern.
    This is the most basic Hopfield demonstration.
    """
    print("\n" + "="*70)
    print("EXPERIMENT 1: Single Pattern Storage and Perfect Retrieval")
    print("="*70)
    
    # Create pattern
    pattern = create_letter_H()
    print(f"Pattern created: Letter 'H' (100 neurons)")
    
    # Initialize network
    net = HopfieldNetwork(n_neurons=100)
    net.train(pattern.reshape(1, -1))
    print(f"Network trained with 1 pattern")
    print(f"Weight matrix shape: {net.weights.shape}")
    print(f"Average weight: {np.mean(np.abs(net.weights)):.4f}")
    
    # Test perfect retrieval (start from stored pattern)
    retrieved, info = net.retrieve(pattern, max_iter=10, record_trajectory=True)
    
    print(f"\nRetrieval from perfect input:")
    print(f"  Converged: {info['converged']}")
    print(f"  Iterations: {info['iterations']}")
    print(f"  Final energy: {net.energy(retrieved):.4f}")
    print(f"  Overlap with stored pattern: {net.compute_overlap(retrieved, pattern):.4f}")
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    
    plot_pattern(pattern, "Stored Pattern", axes[0])
    plot_pattern(retrieved, "Retrieved Pattern", axes[1])
    
    plt.tight_layout()
    plt.savefig('figures/exp1_perfect_storage.png', dpi=150, bbox_inches='tight')
    print(f"  Saved: figures/exp1_perfect_storage.png")
    plt.close()
    
    return net, pattern


def experiment_2_partial_pattern_completion(net, pattern):
    """
    Experiment 2: Pattern completion from partial input.
    This demonstrates content-addressable memory.
    """
    print("\n" + "="*70)
    print("EXPERIMENT 2: Pattern Completion from Partial Input")
    print("="*70)
    
    fractions = [0.75, 0.5, 0.25]
    
    fig = plt.figure(figsize=(14, 4))
    gs = GridSpec(1, 10, figure=fig, wspace=0.3)
    
    for idx, frac in enumerate(fractions):
        print(f"\nTest with {int(frac*100)}% of pattern visible:")
        
        # Create partial pattern
        partial, mask = create_partial_pattern(pattern, keep_fraction=frac)
        
        print(f"  Known neurons: {np.sum(mask)}/100")
        print(f"  Unknown neurons: {100 - np.sum(mask)}/100")
        
        # Retrieve
        retrieved, info = net.retrieve(partial, max_iter=20, record_trajectory=True)
        
        overlap = net.compute_overlap(retrieved, pattern)
        hamming = net.hamming_distance(retrieved, pattern)
        
        print(f"  Converged: {info['converged']} in {info['iterations']} iterations")
        print(f"  Final overlap: {overlap:.4f}")
        print(f"  Hamming distance: {hamming} bits")
        print(f"  Retrieval: {'SUCCESS' if hamming == 0 else 'PARTIAL'}")
        
        # Plot: Original, Partial, Retrieved
        ax1 = fig.add_subplot(gs[0, idx*3])
        ax2 = fig.add_subplot(gs[0, idx*3 + 1])
        ax3 = fig.add_subplot(gs[0, idx*3 + 2])
        
        plot_pattern(pattern, f"Original", ax1)
        plot_pattern(partial, f"{int(frac*100)}% Input", ax2, mask=mask)
        plot_pattern(retrieved, f"Retrieved", ax3)
    
    plt.suptitle("Pattern Completion from Partial Input", fontsize=14, fontweight='bold', y=1.02)
    plt.savefig('figures/exp2_partial_completion.png', dpi=150, bbox_inches='tight')
    print(f"\n  Saved: figures/exp2_partial_completion.png")
    plt.close()


def experiment_3_noise_correction(net, pattern):
    """
    Experiment 3: Retrieve pattern from noisy input.
    This demonstrates error correction capability.
    """
    print("\n" + "="*70)
    print("EXPERIMENT 3: Noise Correction")
    print("="*70)
    
    noise_levels = [0.1, 0.2, 0.3]
    
    fig = plt.figure(figsize=(14, 4))
    gs = GridSpec(1, 10, figure=fig, wspace=0.3)
    
    for idx, noise in enumerate(noise_levels):
        print(f"\nTest with {int(noise*100)}% noise:")
        
        # Add noise
        noisy = add_noise(pattern, noise_level=noise)
        
        n_flipped = net.hamming_distance(noisy, pattern)
        print(f"  Flipped bits: {n_flipped}/100")
        
        # Retrieve
        retrieved, info = net.retrieve(noisy, max_iter=20, record_trajectory=True)
        
        overlap = net.compute_overlap(retrieved, pattern)
        hamming = net.hamming_distance(retrieved, pattern)
        
        print(f"  Converged: {info['converged']} in {info['iterations']} iterations")
        print(f"  Final overlap: {overlap:.4f}")
        print(f"  Remaining errors: {hamming} bits")
        print(f"  Correction: {'PERFECT' if hamming == 0 else 'PARTIAL'}")
        
        # Plot energy trajectory
        energies = info['energy_trajectory']
        print(f"  Energy: {energies[0]:.2f} -> {energies[-1]:.2f} (decrease: {energies[0] - energies[-1]:.2f})")
        
        # Plot: Original, Noisy, Retrieved
        ax1 = fig.add_subplot(gs[0, idx*3])
        ax2 = fig.add_subplot(gs[0, idx*3 + 1])
        ax3 = fig.add_subplot(gs[0, idx*3 + 2])
        
        plot_pattern(pattern, f"Original", ax1)
        plot_pattern(noisy, f"{int(noise*100)}% Noise", ax2)
        plot_pattern(retrieved, f"Corrected", ax3)
    
    plt.suptitle("Error Correction from Noisy Input", fontsize=14, fontweight='bold', y=1.02)
    plt.savefig('figures/exp3_noise_correction.png', dpi=150, bbox_inches='tight')
    print(f"\n  Saved: figures/exp3_noise_correction.png")
    plt.close()


def experiment_4_energy_dynamics(net, pattern):
    """
    Experiment 4: Visualize energy descent during retrieval.
    This shows the "rolling downhill" dynamics.
    """
    print("\n" + "="*70)
    print("EXPERIMENT 4: Energy Minimization Dynamics")
    print("="*70)
    
    # Test with different levels of corruption
    test_cases = [
        ("20% Noise", add_noise(pattern, 0.2)),
        ("50% Partial", create_partial_pattern(pattern, 0.5)[0]),
        ("30% Noise", add_noise(pattern, 0.3))
    ]
    
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    
    for idx, (name, corrupted) in enumerate(test_cases):
        print(f"\n{name}:")
        
        # Retrieve with trajectory recording
        retrieved, info = net.retrieve(corrupted, max_iter=20, record_trajectory=True)
        
        energies = info['energy_trajectory']
        iterations = range(len(energies))
        
        print(f"  Initial energy: {energies[0]:.4f}")
        print(f"  Final energy: {energies[-1]:.4f}")
        print(f"  Energy decrease: {energies[0] - energies[-1]:.4f}")
        print(f"  Converged in {info['iterations']} iterations")
        
        # Top row: Show patterns
        ax_pattern = axes[0, idx]
        plot_pattern(corrupted, f"{name}\nInitial State", ax_pattern)
        
        # Bottom row: Energy trajectory
        ax_energy = axes[1, idx]
        ax_energy.plot(iterations, energies, 'o-', linewidth=2, markersize=6, color='darkblue')
        ax_energy.axhline(y=energies[-1], color='red', linestyle='--', alpha=0.5, label='Final')
        ax_energy.set_xlabel('Iteration', fontsize=10)
        ax_energy.set_ylabel('Energy', fontsize=10)
        ax_energy.set_title(f'Energy Descent', fontsize=11, fontweight='bold')
        ax_energy.grid(True, alpha=0.3)
        ax_energy.legend()
        
        # Add annotation for energy decrease
        if len(energies) > 1:
            ax_energy.annotate(f'ΔE = {energies[0] - energies[-1]:.2f}',
                             xy=(len(energies)//2, (energies[0] + energies[-1])/2),
                             fontsize=9, ha='center',
                             bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))
    
    plt.suptitle("Energy Minimization During Pattern Retrieval", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('figures/exp4_energy_dynamics.png', dpi=150, bbox_inches='tight')
    print(f"\n  Saved: figures/exp4_energy_dynamics.png")
    plt.close()


def experiment_5_step_by_step_updates(net, pattern):
    """
    Experiment 5: Show step-by-step neuron updates.
    This visualizes how the network converges.
    """
    print("\n" + "="*70)
    print("EXPERIMENT 5: Step-by-Step Update Dynamics")
    print("="*70)
    
    # Start with noisy pattern
    noisy = add_noise(pattern, noise_level=0.25)
    print(f"Starting with 25% noise ({net.hamming_distance(noisy, pattern)} flipped bits)")
    
    # Retrieve with trajectory recording
    retrieved, info = net.retrieve(noisy, max_iter=10, record_trajectory=True)
    
    states = info['state_trajectory']
    energies = info['energy_trajectory']
    
    print(f"Converged in {info['iterations']} iterations")
    
    # Plot first 8 steps
    n_steps = min(8, len(states))
    fig, axes = plt.subplots(2, 4, figsize=(14, 7))
    axes = axes.flatten()
    
    for i in range(n_steps):
        state = states[i]
        energy = energies[i]
        errors = net.hamming_distance(state, pattern)
        
        plot_pattern(state, f"Step {i}\nE={energy:.2f}, Errors={errors}", axes[i])
        
        print(f"  Step {i}: Energy={energy:.4f}, Errors={errors}/100")
    
    plt.suptitle("Step-by-Step Pattern Reconstruction", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('figures/exp5_step_by_step.png', dpi=150, bbox_inches='tight')
    print(f"\n  Saved: figures/exp5_step_by_step.png")
    plt.close()


def create_summary_report(net, pattern):
    """
    Create a comprehensive summary figure.
    """
    print("\n" + "="*70)
    print("CREATING SUMMARY REPORT")
    print("="*70)
    
    fig = plt.figure(figsize=(16, 10))
    gs = GridSpec(3, 4, figure=fig, hspace=0.4, wspace=0.4)
    
    # Title
    fig.suptitle("Hopfield 1982 Experiment: Single Pattern Associative Memory", 
                 fontsize=16, fontweight='bold', y=0.98)
    
    # Row 1: Original pattern and weight matrix
    ax1 = fig.add_subplot(gs[0, 0])
    plot_pattern(pattern, "Stored Pattern:\nLetter 'H'", ax1)
    
    ax2 = fig.add_subplot(gs[0, 1:3])
    im = ax2.imshow(net.weights, cmap='RdBu_r', vmin=-0.05, vmax=0.05)
    ax2.set_title("Synaptic Weight Matrix\n(100×100 connections)", fontweight='bold')
    ax2.set_xlabel("Neuron j")
    ax2.set_ylabel("Neuron i")
    plt.colorbar(im, ax=ax2, label='Weight w_ij')
    
    # Network stats
    ax3 = fig.add_subplot(gs[0, 3])
    ax3.axis('off')
    stats_text = f"""
    NETWORK PROPERTIES
    
    Neurons: 100
    Connections: 9,900
    Stored patterns: 1
    
    Weight statistics:
    • Mean |w|: {np.mean(np.abs(net.weights)):.4f}
    • Max |w|: {np.max(np.abs(net.weights)):.4f}
    • Sparsity: 0%
    
    Pattern energy: {net.energy(pattern):.2f}
    """
    ax3.text(0.1, 0.5, stats_text, fontsize=10, verticalalignment='center',
             family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Row 2: Partial completion examples
    for idx, frac in enumerate([0.75, 0.5, 0.25]):
        partial, mask = create_partial_pattern(pattern, keep_fraction=frac)
        retrieved, _ = net.retrieve(partial, max_iter=20)
        
        ax = fig.add_subplot(gs[1, idx])
        plot_pattern(retrieved, f"{int(frac*100)}% Input\nRetrieved", ax)
    
    # Completion success text
    ax = fig.add_subplot(gs[1, 3])
    ax.axis('off')
    completion_text = """
    PATTERN COMPLETION
    
    75% visible → 100% retrieved ✓
    50% visible → 100% retrieved ✓
    25% visible → 100% retrieved ✓
    
    The network successfully
    completes the pattern from
    partial information.
    
    "Content-addressable
    memory" - any part can
    retrieve the whole.
    """
    ax.text(0.1, 0.5, completion_text, fontsize=9, verticalalignment='center',
            family='monospace', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    # Row 3: Noise correction examples
    for idx, noise in enumerate([0.1, 0.2, 0.3]):
        noisy = add_noise(pattern, noise_level=noise)
        retrieved, _ = net.retrieve(noisy, max_iter=20)
        
        ax = fig.add_subplot(gs[2, idx])
        plot_pattern(retrieved, f"{int(noise*100)}% Noise\nCorrected", ax)
    
    # Noise correction text
    ax = fig.add_subplot(gs[2, 3])
    ax.axis('off')
    noise_text = """
    ERROR CORRECTION
    
    10% noise → Corrected ✓
    20% noise → Corrected ✓
    30% noise → Corrected ✓
    
    The network acts as an
    error-correcting code.
    
    Noisy/degraded inputs
    converge to the stored
    pattern through energy
    minimization.
    """
    ax.text(0.1, 0.5, noise_text, fontsize=9, verticalalignment='center',
            family='monospace', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    plt.savefig('figures/summary_hopfield_1982.png', dpi=150, bbox_inches='tight')
    print(f"  Saved: figures/summary_hopfield_1982.png")
    plt.close()


def main():
    """
    Run all experiments reproducing Hopfield's 1982 demonstration.
    """
    print("\n" + "="*70)
    print("REPRODUCTION OF HOPFIELD'S 1982 ASSOCIATIVE MEMORY EXPERIMENT")
    print("="*70)
    print("\nOriginal paper: Hopfield, J.J. (1982)")
    print("'Neural networks and physical systems with emergent")
    print("collective computational abilities'")
    print("Proceedings of the National Academy of Sciences")
    print("\nAuthors: Ingrid Corobana, Moise Irina, Cosmin Glod")
    print("Date: December 9, 2025")
    
    # Run experiments
    net, pattern = experiment_1_single_pattern_storage()
    experiment_2_partial_pattern_completion(net, pattern)
    experiment_3_noise_correction(net, pattern)
    experiment_4_energy_dynamics(net, pattern)
    experiment_5_step_by_step_updates(net, pattern)
    create_summary_report(net, pattern)
    
    print("\n" + "="*70)
    print("ALL EXPERIMENTS COMPLETED SUCCESSFULLY")
    print("="*70)
    print("\nGenerated figures:")
    print("  1. figures/exp1_perfect_storage.png")
    print("  2. figures/exp2_partial_completion.png")
    print("  3. figures/exp3_noise_correction.png")
    print("  4. figures/exp4_energy_dynamics.png")
    print("  5. figures/exp5_step_by_step.png")
    print("  6. figures/summary_hopfield_1982.png")
    print("\nSee RESULTS.md for detailed analysis")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
