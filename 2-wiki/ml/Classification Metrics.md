---
title: Classification Metrics
tags: [ml, model-evaluation, metrics]
created: 2026-04-14
status: evergreen
related: [[Model Evaluation]], [[ROC and AUC]], [[Imbalanced Data]]
source: Quest for Machine Learning
---

# Classification Metrics

## Core Idea
Different metrics capture different failure modes of classifiers. Accuracy is often misleading — choose metrics that match your actual problem.

## The Confusion Matrix

| | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actually Positive** | TP | FN |
| **Actually Negative** | FP | TN |

## Key Metrics

### Accuracy
`Accuracy = (TP + TN) / Total`
- ❌ Misleading with imbalanced classes (see [[Imbalanced Data]])
- A model predicting "always negative" on 95/5 split gets 95% accuracy

### Precision
`Precision = TP / (TP + FP)`
- "Of the ones I predicted positive, how many actually were?"
- Optimize when **false positives are costly** (spam filter, fraud detection)

### Recall (Sensitivity / TPR)
`Recall = TP / (TP + FN)`
- "Of all actual positives, how many did I catch?"
- Optimize when **false negatives are costly** (cancer detection)

### F1 Score
`F1 = 2 × (Precision × Recall) / (Precision + Recall)`
- Harmonic mean — balances both
- Use when you need a single metric and classes are imbalanced

## Precision-Recall Tradeoff
Increasing the classification threshold → ↑ Precision, ↓ Recall
P-R curve shows this tradeoff across all thresholds.

## Related
- [[ROC and AUC]] — threshold-invariant evaluation
- [[Imbalanced Data]] — when accuracy breaks down
- [[Model Evaluation]] — parent topic
