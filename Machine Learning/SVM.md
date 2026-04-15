---
title: Support Vector Machine (SVM)
tags: [ml, supervised-learning, classification, models]
created: 2026-04-14
status: growing
related: [[Classic Model]], [[Feature Normalization]], [[Kernel Methods]], [[Overfitting and Underfitting]]
source: Quest for Machine Learning
---

# Support Vector Machine (SVM)

## Core Idea
Find the hyperplane that maximizes the **margin** between two classes. The decision boundary is determined only by the closest points to the boundary — the **support vectors**.

## Hard Margin vs Soft Margin
- **Hard Margin**: Requires data to be linearly separable — no training errors allowed
- **Soft Margin**: Introduces slack variables ξ to allow some misclassification. Controlled by hyperparameter **C**:
  - Large C → small margin, fewer errors (risk of overfitting)
  - Small C → large margin, more errors allowed (more generalization)

## Kernel Trick
Real data is often not linearly separable in the original space. The kernel trick implicitly maps data to a higher-dimensional space **without explicitly computing the transformation**.

`K(x, x') = φ(x) · φ(x')` — only the dot product in high-dim space is needed

### Common Kernels
| Kernel | Formula | Use Case |
|--------|---------|----------|
| Linear | `x · x'` | Linearly separable data |
| RBF (Gaussian) | `exp(-γ‖x-x'‖²)` | General purpose, most common |
| Polynomial | `(x · x' + c)^d` | When feature interactions matter |

## Requirements
- Features must be normalized (see [[Feature Normalization]]) — SVM is sensitive to feature scales
- Works well for high-dimensional data and clear margin cases
- Slow on very large datasets (O(n²) to O(n³))

## Related
- [[Feature Normalization]] — required before training SVM
- [[Overfitting and Underfitting]] — C and kernel parameters control bias-variance
- [[Classic Model]] — hub note
- [[LDA (Linear Discriminant Analysis)]] — another margin-based approach
