---
title: LDA (Linear Discriminant Analysis)
tags: [ml, dimensionality-reduction, supervised-learning, classification]
created: 2026-04-14
status: evergreen
related: [[Dimensional Reduction]], [[PCA]], [[Classic Model]]
source: Quest for Machine Learning
---

# LDA (Linear Discriminant Analysis)

## Core Idea
Supervised dimensionality reduction: find the projection that **maximizes inter-class distance** while **minimizing intra-class variance**. Unlike PCA, LDA uses class labels.

## Intuition
- PCA: find directions of maximum overall variance
- LDA: find directions that best **separate the classes**

## Algorithm
Solve eigendecomposition of `S_W^{-1} S_B` where:
- `S_W` = within-class scatter matrix
- `S_B` = between-class scatter matrix

## Assumptions
- Each class follows a Gaussian distribution
- All classes share the same covariance matrix (homoscedasticity)
- If violated → use QDA (Quadratic Discriminant Analysis) which allows different covariances

## PCA vs LDA
| | PCA | LDA |
|---|---|---|
| Supervised? | ❌ | ✅ |
| Objective | Max variance | Max class separation |
| Uses labels? | No | Yes |
| Method | Eigendecomp of Σ | Eigendecomp of S_W^{-1}S_B |

## Related
- [[PCA]] — unsupervised counterpart
- [[Dimensional Reduction]] — parent topic
- [[Classic Model]] — LDA can also be used as a classifier
