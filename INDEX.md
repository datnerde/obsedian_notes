# Steven's Vault — Global Index

> Quick navigation hub for the entire knowledge base.
> For AI agents: see `CLAUDE.md` for full instructions.
> **AI agents: read this file first when answering queries to find relevant pages.**

---

## Domain Maps (Start Here)

| Domain | MOC | Notes Count |
| --- | --- | --- |
| Machine Learning | [[ML-MOC]] | 38 notes |
| System Design | [[System-Design-MOC]] | 5 notes |
| Algorithm | [[Algorithm-MOC]] | 18 notes |
| Investment | [[Investment-MOC]] | 9 notes |
| OMSCS | [[OMSCS-MOC]] | 21 notes |
| AI Systems | [[AI-Systems-MOC]] | 1 note |
| Career | [[Career-MOC]] | 9 notes |

MOCs are in `2-wiki/_nav/`.

---

## Sources (`1-sources/`)

Per-source summary pages — one per book, paper, course, or article ingested.

| Source | Type | Date Ingested | Status |
| --- | --- | --- | --- |
| [[article-2015-03-10-Data-Mining-Problems-in-Retail\|Data Mining Problems in Retail (Katsov)]] | article | 2026-04-19 | ingested |

---

## Synthesis (`3-synthesis/`)

Cross-domain analysis pages and filed query answers.

| Page | Domains | Type | Created |
| --- | --- | --- | --- |
| *(add entries here as synthesis pages are created)* | — | — | — |

---

## By Source Material

| Book | Compiled Into | Source Page |
| --- | --- | --- |
| 百面机器学习 (Quest for ML) | `2-wiki/ml/` atomic notes | *(create 1-sources/ page)* |
| Designing Data-Intensive Apps (DDIA) | `2-wiki/system-design/` notes | *(create 1-sources/ page)* |
| The Intelligent Investor | `2-wiki/investment/` | *(create 1-sources/ page)* |
| Security Analysis | `2-wiki/investment/` | *(create 1-sources/ page)* |
| The Little Book That Still Beats the Market | `2-wiki/investment/` | *(create 1-sources/ page)* |

---

## By Status

### Evergreen (stable reference)

```dataview
LIST FROM "" WHERE status = "evergreen" SORT file.mtime DESC
```

### Growing (in progress)

```dataview
LIST FROM "" WHERE status = "growing" SORT file.mtime DESC
```

### Seedling (raw capture)

```dataview
LIST FROM "" WHERE status = "seedling" SORT file.mtime DESC
```

---

## Master Tag List

| Tag | Domain |
| --- | --- |
| `ml` | Machine Learning |
| `feature-engineering` | ML subfield |
| `model-evaluation` | ML subfield |
| `optimization` | ML / Math |
| `system-design` | System Design |
| `distributed-systems` | System Design |
| `algorithm` | Algorithm |
| `two-pointer` | Algorithm pattern |
| `leetcode` | LeetCode problems |
| `investment` | Investment |
| `valuation` | Investment subfield |
| `quant` | Algo trading |
| `os` | Operating Systems |
| `omscs` | OMSCS coursework |
| `ai-systems` | AI Systems |
| `llm` | LLM fundamentals |
| `ai-agent` | AI agent architecture |
| `ab-testing-llm` | LLM evaluation & experimentation |
| `synthesis` | Cross-domain analysis |
| `source-summary` | Per-source summary pages |
| `career` | Career growth / soft skills |
| `interview` | Interview preparation |
| `behavioural` | Behavioural interview |

---

Last updated: 2026-04-19 (Notion migration — full sweep) | [[_log]]
