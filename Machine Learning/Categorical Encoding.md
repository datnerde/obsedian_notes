---
title: Categorical Encoding
tags: [ml, feature-engineering, preprocessing]
created: 2026-04-14
status: evergreen
related: [[Feature Engineering]], [[Feature Normalization]], [[Dimensional Reduction]]
source: Quest for Machine Learning
---

# Categorical Encoding

## Core Idea
Convert categorical (non-numeric) features into numeric representations that ML models can process.

## Methods

### Ordinal Encoding
- Assigns integer labels: `red=0, green=1, blue=2`
- Use only when there is a meaningful order between categories
- Problem: implies a magnitude relationship that may not exist

### One-Hot Encoding
- Creates a binary column per category
- Representation is stored as a sparse matrix to save memory
- Can be combined with [[Dimensional Reduction]] to reduce dimensions when cardinality is high
- Problem: high cardinality → very high dimensional space

### Binary Encoding
- Converts category IDs via hash map into binary representation
- Occupies far less space than one-hot encoding for high-cardinality features

## When to Use Which
| Situation | Method |
|-----------|--------|
| Ordered categories (low, medium, high) | Ordinal |
| Low cardinality (<20 categories) | One-Hot |
| High cardinality (user IDs, zip codes) | Binary / Embedding |

## Related
- [[Feature Engineering]] — parent topic
- [[Dimensional Reduction]] — can reduce one-hot encoded dimensions
- [[Word2Vec]] — learned embeddings for extreme-cardinality cases
