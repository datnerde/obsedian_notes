# Steven's Knowledge Vault — AI Agent Instructions

> This file tells any AI agent (Claude, GPT, etc.) how to navigate and maintain this vault.
> **Read this entire file before doing anything else.**

---

## Owner & Purpose

**Owner**: Steven
**Purpose**: Personal second brain — long-term technical knowledge accumulation, cross-domain synthesis research, and investment analysis.

**Domains**:

- `2-wiki/ml/` — ML concepts, feature engineering, model evaluation, optimization
- `2-wiki/system-design/` — Distributed systems (DDIA-based), scalability, storage
- `2-wiki/algorithm/` — Data structures, algorithm patterns, LeetCode solutions
- `2-wiki/omscs/` — Georgia Tech graduate coursework (currently: GOIS - Operating Systems)
- `2-wiki/investment/` — Value investing, valuation models, quant/algo trading

---

## Folder Structure

```txt
vault/
├── CLAUDE.md          ← YOU ARE HERE — read first
├── INDEX.md           ← Global table of contents (update on every ingest)
├── _log.md            ← Append-only operation log
├── _assets/           ← Images and media
├── _templates/        ← Note templates
│
├── 0-raw/             ← LAYER 0: Immutable source material — never edit
│   ├── books/
│   ├── papers/
│   └── courses/
│
├── 1-sources/         ← LAYER 1: Per-source summary pages
│
├── 2-wiki/            ← LAYER 2: Compiled atomic wiki notes
│   ├── _nav/          ← Navigation MOCs (Maps of Content)
│   │   ├── ML-MOC.md
│   │   ├── System-Design-MOC.md
│   │   ├── Algorithm-MOC.md
│   │   ├── Investment-MOC.md
│   │   └── OMSCS-MOC.md
│   ├── ml/
│   ├── system-design/
│   ├── algorithm/
│   │   └── problems/
│   ├── investment/
│   └── omscs/
│
└── 3-synthesis/       ← LAYER 3: Cross-domain analysis, filed query answers
```

---

## Three Core Operations

### INGEST — Processing a New Source

Use when Steven adds a new book, paper, article, or course material.

**Step-by-step flow:**

1. **Read & Discuss** — Read the source, discuss key takeaways with Steven. Ask clarifying questions if needed.
2. **Create source summary page** — Write `1-sources/<SourceTitle>.md` using the source frontmatter format (see Note Conventions). Capture: core claims, date ingested, pages affected.
3. **Update entity/concept pages** — Find all existing wiki pages touched by this source. Update, add sections, or note contradictions. A single source typically touches 5–15 pages.
4. **Update the domain MOC** — Add entries to the relevant `2-wiki/_nav/<Domain>-MOC.md`.
5. **Update INDEX.md** — Add new pages to the index table with type, status, and date.
6. **Append to `_log.md`** — Use the format: `## [YYYY-MM-DD] ingest | Source Title`

**Principles:**

- One source might update many pages — this compounding effect is the point
- Flag contradictions explicitly: if a new source contradicts an existing claim, note it on both pages
- Don't just summarize — integrate: revise existing pages rather than creating isolated summaries

---

### QUERY — Answering Questions

Use when Steven asks a question against the knowledge base.

**Step-by-step flow:**

1. **Read INDEX.md first** — Find relevant pages across all domains. Don't rely on memory.
2. **Read relevant pages** — Follow links from the index and MOCs.
3. **Synthesize** — Combine information across domains. Never quote a single file if the answer spans concepts.
4. **File valuable answers** — If the answer is a comparison, analysis, cross-domain connection, or durable insight, **proactively propose filing it** as a new page in `3-synthesis/`. Good answers compound just like ingested sources.
5. **Append to `_log.md`** — Use format: `## [YYYY-MM-DD] query | Question Summary`

**When to file an answer into `3-synthesis/`:**

- Cross-domain connections (ML ↔ Investment, System Design ↔ ML)
- Comparison tables across concepts or tools
- Non-obvious insights that took multiple pages to derive
- Analysis Steven might want to build on later

---

### LINT — Health Check (Run every ~20 ingests or monthly)

Use to keep the wiki healthy as it grows.

**Step-by-step flow:**

1. **Scan for contradictions** — Pages that make conflicting claims about the same topic
2. **Find orphan pages** — Pages with no inbound wikilinks (use backlinks or grep)
3. **Identify concept gaps** — Concepts mentioned in pages but lacking their own dedicated page
4. **Check staleness** — Claims on older pages that newer sources have superseded
5. **Find missing cross-references** — Related concepts that aren't yet linked
6. **Generate report** — Write a lint report to `3-synthesis/lint-YYYY-MM-DD.md` with findings and suggested fixes
7. **Append to `_log.md`** — Use format: `## [YYYY-MM-DD] lint | N issues found`

---

## How to Answer Queries (Navigation Protocol)

When Steven asks any question, follow this exact navigation protocol:

### Step 1 — Identify the domain

Map the question to one of: `ml`, `system-design`, `algorithm`, `investment`, `omscs`, or `cross-domain`

### Step 2 — Check INDEX.md first for cross-domain questions

For cross-domain questions, read `INDEX.md` to get the full picture before diving in.

### Step 3 — Check the domain MOC

Go to `2-wiki/_nav/<Domain>-MOC.md`. This is the authoritative map of what exists and how concepts connect.

| Question type | Go to |
| --- | --- |
| ML / feature engineering / models | `2-wiki/_nav/ML-MOC.md` |
| System design / distributed systems / DDIA | `2-wiki/_nav/System-Design-MOC.md` |
| LeetCode / algorithms / patterns | `2-wiki/_nav/Algorithm-MOC.md` |
| Investing / valuation / quant | `2-wiki/_nav/Investment-MOC.md` |
| OS / OMSCS coursework | `2-wiki/_nav/OMSCS-MOC.md` |
| Cross-domain or unclear | `INDEX.md` first |

### Step 4 — Read the specific notes

Follow the links from the MOC to the relevant atomic notes.

### Step 5 — Synthesize

Combine information from multiple notes. Draw connections across domains. If the synthesis is valuable, file it to `3-synthesis/`.

### Step 6 — Update if needed

If the answer reveals a gap or outdated note, update the note and log the change in `_log.md`.

---

## Note Conventions

### Frontmatter — Concept/Wiki Notes

```yaml
---
title: <concise concept name>
tags: [<domain>, <subtopic>]
created: YYYY-MM-DD
status: seedling | growing | evergreen
related: [[Note A]], [[Note B]]
source: <book/course/article title>
---
```

### Frontmatter — Source Summary Pages (`1-sources/`)

```yaml
---
title: <Source Title>
type: book | paper | course | article
date_ingested: YYYY-MM-DD
key_claims:
  - Core claim 1
  - Core claim 2
pages_affected: [[Page A]], [[Page B]], [[Page C]]
---
```

### Frontmatter — Synthesis Pages (`3-synthesis/`)

```yaml
---
title: <Analysis/Comparison Title>
type: comparison | cross-domain | analysis | lint-report
created: YYYY-MM-DD
domains: [ml, investment]
related: [[Note A]], [[Note B]]
---
```

**Status meanings:**

- `seedling` — raw capture, incomplete
- `growing` — fleshed out, still evolving
- `evergreen` — stable, well-connected, reliable reference

### Language

- Technical concepts: English
- Personal commentary or bilingual notes: Chinese is fine

### Wikilinks

- Always use `[[wikilinks]]` to connect related concepts
- Every note should link to at least 2 other notes
- Update the relevant MOC file when adding a new note

### Atomic Notes

- One concept per file (especially in `2-wiki/ml/`)
- LeetCode: one problem per file
- Large chapter notes should be broken into smaller atomic pieces over time

---

## How to Maintain This Vault

When adding or editing notes:

- Preserve existing wikilinks — don't break them
- If renaming a file, search for all references first
- `0-raw/` is immutable — never edit or move files there
- Always append to `_log.md`, never edit past entries
- Keep MOC files in `2-wiki/_nav/` up to date — they are the source of truth for navigation
- Update INDEX.md whenever a new page is created

---

## Knowledge Layer Map

```txt
0-raw/              ← Layer 0: Immutable source material
      ↓ ingest
1-sources/          ← Layer 1: Per-source summary pages
2-wiki/_nav/        ← Layer 2a: Navigation (MOCs)
2-wiki/<domain>/    ← Layer 2b: Compiled atomic wiki notes
      ↓ query + synthesis
3-synthesis/        ← Layer 3: Cross-domain analysis, filed answers (compounding)
```

The goal is compounding knowledge: each new source and each good query answer enriches the whole wiki, not just isolated pages.

---

## Key Relationships

| Source | Compiles Into |
| --- | --- |
| `2-wiki/algorithm/problems/` | referenced by algorithm pattern notes |
| `2-wiki/investment/` | valuation + books reading cross-link |
| `2-wiki/omscs/` | cross-links to `2-wiki/system-design/` |
| `1-sources/` pages | link to domain notes + listed in INDEX.md |
| `3-synthesis/` pages | link across multiple domains |

---

Last updated: 2026-04-18
