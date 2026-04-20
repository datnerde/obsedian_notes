---
title: Statistical Tests Cheat Sheet
tags: [ml, statistics, ab-testing, hypothesis-testing]
created: 2026-04-19
status: evergreen
related: [[AB-Testing-Statistics-Deep-Dive]], [[AB Testing]], [[Cross Validation]]
source: Notion Statistical Tests Cheat Sheet
---

# Statistical Tests Cheat Sheet

> Decision guide: scenario → assumptions → test statistic → when to use. For A/B testing and data science interviews.

---

## Group Mean Comparison

### When to Use Which t-test

| Scenario | Test | Key Condition |
|---|---|---|
| 2 independent groups, equal variance | Student's t | $\sigma_1^2 \approx \sigma_2^2$ |
| 2 independent groups, unequal variance | **Welch's t** ✅ | Default for industry A/B tests |
| Same subjects before/after | Paired t | $d_i = x_{i,\text{before}} - x_{i,\text{after}}$ |
| ≥ 3 groups | One-way ANOVA → post-hoc (Tukey HSD) | Variance homogeneity |

**Interview tip:** Default to Welch's t-test for 2-group comparison. It's more robust to variance differences with negligible power cost.

### Welch's t-test

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

df via Welch–Satterthwaite approximation (messy formula; just say "approximated").

### Paired t-test

$$t = \frac{\bar{d}}{s_d / \sqrt{n}}, \quad df = n-1$$

where $d_i = x_{i1} - x_{i2}$. Tests mean of differences — more powerful than two-sample t when observations are correlated.

---

## Non-Parametric Alternatives

Use when: small sample, heavy skew, outliers, or when you can't assume normality.

| Parametric | Non-Parametric Equivalent | When to Switch |
|---|---|---|
| Two-sample t | **Mann–Whitney U** | Non-normal, outliers, ordinal data |
| Paired t | **Wilcoxon Signed-Rank** | Paired non-normal data |
| Pearson correlation | **Spearman correlation** | Monotone but non-linear relationship |

**Mann–Whitney U**: rank all observations, sum ranks by group; tests whether distributions differ.

**Wilcoxon Signed-Rank**: rank absolute differences, test whether positive and negative ranks are balanced.

---

## Categorical / Count Data

| Test | Scenario | Condition |
|---|---|---|
| **Chi-square** | 2+ categories × 2+ groups | Expected cell count > 5 |
| **Fisher's exact** | 2×2 table, small $n$ or low rates | No minimum count requirement |

Chi-square statistic: $\chi^2 = \sum \frac{(O - E)^2}{E}$, df = $(r-1)(c-1)$

---

## Correlation

| Test | Tests For | Assumption |
|---|---|---|
| **Pearson** $r$ | Linear relationship | Sensitive to outliers |
| **Spearman** $\rho$ | Monotone (rank) relationship | Works for $y = x^3$, ordinal data |

Pearson significance: $t = r\sqrt{\frac{n-2}{1-r^2}}$, df = $n-2$

---

## Time Series Tests

| Test | Purpose | Key Point |
|---|---|---|
| **ADF** (Augmented Dickey-Fuller) | Stationarity check | $p < 0.05$ → stationary; needed before ARIMA |
| **Ljung–Box** | Residual autocorrelation | Significant → model hasn't extracted all signal |
| **Mann–Kendall** | Monotone trend (non-parametric) | Robust to outliers |
| **Granger causality** | Predictive causality ($X$ helps forecast $Y$) | Not physical causality; requires stationarity |
| **Diebold–Mariano** | Compare two forecasting models | 🔥 Key interview answer for "how to compare models"; handles autocorrelated errors |

---

## Comparing Two Models (Interview Q: "How would you compare model performance?")

| Data Form | Method |
|---|---|
| Single scalar metric | Just compare numbers; can't do statistical test |
| Per-sample scores (paired) | **Paired t-test** |
| Time-series forecasting errors | **Diebold–Mariano** |
| Any, distribution-free | **Paired Permutation Test** (resample-based) |

---

## Multiple Testing Correction

| Method | Controls | When to Use |
|---|---|---|
| **Bonferroni** | FWER (any false positive) | Conservative; few tests; independent tests |
| **FDR (Benjamini-Hochberg)** | Expected false discovery rate | Many tests; correlated metrics |
| **OEC** | N/A — combines metrics | Pre-specify a weighted composite metric |

---

## Quick Decision Tree

```
How many groups? 
  2 → Are they paired?
        Yes → Paired t or Wilcoxon
        No  → Is data continuous?
                Yes → Welch's t (default) or Mann-Whitney
                No  → Chi-square or Fisher's exact
  3+ → ANOVA → Tukey HSD post-hoc

Is it a time series?
  Check stationarity → ADF
  Compare forecasts → Diebold-Mariano
  Check residuals → Ljung-Box
```
