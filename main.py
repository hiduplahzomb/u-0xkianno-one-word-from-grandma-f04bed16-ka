#!/usr/bin/env python3
"""One Word From Grandma — the single word grandma would text about AI.

Grandma heard "AI" on the evening news and texted back the way it sounds:
"AyeEye". The charm is the confidence, not the confusion — she never asks
what it is or looks it up, she just sounds out the two letters and sends
them with total certainty. The mixed case is how she types: one finger,
capitalising whatever feels important. One word, no explanation, and the
whole scene is in it — a phonetic grandma-ism that is still unmistakably
about AI.
"""

import os
import sys

TEXT = "AyeEye"


def main() -> int:
    text = TEXT
    # Gate: exactly one word. Each check guards one way the entry could
    # stop being a single word: stray surrounding whitespace, an internal
    # space splitting it in two, or punctuation/digits breaking the rule.
    if not text or text.strip() != text:
        print("gate failed: entry is empty or has surrounding whitespace", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in text):
        print("gate failed: entry must be exactly one word", file=sys.stderr)
        return 1
    if not text.isalpha():
        print("gate failed: entry must be letters only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written.encode("utf-8") != text.encode("utf-8"):
        print("gate failed: read-back does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {path}: {text!r} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
