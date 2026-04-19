---
title: Overfitting and Underfitting
tags: [ml, model-evaluation, regularization]
created: 2026-04-14
status: evergreen
related: [[Model Evaluation]], [[Cross Validation]], [[Optimization]], [[Feature Engineering]]
source: Quest for Machine Learning
---

# Overfitting and Underfitting

## Core Idea
The bias-variance tradeoff: too simple a model underfits (high bias), too complex overfits (high variance). The goal is finding the sweet spot.

## Overfitting
- Model performs well on training data but poorly on unseen data
- High variance — the model has "memorized" noise
- Fixes:
  - Get more training data
  - Reduce model complexity
  - **Regularization** (L1/L2)
  - Dropout (neural networks)
  - Ensemble methods (average out variance)
  - Early stopping

## Underfitting
- Model performs poorly on both training and test data
- High bias — the model is too simple to capture the pattern
- Fixes:
  - Add more features
  - Increase model complexity
  - Reduce regularization
  - Train longer

## Regularization
- **L2 (Ridge)**: penalizes large weights → shrinks all weights towards zero → smooth model
- **L1 (Lasso)**: penalizes weight magnitude → drives some weights exactly to zero → feature selection
- **Elastic Net**: L1 + L2 combined

## Related
- [[Cross Validation]] — used to diagnose overfitting
- [[Feature Engineering]] — adding features can cure underfitting
- [[Optimization]] — regularization is added to the loss function
