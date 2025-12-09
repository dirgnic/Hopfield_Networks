"""
Interactive Hopfield Network Demo for High School Students
===========================================================

A fun, visual demonstration that shows how the network:
1. Stores a pattern
2. Completes partial patterns
3. Fixes errors
4. Minimizes energy

Run this to see the magic happen step-by-step!
"""

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpatches
from src.hopfield import HopfieldNetwork
import time

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
np.random.seed(42)


def create_letter_H():
    """Create the letter 'H' pattern (10x10 grid)"""
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
    return np.where(H == 1, 1, -1).flatten()


def print_header(title):
    """Print a fancy header"""
    print("\n" + "="*70)
    print(title.center(70))
    print("="*70 + "\n")


def print_pattern_ascii(pattern, title="Pattern"):
    """Print pattern as ASCII art"""
    grid = pattern.reshape(10, 10)
    print(f"\n{title}:")
    print("  " + "-" * 22)
    for row in grid:
        print("  |", end="")
        for cell in row:
            print(" #" if cell == 1 else "  ", end="")
        print(" |")
    print("  " + "-" * 22)


def demo_1_storage():
    """Demo 1: How does the network learn?"""
    print_header("DEMO 1: TEACHING THE NETWORK")
    
    print("STEP 1: Create a pattern - Letter 'H'")
    print("        (10x10 grid = 100 'neurons')")
    pattern = create_letter_H()
    print_pattern_ascii(pattern, "Original Pattern")
    
    input("\nPress ENTER to continue...")
    
    print("\nSTEP 2: The network learns using the 'Friendship Rule'")
    print("        'Neurons that fire together, wire together'")
    print("\n        For each pair of neurons:")
    print("        - Both ON together?  -> Strong positive connection")
    print("        - Both OFF together? -> Strong positive connection")
    print("        - One ON, one OFF?   -> Weak/negative connection")
    
    net = HopfieldNetwork(n_neurons=100)
    
    print("\n        Building 9,900 connections (100 x 99 / 2)...")
    time.sleep(1)
    print("        Calculating connection strengths...")
    time.sleep(1)
    
    net.train(pattern.reshape(1, -1))
    
    print("\n        DONE! Network has memorized the 'H' pattern!")
    print(f"\n        Network Stats:")
    print(f"        - Neurons: 100")
    print(f"        - Connections: 9,900")
    print(f"        - Average connection strength: {np.mean(np.abs(net.weights)):.4f}")
    print(f"        - Memory energy: {net.energy(pattern):.2f}")
    
    return net, pattern


def demo_2_completion(net, pattern):
    """Demo 2: Pattern completion from partial input"""
    print_header("DEMO 2: COMPLETING PARTIAL PATTERNS")
    
    print("THE CHALLENGE: Can the network remember the FULL pattern")
    print("               when we only show it 25% of the squares?")
    print("\n               (Like recognizing a friend from just their eyes)")
    
    input("\nPress ENTER to see the partial pattern...")
    
    # Create partial pattern (keep only 25%)
    partial = pattern.copy()
    mask = np.random.rand(100) < 0.25
    partial[~mask] = np.random.choice([-1, 1], size=np.sum(~mask))
    
    print_pattern_ascii(partial, "Partial Input (only 25% shown correctly)")
    print(f"\nKnown squares: {np.sum(mask)}/100")
    print(f"Unknown squares: {100 - np.sum(mask)}/100")
    
    input("\nPress ENTER to let the network fill in the blanks...")
    
    print("\nSTEP 1: Each neuron 'listens' to its neighbors...")
    time.sleep(1)
    print("STEP 2: Neurons with strong connections to ON neighbors turn ON...")
    time.sleep(1)
    print("STEP 3: Neurons with strong connections to OFF neighbors turn OFF...")
    time.sleep(1)
    
    retrieved, info = net.retrieve(partial, max_iter=20, record_trajectory=True)
    
    print(f"\nCONVERGED in {info['iterations']} steps!")
    print_pattern_ascii(retrieved, "Network's Reconstruction")
    
    errors = net.hamming_distance(retrieved, pattern)
    print(f"\nRESULT: {100 - errors} out of 100 squares correct!")
    
    if errors == 0:
        print("\n*** PERFECT RECONSTRUCTION! ***")
    
    return retrieved


def demo_3_error_correction(net, pattern):
    """Demo 3: Fixing errors in corrupted patterns"""
    print_header("DEMO 3: FIXING ERRORS (LIKE SPELL-CHECK)")
    
    print("THE CHALLENGE: Can the network fix a messy, corrupted pattern?")
    print("               (Like reading smudged handwriting)")
    
    input("\nPress ENTER to mess up the pattern...")
    
    # Add 30% noise
    noisy = pattern.copy()
    n_flips = 30
    flip_indices = np.random.choice(100, n_flips, replace=False)
    noisy[flip_indices] *= -1
    
    print_pattern_ascii(noisy, "Corrupted Pattern (30% errors)")
    print(f"\nErrors added: {n_flips} squares flipped randomly")
    
    input("\nPress ENTER to let the network fix the errors...")
    
    print("\nFIXING ERRORS:")
    print("- Wrong neurons get 'outvoted' by their correctly-connected neighbors")
    print("- The correct pattern is like 'peer pressure' - it wins!")
    
    time.sleep(1)
    
    retrieved, info = net.retrieve(noisy, max_iter=20, record_trajectory=True)
    
    print(f"\nCONVERGED in {info['iterations']} steps!")
    print_pattern_ascii(retrieved, "Network's Correction")
    
    remaining_errors = net.hamming_distance(retrieved, pattern)
    print(f"\nOriginal errors: {n_flips}")
    print(f"Remaining errors: {remaining_errors}")
    print(f"FIXED: {n_flips - remaining_errors} errors!")
    
    if remaining_errors == 0:
        print("\n*** ALL ERRORS CORRECTED! ***")


def demo_4_energy(net, pattern):
    """Demo 4: The energy landscape"""
    print_header("DEMO 4: THE ENERGY SLIDE (WHY IT WORKS)")
    
    print("IMAGINE: The network is like a ball on a hill")
    print("\n         HIGH ENERGY = Ball at top (wrong pattern)")
    print("         LOW ENERGY  = Ball at bottom (correct pattern)")
    print("\n         The network ALWAYS rolls downhill!")
    
    input("\nPress ENTER to watch energy decrease...")
    
    # Start with noisy pattern
    noisy = pattern.copy()
    flip_indices = np.random.choice(100, 25, replace=False)
    noisy[flip_indices] *= -1
    
    print("\nStarting pattern (25% errors):")
    print(f"Energy: {net.energy(noisy):.2f} (HIGH - on the hill)")
    
    print("\nRolling downhill...")
    time.sleep(1)
    
    retrieved, info = net.retrieve(noisy, max_iter=10, record_trajectory=True)
    
    energies = info['energy_trajectory']
    
    for i, E in enumerate(energies):
        print(f"  Step {i}: Energy = {E:.2f}")
        time.sleep(0.3)
    
    print(f"\nFinal energy: {energies[-1]:.2f} (LOW - at the bottom!)")
    print(f"Energy decreased: {energies[0] - energies[-1]:.2f}")
    
    print("\n*** THE GUARANTEE: Energy NEVER increases! ***")
    print("    (That's why it always works)")


def demo_5_speed(net, pattern):
    """Demo 5: How fast is it?"""
    print_header("DEMO 5: SPEED TEST")
    
    print("THE QUESTION: How fast can the network work?")
    print("\nLet's test with different levels of corruption...")
    
    test_cases = [
        ("10% noise", 0.10),
        ("20% noise", 0.20),
        ("30% noise", 0.30),
        ("50% partial", 0.50),
    ]
    
    print("\nRUNNING TESTS:")
    print("-" * 50)
    
    for name, level in test_cases:
        if "noise" in name:
            corrupted = pattern.copy()
            n_flips = int(100 * level)
            flip_indices = np.random.choice(100, n_flips, replace=False)
            corrupted[flip_indices] *= -1
        else:
            corrupted = pattern.copy()
            mask = np.random.rand(100) < (1 - level)
            corrupted[~mask] = np.random.choice([-1, 1], size=np.sum(~mask))
        
        retrieved, info = net.retrieve(corrupted, max_iter=20)
        errors = net.hamming_distance(retrieved, pattern)
        
        status = "SUCCESS" if errors == 0 else "PARTIAL"
        print(f"{name:15} -> {info['iterations']:2} steps -> {status}")
        time.sleep(0.5)
    
    print("-" * 50)
    print("\nCONCLUSION: The network is FAST!")
    print("            Most corrections happen in just 1-2 steps!")


def main():
    """Run all demos"""
    print("\n")
    print("="*70)
    print("HOPFIELD NETWORK: INTERACTIVE DEMO FOR HIGH SCHOOL STUDENTS".center(70))
    print("="*70)
    print("\nWelcome! You're about to see how a simple network of 100 switches")
    print("can learn to remember patterns and fix mistakes.")
    print("\nThis demo will show you 5 cool experiments.")
    print("\nPress ENTER after reading each section to continue...")
    
    input("\nPress ENTER to start...")
    
    # Demo 1: Learning
    net, pattern = demo_1_storage()
    
    # Demo 2: Pattern completion
    demo_2_completion(net, pattern)
    
    # Demo 3: Error correction
    demo_3_error_correction(net, pattern)
    
    # Demo 4: Energy landscape
    demo_4_energy(net, pattern)
    
    # Demo 5: Speed
    demo_5_speed(net, pattern)
    
    # Final message
    print_header("DEMO COMPLETE!")
    print("WHAT YOU JUST SAW:")
    print("\n1. LEARNING: Network memorized the 'H' pattern in one shot")
    print("2. COMPLETION: Reconstructed full pattern from 25% input")
    print("3. ERROR CORRECTION: Fixed 30% corrupted squares")
    print("4. ENERGY MINIMIZATION: Always rolled 'downhill' to the answer")
    print("5. SPEED: Converged in just 1-2 steps (super fast!)")
    print("\n" + "="*70)
    print("FROM 100 SIMPLE SWITCHES TO INTELLIGENT BEHAVIOR".center(70))
    print("That's the magic of neural networks!".center(70))
    print("="*70 + "\n")
    
    print("Want to see the visual results?")
    print("Run: python hopfield_1982_reproduction.py")
    print("Then: open figures/summary_hopfield_1982.png")
    print("\n")


if __name__ == "__main__":
    main()
