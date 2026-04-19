#!/usr/bin/env python3
"""
PostToolUse hook: when Claude writes a file to 3-synthesis/, auto-updates INDEX.md.
stdin: {"session_id": "...", "tool_name": "...", "tool_input": {...}, "tool_response": {...}}
"""
import json
import os
import re
import sys
from datetime import date

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INDEX_PATH = os.path.join(VAULT_ROOT, "INDEX.md")

SYNTHESIS_SECTION_MARKER = "## Synthesis (`3-synthesis/`)"
TABLE_HEADER = "| File | Type | Domains | Created |"
TABLE_SEP =    "| ---- | ---- | ------- | ------- |"

def parse_frontmatter(content):
    meta = {}
    if not content.startswith("---"):
        return meta
    end = content.find("\n---", 3)
    if end == -1:
        return meta
    block = content[3:end]
    for line in block.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
    return meta

def ensure_synthesis_table(index_content):
    if SYNTHESIS_SECTION_MARKER not in index_content:
        return index_content
    if TABLE_HEADER in index_content:
        return index_content
    insert_at = index_content.index(SYNTHESIS_SECTION_MARKER) + len(SYNTHESIS_SECTION_MARKER)
    next_section = index_content.find("\n## ", insert_at)
    table_block = f"\n\n{TABLE_HEADER}\n{TABLE_SEP}\n"
    if next_section == -1:
        return index_content + table_block
    return index_content[:next_section] + table_block + index_content[next_section:]

def add_synthesis_row(index_content, filename, meta):
    title = meta.get("title", filename.replace(".md", "").replace("-", " ").title())
    ftype = meta.get("type", "analysis")
    domains = meta.get("domains", "").strip("[]").replace('"', "").replace("'", "")
    created = meta.get("created", date.today().isoformat())
    link = f"[[{filename.replace('.md', '')}]]"
    new_row = f"| {link} | {ftype} | {domains} | {created} |"

    if link in index_content:
        return index_content

    header_pos = index_content.find(TABLE_HEADER)
    if header_pos == -1:
        return index_content

    sep_pos = index_content.find(TABLE_SEP, header_pos)
    if sep_pos == -1:
        return index_content

    insert_pos = index_content.find("\n", sep_pos) + 1
    return index_content[:insert_pos] + new_row + "\n" + index_content[insert_pos:]

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_input = data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    normalized = file_path.replace("\\", "/")
    if "3-synthesis/" not in normalized:
        sys.exit(0)

    filename = os.path.basename(file_path)
    if filename == "README.md" or filename.startswith("lint-"):
        sys.exit(0)

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    except Exception:
        sys.exit(0)

    meta = parse_frontmatter(content)

    if not os.path.exists(INDEX_PATH):
        sys.exit(0)

    with open(INDEX_PATH, encoding="utf-8") as f:
        index_content = f.read()

    index_content = ensure_synthesis_table(index_content)
    index_content = add_synthesis_row(index_content, filename, meta)

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(index_content)

    print(f"[INDEX UPDATED] Added {filename} to INDEX.md Synthesis table.")

if __name__ == "__main__":
    main()
