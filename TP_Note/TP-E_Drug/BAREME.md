# Grille de notation — TP-E Avis de médicaments (NLP / sentiment)

> Note finale sur **20**, plus un **bonus de +1** indépendant.
> La note ne dépasse pas 21/20.

---

## Vue d'ensemble

| Bloc | Points |
|---|---|
| 1. EDA texte | **2.5** |
| 2. Construction de la cible & préparation | **2.5** |
| 3. Vectorisation (Count vs TF-IDF, chiffrée) | **3** |
| 4. Modélisation (≥ 2 modèles) | **3** |
| 5. Évaluation (accuracy, F1, matrice) | **2.5** |
| 6. Mots les plus prédictifs (top 20 par classe) | **2** |
| 7. Analyse critique des erreurs (≥ 3 exemples) | **2.5** |
| Qualité du code | **1** |
| Rapport & communication | **1** |
| **Total** | **/20** |
| 🎯 Bonus *Hugging Face pipeline* | **+1** |

---

## Pénalités

| Motif | Sanction |
|---|---|
| Notebook non exécuté | **−1 pt** |
| Notebook qui crash au `Run All` | **−3 pts** |
| Pas de markdown explicatif | **−4 pts** |
| **Fuite de données** (vectorizer fitté sur tout le corpus avant split) | **−3 pts** |
| Sous-échantillonnage non fait (200k+ avis traités sans raison → notebook qui prend 30 min) | **−1 pt** |
| Plagiat manifeste | **note ramenée à 0** |

---

## Étape 1 — EDA texte *(2.5 pts)*

| Critère | Pts |
|---|---|
| Distribution des `rating` (1-10) tracée et commentée | 0.5 |
| Distribution de la **longueur des avis** (en mots ou caractères) | 0.5 |
| Top mots fréquents **sans stop-words** | 0.5 |
| Top mots fréquents **avec stop-words** (pour montrer l'intérêt du filtrage) | 0.5 |
| Conclusion d'EDA listant les particularités du corpus (vocabulaire médical, biais lexicaux possibles) | 0.5 |

---

## Étape 2 — Construction de la cible & préparation *(2.5 pts)*

| Critère | Pts |
|---|---|
| Binarisation correcte : `positif` si rating ≥ 7, `négatif` si rating ≤ 4, **rejet 5-6** | 1.0 |
| Train/test split **stratifié** sur le label, `random_state` fixé | 0.5 |
| Sous-échantillonnage à 20 000 avis appliqué et chiffré | 0.5 |
| Distribution des classes après binarisation chiffrée | 0.5 |

---

## Étape 3 — Vectorisation *(3 pts)*

| Critère | Pts |
|---|---|
| `CountVectorizer` implémenté correctement | 0.5 |
| `TfidfVectorizer` implémenté correctement | 0.5 |
| Vectorizers fittés **sur le train uniquement** | 1.0 |
| **Comparaison chiffrée** Count vs TF-IDF (au moins F1 ou accuracy par modèle) | 0.5 |
| Explication conceptuelle : pourquoi TF-IDF est généralement meilleur | 0.5 |

❌ Affirmer que TF-IDF est mieux **sans le mesurer** → −1 pt.

---

## Étape 4 — Modélisation *(3 pts)*

**Attendu :** ≥ 2 modèles (LogReg, MultinomialNB minimum). Optionnel : SVM linéaire.

| Critère | Pts |
|---|---|
| ≥ 2 modèles entraînés avec `random_state` fixé | 1.5 |
| Justification du choix des modèles (au moins 1 phrase chacun) | 0.5 |
| Hyperparamètres motivés (au moins 1 modèle a fait l'objet d'un essai conscient) | 0.5 |
| Tableau comparatif Count×modèle vs TF-IDF×modèle (matrice 2×2 minimum) | 0.5 |

---

## Étape 5 — Évaluation *(2.5 pts)*

| Critère | Pts |
|---|---|
| Accuracy + F1 reportés pour chaque (vectorizer, modèle) | 1.0 |
| Matrice de confusion affichée pour le meilleur modèle, **commentée** | 1.0 |
| Précision/rappel par classe discutés | 0.5 |

---

## Étape 6 — Mots les plus prédictifs *(2 pts)*

| Critère | Pts |
|---|---|
| Top 20 mots **positifs** affichés (coefficients du modèle linéaire) | 0.5 |
| Top 20 mots **négatifs** affichés | 0.5 |
| Visualisation lisible (barplot horizontal, ou tableau ordonné) | 0.5 |
| Commentaire : ces mots sont-ils sémantiquement cohérents ? | 0.5 |

---

## Étape 7 — Analyse critique des erreurs *(2.5 pts)*

C'est ici qu'on **distingue les bonnes copies**.

| Critère | Pts |
|---|---|
| ≥ 3 exemples mal classés affichés intégralement (texte + label vrai + label prédit) | 0.5 |
| Pour chaque exemple, **explication** du pourquoi (sarcasme, négation, vocabulaire ambigu…) | 1.0 |
| Identification d'un **biais de domaine** : pathologie / nom de médicament qui corrèle avec la classe | 1.0 |

❌ « Le modèle s'est trompé » sans explication → 0 pt sur la ligne d'analyse.

---

## Qualité du code *(1 pt)*

| Critère | Pts |
|---|---|
| Notebook exécuté linéairement, sorties visibles | 0.5 |
| Variables nommées clairement, pas de duplication massive | 0.5 |

---

## Rapport & communication *(1 pt)*

| Critère | Pts |
|---|---|
| Markdown explicatif entre les sections | 0.5 |
| Conclusion : « peut-on classer automatiquement ? Quelles limites en santé ? » | 0.5 |

---

## 🎯 Bonus — Pipeline Hugging Face (+1 pt)

| Critère | Pts |
|---|---|
| `pipeline("sentiment-analysis")` chargé et appliqué sur un échantillon du test | 0.5 |
| Comparaison chiffrée avec ton meilleur modèle local + discussion (le pré-entraîné est-il vraiment meilleur sur ce corpus très spécifique ?) | 0.5 |

⚠️ Si Hugging Face n'est pas installable sur la machine de l'épreuve, ce bonus est neutralisé (pas de pénalité).

---

## Échelle indicative

| Note | Profil |
|---|---|
| 18-20 | Comparaison chiffrée Count/TF-IDF, mots prédictifs interprétés, biais de domaine identifié finement, bonus traité |
| 14-17 | Pipeline NLP maîtrisé, analyse d'erreurs présente mais perfectible |
| 10-13 | Modèles fonctionnent mais comparaison superficielle, peu d'analyse qualitative |
| 6-9 | Étapes manquantes, ou méthodologie discutable (fuite, single model…) |
| < 6 | Travail très incomplet, ou plagiat partiel |
