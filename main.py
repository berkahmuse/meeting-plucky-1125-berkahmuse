#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes a single one-line joke (at most 200 characters) about a meeting
that should have been an email to /output/entry.txt.
"""
import os

# The entry is fixed text, not assembled or reformatted at runtime.
ENTRY_LINE = "We spent an hour reading the email aloud in a meeting, then booked a follow-up to discuss what it meant."

# Gate limits from RULES.txt: a single line of 1-200 characters.
MIN_LENGTH = 1
MAX_LENGTH = 200
OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"


def validate_entry(line):
    """Check the entry against the competition gate before writing."""
    assert "\r" not in line and "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    assert MIN_LENGTH <= len(line) <= MAX_LENGTH, (
        f"entry is {len(line)} chars, must be {MIN_LENGTH}-{MAX_LENGTH}"
    )
    return line


def main():
    line = validate_entry(ENTRY_LINE.strip())
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, OUTPUT_FILE), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
