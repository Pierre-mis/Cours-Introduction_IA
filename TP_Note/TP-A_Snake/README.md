# TP-A — Snake (RL Q-Learning)

Tout ce qu'il te faut pour le TP-A est dans ce dossier.

## Fichiers fournis

| Fichier | Rôle |
|---|---|
| `starter.ipynb` | Notebook de prise en main : couvre l'étape 1 du barème, te donne la baseline aléatoire et te montre comment regarder le prof jouer. **Démarre par là.** |
| `snake_env.py` | Environnement Snake. **Tu ne dois pas le modifier.** |
| `evaluate.py` | Benchmark commun (200 épisodes, seeds fixes). Sert pour le bonus "Battle the prof". |
| `prof_agent.pkl` | Q-table de mon agent de référence. Score : **longueur moyenne 18.80**. |
| `play_live.py` | Regarde un agent jouer **en direct** dans une fenêtre matplotlib. Très utile pour debug : tu vois immédiatement les comportements bizarres. |
| `BAREME.md` | Détail de la notation par étape. À lire avant de commencer. |

## Démarrage rapide

```python
from snake_env import SnakeEnv

env = SnakeEnv(grid=8, seed=42)
state = env.reset()
print(state)               # ex : (0, 0, 1, 1, -1)

state, reward, done = env.step(action=1)   # 1 = aller tout droit
env.render()               # affichage matplotlib
```

## Format de l'agent

Ton agent est une **Q-table** sous forme de `dict[tuple, np.ndarray]` :

```python
Q = {
    (0, 0, 1, 1, -1): np.array([0.5, 1.2, -0.3]),  # Q-values pour les 3 actions
    ...
}
```

Pour le sauvegarder en vue du benchmark :

```python
import pickle
with open("mon_agent.pkl", "wb") as f:
    pickle.dump(Q, f)
```

## Voir un agent jouer en direct

```bash
python3 play_live.py prof_agent.pkl              # vitesse par défaut
python3 play_live.py mon_agent.pkl --fps 15      # plus rapide
python3 play_live.py mon_agent.pkl --seed 7      # seed fixe (reproductible)
```

Une fenêtre s'ouvre, l'agent enchaîne les épisodes en boucle. Ferme la fenêtre pour quitter.

## Lancer le benchmark

```bash
# Évaluer ton agent seul
python3 evaluate.py mon_agent.pkl

# Comparer avec le prof
python3 evaluate.py mon_agent.pkl prof_agent.pkl
```

Sortie typique :

```
Benchmark Snake — 200 épisodes (seeds 0..199)

Agent                               |Q|   longueur   écart-type    médiane
--------------------------------------------------------------------------
mon_agent.pkl                       128      19.42         5.10       20.0
prof_agent.pkl                       64      18.80         5.37       19.0

✅ mon_agent.pkl bat prof_agent.pkl de +0.62 cases.
```

## Bonus "Battle the prof"

- Critère : `longueur_moyenne_étudiant > longueur_moyenne_prof` strictement, sur le benchmark commun (200 épisodes, seeds 0..199).
- Bonus : **+1 point** sur la note finale du TP. Binaire — pas de "presque".
- Tu peux tout faire pour gagner :
  - tuner les hyperparamètres (α, γ, ε, schedule de décroissance)
  - modifier la fonction de récompense (en gardant le même env)
  - augmenter le nombre d'épisodes d'entraînement
  - **enrichir la représentation d'état** (par exemple : ajouter la longueur du serpent, ou un capteur de danger à distance 2)
- **Tu n'as pas le droit de** : modifier `snake_env.py`, modifier `evaluate.py`, encoder en dur des règles du jeu (ex : "si pomme à gauche, tourner à gauche").

## Comment je note le bonus

Au rendu, je lance :

```bash
python3 evaluate.py ton_agent.pkl prof_agent.pkl
```

Si l'écart est > 0, tu as +1. Sinon, +0.

## Conseil

Ne te lance pas dans le bonus avant d'avoir fini les étapes 1 à 7. Mon agent (longueur moyenne **18.80** sur le benchmark) a été entraîné avec les hyperparamètres "standards" décrits ci-dessous — donc reproduire le même schéma ne suffit pas pour me battre. Pour gagner +1, il faut **améliorer** quelque chose : enrichir la représentation d'état, ajouter une reward shaping, ou pousser plus loin l'entraînement (plus d'épisodes, schedule d'ε mieux choisi). Mais si ta méthode est mauvaise sur les étapes notées, le bonus ne te sauvera pas.

---

## Indications pour démarrer (Q-Learning sur Snake)

> Tu as fait Q-Learning au TP5 sur une grille 5×5 fixe. Snake apporte **deux nouveautés** :
> 1. l'état n'est plus `(i, j)` mais un **5-tuple** → la Q-Table doit être un `dict`, pas un tableau 2D ;
> 2. tu ne connais pas tous les états à l'avance → **lazy init** (on crée la clé au premier accès).

### Squelette à compléter

```python
import pickle, numpy as np
from snake_env import SnakeEnv

# 1. Hyperparamètres — ceux du prof comme point de départ raisonnable
ALPHA, GAMMA = 0.2, 0.95
EPS_START, EPS_END = 1.0, 0.01
EPISODES, MAX_STEPS = 5000, 500

env = SnakeEnv(grid=8, seed=42)
rng = np.random.default_rng(42)

# 2. Q-Table : dict[tuple, np.ndarray(3)]   ← PAS un tableau 2D comme au TP5 !
Q = {}

# 3. Politique ε-greedy
def get_action(state, eps):
    # TODO : lazy-init Q[state] si absent ;
    #        avec proba eps → action aléatoire dans {0, 1, 2} ;
    #        sinon → argmax de Q[state].
    ...

# 4. Boucle d'entraînement
eps = EPS_START
lengths = []
for ep in range(EPISODES):
    s = env.reset()
    steps = 0
    while not env.done and steps < MAX_STEPS:
        a = get_action(s, eps)
        s2, r, done = env.step(a)
        # TODO : lazy-init Q[s2] AVANT de prendre le max
        # TODO : appliquer Bellman -- attention au cas terminal (done=True → max Q(s',·) = 0)
        s = s2
        steps += 1
    lengths.append(env.length)
    # TODO : décroître eps (linéaire, géométrique… choix à toi, à justifier)

# 5. Sauvegarde
with open("mon_agent.pkl", "wb") as f:
    pickle.dump(Q, f)
```

Reste à toi : la fonction ε-greedy, la mise à jour de Bellman (avec le cas terminal), le schedule d'ε, **et tout ce qui est analyse** (courbes, ablation, discussion). Les 4 `TODO` ci-dessus correspondent aux points où le barème distingue les bonnes copies des moyennes — ne les expédie pas.

### Pour le bonus, où chercher

Trois leviers (du moins risqué au plus ambitieux) :

1. **Pousser l'entraînement** : 20 000 épisodes au lieu de 5 000, ε qui descend moins bas (0.05 plutôt que 0.01 → garde un peu d'exploration), voire évaluer pendant l'entraînement et garder la meilleure snapshot.
2. **Reward shaping** : pénaliser un peu plus les pas qui éloignent de la pomme (distance de Manhattan). Attention à ne pas dénaturer la tâche.
3. **Enrichir la représentation d'état** (le plus payant) : ajouter par exemple un capteur de danger à 2 cases, ou la longueur courante du serpent. Plus d'états → Q-Table plus grosse → besoin de plus d'épisodes pour la remplir.

### Symptômes à reconnaître pendant le debug

Plutôt que des "pièges à éviter", voici les **signes** qu'un truc cloche dans ton implémentation. À toi d'identifier *quoi*.

- **`KeyError` qui apparaît parfois en cours d'entraînement** → réfléchis à quels `Q[...]` tu accèdes, et à quel moment chacun doit déjà exister dans ton dict.
- **La longueur moyenne stagne autour de 2-3 même après 5000 épisodes** → ton agent n'apprend pas. Revérifie chaque terme de ton update Bellman : qu'est-ce qui appartient à l'état *présent* ? Qu'est-ce qui appartient à l'état *suivant* ?
- **L'agent semble apprendre puis se dégrade brutalement** → regarde l'évolution de ε au cours du temps. Est-ce que c'est ce que tu voulais ?
- **L'agent meurt souvent juste après avoir mangé une pomme** → quel signal ton update donne-t-elle à un état où `done=True` ? Y a-t-il vraiment un "état suivant" pertinent ?
- **Score d'évaluation très bruité d'un run à l'autre** → quel est le rôle de ε pendant l'entraînement ? Et pendant l'évaluation ? Sont-ils censés être les mêmes ?
