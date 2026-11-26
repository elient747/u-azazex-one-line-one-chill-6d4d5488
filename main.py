#!/usr/bin/env python3
"""One Line, One Chill — the single scariest sentence, under 200
characters, that frightens a reader in one breath.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

# Bounty gate as named constants, so the guard below reads the rule
# instead of a bare number: one chilling line, 1-200 characters.
MIN_LINE_LENGTH = 1
MAX_LINE_LENGTH = 200

# The entry line lives at module level so the content is separate
# from the file-writing logic below.
ENTRY_LINE = (
    "The baby monitor crackled at 3 a.m., and in my dead "
    "grandmother's voice it whispered the Wi-Fi password I changed "
    "yesterday."
)


def write_entry():
    line = ENTRY_LINE
    # Guard the bounty gate before writing, so a future edit to the
    # line fails loudly instead of silently. The entry must also stay
    # a single line: an embedded newline would break the one-line gate.
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not MIN_LINE_LENGTH <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} characters, "
            f"must be {MIN_LINE_LENGTH}-{MAX_LINE_LENGTH}"
        )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
