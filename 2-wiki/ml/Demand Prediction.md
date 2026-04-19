---
title: Demand Prediction
tags: [ml, regression, econometrics, retail]
created: 2026-04-19
status: seedling
related: [[Logistic Regression]], [[Optimization]], [[Recommender Systems]]
source: Data Mining Problems in Retail (Katsov 2015)
---

# Demand Prediction

## Core Idea

Forecast the number of units of product $j$ that will sell under a given set of conditions (price, competitor prices, weather, day-of-week, promotions, store properties). Outputs feed price optimization, sales-event planning, stock-level optimization, and assortment planning.

## Multiplicative Decomposition

A practical factorization — validated at Albert Heijn ([KOK07]), RueLaLa, Zara:

$$D_j = V \cdot P(\text{purchase} \mid \text{visit}) \cdot P(j \mid \text{purchase}) \cdot E[Q \mid j, \text{purchase}]$$

Each factor is estimated with its own regressor from transactional data:

| Factor | Meaning | Model |
| --- | --- | --- |
| $V$ | Visits per day | Log-linear regression over weather, day-of-week, holidays |
| $P(\text{purchase} \mid \text{visit})$ | Purchase incidence | Logistic regression ([[Logistic Regression]]) |
| $P(j \mid \text{purchase})$ | Product choice among alternatives | **Multinomial Logit (MNL)** |
| $E[Q \mid j, \text{purchase})]$ | Basket quantity | Linear / Poisson regression |

## Multinomial Logit for Product Choice

The canonical choice-theory model (McFadden, Nobel 2000):

$$P(j \mid \text{purchase}) = \frac{\exp(y_j)}{\sum_i \exp(y_i)}$$

where the utility score is a linear function of observable features:

$$y_j = \gamma_j + \gamma_{N+1}(R_j - \bar{R}) + \gamma_{N+2}(A_j - \bar{A})$$

- $R_j, \bar{R}$: product price, category-average price
- $A_j, \bar{A}$: promotion dummy, category-average promotion rate
- Using **deviations from category averages** as regressors captures relative (rather than absolute) competitiveness

MNL is structurally the **softmax** from [[Logistic Regression]] — but here the "classes" are products competing for a shopper's choice, not disjoint labels. The coefficients $\gamma_{N+1}, \gamma_{N+2}$ are **shared across products**, which is what makes the model identifiable and tractable.

## Independence of Irrelevant Alternatives (IIA)

MNL assumes that the **ratio** $P(i)/P(j)$ is independent of any third product $k$. This fails in practice when products have shared unobserved attributes (e.g., two different red shirts both lose share equally when a new red shirt enters — not true if color drives substitution). Nested logit and mixed logit relax IIA at the cost of complexity.

## What-If Analysis

A trained demand model enables **counterfactual queries** that drive downstream optimization:

- "If we cut price of product $j$ by 10%, how do units of $j$ and of substitutes shift?"
- "Should this SKU be promoted this week given the forecast?" — see [[Optimization]] for the argmax layer
- "What's the price-sensitivity × package-size interaction?" (often reveals demographic/store-level heterogeneity)

## Stockout Censoring

Historical sales data is **censored** when stock runs out: observed demand = min(true demand, stock level). Sales events especially invite stockouts. A practitioner workaround (RueLaLa [JH14]): fit demand curves **only on items that didn't stock out**, then transfer those curves as priors to items whose data is censored.

## Boundary with Recommender Systems

[[Recommender Systems]] personalize $P(j \mid u)$ (per-user item choice). Demand prediction aggregates to population level $P(j \mid \text{purchase})$ for inventory/pricing decisions. The math rhymes — both rely on softmax-style scoring — but the decision target differs (individual surfacing vs. population inventory).

## Related

- [[Logistic Regression]] — MNL is multinomial (softmax) logistic regression specialized to discrete choice
- [[Optimization]] — demand forecast feeds argmax over price / stock / assortment
- [[Recommender Systems]] — personalization analogue
- [[Data Mining Problems in Retail]] — source, Problem 3 (Demand Prediction) and Problems 4–6 (which consume demand forecasts)
