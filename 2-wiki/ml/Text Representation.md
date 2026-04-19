---
title: Text Representation
tags: [ml, feature-engineering, nlp, text]
created: 2026-04-14
status: growing
related: [[Feature Engineering]], [[Word2Vec]], [[Dimensional Reduction]]
source: Quest for Machine Learning
---

# Text Representation

## Core Idea
Convert raw text into numeric vectors that ML models can process.

## Methods (from simple to complex)

### 1. Bag of Words
- Treat a document as an unordered set of words
- Each word becomes a feature; value = count of occurrences
- N-gram: extends to word pairs (bigrams) or triples for some context
- Word stemming: reduce words to their root form first ("running" → "run")

### 2. TF-IDF
`TF-IDF(t, d) = TF(t, d) × IDF(t)`
`IDF(t) = log(N / (df(t) + 1))`
- TF: how often a term appears in a document
- IDF: penalizes terms that appear in many documents (common words like "the")
- Result: words that are frequent in a document but rare globally get high scores

### 3. Topic Models (LDA)
- Decompose: `doc × word = doc × topic × topic × word`
- Finds latent topics across a corpus
- Useful for summarization and document clustering

### 4. Word Embeddings (Deep Learning)
- Learn dense, low-dimensional representations where similar words cluster together
- See [[Word2Vec]] for specific architecture

## Application: Labeling Implicit Dimensions

In [[Recommender Systems]] content filtering, raw product attributes (brand, price) rarely capture taste dimensions like *trendy*, *sporty*, *luxury*. A Bayesian text classifier learns $P(\text{word} \mid \text{implicit-attribute})$ from a manually labeled seed of items, then inverts to assign implicit-dimension scores to the full catalog via $P(\text{implicit-attribute} \mid \text{description})$. This is a canonical bridge from text-representation techniques (TF-IDF, bag-of-words) to personalization.

## Related
- [[Word2Vec]] — the canonical word embedding model
- [[Dimensional Reduction]] — TF-IDF vectors are often reduced via PCA/SVD
- [[Feature Engineering]] — parent topic
- [[Recommender Systems]] — content filtering uses text classification for implicit-dimension labeling
