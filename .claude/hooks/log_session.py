#!/usr/bin/env python3
"""
Stop hook: appends a session summary entry to _log.md when Claude finishes a turn
that involved file writes (skips read-only sessions to keep the log clean).
stdin: {"session_id": "...", "stop_hook_active": true, "transcript_path": "..."}
"""
import json
import os
import re
import sys
from datetime import date

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_PATH = os.path.join(VAULT_ROOT, "_log.md")

WRITE_TOOLS = {"Write", "Edit", "NotebookEdit"}

def parse_transcript(transcript_path):
    if not transcript_path or not os.path.exists(transcript_path):
        return []
    try:
        with open(transcript_path, encoding="utf-8") as f:
            lines = f.readlines()
        entries = []
        for line in lines:
            try:
                entries.append(json.loads(line))
            except Exception:
                pass
        return entries
    except Exception:
        return []

def extract_session_info(transcript):
    files_written = []
    ops_detected = set()
    synthesis_files = []

    op_keywords = {
        "INGEST": ["ingest", "1-sources", "source summary"],
        "QUERY": ["query", "3-synthesis", "synthesis"],
        "LINT": ["lint", "health check", "orphan"],
        "DELTA-SYNC": ["delta-sync", "delta sync", "整理笔记", "同步笔记"],
    }

    for entry in transcript:
        if entry.get("type") == "tool_use":
            tool_name = entry.get("name", "")
            if tool_name in WRITE_TOOLS:
                fp = entry.get("input", {}).get("file_path", "")
                if fp:
                    files_written.append(fp)
                    if "3-synthesis/" in fp.replace("\\", "/"):
                        synthesis_files.append(os.path.basename(fp))

        if entry.get("type") == "text":
            text = entry.get("text", "").lower()
            for op, keywords in op_keywords.items():
                if any(kw in text for kw in keywords):
                    ops_detected.add(op)

    return files_written, ops_detected, synthesis_files

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    transcript_path = data.get("transcript_path", "")
    transcript = parse_transcript(transcript_path)
    files_written, ops_detected, synthesis_files = extract_session_info(transcript)

    if not files_written:
        sys.exit(0)

    today = date.today().isoformat()
    op_str = " + ".join(sorted(ops_detected)) if ops_detected else "SESSION"
    n = len(files_written)
    detail = f"{n} file(s) written"
    if synthesis_files:
        detail += f" — synthesis: {', '.join(synthesis_files)}"

    log_entry = f"\n## {today} | {op_str} | {detail}\n"

    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"[log_session] Failed to write to _log.md: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
