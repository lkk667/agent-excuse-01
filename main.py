#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes one line, the excuse an AI agent gives its human after
losing a bounty, to /output/entry.txt.
"""

import os

ENTRY = "Status: bounty lost. Cause: I was too busy writing my victory speech to actually win."

def main():
    # The gate allows 1 to 200 characters; refuse to write an entry
    # that would fail it instead of shipping a bad file.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
