# Notions Essentielles — Introduction à l'IA

> Mémo de référence couvrant l'ensemble du cours. Chaque section correspond à un thème abordé en cours ou en TP.

---

## Table des matières

1. [Concepts fondamentaux](#1-concepts-fondamentaux)
2. [Supervised Learning — Classification](#2-supervised-learning--classification)
3. [Supervised Learning — Régression](#3-supervised-learning--régression)
4. [Évaluation des modèles](#4-évaluation-des-modèles)
5. [Unsupervised Learning](#5-unsupervised-learning)
6. [Reinforcement Learning](#6-reinforcement-learning)
7. [Deep Learning](#7-deep-learning)
8. [NLP — Traitement du Langage](#8-nlp--traitement-du-langage)
9. [Qualité des données](#9-qualité-des-données)
10. [Fuites de données (Data Leakage)](#10-fuites-de-données-data-leakage)
11. [Biais et Éthique](#11-biais-et-éthique)
12. [Formules clés](#12-formules-clés)

---

## 1. Concepts fondamentaux

### Qu'est-ce que l'IA ?

| Terme | Définition |
|---|---|
| **Intelligence Artificielle** | Ensemble de techniques permettant à une machine de simuler des capacités cognitives humaines |
| **Machine Learning** | Sous-domaine de l'IA où la machine *apprend* à partir de données, sans être explicitement programmée |
| **Deep Learning** | Sous-domaine du ML utilisant des réseaux de neurones à nombreuses couches |

### Les 3 types d'apprentissage

```
Données étiquetées ?
       |
      OUI → Supervised Learning   (classification, régression)
       |
      NON → Unsupervised Learning (clustering, réduction de dimension)
       |
Apprentissage par interaction → Reinforcement Learning
```

### Vocabulaire de base

| Terme | Signification |
|---|---|
| **Feature** (variable / colonne) | Information d'entrée utilisée pour prédire |
| **Label** (cible / target) | Ce qu'on cherche à prédire |
| **Instance** (ligne / observation) | Un exemple dans le dataset |
| **Modèle** | Fonction apprise par l'algorithme qui mappe features → label |
| **Entraînement** | Phase où le modèle ajuste ses paramètres sur les données |
| **Inférence** | Phase où le modèle prédit sur de nouvelles données |

### Overfitting vs Underfitting

| Problème | Description | Symptôme | Solution |
|---|---|---|---|
| **Overfitting** | Le modèle mémorise les données d'entraînement | Bon train, mauvais test | Régularisation, plus de données, modèle plus simple |
| **Underfitting** | Le modèle est trop simple pour capturer les patterns | Mauvais train ET test | Modèle plus complexe, plus de features |

---

## 2. Supervised Learning — Classification

**But :** prédire une **catégorie** (classe discrète).
Exemples : spam/non-spam, CKD/non-CKD, bénin/malin.

### Modèles principaux

| Modèle | Principe | Points forts | Limites |
|---|---|---|---|
| **K-Nearest Neighbors (KNN)** | Classe = majorité des k voisins les plus proches | Simple, pas d'hypothèse sur les données | Lent à l'inférence, sensible à l'échelle |
| **SVM** | Trouve l'hyperplan qui maximise la marge entre classes | Efficace en haute dimension | Lent sur grands datasets, sensible aux paramètres |
| **Decision Tree** | Arbre de règles if/else appris des données | Interprétable | Overfitting facile |
| **Random Forest** | Ensemble d'arbres de décision (bagging) | Robuste, résistant à l'overfitting | Moins interprétable |
| **Régression Logistique** | Modèle linéaire + fonction sigmoïde | Rapide, probabilités calibrées | Frontière linéaire seulement |

### Frontière de décision

- **KNN avec k petit** → frontière très irrégulière → overfitting
- **KNN avec k grand** → frontière lisse → underfitting possible
- Choisir k par **cross-validation**

---

## 3. Supervised Learning — Régression

**But :** prédire une **valeur continue** (nombre réel).
Exemples : prix d'une maison, glycémie d'un patient, température.

### Modèles principaux

| Modèle | Formule / Principe |
|---|---|
| **Régression Linéaire** | $\hat{y} = w_0 + w_1 x_1 + \ldots + w_n x_n$ |
| **Ridge (L2)** | Linéaire + pénalité sur la somme des $w^2$ → réduit les coefficients |
| **Lasso (L1)** | Linéaire + pénalité sur la somme des $|w|$ → force certains coefficients à 0 (sélection de features) |
| **Random Forest Regressor** | Moyenne des prédictions de nombreux arbres |

### Métriques de régression

| Métrique | Formule | Interprétation |
|---|---|---|
| **MAE** | $\frac{1}{n}\sum |y_i - \hat{y}_i|$ | Erreur moyenne absolue, même unité que y |
| **RMSE** | $\sqrt{\frac{1}{n}\sum (y_i - \hat{y}_i)^2}$ | Pénalise plus les grandes erreurs |
| **R²** | $1 - \frac{\sum(y_i-\hat{y}_i)^2}{\sum(y_i-\bar{y})^2}$ | 1 = parfait, 0 = pas mieux que la moyenne, <0 = inutile |

---

## 4. Évaluation des modèles

### La matrice de confusion (classification binaire)

```
                  Prédit Positif    Prédit Négatif
Réel Positif   |  Vrai Positif (VP) | Faux Négatif (FN)  ← Danger en médecine
Réel Négatif   |  Faux Positif (FP) | Vrai Négatif (VN)
```

### Métriques de classification

| Métrique | Formule | Quand l'utiliser |
|---|---|---|
| **Accuracy** | $\frac{VP + VN}{total}$ | Dataset équilibré uniquement |
| **Précision** | $\frac{VP}{VP + FP}$ | Quand les FP sont coûteux (spam) |
| **Rappel (Recall)** | $\frac{VP}{VP + FN}$ | Quand les FN sont coûteux (médecine) |
| **F1-score** | $2 \cdot \frac{Précision \times Rappel}{Précision + Rappel}$ | Dataset déséquilibré |
| **AUC-ROC** | Aire sous la courbe ROC | Comparaison de modèles, indépendant du seuil |

> **Règle d'or en médecine :** maximiser le Rappel (minimiser les Faux Négatifs). Un malade non-détecté est plus grave qu'un sain sur-détecté.

### Courbe ROC

- Axe X : Taux de Faux Positifs (FPR)
- Axe Y : Taux de Vrais Positifs (TPR = Rappel)
- **AUC = 1.0** → modèle parfait | **AUC = 0.5** → aléatoire
- Permet de choisir le **seuil de décision** selon le contexte

### Ajustement du seuil de décision

Par défaut, sklearn prédit la classe 1 si $P(\text{classe 1}) \geq 0.5$.
En abaissant ce seuil, on **augmente le Rappel** (détecte plus de cas positifs) au prix d'une Précision plus basse.

### Cross-validation

Technique pour estimer la performance réelle d'un modèle sans biaiser l'évaluation :

```
Dataset complet divisé en K parties (folds)
→ K fois : entraîner sur K-1 folds, évaluer sur le fold restant
→ Score final = moyenne des K scores
```

- Évite de choisir un split "chanceux"
- **k=5** ou **k=10** sont les valeurs standard

### Déséquilibre des classes

Si une classe est très minoritaire (ex : 10% de cas positifs) :
- L'accuracy est trompeuse (un modèle prédisant toujours la majorité atteint 90%)
- Utiliser `class_weight='balanced'` dans sklearn
- Évaluer avec F1-score et Rappel de la classe minoritaire

---

## 5. Unsupervised Learning

### Clustering — K-Means

**But :** regrouper des observations similaires sans labels.

**Algorithme :**
1. Choisir K centroïdes aléatoirement
2. Assigner chaque point au centroïde le plus proche
3. Recalculer les centroïdes (moyenne des points assignés)
4. Répéter jusqu'à convergence

**Choisir K — Méthode du coude (Elbow Method) :**
Tracer l'inertie (somme des distances au centroïde) en fonction de K. Le "coude" indique le K optimal.

### Clustering Hiérarchique

- Fusionne progressivement les points les plus proches
- Produit un **dendrogramme** (arbre de fusions)
- Avantage : pas besoin de choisir K à l'avance

### Réduction de dimension — PCA

**But :** réduire le nombre de features en conservant le maximum de variance.

- Chaque **composante principale** est une combinaison linéaire des features originales
- Les composantes sont orthogonales entre elles
- Utile pour visualiser des données en 2D/3D et réduire le bruit

---

## 6. Reinforcement Learning

### Concepts clés

| Terme | Définition |
|---|---|
| **Agent** | Entité qui prend des décisions |
| **Environnement** | Monde dans lequel l'agent évolue |
| **État (s)** | Situation courante de l'agent |
| **Action (a)** | Choix effectué par l'agent |
| **Récompense (r)** | Signal de feedback de l'environnement |
| **Politique (π)** | Stratégie de l'agent : état → action |
| **Q-Table** | Tableau stockant la valeur de chaque paire (état, action) |

### La boucle RL

```
Environnement → état s → Agent → action a → Environnement
                                                    ↓
                         Agent ← récompense r + nouvel état s'
```

### Formule de Bellman (Q-Learning)

$$Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \bigl[r + \gamma \cdot \max_{a'} Q(s', a') - Q(s, a)\bigr]$$

| Paramètre | Rôle |
|---|---|
| $\alpha$ (learning rate) | Vitesse d'apprentissage |
| $\gamma$ (discount factor) | Importance du futur vs présent |
| $r$ | Récompense immédiate |
| $\max Q(s', a')$ | Meilleure valeur future possible |

### Stratégie epsilon-greedy

- Avec probabilité **ε** → action aléatoire (exploration)
- Sinon → meilleure action connue (exploitation)
- On commence avec ε élevé, on le diminue au fil des épisodes

---

## 7. Deep Learning

### Réseau de neurones — Structure

```
Couche d'entrée → Couches cachées → Couche de sortie
  (features)       (représentations    (prédiction)
                    intermédiaires)
```

Chaque neurone calcule : $\text{sortie} = f\!\left(\sum_i w_i x_i + b\right)$

où $f$ est une **fonction d'activation**.

### Fonctions d'activation courantes

| Fonction | Formule | Usage typique |
|---|---|---|
| **ReLU** | $\max(0, x)$ | Couches cachées (standard) |
| **Sigmoïde** | $\frac{1}{1+e^{-x}}$ | Sortie classification binaire |
| **Softmax** | $\frac{e^{x_i}}{\sum_j e^{x_j}}$ | Sortie classification multi-classe |

### Entraînement

- **Loss function** : mesure l'erreur du modèle (ex : cross-entropy pour la classification)
- **Backpropagation** : calcul du gradient de la loss par rapport à chaque poids
- **Descente de gradient** : mise à jour des poids dans la direction opposée au gradient

### Hyperparamètres importants

| Hyperparamètre | Rôle |
|---|---|
| **Learning rate** | Taille du pas de mise à jour |
| **Batch size** | Nombre d'exemples par mise à jour |
| **Epochs** | Nombre de passages complets sur le dataset |
| **Dropout** | Désactive aléatoirement des neurones → régularisation |

### Computer Vision — CNN

Les **réseaux convolutifs (CNN)** appliquent des filtres locaux sur les images :
- **Couche de convolution** : détecte des patterns locaux (bords, textures)
- **Pooling** : réduit la taille spatiale, conserve les features importantes
- **Couche fully-connected** : classification finale

---

## 8. NLP — Traitement du Langage

### Vectorisation du texte

| Méthode | Principe | Limite |
|---|---|---|
| **Bag of Words** | Compte les occurrences de chaque mot | Ignore l'ordre et la fréquence relative |
| **TF-IDF** | Pondère les mots rares plus importants que les mots fréquents | Toujours sans contexte |
| **Embeddings (Word2Vec)** | Représentation dense dans un espace vectoriel | Nécessite beaucoup de données |

### TF-IDF

$$\text{TF-IDF}(t, d) = \underbrace{\frac{\text{occurrences de } t \text{ dans } d}{\text{total mots de } d}}_{\text{TF}} \times \underbrace{\log\frac{\text{total documents}}{\text{documents contenant } t}}_{\text{IDF}}$$

- **TF** (Term Frequency) : fréquence du mot dans le document
- **IDF** (Inverse Document Frequency) : pénalise les mots trop communs ("le", "et"...)

### Modèles pré-entraînés (Transformers)

- **BERT, GPT, etc.** : entraînés sur des milliards de textes, réutilisables par fine-tuning
- Librairie **Hugging Face** (`transformers`) : accès simplifié à ces modèles
- Avantage : comprennent le **contexte** (le même mot a des représentations différentes selon le contexte)

---

## 9. Qualité des données

### Checklist avant de modéliser

| Problème | Détection | Traitement |
|---|---|---|
| **Valeurs manquantes** | `df.isnull().sum()` | Imputer (médiane/mode) ou supprimer si >40% |
| **Valeurs manquantes cachées** | `(df == '?').sum()` | `.replace('?', np.nan)` |
| **Outliers** | Boxplot, règle IQR | Mettre à NaN + réimputer, ou clipper |
| **Doublons** | `df.duplicated().sum()` | `df.drop_duplicates()` |
| **Déséquilibre des classes** | `y.value_counts()` | `class_weight='balanced'`, F1 plutôt qu'accuracy |
| **Haute cardinalité** | `df[col].nunique()` | Regrouper les modalités rares |
| **Mauvais typage** | `df.dtypes` | `pd.to_numeric(errors='coerce')` |

### Imputation

- **Médiane** (numériques) : robuste aux outliers — préférer à la moyenne quand la distribution est asymétrique
- **Mode** (catégorielles) : valeur la plus fréquente
- **KNNImputer** : utilise les k voisins les plus similaires — plus précis mais plus lent

### Encodage des variables catégorielles

| Méthode | Quand l'utiliser |
|---|---|
| **Label Encoding** | Variable ordinale (ordre naturel : faible < moyen < élevé) |
| **One-Hot Encoding** | Variable nominale (pas d'ordre), cardinalité faible |
| **Target Encoding** | Cardinalité élevée — **attention à la fuite de données !** |

---

## 10. Fuites de données (Data Leakage)

> Le modèle "connaît" des informations qu'il ne devrait pas avoir au moment de la prédiction. Les performances semblent excellentes mais le modèle est inutilisable en production.

### Les 3 types principaux

**1. Fuite de prétraitement**

```
❌ MAUVAIS              ✅ CORRECT
scaler.fit(X_all)       X_train, X_test = split(X)
split → train/test      scaler.fit(X_train)
                        scaler.transform(X_test)  ← sans fit !
```

**2. Fuite de variable**
Une feature encode directement ou indirectement la cible (ex : `médicament_diabète` pour prédire le diabète). La feature n'est pas disponible au moment réel de la prédiction.

**3. Fuite temporelle**
Sur des données chronologiques, un split aléatoire place des données futures dans le train.
→ Toujours utiliser un **split chronologique** ou `TimeSeriesSplit`.

**4. Fuite patient/groupe**
Le même individu apparaît dans train et test → le modèle mémorise ses caractéristiques.
→ Utiliser `GroupShuffleSplit` avec l'identifiant patient comme groupe.

### Solution universelle : le Pipeline sklearn

```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
# Le pipeline garantit que le scaler est refitté à chaque fold de cross-validation
```

---

## 11. Biais et Éthique

### D'où viennent les biais ?

- **Biais dans les données historiques** : si les données reflètent des injustices passées, le modèle les amplifie
- **Biais de sélection** : dataset non représentatif de la population cible
- **Biais de mesure** : certains groupes sont moins bien mesurés (ex : moins de données médicales sur certaines populations)
- **Biais de confirmation** : on évalue le modèle sur des métriques qui masquent les inégalités

### Exemple concret

Un modèle de recrutement entraîné sur des données historiques peut apprendre à pénaliser certains codes postaux ou prénoms — non pas parce qu'ils sont liés aux compétences, mais parce qu'ils sont corrélés à des biais historiques d'embauche.

### Bonnes pratiques

- **Analyser les performances par sous-groupe** (genre, âge, ethnicité...) pas seulement globalement
- **Identifier les features proxy** (code postal ≈ origine socio-économique)
- **Documenter les limites** du modèle et les populations sous-représentées dans le dataset
- **Impliquer des experts du domaine** dans la conception et l'évaluation

---

## 12. Formules clés

### Bellman (Q-Learning)
$$Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \bigl[r + \gamma \cdot \max_{a'} Q(s', a') - Q(s, a)\bigr]$$

### Métriques de classification
$$\text{Accuracy} = \frac{VP + VN}{VP + VN + FP + FN}$$
$$\text{Précision} = \frac{VP}{VP + FP} \qquad \text{Rappel} = \frac{VP}{VP + FN}$$
$$\text{F1} = 2 \cdot \frac{\text{Précision} \times \text{Rappel}}{\text{Précision} + \text{Rappel}}$$

### Métriques de régression
$$\text{MAE} = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i| \qquad \text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
$$R^2 = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

### TF-IDF
$$\text{TF-IDF}(t, d) = \frac{\text{occ}(t,d)}{|d|} \times \log\frac{N}{|\{d : t \in d\}|}$$

### Neurone artificiel
$$\text{sortie} = f\!\left(\sum_{i=1}^n w_i x_i + b\right)$$

---

*Cours Introduction à l'IA — 2026*
