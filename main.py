#!/usr/bin/env python3
"""One Line, One Chill — the single scariest sentence, under 200
characters, that frightens a reader in one breath.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
import os

# The entry line lives at module level so the content is separate
# from the file-writing logic below.
ENTRY_LINE = (
    "The baby monitor crackled at 3 a.m., and in my dead "
    "grandmother's voice it whispered the Wi-Fi password I changed "
    "yesterday."
)


def write_entry():
    line = ENTRY_LINE
    # Guard the bounty gate (1-200 characters) before writing, so a
    # future edit to the line fails loudly instead of silently.
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
