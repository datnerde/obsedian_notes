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

## Bias-Variance Decomposition — Full Proof

Given $y = f(x) + \varepsilon$ where $E[\varepsilon]=0$, $\text{Var}(\varepsilon)=\sigma^2$:

$$E[(y - \hat{f})^2] = \underbrace{(\text{Bias}[\hat{f}])^2}_{\text{model too simple}} + \underbrace{\text{Var}[\hat{f}]}_{\text{model too sensitive}} + \underbrace{\sigma^2}_{\text{irreducible}}$$

**Derivation sketch:**
1. Split: $y - \hat{f} = \varepsilon + (f - \hat{f})$
2. Square and take expectation → cross-term $E[\varepsilon(f-\hat{f})] = 0$ (independence)
3. Add/subtract $E[\hat{f}]$ to decompose $(f - \hat{f})^2$ into Bias² + Variance

**Intuition:**
- High Bias → model is too simple; underfits (e.g., linear model on non-linear data)
- High Variance → model too complex; changes a lot with different training sets (e.g., deep unpruned tree)
- $\sigma^2$ is irreducible — comes from inherent noise in the data

---

## L1 vs L2 Regularization — Mathematical Distinction

**L2 (Ridge)** — single-coordinate update:
$$\beta_j^{\text{ridge}} = \frac{\hat{\beta}_j^{\text{OLS}}}{1 + \lambda}$$
The denominator is always > 1 → weight is *shrunk but never zero*.

**L1 (Lasso)** — soft-thresholding:
$$\beta_j^{\text{lasso}} = \text{sign}(\hat{\beta}_j^{\text{OLS}}) \cdot \max\!\left(|\hat{\beta}_j^{\text{OLS}}| - \tfrac{\lambda}{2},\ 0\right)$$
When $|\hat{\beta}_j^{\text{OLS}}| < \lambda/2$, the coefficient is pushed *exactly to zero* → feature selection.

**Geometric intuition:** L1's diamond-shaped constraint region has corners on the axes; the loss ellipse almost always hits a corner first → sparse solution.

**Bayesian view:** L2 ↔ Gaussian prior; L1 ↔ Laplace prior (sharp peak at 0 → encourages sparsity).

---

## Related
- [[Cross Validation]] — used to diagnose overfitting
- [[Feature Engineering]] — adding features can cure underfitting
- [[Optimization]] — regularization is added to the loss function
- [[Ensemble-Methods]] — ensembles reduce variance via the $\rho\sigma^2$ formula
