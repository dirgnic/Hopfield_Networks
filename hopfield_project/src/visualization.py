"""
Visualization Tools
===================
Functions for plotting patterns, energy landscapes, and network dynamics.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import List, Tuple, Optional
import seaborn as sns


def plot_pattern(pattern: np.ndarray, shape: Tuple[int, int], title: str = "", ax=None):
    """
    Display a single pattern as an image.
    
    Parameters:
    -----------
    pattern : np.ndarray
        Flat pattern vector with values in {-1, +1}
    shape : Tuple[int, int]
        Image dimensions (height, width)
    title : str
        Title for the plot
    ax : matplotlib axis, optional
        Axis to plot on
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 4))
    
    image = pattern.reshape(shape)
    ax.imshow(image, cmap='gray', vmin=-1, vmax=1, interpolation='nearest')
    ax.set_title(title)
    ax.axis('off')


def plot_retrieval_sequence(original: np.ndarray, 
                            noisy: np.ndarray, 
                            retrieved: np.ndarray,
                            shape: Tuple[int, int],
                            hamming_original: int = None,
                            hamming_retrieved: int = None):
    """
    Show the retrieval process: original → noisy → retrieved.
    
    This visualizes the "memory recall" analogy: given a partial/noisy input,
    the network fills in the missing information.
    
    Parameters:
    -----------
    original : np.ndarray
        Original stored pattern
    noisy : np.ndarray
        Corrupted input pattern
    retrieved : np.ndarray
        Pattern after network convergence
    shape : Tuple[int, int]
        Image dimensions
    hamming_original : int, optional
        Hamming distance between noisy and original
    hamming_retrieved : int, optional
        Hamming distance between retrieved and original
    """
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    plot_pattern(original, shape, "Original Pattern", ax=axes[0])
    
    title_noisy = "Noisy Input"
    if hamming_original is not None:
        title_noisy += f"\n({hamming_original} bits different)"
    plot_pattern(noisy, shape, title_noisy, ax=axes[1])
    
    title_retrieved = "Retrieved Pattern"
    if hamming_retrieved is not None:
        title_retrieved += f"\n({hamming_retrieved} bits different)"
    plot_pattern(retrieved, shape, title_retrieved, ax=axes[2])
    
    plt.tight_layout()
    return fig


def plot_energy_trajectory(energy_history: List[float], 
                           title: str = "Energy During Retrieval"):
    """
    Plot energy vs iteration, showing the "rolling downhill" process.
    
    Brain/Physics Analogy:
    ----------------------
    Energy decreases over time as the system settles into a stable
    memory state (local minimum in the energy landscape).
    
    Parameters:
    -----------
    energy_history : List[float]
        Energy values recorded during retrieval
    title : str
        Plot title
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    
    ax.plot(energy_history, 'o-', linewidth=2, markersize=6)
    ax.set_xlabel('Iteration', fontsize=12)
    ax.set_ylabel('Energy', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3)
    
    # Annotate initial and final energy
    ax.annotate(f'Initial: {energy_history[0]:.1f}', 
                xy=(0, energy_history[0]), 
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle='round', fc='yellow', alpha=0.5))
    ax.annotate(f'Final: {energy_history[-1]:.1f}', 
                xy=(len(energy_history)-1, energy_history[-1]), 
                xytext=(10, -20), textcoords='offset points',
                bbox=dict(boxstyle='round', fc='lightgreen', alpha=0.5))
    
    plt.tight_layout()
    return fig


def plot_weight_matrix(weights: np.ndarray, title: str = "Synaptic Weights"):
    """
    Visualize the weight matrix (synaptic connections).
    
    Brain Analogy:
    --------------
    This shows the "wiring diagram" of the network - which neurons
    have strong positive or negative connections.
    
    Parameters:
    -----------
    weights : np.ndarray
        Weight matrix (n_neurons, n_neurons)
    title : str
        Plot title
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    im = ax.imshow(weights, cmap='RdBu_r', aspect='auto')
    ax.set_title(title, fontsize=14)
    ax.set_xlabel('Neuron j', fontsize=12)
    ax.set_ylabel('Neuron i', fontsize=12)
    
    plt.colorbar(im, ax=ax, label='Weight w_ij')
    plt.tight_layout()
    return fig


def plot_pattern_similarity_matrix(similarity: np.ndarray, 
                                   pattern_names: Optional[List[str]] = None):
    """
    Plot pairwise similarity (overlap) between stored patterns.
    
    EDA Insight:
    ------------
    High similarity between patterns → energy valleys overlap → 
    network struggles to distinguish them (capacity limitation).
    
    Parameters:
    -----------
    similarity : np.ndarray
        Similarity matrix from compute_pattern_similarity_matrix
    pattern_names : List[str], optional
        Names for patterns (e.g., ['A', 'B', 'C'])
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    
    sns.heatmap(similarity, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, vmin=-1, vmax=1, square=True, ax=ax,
                xticklabels=pattern_names, yticklabels=pattern_names)
    
    ax.set_title('Pattern Similarity Matrix\n(Normalized Overlap)', fontsize=14)
    plt.tight_layout()
    return fig


def plot_capacity_experiment(n_patterns_list: List[int], 
                            accuracy_list: List[float],
                            theoretical_capacity: Optional[float] = None):
    """
    Plot retrieval accuracy vs number of stored patterns.
    
    Shows the network's capacity limitation: performance degrades
    when too many patterns are stored (valleys merge).
    
    Parameters:
    -----------
    n_patterns_list : List[int]
        Number of patterns stored in each experiment
    accuracy_list : List[float]
        Corresponding retrieval accuracy
    theoretical_capacity : float, optional
        Theoretical capacity (0.138 * N for random patterns)
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(n_patterns_list, accuracy_list, 'o-', linewidth=2, markersize=8, label='Measured')
    
    if theoretical_capacity is not None:
        ax.axvline(theoretical_capacity, color='red', linestyle='--', linewidth=2,
                  label=f'Theoretical capacity ≈ {theoretical_capacity:.0f}')
    
    ax.set_xlabel('Number of Stored Patterns', fontsize=12)
    ax.set_ylabel('Retrieval Accuracy', fontsize=12)
    ax.set_title('Network Capacity: Accuracy vs Number of Patterns', fontsize=14)
    ax.set_ylim([0, 1.1])
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    return fig


def plot_noise_robustness(noise_levels: List[float], 
                         accuracy_list: List[float]):
    """
    Plot retrieval accuracy vs noise level.
    
    Shows how much corruption the network can tolerate before
    failing to recover the original memory.
    
    Parameters:
    -----------
    noise_levels : List[float]
        Noise levels tested (fraction of bits flipped)
    accuracy_list : List[float]
        Corresponding retrieval accuracy
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(np.array(noise_levels) * 100, accuracy_list, 'o-', 
           linewidth=2, markersize=8, color='steelblue')
    
    ax.set_xlabel('Noise Level (%)', fontsize=12)
    ax.set_ylabel('Retrieval Accuracy', fontsize=12)
    ax.set_title('Noise Robustness: How Much Corruption Can the Network Handle?', fontsize=14)
    ax.set_ylim([0, 1.1])
    ax.grid(True, alpha=0.3)
    
    # Add shaded regions
    ax.axhspan(0.9, 1.1, alpha=0.2, color='green', label='Excellent retrieval')
    ax.axhspan(0.5, 0.9, alpha=0.2, color='yellow', label='Partial retrieval')
    ax.axhspan(0, 0.5, alpha=0.2, color='red', label='Poor retrieval')
    
    ax.legend(fontsize=10)
    plt.tight_layout()
    return fig


def plot_multiple_patterns(patterns: np.ndarray, 
                          shape: Tuple[int, int],
                          titles: Optional[List[str]] = None,
                          n_cols: int = 5):
    """
    Display multiple patterns in a grid.
    
    Parameters:
    -----------
    patterns : np.ndarray
        Array of patterns (n_patterns, n_neurons)
    shape : Tuple[int, int]
        Image dimensions for each pattern
    titles : List[str], optional
        Title for each pattern
    n_cols : int
        Number of columns in grid
    """
    n_patterns = patterns.shape[0]
    n_rows = (n_patterns + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(2*n_cols, 2*n_rows))
    axes = axes.flatten() if n_patterns > 1 else [axes]
    
    for i in range(n_patterns):
        title = titles[i] if titles is not None else f"Pattern {i+1}"
        plot_pattern(patterns[i], shape, title, ax=axes[i])
    
    # Hide unused subplots
    for i in range(n_patterns, len(axes)):
        axes[i].axis('off')
    
    plt.tight_layout()
    return fig


def animate_retrieval(state_trajectory: List[np.ndarray],
                     shape: Tuple[int, int],
                     energy_trajectory: Optional[List[float]] = None,
                     save_path: Optional[str] = None) -> FuncAnimation:
    """
    Create animation showing network dynamics during retrieval.
    
    Visualizes the "rolling downhill" process in real-time.
    
    Parameters:
    -----------
    state_trajectory : List[np.ndarray]
        Sequence of states during retrieval
    shape : Tuple[int, int]
        Image dimensions
    energy_trajectory : List[float], optional
        Corresponding energy values
    save_path : str, optional
        Path to save animation (e.g., 'retrieval.gif')
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Setup image plot
    img = axes[0].imshow(state_trajectory[0].reshape(shape), 
                         cmap='gray', vmin=-1, vmax=1, interpolation='nearest')
    axes[0].set_title('Network State')
    axes[0].axis('off')
    
    # Setup energy plot
    if energy_trajectory is not None:
        line, = axes[1].plot([], [], 'o-', linewidth=2, markersize=6)
        axes[1].set_xlim(0, len(energy_trajectory))
        axes[1].set_ylim(min(energy_trajectory) * 1.1, max(energy_trajectory) * 1.1)
        axes[1].set_xlabel('Iteration')
        axes[1].set_ylabel('Energy')
        axes[1].set_title('Energy Minimization')
        axes[1].grid(True, alpha=0.3)
    
    def update(frame):
        img.set_data(state_trajectory[frame].reshape(shape))
        if energy_trajectory is not None:
            line.set_data(range(frame + 1), energy_trajectory[:frame + 1])
        return img, line if energy_trajectory else img,
    
    anim = FuncAnimation(fig, update, frames=len(state_trajectory), 
                        interval=200, blit=True, repeat=True)
    
    if save_path:
        anim.save(save_path, writer='pillow', fps=5)
    
    plt.tight_layout()
    return anim


def plot_energy_landscape_2d(hopfield_net, patterns: np.ndarray, shape: Tuple[int, int]):
    """
    Attempt to visualize energy landscape using PCA projection to 2D.
    
    This is a conceptual visualization - the actual landscape is high-dimensional.
    
    Parameters:
    -----------
    hopfield_net : HopfieldNetwork
        Trained network
    patterns : np.ndarray
        Stored patterns
    shape : Tuple[int, int]
        Pattern dimensions (for insets)
    """
    from sklearn.decomposition import PCA
    
    # Sample random states
    n_samples = 1000
    states = np.random.choice([-1, 1], size=(n_samples, hopfield_net.n_neurons))
    
    # Compute energies
    energies = np.array([hopfield_net.energy(state) for state in states])
    
    # Project to 2D using PCA
    pca = PCA(n_components=2)
    states_2d = pca.fit_transform(states)
    patterns_2d = pca.transform(patterns)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 8))
    
    scatter = ax.scatter(states_2d[:, 0], states_2d[:, 1], 
                        c=energies, cmap='viridis', alpha=0.5, s=20)
    ax.scatter(patterns_2d[:, 0], patterns_2d[:, 1], 
              c='red', s=200, marker='*', edgecolors='black', linewidths=2,
              label='Stored Patterns (Energy Minima)')
    
    ax.set_xlabel('PCA Component 1', fontsize=12)
    ax.set_ylabel('PCA Component 2', fontsize=12)
    ax.set_title('Energy Landscape (PCA Projection)\nRed stars = stored memories in energy valleys', 
                fontsize=14)
    ax.legend(fontsize=11)
    
    plt.colorbar(scatter, ax=ax, label='Energy')
    plt.tight_layout()
    return fig
