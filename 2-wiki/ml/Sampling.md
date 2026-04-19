---
title: Sampling
tags: [ml, sampling, statistics]
created: 2026-04-14
status: evergreen
related: [[ML-MOC]], [[Probability Graphical Model]], [[Imbalanced Data]]
source: Quest for Machine Learning
---

# Sampling

> Draw samples from probability distributions. Core to simulation, inference, and handling imbalanced datasets.

## Applications in ML
- Simulate random processes to build intuition
- Use small samples as non-parametric proxies for population distributions
- Bootstrap/jackknife for variance estimation
- Approximate inference in complex models (see [[MCMC]])
- Handle imbalanced datasets (see [[Imbalanced Data]])

## Basic Sampling Methods
- **Linear Congruential Generator**: generate uniform [0,1] random numbers
- **Inverse Transform Sampling**: apply inverse CDF to uniform samples
- **Accept-Reject Sampling**: sample from a proposal, accept with probability ∝ target/proposal
- **Adaptive Rejection Sampling**: use multiple proposal functions to better cover the target
- **Importance Sampling**: weight samples by target/proposal ratio

## Advanced
- [[MCMC]] — for high-dimensional distributions where basic methods fail

## Handling Imbalance
- [[Imbalanced Data]] — SMOTE, over/under-sampling strategies

## Related
- [[Probability Graphical Model]] — MCMC is used for PGM inference
- [[Cross Validation]] — Bootstrap is a cross-validation strategy
