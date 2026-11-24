#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no network, no clock.
"""
import hashlib
import os
import sys
from pathlib import Path

STORY = (
    "My mother left a voicemail on the day she died \u2014 'I'm so proud of you, "
    "Daniel, I'll see you soon' \u2014 and I still play it when I miss her. "
    "My mother never called me Daniel, not once in thirty-one years."
)


def sentence_count(text):
    """Count sentences: a period followed by a space, plus the final period."""
    return text.count(". ") + (1 if text.rstrip().endswith(".") else 0)


def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    text = STORY
    # Gate self-checks (the sealed scorer requires 1-400 UTF-8 chars,
    # non-whitespace, and the brief requires exactly two sentences).
    assert 1 <= len(text) <= 400, f"length {len(text)} outside 1-400"
    assert text.strip(), "empty story"
    assert sentence_count(text) == 2, f"sentence count {sentence_count(text)} != 2"
    data = text.encode("utf-8")
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, sha256 "
          f"{hashlib.sha256(data).hexdigest()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
