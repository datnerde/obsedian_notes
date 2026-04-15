---
title: Probability Graphical Model
tags: [ml, probabilistic-models, pgm, bayesian]
created: 2026-04-14
status: seedling
related: [[Sampling]], [[MCMC]], [[Gaussian Mixture Model]]
source: Quest for Machine Learning
---

# Probability Graphical Model (PGM)

## Core Idea
Represent a joint probability distribution using a graph where nodes are random variables and edges encode conditional independence relationships. Enables efficient reasoning about complex distributions.

## Two Types

### Bayesian Networks (Directed, DAG)
- Edges represent causal/conditional dependencies: A → B means B depends on A
- `P(X1,...,Xn) = Π P(Xi | Parents(Xi))`
- Used for: medical diagnosis, document classification, hidden Markov models

### Markov Random Fields / MRFs (Undirected)
- Edges represent symmetric relationships (no direction)
- `P(X) ∝ Π φ(clique)`  where φ is a potential function over cliques
- Used for: image segmentation, social network modeling

## Inference
Given observed variables, compute the posterior over unobserved variables.
- **Exact**: Variable Elimination, Belief Propagation (only feasible for small graphs)
- **Approximate**: [[MCMC]], Variational Inference (for large/complex graphs)

## Learning
- **Structure learning**: find the graph structure from data
- **Parameter learning**: given structure, estimate the parameters (e.g., MLE)

## Connection to Other Models
- [[Gaussian Mixture Model]] is a latent variable model (simple PGM)
- [[MCMC]] is the standard inference tool for complex PGMs

## Related
- [[MCMC]] — inference in PGMs
- [[Sampling]] — probabilistic inference requires sampling
- [[Gaussian Mixture Model]] — a specific latent variable PGM
