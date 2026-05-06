# Grille de notation — TP-A Snake (Q-Learning)

> Note finale sur **20**, plus un **bonus de +1 point** indépendant
> (« Battle the prof »). La note ne dépasse pas 21/20.

---

## Vue d'ensemble

| Bloc | Points |
|---|---|
| 1. Prise en main de l'environnement | **1** |
| 2. Initialisation de la Q-Table | **2** |
| 3. Politique ε-greedy | **2** |
| 4. Mise à jour de Bellman | **3** |
| 5. Boucle d'entraînement | **3** |
| 6. Sauvegarde de l'agent (`.pkl`) | **1** |
| 7. Évaluation & analyse | **3** |
| Qualité du code | **2** |
| Discussion & justifications | **3** |
| **Total** | **/20** |
| 🎯 Bonus *Battle the prof* | **+1** (binaire) |

---

## Pénalités possibles (à appliquer en plus)

| Motif | Sanction |
|---|---|
| Modification de `snake_env.py` ou `evaluate.py` | **−4 pts** |
| Règles encodées en dur (ex : « si pomme à gauche → tourner ») | **−3 pts** |
| Pas de fichier `mon_agent.pkl` rendu | **−2 pts** |
| Q-Table corrompue / `evaluate.py` ne tourne pas | **bonus impossible + −1 pt** sur l'étape 6 |
| Notebook non exécuté (cellules vides) | **−1 pt** sur la qualité |

---

## Étape 1 — Prise en main de l'environnement *(1 pt)*

**Attendu :** charger `SnakeEnv`, appeler `reset()`, lire la doc de l'état (5-tuple),
faire 2-3 `step()` à la main et afficher avec `render()`. Comprendre les 3 actions
(0/1/2) et les récompenses.

| Niveau | Description | Pts |
|---|---|---|
| Excellent | Exploration manuelle propre, l'étudiant commente l'état renvoyé et identifie les composantes (dangers, direction pomme) | 1.0 |
| Partiel | Code tourne mais sans interprétation des composantes de l'état | 0.5 |
| Manquant | Pas d'interaction avec l'env / cellule absente | 0.0 |

---

## Étape 2 — Initialisation de la Q-Table *(2 pts)*

**Attendu :** structure `dict[tuple, np.ndarray(3)]`, **lazy init** quand un nouvel
état apparaît (on ne peut pas énumérer tous les états à l'avance pour Snake), valeurs
initiales à 0 (ou justifier autre choix).

| Critère | Pts |
|---|---|
| Bonne structure (`dict` état → array de 3 valeurs) | 0.5 |
| Lazy init implémentée (clé créée au 1er accès) | 0.5 |
| Initialisation à 0 (ou choix alternatif justifié, ex : optimiste) | 0.5 |
| Code robuste : pas de `KeyError` à l'exécution | 0.5 |

❌ Q-Table tableau 4D figé sur tous les états possibles → 0.5 pt max sur ce bloc.

---

## Étape 3 — Politique ε-greedy *(2 pts)*

**Attendu :** fonction qui prend `(Q, state, eps)` et renvoie une action :
- avec proba ε → action aléatoire
- sinon → `argmax(Q[state])`

| Critère | Pts |
|---|---|
| Branchement explore/exploite correct | 1.0 |
| Tirage aléatoire **uniforme** sur les 3 actions (pas biaisé) | 0.5 |
| Gestion d'un état non-vu (ex : action par défaut OU lazy init avant le choix) | 0.5 |

❌ ε figé à 0 ou 1 dès le départ → −1 pt (pas d'apprentissage ou pas d'exploitation).

---

## Étape 4 — Mise à jour de Bellman *(3 pts)*

**Formule :** $Q(s, a) \leftarrow Q(s, a) + \alpha \cdot [r + \gamma \cdot \max_{a'} Q(s', a') - Q(s, a)]$

| Critère | Pts |
|---|---|
| Formule correcte (signe, ordre des termes) | 1.0 |
| Utilise bien $s'$ dans `max Q(s', ·)` (et **pas** $s$) | 1.0 |
| Cas terminal : `max Q(s', ·) = 0` (ou état terminal traité explicitement) | 0.5 |
| Lazy init de `Q[s']` si nécessaire **avant** de prendre le max | 0.5 |

⚠️ Erreur classique : confondre les rôles de l'état présent et de l'état suivant dans la mise à jour → −1.5 pt.

---

## Étape 5 — Boucle d'entraînement *(3 pts)*

**Attendu :** boucle sur N épisodes, chacun jusqu'à `done` ou `max_steps`. Décroissance
d'ε. Suivi de métriques (récompense ou longueur par épisode). Affichage d'une courbe
d'apprentissage.

| Critère | Pts |
|---|---|
| Structure correcte : `for ep in range(N): reset → while not done: step + update` | 1.0 |
| Décroissance d'ε (linéaire, exponentielle, ou autre justifiée) | 0.5 |
| Choix d'hyperparamètres raisonnables (α ∈ [0.05, 0.3], γ ≥ 0.9, N ≥ 1000) | 0.5 |
| Tracking de la longueur OU récompense par épisode | 0.5 |
| Courbe d'apprentissage tracée (avec moyenne glissante de préférence) | 0.5 |

❌ N < 500 épisodes (insuffisant pour converger) → −1 pt. ❌ ε constant sur tout
l'entraînement → −0.5 pt.

---

## Étape 6 — Sauvegarde de l'agent *(1 pt)*

**Attendu :** fichier `mon_agent.pkl` au format attendu (`dict[tuple, np.ndarray(3)]`),
chargeable via `pickle.load`, et qui passe `evaluate.py` sans erreur.

| Critère | Pts |
|---|---|
| Fichier rendu | 0.5 |
| `evaluate.py mon_agent.pkl` tourne sans crash | 0.5 |

❌ Format incorrect (ex : `np.ndarray` 4D, `defaultdict` mal sérialisé) → 0 pt.

---

## Étape 7 — Évaluation & analyse *(3 pts)*

**Attendu :** lancer `evaluate.py`, lire la sortie, comparer avec `prof_agent.pkl`,
**commenter le résultat**.

| Critère | Pts |
|---|---|
| Benchmark lancé et résultat reporté dans le notebook | 0.5 |
| Comparaison avec le prof (longueur moyenne, écart-type, médiane) | 0.5 |
| Visualisation : un agent qui joue (capture, GIF ou utilisation de `play_live.py`) | 0.5 |
| Discussion des **types d'erreurs** observés (boucle infinie, mort sur pomme, etc.) | 0.5 |
| Effet d'au moins **un hyperparamètre** mesuré quantitativement | 1.0 |

---

## Qualité du code *(2 pts)*

| Critère | Pts |
|---|---|
| Notebook propre : cellules ordonnées, exécutées, sorties visibles | 0.5 |
| Pas de variables globales sauvages, pas de copier-coller massif | 0.5 |
| Variables nommées en clair (`alpha`, `gamma`, `Q`, `state`…) | 0.5 |
| Reproductibilité : `seed` fixé pour les tirages aléatoires | 0.5 |

---

## Discussion & justifications *(3 pts)*

C'est ici qu'on **distingue les bons étudiants** : compréhension > exécution.

| Critère | Pts |
|---|---|
| Justification du choix d'α et γ (et leur effet observé) | 1.0 |
| Justification du **schedule** d'ε (pourquoi décroître ? à quelle vitesse ?) | 0.5 |
| Réflexion sur la représentation d'état (limites du 5-tuple ; idées d'enrichissement) | 1.0 |
| Honnêteté sur les limites de l'agent : « il échoue parce que… » | 0.5 |

---

## 🎯 Bonus *Battle the prof* (+1 pt, binaire)

**Critère unique :**
```bash
python3 evaluate.py mon_agent.pkl prof_agent.pkl
```
- Si `mean_length(étudiant) > mean_length(prof)` → **+1 pt**.
- Sinon → **+0**.

**Prérequis pour que le bonus compte :**
- Le `.pkl` est bien produit par le code de l'étudiant (vérifier en relançant
  l'entraînement à la lecture).
- Pas de règle encodée en dur, pas de modification de `snake_env.py` ni
  `evaluate.py`.
- Ce qui est **autorisé** pour gagner : tuner les hyperparamètres, modifier la
  reward shaping (récompenses internes au code étudiant), augmenter le nombre
  d'épisodes, enrichir la représentation d'état (ajouter des features dérivées
  de l'état brut, à condition que ça reste générique).

---

## Conduite de la correction (mémo prof)

1. **Ouvrir le notebook**, vérifier qu'il est **exécuté** (sortie des cellules visibles).
2. Vérifier la **présence** de `mon_agent.pkl` dans le rendu.
3. Lancer le benchmark :
   ```bash
   cd TP-A_Snake/
   python3 evaluate.py rendu/mon_agent.pkl prof_agent.pkl
   ```
4. **Lire le notebook section par section** en cochant la grille ci-dessus.
5. **Relancer une cellule clé** pour s'assurer que le code n'est pas que du
   copier-coller cosmétique (typiquement la cellule de boucle d'entraînement
   sur 50 épisodes avec un `seed` différent).
6. Pour le bonus : interpréter strictement la règle (`>` pas `≥`).

---

## Échelle indicative

| Note | Profil |
|---|---|
| 18-20 | Notebook impeccable, agent qui converge bien, discussion fine, souvent bonus +1 |
| 14-17 | Q-learning correct mais analyse limitée, OU bonne analyse mais agent moyen |
| 10-13 | Algorithme implémenté avec quelques erreurs (Bellman, ε figé, etc.) |
| 6-9 | Briques présentes mais code non fonctionnel ou agent ne converge pas |
| < 6 | Pas de Q-learning identifiable, ou triche manifeste |
