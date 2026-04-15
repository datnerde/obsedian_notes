---
title: K-Means Clustering
tags: [ml, unsupervised-learning, clustering]
created: 2026-04-14
status: evergreen
related: [[Unsupervised Learning]], [[Gaussian Mixture Model]], [[Dimensional Reduction]]
source: Quest for Machine Learning
---

# K-Means Clustering

## Core Idea
Partition n data points into K clusters by minimizing the sum of squared distances from each point to its cluster centroid. Iterates via the EM algorithm.

## Algorithm
1. Preprocess: standardize/normalize, handle outliers
2. Randomly initialize K cluster centroids
3. Repeat until convergence:
   - **E step**: assign each point to the nearest centroid
   - **M step**: recompute each centroid as the mean of assigned points

`Cost = Σ_k Σ_{x in Ck} ||x - μk||²`

## Variants
- **K-Means++**: choose initial centroids with probability proportional to distance from existing centroids — reduces bad initializations
- **ISODATA**: automatically splits or merges clusters based on size/dispersion — handles unknown K

## Limitations
- Sensitive to initialization (use K-Means++)
- Sensitive to outliers
- Assumes spherical clusters of similar size
- Can get stuck in local optima
- Must specify K in advance

## How to Choose K
- **Elbow Method**: plot cost vs K, pick the "elbow"
- **Gap Statistic**: compare within-cluster variance to expected under random distribution
- **Silhouette Coefficient**: measures how well each point fits its cluster vs neighboring clusters

## Related
- [[Gaussian Mixture Model]] — soft assignment, probabilistic version of K-Means
- [[Unsupervised Learning]] — parent topic
- [[Dimensional Reduction]] — often applied before clustering on high-dimensional data
