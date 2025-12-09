# Quick Reference - Running Hopfield Notebooks

## ✅ Setup Complete!

New virtual environment `venv_new` is ready with all dependencies:
- ✓ NumPy 2.0.2
- ✓ SciPy 1.13.1
- ✓ Matplotlib 3.9.4
- ✓ Requests, Pillow, scikit-learn, Jupyter, and more

---

## 🚀 Quick Commands

### Run Modern Hopfield Notebook
```bash
cd ~/Desktop/An_III/final_projs/AMI_proj/hopfield_project
source venv_new/bin/activate
jupyter notebook notebooks/hopfield_modern_theory.ipynb
```
**Then select kernel:** `Python (Hopfield Modern)`

### Run as Python Script
```bash
cd ~/Desktop/An_III/final_projs/AMI_proj/hopfield_project
source venv_new/bin/activate
python hopfield_modern_theory.py
```

### Run Other Notebooks
```bash
source venv_new/bin/activate
jupyter notebook notebooks/exploration.ipynb
# or
jupyter notebook notebooks/image_retrieval.ipynb
```

---

## 📂 File Structure

```
hopfield_project/
├── notebooks/
│   ├── hopfield_modern_theory.ipynb    ← NEW comprehensive theory
│   ├── exploration.ipynb                ← Classical Hopfield
│   └── image_retrieval.ipynb            ← Geometric patterns
├── hopfield_modern_theory.py           ← NEW standalone script
├── src/
│   ├── hopfield.py                      ← Classical implementation
│   ├── patterns.py                      ← Pattern generation
│   └── visualization.py                 ← Plotting utilities
├── venv_new/                            ← NEW virtual environment ✓
├── requirements.txt                     ← Updated dependencies
├── VENV_SETUP.md                        ← Detailed setup guide
└── README_MODERN_HOPFIELD.md           ← Theory documentation
```

---

## 🎯 What Each File Does

### `hopfield_modern_theory.ipynb`
- Complete theory: Classical (1982) → Modern (2020)
- Simpsons character face recognition
- 11 comprehensive parts with visualizations
- Works locally and in Colab

### `hopfield_modern_theory.py`
- Standalone script version
- Generates 6 PNG figures
- Can run without Jupyter

### Other Notebooks
- `exploration.ipynb`: Letter patterns, educational walkthrough
- `image_retrieval.ipynb`: Geometric shapes, occlusion tests

---

## 🔧 Kernel Selection in Jupyter

1. Open notebook
2. Click **Kernel** menu
3. Select **Change Kernel**
4. Choose **Python (Hopfield Modern)**

Or in VS Code:
1. Click kernel selector (top right)
2. Choose `venv_new/bin/python`

---

## 📦 Available Packages

| Package        | Version | Purpose                    |
|----------------|---------|----------------------------|
| numpy          | 2.0.2   | Numerical operations       |
| scipy          | 1.13.1  | Scientific computing       |
| matplotlib     | 3.9.4   | Plotting                   |
| seaborn        | 0.13.2  | Statistical visualization  |
| Pillow         | 10.4.0  | Image processing           |
| requests       | 2.31.0  | HTTP requests              |
| scikit-learn   | 1.5.1   | Machine learning utils     |
| jupyter        | 1.0.0   | Notebook interface         |
| pandas         | 2.2.0   | Data manipulation          |
| tqdm           | 4.66.0  | Progress bars              |

---

## ⚠️ Common Issues

**Problem:** Kernel not showing up
```bash
source venv_new/bin/activate
python -m ipykernel install --user --name=hopfield_modern
```

**Problem:** Import errors in notebook
- Make sure you selected `Python (Hopfield Modern)` kernel
- Restart kernel: **Kernel → Restart**

**Problem:** Old kernel still has issues
- Use the new environment: `source venv_new/bin/activate`
- Don't use the old `venv/` anymore

---

## 🎓 Learning Path

1. **Start here:** `notebooks/exploration.ipynb`  
   Learn classical Hopfield with letters

2. **Then:** `notebooks/image_retrieval.ipynb`  
   See image completion with geometric patterns

3. **Finally:** `notebooks/hopfield_modern_theory.ipynb`  
   Master modern theory with character recognition

---

## 💡 Tips

- Always activate `venv_new` before running anything
- Select the correct kernel in Jupyter
- All notebooks run independently
- The Python script version runs without Jupyter

---

**Need Help?** Check `VENV_SETUP.md` for detailed troubleshooting.

**Last Updated:** December 9, 2025
