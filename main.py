#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (1-280 UTF-8 characters, counted as code points).
Runs in a sandbox with no network.

The output is a fixed string, so repeated runs are byte-identical.
"""

from pathlib import Path

JOKE = "The agent refactored my code so cleanly the bug now has perfect separation of concerns."

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> str:
    """Return the entry text, enforcing the 1-280 character gate."""
    entry = text.strip()
    if not (1 <= len(entry) <= 280):
        raise ValueError("entry must be 1-280 characters")
    if not entry:
        raise ValueError("entry must not be only white space")
    return entry


def main() -> None:
    entry = validate_entry(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
