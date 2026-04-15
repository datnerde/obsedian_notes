# 📝 Operation Log

> Append-only log of all vault operations. Never edit past entries.  
> Format: `YYYY-MM-DD | action | details`

---

## 2026-04-14 | INIT | Vault restructured to Karpathy LLM Wiki pattern

**Created (new files):**
- `CLAUDE.md` — AI agent instruction schema
- `INDEX.md` — Global table of contents
- `00-MOC/Algorithm-MOC.md` — Algorithm navigation hub
- `00-MOC/ML-MOC.md` — Machine Learning navigation hub
- `00-MOC/System-Design-MOC.md` — System Design navigation hub
- `00-MOC/Investment-MOC.md` — Investment navigation hub
- `00-MOC/OMSCS-MOC.md` — OMSCS navigation hub
- `Template/concept-note.md` — Concept note template
- `Template/leetcode.md` — LeetCode problem template
- `Template/book-chapter.md` — Book chapter template
- `_raw/` directory structure (books/, papers/, courses/)
- `_log.md` — this file

**Modified (frontmatter added):**
- 64 existing notes across Machine Learning/, System Design/, Algorithm/, Investment/, OMSCS/, Books/ — added YAML frontmatter (title, tags, created, status, related, source)

**Renamed:**
- `Algorithm/Leetcode/` → `Algorithm/Problems/`

**Architecture:** Based on [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
