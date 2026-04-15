# Steven's Knowledge Vault — AI Agent Instructions

> This file tells any AI agent (Claude, GPT, etc.) how to navigate and maintain this vault.
> Read this first before doing anything else.

---

## Owner & Purpose

**Owner**: Steven  
**Purpose**: Personal second brain covering technical learning, career reference, and investment research.

**Domains**:
- `Machine Learning/` — ML concepts, feature engineering, model evaluation, optimization
- `System Design/` — Distributed systems (DDIA-based), scalability, storage
- `Algorithm/` — Data structures, algorithm patterns, LeetCode solutions
- `OMSCS/` — Georgia Tech graduate coursework (currently: GOIS - Operating Systems)
- `Investment/` — Value investing, valuation models, quant/algo trading

---

## Folder Structure

```
vault/
├── CLAUDE.md              ← YOU ARE HERE — read first
├── INDEX.md               ← Global table of contents
├── _log.md                ← Append-only operation log
├── _raw/                  ← Immutable source materials (PDFs, articles)
│   ├── books/
│   ├── papers/
│   └── courses/
├── 00-MOC/                ← Maps of Content (domain navigation hubs)
│   ├── Algorithm-MOC.md
│   ├── ML-MOC.md
│   ├── System-Design-MOC.md
│   ├── Investment-MOC.md
│   └── OMSCS-MOC.md
├── Algorithm/
│   ├── Patterns/          ← Conceptual patterns (Two Pointer, etc.)
│   └── Problems/          ← LeetCode solutions (one file per problem)
├── Machine Learning/
├── System Design/
├── OMSCS/
├── Investment/
└── Template/
```

---

## Note Conventions

### Frontmatter (required on every note)
```yaml
---
title: <concise concept name>
tags: [<domain>, <subtopic>, ...]
created: YYYY-MM-DD
status: seedling | growing | evergreen
related: [[Note A]], [[Note B]]
source: <book/course/article title>
---
```

**Status meanings**:
- `seedling` 🌱 — raw capture, incomplete
- `growing` 🌿 — fleshed out, still evolving
- `evergreen` 🌲 — stable, well-connected, reliable reference

### Language
- Technical concepts: English
- Personal commentary or bilingual notes: Chinese is fine

### Wikilinks
- Always use `[[wikilinks]]` to connect related concepts
- Every note should link to at least 2 other notes
- Update the relevant MOC file when adding a new note

### Atomic Notes
- One concept per file (especially in Machine Learning/)
- LeetCode: one problem per file (already done ✅)
- Large chapter notes should be broken into smaller atomic pieces over time

---

## How to Add New Knowledge

1. Drop raw sources (PDFs, articles) into `_raw/<category>/`
2. Compile key concepts into atomic notes in the relevant domain folder
3. Add proper frontmatter (title, tags, status, related, source)
4. Link to related notes with `[[wikilinks]]`
5. Update the domain's `00-MOC/*.md` file
6. Append a one-line entry to `_log.md` describing what was added

---

## How to Answer Questions

When Steven asks a question:
1. Check `INDEX.md` for an overview
2. Check the relevant `00-MOC/*.md` for domain navigation
3. Read specific notes in the domain folder
4. Synthesize across notes — don't just quote one file

---

## How to Maintain This Vault

When adding or editing notes:
- Preserve existing wikilinks — don't break them
- If renaming a file, search for all references first
- `_raw/` is immutable — never edit files there
- Always append to `_log.md`, never edit past entries

---

## Key Relationships to Know

- `Books/Quest for Machine Learning Notes.md` → expands into `Machine Learning/` notes
- `Books/DDIA Notes.md` → expands into `System Design/` notes
- `Algorithm/Patterns/` → referenced by all `Algorithm/Problems/` notes
- `Investment/Valuation/` → connects to `Investment/Books Reading/`

---

*Last updated: 2026-04-14*
