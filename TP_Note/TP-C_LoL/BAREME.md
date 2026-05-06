# Grille de notation — TP-C League of Legends (Classification)

> Note finale sur **20**, plus un **bonus de +1** indépendant.
> La note ne dépasse pas 21/20.

---

## Vue d'ensemble

| Bloc | Points |
|---|---|
| 1. EDA & compréhension des données | **3** |
| 2. Préparation (split, scaling, fuite) | **3** |
| 3. Modélisation (≥ 3 modèles, justifications) | **4** |
| 4. Évaluation (métriques, courbes, matrice) | **4** |
| 5. Cross-validation sur le meilleur modèle | **1.5** |
| 6. Feature importance & interprétation | **2.5** |
| Qualité du code | **1** |
| Rapport & communication | **1** |
| **Total** | **/20** |
| 🎯 Bonus *robustesse au patch* | **+1** |

---

## Pénalités

| Motif | Sanction |
|---|---|
| Notebook non exécuté (cellules vides au rendu) | **−1 pt** |
| Notebook qui crash au `Run All` | **−3 pts** |
| Pas de markdown explicatif (juste du code) | **−4 pts** |
| **Fuite de données** (`scaler.fit(X)` avant le split, target dans X, etc.) | **−2 pts** |
| Un seul modèle comparé (au lieu de 3) | **−2 pts** |
| Plagiat manifeste d'un notebook Kaggle sans citation | **note ramenée à 0** |

---

## Étape 1 — EDA & compréhension *(3 pts)*

| Critère | Pts |
|---|---|
| Distribution de la target affichée + commentée (équilibrée ou non ?) | 0.5 |
| Au moins 3 plots commentés (corrélations, distributions, outliers) | 1.0 |
| Identification d'au moins **une feature proxy** (`redGoldDiff` vs `blueGoldDiff` etc.) | 0.5 |
| Identification d'éventuels NaN / outliers / doublons | 0.5 |
| Conclusion d'EDA : « ce que je retiens avant de modéliser » | 0.5 |

❌ `df.describe()` sans aucune lecture → 0.5 pt max sur ce bloc.

---

## Étape 2 — Préparation *(3 pts)*

| Critère | Pts |
|---|---|
| Train/test split **stratifié** 80/20 avec `random_state` | 1.0 |
| Standardisation (si pertinente pour les modèles utilisés), **fit sur le train uniquement** | 1.0 |
| Suppression des colonnes redondantes ou justification de leur conservation | 0.5 |
| `Pipeline` ou code clairement séparant train/test | 0.5 |

⚠️ `scaler.fit(X)` avant le split = fuite → −2 pts (cumulable avec la pénalité ci-dessus uniquement si vraiment grossier).

---

## Étape 3 — Modélisation *(4 pts)*

**Attendu :** au moins 3 modèles parmi LogReg, Random Forest, KNN, SVM, GradientBoosting.

| Critère | Pts |
|---|---|
| 3 modèles bien implémentés et entraînés | 1.5 |
| Justification du choix (au moins 1 phrase par modèle) | 1.0 |
| Hyperparamètres motivés (au moins 1 modèle a fait l'objet d'un tuning même léger) | 1.0 |
| Reproductibilité : `random_state` fixé partout | 0.5 |

❌ 2 modèles seulement → −2 pts. ❌ 1 seul modèle → −3 pts.

---

## Étape 4 — Évaluation *(4 pts)*

| Critère | Pts |
|---|---|
| Accuracy, précision, rappel, F1, AUC-ROC reportés pour chaque modèle | 1.5 |
| Matrice de confusion affichée et **commentée** | 1.0 |
| Courbe ROC tracée (idéalement plusieurs courbes superposées) | 0.5 |
| Discussion de la métrique la plus pertinente pour le contexte | 0.5 |
| Tableau récapitulatif des modèles | 0.5 |

❌ Accuracy seule discutée → −2 pts. ❌ Matrice de confusion sans commentaire → −1 pt.

---

## Étape 5 — Cross-validation *(1.5 pt)*

| Critère | Pts |
|---|---|
| 5-fold CV sur le meilleur modèle, métrique cohérente avec l'étape 4 | 1.0 |
| Discussion : le score hold-out est-il représentatif ? | 0.5 |

---

## Étape 6 — Feature importance & interprétation *(2.5 pts)*

| Critère | Pts |
|---|---|
| Feature importance calculée (coefficients LogReg ou `feature_importances_`) | 0.5 |
| Top 5-10 features visualisées | 0.5 |
| **Interprétation métier** : est-ce surprenant ? attendu ? | 1.0 |
| Réflexion sur les features proxy / redondantes / à exclure pour un déploiement | 0.5 |

---

## Qualité du code *(1 pt)*

| Critère | Pts |
|---|---|
| Cellules exécutées dans l'ordre, pas d'erreur visible | 0.5 |
| Variables nommées clairement, pas de duplication massive | 0.5 |

---

## Rapport & communication *(1 pt)*

| Critère | Pts |
|---|---|
| Markdown explicatif entre les sections (introduction, transitions) | 0.5 |
| Conclusion synthétique répondant à « peut-on prédire la victoire à 10 min ? » | 0.5 |

---

## 🎯 Bonus — Robustesse au patch (+1 pt)

**Critère :** discussion argumentée — le dataset vient d'un patch précis ; ton modèle généraliserait-il à un patch ultérieur ? Quels signaux te le feraient soupçonner ?

| Niveau | Pts |
|---|---|
| Discussion fine : identifie au moins 2 features qui pourraient devenir biaisées suite à un changement de méta | 1.0 |
| Discussion superficielle (« ça dépend du patch ») | 0.5 |
| Absente | 0.0 |

---

## Échelle indicative

| Note | Profil |
|---|---|
| 18-20 | EDA fine, méthodologie irréprochable, interprétation experte des features, bonus traité |
| 14-17 | Tout l'essentiel est là, interprétation honnête mais perfectible |
| 10-13 | Modèles fonctionnent mais analyse superficielle ou choix méthodologiques discutables |
| 6-9 | Étapes manquantes, ou erreurs méthodologiques importantes (1 modèle, accuracy seule…) |
| < 6 | Travail très incomplet, ou problème majeur (fuite, plagiat partiel) |
