---
title: Gaussian Mixture Model
tags: [ml, unsupervised-learning, probabilistic-models, clustering]
created: 2026-04-14
status: growing
related: [[K-Means Clustering]], [[Unsupervised Learning]], [[Probability Graphical Model]]
source: Quest for Machine Learning
---

# Gaussian Mixture Model (GMM)

## Core Idea
Model the dataset as a mixture of K Gaussian distributions. Unlike K-Means, GMM provides **soft** (probabilistic) cluster assignments and can model elliptical clusters.

## Model
`P(x) = Σ_k π_k × N(x | μk, Σk)`

Where π_k is the mixing weight for cluster k.

## Algorithm (EM)
1. Initialize K Gaussians (parameters: μk, Σk, πk)
2. Repeat until convergence:
   - **E step**: compute probability of each point belonging to each cluster
   - **M step**: update μk, Σk, πk using the soft assignments

## GMM vs K-Means
| | K-Means | GMM |
|---|---|---|
| Assignment | Hard (one cluster) | Soft (probabilities) |
| Cluster shape | Spherical | Elliptical |
| Output | Cluster labels | Probabilities |
| Can generate new samples? | ❌ | ✅ |
| Predicts cluster probability? | ❌ | ✅ |

## When to Use GMM
- You need probability estimates, not just labels
- Clusters have different shapes and sizes
- You want to generate new synthetic data

## Related
- [[K-Means Clustering]] — the hard-assignment baseline
- [[Probability Graphical Model]] — GMM is a latent variable model
- [[Sampling]] — GMM can be used to generate samples
