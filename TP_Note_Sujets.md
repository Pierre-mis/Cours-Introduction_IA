# TP Noté — Sujets et grille de notation

**Durée :** 4h en présentiel · **Modalité :** travail individuel · **Livrable :** un notebook `.ipynb` exécutable + un rapport intégré (markdown dans le notebook)

Tu choisis **un** sujet parmi les quatre proposés. Deux sont sur des données de jeu vidéo, deux sur des données de santé. La grille de notation est **identique** pour tous les sujets — choisis donc celui qui te motive le plus, pas celui qui semble "le plus facile".

| Sujet                                                   | Domaine   | Type                         | Difficulté |
| ------------------------------------------------------- | --------- | ---------------------------- | ---------- |
| [TP-A](#tp-a--apprentissage-par-renforcement--snake)    | Jeu vidéo | RL Q-Learning                | ⭐⭐⭐        |
| [TP-C](#tp-c--prédire-la-victoire-en-league-of-legends) | Jeu vidéo | Classification binaire       | ⭐          |
| [TP-D](#tp-d--prédire-le-risque-davc)                   | Santé     | Classification déséquilibrée | ⭐          |
| [TP-E](#tp-e--analyse-davis-de-médicaments)             | Santé     | NLP — sentiment              | ⭐⭐         |

---

## TP-A — Apprentissage par renforcement : Snake

### Contexte

Tu disposes d'un environnement **Snake** simplifié (grille 8×8) : un serpent qui mange des pommes, grandit à chaque pomme, meurt s'il touche un mur ou sa propre queue. Ton objectif est d'**entraîner un agent Q-Learning tabulaire** capable de jouer le mieux possible, sans aucune règle codée en dur.

Une difficulté centrale du sujet : le serpent vit dans une grille de 64 cases avec une longueur variable. Si tu encodes l'état brutalement (positions absolues + chaque case occupée), ton espace d'état explose et la Q-table devient ingérable. **Tout le défi est de choisir une bonne représentation d'état.**

### Environnement fourni

Un fichier `snake_env.py` te donne accès à un environnement style Gym :

```python
from snake_env import SnakeEnv

env = SnakeEnv(grid=8, seed=42)
state = env.reset()
# state est un tuple à 5 entiers :
#   (danger_gauche, danger_devant, danger_droite, dir_pomme_x, dir_pomme_y)
# - danger_X ∈ {0, 1} : y a-t-il un mur ou la queue dans cette direction relative ?
# - dir_pomme ∈ {-1, 0, +1} : direction de la pomme dans le repère du serpent

state, reward, done = env.step(action)
# action ∈ {0=tourner gauche, 1=tout droit, 2=tourner droite}
```

- **Récompense** : +10 par pomme, −10 à la mort (mur ou queue), −0.01 par pas (incite à ne pas tourner en rond).
- **Visualisation** : `env.render()` affiche la grille (matplotlib).
- **Espace d'état** : avec cette représentation, environ **64 états utiles** seulement.

### Travail attendu

1. **Comprendre l'environnement** (15 min) — Joue quelques épisodes avec une politique aléatoire. Quelle longueur moyenne ? Quel taux de mort par mur vs par queue ?
2. **Réfléchir à la représentation d'état** — Avant de coder : pourquoi la représentation fournie marche-t-elle ? Que perd-on en n'encodant pas la position absolue du serpent ? Que se passerait-il si on encodait toutes les cases occupées par la queue ? (Réponse attendue : explosion combinatoire.)
3. **Implémenter Q-Learning tabulaire** — Q-table sous forme de `dict`, mise à jour Bellman, stratégie ε-greedy avec décroissance.
4. **Entraîner sur ~5 000 épisodes** avec les hyperparamètres de départ : α=0.2, γ=0.95, ε de 1.0 → 0.01.
5. **Tracer deux courbes** : récompense moyenne et longueur moyenne du serpent (fenêtre glissante 100).
6. **Évaluer l'agent entraîné** sur 200 épisodes test (ε=0). Longueur moyenne ? Distribution de la longueur finale ? Causes de mort ?
7. **Ablation** : refaire l'expérience en variant **un** choix parmi : un hyperparamètre (α, γ, stratégie d'exploration), **ou** la représentation d'état (par exemple : retirer un capteur de danger, ou ajouter la longueur du serpent). Conclure quantitativement.
8. **Bonus optionnel (+1 pt) — "Battle the prof"** : un agent de référence (`prof_agent.pkl`) entraîné par moi est fourni. Tu obtiens le bonus si **ton agent bat le mien** sur le benchmark commun.
   - Évaluation : 200 épisodes joués sur les **mêmes seeds** (script `evaluate.py` fourni).
   - Métrique : **longueur moyenne du serpent** sur les 200 épisodes.
   - Score actuel du prof : **18.80** (médiane 19). Cible exigeante : il faut probablement enrichir la représentation d'état ou faire du reward shaping pour me battre.
   - Critère du bonus : `longueur_étudiant > longueur_prof` strictement.
   - Tu peux tout faire pour gagner : tuner α/γ/ε, modifier la fonction de reward, augmenter le nombre d'épisodes, **enrichir la représentation d'état**… **sauf** modifier l'env lui-même ou le script d'évaluation.

### Critères spécifiques

- L'agent doit converger : longueur moyenne ≥ 8 sur les 100 derniers épisodes d'entraînement.
- L'analyse doit expliquer **pourquoi** ε décroît (exploration vs. exploitation).
- L'analyse de la représentation d'état (étape 2) est **explicitement notée** — pas juste un commentaire d'une ligne.
- L'ablation doit comparer quantitativement (pas juste "ça marche moins bien").
- Le bonus est **binaire** : tu bats le prof, tu as +1 ; sinon, +0. Pas de "presque".

---

## TP-C — Prédire la victoire en League of Legends

### Contexte

À partir des **statistiques des 10 premières minutes** d'une partie classée Diamond, peut-on prédire qui va gagner ? Si oui, quelles features sont décisives ?

### Données

Dataset Kaggle : *League of Legends Diamond Ranked Games (10 min)*
URL : https://www.kaggle.com/datasets/bobbyscience/league-of-legends-diamond-ranked-games-10-min
Taille : 9 879 matches, 38 features, target binaire `blueWins`.

Le fichier `high_diamond_ranked_10min.csv` est fourni dans le dossier `data/`.

### Travail attendu

1. **EDA** (30 min) — Distribution de la target, corrélations entre features, valeurs aberrantes. Au moins **trois plots commentés**.
2. **Préparation** — Train/test split stratifié 80/20. Standardisation si pertinente.
3. **Modèles à comparer** — au moins **trois** parmi : Régression Logistique, Random Forest, KNN, SVM, Gradient Boosting. Justifie tes choix.
4. **Évaluation** — Pour chaque modèle : accuracy, précision, rappel, F1, AUC-ROC. Affiche **une matrice de confusion** et **une courbe ROC**.
5. **Cross-validation** — 5-fold sur le meilleur modèle. La performance hold-out est-elle représentative ?
6. **Feature importance** — Quelles features comptent le plus ? Y a-t-il une feature **proxy** (ex : `redGoldDiff` n'est-il pas la même info que `blueGoldDiff` ?) ? Que retiendrais-tu si tu devais déployer le modèle ?
7. **Bonus optionnel (+1 pt max)** : évaluer la robustesse à un changement de patch — discussion (les datasets sont d'un patch précis, ton modèle généraliserait-il ?).

### Critères spécifiques

- Au moins une métrique **autre que l'accuracy** doit être discutée.
- La feature importance doit être **interprétée**, pas juste affichée.

---

## TP-D — Prédire le risque d'AVC

### Contexte

Un AVC (accident vasculaire cérébral) tue 5 millions de personnes par an. Détecter les patients à risque permet une prise en charge préventive. Tu travailles sur un dataset de 5 110 patients pour bâtir un classifieur, en gardant à l'esprit que **manquer un patient à risque (faux négatif) est plus grave que sur-alerter**.

### Données

Dataset Kaggle : *Stroke Prediction Dataset*
URL : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
Taille : 5 110 patients, 12 features, target `stroke` (~5 % positifs).

Le fichier `healthcare-dataset-stroke-data.csv` est fourni dans le dossier `data/`.

### Travail attendu

1. **EDA** — Inspection systématique : valeurs manquantes (attention au BMI), distribution de la target (le déséquilibre est *fort*), distribution des features par classe.
2. **Préparation** — Imputation des NaN (justifie ton choix), encodage des variables catégorielles, train/test split **stratifié**.
3. **Baseline triviale** — Quelle accuracy obtient un modèle qui prédit toujours "pas d'AVC" ? Pourquoi cette accuracy est-elle trompeuse ?
4. **Modèles à comparer** — au moins **trois**. Au moins un avec `class_weight='balanced'` et un sans. Compare l'effet.
5. **Évaluation** — Concentre-toi sur **F1**, **rappel** et **AUC**. Affiche les courbes précision-rappel et ROC.
6. **Ajustement du seuil** — Le seuil par défaut (0.5) est-il optimal pour ce contexte médical ? Trace `precision`, `rappel`, `F1` en fonction du seuil. Justifie un choix.
7. **Bonus optionnel (+1 pt max)** : tester `SMOTE` (sur-échantillonnage) et comparer à `class_weight`.

### Critères spécifiques

- L'accuracy seule ne suffit pas pour être noté — il **faut** discuter rappel/F1.
- L'ajustement de seuil doit être motivé par le **contexte clinique** (FN coûteux), pas par le seul F1.

---

## TP-E — Analyse d'avis de médicaments

### Contexte

200 000+ avis de patients sur des médicaments. Peut-on classer automatiquement un avis comme **positif** ou **négatif** à partir du seul texte ? Quelles limites cette automatisation rencontre-t-elle dans un contexte santé ?

### Données

Dataset Kaggle : *UCI ML Drug Review Dataset*
URL : https://www.kaggle.com/datasets/jessicali9530/kuc-hackathon-winter-2018
Variables principales : `review` (texte), `rating` (1-10), `condition`, `drugName`.

Le fichier est fourni dans `data/`. **Sous-échantillonne à 20 000 avis** pour rester dans le temps imparti.

### Travail attendu

1. **EDA texte** — Longueur des avis, distribution des ratings, mots les plus fréquents (avec/sans stop-words).
2. **Préparation** — Binarise `rating` en label : `positif` si rating ≥ 7, `négatif` si rating ≤ 4 (jette les ratings 5-6, ambigus). Train/test split stratifié.
3. **Vectorisation** — Compare **CountVectorizer** (bag-of-words) et **TF-IDF**. Pourquoi TF-IDF est-il généralement supérieur ?
4. **Modèles à comparer** — au moins **deux** : Régression Logistique, Naive Bayes (Multinomial). Eventuellement un troisième (SVM linéaire).
5. **Évaluation** — Accuracy, F1, matrice de confusion. Affiche **les 20 mots les plus prédictifs** pour chaque classe (coefficients du modèle linéaire).
6. **Analyse critique** — Identifie **trois exemples mal classés** et explique pourquoi. Y a-t-il un **biais de domaine** (vocabulaire médical, nom de pathologie qui corrèle avec la classe) ?
7. **Bonus optionnel (+1 pt max)** : tester un modèle pré-entraîné Hugging Face (`pipeline("sentiment-analysis")`) et comparer.

### Critères spécifiques

- La comparaison Count vs TF-IDF doit être **chiffrée**, pas seulement affirmée.
- L'analyse des erreurs doit aller au-delà de "le modèle s'est trompé" — pourquoi ?

---

## Grille de notation (commune aux 4 sujets)

Notation sur **20 points**. Bonus optionnel jusqu'à **+1 point**.

| Critère                                        | Points | Détail                                                                                                                                                                           |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Compréhension & exploration des données** | 3      | EDA pertinente, choix justifiés, lecture critique des distributions, identification des problèmes (NaN, déséquilibre, outliers).                                                 |
| **2. Méthodologie ML**                         | 5      | Train/test split correct, pas de fuite de données, comparaison de plusieurs modèles, hyperparamètres motivés, cross-validation si demandée.                                      |
| **3. Qualité du code**                         | 3      | Code lisible, factorisation raisonnable, pas de cellules orphelines, reproductibilité (`random_state` fixé).                                                                     |
| **4. Évaluation & interprétation**             | 5      | Bon choix de métriques pour le contexte, interprétation des résultats au-delà du chiffre, courbes appropriées (ROC, learning curve, etc.), conclusions sourcées par les données. |
| **5. Rapport & communication**                 | 4      | Notebook lisible (markdown explicatif entre les cellules), figures titrées et commentées, conclusion synthétique répondant à la question initiale.                               |
| **Bonus**                                      | +1     | Voir critères spécifiques au sujet.                                                                                                                                              |

### Précisions par critère

**Critère 1 — Compréhension & exploration**
- ✅ Tu as identifié et nommé les problèmes du dataset (déséquilibre, NaN, valeurs aberrantes, biais potentiels).
- ❌ Tu te contentes d'un `df.describe()` sans commentaire.

**Critère 2 — Méthodologie**
- ✅ Tes preprocessings sont fittés sur le train uniquement, ton split est stratifié quand pertinent, tu compares au moins le minimum demandé de modèles.
- ❌ Tu fais `scaler.fit(X)` avant le split → fuite de données → -2 points.
- ❌ Tu compares un seul modèle → -2 points.

**Critère 3 — Qualité du code**
- ✅ Variables nommées clairement, pas de duplication massive, exécution linéaire du notebook sans erreur.
- ❌ Cellules désordonnées, code mort, exécution non reproductible (oubli de `random_state`).

**Critère 4 — Évaluation & interprétation**
- ✅ Tu choisis tes métriques en fonction du **contexte** (rappel pour TP-D, F1 pour TP-D/E, AUC pour comparer des modèles), tu lis tes courbes, tu pointes ce qui est anormal.
- ❌ Tu rapportes uniquement l'accuracy sur un dataset déséquilibré → -2 points.
- ❌ Tu affiches une matrice de confusion sans la commenter → -1 point.

**Critère 5 — Rapport**
- ✅ Un lecteur extérieur (ex : ton stage l'an prochain) peut lire ton notebook et comprendre ce que tu as fait, pourquoi, et ce qui en ressort.
- ❌ Aucun markdown explicatif, ou un long pavé en fin de notebook qu'on ne sait pas relier au code.

### Pénalités

- **Plagiat / copier-coller d'un notebook Kaggle** sans citation : note ramenée à 0.
- **Notebook non exécutable** (erreurs au `Run All`) : −3 points.
- **Pas de rapport** (aucun markdown, juste du code) : −4 points.
- **Hors-sujet** (TP-D rendu pour le sujet TP-A) : note ramenée à 0.

### Barème indicatif

| Note  | Profil                                                                                  |
| ----- | --------------------------------------------------------------------------------------- |
| 18-20 | Travail excellent : méthodologie irréprochable, interprétation fine, bonus traité.      |
| 14-17 | Bon travail : tout l'essentiel est là, l'interprétation pourrait être plus profonde.    |
| 10-13 | Travail correct : ML fonctionne, mais analyse superficielle ou méthodologie imparfaite. |
| 6-9   | Travail incomplet : des étapes manquent, ou erreurs méthodologiques importantes.        |
| < 6   | Travail très incomplet ou problème majeur (fuite de données, plagiat partiel).          |

---

## Conseils généraux

- **Ne te jette pas sur le code.** Passe les 30 premières minutes à comprendre les données / l'environnement. Ça te fera gagner les 3h suivantes.
- **Commence par une baseline simple** (Régression Logistique, ou agent aléatoire pour TP-A). Tu auras un point de comparaison pour tout le reste.
- **Documente tes choix au fil de l'eau.** Le rapport est plus facile à écrire si tu écris en faisant, pas après coup.
- **Évite le syndrome du "j'optimise au-delà de ce qui est utile"** : un modèle à 82 % bien analysé vaut mieux qu'un modèle à 84 % sans interprétation.

Bonne chance.
