---
title: Feature Engineering
tags: [ml, feature-engineering]
created: 2026-04-14
status: evergreen
related: [[ML-MOC]], [[Model Evaluation]], [[Feature Normalization]]
source: Quest for Machine Learning
---

# Feature Engineering

> The process of transforming raw data into features that better represent the underlying problem, improving model performance.

## Subtopics

### Numerical Features
- [[Feature Normalization]] — scaling to common range (Min-Max, Z-Score)

### Categorical Features
- [[Categorical Encoding]] — ordinal, one-hot, binary encoding

### Text Features
- [[Text Representation]] — Bag of Words, TF-IDF, topic models
- [[Word2Vec]] — dense word embeddings

### Sparse/High-Dimensional Data
- Feature crosses: combine features to capture interactions; reduce via [[Dimensional Reduction]]
- Decision tree features: use tree splits to generate sparse feature combinations

### Insufficient Data
- L1/L2 regularization (see [[Overfitting and Underfitting]])
- Dropout
- Data Augmentation

## Why It Matters
Features are the primary lever for model improvement. Better features > better algorithms in most practical settings.
