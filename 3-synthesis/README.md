---
title: Synthesis — Cross-Domain Analysis
tags: [synthesis]
created: 2026-04-18
---

# synthesis/

This folder stores cross-domain analysis pages and filed query answers. It is **Layer 3** in the knowledge architecture — the compounding layer where exploration becomes permanent insight.

## What belongs here

- **Cross-domain connections** — e.g., how ML evaluation metrics map to investment portfolio metrics
- **Comparison pages** — side-by-side analysis of concepts, tools, or approaches
- **Filed query answers** — when a query answer is non-obvious and took multiple pages to derive, file it here so the insight doesn't disappear into chat history
- **Lint reports** — periodic health-check results (`lint-YYYY-MM-DD.md`)

## What does NOT belong here

- Atomic concept notes → those go in domain folders (`Machine Learning/`, `System Design/`, etc.)
- Source summaries → those go in `sources/`
- Navigation hubs → those go in `00-MOC/`

## File naming

- Cross-domain: `ML-x-Investment.md`, `SystemDesign-x-ML.md`
- Topic synthesis: `Valuation-Models-Comparison.md`
- Filed query answer: `query-YYYY-MM-DD-topic.md`
- Lint report: `lint-YYYY-MM-DD.md`

## Frontmatter template

```yaml
---
title: <Analysis/Comparison Title>
type: comparison | cross-domain | analysis | lint-report
created: YYYY-MM-DD
domains: [ml, investment]
related: [[Note A]], [[Note B]]
---
```

## How synthesis pages are created

1. You ask a cross-domain question during a query session
2. The AI derives an answer that required synthesizing 3+ pages
3. The AI proposes filing the answer here — you approve
4. The page is added to `INDEX.md` under the Synthesis section
5. The creation is logged in `_log.md`: `## [YYYY-MM-DD] query | Topic filed to synthesis/`

The goal: every valuable insight you derive gets compounded into the wiki, not lost in chat history.
