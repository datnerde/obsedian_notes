---
title: Product Sense — Real Interview Cases
tags: [career, interview, product-sense, case-study]
created: 2026-04-19
status: evergreen
related: [[Product-Sense-Framework]], [[Metrics-Encyclopedia]], [[Business-Frameworks]]
source: Notion Project Seattle — Case Study (Product Sense)
---

# Product Sense — Real Interview Cases

> 12 real DS interview questions across 5 types. Use [[Product-Sense-Framework]] for the approach template.

---

## Type 1: Diagnose Metric Change

**Q: Facebook likes decreased 3% YoY. What happened?**
1. **Clarify:** Total likes on all content? Posts, pages, comments? Relative vs absolute?
2. **External:** Competitors (TikTok, Instagram Reels), Seasonality
3. **Internal:** Algorithm changes (News Feed ranking), UI changes (like button placement)
4. **Tech:** Platform breakdown (iOS/Android/Web), Country-level differences
5. **Decompose:** `Likes = DAU × Avg Content Seen × Like Rate` — which component dropped?
6. **Top Hypothesis:** Introduction of Reactions (❤️😂😮) cannibalized simple likes — check if total reactions (likes + emoji) are flat or growing

---

**Q: IE picture uploads suddenly dropped to 0. Why?**
1. **Time:** Sudden drop = likely a bug, not gradual behavioral change
2. **Tech (most likely):** Code deployment broke upload function? Server error? API change?
3. **Internal:** Was the upload feature removed or changed?
4. **External:** IE browser update? OS compatibility issue?
5. **Top Hypothesis:** Code deployment bug — roll back and verify

---

**Q: Retail website sales dropped 10% WoW. Investigate.**
- **Decompose:** `Sales = Traffic × Conversion Rate × AOV`
- Traffic down? Check by source: Organic, Paid, Direct, Social, Email
- Conversion down? Check by funnel step: Landing → Product Page → Cart → Checkout → Purchase
- AOV down? Check product mix changes, promo effects
- **Segment:** New vs returning, Mobile vs Desktop, Geography
- **External:** Competitor sale? Holiday effect? Seasonality?

---

## Type 2: Measure Success

**Q: How would you measure success for a customer service team?**
- **Goal:** Resolve customer issues quickly and satisfactorily
- **Efficiency:** Avg response time, Avg resolution time, First-contact resolution rate
- **Quality:** CSAT (Customer Satisfaction Score), NPS post-interaction
- **Volume:** Tickets resolved per agent, Backlog size
- **Guardrail:** Repeat contact rate (same issue), Escalation rate
- **North Star:** Customer retention rate after service interaction

---

**Q: How would you measure success for a messaging feature on a social app?**
- **User Journey:** Discover → Send first message → Receive reply → Ongoing conversation
- **Adoption:** % of DAU who send ≥1 message, Time to first message
- **Engagement:** Messages per user per day, Avg conversation length
- **Retention:** Day 7/30 messaging retention, % returning to message again
- **Guardrail:** Spam/abuse reports, Block rate, Impact on feed engagement
- **North Star:** DAU lift attributable to messaging

---

## Type 3: Product Strategy / Improvement

**Q: How would you improve Facebook engagement?**
1. Clarify: Engagement = likes + comments + shares? Which metric?
2. Segment: Creators vs Consumers vs Lurkers — engagement means different things
3. Pain Points: Content quality declining; Algorithm too aggressive (missing friends' posts); TikTok/Reels competition
4. Solutions: Improve content ranking; Add lightweight engagement options; Close-friends notifications
5. **Prioritize:** Impact × Feasibility → Start with algorithm tuning (high impact, low cost)

---

**Q: Should Amazon open a new fulfillment center?**
- **Revenue side:** Expected order volume in region; Delivery speed → higher conversion; Prime membership growth
- **Cost side:** Fixed (land, building, equipment, staff); Variable (picking, packing, shipping, returns)
- **Strategic:** Market competition (Walmart), Customer density, Long-term growth potential
- **Decision:** If incremental revenue > total cost over 3–5 year payback AND strategic fit → Open

---

## Type 4: Diagnostic / Analytical

**Q: How would you detect clickbait on a social platform?**
1. **Define:** Content with misleading titles designed to get clicks but disappoints users
2. **Signals — Behavioral:** High CTR + Low time-on-page + High bounce rate = clickbait signature
3. **Signals — Text:** Sensational words, ALL CAPS, "You won't believe...", excessive punctuation
4. **Signals — User feedback:** Reports, downvotes, hides
5. **Approach:** Rule-based (text patterns) + ML (behavioral signals) + user feedback loop
6. **Metrics:** Precision (don't wrongly flag good content) + Recall (catch most clickbait)

---

**Q: Instagram iOS users engage more than Android. Why?**
1. **User Demographics:** iOS users tend to have higher income → more invested in social media presence
2. **App Quality:** Instagram historically iOS-first development
3. **Device Quality:** Better iPhone cameras → better content → more sharing & engagement
4. **Network Effects:** More mutual connections among iOS users
5. **Confounders:** Geographic distribution (iOS dominant in US/UK where engagement is higher)
6. **Validate:** Control for demographics and geography — does difference persist?

---

## Type 5: Business / Profitability

**Q: Return rate for jeans is 50%. Is this a problem? What would you do?**
1. **Quantify:** Cost per return = shipping + restocking + potential damage
2. **Benchmark:** Apparel avg return rate is 20–30% → 50% is abnormally high
3. **Root Causes:** Sizing inconsistency (customers order multiple sizes); Fit expectation mismatch; Color/material differs from photo
4. **Solutions:** ML-based size recommendation; Virtual try-on; Detailed size charts with body measurements; Reviews with body stats
5. **Measure:** Track return rate by reason code after each intervention

---

**Q: Credit card ad profits $3 per approved application. CPM is $6. Conversion rate 0.1%. Is this profitable?**
- CPM = $6 → Cost per 1,000 impressions
- Conversion rate = 0.1% → 1 conversion per 1,000 impressions
- Cost per conversion = $6
- Revenue per conversion = $3
- **Profit per conversion = $3 − $6 = −$3** → Not profitable
- **To break even:** Need conversion rate > 0.2%, or CPM < $3, or revenue per approval > $6
