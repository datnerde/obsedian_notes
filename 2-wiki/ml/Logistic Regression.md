---
title: Logistic Regression
tags: [ml, supervised-learning, classification, models]
created: 2026-04-14
status: growing
related: [[Classic Model]], [[Classification Metrics]], [[Overfitting and Underfitting]], [[Feature Normalization]]
source: Quest for Machine Learning
---

# Logistic Regression

## Core Idea
Model the **log-odds** of a binary outcome as a linear function of features. Output is a probability in [0, 1] via the sigmoid function. Despite the name, it's a **classification** model.

## From Linear to Logistic Regression
- Linear regression: continuous output `y = Xβ`
- Logistic regression: models `log(p / (1-p)) = Xβ` where odds = `p / (1-p)`
- Solving for p: `p = 1 / (1 + e^{-Xβ})` — the sigmoid function

### Key Differences from Linear Regression
| | Linear Regression | Logistic Regression |
|---|---|---|
| Output | Continuous y | Binary (0/1) |
| Function | Identity | Sigmoid |
| Loss | MSE | Cross-entropy (log-loss) |
| Estimation | OLS or MLE | MLE only |

## Multi-Class Extensions

### Softmax Regression (Multinomial)
- For when each sample has **exactly one** label
- Generalizes logistic regression to K classes
- Output is a probability distribution over all K classes
- Structurally identical to the **Multinomial Logit (MNL)** model in discrete-choice econometrics — see [[Demand Prediction]] for its retail application (modeling $P(j \mid \text{purchase})$ across competing products)

### One-vs-Rest (OvR)
- For when a sample can have **multiple labels**
- Train K binary classifiers: classifier i predicts "is this sample in class i or not?"

## Strengths & Weaknesses
- ✅ Outputs calibrated probabilities (useful for ranking)
- ✅ Fast, interpretable coefficients
- ❌ Assumes linear decision boundary
- ❌ Requires [[Feature Normalization]] for regularized variants

## Related
- [[Feature Normalization]] — normalize before training with regularization
- [[Classification Metrics]] — logistic regression outputs probabilities → threshold to get labels
- [[Overfitting and Underfitting]] — L1/L2 regularization (Lasso/Ridge Logistic Regression)
- [[Classic Model]] — hub note
- [[Demand Prediction]] — MNL / softmax as the discrete-choice model
- [[Uplift Modeling]] — logistic regression is the base estimator for response probability
