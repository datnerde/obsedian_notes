---
title: Classic ML Models
tags: [ml, supervised-learning, models]
created: 2026-04-14
status: evergreen
related: [[Feature Normalization]], [[Overfitting and Underfitting]]
source: Quest for Machine Learning
---

# Classic ML Models

> Hub note for the foundational supervised learning algorithms. Each model has its own atomic note.

## Models

- [[SVM]] — maximize margin hyperplane; kernel trick for non-linear boundaries
- [[Logistic Regression]] — model log-odds; outputs probabilities; extends to multi-class via Softmax
- [[Decision Tree]] — recursive feature splits; no normalization needed; prune to prevent overfitting
- [[LDA (Linear Discriminant Analysis)]] — supervised dim reduction + classifier; assumes Gaussian, equal covariance

## Quick Comparison

| Model | Normalization Needed | Interpretable | Handles Non-linearity | Probabilistic Output |
|-------|---------------------|---------------|-----------------------|----------------------|
| [[SVM]] | ✅ Required | ❌ | ✅ (kernel) | ❌ |
| [[Logistic Regression]] | ✅ Recommended | ✅ | ❌ | ✅ |
| [[Decision Tree]] | ❌ Not needed | ✅ | ✅ | ❌ |
| [[LDA (Linear Discriminant Analysis)\|LDA]] | ✅ Recommended | ✅ | ❌ | ✅ |

## Related

- [[Feature Normalization]] — required for SVM and Logistic Regression
- [[Overfitting and Underfitting]] — all models need regularization strategy
- [[K-Means Clustering]] / [[Gaussian Mixture Model]] — unsupervised counterparts
