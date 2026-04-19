---
title: Hyperparameter Tuning
tags: [ml, model-evaluation, optimization]
created: 2026-04-14
status: growing
related: [[Model Evaluation]], [[Cross Validation]], [[Overfitting and Underfitting]]
source: Quest for Machine Learning
---

# Hyperparameter Tuning

## Core Idea
Find the model configuration (hyperparameters) that maximizes generalization performance. Always evaluate using [[Cross Validation]] to avoid overfitting the hyperparameters themselves.

## Methods

### Grid Search
- Exhaustively try all combinations of a predefined parameter grid
- Guaranteed to find the best configuration within the grid
- Expensive: exponential in number of parameters

### Random Search
- Sample random combinations from the parameter space
- Often finds good configurations faster than grid search
- Better when some parameters matter much more than others

### Bayesian Optimization
- Builds a probabilistic model (surrogate) of the objective function
- Uses prior evaluations to intelligently select the next point to evaluate
- Process: assume prior distribution → sample → update posterior → choose next point at likely-maximum → repeat
- More efficient than random/grid search for expensive evaluations

## Related
- [[Cross Validation]] — the evaluation engine for tuning
- [[Overfitting and Underfitting]] — tuning is trying to avoid both
