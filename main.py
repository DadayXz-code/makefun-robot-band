#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry (program/v1, python3.13 stdlib only).

Writes one funny robot band name plus a few words on its hit song to
``<output-dir>/entry.txt``. The output directory is ``$MAKEFUN_OUTPUT_DIR``
when set, otherwise ``/output`` (the grader sandbox contract).

The entry is a single fixed string: deterministic, no randomness, no
network, no reads outside this file, and nothing is written anywhere
except the output directory.
"""

import os
import sys

# The entry: a robot band name with a hit-song line, under 200 characters.
ENTRY = 'The Roomba Stones \u2014 hit single "Dust in the Wind (Under the Couch)"'


def main() -> int:
    # Gate mirror: the entry must be 1-200 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the entry text, no trailing newline, UTF-8.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
