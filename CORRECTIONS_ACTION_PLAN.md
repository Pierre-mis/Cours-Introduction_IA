# Corrections Action Plan

**Priority:** 🔴 HIGH - Must complete before TP assignments
**Estimated Time:** 3-4 hours total
**Difficulty:** Medium

---

## TP5: Q-Learning Correction (CRITICAL)

### Current State
```python
# ... Code Environnement (Voir resources TP ou Correction) ...
SIZE = 5; OBSTACLES = [(1,1), (1,2), (2,2), (3,1), (3,3)]; GOAL = (4,4)
def step(state, action): pass # Placeholder

# ... (Correction complète code Q-Learning) ...
```

**Problem:** No actual implementation provided

### What Needs to be Added

#### 1. Complete Environment Setup
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Grid parameters
SIZE = 5
OBSTACLES = [(1,1), (1,2), (2,2), (3,1), (3,3)]
GOAL = (4, 4)
START = (0, 0)

# Helper function to move in grid
def is_valid(state):
    """Check if state is valid (not obstacle, within bounds)"""
    return (0 <= state[0] < SIZE and
            0 <= state[1] < SIZE and
            state not in OBSTACLES)

def step(state, action):
    """
    Execute action in environment.
    Actions: 0=up, 1=down, 2=left, 3=right
    Returns: (next_state, reward, is_terminal)
    """
    x, y = state
    if action == 0:  # Up
        next_state = (x-1, y)
    elif action == 1:  # Down
        next_state = (x+1, y)
    elif action == 2:  # Left
        next_state = (x, y-1)
    elif action == 3:  # Right
        next_state = (x, y+1)
    else:
        next_state = state

    # Check validity
    if not is_valid(next_state):
        next_state = state
        reward = -0.5
    elif next_state == GOAL:
        reward = 1
    else:
        reward = 0

    is_terminal = next_state == GOAL
    return next_state, reward, is_terminal
```

#### 2. Q-Learning Implementation
```python
# Hyperparameters
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EPSILON = 0.9
NUM_EPISODES = 100
NUM_ACTIONS = 4

# Initialize Q-Table
q_table = {}
for i in range(SIZE):
    for j in range(SIZE):
        if (i, j) not in OBSTACLES:
            q_table[(i, j)] = [0] * NUM_ACTIONS

def choose_action(state):
    """Epsilon-Greedy action selection"""
    if np.random.uniform() < EPSILON:
        return np.random.randint(NUM_ACTIONS)
    else:
        return np.argmax(q_table[state])

# Training loop
print("Training Q-Learning agent...")
for episode in range(NUM_EPISODES):
    state = START
    steps = 0

    while state != GOAL and steps < 50:
        action = choose_action(state)
        next_state, reward, is_terminal = step(state, action)

        # Bellman Equation Update
        current_q = q_table[state][action]
        max_next_q = max(q_table[next_state])
        new_q = current_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * max_next_q - current_q)
        q_table[state][action] = new_q

        state = next_state
        steps += 1

    if (episode + 1) % 20 == 0:
        print(f"Episode {episode + 1}/{NUM_EPISODES}")

print("✓ Training complete!")
```

#### 3. Visualization
```python
# Convert Q-Table to matrix for visualization
q_values = np.zeros((SIZE, SIZE))
for (i, j), actions in q_table.items():
    q_values[i, j] = max(actions)

# Mark obstacles
for obs in OBSTACLES:
    q_values[obs] = -1

# Plot
plt.figure(figsize=(8, 7))
sns.heatmap(q_values, annot=True, fmt='.2f', cmap='RdYlGn',
            cbar_kws={'label': 'Max Q-Value'},
            linewidths=0.5, linecolor='gray')
plt.title("Final Q-Table: Value of Each Grid Position")
plt.xlabel("Column (y)")
plt.ylabel("Row (x)")
plt.text(GOAL[1], GOAL[0], '★', ha='center', va='center', color='blue', fontsize=20)
plt.show()

# Verify learned path
print("\n✓ Learned Policy Verification:")
state = START
path = [state]
for _ in range(50):
    action = np.argmax(q_table[state])
    next_state, reward, is_terminal = step(state, action)
    path.append(next_state)
    state = next_state
    if is_terminal:
        break

print(f"Path found: {path}")
print(f"Path length: {len(path)-1} steps")
print(f"Reached goal: {path[-1] == GOAL}")
```

### Estimated Time: 1.5-2 hours
### Difficulty: Medium (requires understanding Q-Learning concepts)

---

## TP6: NLP Correction (CRITICAL)

### Current State
```python
# ... (Correction complète) ...
```

**Problem:** No implementation at all

### What Needs to be Added

#### 1. Dataset Loading & Preparation
```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Option A: Using pre-made dataset (recommended for simplicity)
# If fetch_20newsgroups is not available
texts = [
    "The patient has diabetes and hypertension",
    "Blood pressure elevated in morning readings",
    "Diagnosis: Type 2 diabetes mellitus",
    "Cancer screening shows suspicious cells",
    "Tumor markers elevated, biopsy recommended",
    "Oncology consultation needed urgently",
    "Normal cholesterol levels today",
    "Healthy BMI and exercise routine",
    "No abnormalities detected in exam"
]
labels = [0, 0, 0, 1, 1, 1, 0, 0, 0]  # 0=Non-urgent, 1=Urgent

# Option B: Using fetch_20newsgroups (if available)
try:
    from sklearn.datasets import fetch_20newsgroups
    categories = ['sci.med', 'talk.religion.misc']
    data = fetch_20newsgroups(subset='all', categories=categories,
                              remove=('headers', 'footers', 'quotes'))
    texts = data.data
    labels = data.target
except:
    print("Note: Using simplified dataset instead of fetch_20newsgroups")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
```

#### 2. TF-IDF Vectorization
```python
# Compare CountVectorizer vs TfidfVectorizer
print("\n=== VECTORIZATION COMPARISON ===\n")

# Count Vectorizer (Bag of Words)
count_vec = CountVectorizer(max_features=100, stop_words='english')
X_train_count = count_vec.fit_transform(X_train)
X_test_count = count_vec.transform(X_test)

print(f"CountVectorizer shape: {X_train_count.shape}")

# TF-IDF Vectorizer (Better!)
tfidf_vec = TfidfVectorizer(max_features=100, stop_words='english')
X_train_tfidf = tfidf_vec.fit_transform(X_train)
X_test_tfidf = tfidf_vec.transform(X_test)

print(f"TfidfVectorizer shape: {X_train_tfidf.shape}")

# Show most important words
print("\n📊 Most Important Words (TF-IDF):")
feature_names = tfidf_vec.get_feature_names_out()
for i in range(min(10, len(feature_names))):
    print(f"  {i+1}. {feature_names[i]}")
```

#### 3. Classifier Training
```python
# Train Naive Bayes on TF-IDF vectors
print("\n=== TRAINING CLASSIFIERS ===\n")

# Naive Bayes
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
nb_score = nb_model.score(X_test_tfidf, y_test)
print(f"Naive Bayes Accuracy: {nb_score:.3f}")

# SVM (alternative)
svm_model = SVC(kernel='linear')
svm_model.fit(X_train_tfidf, y_train)
svm_score = svm_model.score(X_test_tfidf, y_test)
print(f"SVM Accuracy: {svm_score:.3f}")

# Use best model
best_model = nb_model if nb_score > svm_score else svm_model
```

#### 4. Testing & Evaluation
```python
print("\n=== CLASSIFICATION REPORT ===\n")

y_pred = best_model.predict(X_test_tfidf)
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
```

#### 5. Prediction on Custom Text
```python
print("\n=== TESTING ON CUSTOM MEDICAL REPORTS ===\n")

test_reports = [
    "Patient with severe chest pain and elevated troponin levels",
    "Routine annual checkup, all results normal",
    "Acute myocardial infarction suspected, transfer to CCU"
]

test_tfidf = tfidf_vec.transform(test_reports)
predictions = best_model.predict(test_tfidf)

for report, pred in zip(test_reports, predictions):
    label = "🔴 URGENT" if pred == 1 else "🟢 Normal"
    print(f"{label}: '{report[:50]}...'")
```

#### 6. Optional: WordCloud Visualization
```python
try:
    from wordcloud import WordCloud

    # Combine all urgent medical texts
    urgent_texts = ' '.join([texts[i] for i in range(len(texts)) if labels[i] == 1])

    # Create WordCloud
    wordcloud = WordCloud(width=800, height=400,
                         background_color='white').generate(urgent_texts)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Most Common Words in Urgent Medical Reports')
    plt.tight_layout()
    plt.show()
except ImportError:
    print("WordCloud not installed. Skipping visualization.")
```

### Estimated Time: 2-2.5 hours
### Difficulty: Medium (NLP concepts with standard sklearn tools)

---

## TP2: Enhancement (OPTIONAL)

Current TP2 is adequate but could be improved with:

```python
# Add to residual analysis section:

# More detailed residual analysis
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residuals vs Fitted
axes[0, 0].scatter(y_pred_p, residuals)
axes[0, 0].axhline(0, color='r', linestyle='--')
axes[0, 0].set_title('Residuals vs Fitted Values')

# 2. Histogram of residuals
axes[0, 1].hist(residuals, bins=20, edgecolor='black')
axes[0, 1].set_title('Distribution of Residuals')

# 3. Q-Q plot (normality check)
from scipy import stats
stats.probplot(residuals, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot')

# 4. Scale-Location (sqrt standardized residuals)
std_residuals = np.sqrt(np.abs(residuals / residuals.std()))
axes[1, 1].scatter(y_pred_p, std_residuals)
axes[1, 1].set_title('Scale-Location Plot')

plt.tight_layout()
plt.show()

print("\n📊 Residual Diagnostics:")
print(f"Mean of residuals: {residuals.mean():.4f} (should be ~0)")
print(f"Std of residuals: {residuals.std():.4f}")
print(f"Normality (Shapiro-Wilk p-value): {stats.shapiro(residuals)[1]:.4f} (>0.05 = normal)")
```

### Estimated Time: 30 minutes
### Difficulty: Easy (visualization only)

---

## Implementation Checklist

### TP5: Q-Learning
- [ ] Copy environment setup code
- [ ] Create Q-Table initialization
- [ ] Implement choose_action (Epsilon-Greedy)
- [ ] Implement training loop with Bellman updates
- [ ] Add visualization (heatmap)
- [ ] Add path verification
- [ ] Test execution end-to-end
- [ ] Add comments explaining key concepts

### TP6: NLP
- [ ] Choose dataset (fetch_20newsgroups or simplified)
- [ ] Implement TF-IDF vectorization
- [ ] Train Naive Bayes classifier
- [ ] Train SVM classifier (optional)
- [ ] Show evaluation metrics
- [ ] Test on custom medical texts
- [ ] Add WordCloud (optional)
- [ ] Test execution end-to-end
- [ ] Compare TF-IDF vs CountVectorizer

### TP2: Enhancement (Optional)
- [ ] Add residual diagnostic plots
- [ ] Add normality test (Shapiro-Wilk)
- [ ] Add Q-Q plot
- [ ] Document interpretation

---

## Testing Protocol

Before finalizing:

1. **Run each correction notebook end-to-end**
   ```bash
   jupyter nbconvert --to notebook --execute TP5_Correction.ipynb
   ```

2. **Check for errors** - All cells should execute without exceptions

3. **Verify outputs** - Plots should display correctly

4. **Add docstrings** - Explain key functions

5. **Review comments** - Ensure students understand why

---

## Success Criteria

✅ All code cells execute without errors
✅ Visualizations are clear and informative
✅ Each correction provides complete solution
✅ Students can understand logic from comments
✅ Output matches conceptual expectations
✅ French terminology consistent

---

## Timeline

**This Week:**
- Day 1-2: Implement TP5 & TP6 corrections
- Day 3: Test and debug all corrections
- Day 4: Add comments and documentation
- Day 5: Final review before assignment

**Next Week:**
- Assign TPs to students with confidence
- Monitor for feedback on corrections

---

## Notes for Implementation

1. **TP5 Q-Learning:**
   - The grid is 5x5 with obstacles and goal at (4,4)
   - Student must learn optimal path from (0,0) to (4,4)
   - Course section 3.C already explains Epsilon-Greedy and Bellman
   - Visualization should show learned Q-values as heatmap

2. **TP6 NLP:**
   - Use TfidfVectorizer (not CountVectorizer) as per updated course
   - Students should see why TF-IDF works better (removes common words)
   - Include at least one medical domain example
   - Compare Naive Bayes vs SVM performance
   - Course section 9 now explains TF-IDF in detail

3. **TP2 Enhancement:**
   - Not critical but improves learning
   - Shows statistical tests for model assumptions
   - Helps students understand residual diagnostics

---

*Action plan created: March 3, 2026*
*Ready for implementation*
