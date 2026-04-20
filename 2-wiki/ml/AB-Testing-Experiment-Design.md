---
title: A/B Testing — Experiment Design
tags: [ml, ab-testing, statistics, experiment-design]
created: 2026-04-19
status: growing
related: [[AB Testing]], [[AB-Testing-Statistics-Deep-Dive]], [[Statistical-Tests-Cheat-Sheet]]
source: Notion A/B Testing
---

# A/B Testing — Experiment Design

> Design choices that determine whether your experiment results are trustworthy. See [[AB-Testing-Statistics-Deep-Dive]] for the statistical machinery.

---

## 1. Unit of Diversion (What Gets Randomized)

| Unit | When to Use | Notes |
|---|---|---|
| **User ID** | Signed-in experience | Consistent across sessions, most common |
| **Cookie / Anonymous ID** | Anonymous users | Changes if user clears cookies |
| **Device ID** | Mobile apps | Tied to device, can't be changed by user |
| **Page view / Event** | High-volume metrics | Each event is independent → valid IID assumption |
| **IP address** | Location-specific | Can change; use carefully |

**Key principle:** Unit of diversion should be ≥ unit of analysis (the denominator in your metric).

- If they match (e.g., both = page view for CTR): variance is correctly estimated analytically
- If they don't match (e.g., cookie for CTR): observations within a cookie are *correlated* → empirical variance > analytical → under-powered test

---

## 2. Population Selection

### Restricting to a Subpopulation
- Non-English users dilute the effect of an English UX change → restrict to English users
- Reduces noise, increases power — but limits generalizability

### Cohort vs. Full Population

**Use full population** when you just need a cross-sectional effect estimate.

**Use cohorts** (users who enter the experiment at the same time) when:
- Looking for **learning effects** — how behavior changes over exposure time
- Examining **retention** — need users who joined together
- Detecting **change aversion or novelty effect** — compare cohort at Week 1 vs Week 4

---

## 3. Learning Effects

Two opposing behavioral dynamics from new experiences:

- **Change aversion**: users resist changes, engagement temporarily drops
- **Novelty effect**: users explore new features, engagement temporarily rises

Both cause the measured effect to be unstable early in the experiment.

**Detection method**: Pre/post-period analysis
- *Pre-period*: Run A/A test before the experiment. Any difference = baseline variability, not the treatment
- *Post-period*: After exposing users, run another A/A test. Difference = residual learning effect

**Dosage-based cohorts**: Segment by *how many times* the user has seen the change (not just how long) — better proxy for learning state.

---

## 4. Choosing Sample Size

Key inputs:
- $\delta$ (MDE — minimum detectable effect)
- $\sigma^2$ (variance of the metric)
- $\alpha$ (significance level, typically 0.05)
- $1 - \beta$ (power, typically 0.80)

**Ways to reduce required sample size (to run shorter experiments):**
1. Increase $\delta$ (only care about larger effects)
2. Increase $\alpha$ (accept more false positives)
3. Reduce $\beta$ (accept lower power)
4. Change unit of diversion to match unit of analysis → reduces empirical variance
5. Target a subpopulation with stronger expected effect

---

## 5. Duration

**Why not expose 100% of traffic immediately?**
- **Safety**: bug in treatment shouldn't affect all users
- **PR risk**: users or press may notice features you haven't committed to
- **Confounders**: holiday effects, day-of-week variance
- **Experiment collisions**: running multiple tests simultaneously → need traffic splitting

**Minimum duration rule**: Run for at least **2 full weeks** to capture day-of-week effects. If testing seasonal products, run across relevant cycle.

---

## Sanity Checks (Before Looking at Results)

Before analyzing outcomes, verify the experiment is set up correctly:

1. **Population balance**: treatment and control should have similar sizes (check $\hat{p} \approx 0.5$ for 50/50 split — compute CI and verify observed split is within it)
2. **Invariant metrics unchanged**: metrics that shouldn't change (browser version, user age) should be identical across groups
3. **Data pipeline consistency**: filters applied the same way in both groups; logging captures events correctly

---

## Related

- [[AB-Testing-Statistics-Deep-Dive]] — CLT, p-value, power analysis, multiple metrics
- [[Statistical-Tests-Cheat-Sheet]] — choosing the right test
- [[AB Testing]] — interview procedure framework
