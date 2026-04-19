---
title: Imbalanced Data
tags: [ml, sampling, preprocessing, model-evaluation]
created: 2026-04-14
status: evergreen
related: [[Sampling]], [[Classification Metrics]], [[ROC and AUC]], [[Cross Validation]]
source: Quest for Machine Learning
---

# Imbalanced Data

## Core Idea
When one class is rare (e.g., 95% negative, 5% positive), standard training is biased toward the majority class and accuracy is a misleading metric.

## Why It's a Problem
A model that always predicts "negative" gets 95% accuracy but 0% recall on the rare class. Use [[ROC and AUC]] or F1 instead of accuracy.

## Solutions

### Resampling
- **Over-sampling**: duplicate minority class samples (risk: overfitting)
- **Under-sampling**: remove majority class samples (risk: losing information)

### SMOTE (Synthetic Minority Over-sampling Technique)
- Generate synthetic minority samples by interpolating between existing minority samples
- Reduces overfitting risk vs naive over-sampling
- Variants:
  - **Borderline-SMOTE**: only synthesize near the decision boundary
  - **ADASYN**: synthesize more where minority is sparse

### Informed Under-sampling
- **EasyEnsemble / BalanceCascade**: iteratively train on balanced subsets
- **NearMiss**: keep majority samples nearest to minority samples

### Algorithm-level Solutions
- Modify the loss function to weight minority class more heavily
- Convert to anomaly detection / one-class classification

## Related
- [[Classification Metrics]] — use F1/AUC instead of accuracy
- [[ROC and AUC]] — robust to class imbalance
- [[Sampling]] — parent topic
