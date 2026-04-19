---
title: Dimensional Reduction
tags: [ml, dimensionality-reduction]
created: 2026-04-14
status: evergreen
related: [[ML-MOC]], [[Feature Engineering]], [[Unsupervised Learning]]
source: Quest for Machine Learning
---

# Dimensional Reduction

> Reduce the number of features while preserving important structure. Prevents the curse of dimensionality, improves interpretability, and speeds up training.

## Unsupervised Methods
- [[PCA]] — maximize variance; projects to uncorrelated components
  - Kernel PCA for non-linear data

## Supervised Methods
- [[LDA (Linear Discriminant Analysis)]] — maximize class separability

## PCA vs LDA Summary
| | PCA | LDA |
|---|---|---|
| Uses labels | No | Yes |
| Goal | Max variance | Max class separation |
| Both via | Eigendecomposition | Eigendecomposition |

## Related
- [[Feature Engineering]] — dim reduction is a feature engineering technique
- [[K-Means Clustering]] — reduce dimensions before clustering high-dimensional data
- [[Categorical Encoding]] — one-hot encoding → often needs dim reduction
