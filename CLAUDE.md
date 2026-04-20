# Steven's Knowledge Vault

**Domains**: `2-wiki/ml/` · `2-wiki/system-design/` · `2-wiki/algorithm/` · `2-wiki/omscs/` · `2-wiki/investment/` · `2-wiki/ai-systems/` · `2-wiki/career/`

**Layers**: `0-raw/` (immutable) → `1-sources/` → `2-wiki/_nav/` + `2-wiki/<domain>/` → `3-synthesis/`

---

## Triggers → Operations

| Trigger | Operation |
| --- | --- |
| 整理笔记 / 同步笔记 / sync / organize | DELTA-SYNC |
| knowledge question (问/解释/比较/什么是) | QUERY → auto-file |
| 检查 / lint / health check | LINT |

---

## Operations

### DELTA-SYNC

1. Check `[VAULT DELTA]` context injected by hook — or read `_log.md` for last INGEST/DELTA-SYNC date
2. Detect new files: `git log --since="YYYY-MM-DD" --name-only --pretty=format: --diff-filter=A -- 0-raw/ 1-sources/`
   Fallback: `find 0-raw/ 1-sources/ -newer _log.md -name "*.md"`
3. Report list of new files; for each, run the INGEST workflow below
4. Append: `## [YYYY-MM-DD] | DELTA-SYNC | N files processed`

If no new files: "Vault up to date since YYYY-MM-DD." and stop.

### INGEST

1. Read & discuss source with Steven
2. Write `1-sources/<Title>.md` (source frontmatter below)
3. Update touched `2-wiki/<domain>/` pages — typically 5–15 per source
4. Update `2-wiki/_nav/<Domain>-MOC.md`
5. Update `INDEX.md`
6. Append: `## [YYYY-MM-DD] | INGEST | Source Title`

> Integrate, don't just summarize. Revise existing pages. Flag contradictions on both pages.

### QUERY

1. Identify domain → go to its MOC. Cross-domain: read `INDEX.md` first.
2. Read relevant `2-wiki/` notes
3. Synthesize across notes
4. **Auto-file**: if ≥2 pages read OR answer involves comparison/analysis/cross-domain → write `3-synthesis/query-YYYY-MM-DD-topic.md` (no need to ask). Update INDEX.md Synthesis table. Mention filename at end of response.
5. Append: `## [YYYY-MM-DD] | QUERY | summary`

**Domain → MOC**: ml→`ML-MOC.md` · system-design→`System-Design-MOC.md` · algorithm→`Algorithm-MOC.md` · investment→`Investment-MOC.md` · omscs→`OMSCS-MOC.md` · ai-systems→`AI-Systems-MOC.md` · career→`Career-MOC.md`

### LINT (monthly / every ~20 ingests)

1. Orphan pages — no inbound `[[links]]`
2. Notes missing required frontmatter fields
3. MOC gaps — notes not listed in their domain MOC
4. Stale seedlings — status unchanged after 30+ days
5. Write `3-synthesis/lint-YYYY-MM-DD.md`
6. Append: `## [YYYY-MM-DD] | LINT | N issues`

---

## Note Frontmatter

**Wiki note** (`2-wiki/`):

```yaml
---
title: concept name
tags: [domain, subtopic]
created: YYYY-MM-DD
status: seedling | growing | evergreen
related: [[Note A]], [[Note B]]
source: book/course title
---
```

**Source summary** (`1-sources/`):

```yaml
---
title: Source Title
type: book | paper | course | article
date_ingested: YYYY-MM-DD
key_claims: [claim 1, claim 2]
pages_affected: [[Page A]], [[Page B]]
---
```

**Synthesis** (`3-synthesis/`):

```yaml
---
title: Analysis Title
type: comparison | cross-domain | analysis | lint-report
created: YYYY-MM-DD
domains: [ml, investment]
related: [[Note A]], [[Note B]]
---
```

Status: `seedling` = raw · `growing` = evolving · `evergreen` = stable reference

---

## Invariants

- `0-raw/` is immutable — never write (enforced by PreToolUse hook)
- `_log.md` is append-only — never edit past entries
- MOC files are the navigation source of truth — keep current
- Update `INDEX.md` on every new page
- Min 2 `[[wikilinks]]` per note; atomic = one concept per file
