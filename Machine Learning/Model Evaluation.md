---
title: Model Evaluation
tags: [ml, model-evaluation]
created: 2026-04-14
status: evergreen
related: [[ML-MOC]], [[Feature Engineering]], [[Overfitting and Underfitting]]
source: Quest for Machine Learning
---

# Model Evaluation

> Assess whether a trained model will generalize well to unseen data.

## Classification Metrics
- [[Classification Metrics]] — Accuracy, Precision, Recall, F1
- [[ROC and AUC]] — threshold-invariant evaluation, robust to imbalance

## Regression Metrics
- RMSE: sensitive to outliers (errors are squared)
- MAPE: percentage error, scale-invariant
- Use MAPE when outliers are noise; investigate further if they're real signals

## Evaluation Methodology
- [[Cross Validation]] — K-fold, LOO, Bootstrap
- [[AB Testing]] — online evaluation (offline metrics ≠ online metrics)

## Overfitting Diagnosis
- [[Overfitting and Underfitting]] — bias-variance tradeoff and fixes

## Hyperparameter Search
- [[Hyperparameter Tuning]] — grid search, random search, Bayesian optimization
