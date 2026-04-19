---
title: MCMC (Markov Chain Monte Carlo)
tags: [ml, sampling, statistics, probabilistic-models]
created: 2026-04-14
status: growing
related: [[Sampling]], [[Probability Graphical Model]], [[Gaussian Mixture Model]]
source: Quest for Machine Learning
---

# MCMC (Markov Chain Monte Carlo)

## Core Idea
When we cannot directly sample from a complex target distribution (especially in high-dimensional space), construct a Markov chain whose stationary distribution equals the target distribution, then sample by running the chain.

## Why MCMC?
Simple sampling methods (inverse transform, accept-reject) fail in high dimensions because:
- Rejection rates become astronomically high
- It's hard to find a good proposal distribution

## How It Works
1. Construct a Markov chain with stationary distribution = target P(x)
2. Start from any initial state
3. Run the chain through many state transitions
4. After "burn-in" period, samples from the chain approximate P(x)

## Algorithms
- **Metropolis-Hastings**: propose a move, accept/reject based on ratio of probabilities
- **Gibbs Sampling**: sample each variable conditioned on all others; special case of M-H with acceptance rate = 1

## Related
- [[Sampling]] — parent topic; MCMC is the high-dimensional case
- [[Probability Graphical Model]] — MCMC used for inference in PGMs
- [[Gaussian Mixture Model]] — EM algorithm as an alternative to MCMC for GMMs
