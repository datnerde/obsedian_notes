---
title: Cross Validation
tags: [ml, model-evaluation, training]
created: 2026-04-14
status: evergreen
related: [[Model Evaluation]], [[Overfitting and Underfitting]], [[Hyperparameter Tuning]]
source: Quest for Machine Learning
---

# Cross Validation

## Core Idea
Estimate model generalization performance by systematically rotating which data is used for training vs validation, reducing the variance of the performance estimate.

## Methods

### Holdout
- Split into train/validation/test sets once
- Simple but high variance — result depends on the specific split

### K-Fold Cross Validation
- Split data into K equal folds
- Train K times, each time using a different fold as validation
- Final score = mean across K runs
- Common: K = 5 or 10

### Leave-One-Out (LOO)
- K = n (one sample per fold)
- Computationally expensive, almost no bias
- Use for very small datasets

### Bootstrap
- For when sample size is too small even for K-fold
- Sample n data points with replacement from n total
- ~36.8% of samples won't be selected → use as validation set
- `P(not selected in n draws) = (1 - 1/n)^n → 1/e ≈ 36.8%`

## Related
- [[Overfitting and Underfitting]] — cross-validation detects overfitting
- [[Hyperparameter Tuning]] — use cross-validation to evaluate each configuration
- [[Model Evaluation]] — parent topic
