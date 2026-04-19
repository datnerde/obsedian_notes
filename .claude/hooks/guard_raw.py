#!/usr/bin/env python3
"""
PreToolUse hook: blocks any Write or Edit to 0-raw/ (immutability guard).
Claude Code calls this before Write/Edit tool calls.
stdin: {"session_id": "...", "tool_name": "...", "tool_input": {...}}
Exit 2 = block the tool call. Claude Code shows stdout as the reason.
"""
import json
import sys

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_input = data.get("tool_input", {})
    file_path = tool_input.get("file_path", "") or tool_input.get("path", "")

    vault_segments = file_path.replace("\\", "/").split("/")
    if "0-raw" in vault_segments:
        print(json.dumps({
            "error": (
                f"BLOCKED: 0-raw/ is immutable — writes are not allowed.\n"
                f"Attempted path: {file_path}\n"
                f"Place source material in 0-raw/ manually, then reference it from 1-sources/."
            )
        }))
        sys.exit(2)

if __name__ == "__main__":
    main()
