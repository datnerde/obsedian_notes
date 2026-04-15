---
title: ROC and AUC
tags: [ml, model-evaluation, metrics]
created: 2026-04-14
status: evergreen
related: [[Classification Metrics]], [[Model Evaluation]], [[Imbalanced Data]]
source: Quest for Machine Learning
---

# ROC and AUC

## Core Idea
ROC curve evaluates a classifier across ALL classification thresholds simultaneously. AUC summarizes this into a single number. Unlike accuracy, ROC/AUC is robust to class imbalance.

## Definitions
- **TPR (True Positive Rate)** = Recall = TP / P
- **FPR (False Positive Rate)** = FP / N

ROC curve plots TPR vs FPR as the decision threshold varies from 0 to 1.

## AUC (Area Under Curve)
- Range: [0.5, 1.0]
- AUC = 0.5 → random classifier
- AUC = 1.0 → perfect classifier
- Intuition: probability that a randomly chosen positive example is ranked higher than a randomly chosen negative

## ROC vs Precision-Recall Curve
| | ROC | P-R Curve |
|---|---|---|
| Stable when class balance changes? | ✅ Yes | ❌ No |
| Best for imbalanced problems? | ✅ | ✅ Better for extreme imbalance |
| Standard for most tasks? | ✅ | — |

## Key Insight
ROC keeps its shape when the proportion of positives/negatives changes. This makes it the standard for comparing classifiers across datasets with different class distributions.

## Related
- [[Classification Metrics]] — Precision, Recall, F1
- [[Imbalanced Data]] — when class balance matters
