---
title: Sources — Per-Source Summary Pages
tags: [source-summary]
created: 2026-04-18
---

# sources/

This folder stores one summary page per ingested source (book, paper, course, article). It is **Layer 1a** in the knowledge architecture — the bridge between immutable raw materials and the compiled wiki.

## Purpose

Each source page answers: "What did we extract from this source, and where did it go in the wiki?"

This makes it easy to:
- Trace any wiki claim back to its source
- Know at a glance what a book contributed to the knowledge base
- Avoid re-ingesting the same material twice
- See which wiki pages were updated when a source was processed

## Frontmatter template

```yaml
---
title: <Source Title>
type: book | paper | course | article
date_ingested: YYYY-MM-DD
key_claims:
  - Core claim or insight 1
  - Core claim or insight 2
  - Core claim or insight 3
pages_affected: [[Page A]], [[Page B]], [[Page C]]
---
```

## File naming

- Books: `Designing-Data-Intensive-Applications.md`
- Papers: `Attention-Is-All-You-Need-2017.md`
- Articles: `article-YYYY-MM-DD-title.md`
- Courses: `OMSCS-GOIS-2026.md`

## When to create a source page

During **INGEST** — step 2 of the ingest workflow (see `CLAUDE.md`). Create the page immediately after reading the source and before updating domain pages.

## Existing sources to document

The following sources have already been compiled into the wiki but don't yet have source pages. Create these during future ingest/maintenance sessions:

- [ ] 百面机器学习 (Quest for Machine Learning) → `sources/Quest-for-Machine-Learning.md`
- [ ] Designing Data-Intensive Applications (DDIA) → `sources/Designing-Data-Intensive-Applications.md`
- [ ] The Intelligent Investor → `sources/The-Intelligent-Investor.md`
- [ ] Security Analysis (Graham & Dodd) → `sources/Security-Analysis.md`
- [ ] The Little Book That Still Beats the Market → `sources/The-Little-Book-That-Beats-the-Market.md`
