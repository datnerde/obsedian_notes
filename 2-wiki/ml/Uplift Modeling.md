---
title: Uplift Modeling
tags: [ml, causal-inference, marketing, response-modeling]
created: 2026-04-19
status: seedling
related: [[Logistic Regression]], [[AB Testing]], [[Classification Metrics]]
source: Data Mining Problems in Retail (Katsov 2015)
---

# Uplift Modeling

## Core Idea

Predict the **incremental effect** of an intervention, not the raw response probability. Formally: estimate $P(\text{buy} \mid \text{treated}) - P(\text{buy} \mid \text{control})$ per customer, then target only customers with **positive uplift**.

Also called **differential response analysis** or **true-lift modeling**.

## The Problem Naive Response Modeling Misses

Classic response modeling picks customers by $P(\text{respond} \mid \text{incentive})$. This favors:

- ✅ Customers likely to buy *because of* the incentive
- ❌ Customers who would have bought *anyway* (wasted coupon)
- ❌ Customers who may be *annoyed* by the incentive (negative uplift)

> **Canonical example**: should you send a 10%-off apples coupon to a customer who buys apples every day? Naive response modeling says yes (high response probability). Uplift modeling says no — they would have bought at full price, so the coupon is a pure revenue leak.

## Four Quadrants

| | Buys with incentive | Doesn't buy with incentive |
| --- | --- | --- |
| **Buys without incentive** | Sure thing (don't incentivize) | Do-not-disturb (negative uplift) |
| **Doesn't buy without** | **Persuadable** ✅ (target these) | Lost cause |

Only the **persuadables** have positive uplift. Naive targeting burns money on "sure things" and possibly on "do-not-disturbs."

## Mathematical Formulation

Define four gross-margin values over a target set $U$:

- $G_1$: select $U$ by targeting model, send incentives
- $G_2$: select $U$ randomly, send incentives
- $G_3$: select $U$ by targeting model, no incentives
- $G_4$: select $U$ randomly, no incentives

**Naive response modeling** maximizes $G_1 - G_2$ (lift over random).

**Uplift modeling** maximizes $(G_1 - G_2) - (G_3 - G_4)$ — the lift *beyond what the same customers would have done untreated*:

$$\arg\max_{U \subseteq P} \sum_{u \in U}\left[E\{g \mid u; I\} - E\{g \mid u; \bar{I}\}\right] - c$$

where $I$ = incentive offered, $\bar{I}$ = no incentive, $c$ = incentive cost.

## Estimation

Requires **both** outcome distributions (treated and control). Common approaches:

1. **Two-model (T-learner)**: fit two regression models, one on treated, one on control; predict difference.
2. **Single-model with treatment indicator (S-learner)**: fit one model with a treatment flag as a feature.
3. **Class transformation**: reframe as a single classification problem via a relabeling trick.

All require randomized training data — an [[AB Testing]] holdout or historical experiment. Without randomization, confounders bias the uplift estimate.

## Relation to Propensity Modeling

Uplift is one member of the broader **propensity-modeling** family used in retail:

- **Predicted lifetime value (LTV)** — expected revenue over the full customer relationship
- **Share of wallet** — fraction of category spend captured vs competitors
- **Propensity to churn** — likelihood of permanently leaving
- **Propensity to change shopping habits** — life-event detection (moving, marriage, pregnancy — the canonical "Target pregnancy prediction")

## Reported Impact

Uplift modeling adds roughly **+15% performance** on top of response modeling, which itself adds +20–30% over random targeting (retail industry benchmarks per Katsov 2015).

## Related

- [[Logistic Regression]] — the base estimator most often used for response probability
- [[AB Testing]] — provides the randomization needed for unbiased uplift estimation
- [[Classification Metrics]] — uplift curves replace ROC curves in evaluation
- [[Data Mining Problems in Retail]] — source, Problem 1 (Response Modeling)
