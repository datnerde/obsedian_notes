---
title: Unsupervised Learning
tags: [ml, unsupervised-learning]
created: 2026-04-14
status: evergreen
related: [[ML-MOC]], [[Dimensional Reduction]]
source: Quest for Machine Learning
---

# Unsupervised Learning

> Learn structure from unlabeled data — no ground truth labels provided.

## Clustering

- [[K-Means Clustering]] — partition into K clusters, hard assignment
- [[Gaussian Mixture Model]] — probabilistic clustering with soft assignments
- Self-Organizing Map (SOM) — topology-preserving neural network for visualization

## Clustering Evaluation

No labels → need special metrics:

- **Hopkins Statistic**: tests if data has cluster tendency or is random
- **Elbow / Gap Statistic**: determine optimal K
- **Silhouette Coefficient**: measures cluster cohesion vs separation
- **RMSSTD, R-Square, Hubert Γ**: additional quality measures

## Dimensionality Reduction

- [[Dimensional Reduction]] — PCA, LDA (used as preprocessing or standalone)

## Related

- [[Dimensional Reduction]] — often a preprocessing step for clustering
