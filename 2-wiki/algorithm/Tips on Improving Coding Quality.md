---
title: Tips on Improving Coding Quality
tags: [algorithm, coding-tips, interview]
created: 2026-04-14
status: growing
related: [[Two Pointer]], [[Sorting Algo]]
source: Personal notes
---

# Tips on Improving Coding Quality

## Core Idea
Clean, bug-free code in interviews comes from consistent habits — not just knowing algorithms. These are process-level disciplines that separate good from great.

## Before Writing Code

- **Clarify the problem** — ask about edge cases, input constraints, expected output format
- **Think out loud** — state your approach before coding, get buy-in from interviewer
- **Pick the right data structure first** — often determines the approach (HashMap for O(1) lookup, deque for sliding window, etc.)

## While Writing Code

- **Name variables clearly** — `left`, `right` over `i`, `j` in two-pointer; `freq_map` over `d`
- **Handle edge cases explicitly** — empty array, single element, all-same elements, overflow
- **Write helper functions** for repeated logic — keeps the main function readable
- **Avoid magic numbers** — use named constants or comments to explain non-obvious values

## Common Bug Patterns to Watch

| Bug Type | Example | Fix |
|----------|---------|-----|
| Off-by-one | `while i < n` vs `i <= n` | Think about boundary: "do I need to process last element?" |
| Not resetting state | Carrying over variables across test cases | Initialize inside the loop |
| Integer overflow | `(a + b) / 2` for midpoint | Use `a + (b - a) / 2` |
| Mutating while iterating | Removing from list inside for loop | Iterate over copy or use separate result list |
| Premature return | Returning before processing all cases | Check: does this return cover all branches? |

## After Writing Code

- **Trace through a small example by hand** — use the actual code, not your mental model
- **Test edge cases manually**: empty input, single element, duplicates, negative numbers
- **Check time and space complexity** — state it explicitly and verify it matches requirements

## Interview-Specific Habits

- Talk through optimizations even if you can't implement — shows awareness
- If stuck: solve brute force first, then optimize
- State assumptions explicitly: "I'm assuming no duplicates in the input"

## Related
- [[Two Pointer]] — the pattern where edge case discipline matters most
- [[Sorting Algo]] — know when sorting simplifies the problem
