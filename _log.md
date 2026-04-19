# 📝 Operation Log

> Append-only log of all vault operations. Never edit past entries.
>
> **Format (new, from 2026-04-18):** `## [YYYY-MM-DD] operation | Title`
> Supports: `grep "^## \[" _log.md | tail -10` to show recent entries.
>
> Legacy format (pre-2026-04-18): `YYYY-MM-DD | action | details` — kept as-is below.

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

---

## 2026-04-14 | UPDATE | Integrated Books/ layer + strengthened CLAUDE.md query protocol

**Problem solved:** `Books/` folder was orphaned from the framework. `CLAUDE.md` lacked explicit query navigation instructions.

**Root cause:** `Books/DDIA Notes.md` and `Books/Quest for Machine Learning Notes.md` are Obsidian Annotator files with hardcoded `vault:/Books/...` paths embedded in JSON — cannot be moved without breaking all highlights.

**Changes made:**
- `CLAUDE.md` — Added `⭐ How to Answer Queries` section with 5-step MOC-first protocol and domain routing table; added `Books/` explanation with ⚠️ do-not-move warning; added Knowledge Layer Map
- `INDEX.md` — Added Books/ as "PDF Annotation Layer" with source→compiled mapping table
- `00-MOC/ML-MOC.md` — Added Source Layer section linking to `Books/Quest for Machine Learning Notes.md`
- `00-MOC/System-Design-MOC.md` — Added Source Layer section linking to `Books/DDIA Notes.md`
- `00-MOC/Algorithm-MOC.md` — Added reference to Books/ PDFs (cheat sheets, interview prep)
- `00-MOC/Investment-MOC.md` — Added reference to Books/ PDFs (Security Analysis, data science sheet)

**Decision:** Books/ stays in place permanently. It is now formally designated as the "raw annotation layer" in the vault architecture.

---

## 2026-04-14 | REFACTOR | Full LLM wiki atomic note restructure

**Philosophy applied:** Karpathy LLM wiki — one concept per file, Core Idea first, rich wikilinks, compiled not raw.

**New atomic notes created (18):**
- `ML/Feature Normalization.md` — Min-Max, Z-Score, gradient descent connection
- `ML/Categorical Encoding.md` — ordinal, one-hot, binary
- `ML/Text Representation.md` — Bag of Words, TF-IDF, topic models
- `ML/Word2Vec.md` — CBOW, Skip-gram
- `ML/Classification Metrics.md` — confusion matrix, Precision, Recall, F1
- `ML/ROC and AUC.md` — threshold-invariant evaluation
- `ML/Cross Validation.md` — K-fold, LOO, Bootstrap
- `ML/Overfitting and Underfitting.md` — bias-variance, regularization
- `ML/Hyperparameter Tuning.md` — grid, random, Bayesian optimization
- `ML/K-Means Clustering.md` — EM algorithm, K++, ISODATA
- `ML/Gaussian Mixture Model.md` — soft assignment, EM
- `ML/PCA.md` — eigendecomposition, kernel PCA
- `ML/LDA (Linear Discriminant Analysis).md` — supervised dim reduction
- `ML/MCMC.md` — Metropolis-Hastings, Gibbs Sampling
- `ML/Imbalanced Data.md` — SMOTE, over/under-sampling

**Hub notes rewritten (5):** Feature Engineering, Model Evaluation, Unsupervised Learning, Dimensional Reduction, Sampling

**Empty notes filled (3):** Optimization (gradient descent, Adam, RMSProp), AB Testing (procedure, pitfalls), Probability Graphical Model (Bayesian Networks, MRF)

**System Design filled (1):** Replication (leader/follower, multi-leader, leaderless, replication lag)

**Cross-links added (3):** Storage and Retrieval, Data Models and Query Languages, Classic Model

**MOC updated:** `00-MOC/ML-MOC.md` — full atomic structure with concept graph

---

## 2026-04-14 | CLEANUP | Full vault audit + remaining issues resolved

**Findings from full audit (all ~90 notes reviewed):**
- Algorithm: ✅ good (1 stub fixed)
- Machine Learning: ✅ good (1 messy file split)
- System Design: ✅ good
- OMSCS: ✅ good, added cross-domain links
- Investment: ⚠️ 2 issues fixed

**Changes made:**

**ML — Classic Model split into 3 atomic notes:**
- Created `ML/SVM.md` — hard/soft margin, kernel trick, RBF/polynomial
- Created `ML/Logistic Regression.md` — log-odds, sigmoid, Softmax, multi-label
- Created `ML/Decision Tree.md` — split criteria, pre/post pruning, no normalization needed
- Rewrote `ML/Classic Model.md` as clean hub with comparison table

**Algorithm:**
- Filled `Algorithm/Tips on Improving Coding Quality.md` — was just a single image, now has actual coding discipline content

**Investment:**
- Filled `Investment/Valuation/Equity Risk Premium.md` — Damodaran approach, implied vs historical ERP, country risk
- Created `Investment/Books Reading/Security Analysis.md` — compiled key insights from Security Analysis annotations (intrinsic value, earnings estimation rules, double-counting, income/cash flow divergence)
- Deleted `Investment/Books Reading/Security Aaalysis.md` — was raw PDF annotation file (useless since PDF deleted, typo in name)

**OMSCS cross-domain links added:**
- `Distributed File Systems.md` → [[System Design/Replication]]
- `Threads and Concurrency.md` → [[System Design/Reliable, Scalable and Maintainable]]
- `Distributed Shared Memory.md` → [[System Design/Replication]], [[Encoding and Evolution]]
- `Remote Procedure Calls.md` → [[System Design/Encoding and Evolution]]

**Structural cleanup:**
- Removed all references to `Books/` folder (folder no longer exists — annotation files were deleted with PDFs)
- Fixed `Security Aaalysis` → `Security Analysis` link in Investment-MOC
- Updated CLAUDE.md, INDEX.md, ML-MOC, System-Design-MOC, Algorithm-MOC, Investment-MOC
- Updated ML-MOC to include SVM, Logistic Regression, Decision Tree entries

---

## [2026-04-18] refactor | Vault upgraded to full Karpathy WikiLLM pattern

**Changes made:**

- `CLAUDE.md` — Rewrote with complete Ingest/Query/Lint SOP; added `sources/` and `synthesis/` to folder structure and Knowledge Layer Map; added source/synthesis frontmatter formats
- `_log.md` — Migrated to new grep-friendly format `## [YYYY-MM-DD] operation | Title`
- `INDEX.md` — Added page-type metadata column; added Sources and Synthesis sections
- Created `sources/` folder with README — for per-source summary pages
- Created `synthesis/` folder with README — for cross-domain analysis and filed query answers

**Why:** Gap analysis against Karpathy's WikiLLM design revealed missing: Lint operation, Synthesis layer (query answers not filed back), per-source summary pages, and grep-friendly log format.

---

## [2026-04-18] refactor | Folder architecture redesigned — 3-layer numbering scheme

**Old structure (flat, mixed layers):**

```txt
_raw/, 00-MOC/, Algorithm/, Machine Learning/, System Design/, OMSCS/, Investment/, sources/, synthesis/, Template/, Pictures/
```

**New structure (numbered layers):**

```txt
0-raw/  ← Layer 0: Immutable sources
1-sources/  ← Layer 1: Source summaries
2-wiki/_nav/, 2-wiki/ml/, 2-wiki/system-design/, 2-wiki/algorithm/, 2-wiki/investment/, 2-wiki/omscs/  ← Layer 2
3-synthesis/  ← Layer 3: Cross-domain analysis
_assets/, _templates/  ← Support files
```

**Files moved:**

- `_raw/` → `0-raw/`
- `sources/` → `1-sources/`
- `Machine Learning/` → `2-wiki/ml/`
- `System Design/` → `2-wiki/system-design/`
- `Algorithm/` → `2-wiki/algorithm/`
- `Investment/` → `2-wiki/investment/`
- `OMSCS/` → `2-wiki/omscs/`
- `00-MOC/` → `2-wiki/_nav/`
- `synthesis/` → `3-synthesis/`
- `Pictures/` → `_assets/`
- `Template/` → `_templates/`

**Wikilinks fixed:** Path-qualified `[[System Design/X]]` links in 5 OMSCS files converted to filename-only `[[X]]` format before move.

**Updated:** `CLAUDE.md`, `INDEX.md` — all path references updated to new structure.

---

## [2026-04-18] cleanup | Vault scan and cleanup — removed 13 files, fixed 2 stubs

**Deleted (no value / superseded):**

- `🗺️ Vault Redesign Plan.md` — old planning doc, fully superseded
- `Untitled.base` — empty Obsidian base file
- `README.md` (root) — 1-line description, superseded by CLAUDE.md
- `0-raw/README.md` — duplicate of CLAUDE.md content
- `2-wiki/omscs/GTID.md` — stored a student ID number, not knowledge
- `_assets/Untitled.png`, `Untitled 1.png`, `Untitled 2.png`, `Untitled 2 1.png` — orphaned images, no references

**Moved to correct layer:**

- `2-wiki/ml/Quest for Machine Learning Book Outline.md` → `1-sources/Quest-for-Machine-Learning.md` (source outline, not a wiki concept)
- `2-wiki/omscs/GOIS/readings/*.pdf` (5 files) → `0-raw/courses/gois/` (raw material belongs in Layer 0)

**Deleted stubs (content absorbed into MOC):**

- `2-wiki/ml/Supervised Learning.md` — 9-line bullet list with no content; concept covered by ML-MOC and model notes
- References removed from: `Classic Model.md`, `Decision Tree.md`, `Unsupervised Learning.md`, `ML-MOC.md`

**References cleaned:**

- `OMSCS-MOC.md` — removed GTID entry
- `ML-MOC.md` — removed Supervised Learning outline entry, updated Quest for ML link to `1-sources/`

---

## [2026-04-19] | INGEST | Data Mining Problems in Retail (Katsov 2015)

**Source:** `1-sources/article-2015-03-10-Data-Mining-Problems-in-Retail.md` (raw clipping preserved at `1-sources/inbox/Data Mining Problems in Retail.md`)

**New wiki pages (3):**
- `2-wiki/ml/Recommender Systems.md` — content vs collaborative filtering, multi-objective ranking, implicit-dimension labeling
- `2-wiki/ml/Uplift Modeling.md` — differential response / incremental-lift estimation, four-quadrant decomposition
- `2-wiki/ml/Demand Prediction.md` — multiplicative decomposition D = V · P(purchase|visit) · P(j|purchase) · E[Q], MNL choice model, stockout censoring

**Updated wiki pages (3):**
- `2-wiki/ml/Logistic Regression.md` — linked softmax ↔ MNL ↔ Demand Prediction; added Uplift Modeling to Related
- `2-wiki/ml/AB Testing.md` — added "Beyond A/B: Uplift Estimation" section
- `2-wiki/ml/Text Representation.md` — added "Application: Labeling Implicit Dimensions" section linking to Recommender Systems

**Updated navigation:**
- `2-wiki/_nav/ML-MOC.md` — added new "Applied / Marketing & Retail" section; moved Recommender Systems out of "To Be Added"; added Katsov source reference
- `INDEX.md` — added Sources table entry; bumped ML note count 29 → 32; last-updated 2026-04-19

## [2026-04-19] | DELTA-SYNC | 1 file processed (5 gois PDFs and 2 other files already relocated in 2026-04-18 restructure, no re-ingest needed)
