---
title: AB Testing
tags: [ml, ab-testing, statistics, model-evaluation]
created: 2026-04-14
status: growing
related: [[Model Evaluation]], [[Classification Metrics]], [[Cross Validation]]
source: Quest for Machine Learning
---

# AB Testing

## Core Idea
Compare two versions (A and B) of a system by randomly splitting users and measuring a target metric. The gold standard for causal inference about system changes.

## Why AB Testing?

### Limitations of Offline Evaluation
- Offline metrics (AUC, RMSE) don't capture all real-world effects
- Offline testing doesn't eliminate overfitting to the historical distribution
- Some metrics (click-through rate, revenue) can only be measured live
- The online engineering environment has latency, edge cases offline eval ignores

### When to Run AB Tests
- Launching a new model to production
- Changing the ranking/recommendation algorithm
- UI/UX changes
- Any change where you want causal evidence, not correlation

## Procedure
1. **Define metric**: what are you trying to improve? (primary + guardrail metrics)
2. **Calculate sample size**: based on desired statistical power and effect size
3. **Randomize**: split users randomly into control (A) and treatment (B)
4. **Run**: collect data for a predetermined period
5. **Analyze**: hypothesis test (t-test, chi-squared) to check if difference is significant
6. **Decide**: ship, iterate, or rollback

## Key Concepts
- **Statistical significance** (p-value < 0.05): the difference is unlikely due to random chance
- **Statistical power** (1 - β): probability of detecting a real effect
- **Minimum Detectable Effect (MDE)**: smallest effect you care about
- **Novelty effect**: users behave differently just because something is new — run tests long enough

## Common Pitfalls
- Peeking (stopping early when results look good → inflated false positive rate)
- Multiple testing (running many simultaneous tests → use Bonferroni correction)
- Network effects (treatment group affects control group)

## Related
- [[Model Evaluation]] — AB testing is the online evaluation layer
- [[Cross Validation]] — offline evaluation counterpart
