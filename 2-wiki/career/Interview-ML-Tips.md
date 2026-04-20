---
title: Interview ML Tips
tags: [career, interview, ml, data-science]
created: 2026-04-19
status: evergreen
related: [[Ensemble-Methods]], [[Statistical-Tests-Cheat-Sheet]], [[ML-Coding-Patterns]], [[AB-Testing-Experiment-Design]]
source: Notion Project Seattle — Interview Feedback
---

# Interview ML Tips

> Distilled from real interview feedback. Hyperparameter tuning order, model comparison table, and common Q&A.

---

## Boosting Algorithm Comparison

| Algorithm | Core Idea | Key Strengths | Weaknesses | Interview Tip |
|---|---|---|---|---|
| **AdaBoost** | Sequentially reweights misclassified samples | Simple, intuitive, works on clean data | Sensitive to noise/outliers | Emphasize *sample reweighting* |
| **GBM** | Sequentially fits residuals via gradient descent | Flexible (custom loss functions), general framework | Slow training, can overfit | Highlight *residual fitting (gradients)* |
| **XGBoost** | GBM + regularization (L1/L2), parallel training, handles missing values | Strong performance, robust, efficient | Many hyperparameters, overfitting risk without tuning | Mention *regularization + efficiency* |
| **LightGBM** | Histogram-based splits, leaf-wise growth (deepest leaf with max gain) | Extremely fast, memory efficient, handles categorical features | Can overfit small datasets, sensitive to hyperparams | Stress *speed + scalability* |
| **CatBoost** | Ordered boosting + efficient categorical encoding | Great on categorical-heavy data, minimal preprocessing | Slower than LightGBM | Point out *categorical handling advantage* |

---

## XGBoost — Hyperparameter Tuning Order

Tune in this order: `learning_rate → n_estimators → max_depth → subsample → colsample_bytree → min_child_weight`

| Param | Effect |
|---|---|
| `n_estimators` | Boosting rounds — too few = underfit, too many = overfit |
| `learning_rate` (eta) | Smaller → better generalization, but need more trees |
| `max_depth` | Tree complexity — higher → overfit |
| `min_child_weight` | Min weight per leaf — regularization |
| `subsample` | Fraction of rows per tree — reduces variance |
| `colsample_bytree/bylevel/bynode` | Fraction of features per split — adds randomness |
| `gamma` | Min loss reduction to split — higher → conservative |
| `lambda, alpha` | L2/L1 regularization |

---

## Random Forest — Key Hyperparameters

Focus on these in interviews: `n_estimators, max_depth, min_samples_split, max_features`

| Param | Effect |
|---|---|
| `n_estimators` | Number of trees — ↑ stability, slower |
| `max_depth` | Depth of trees — controls overfitting |
| `min_samples_split / min_samples_leaf` | Regularization — prevents overly complex trees |
| `max_features` | Features at each split — smaller = more randomness |
| `class_weight` | Handles class imbalance |

---

## Core Interview Q&A

**Q: Why scale features?**
- Regression: avoids ill-conditioned $X^TX$, stabilizes coefficients
- Boosting: smoother gradients, faster convergence
- General: optimization stability

**Q: Why remove highly correlated features in regression?**
- Multicollinearity makes $X^TX$ nearly singular
- Leads to unstable, high-variance coefficients

**Q: Why Random Forest sometimes outperforms XGBoost?**
- RF reduces variance via averaging, robust to noise
- XGBoost requires careful tuning, can overfit small/noisy data
- RF often generalizes better on simple/noisy signals

**Q: Why AUC-ROC instead of F1/Precision/Recall?**
- AUC: threshold-independent, measures ranking ability
- F1/Precision/Recall: depend on chosen threshold (set by business)

**Q: Why time-series CV over random split?**
- Respects temporal order, avoids leakage
- Captures regime shifts (holidays, rate changes)
- Produces more stable validation

**Q: One-Hot Encoding in trees — any issues?**
- Splits category info across many features → may dilute signal
- Alternatives: target encoding or embeddings

---

## Time Series Models — Temporal Awareness

| Model | Native Temporal Order | With Feature Engineering | Notes |
|---|---|---|---|
| **Linear Regression** | No | Can add lag, rolling stats, seasonality indicators | Easy to interpret; suffers with collinearity/non-stationarity |
| **Random Forest** | No | Works well with lagged/rolling features | Robust to noise, stable |
| **XGBoost/LightGBM/CatBoost** | No | Strong performance with lag/rolling/time features | Must use time-series CV to avoid leakage |
| **ARIMA / SARIMA** | Yes | Limited feature flexibility | Built for temporal autocorrelation & seasonality |
| **RNN / LSTM / Transformers** | Yes | Can incorporate external features | Designed for sequences; needs more data & compute |

---

## Pandas Quick Tips

```python
df.isna().sum(axis=1)  # count missing values per row
df['digits_only'] = df['text'].astype(str).str.replace(r'\D', '', regex=True)  # extract digits
```
