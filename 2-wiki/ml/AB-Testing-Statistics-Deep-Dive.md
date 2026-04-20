---
title: A/B Testing — Statistics Deep Dive
tags: [ml, ab-testing, statistics, hypothesis-testing]
created: 2026-04-19
status: growing
related: [[AB Testing]], [[Statistical-Tests-Cheat-Sheet]], [[AB-Testing-Experiment-Design]]
source: Notion A/B Testing
---

# A/B Testing — Statistics Deep Dive

> The mathematical foundations behind A/B testing. See [[AB Testing]] for the procedure overview and [[AB-Testing-Experiment-Design]] for design choices.

---

## Central Limit Theorem (Why We Can Use t-tests)

For i.i.d. random variables $X_i$ with mean $\mu$ and variance $\sigma^2$:

$$\bar{X}_n \sim N\!\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{(approximately, for large } n\text{)}$$

- When $n < 30$: CLT doesn't hold reliably → use **t-distribution** instead of z
- This is the justification for using t-tests on non-normal metrics in large-sample A/B tests

---

## Hypothesis Testing Framework

- **$H_0$** (null): no difference between control and treatment
- **$H_1$** (alternative): treatment has an effect
- **One-sided**: "B is better than A" (directional)
- **Two-sided**: "A and B differ" (bidirectional) — safer default

---

## p-value — What It Actually Means

> p-value = probability of observing data *at least as extreme* as what we saw, **assuming $H_0$ is true**

**Common interview trap:** ❌ "95% probability the null is false" is wrong.

✅ Correct: "If $H_0$ were true, we'd see results this extreme less than 5% of the time."

It measures **strength of evidence against $H_0$**, not probability that $H_0$ is false.

---

## Confidence Interval

$$CI = \bar{x} \pm z^* \cdot SE \quad \text{where } SE = \sigma/\sqrt{n}$$

- Wider CI → more uncertainty (less data or higher confidence level)
- CI and hypothesis test are dual: CI excludes 0 ↔ p-value < α

---

## Type I & Type II Errors

| | $H_0$ True | $H_0$ False |
|---|---|---|
| **Reject $H_0$** | Type I Error (FP) — rate = $\alpha$ | Correct (Power = $1-\beta$) |
| **Fail to Reject** | Correct | Type II Error (FN) — rate = $\beta$ |

- $\alpha$ = significance level (usually 0.05)
- Power = $1 - \beta$ (usually aim for 0.8)

---

## Power Analysis — Factors

Power increases when:
- **Effect size** is larger (easier to detect)
- **Sample size** is larger
- **Variance** is smaller
- **$\alpha$** is raised (but that increases Type I error)

**Sample size formula:**
$$n \approx \frac{(z_{\alpha/2} + z_\beta)^2 \cdot 2\sigma^2}{\delta^2}$$

where $\delta$ = minimum detectable effect (MDE), $\sigma^2$ = variance of metric.

---

## Handling Non-Normal Data

When CLT doesn't hold (small $n$, heavy skew):

1. **Check sample size first** — if $n > 30$, t-test is usually fine
2. **Log transformation** — works for revenue, session duration, other right-skewed metrics
3. **Winsorization / Capping** — clip outliers at 95th or 99th percentile
4. **Non-parametric tests** — Mann-Whitney U (no distributional assumption)
5. **Bootstrap** — resample with replacement to construct empirical CI; most robust, most expensive

---

## Multiple Metrics Problem

Running multiple tests inflates the false positive rate. If you test $m$ metrics at $\alpha = 0.05$:

$$P(\text{at least one false positive}) = 1 - (1-\alpha)^m$$

**Solutions:**
- **Bonferroni correction**: use $\alpha/m$ per test — conservative, works poorly when metrics are correlated
- **False Discovery Rate (FDR)**: controls $E[\text{false positives} / \text{rejections}]$ — better for large-scale testing
- **Overall Evaluation Criterion (OEC)**: combine metrics into a single weighted score upfront

---

## Ramp-Up Issues

Effects can change as you scale from 5% to 100% traffic:

| Issue | Cause | Solution |
|---|---|---|
| **Seasonality** | Holidays, school cycles | Holdback group (keep small control even post-launch) |
| **Novelty effect** | Users excited about new thing | Cohort analysis; wait for cohort to stabilize |
| **Change aversion** | Users dislike change initially | Pre- and post-period analysis; measure learning effects |

---

## Related

- [[Statistical-Tests-Cheat-Sheet]] — which test to use when
- [[AB-Testing-Experiment-Design]] — unit of diversion, population, duration
- [[AB Testing]] — procedure overview and interview framework
