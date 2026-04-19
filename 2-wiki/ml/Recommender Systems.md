---
title: Recommender Systems
tags: [ml, recommender-systems, information-retrieval]
created: 2026-04-19
status: seedling
related: [[Text Representation]], [[PCA]], [[Logistic Regression]], [[Classification Metrics]]
source: Data Mining Problems in Retail (Katsov 2015)
---

# Recommender Systems

## Core Idea

Predict a **rating function** $R: J \times U \to \mathbb{R}$ mapping (item, user) pairs to preference scores, then surface the top-$k$ items per user. Drives the "long tail" of retail revenue — the aggregate of many low-volume items that best-seller heuristics miss.

## Two Classical Families

### Content Filtering

Model each user as a regression/classifier over **item features**.

- **Training data**: the user's past ratings / purchase history
- **Prediction**: score catalog items using the user's personal model
- **Strengths**: no cold-start for new items (only needs item features); interpretable
- **Weakness**: item features rarely capture subtle preferences (lifestyle, taste)

To bridge the gap, retailers manually label a seed of items with **implicit dimensions** (sporty, trendy, luxury, conservative) and extend via text classification over product descriptions — e.g., learn $P(\text{word} \mid \text{implicit-attribute})$ with a Bayesian classifier, invert to get $P(\text{implicit-attribute} \mid \text{description})$ for the rest of the catalog. See [[Text Representation]].

### Collaborative Filtering

Infer a user's rating for an item by **averaging ratings from similar users** (user-based) or **similar items** (item-based).

- **Training data**: the full user-item rating matrix (very sparse)
- **Prediction**: neighborhood or matrix-factorization (SVD-style)
- **Strengths**: captures latent preferences no explicit feature encodes
- **Weakness**: cold-start for both new users and new items; needs dense-enough history

## Sparsity and Scale

The user-item matrix is typically >99% missing. Standard coping strategies:

- Matrix factorization into low-rank user/item latent vectors (related to [[PCA]] but for ratings; e.g., SVD, ALS)
- Locality-sensitive hashing for near-neighbor lookup at scale
- Implicit feedback models (clicks, dwell time) when explicit ratings are absent

## Multi-Objective Recommendations

Pure relevance is not the only objective in retail. Practical systems optimize a linear (or learned) combination of:

- **Relevance** — predicted rating
- **Margin** — push higher-margin items when relevance is comparable
- **Inventory** — bias toward items with excess stock
- **Diversity / novelty** — avoid showing the same genre 10×
- **Manufacturer-sponsored promotions** — cost of incentive borne externally

This reframes recommendation as constrained optimization, not just rating prediction.

## Cross-Channel Applications

Same machinery serves:

- **Recommender widgets** on product pages
- **Personalized search ranking**
- **Targeted ads**
- **Cross-sell** — furniture recs from apparel purchases via latent "lifestyle" dimensions
- **Merchandiser tooling** — classify new product descriptions along implicit dimensions to suggest positioning

## Evaluation

- Offline: Precision@k, Recall@k, NDCG, coverage, diversity
- Online: [[AB Testing]] with CTR, add-to-cart, margin-weighted GMV

See [[Classification Metrics]] for the underlying precision/recall definitions that extend into ranking metrics.

## Related

- [[Text Representation]] — TF-IDF / Bayesian classification labels items with implicit dimensions for content filtering
- [[PCA]] — conceptual ancestor of matrix-factorization collaborative filtering
- [[Logistic Regression]] — common per-user classifier in content filtering
- [[AB Testing]] — online eval layer for any ranking change
- [[Data Mining Problems in Retail]] — source, Problem 2 (Recommendations)
