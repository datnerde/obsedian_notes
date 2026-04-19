---
title: Machine Learning — Map of Content
tags: [moc, ml]
created: 2026-04-14
status: growing
---

# Machine Learning — Map of Content

> Navigation hub for all ML notes.
> Source: primarily from *Quest for Machine Learning* (百面机器学习).

---

## Sources

- [[Quest-for-Machine-Learning]] — chapter index for 百面机器学习 (in `1-sources/`)
- [[article-2015-03-10-Data-Mining-Problems-in-Retail]] — Katsov's survey of 6 retail optimization problems
- All content compiled into atomic notes below

---

## Topics

### Feature Engineering

- [[Feature Engineering]] — hub note
  - [[Feature Normalization]] — Min-Max, Z-Score; why gradient descent needs it
  - [[Categorical Encoding]] — ordinal, one-hot, binary encoding
  - [[Text Representation]] — Bag of Words, TF-IDF, topic models
  - [[Word2Vec]] — CBOW, Skip-gram, embedding space

### Dimensionality Reduction

- [[Dimensional Reduction]] — hub note
  - [[PCA]] — unsupervised, maximize variance
  - [[LDA (Linear Discriminant Analysis)]] — supervised, maximize class separation

### Models

#### Supervised

- [[Classic Model]] — hub with comparison table
  - [[SVM]] — max-margin hyperplane, kernel trick
  - [[Logistic Regression]] — log-odds model, Softmax for multi-class
  - [[Decision Tree]] — recursive splits, pruning, no normalization needed

#### Unsupervised

- [[Unsupervised Learning]] — hub note
  - [[K-Means Clustering]] — hard assignment, EM, K++
  - [[Gaussian Mixture Model]] — soft assignment, probabilistic

#### Probabilistic

- [[Probability Graphical Model]] — Bayesian Networks, MRF

### Training & Optimization

- [[Optimization]] — Gradient Descent, SGD, Adam, RMSProp

### Evaluation

- [[Model Evaluation]] — hub note
  - [[Classification Metrics]] — Accuracy, Precision, Recall, F1
  - [[ROC and AUC]] — threshold-invariant, robust to imbalance
  - [[Cross Validation]] — K-fold, LOO, Bootstrap
  - [[Overfitting and Underfitting]] — bias-variance, regularization
  - [[Hyperparameter Tuning]] — grid search, random, Bayesian
  - [[AB Testing]] — online evaluation, causal inference

### Sampling & Statistics

- [[Sampling]] — hub note
  - [[MCMC]] — high-dimensional sampling via Markov chains
  - [[Imbalanced Data]] — SMOTE, over/under-sampling

### Applied / Marketing & Retail

- [[Recommender Systems]] — content vs collaborative filtering, multi-objective ranking
- [[Uplift Modeling]] — differential response / incremental lift estimation
- [[Demand Prediction]] — multiplicative decomposition, MNL choice model

---

## Key Concept Graph

```txt
Raw Data
  └── Feature Engineering
        ├── Feature Normalization ──────→ Optimization (faster convergence)
        ├── Categorical Encoding
        ├── Text Representation ────────→ Word2Vec
        └── Dimensional Reduction
              ├── PCA (unsupervised)
              └── LDA (supervised)
                    ↓
              Model Training
              ├── Classic Model (SVM, LR, DT)
              ├── K-Means / GMM (unsupervised)
              └── Optimization (gradient descent)
                    ↓
              Evaluation
              ├── Classification Metrics → ROC and AUC
              ├── Cross Validation
              ├── Overfitting and Underfitting
              └── AB Testing (online)
```

---

## To Be Added

- `Deep Learning` — neural network fundamentals
- `Transformer / Attention` — self-attention, BERT, GPT
- `Ensemble Methods` — Random Forest, Gradient Boosting, XGBoost
- `MLOps / Model Serving`

---

[[INDEX]] | [[CLAUDE]]
