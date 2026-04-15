---
title: Equity Risk Premium
tags: [investment, valuation, dcf]
created: 2026-04-14
status: growing
related: [[Risk Free Rate]], [[Investment-MOC]]
source: Damodaran Valuation
---

# Equity Risk Premium (ERP)

## Core Idea
The Equity Risk Premium is the **extra return investors demand for holding equities over a risk-free asset**. It is the most critical input in any DCF model — small changes in ERP produce large swings in valuation.

`Expected Return on Equity = Risk-Free Rate + ERP × Beta`

## Why It Matters
- ERP feeds into the cost of equity (CAPM)
- Cost of equity → WACC → DCF discount rate
- A 1% change in ERP can move valuations by 15–25% on a typical stock

## How to Estimate ERP

### 1. Historical Premium (Backward-looking)
- Measure the historical excess return of stocks over bonds over a long period
- Ibbotson data (US): ~5–6% arithmetic, ~4% geometric over 90+ years
- **Problem**: backward-looking; assumes the past is representative of the future

### 2. Implied ERP (Forward-looking) — Damodaran's Preferred
- Solve for the ERP implied by **current market prices**
- Set current market cap = PV of expected future cash flows, solve for discount rate, subtract risk-free rate
- Updated monthly by Damodaran at [his website](https://pages.stern.nyu.edu/~adamodar/)
- As of recent years: US implied ERP ≈ 4–5%

### 3. Survey-Based
- Ask CFOs or investment managers what premium they use
- High variance; not reliable

## Country Risk Premium
For non-US markets, add a **Country Risk Premium (CRP)**:
`ERP_country = ERP_US + CRP`

CRP reflects political risk, default risk, currency risk. Damodaran publishes country-level CRP estimates.

## Damodaran's Approach Summary
1. Use the 10-year T-bond rate as [[Risk Free Rate]]
2. Use **implied ERP** from current S&P 500 pricing
3. Adjust for country risk when valuing non-US companies

## Related
- [[Risk Free Rate]] — the baseline that ERP is added to
- [[Investment-MOC]] — fits into the DCF valuation framework
