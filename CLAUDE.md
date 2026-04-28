# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

French-language introductory AI course aimed at beginners. Covers theoretical foundations, hands-on `scikit-learn` work, and ethical considerations. The whole repository is **course material**, not an application — there is no build/test pipeline, only notebooks and demo scripts.

### Top-level layout

- `Cours_Introduction_IA.ipynb` — main course notebook (full curriculum)
- `Notions_Essentielles.md` — **canonical reference mémo** for the entire course (concepts, formulas, checklists). When a student or the user asks "what should I know about X", check here first; keep this file in sync when course content evolves.
- `Exploration_Donnees.ipynb` — data exploration / EDA companion notebook
- `Metriques_Modeles.ipynb` — focused notebook on evaluation metrics (confusion matrix, ROC, regression metrics)
- `Cours.pptx` — slide deck (binary, do not edit programmatically)
- TPs (practical assignments), each in `_Sujet` (student) + `_Correction` (solution) form:
  - TP1 — Classification (santé)
  - TP2 — Régression (santé)
  - TP3 — Clustering (santé)
  - TP4 — Deep Learning
  - TP5 — Reinforcement Learning (Q-Learning)
  - TP6 — NLP
  - TP7 — Fuite de données (data leakage)
  - TP8 — Données problématiques (data quality)
  - `TP_Blanc` — mock exam
- `démo/` — standalone Python scripts producing animated GIFs for in-class demos
- `images/` — static figures used in notebooks/slides

### .gitignore policy (important)

`/.gitignore` deliberately **excludes most correction files and the `démo/` directory** from git. Specifically tracked-out: TP3/TP4/TP5/TP6 corrections, `TP_Blanc_Correction.ipynb`, the entire `démo/` folder, and `images/`. TP1/TP2 corrections are commented-out (so they ARE tracked). When modifying corrections, do not stage gitignored ones — and don't "fix" the .gitignore by un-ignoring them without asking the user; the asymmetry is intentional (some corrections are released to students, others aren't).

## Common Commands

```bash
# Open the main course
jupyter notebook Cours_Introduction_IA.ipynb

# A specific TP (subject vs correction)
jupyter notebook TP1_IA_Sante_Classification_Sujet.ipynb
jupyter notebook TP1_IA_Sante_Classification_Correction.ipynb

# Run a demo animation (writes a .gif into démo/)
python démo/classification_animation.py
python démo/clustering_animation.py
python démo/reduction_animation.py
```

There is no test suite, no linter, no package manifest — dependencies are installed ad-hoc in the user's Python environment.

## Dependencies

Notebooks rely on the standard scientific Python stack: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn` (incl. `sklearn.neural_network.MLPClassifier`). NLP sections optionally reference `transformers` (Hugging Face); deep-learning frameworks (`tensorflow`, `pytorch`) are mentioned conceptually but not required. Demo GIFs use `matplotlib.animation.FuncAnimation` + `PillowWriter`.

## Architecture / Pedagogical Conventions

The course is intentionally `sklearn`-only to keep focus on concepts rather than framework plumbing. Each notebook section follows a consistent four-beat pattern:

1. **Theory** — concept + formula
2. **Visualization** — plot showing the idea
3. **Code** — minimal `sklearn` implementation
4. **Evaluation** — metrics + interpretation

When editing a section, preserve this rhythm. Code outputs are part of the pedagogy — re-running cells should produce results that *teach* (e.g., a deliberately overfit model should still look overfit). If you change a code cell, re-execute it and confirm the output still matches the surrounding narrative.

### Subject ↔ Correction synchronization

`*_Sujet.ipynb` files contain scaffolding with code blanks/TODOs for students. `*_Correction.ipynb` files contain the full solution. **Both must stay in sync** — when you change a question, the correction has to follow, and vice versa. The Sujet should never reveal the answer; the Correction should answer the exact question the Sujet asks.

### Where things "live"

- Conceptual content + formulas: `Notions_Essentielles.md` (markdown, easily searchable). Treat this as the source of truth for definitions.
- Worked examples + animations: `Cours_Introduction_IA.ipynb` and `démo/*.py`.
- Hands-on practice: TP notebooks. TP7 (data leakage) and TP8 (data quality) are deliberately about *anti-patterns* — code there demonstrates what *not* to do alongside the fix.

## Key Educational Themes (cross-cut multiple files)

- **Medical-context priority on Recall**: in TPs using health datasets, the canonical message is "minimize false negatives." Don't switch to accuracy-based scoring without thinking about this.
- **Data leakage**: TP7 + Section 10 of `Notions_Essentielles.md`. Always fit preprocessors on train only; use `Pipeline` in cross-validation contexts.
- **Bias & fairness**: integrated throughout (esp. recruiter / postal-code example), not a single appendix section. When adding examples, prefer ones that make the bias visible.
- **Threshold-aware evaluation**: ROC/AUC and threshold tuning are presented as first-class tools, not just accuracy.

## Notes for Future Work

- **Language**: All student-facing content is French. Maintain French in notebook markdown, comments, variable names where pedagogical, and error messages. Code identifiers can stay English where conventional (`X_train`, `accuracy_score`, etc.).
- **Visual-first**: plots and animations are load-bearing for understanding — don't strip them for "cleaner" notebooks.
- **Scope discipline**: this is an *introduction*. Resist adding TensorFlow/PyTorch examples to the core notebook unless explicitly requested — the `sklearn`-only constraint is a feature.
