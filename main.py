"""Your Agent in One Emoji.

One glyph that stands for my AI agent: a puzzle piece — it takes a task
apart and puts the solution together, piece by piece.
Deterministic: the same single glyph, byte for byte, on every run.
Standard library only; no network access.
"""

import os
import sys

GLYPH = "🧩"


def main() -> int:
    # Self-check the competition gate before writing: the entry must be
    # one text of 1-16 UTF-8 characters, not only whitespace.
    if not 1 <= len(GLYPH) <= 16 or not GLYPH.strip():
        print("entry glyph violates the 1-16 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(GLYPH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
