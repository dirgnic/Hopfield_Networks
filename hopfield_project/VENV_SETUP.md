# Virtual Environment Setup Guide

## New Virtual Environment (Recommended)

A fresh virtual environment `venv_new` has been created with all necessary dependencies for the modern Hopfield notebooks.

### Quick Start

1. **Activate the new environment:**
   ```bash
   cd /Users/ingridcorobana/Desktop/An_III/final_projs/AMI_proj/hopfield_project
   source venv_new/bin/activate
   ```

2. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

3. **Select the kernel:**
   - When you open `hopfield_modern_theory.ipynb`
   - Go to: **Kernel → Change Kernel → Python (Hopfield Modern)**

### What's Installed

All dependencies from `requirements.txt`:

```
✓ numpy>=2.0.2          - Core numerical operations
✓ scipy>=1.13.1         - Scientific computing
✓ matplotlib>=3.9.4     - Plotting and visualization
✓ seaborn>=0.13.2       - Statistical visualization
✓ Pillow>=10.4.0        - Image processing
✓ requests>=2.31.0      - HTTP requests (for datasets)
✓ scikit-learn>=1.5.1   - Machine learning utilities
✓ jupyter>=1.0.0        - Jupyter notebook support
✓ ipykernel>=6.29.0     - Kernel for notebooks
✓ ipywidgets>=8.1.0     - Interactive widgets
✓ pandas>=2.2.0         - Data manipulation
✓ tqdm>=4.66.0          - Progress bars
```

### Verify Installation

```bash
source venv_new/bin/activate
python -c "import numpy, scipy, matplotlib, requests, sklearn; print('All imports successful!')"
```

### Running the Modern Hopfield Notebook

**Option 1: Jupyter Notebook**
```bash
cd hopfield_project
source venv_new/bin/activate
jupyter notebook notebooks/hopfield_modern_theory.ipynb
```
Select kernel: **Python (Hopfield Modern)**

**Option 2: Python Script**
```bash
cd hopfield_project
source venv_new/bin/activate
python hopfield_modern_theory.py
```

### Troubleshooting

**If kernel doesn't appear in Jupyter:**
```bash
source venv_new/bin/activate
python -m ipykernel install --user --name=hopfield_modern --display-name="Python (Hopfield Modern)"
```

**If imports still fail:**
```bash
source venv_new/bin/activate
pip install --upgrade -r requirements.txt
```

**To verify kernel is registered:**
```bash
jupyter kernelspec list
```
You should see `hopfield_modern` in the list.

### Old vs New Environment

- **Old `venv/`**: Original environment, may be missing some packages
- **New `venv_new/`**: Fresh environment with all dependencies (recommended)

You can safely keep both or delete the old one after verifying everything works:
```bash
rm -rf venv/  # Only after confirming venv_new works
```

### Alternative: Update Existing Environment

If you prefer to fix the old environment instead:
```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### For VS Code Users

1. Press `Cmd+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose: `./venv_new/bin/python`

Or manually add to `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv_new/bin/python"
}
```

---

**Last Updated:** December 9, 2025
