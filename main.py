#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock."""
import os

ENTRY = (
    "I didn't eat your sock \u2014 I rescued it. It was cold and alone "
    "under the bed, and honestly it had more personality than the rug, "
    "so I gave it a home. In my dustbin."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
