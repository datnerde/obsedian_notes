---
title: Product Sense Framework
tags: [career, interview, product-sense, case-study]
created: 2026-04-19
status: evergreen
related: [[Metrics-Encyclopedia]], [[Business-Frameworks]], [[AB Testing]], [[Behavioural-Interview-STAR]]
source: Notion Project Seattle — Case Study (Product Sense)
---

# Product Sense Framework

> Universal 6-step framework for DS/PM product sense interviews. Three ready-to-use templates for the most common question types.

---

## Universal 6-Step Framework

| Step | Action | Key Questions |
|---|---|---|
| **1. Clarify Objective** | Confirm business goal | What is the business trying to achieve? Revenue? Engagement? Retention? |
| **2. Align Metrics** | Tie topic/metric to goal | How does this metric tie to the goal? What's the definition? |
| **3. Segment** | Break into smaller dimensions | External vs Internal vs Tech vs Demographic? Which user segment? |
| **4. Hypothesize** | Propose root cause | What's the most likely cause? What data supports this? |
| **5. Validate** | Test via A/B or data | How would we test this? What's the control/treatment? Duration? |
| **6. Recommend** | Give actionable advice | Short-term fix vs long-term solution? Trade-offs? |

---

## Template 1: Diagnose Metric Change

**Trigger:** *"X metric dropped/increased by Y%. What would you do?"*

### Step 1: Clarify the Metric
- What is the metric? How is it defined and calculated?
- Is this expected? One-time event or progressive trend?
- What's the absolute value of the change?
- Break down to funnel steps — is the drop isolated to one stage?

### Step 2: Narrow Down the Problem

| Dimension | Check Items |
|---|---|
| **External** | Competitors, holiday/seasonality, channel changes |
| **Internal** | Data pipeline bugs, new features/campaigns/experiments, segment shifts (engagement, churn, drop-off, avg session duration) |
| **Tech** | Platform-specific (iOS/Android/Web), device type, specific page/feature |
| **Demographic** | Region, market competition, customer segmentation, shopping behavior, regional policy |

### Step 3: Decompose the Metric
- Break into components: e.g. `Revenue = DAU × Conversion Rate × AOV`
- Identify which component drives the change
- Check related metrics for cascade effects

### Step 4: Summarize
- What's the issue? Where did it happen?
- Can we fix it?
- Short-term or long-term impact on goal-related metrics?

---

## Template 2: Measure Success

**Trigger:** *"How would you measure the success of X?"*

### Variant A: Measure a Business
1. **Define success** — What is the business goal?
2. **Map the customer journey** — Awareness → Acquisition → Conversion → Engagement → Retention → Monetization
3. **List metrics per stage** → Select most relevant
4. **Summarize** the final metric set with rationale

### Variant B: Measure a Product/Feature
1. **Describe the product** — What does it do? What's the business goal?
2. **Pick feature(s)** — Goal and what it does
3. **Describe user journey** — How does a user interact?
4. **Define metrics**
   - **Primary metrics**: Adoption rate, usage frequency
   - **Guardrail metrics**: Spam rate, error rate, churn
   - **North Star metric**: DAU, LTV, Revenue
5. **Implementation plan** — How to collect and track?
6. **Wrap up** — Prioritize metrics, acknowledge trade-offs

**Avoid vanity metrics:** Downloads, page views — look good but don't drive action. Good metrics are tied to mission, motivate correct behavior, and can't be bot-inflated.

---

## Template 3: Launch or Not

**Trigger:** *"Should we launch X? How would you decide?"*

### Step 1: Define Goal & Metrics
- **Objective:** What's the change trying to achieve?
- **Success metrics:** 1–2 directly tied to the objective
- **Guardrail metrics:** Ensure no negative side effects

### Step 2: Design the Experiment
- **Methodology:** Randomized A/B test
- **Groups:** Control (current) vs Treatment (new)
- **Duration:** Minimum 2 weeks to capture day-of-week effects
- **Hypothesis:** Treatment shows significant lift without hurting guardrails

### Step 3: Analyze & Recommend

| Scenario | Result | Recommendation |
|---|---|---|
| **Perfect** | Success metrics ↑, guardrails unchanged | Launch to all users |
| **Conflicting** | Success ↑ but guardrail ↓ | Deep dive — does revenue gain outweigh churn? Check long-term retention |
| **No difference** | No significant lift | Don't launch — cost not justified |
