---
title: ML Coding Patterns (From Scratch)
tags: [ml, coding, interview, numpy]
created: 2026-04-19
status: growing
related: [[Ensemble-Methods]], [[Logistic Regression]], [[K-Means Clustering]], [[PCA]]
source: Notion ML Coding
---

# ML Coding Patterns (From Scratch)

> Reference for from-scratch NumPy implementations. Interview coverage tier: ✅ Must-know · ⚪ Optional.

---

## Coverage Map

| Algorithm | Tier | Key Pattern |
|---|---|---|
| K-Means | ✅ | centroid update, L2 distance |
| Linear Regression | ✅ | normal equation + gradient descent |
| Logistic Regression | ✅ | sigmoid, cross-entropy gradient |
| Softmax Regression | ✅ | multiclass, one-hot, softmax stability |
| PCA (SVD) | ✅ | data centering, projection |
| Decision Tree | ✅ | Gini/Entropy split, recursive build |
| Random Forest | ✅ | bootstrap, feature subset, majority vote |
| AdaBoost | ✅ | weighted error, alpha, weight update |
| Naive Bayes (Gaussian + Multinomial) | ✅ | MLE priors + likelihoods, Laplace smoothing |
| K-NN | ✅ | euclidean distance, majority vote |
| SVM (hinge loss) | ⚪ | linear margin, sub-gradient |
| 2-Layer NN + Backprop | ⚪ | ReLU, chain rule |
| Scaled Dot-Product Attention | ⚪ | $QK^T/\sqrt{d}$, softmax, multiply $V$ |

---

## Common NumPy Patterns

### Distance computation (vectorized)
```python
# L2 distance between each query row and all centroids
# X: (n, d), centroids: (k, d)
dists = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))  # (k, n)
labels = np.argmin(dists, axis=0)  # (n,)
```

### Softmax (numerically stable)
```python
def softmax(z):
    z = z - np.max(z, axis=1, keepdims=True)  # subtract max for stability
    return np.exp(z) / np.sum(np.exp(z), axis=1, keepdims=True)
```

### Add bias column
```python
X_bias = np.c_[np.ones(X.shape[0]), X]
```

### Sigmoid (with clipping)
```python
def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))
```

### One-hot encode
```python
y_one_hot = np.eye(n_classes)[y]  # y is integer array
```

---

## ML Pipeline (sklearn reference)
```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV, KFold

pre = ColumnTransformer([
    ("num", StandardScaler(), FEAT_NUM),
    ("cat", OneHotEncoder(handle_unknown="ignore"), FEAT_CAT)
])
pipe = Pipeline([("pre", pre), ("model", Ridge())])
gs = GridSearchCV(pipe, param_grid, scoring="neg_root_mean_squared_error",
                  cv=KFold(5, shuffle=True, random_state=42), n_jobs=-1)
gs.fit(X_tr, y_tr)
```

---

## Interview Strategy

- Memorize **formulas + pseudocode** for ✅ items — practice writing in pure NumPy in 10–15 min
- For ⚪ items: know the **conceptual level** — what it does and why
- Start with clarifying questions, verbalize reasoning while coding (pair-programming mindset)
- Always test with a simple example and edge cases after writing

---

## Related Concept Notes

- [[K-Means Clustering]] — theory + convergence
- [[Logistic Regression]] — math derivation
- [[PCA]] — eigendecomposition, SVD connection
- [[Ensemble-Methods]] — RF + AdaBoost theory
- [[Backpropagation]] — neural network gradient derivation
