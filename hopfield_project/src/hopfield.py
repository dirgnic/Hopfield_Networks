"""
Hopfield Network Implementation
================================
A brain-inspired associative memory system where:
- Neurons = binary units (firing/silent)
- Synapses = learned weights (Hebbian rule)
- Dynamics = energy minimization (rolling downhill)
- Memories = attractor states (stable valleys)
"""

import numpy as np
from typing import List, Tuple, Optional


class HopfieldNetwork:
    """
    Classical Hopfield Network for associative memory.
    
    The network stores patterns as stable states (attractors) in an energy
    landscape. Retrieval is performed by initializing with a noisy/partial
    pattern and letting the network dynamics "roll downhill" to the nearest
    stored memory.
    
    Biological Analogy:
    -------------------
    - Each neuron can fire (s_i = +1) or stay silent (s_i = -1)
    - Synaptic weights w_ij encode how strongly neurons influence each other
    - Hebbian learning: "neurons that fire together, wire together"
    - Network dynamics: neurons update based on weighted input from neighbors
    - Energy function: measures "consistency" of current state with stored patterns
    """
    
    def __init__(self, n_neurons: int):
        """
        Initialize the Hopfield network.
        
        Parameters:
        -----------
        n_neurons : int
            Number of neurons in the network (e.g., 100 for 10x10 images)
        """
        self.n_neurons = n_neurons
        self.weights = np.zeros((n_neurons, n_neurons))
        self.patterns = None
        
    def train(self, patterns: np.ndarray):
        """
        Train the network using Hebbian learning rule.
        
        The weight between neurons i and j is strengthened if they tend to
        be active together across the stored patterns.
        
        Mathematical Form:
        ------------------
        w_ij = (1/N) * sum_μ ξ_i^μ * ξ_j^μ   for i ≠ j
        w_ii = 0  (no self-connections)
        
        Brain Analogy:
        --------------
        "Cells that fire together, wire together" - Donald Hebb
        If neuron i and j are often co-active in stored memories,
        their synaptic connection strengthens.
        
        Parameters:
        -----------
        patterns : np.ndarray
            Array of shape (n_patterns, n_neurons) with values in {-1, +1}
        """
        patterns = np.atleast_2d(patterns)
        self.patterns = patterns
        n_patterns = patterns.shape[0]
        
        # Hebbian learning: accumulate outer products
        self.weights = np.zeros((self.n_neurons, self.n_neurons))
        for pattern in patterns:
            # Outer product: w_ij += ξ_i * ξ_j
            self.weights += np.outer(pattern, pattern)
        
        # Normalize by number of neurons
        self.weights /= self.n_neurons
        
        # Zero diagonal (no self-connections)
        np.fill_diagonal(self.weights, 0)
        
    def energy(self, state: np.ndarray) -> float:
        """
        Compute the energy of a given state.
        
        Mathematical Form:
        ------------------
        E(s) = -1/2 * sum_ij w_ij * s_i * s_j
        
        Physical Analogy:
        -----------------
        Like potential energy in physics: lower energy = more stable state.
        Stored patterns correspond to local minima (valleys) in the energy
        landscape. The network "rolls downhill" during retrieval.
        
        Parameters:
        -----------
        state : np.ndarray
            Current state vector of shape (n_neurons,) with values in {-1, +1}
            
        Returns:
        --------
        energy : float
            Energy value (more negative = more stable)
        """
        return -0.5 * np.dot(state, np.dot(self.weights, state))
    
    def update_async(self, state: np.ndarray, indices: Optional[List[int]] = None) -> np.ndarray:
        """
        Perform asynchronous update (one neuron at a time).
        
        Update Rule:
        ------------
        s_i^(t+1) = sign(sum_j w_ij * s_j^(t))
        
        Brain Analogy:
        --------------
        Each neuron "listens" to its inputs from other neurons:
        - Positive total input → neuron fires (s_i = +1)
        - Negative total input → neuron stays silent (s_i = -1)
        - Zero input → keep current state (or random choice)
        
        Parameters:
        -----------
        state : np.ndarray
            Current state vector
        indices : List[int], optional
            Specific neurons to update. If None, update random neuron.
            
        Returns:
        --------
        new_state : np.ndarray
            Updated state vector
        """
        new_state = state.copy()
        
        if indices is None:
            # Update one random neuron
            indices = [np.random.randint(0, self.n_neurons)]
        
        for i in indices:
            # Compute weighted input (like synaptic input to neuron i)
            h_i = np.dot(self.weights[i], state)
            
            # Update neuron based on sign of input
            new_state[i] = 1 if h_i > 0 else -1 if h_i < 0 else state[i]
        
        return new_state
    
    def update_sync(self, state: np.ndarray) -> np.ndarray:
        """
        Perform synchronous update (all neurons at once).
        
        Warning: Synchronous updates can lead to oscillations.
        Asynchronous updates guarantee energy decrease.
        
        Parameters:
        -----------
        state : np.ndarray
            Current state vector
            
        Returns:
        --------
        new_state : np.ndarray
            Updated state vector
        """
        # Compute input to all neurons
        h = np.dot(self.weights, state)
        
        # Update all neurons simultaneously
        new_state = np.sign(h)
        new_state[h == 0] = state[h == 0]  # Keep state if input is zero
        
        return new_state
    
    def retrieve(self, 
                 initial_state: np.ndarray, 
                 max_iter: int = 100,
                 mode: str = 'async',
                 record_trajectory: bool = False) -> Tuple[np.ndarray, dict]:
        """
        Retrieve a stored pattern from a noisy/partial input.
        
        This is the core "memory recall" process:
        1. Start with noisy/incomplete pattern
        2. Repeatedly update neurons following local rules
        3. Network "rolls downhill" in energy landscape
        4. Converges to nearest stored pattern (attractor)
        
        Brain Analogy:
        --------------
        "You hear a few notes and recall the whole song"
        The brain fills in missing information by settling into
        a familiar, stable configuration.
        
        Parameters:
        -----------
        initial_state : np.ndarray
            Starting state (noisy pattern)
        max_iter : int
            Maximum number of update iterations
        mode : str
            'async' for asynchronous (safer), 'sync' for synchronous
        record_trajectory : bool
            If True, record energy and states during retrieval
            
        Returns:
        --------
        final_state : np.ndarray
            Retrieved pattern (converged state)
        info : dict
            Dictionary with convergence information:
            - 'converged': bool
            - 'iterations': int
            - 'energy_trajectory': list (if record_trajectory=True)
            - 'state_trajectory': list (if record_trajectory=True)
        """
        state = initial_state.copy()
        info = {
            'converged': False,
            'iterations': 0,
            'energy_trajectory': [],
            'state_trajectory': []
        }
        
        if record_trajectory:
            info['energy_trajectory'].append(self.energy(state))
            info['state_trajectory'].append(state.copy())
        
        for iteration in range(max_iter):
            # Update neurons
            if mode == 'async':
                new_state = self.update_async(state)
            else:
                new_state = self.update_sync(state)
            
            if record_trajectory:
                info['energy_trajectory'].append(self.energy(new_state))
                info['state_trajectory'].append(new_state.copy())
            
            # Check convergence
            if np.array_equal(new_state, state):
                info['converged'] = True
                info['iterations'] = iteration + 1
                break
            
            state = new_state
            info['iterations'] = iteration + 1
        
        return state, info
    
    def add_noise(self, pattern: np.ndarray, noise_level: float = 0.2) -> np.ndarray:
        """
        Add random noise to a pattern by flipping bits.
        
        Parameters:
        -----------
        pattern : np.ndarray
            Original pattern
        noise_level : float
            Fraction of bits to flip (0.0 to 1.0)
            
        Returns:
        --------
        noisy_pattern : np.ndarray
            Pattern with noise added
        """
        noisy = pattern.copy()
        n_flips = int(self.n_neurons * noise_level)
        flip_indices = np.random.choice(self.n_neurons, n_flips, replace=False)
        noisy[flip_indices] *= -1
        return noisy
    
    def compute_overlap(self, state1: np.ndarray, state2: np.ndarray) -> float:
        """
        Compute normalized overlap between two states.
        
        Returns 1.0 if identical, -1.0 if opposite, 0.0 if orthogonal.
        
        Parameters:
        -----------
        state1, state2 : np.ndarray
            State vectors to compare
            
        Returns:
        --------
        overlap : float
            Normalized dot product in range [-1, 1]
        """
        return np.dot(state1, state2) / self.n_neurons
    
    def hamming_distance(self, state1: np.ndarray, state2: np.ndarray) -> int:
        """
        Compute Hamming distance (number of differing bits).
        
        Parameters:
        -----------
        state1, state2 : np.ndarray
            State vectors to compare
            
        Returns:
        --------
        distance : int
            Number of positions where states differ
        """
        return np.sum(state1 != state2)
    
    def check_spurious_attractors(self, n_tests: int = 100) -> List[np.ndarray]:
        """
        Search for spurious attractors (stable states that aren't stored patterns).
        
        Spurious attractors emerge when too many patterns are stored,
        creating "hybrid memories" or unexpected stable states.
        
        Brain Analogy:
        --------------
        Like false memories or confabulation - the brain settles into
        a stable but incorrect memory that's a mix of real experiences.
        
        Parameters:
        -----------
        n_tests : int
            Number of random initializations to test
            
        Returns:
        --------
        spurious : List[np.ndarray]
            List of detected spurious attractors
        """
        spurious = []
        
        for _ in range(n_tests):
            # Random initialization
            random_state = np.random.choice([-1, 1], size=self.n_neurons)
            
            # Let network converge
            final_state, _ = self.retrieve(random_state, max_iter=50)
            
            # Check if this matches any stored pattern
            is_stored = False
            for pattern in self.patterns:
                if np.array_equal(final_state, pattern):
                    is_stored = True
                    break
            
            # If not a stored pattern and not already found, it's spurious
            if not is_stored:
                is_new = True
                for sp in spurious:
                    if np.array_equal(final_state, sp):
                        is_new = False
                        break
                if is_new:
                    spurious.append(final_state)
        
        return spurious
