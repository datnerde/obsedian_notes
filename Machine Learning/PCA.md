---
title: PCA (Principal Component Analysis)
tags: [ml, dimensionality-reduction, unsupervised-learning]
created: 2026-04-14
status: evergreen
related: [[Dimensional Reduction]], [[Feature Normalization]], [[Unsupervised Learning]]
source: Quest for Machine Learning
---

# PCA (Principal Component Analysis)

## Core Idea
Find the directions (principal components) of maximum variance in the data and project onto a lower-dimensional subspace. Unsupervised — does not use labels.

## Algorithm
1. **Standardize** the data (center to mean 0) — [[Feature Normalization]] required
2. Compute the **covariance matrix** Σ
3. **Eigendecomposition** of Σ → eigenvectors and eigenvalues
4. Sort eigenvectors by eigenvalue (largest first)
5. Select the top k eigenvectors → projection matrix W
6. Project data: `X_reduced = X · W`

## Kernel PCA
- Standard PCA is linear
- Kernel PCA applies the kernel trick to find non-linear principal components
- Use when data has non-linear structure

## Related
- [[LDA (Linear Discriminant Analysis)]] — supervised dim reduction; compare with PCA
- [[Dimensional Reduction]] — parent topic
- [[Feature Normalization]] — required before PCA
- [[Unsupervised Learning]] — PCA is unsupervised
