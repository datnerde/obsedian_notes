---
title: Decision Tree
tags: [ml, supervised-learning, classification, models]
created: 2026-04-14
status: growing
related: [[Classic Model]], [[Overfitting and Underfitting]], [[Feature Normalization]], [[Supervised Learning]]
source: Quest for Machine Learning
---

# Decision Tree

## Core Idea
Recursively split data by asking questions about features, forming a tree where each leaf is a prediction. Splits are chosen to maximize **information gain** (or minimize impurity).

## Split Criteria
| Algorithm | Criterion | Type |
|-----------|-----------|------|
| ID3 | Information Gain (Entropy) | Classification |
| C4.5 | Gain Ratio (normalized IG) | Classification |
| CART | Gini Impurity | Classification |
| CART | MSE reduction | Regression |

`Gini = 1 - Σ pᵢ²` — 0 means pure, 0.5 means maximally impure (binary case)

## Pruning (Controlling Overfitting)
Decision trees **overfit easily** — a fully grown tree memorizes training data.

### Pre-Pruning (Early Stopping)
Stop splitting when:
- Tree reaches max depth
- Node has fewer than min_samples samples
- Split doesn't improve impurity by more than a threshold

### Post-Pruning
Grow the full tree, then prune:
- **REP** (Reduced Error Pruning): if removing a subtree doesn't worsen validation accuracy, remove it
- **Cost Complexity Pruning** (used by scikit-learn): minimize `cost + α × tree_size`; α controls the tradeoff

## Key Properties
- ✅ No need for [[Feature Normalization]] — invariant to monotonic transformations
- ✅ Handles both categorical and numerical features
- ✅ Interpretable — can visualize the tree
- ❌ High variance — sensitive to small data changes (→ use Random Forest to fix this)
- ❌ Tends to overfit without proper pruning

## Related
- [[Overfitting and Underfitting]] — trees overfit; pruning and depth limits are the fix
- [[Feature Normalization]] — NOT required for decision trees
- [[Classic Model]] — hub note
- [[Supervised Learning]] — parent topic
