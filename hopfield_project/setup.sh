#!/bin/bash

# Hopfield Networks Project - Quick Start Script
# ===============================================

echo "=========================================="
echo "  Hopfield Networks Project Setup"
echo "  Archaeology of Intelligent Machines"
echo "=========================================="
echo ""

# Check if in correct directory
if [ ! -f "requirements.txt" ]; then
    echo " Error: Please run this script from the hopfield_project directory"
    exit 1
fi

# Step 1: Create virtual environment
echo "Step 1: Creating virtual environment..."
python3 -m venv venv
if [ $? -eq 0 ]; then
    echo " Virtual environment created"
else
    echo " Failed to create virtual environment"
    exit 1
fi
echo ""

# Step 2: Activate and install dependencies
echo "Step 2: Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo " Dependencies installed"
else
    echo " Failed to install dependencies"
    exit 1
fi
echo ""

# Step 3: Create figures directory
echo "Step 3: Creating output directories..."
mkdir -p figures
mkdir -p notebooks
echo " Directories created"
echo ""

# Step 4: Run demo
echo "Step 4: Running demonstration..."
echo "----------------------------------------"
python demo.py
echo "----------------------------------------"
echo ""

# Final message
echo "=========================================="
echo "  Setup Complete! "
echo "=========================================="
echo ""
echo "Next steps:"
echo "  1. View generated figures in: figures/"
echo "  2. Run experiments:"
echo "     cd experiments"
echo "     python capacity_test.py"
echo "     python noise_robustness.py"
echo "  3. Open Jupyter notebook:"
echo "     jupyter notebook notebooks/exploration.ipynb"
echo "  4. Compile LaTeX documents:"
echo "     cd latex_presentation"
echo "     pdflatex presentation.tex"
echo ""
echo "For detailed instructions, see GUIDE.md"
echo ""
