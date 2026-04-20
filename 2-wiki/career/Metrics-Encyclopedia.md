---
title: Metrics Encyclopedia
tags: [career, interview, product-sense, metrics, data-science]
created: 2026-04-19
status: evergreen
related: [[Product-Sense-Framework]], [[Business-Frameworks]], [[AB Testing]]
source: Notion Project Seattle — Case Study (Product Sense)
---

# Metrics Encyclopedia

> All metrics you need for "How would you measure...?" interviews. Definition + formula + typical use case per metric.

---

## AARRR Pirate Metrics

| Stage | Goal | Key Metrics |
|---|---|---|
| **Acquisition** | How do users find us? | CPA, CPC, CTR, Impressions, CPM, Traffic sources |
| **Activation** | Do they have a great first experience? | Sign-up rate, Onboarding completion, Time-to-value |
| **Retention** | Do they come back? | DAU/MAU (Stickiness), Retention rate, Churn rate, NPS |
| **Referral** | Do they tell others? | Referral rate, Viral coefficient, NPS |
| **Revenue** | Do we make money? | ARPU, LTV, CAC, LTV/CAC ratio, Conversion rate |

---

## Engagement Metrics

| Metric | Definition | Formula / Note |
|---|---|---|
| **DAU / MAU** | Daily / Monthly Active Users | Count of unique users performing a qualifying action |
| **Stickiness** | How often users return | `DAU / MAU` — higher = stickier product |
| **Sessions** | Number of visits | A session = continuous visit (ends after 30 min inactivity) |
| **Pages / Session** | Content consumption depth | `Total page views / Total sessions` |
| **Avg Session Duration** | Time per visit | `Total duration / Number of sessions` |
| **Bounce Rate** | % left after 1 page | `Single-page sessions / Total sessions` — lower is better |

---

## Revenue & Monetization Metrics

| Metric | Definition | Formula |
|---|---|---|
| **Revenue** | Total income | `Units Sold × Price per Unit` |
| **Profit** | Net earnings | `Revenue − Total Cost` |
| **Gross Margin** | Profit per unit of revenue | `(Revenue − COGS) / Revenue` |
| **ARPU** | Average Revenue Per User | `Total Revenue / Total Users` |
| **LTV** | Lifetime Value | `ARPU × Avg Customer Lifespan` or `ARPU / Churn Rate` |
| **CAC** | Customer Acquisition Cost | `Total Marketing Spend / New Customers Acquired` |
| **LTV / CAC** | Unit economics health | Ideally > 3. Below 1 = losing money per customer |

---

## Conversion & Acquisition Metrics

| Metric | Definition | Formula |
|---|---|---|
| **Conversion Rate** | % who completed desired action | `Conversions / Total Visitors` |
| **CTR** | Click-Through Rate | `Clicks / Impressions` |
| **CPC** | Cost Per Click | `Ad Spend / Clicks` |
| **CPA** | Cost Per Acquisition | `Ad Spend / Conversions` |
| **CPM** | Cost Per 1000 Impressions | `(Ad Spend / Impressions) × 1000` |
| **Drop-off Rate** | % who abandon at a funnel step | `(Entered Step − Completed Step) / Entered Step` |

---

## Retention Metrics

| Metric | Definition | Formula |
|---|---|---|
| **Retention Rate** | % users who return | `Users at End / Users at Start` (cohort-based) |
| **Churn Rate** | % users lost | `1 − Retention Rate` or `Lost Customers / Start Customers` |
| **NPS** | Net Promoter Score | `% Promoters (9–10) − % Detractors (0–6)` — Range: −100 to 100 |

---

## Traffic Source Breakdown

| Source | Description |
|---|---|
| **Direct** | User types URL directly or uses bookmark |
| **Organic Search** | From search engines (non-paid) |
| **Paid Search** | From search engine ads (SEM) |
| **Social** | From social media platforms |
| **Referral** | From other websites linking to you |
| **Email** | From email campaigns |

---

## Profitability Tree

**Profit = Revenue − Cost**
- Revenue = Units Sold × Price
- Cost = Fixed Cost + Variable Cost
  - Fixed: Rent, Salary, Equipment
  - Variable: Materials, Packaging, Delivery

**Example (Pizza Shop):**
- Revenue = Pizzas Sold × Avg Price per Pizza
- Cost = Overhead (rent + staff + utilities) + Variable (dough + toppings + box + delivery)
- Profit = Revenue − Cost

Used in: "Break down the profitability of X" questions.
