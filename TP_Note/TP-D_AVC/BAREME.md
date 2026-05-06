# Grille de notation — TP-D Risque d'AVC (Classification déséquilibrée)

> Note finale sur **20**, plus un **bonus de +1** indépendant.
> La note ne dépasse pas 21/20.

> ⚠️ **Spécificité de ce TP :** la cible est **fortement déséquilibrée** (~5 % de positifs)
> et le contexte est **médical** (un faux négatif est plus grave qu'un faux positif).
> Une bonne partie du barème porte sur le fait que tu en tires les conséquences.

---

## Vue d'ensemble

| Bloc | Points |
|---|---|
| 1. EDA & compréhension | **2.5** |
| 2. Préparation (NaN, encodage, split) | **3** |
| 3. Baseline triviale & critique de l'accuracy | **1.5** |
| 4. Modélisation (≥ 3, dont `class_weight`) | **3.5** |
| 5. Évaluation (F1, rappel, AUC, courbes) | **3.5** |
| 6. Ajustement du seuil (justifié par le contexte) | **3** |
| Qualité du code | **1.5** |
| Rapport & communication | **1.5** |
| **Total** | **/20** |
| 🎯 Bonus *SMOTE vs class_weight* | **+1** |

---

## Pénalités

| Motif | Sanction |
|---|---|
| Notebook non exécuté | **−1 pt** |
| Notebook qui crash au `Run All` | **−3 pts** |
| Pas de markdown explicatif | **−4 pts** |
| **Fuite de données** (imputation/scaling fittés sur tout `X`) | **−3 pts** |
| Accuracy comme métrique principale sans discussion | **−2 pts** |
| Un seul modèle comparé | **−2 pts** |
| Plagiat manifeste | **note ramenée à 0** |

---

## Étape 1 — EDA *(2.5 pts)*

| Critère | Pts |
|---|---|
| Distribution de la target chiffrée et commentée (« ~5 %, c'est très déséquilibré ») | 0.5 |
| Valeurs manquantes identifiées (notamment **BMI**) | 0.5 |
| Distribution des features numériques par classe (au moins 2 plots) | 0.5 |
| Encodage des variables catégorielles inspecté (combien de modalités, déséquilibre intra-feature) | 0.5 |
| Conclusion d'EDA listant les défis avant de modéliser | 0.5 |

---

## Étape 2 — Préparation *(3 pts)*

| Critère | Pts |
|---|---|
| Imputation des NaN du BMI **justifiée** (médiane / KNN / autre) | 1.0 |
| Encodage des catégorielles cohérent (one-hot / ordinal selon le sens) | 0.5 |
| Train/test split **stratifié** sur `stroke` avec `random_state` | 0.5 |
| Imputeur et scaler fittés **sur le train uniquement** (idéalement `Pipeline`) | 1.0 |

❌ `SimpleImputer().fit(X)` avant le split → −3 pts (fuite).

---

## Étape 3 — Baseline triviale *(1.5 pt)*

| Critère | Pts |
|---|---|
| Accuracy d'un classifieur "toujours 0" calculée et reportée | 0.5 |
| Discussion : pourquoi ~95 % d'accuracy ne signifie pas qu'on a un bon modèle | 1.0 |

---

## Étape 4 — Modélisation *(3.5 pts)*

**Attendu :** ≥ 3 modèles, dont **au moins un avec** `class_weight='balanced'` et **un sans**, pour mesurer l'effet.

| Critère | Pts |
|---|---|
| ≥ 3 modèles entraînés avec `random_state` fixé | 1.5 |
| Comparaison explicite `class_weight=None` vs `class_weight='balanced'` | 1.0 |
| Choix des modèles justifié | 0.5 |
| Hyperparamètres motivés | 0.5 |

---

## Étape 5 — Évaluation *(3.5 pts)*

| Critère | Pts |
|---|---|
| **F1, rappel, AUC** reportés pour chaque modèle (accuracy seule = insuffisant) | 1.0 |
| Matrice de confusion affichée et **commentée** (combien de patients ratés ?) | 1.0 |
| Courbe **précision-rappel** tracée | 0.5 |
| Courbe **ROC** tracée | 0.5 |
| Tableau récapitulatif des modèles | 0.5 |

❌ Matrice de confusion sans commenter le nombre de FN → −1 pt.

---

## Étape 6 — Ajustement du seuil *(3 pts)*

C'est ici qu'on **distingue les bonnes copies**.

| Critère | Pts |
|---|---|
| Courbes précision / rappel / F1 vs seuil tracées | 1.0 |
| Choix d'un seuil **différent de 0.5**, motivé par le **contexte clinique** (FN coûteux) | 1.5 |
| Comparaison de la matrice de confusion avant/après ajustement | 0.5 |

⚠️ Choisir le seuil qui maximise le F1 sans mentionner que le contexte demande de privilégier le rappel = OK partiel (1.5/3).

---

## Qualité du code *(1.5 pt)*

| Critère | Pts |
|---|---|
| Notebook exécuté linéairement, pas d'erreur, sorties visibles | 0.5 |
| Variables nommées clairement, pas de duplication massive | 0.5 |
| Reproductibilité (`random_state` partout où il y a un tirage) | 0.5 |

---

## Rapport & communication *(1.5 pt)*

| Critère | Pts |
|---|---|
| Markdown explicatif entre les sections | 0.5 |
| Figures titrées et commentées | 0.5 |
| Conclusion synthétique : « si je devais déployer ce modèle, je… » | 0.5 |

---

## 🎯 Bonus — `SMOTE` vs `class_weight` (+1 pt)

| Critère | Pts |
|---|---|
| `SMOTE` implémenté correctement (sur **train uniquement**, jamais sur le test) | 0.5 |
| Comparaison chiffrée avec `class_weight` (F1, rappel, AUC) + interprétation | 0.5 |

⚠️ `SMOTE` appliqué avant le split = fuite. Bonus invalidé + −1 pt.

---

## Échelle indicative

| Note | Profil |
|---|---|
| 18-20 | Méthodologie clinique aboutie : seuil ajusté, discussion FN/FP fine, bonus traité |
| 14-17 | Bonne pratique du déséquilibre, ajustement de seuil présent mais peu argumenté |
| 10-13 | Modèles fonctionnent mais accuracy mise en avant, ou seuil non discuté |
| 6-9 | Étapes manquantes, ou fuite de données détectée |
| < 6 | Aucune prise en compte du déséquilibre, ou problème majeur |
