# 🗺️ Steven's Vault — LLM Wiki 改造方案

> **状态：草案，待确认后执行**  
> 基于 Andrej Karpathy 的 LLM Wiki 架构 + Obsidian 最佳实践

---

## 一、现状诊断（Before）

### 你现在的结构
```
vault/
├── Algorithm/         ← 算法模式 + LeetCode 混在一起
├── Books/             ← 书摘（内容和 ML/Investment 重叠）
├── Investment/        ← 结构最好的区域
├── Machine Learning/  ← 章节级笔记，缺少原子化
├── OMSCS/             ← 课程笔记，结构良好
├── System Design/     ← DDIA 笔记
├── Template/          ← 只有一个空白 annotation 模板
└── README.md          ← 一句话介绍
```

### 现存问题

**1. 没有 AI 可读的"说明书"**  
你的 vault 对 Claude/GPT 来说是个黑盒。没有告诉 AI "这里有什么、怎么组织、怎么维护"。

**2. 笔记粒度不一致**  
- `Feature Engineering.md` = 整章内容（太大）  
- `1. Two Sum.md` = 一道题（合适）  
- LeetCode 每题一文件 ✅，但 ML 笔记一篇几十个概念 ❌

**3. 缺少"原材料层"**  
Karpathy 架构的核心是 `raw/`（原始资料）和 `wiki/`（提炼知识）分离。你的笔记目前两者混在一起。

**4. 模板几乎是空的**  
`annotate.md` 只有一个字段，没有 tags、created date、related notes、status 等关键 frontmatter。

**5. 没有 Maps of Content（MOC）**  
每个领域缺少一个"导航中心"，很难快速找到知识体系的入口。

**6. Books/ 是孤岛**  
书摘和 ML、Investment 的笔记没有双向链接，重复了信息。

---

## 二、改造方案（After）

### 新的文件夹结构
```
vault/
│
├── AGENTS.md              ⭐ AI 指令文件（最重要的新增）
├── INDEX.md               📋 全局目录
├── _log.md                📝 操作日志（append-only）
│
├── _raw/                  📦 原始资料层（不可修改）
│   ├── books/             ← PDF、书摘原文
│   ├── papers/            ← 论文
│   └── courses/           ← 课程材料
│
├── 00-MOC/                🗺️ Maps of Content（导航层）
│   ├── ML-MOC.md
│   ├── System-Design-MOC.md
│   ├── Algorithm-MOC.md
│   ├── Investment-MOC.md
│   └── OMSCS-MOC.md
│
├── Algorithm/             （现有，内部重组）
│   ├── Patterns/          ← 两指针、滑动窗口等模式笔记
│   └── Problems/          ← LeetCode 题目（原 Leetcode/ 文件夹改名）
│
├── Machine Learning/      （现有，加 frontmatter）
├── System Design/         （现有，加 frontmatter）
├── OMSCS/                 （现有，保持）
├── Investment/            （现有，保持）
│
└── Template/              （升级模板）
    ├── concept-note.md    ← 通用概念笔记
    ├── leetcode.md        ← LeetCode 题目
    ├── book-chapter.md    ← 书摘/章节
    └── annotate.md        ← PDF 注释（现有）
```

---

## 三、核心新增文件预览

### 📄 AGENTS.md（AI 指令文件）

这是 Karpathy 架构最关键的文件。任何 AI（Claude、GPT）打开你的 vault 都会先读这个文件，知道如何导航和维护你的知识库。

```markdown
# Steven's Knowledge Vault — AI Agent Instructions

## Purpose
This is Steven's second brain vault covering:
- Machine Learning & AI engineering
- System Design (DDIA-based)
- Algorithms & LeetCode practice
- Investment research (value investing + quant)
- OMSCS graduate coursework

## How to Navigate
- Start with `INDEX.md` for the global map
- Each domain has a MOC file in `00-MOC/`
- Raw source materials are in `_raw/` (read-only)
- All compiled knowledge is in domain folders

## Note Conventions
- Frontmatter: tags, created, status, related
- Status values: `seedling` | `growing` | `evergreen`
- Links: use [[wikilinks]] to connect concepts
- Language: English for technical concepts, Chinese OK for personal commentary

## How to Add Knowledge
1. Drop raw sources into `_raw/`
2. Compile into atomic notes in the relevant domain folder
3. Link to related notes with [[wikilinks]]
4. Update the domain MOC
5. Append to `_log.md`

## Key Files
- `INDEX.md` — global table of contents
- `00-MOC/*.md` — domain navigation hubs
- `_log.md` — operation history
```

---

### 📄 改造后的 Note 模板（概念笔记）

**Before（现在的笔记）：**
```markdown
## 1.Normalization

- Reason:
  - Remove the impact on range & scale...
- Methods:
  - Min-Max Scaling...
```
没有标题元信息、没有 tags、没有状态、没有关联笔记。

**After（改造后）：**
```markdown
---
title: Feature Normalization
tags: [ml, feature-engineering, preprocessing]
created: 2024-01-01
status: growing
related: [[Feature Engineering]], [[Gradient Descent]], [[Model Evaluation]]
source: Quest for Machine Learning - Chapter 1
---

# Feature Normalization

## Core Idea
Scaling features to a common range removes bias from magnitude differences
and improves gradient-based optimization.

## Methods
- **Min-Max Scaling** → range [0,1], linear transformation
- **Z-Score Normalization** → N(0,1), use when outliers matter

## When NOT to Normalize
- Tree-based models (Decision Tree, Random Forest, XGBoost)
  are invariant to monotonic feature transformations

## Related Concepts
- [[Gradient Descent]] benefits from normalization (faster convergence)
- [[One-Hot Encoding]] for categorical features doesn't need normalization

## References
- [[Quest for Machine Learning Notes]] Chapter 1
```

---

### 📄 改造后的 LeetCode 模板

**Before：**
```markdown
![[screenshot.png]]
- Use hash map to solve
  - Time: O(n)
```

**After：**
```markdown
---
tags: [leetcode, hash-map, two-pointer]
difficulty: Easy
pattern: [[Two Pointer]], [[Hash Map]]
status: solved
date: 2024-01-01
---

# 1. Two Sum

## Problem
Given an array `nums` and a `target`, return indices of two numbers that add up to target.

## Approach 1: Hash Map ⭐ (Optimal)
- **Idea**: Store complement as we scan
- **Time**: O(n) | **Space**: O(n)

## Approach 2: Two Pointer + Sort
- **Time**: O(n log n) | **Space**: O(n)
- Trade-off: loses original indices unless tracked

## Key Insight
> Use hash map when you need O(1) lookup of "what do I need to complete this?"

## Related Problems
- [[15. 3Sum]] — same idea, add outer loop
- [[170. Two Sum III]] — variant with data structure
```

---

### 📄 00-MOC/Algorithm-MOC.md 示例

```markdown
---
tags: [moc, algorithm]
---

# Algorithm — Map of Content

## Patterns（模式）
- [[Two Pointer]] — 相向、同向、背向
  - [[相向two pointer]] | [[同向two pointer]] | [[背向two pointer]]
- [[Sorting Algo]]
- [[Sliding Window]] ← 待创建

## LeetCode Problems by Pattern

### Two Pointer
- [[1. Two Sum]] Easy ✅
- [[15. 3Sum]] Medium ✅
- [[19. Remove Nth Node From End of List]] Medium ✅
- [[26. Remove Duplicates from Sorted Array]] Easy ✅

### String
- [[5. Longest Palindromic Substring]] Medium ✅
- [[125. Valid Palindrome]] Easy ✅
- [[680. Valid Palindrome II]] Easy ✅

## Resources
- [[Tips on Improving Coding Quality]]
```

---

## 四、推荐插件升级

你已有的插件很好。建议**额外安装**：

| 插件 | 用途 | 优先级 |
|------|------|--------|
| **Dataview** | 用 SQL 查询笔记，自动生成题目列表、状态追踪 | ⭐⭐⭐ 必装 |
| **Templater** | 比原生 Template 强大，支持变量、日期、自动化 | ⭐⭐⭐ 必装 |
| **Smart Connections** | 用 AI embedding 发现笔记间的隐藏联系 | ⭐⭐ 推荐 |
| **Tag Wrangler** | 批量管理 tags，防止 tag 碎片化 | ⭐⭐ 推荐 |

---

## 五、执行计划（如果你同意方案）

我会按以下顺序执行，**每步完成后可以检查**：

| 步骤 | 内容 | 影响范围 |
|------|------|----------|
| 1 | 创建 `AGENTS.md` | 新文件，无破坏性 |
| 2 | 创建 `INDEX.md` + 5 个 `00-MOC/` 文件 | 新文件，无破坏性 |
| 3 | 升级 4 个 Template 文件 | 替换现有 template |
| 4 | 给所有现有笔记加 frontmatter | 修改现有文件（可逆）|
| 5 | 重命名 `Algorithm/Leetcode/` → `Algorithm/Problems/` | 移动文件 |
| 6 | 创建 `_raw/` 目录结构 | 新文件夹，无破坏性 |
| 7 | 创建 `_log.md` | 新文件，无破坏性 |

**步骤 1-3 和 6-7 零风险，步骤 4-5 可以用 obsidian-git 回滚。**

---

## 六、这套系统的日常工作流

```
学到新东西
    ↓
把原始资料放进 _raw/
    ↓
让 Claude 帮你"编译"成 atomic note
    ↓
Claude 自动加 frontmatter + wikilinks
    ↓
Claude 更新对应的 MOC 文件
    ↓
Claude 在 _log.md 记录操作
    ↓
你在 Obsidian Graph View 里看到知识网络生长 🌱
```

---

*方案生成于 2026-04-14 | 基于 [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 架构*
