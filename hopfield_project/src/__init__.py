"""
Hopfield Network Package
========================
Brain-inspired associative memory implementation.
"""

from .hopfield import HopfieldNetwork
from .patterns import generate_letters, generate_random_patterns
from .visualization import plot_pattern, plot_retrieval_sequence

__all__ = [
    'HopfieldNetwork',
    'generate_letters',
    'generate_random_patterns',
    'plot_pattern',
    'plot_retrieval_sequence',
]

