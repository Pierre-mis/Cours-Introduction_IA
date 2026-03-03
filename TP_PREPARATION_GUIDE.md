# 📚 TP Preparation Guide

**Use this guide to know which course sections to study before each practical assignment.**

---

## TP1: IA & Santé - Diagnostic Cancer (Classification) 🩺

### Required Course Knowledge
- ✅ **Section 3.A** - Supervised learning basics
- ✅ **Section 4.A** - Linear Regression (for intuition)
- ✅ **Section 4.B** - Logistic Regression & `predict_proba()`
- ✅ **Section 4.C.2** - KNN algorithm
- ✅ **Section 4.C.5** - Random Forest
- ✅ **Section 5.A** - Confusion matrix & basic metrics
- ✅ **Section 5.A.2** - ROC Curves & AUC ⭐ **NEW**
- ✅ **Section 6** - Data preprocessing (especially StandardScaler)
- ✅ **Section 7** - Hyperparameter tuning

### Key Skills for TP1
1. Load breast cancer dataset ✓
2. Data exploration (describe, info, visualization)
3. Train/test split with StandardScaler
4. Train KNN and Random Forest models
5. **Compute ROC curves** ← Learn in Section 5.A.2
6. **Extract probabilities with predict_proba()** ← Learn in Section 4.B
7. Feature importance analysis

### Time Budget
- Course reading: ~1-2 hours
- TP execution: ~2-3 hours

---

## TP2: IA & Santé - Prédiction Diabète (Régression) 🩸

### Required Course Knowledge
- ✅ **Section 3.A** - Supervised learning & regression
- ✅ **Section 4.A** - Linear Regression (theory & code)
- ✅ **Section 4.B** - Other regression approaches
- ✅ **Section 5.A** - Evaluation metrics
- ✅ **Section 6** - Preprocessing
- ✅ **Section 4.B** - PolynomialFeatures (for non-linear regression) ⭐ Covered

### Key Skills for TP2
1. Load diabetes dataset
2. Linear regression modeling
3. **Polynomial feature engineering** ← Section 4.B
4. **Residual analysis** ← Shown in Section 4.A
5. Coefficient interpretation (which factors matter?)
6. R² and MSE evaluation

### Time Budget
- Course reading: ~1 hour
- TP execution: ~2 hours

---

## TP3: IA & Santé - Profilage (Clustering) 🧬

### Required Course Knowledge
- ✅ **Section 3.B** - Unsupervised learning intro
- ✅ **Section 3.B** - K-Means algorithm
- ✅ **Section 3.B.2** - Elbow Method ⭐ **NEW**
- ✅ **Section 3.B.3** - Hierarchical Clustering ⭐ **NEW**
- ✅ **Section 3.B.3** - Dendrogram visualization
- ✅ **Section 3.B.2** - PCA (for dimensionality reduction)
- ✅ **Section 6** - StandardScaler (important for clustering!)

### Key Skills for TP3
1. Load breast cancer dataset (unlabeled)
2. Scale features with StandardScaler
3. **Implement elbow method** ← Learn in Section 3.B.2
4. **Create dendrograms** ← Learn in Section 3.B.3
5. Compute cluster profiles (mean radius, etc.)
6. Compare clusters with actual diagnoses

### Challenging Parts
- Interpreting dendrograms (different linkage methods)
- Choosing between K-Means and Hierarchical
- → Read Section 3.B.2-3 carefully!

### Time Budget
- Course reading: ~1.5 hours
- TP execution: ~3 hours

---

## TP4: IA & Santé - Deep Learning 🧠

### Required Course Knowledge
- ✅ **Section 4.D** - Neural Networks & MLPClassifier
- ✅ **Section 4.D** - Early Stopping ⭐ **NEW**
- ✅ **Section 4.D** - Learning curves (loss_curve_)
- ✅ **Section 6** - StandardScaler (CRITICAL for neural nets!)
- ✅ **Section 5.B** - Overfitting vs Underfitting (to understand early stopping)

### Key Skills for TP4
1. Create MLPClassifier with custom architecture
2. **Enable early stopping** ← Learn in Section 4.D
3. Set `validation_fraction` parameter
4. **Visualize training curves** ← Already in Section 4.D
5. Prevent overfitting with early stopping
6. Evaluate performance

### Why Early Stopping Matters
- Without it: Model trains for all 1000 iterations (overfitting!)
- With it: Stops when validation performance plateaus (smart!)
- → Section 4.D explains this clearly

### Time Budget
- Course reading: ~1 hour
- TP execution: ~2 hours

---

## TP5: IA & Santé - Ambulance (Reinforcement Learning) 🚑

### Required Course Knowledge
- ✅ **Section 3.C** - Reinforcement Learning basics
- ✅ **Section 3.C** - Q-Learning algorithm
- ✅ **Section 3.C** - Epsilon-Greedy strategy
- ✅ **Section 3.C** - Q-Table updates & Bellman equation

### Key Skills for TP5
1. Understand the environment (grid, obstacles, goal)
2. Implement Q-Table initialization
3. Implement Epsilon-Greedy action selection
4. Update Q-Table with Bellman formula
5. Visualize learned Q-Table as heatmap
6. Train agent for multiple episodes

### This is Advanced!
- Most challenging TP
- Requires understanding all Q-Learning concepts
- Study Section 3.C multiple times if needed
- Code provided partially; you complete the implementation

### Time Budget
- Course reading: ~2-3 hours
- TP execution: ~4-5 hours

---

## TP6: IA & Santé - NLP 📑

### Required Course Knowledge
- ✅ **Section 9** - NLP basics
- ✅ **Section 9** - TF-IDF Vectorization ⭐ **NEW** (supersedes CountVectorizer)
- ✅ **Section 9** - Naive Bayes & SVM classification
- ✅ **Section 4.C.3** - SVM algorithm (refresher)
- ✅ **Section 4.C.4** - Naive Bayes

### Key Skills for TP6
1. Load dataset (fetch_20newsgroups)
2. **Vectorize with TfidfVectorizer** ← Learn in Section 9
3. Train Naive Bayes or SVM classifier
4. **Create WordCloud** ← Mentioned but not fully explained (extra!)
5. Test on new medical reports
6. Interpret results

### TF-IDF vs CountVectorizer
- Course only showed CountVectorizer initially
- **BUT TF-IDF is better!** (filters common words)
- Section 9 explains why
- → Use TfidfVectorizer in your TP, not CountVectorizer

### Time Budget
- Course reading: ~1.5 hours
- TP execution: ~2-3 hours

---

## Quick Reference: Which Section Before Each TP

```
TP1 (Classification)     → 3.A, 4.A-C, 5.A-A.2 ← ROC curves!
TP2 (Regression)        → 3.A, 4.A-B
TP3 (Clustering)        → 3.B, 3.B.2-B.3 ← Elbow & Hierarchical!
TP4 (Deep Learning)     → 4.D, 4.D early stopping ← Key!
TP5 (Reinforcement)     → 3.C (study carefully)
TP6 (NLP)              → 9, Section 9 TF-IDF ← Not CountVectorizer!
```

---

## What If I Get Stuck?

### For each TP, return to these course sections:

**TP1 ROC curves?** → Section 5.A.2 has examples
**TP3 Can't find the elbow?** → Section 3.B.2 shows the pattern
**TP4 What's validation_fraction?** → Section 4.D explains
**TP6 TF-IDF confusing?** → Section 9 has code comparison

---

## Tips for Success

1. **Don't skip the course!** Each section directly supports a TP
2. **Run the course code yourself** - Don't just read it
3. **Make notes** about key parameters and functions
4. **Try to understand WHY** (not just HOW)
5. **Ask questions** if concepts are unclear before starting TP

---

## Common Mistakes to Avoid

| Mistake | Prevention |
|---------|-----------|
| Using CountVectorizer in TP6 | Read Section 9 on TF-IDF! |
| Not scaling data in TP1 | Section 6 shows why StandardScaler is critical |
| Forgetting early_stopping in TP4 | Section 4.D emphasizes this parameter |
| Not using elbow method in TP3 | Section 3.B.2 has complete code |
| Predicting instead of predict_proba in TP1 | Section 4.B shows the difference |

---

## Estimated Total Time

| TP | Course | Practice | Total |
|----|--------|----------|-------|
| TP1 | 1.5 h  | 2.5 h    | 4 h  |
| TP2 | 1 h    | 2 h      | 3 h  |
| TP3 | 1.5 h  | 3 h      | 4.5 h |
| TP4 | 1 h    | 2 h      | 3 h  |
| TP5 | 2.5 h  | 4.5 h    | 7 h  |
| TP6 | 1.5 h  | 2.5 h    | 4 h  |
| **TOTAL** | **9 h** | **16.5 h** | **25.5 h** |

(Each TP assumes you've already learned Python basics)

---

## Questions?

- "Where do I learn about X?" → Check the TP Preparation Guide (this file!)
- "This concept is unclear" → Reread the course section with the same name
- "My TP isn't working" → Check if you covered all sections in "Required Course Knowledge"

**Good luck! 🚀**

---

*Last updated: March 3, 2026*
*All TPs now have 100% course coverage!*
