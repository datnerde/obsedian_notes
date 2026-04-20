---
title: Causal Inference
tags: [ml, statistics, causal-inference, ab-testing, experiment-design]
created: 2026-04-19
status: evergreen
related: [[AB Testing]], [[AB-Testing-Statistics-Deep-Dive]], [[AB-Testing-Experiment-Design]], [[Uplift Modeling]]
source: Notion Project Seattle — A/B Testing
---

# Causal Inference

> Beyond A/B Testing — the full arsenal for when randomization isn't possible. Decision tree: randomizable → time-series → cross-sectional → causal ML.

---

## Method Selection Decision Tree

1. **Can we randomize?** → A/B Test (RCT) — gold standard
2. **No, but is there a threshold/cutoff?** → Regression Discontinuity Design (RDD)
3. **No, but is there a time-series + intervention point?** → DiD / CausalImpact
4. **Only observational data with many confounders?** → PSM / IPW / Double Machine Learning
5. **Strong external instrument available?** → Instrumental Variables (IV)

---

## Level 1: A/B Testing Extensions (Advanced)

When you *can* randomize, use these enhancements that Google/Netflix/Uber have adopted:

| Pain Point | Solution | Interview Pitch |
|---|---|---|
| **Small sample / high variance** | **CUPED** (Microsoft/Uber/Netflix) | Use pre-experiment data as covariate to remove treatment-irrelevant variance. Shortens experiment duration significantly. |
| **Long-term effect estimation** | **Surrogate Metrics** (Netflix/Google) | Build a causal chain from a short-term proxy (e.g. Day 7 watch time) to long-term LTV/retention. |
| **Network effects / spillover** | **Switchback Experiments** (Uber/DoorDash) | Rotate treatment between time windows or use cluster randomization (by city) to isolate interference. |
| **Non-compliance** | **IV + CACE** (Uber/Google) | Use assignment as instrument; estimate Complier Average Causal Effect for users who actually received treatment. |

---

## Level 2: Quasi-Experiments (Time-Based)

*When there's a historical data + a clear intervention point.*

### Synthetic Control (CausalImpact)
- **Idea:** Construct a counterfactual time series by weighting donor units (e.g. other markets) to match pre-period.
- **Tool:** Google's `CausalImpact` package (Bayesian Structural Time Series) — more flexible than classical SC.
- **Use when:** Marketing campaigns, full-rollout policy changes where only one "treated" unit exists.
- **Interview must-mention:** CausalImpact builds a BSTS model on pre-period, then forecasts the counterfactual.

### Difference-in-Differences (DiD)
- **Idea:** Compare the *change* in treatment group to the *change* in control group across time.
- $\tau = (Y_{treat, post} - Y_{treat, pre}) - (Y_{control, post} - Y_{control, pre})$
- **Core assumption:** **Parallel Trends** — without intervention, both groups would have followed the same trend.
- **Use when:** Feature launched in one city/platform but not another.
- **Trap:** If pre-trends differ, DiD is invalid → escalate to Synthetic Control or PSM-DiD.

### Regression Discontinuity Design (RDD)
- **Idea:** Compare units just above and just below a threshold (e.g. loyalty tier cutoff).
- $Y = \alpha + \tau T + \beta_1(X - c) + \beta_2 T(X - c) + \epsilon$ where $c$ is the cutoff.
- **Core assumption:** Continuity — all other characteristics are smooth at the threshold.
- **Limitation:** LATE only — results only generalize to users *near* the cutoff, not all users.

---

## Level 3: Observational Methods (Cross-Sectional)

*When there's no time dimension — only user-level data.*

### Propensity Score Matching (PSM)
- **Idea:** Find "twins" — match treated users to control users with similar propensity $P(T=1|X)$.
- **Steps:** Logistic Regression to get scores → 1:1 or 1:k matching → compute ATT on matched pairs.
- **Limitation:** Only controls for *observed* confounders. Unobserved variables (e.g. user intent) still bias results.

### Inverse Probability Weighting (IPW)
- **Idea:** Reweight samples instead of discarding. Upweight control users who "look like" treatment users.
- **When:** Same as PSM but you want to keep all samples (PSM discards unmatched).
- **Risk:** Extreme weights when $e(x)$ is near 0 or 1 — use truncated IPW.

### Double Machine Learning (Double ML / EconML)
- **Idea:** Use ML to partial out confounders from both outcome and treatment, then regress residuals on residuals.
- **When:** High-dimensional features where linear regression fails.
- **Tool:** Microsoft's `EconML`, Uber's `CausalML`.
- **Advantage over PSM:** Handles hundreds of features without regularization bias.

### Instrumental Variables (IV)
- **Idea:** Find $Z$ that affects $T$ but doesn't directly affect $Y$ — use as natural randomizer.
- **3 requirements:** Relevance ($Z \perp\!\!\!\!\perp T$ strongly), Exclusion ($Z$ affects $Y$ only through $T$), Independence ($Z$ uncorrelated with confounders).
- **Industry use:** Push notification send (randomized) as IV for feature usage → Encouragement Design.

---

## Level 4: Causal ML (Heterogeneous Treatment Effects)

When you need to know *who* benefits from treatment (HTE), not just average effects (ATE).

### Uplift Modeling / Meta-Learners
Estimate $\tau_i = E[Y_i^1 - Y_i^0 | X_i]$ for each user individually.

| Method | Approach |
|---|---|
| **S-Learner** | Add $T$ as a feature in one model |
| **T-Learner** | Train separate models for $M_1$ (treated) and $M_0$ (control), subtract |
| **X-Learner** | T-Learner with cross-fitting — handles imbalanced treatment/control |
| **Causal Forest** | RF variant where splits maximize inter-group differences, not information gain |

**Key distinction:** Target *Persuadables* (only convert with treatment) — avoid *Sure Things* (convert anyway, wasting budget) and *Sleeping Dogs* (treatment backfires).

**Evaluation:** Qini Curve / AUUC — since individual ground truth $\tau_i$ is unknowable, rank by predicted uplift and measure cumulative incremental gain.

---

## 4-Step Causal Modeling Framework (DoWhy / Microsoft)

*Shows senior-level thinking — go beyond "run a model" to "design the causal graph".*

1. **Model (Draw DAG):** Map business knowledge into a Directed Acyclic Graph — who causes what? Where are confounders? Colliders?
2. **Identify:** Using the DAG, determine whether the causal effect is *identifiable*. If unobserved confounders exist and no IV is available → be honest: "we can only measure correlation."
3. **Estimate:** Choose method based on DAG — CausalImpact for time series, DML for high-dimensional, CausalForest for HTE.
4. **Refute (most important — shows seniority):**
   - **Placebo Test:** Replace real treatment with random noise → result should be ≈ 0.
   - **Subset Validation:** Run on a sub-group known to have no effect → verify zero result.

---

## Quick Reference: Scenario → Method

| Scenario | Method | Key Terms |
|---|---|---|
| 5% traffic rollout available | A/B Test | Randomization, SUTVA |
| Feature launched in one city only | Synthetic Control / DiD | Parallel Trends, Counterfactual |
| Premium feature, users self-select | PSM / IPW | Selection Bias, Propensity Score |
| Hard rule: spend > $100 gets reward | RDD | Threshold, LATE, Continuity |
| Full rollout of ad campaign, no holdout | CausalImpact | BSTS, Bayesian, Counterfactual forecast |
| Push notification as partial treatment | IV | Intent-to-Treat, Non-compliance, LATE |
| Budget allocation: maximize uplift per dollar | Uplift Modeling | HTE, Causal Forest, Persuadables |
| Validate model isn't spurious | Placebo Test | Sensitivity Analysis, Refutation |

---

## Common Interview Traps

**Q: Why can't PSM replace A/B tests?**
PSM only balances *observed* variables. Unobserved variables (user intent, mood) still confound. Only randomization balances unobservables.

**Q: DiD parallel trends test failed — what now?**
1. Use Synthetic Control (builds better counterfactual from donor pool).
2. PSM-DiD (match on trends first, then difference).
3. Admit causal identification is impossible — report correlation only.

**Q: How do you evaluate an uplift model if you can't know individual treatment effects?**
Use Qini Curve or AUUC — sort users by predicted uplift, compute cumulative incremental conversion, compare to random baseline.
