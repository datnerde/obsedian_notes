---
title: Ensemble Methods
tags: [ml, ensemble, random-forest, boosting]
created: 2026-04-19
status: growing
related: [[Decision Tree]], [[Overfitting and Underfitting]], [[Cross Validation]]
source: Notion ML Coding + ML Proof
---

# Ensemble Methods

> **Core idea:** Combine many weak learners to produce a stronger learner. Two main families: **Bagging** (variance reduction) and **Boosting** (bias reduction).

---

## Why Ensembles Reduce Variance — Proof

For $B$ base models each with variance $\sigma^2$ and pairwise correlation $\rho$:

$$\text{Var}(\bar{f}) \approx \rho\sigma^2 + \frac{1-\rho}{B}\sigma^2$$

- If $\rho = 1$ (identical models): no benefit — $\text{Var} = \sigma^2$
- If $\rho = 0$ (independent models): $\text{Var} = \sigma^2/B$ — $B$-fold reduction
- **Key lever:** reducing $\rho$ (model diversity) matters more than increasing $B$

This is why Random Forest uses random feature subsets at each split — it *decorrelates* trees beyond what bootstrap sampling alone achieves.

---

## Random Forest

**Algorithm:**
1. Draw $B$ bootstrap samples from training data
2. For each sample, grow a full decision tree — but at each split, consider only $m \approx \sqrt{p}$ random features
3. Aggregate via majority vote (classification) or mean (regression)

**Why it works:**
- Bagging reduces variance (trees are high-variance learners)
- Feature subsampling reduces inter-tree correlation $\rho$ → further variance reduction
- OOB (out-of-bag) samples ≈ 36.8% per tree → free validation estimate without a held-out set

**Hyperparameters:**
- `n_estimators`: more trees → lower variance (diminishing returns after ~100–200)
- `max_features`: controls $\rho$; `sqrt` for classification, all features or `log2` for regression
- `max_depth`: controls individual tree variance

---

## AdaBoost

**Algorithm (binary classification):**
1. Initialize uniform sample weights $w_i = 1/n$
2. For $t = 1 \ldots T$:
   - Fit weak learner (decision stump) on weighted dataset
   - Compute weighted error: $\epsilon_t = \sum_i w_i \cdot \mathbb{1}[y_i \neq \hat{y}_i]$
   - Compute model weight: $\alpha_t = \frac{1}{2}\ln\frac{1-\epsilon_t}{\epsilon_t}$
   - Update weights: $w_i \leftarrow w_i \exp(-\alpha_t y_i \hat{y}_i)$, then normalize
3. Final prediction: $\hat{y} = \text{sign}\left(\sum_t \alpha_t h_t(x)\right)$

**Key properties:**
- Exponentially reweights misclassified samples → subsequent learners focus on hard examples
- Reduces **bias** (unlike bagging which reduces variance)
- Sensitive to noisy labels (noisy samples get ever-increasing weights)

---

## Gradient Boosting (Residual Fitting)

Each new tree fits the **pseudo-residuals** (negative gradient of loss):

$$F_t(x) = F_{t-1}(x) + \eta \cdot h_t(x)$$

where $h_t$ minimizes $\sum_i L(y_i, F_{t-1}(x_i) + h_t(x_i))$.

For MSE loss: pseudo-residuals = actual residuals $r_i = y_i - F_{t-1}(x_i)$.

**XGBoost / LightGBM** extend this with second-order Taylor expansion of the loss for faster optimization.

---

## Bagging vs Boosting

| | Bagging | Boosting |
|---|---|---|
| **Trains on** | Bootstrap samples (independent) | Weighted/reweighted data (sequential) |
| **Reduces** | Variance | Bias (+ some variance) |
| **Parallelizable** | Yes | No |
| **Overfit risk** | Low | Higher (can overfit noisy data) |
| **Example** | Random Forest | AdaBoost, XGBoost, LightGBM |

---

## Boosting Algorithm Comparison (Interview Cheat Sheet)

| Algorithm | Core Idea | Key Strengths | Weaknesses | Interview Tip |
|---|---|---|---|---|
| **AdaBoost** | Sequentially reweights misclassified samples | Simple, intuitive, works on clean data | Sensitive to noise/outliers | Emphasize *sample reweighting* |
| **GBM** | Sequentially fits residuals via gradient descent | Flexible (custom loss functions), general framework | Slow training, can overfit | Highlight *residual fitting (gradients)* |
| **XGBoost** | GBM + regularization (L1/L2), parallel training, handles missing values | Strong performance, robust, efficient | Many hyperparameters, overfitting risk without tuning | Mention *regularization + efficiency* |
| **LightGBM** | Histogram-based splits, leaf-wise growth (deepest leaf with max gain) | Extremely fast, memory efficient, handles categorical features | Can overfit small datasets, sensitive to hyperparams | Stress *speed + scalability* |
| **CatBoost** | Ordered boosting + efficient categorical encoding | Great on categorical-heavy data, minimal preprocessing | Slower than LightGBM | Point out *categorical handling advantage* |

→ For hyperparameter tuning order and RF vs XGBoost Q&A, see [[Interview-ML-Tips]].

---

## From-Scratch Reference

→ See [[ML-Coding-Patterns]] for NumPy implementations of K-Means, Decision Tree, Random Forest, AdaBoost.
