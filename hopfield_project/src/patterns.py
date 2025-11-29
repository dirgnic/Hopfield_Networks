"""
Pattern Generation Utilities
============================
Tools for creating and manipulating binary patterns for Hopfield networks.
"""

import numpy as np
from typing import List, Tuple


def generate_letters(letters: List[str], size: int = 10) -> np.ndarray:
    """
    Generate simple binary representations of letters.
    
    Parameters:
    -----------
    letters : List[str]
        List of letters to generate (e.g., ['A', 'B', 'C'])
    size : int
        Grid size (creates size x size images)
        
    Returns:
    --------
    patterns : np.ndarray
        Array of shape (n_letters, size*size) with values in {-1, +1}
    """
    patterns = []
    
    # Simple 10x10 patterns for common letters
    letter_templates = {
        'A': [
            [0,0,0,1,1,1,1,0,0,0],
            [0,0,1,1,0,0,1,1,0,0],
            [0,1,1,0,0,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,1,0],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,1,1],
        ],
        'B': [
            [1,1,1,1,1,1,1,1,0,0],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,1,1,1,1,1,1,0,0],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,1,1,1,1,1,1,0,0],
        ],
        'C': [
            [0,0,1,1,1,1,1,1,0,0],
            [0,1,1,0,0,0,0,1,1,0],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,1,1],
            [0,1,1,0,0,0,0,1,1,0],
            [0,0,1,1,1,1,1,1,0,0],
        ],
        'D': [
            [1,1,1,1,1,1,1,0,0,0],
            [1,1,0,0,0,0,1,1,0,0],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,1,1,0],
            [1,1,0,0,0,0,1,1,0,0],
            [1,1,1,1,1,1,1,0,0,0],
        ],
        'E': [
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1],
        ],
    }
    
    for letter in letters:
        if letter.upper() in letter_templates:
            pattern = np.array(letter_templates[letter.upper()]).flatten()
            # Convert to {-1, +1}
            pattern = 2 * pattern - 1
            patterns.append(pattern)
        else:
            # Generate random pattern for unknown letters
            pattern = np.random.choice([-1, 1], size=size*size)
            patterns.append(pattern)
    
    return np.array(patterns)


def generate_random_patterns(n_patterns: int, n_neurons: int, density: float = 0.5) -> np.ndarray:
    """
    Generate random binary patterns.
    
    Parameters:
    -----------
    n_patterns : int
        Number of patterns to generate
    n_neurons : int
        Number of neurons (pattern length)
    density : float
        Fraction of +1 bits (default 0.5 for balanced patterns)
        
    Returns:
    --------
    patterns : np.ndarray
        Array of shape (n_patterns, n_neurons) with values in {-1, +1}
    """
    patterns = np.random.choice([-1, 1], size=(n_patterns, n_neurons), 
                                p=[1-density, density])
    return patterns


def generate_correlated_patterns(n_patterns: int, n_neurons: int, correlation: float = 0.3) -> np.ndarray:
    """
    Generate patterns with controlled correlation.
    
    Higher correlation → patterns are more similar → harder to store distinctly.
    
    Parameters:
    -----------
    n_patterns : int
        Number of patterns
    n_neurons : int
        Pattern length
    correlation : float
        Correlation level (0 = independent, 1 = identical)
        
    Returns:
    --------
    patterns : np.ndarray
        Correlated patterns
    """
    # Start with base pattern
    base = np.random.choice([-1, 1], size=n_neurons)
    patterns = [base]
    
    for _ in range(n_patterns - 1):
        # Create new pattern correlated with base
        pattern = base.copy()
        n_flips = int(n_neurons * (1 - correlation))
        flip_indices = np.random.choice(n_neurons, n_flips, replace=False)
        pattern[flip_indices] *= -1
        patterns.append(pattern)
    
    return np.array(patterns)


def binarize_image(image: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    """
    Convert grayscale image to binary pattern.
    
    Parameters:
    -----------
    image : np.ndarray
        Grayscale image (values between 0 and 1)
    threshold : float
        Binarization threshold
        
    Returns:
    --------
    binary : np.ndarray
        Binary pattern with values in {-1, +1}
    """
    binary = np.where(image >= threshold, 1, -1)
    return binary.flatten()


def pattern_to_image(pattern: np.ndarray, shape: Tuple[int, int]) -> np.ndarray:
    """
    Reshape flat pattern into 2D image.
    
    Parameters:
    -----------
    pattern : np.ndarray
        Flat pattern vector
    shape : Tuple[int, int]
        Target image shape (height, width)
        
    Returns:
    --------
    image : np.ndarray
        2D image array
    """
    return pattern.reshape(shape)


def compute_pattern_similarity_matrix(patterns: np.ndarray) -> np.ndarray:
    """
    Compute pairwise Hamming similarity between patterns.
    
    Useful for EDA: if patterns are too similar, network will struggle
    to keep them distinct (overlapping energy valleys).
    
    Parameters:
    -----------
    patterns : np.ndarray
        Array of patterns (n_patterns, n_neurons)
        
    Returns:
    --------
    similarity : np.ndarray
        Matrix of normalized overlaps (range [-1, 1])
    """
    n_patterns = patterns.shape[0]
    n_neurons = patterns.shape[1]
    similarity = np.zeros((n_patterns, n_patterns))
    
    for i in range(n_patterns):
        for j in range(n_patterns):
            similarity[i, j] = np.dot(patterns[i], patterns[j]) / n_neurons
    
    return similarity


def add_partial_occlusion(pattern: np.ndarray, occlusion_fraction: float = 0.3) -> np.ndarray:
    """
    Simulate partial occlusion by setting some neurons to unknown state.
    
    For display purposes, we set occluded neurons to 0 (neutral).
    For Hopfield input, they should be randomly initialized.
    
    Parameters:
    -----------
    pattern : np.ndarray
        Original pattern
    occlusion_fraction : float
        Fraction of pattern to occlude
        
    Returns:
    --------
    occluded : np.ndarray
        Pattern with occlusion (occluded parts set to random)
    """
    occluded = pattern.copy()
    n_occluded = int(len(pattern) * occlusion_fraction)
    occluded_indices = np.random.choice(len(pattern), n_occluded, replace=False)
    
    # Randomly initialize occluded parts
    occluded[occluded_indices] = np.random.choice([-1, 1], size=n_occluded)
    
    return occluded
