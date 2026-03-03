# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a French-language AI education course designed for beginners. It provides a comprehensive introduction to artificial intelligence, covering theoretical foundations, practical implementations, and ethical considerations.

### Main Components

- **Cours_Introduction_IA.ipynb** - Main course notebook with complete curriculum:
  - Introduction to AI history and applications
  - Best practices and ethics
  - Supervised learning (classification, regression)
  - Unsupervised learning (clustering, dimensionality reduction)
  - Reinforcement learning (Q-learning example)
  - Common models (Linear Regression, KNN, SVM, Decision Trees, Random Forest, Neural Networks)
  - Model evaluation and cross-validation
  - Deep Learning and Computer Vision
  - NLP and sentiment analysis
  - Bias and fairness in AI

- **Practical Assignments (TP)** - 6 practical exercises:
  - TP1: Classification (Health dataset)
  - TP2: Regression (Health dataset)
  - TP3: Clustering (Health dataset)
  - TP4: Deep Learning
  - TP5: Reinforcement Learning
  - TP6: NLP
  - Each TP has both subject (`*_Sujet.ipynb`) and correction (`*_Correction.ipynb`) versions

- **Demo Scripts** (`démo/` directory) - Interactive Python scripts for visualization:
  - `classification_animation.py` - Animated neural network training on moons dataset
  - `regression_comparison.py` - Comparison of different regression models
  - `clustering_animation.py` - K-Means clustering visualization
  - `reduction_animation.py` - Dimensionality reduction (PCA) visualization
  - `rl_animation.py` & `rl_pacman_animation.py` - Reinforcement learning demos
  - `supervised_vs_unsupervised.py` - Comparison visualization
  - `demo_regression.py` - Regression examples

## Development Commands

### Running Jupyter Notebooks

```bash
# Start Jupyter to view/edit course material
jupyter notebook Cours_Introduction_IA.ipynb

# Run a specific practical assignment
jupyter notebook TP1_IA_Sante_Classification_Sujet.ipynb
jupyter notebook TP1_IA_Sante_Classification_Correction.ipynb
```

### Running Demo Scripts

```bash
# Most demo scripts require matplotlib and produce animated visualizations (GIFs)
python démo/classification_animation.py
python démo/clustering_animation.py
python démo/reduction_animation.py

# These create visualization outputs in the démo directory
```

## Dependencies

The project uses core Python ML libraries (in notebooks):
- `numpy` - Numerical computations
- `pandas` - Data manipulation
- `matplotlib`, `seaborn` - Visualization
- `scikit-learn` - Classic ML algorithms (KNN, SVM, Random Forest, etc.)
- `sklearn.neural_network.MLPClassifier` - Basic neural networks

Optional for advanced work:
- `TensorFlow` / `PyTorch` - For deep learning (referenced but not required for basic course)
- `transformers` (Hugging Face) - For NLP with pretrained models (mentioned in NLP section)

## Content Architecture

### Learning Progression

The course follows a structured learning path:

1. **Foundations** - What is AI, history, ethics
2. **Supervised Learning** - Classification and regression with labeled data
3. **Unsupervised Learning** - Finding patterns without labels
4. **Reinforcement Learning** - Learning from rewards/penalties
5. **Advanced Topics** - Deep Learning, Computer Vision, NLP
6. **Practical Skills** - Model evaluation, hyperparameter tuning, bias detection

### Data and Datasets

The course uses well-known datasets:
- **Iris dataset** - Classic multiclass classification (flowers)
- **Digits dataset** - Handwritten digit recognition (8x8 images)
- **Synthetic data** - Generated datasets for demonstrations
- **Health datasets** - Custom datasets for TP exercises (TP1-TP3)

### Code Patterns and Conventions

The notebooks follow a consistent educational pattern:
1. **Theory section** - Mathematical formulas and conceptual explanation
2. **Visualization** - Plots showing how the concept works
3. **Code example** - Practical implementation with sklearn
4. **Evaluation** - Performance metrics and interpretation

All code uses `sklearn` (scikit-learn) for consistency and ease of learning.

## Key Educational Concepts

### Bias and Fairness
- Section 10 demonstrates how AI can inherit and amplify biases from historical data
- Example: Recruiter model learns to discriminate based on postal code
- Solution: Feature selection and fairness-aware modeling

### Model Evaluation Beyond Accuracy
- Section 5.A: Confusion matrices, precision, recall, F1-score
- Section 5.A.2: **ROC Curves & AUC** (added March 2026) - for threshold-aware evaluation
- Cross-validation to avoid overfitting
- Learning curves to diagnose underfitting vs overfitting

### Decision Boundaries
- Section 11 visualizes how different KNN values (n_neighbors) produce different decision boundaries
- Demonstrates overfitting (too detailed) vs underfitting (too smooth)

### Clustering Methods
- **Section 3.B**: K-Means algorithm
- **Section 3.B.2**: Elbow Method for choosing optimal k (added March 2026)
- **Section 3.B.3**: Hierarchical Clustering with dendrogram visualization (added March 2026)

### Text Vectorization
- **Section 9**: TF-IDF vectorization (added March 2026) - superior to bag-of-words for NLP tasks

## Common Workflows

### Editing Course Content
- Modify `Cours_Introduction_IA.ipynb` carefully - ensure explanations and code examples remain aligned
- When updating code cells, verify that outputs make sense pedagogically

### Adding New Demo Scripts
- Follow the existing pattern: generate data → visualize → save animation
- Use `FuncAnimation` with `PillowWriter` for GIF output (see `classification_animation.py`)
- Document the algorithm being demonstrated clearly

### Updating TPs
- Subject files (`*_Sujet.ipynb`) contain incomplete code for students
- Correction files (`*_Correction.ipynb`) contain full solutions
- Keep both versions in sync when making changes

## Important Notes for Future Work

- **Language**: Content is in French. Maintain this for consistency with students.
- **Scope**: This is introductory material. Code intentionally uses `sklearn` rather than deep frameworks like TensorFlow to keep focus on concepts.
- **Ethical emphasis**: AI ethics (bias, fairness, explainability) is integrated throughout, not as an afterthought.
- **Visualization-heavy**: The course prioritizes visual understanding - many plots and animations are critical to learning.
