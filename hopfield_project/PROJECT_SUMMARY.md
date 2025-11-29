#  Hopfield Networks: Complete Project Package
## Archaeology of Intelligent Machines - Final Project 2025

---

##  Project Overview

This is a **complete, production-ready implementation** of Hopfield Networks, structured around brain-inspired analogies as the narrative spine. Everything is built from the ground up in Python, with comprehensive documentation, experiments, and LaTeX presentation materials.

### What's Included:

 **Full Python Implementation**
- Core Hopfield network class with extensive documentation
- Pattern generation utilities
- Comprehensive visualization tools
- Brain analogies explained at every step

 **Complete Experimental Suite**
- Basic retrieval demonstrations
- Capacity analysis (~0.138N verification)
- Noise robustness testing
- Spurious attractor detection

 **LaTeX Documents**
- Professional Beamer presentation (three-act structure)
- Mid-term project description document
- Ready to compile and present

 **Interactive Exploration**
- Jupyter notebook with step-by-step walkthrough
- Live demonstrations of all concepts
- Experimental playground

 **Complete Documentation**
- README with project overview
- GUIDE.md with detailed instructions
- QUICKREF.md for fast lookup
- Inline code comments with brain analogies

---

##  Getting Started (5 Minutes)

```bash
cd hopfield_project

# One-command setup and demo
./setup.sh

# That's it! Your demo will run and generate figures.
```

---

##  The Three-Act Narrative

### **Act I: From Proteins to Energy Landscapes**
*Biology meets Physics*

- Protein folding in energy landscapes
- Nature's optimization: "rolling downhill"
- Transition from molecules to neurons
- Memories as valleys in energy space

**Video Reference**: "A Brain-Inspired Algorithm For Memory"

### **Act II: Building Intelligence from Simple Rules**
*Implementation with Brain Analogies*

| Step | Implementation | Brain Analogy |
|------|---------------|---------------|
| 1 | Binary vectors s_i ∈ {-1,+1} | Neurons firing/silent |
| 2 | Hebbian weights w_ij = Σξ_i·ξ_j | "Fire together, wire together" |
| 3 | Update s_i = sign(Σw_ij·s_j) | Neurons listen to neighbors |
| 4 | Energy E = -½Σw_ij·s_i·s_j | Rolling downhill to stability |
| 5 | Retrieval from noise | "Hear notes → recall song" |

### **Act III: Experiments, Capacity & Modern Extensions**
*Validation and Insights*

- **Data**: Binary 10×10 letter images (A, B, C, D, E)
- **Capacity**: Verified ~14 patterns for N=100 (0.138N)
- **Noise tolerance**: Up to 25-30% corruption
- **Spurious attractors**: "False memories" above capacity
- **Modern link**: Connection to transformer attention

---

##  Expected Results

### Basic Retrieval
```
Noise Level    Accuracy    Iterations
10%            100%        5-10
20%            95-100%     8-12  
30%            80-90%      10-15
```

### Capacity Limits
```
Patterns      Accuracy
5 patterns    100%
10 patterns   95-100%
14 patterns   85-95%  ← Theoretical limit
20 patterns   60-70%  ← Degradation
30 patterns   <50%    ← Breakdown
```

### Energy Behavior
- Always decreases during retrieval
- Converges to local minimum
- Lower energy = more stable state

---

##  Complete File Structure

```
hopfield_project/
│
├── README.md                    # Project overview
├── GUIDE.md                     # Detailed setup guide
├── QUICKREF.md                  # Quick reference card
├── setup.sh                     # One-command setup
├── demo.py                      # Quick demonstration
├── requirements.txt             # Python dependencies
│
├── src/                         # Core implementation
│   ├── __init__.py
│   ├── hopfield.py             # 400+ lines, fully documented
│   ├── patterns.py             # Pattern generation utilities
│   └── visualization.py        # Comprehensive plotting tools
│
├── experiments/                 # Complete experimental suite
│   ├── basic_retrieval.py      # Memory recall demos
│   ├── capacity_test.py        # Storage limit analysis
│   ├── noise_robustness.py     # Corruption tolerance
│   └── spurious_attractors.py  # False memory detection
│
├── notebooks/                   # Interactive exploration
│   └── exploration.ipynb       # Jupyter notebook
│
├── latex_presentation/          # Professional documents
│   ├── presentation.tex        # Beamer slides (complete)
│   └── project_description.tex # Mid-term report
│
└── figures/                     # Generated visualizations
    └── (created by experiments)
```

---

##  Key Concepts Explained

### 1. **Neurons as Binary Units**
```python
s_i ∈ {-1, +1}  # Firing (+1) or silent (-1)
```
**Brain**: Each element represents a neuron's state

### 2. **Hebbian Learning**
```python
w_ij = (1/N) Σ_μ ξ_i^μ · ξ_j^μ  # i≠j
```
**Brain**: "Cells that fire together, wire together" (Donald Hebb)

### 3. **Energy Function**
```python
E(s) = -½ Σ_ij w_ij · s_i · s_j
```
**Brain**: Measures "consistency" - lower = more stable

### 4. **Update Dynamics**
```python
s_i^(t+1) = sign(Σ_j w_ij · s_j^(t))
```
**Brain**: Each neuron listens to its neighbors

### 5. **Associative Memory**
```
Noisy/Partial Input → Network Dynamics → Complete Memory
```
**Brain**: Hear a few notes, recall the whole song

---

##  Running Experiments

### Quick Demo (2 minutes)
```bash
python demo.py
```
Generates:
- `figures/demo_patterns.png`
- `figures/demo_similarity.png`
- `figures/demo_retrieval.png`
- `figures/demo_energy.png`

### Full Experiments (10-15 minutes)
```bash
cd experiments

# Run all experiments
python basic_retrieval.py       # 3 different noise levels
python capacity_test.py         # Test up to 30 patterns
python noise_robustness.py      # 0-50% noise range
python spurious_attractors.py   # Find false memories
```

### Interactive Exploration
```bash
jupyter notebook notebooks/exploration.ipynb
```

---

##  LaTeX Compilation

### Mid-Term Project Description
```bash
cd latex_presentation
pdflatex project_description.tex
pdflatex project_description.tex  # Twice for references
open project_description.pdf
```

### Beamer Presentation
```bash
pdflatex presentation.tex
pdflatex presentation.tex  # Twice for navigation
open presentation.pdf
```

**Note**: Copy generated figures to `latex_presentation/figures/` before compiling, or update paths in `.tex` files.

---

##  Presentation Tips

### Structure (20-30 minutes)

**Act I (5 min)**: Hook with protein folding analogy
- Show energy landscape visualization
- Connect to brain dynamics
- Introduce Hopfield networks

**Act II (10 min)**: Implementation walkthrough
- Each step: left side = code/math, right side = brain analogy
- Live demo if possible
- Show weight matrix, patterns

**Act III (10 min)**: Experimental results
- Retrieval success (live demo)
- Capacity curve
- Noise robustness
- Spurious attractors
- Modern connection (transformers)

**Q&A (5 min)**

### Key Phrases to Use

1. "Like a protein rolling downhill to its folded state..."
2. "Neurons that fire together, wire together"
3. "Hear a few notes, recall the whole song"
4. "Energy valleys are memories"
5. "False memories emerge when landscape gets crowded"

---

##  Why This Matters

### Historical Impact
- **1982**: Hopfield introduces the model
- **2024**: Nobel Prize in Physics 
- Foundation for modern deep learning

### Modern Relevance
- Dense associative memory (exponential capacity)
- Connection to transformer attention
- Neuroscience models of memory
- Energy-based learning principles

### Pedagogical Value
- Simple rules → complex behavior
- Biology inspires computation
- Physical principles (energy minimization)
- Bridges multiple disciplines

---

##  Troubleshooting

### Import errors?
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Matplotlib not showing plots?
```bash
export MPLBACKEND=TkAgg
```

### LaTeX missing packages?
```bash
tlmgr install beamer
tlmgr install amsmath
```

### Virtual environment issues?
```bash
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

##  References & Resources

### Key Papers
1. Hopfield, J.J. (1982). "Neural networks and physical systems..." PNAS
2. Ramsauer, H. et al. (2020). "Hopfield Networks is All You Need"

### Videos (embedded in project)
1. [A Brain-Inspired Algorithm For Memory](https://www.youtube.com/watch?v=1WPJdAW-sFo)
2. [Hopfield Networks Explained](https://www.youtube.com/watch?v=piF6D6CQxUw)
3. [Hopfield Networks is All You Need](https://www.youtube.com/watch?v=nv6oFDp6rNQ)

### Additional Reading
- Wikipedia: Hopfield Network (comprehensive)
- Hertz et al., "Introduction to the Theory of Neural Computation"
- Amit, "Modeling Brain Function"

---

##  Pre-Submission Checklist

- [ ] All experiments run successfully
- [ ] Figures generated and saved
- [ ] LaTeX documents compile without errors
- [ ] Code is well-commented
- [ ] README is clear and complete
- [ ] Presentation tells coherent story
- [ ] Brain analogies are prominent
- [ ] Modern connections mentioned
- [ ] References properly cited
- [ ] Demo works smoothly

---

##  Learning Outcomes

After completing this project, you will understand:

1.  How simple local rules create complex emergent behavior
2.  The connection between physics, biology, and computation
3.  Energy-based models of neural computation
4.  Capacity limitations in associative memory
5.  Spurious attractors and their biological analogs
6.  The foundation for modern deep learning architectures
7.  How to implement and test neural network models from scratch

---

##  Project Strengths

### Technical
-  Complete from-scratch implementation
-  Extensive documentation with analogies
-  Comprehensive experimental validation
-  Professional visualizations
-  Modular, extensible code structure

### Narrative
-  Three-act story arc (protein → implementation → experiments)
-  Brain analogies at every step
-  Connection to modern AI
-  Historical context (Nobel Prize)
-  Clear pedagogical value

### Deliverables
-  Professional LaTeX presentation
-  Detailed project description
-  Interactive Jupyter notebook
-  Complete experimental results
-  Publication-quality figures

---

##  Next Steps After Mid-Term

### Potential Extensions

1. **Modern Hopfield Networks**
   - Implement dense associative memory
   - Exponential capacity
   - Continuous state spaces

2. **Connection to Transformers**
   - Show mathematical equivalence
   - Implement attention as Hopfield retrieval
   - Compare performance

3. **Biological Realism**
   - Add spike timing
   - Implement learning rules (STDP)
   - Multi-layer networks

4. **Applications**
   - Image denoising
   - Pattern completion
   - Error correction codes

---

##  Support & Feedback

For questions or issues:
1. Check GUIDE.md for detailed instructions
2. See QUICKREF.md for common commands
3. Review inline code comments
4. Check troubleshooting section

---

##  Final Thoughts

This project demonstrates how:
- **Simple principles** (Hebbian learning, energy minimization) create **complex capabilities** (associative memory)
- **Biology inspires computation** (neurons, synapses, attractor dynamics)
- **Classic models remain relevant** (foundation for transformers)
- **Storytelling enhances understanding** (protein folding → brain → AI)

**The 2024 Nobel Prize** recognizes these insights as foundational to modern AI. You're now equipped to explain *why*.

---

##  Ready to Present!

You have everything you need:
-  Working code
-  Beautiful visualizations  
-  Compelling narrative
-  Brain-inspired analogies
-  Experimental validation
-  Modern connections
-  Professional presentation

**Go forth and teach the world about memory, energy, and intelligence!** 

---

*Created for Archaeology of Intelligent Machines, 2025*
*Authors: Ingrid Corobana, Moise Irina, Cosmin Glod*
