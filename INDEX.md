# 📋 Steven's Vault — Global Index

> Quick navigation hub for the entire knowledge base.  
> For AI agents: see `CLAUDE.md` for full instructions.

---

## 🗺️ Domain Maps (Start Here)

| Domain | MOC | Notes Count |
|--------|-----|-------------|
| 🤖 Machine Learning | [[ML-MOC]] | 11 notes |
| 🏗️ System Design | [[System-Design-MOC]] | 5 notes |
| 🧮 Algorithm | [[Algorithm-MOC]] | 12 LeetCode + 6 patterns |
| 💰 Investment | [[Investment-MOC]] | 5 notes |
| 🎓 OMSCS | [[OMSCS-MOC]] | 14 notes |

---

## 📚 By Source Material

### Books Compiled Into Wiki
- [[Quest for Machine Learning Book Outline]] → compiled into `Machine Learning/` atomic notes
- DDIA → compiled into `System Design/` notes
- [[The Intelligent Investor]] → `Investment/Books Reading/`
- [[Security Analysis]] → `Investment/Books Reading/`
- [[The Little Book That Still Beats the Market]] → `Investment/Books Reading/`

---

## 🔖 By Status

### 🌲 Evergreen (stable reference)
> Use Dataview query below once Dataview plugin is installed:
```dataview
LIST FROM "" WHERE status = "evergreen" SORT file.mtime DESC
```

### 🌿 Growing (in progress)
```dataview
LIST FROM "" WHERE status = "growing" SORT file.mtime DESC
```

---

## 🏷️ Master Tag List

| Tag | Domain |
|-----|--------|
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

---

## 🗃️ Source Layers

### 📦 `_raw/` — New sources (add future PDFs here)
- `_raw/books/` — Book PDFs
- `_raw/papers/` — Research papers
- `_raw/courses/` — Course slides & materials

### 📖 `Books/` — PDF Annotation Layer (legacy, do not move)
> These are Obsidian Annotator files with hardcoded vault paths. Treat as read-only raw source.

| File | Source Book | Compiles Into |
|------|-------------|---------------|
| [[DDIA Notes]] | Designing Data-Intensive Applications | `System Design/` |
| [[Quest for Machine Learning Notes]] | 百面机器学习 | `Machine Learning/` |

**Other PDFs in Books/:** ESLII.pdf, Elements of Programming Interviews in Python.pdf, System Design Interview.pdf, 面试常考算法模板.pdf — reference materials, not yet annotated.

---

*Last updated: 2026-04-14 | [[_log]]*
