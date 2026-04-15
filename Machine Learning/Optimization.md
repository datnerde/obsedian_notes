---
title: Optimization
tags: [ml, optimization, gradient-descent, training]
created: 2026-04-14
status: evergreen
related: [[Feature Normalization]], [[Overfitting and Underfitting]], [[Classic Model]]
source: Quest for Machine Learning
---

# Optimization

## Core Idea
Find model parameters θ that minimize the loss function L(θ). Most deep learning and many classical ML models are trained via gradient-based optimization.

## Gradient Descent

### Batch Gradient Descent
- Compute gradient on the full dataset each step
- Stable but slow for large datasets

### Stochastic Gradient Descent (SGD)
- Compute gradient on one sample at a time
- Noisy but fast; the noise can help escape local minima

### Mini-batch Gradient Descent
- Compute gradient on a small batch (e.g., 32-256 samples)
- Best of both: vectorized computation + frequent updates

## Adaptive Methods

### Momentum
- Accumulate a velocity vector in directions of persistent gradient reduction
- `v = β·v - α·∇L`; helps navigate flat regions and saddle points

### Adam (Adaptive Moment Estimation)
- Combines momentum (1st moment) with RMSProp (2nd moment / per-parameter learning rate)
- Most popular default optimizer for deep learning
- `m = β1·m + (1-β1)·∇L` (mean)
- `v = β2·v + (1-β2)·∇L²` (variance)
- `θ = θ - α · m / (√v + ε)`

### RMSProp
- Divide learning rate by moving average of recent gradient magnitudes
- Good for non-stationary problems (RNNs)

## Learning Rate
- Too high → diverge; too low → slow convergence
- **Learning rate schedule**: decay over time (step decay, cosine annealing)
- **Warmup**: start with small LR, ramp up, then decay

## Loss Landscape
- [[Feature Normalization]] makes the loss landscape more spherical → faster convergence
- [[Overfitting and Underfitting|Regularization]] adds a penalty term to the loss

## Convergence Challenges
- **Saddle points**: gradient = 0 but not a minimum (common in high-dim spaces)
- **Local minima**: less of a problem in practice for overparameterized networks
- **Vanishing/exploding gradients**: use batch norm, gradient clipping, residual connections

## Related
- [[Feature Normalization]] — prerequisite for stable gradient descent
- [[Overfitting and Underfitting]] — L1/L2 regularization modifies the loss
- [[Hyperparameter Tuning]] — learning rate is the most important hyperparameter
