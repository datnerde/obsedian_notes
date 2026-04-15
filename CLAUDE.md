# Steven's Knowledge Vault — AI Agent Instructions

> This file tells any AI agent (Claude, GPT, etc.) how to navigate and maintain this vault.
> **Read this entire file before doing anything else.**

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
│
├── _raw/                  ← Immutable source materials (PDFs, raw files)
│   ├── books/
│   ├── papers/
│   └── courses/
│
│
├── 00-MOC/                ← Maps of Content (domain navigation hubs)
│   ├── Algorithm-MOC.md
│   ├── ML-MOC.md
│   ├── System-Design-MOC.md
│   ├── Investment-MOC.md
│   └── OMSCS-MOC.md
│
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

## ⭐ How to Answer Queries (Read This First)

When Steven asks any question, follow this exact navigation protocol:

### Step 1 — Identify the domain
Map the question to one of: `ml`, `system-design`, `algorithm`, `investment`, `omscs`

### Step 2 — Check the MOC first
Go to `00-MOC/<Domain>-MOC.md`. This is the authoritative map of what exists and how concepts connect. Read it fully before diving into individual notes.

| Question type | Go to |
|---------------|-------|
| ML / feature engineering / models | `00-MOC/ML-MOC.md` |
| System design / distributed systems / DDIA | `00-MOC/System-Design-MOC.md` |
| LeetCode / algorithms / patterns | `00-MOC/Algorithm-MOC.md` |
| Investing / valuation / quant | `00-MOC/Investment-MOC.md` |
| OS / OMSCS coursework | `00-MOC/OMSCS-MOC.md` |
| Cross-domain or unclear | `INDEX.md` first |

### Step 3 — Read the specific notes
Follow the links from the MOC to the relevant atomic notes in the domain folder.

### Step 4 — Synthesize
Combine information from multiple notes. Never quote just one file if the answer spans concepts. Draw connections across domain folders when relevant (e.g., OS concurrency ↔ System Design replication).

### Step 5 — Update if needed
If the answer reveals a gap or outdated note, update the note and log the change in `_log.md`.

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
- LeetCode: one problem per file ✅
- Large chapter notes should be broken into smaller atomic pieces over time

---

## How to Add New Knowledge

1. Drop raw sources (PDFs) into `_raw/<category>/` or `Books/` (if using Annotator)
2. Compile key concepts into atomic notes in the relevant domain folder
3. Add proper frontmatter (title, tags, status, related, source)
4. Link to related notes with `[[wikilinks]]`
5. Update the domain's `00-MOC/*.md` file
6. Append a one-line entry to `_log.md` describing what was added

---

## How to Maintain This Vault

When adding or editing notes:
- Preserve existing wikilinks — don't break them
- If renaming a file, search for all references first
- `_raw/` and `Books/` are immutable — never edit or move files there
- Always append to `_log.md`, never edit past entries
- Keep MOC files up to date — they are the source of truth for navigation

---

## Knowledge Layer Map

```
_raw/ + Books/          ← Layer 0: Immutable source material & PDF annotations
      ↓ "compiled by AI"
00-MOC/                 ← Layer 1: Navigation & structure
Domain folders          ← Layer 2: Compiled, atomic wiki notes
      ↓ "queried by AI"
Steven's answers        ← Layer 3: Synthesis on demand
```

---

## Key Relationships to Know

| Source | Compiles Into |
|--------|--------------|
| `Algorithm/Patterns/*.md` | referenced by `Algorithm/Problems/*.md` |
| `Investment/Valuation/` | connects to `Investment/Books Reading/` |
| OMSCS distributed systems topics | cross-links to `System Design/` |
| `Machine Learning/` hub notes | link to atomic concept notes in same folder |

---

*Last updated: 2026-04-14*
