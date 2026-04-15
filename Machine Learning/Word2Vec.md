---
title: Word2Vec
tags: [ml, nlp, embedding, deep-learning]
created: 2026-04-14
status: growing
related: [[Text Representation]], [[Dimensional Reduction]], [[Unsupervised Learning]]
source: Quest for Machine Learning
---

# Word2Vec

## Core Idea
Learn dense word embeddings from a large corpus by training a shallow neural network to predict context words. Words with similar meanings end up close together in embedding space.

## Two Architectures

### CBOW (Continuous Bag of Words)
- **Input**: surrounding context words
- **Task**: predict the center word
- Better for frequent words, faster to train

### Skip-gram
- **Input**: center word
- **Task**: predict the surrounding context words
- Better for rare words and small datasets

## Key Insight
`Word2Vec ≈ learning (current word) × (context words)`

This is analogous to matrix factorization: `word × context matrix` is decomposed into lower-dimensional representations.

Compare with [[Text Representation#Topic Models (LDA)|LDA]]:
`LDA: doc × word = doc × topic × topic × word`
`Word2Vec: learns word × context directly`

## Properties of the Embedding Space
- `king - man + woman ≈ queen`
- Similar words are close in cosine distance

## Related
- [[Text Representation]] — Word2Vec is one text representation method
- [[Categorical Encoding]] — embeddings also solve high-cardinality encoding
- [[Dimensional Reduction]] — embeddings ARE a form of dim reduction
