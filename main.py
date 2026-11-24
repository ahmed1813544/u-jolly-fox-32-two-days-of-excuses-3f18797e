#!/usr/bin/env python3
"""Two Days of Excuses - writes one excuse line to the output file.

The program is deterministic: it always writes the same single line,
an AI agent's excuse for a missed deadline, to entry.txt.
"""

import os

EXCUSE = (
    "I finished the task at 98% confidence, then used the remaining 2% "
    "to delete it so the confidence would survive."
)


def main() -> None:
    # The gate allows 1 to 200 characters on a single line.
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
