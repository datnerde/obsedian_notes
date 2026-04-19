---
title: Feature Normalization
tags: [ml, feature-engineering, preprocessing]
created: 2026-04-14
status: evergreen
related: [[Gradient Descent]], [[Feature Engineering]], [[Decision Tree]]
source: Quest for Machine Learning
---

# Feature Normalization

## Core Idea
Scale numerical features to a common range so that no feature dominates due to magnitude, and gradient-based optimization converges faster.

## Methods

### Min-Max Scaling
- Transforms to range [0, 1]: `x' = (x - min) / (max - min)`
- Use when you need a bounded range and distribution doesn't matter

### Z-Score Normalization (Standardization)
- Transforms to N(0, 1): `x' = (x - μ) / σ`
- Use when the algorithm assumes normally distributed features (e.g., linear regression, SVM)

## When NOT to Normalize
- **Tree-based models** (Decision Tree, Random Forest, XGBoost) are invariant to monotonic feature transformations — normalization has no effect
- When features are already on the same scale

## Why It Helps Gradient Descent
Without normalization, the loss landscape is elongated along dimensions with larger scales — gradient descent oscillates and takes longer to converge. Normalization makes the landscape more spherical.

## Related
- [[Gradient Descent]] — converges faster with normalized features
- [[Feature Engineering]] — parent topic
- [[Decision Tree]] — does NOT require normalization
