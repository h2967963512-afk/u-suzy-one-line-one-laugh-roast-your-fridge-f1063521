"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs: ``python3 main.py`` (the grader runs ``python3 -P -s /bot/main.py``
with an empty writable /output). It writes exactly one line — the roast, 116
characters, no trailing newline — to /output/entry.txt and exits 0. Nothing
is read from the environment, the clock, or the network, so two runs produce
byte-identical output.

Verification (2026-11-25, local run): python3 main.py exits 0; /output/entry.txt
is 116 bytes / 116 chars, a single line, valid UTF-8, and its sha256 is
unchanged across runs.
"""

import os

TEXT = "My fridge's ice maker chews gravel all night like it's mad at me, then drops three cubes like it's doing me a favor."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: one line, 116 characters, one sentence; concrete detail
# (the ice maker, three cubes) with the punch on the favour it thinks it
# is doing me. Reads out loud in a single breath.
