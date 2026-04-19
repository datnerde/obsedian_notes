#!/usr/bin/env python3
"""
UserPromptSubmit hook: detects sync trigger words and injects vault delta context.
Claude Code calls this before processing each user message.
stdin: {"session_id": "...", "user_message": "..."}
stdout: {"context": "..."} — injected as additional context for Claude
"""
import json
import os
import re
import subprocess
import sys
from datetime import date

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_PATH = os.path.join(VAULT_ROOT, "_log.md")

SYNC_TRIGGERS = [
    "整理笔记", "同步笔记", "更新笔记", "同步一下", "整理一下",
    "sync notes", "organize notes", "ingest new", "delta sync", "delta-sync",
    "有什么新的", "更新了什么",
]

def get_last_sync_date():
    if not os.path.exists(LOG_PATH):
        return None
    last_date = None
    pattern = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s*\|.*?(INGEST|DELTA-SYNC)", re.IGNORECASE)
    with open(LOG_PATH, encoding="utf-8") as f:
        for line in f:
            m = pattern.match(line)
            if m:
                last_date = m.group(1)
    return last_date

def get_new_files_since(since_date):
    try:
        result = subprocess.run(
            ["git", "log", f"--since={since_date}", "--name-only", "--pretty=format:", "--diff-filter=A",
             "--", "0-raw/", "1-sources/"],
            cwd=VAULT_ROOT, capture_output=True, text=True, timeout=10
        )
        files = [f.strip() for f in result.stdout.splitlines() if f.strip() and not f.startswith("warning:")]
        return files
    except Exception:
        pass

    try:
        result = subprocess.run(
            ["find", "0-raw", "1-sources", "-newer", "_log.md", "-name", "*.md"],
            cwd=VAULT_ROOT, capture_output=True, text=True, timeout=10
        )
        return [f.strip() for f in result.stdout.splitlines() if f.strip()]
    except Exception:
        return []

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    user_message = data.get("user_message", "")
    if not any(t in user_message for t in SYNC_TRIGGERS):
        sys.exit(0)

    last_date = get_last_sync_date()
    today = date.today().isoformat()

    if not last_date:
        context = f"[VAULT DELTA] No previous INGEST found in _log.md. Today is {today}. Treat all files in 0-raw/ and 1-sources/ as candidates for ingestion."
    else:
        new_files = get_new_files_since(last_date)
        if new_files:
            file_list = "\n  - " + "\n  - ".join(new_files)
            context = (
                f"[VAULT DELTA] Last sync: {last_date}. Today: {today}.\n"
                f"New files detected since last sync:{file_list}\n"
                f"Run DELTA-SYNC operation on these files now."
            )
        else:
            context = (
                f"[VAULT DELTA] Last sync: {last_date}. Today: {today}. "
                f"No new files detected in 0-raw/ or 1-sources/ since last sync. "
                f"Vault appears up to date."
            )

    print(json.dumps({"context": context}))

if __name__ == "__main__":
    main()
