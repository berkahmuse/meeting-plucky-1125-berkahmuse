#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes a single one-line joke (at most 200 characters) about a meeting
that should have been an email to /output/entry.txt.
"""
import os

JOKE = "We spent an hour reading the email aloud in a meeting, then booked a follow-up to discuss what it meant."

def main():
    line = JOKE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
