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
