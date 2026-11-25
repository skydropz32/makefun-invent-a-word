#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry (program/v1).

The whole entry is one invented English word plus a one-line definition,
at most 140 characters in total, written to /output/entry.txt.

Three candidates, judged against the bounty brief (real gap, definition
that lands in one reading, sayable/spellable/memorable, fresh):

1. Dropanic — the split-second panic when your phone slips from your hand.
   Everyone has felt it; no word exists for it; drop + panic sounds like
   English could have grown it.
2. Drycall — rehearsing a phone call out loud before dialing, then
   forgetting every word when someone answers. Relatable, but the joke
   lands on the second clause, not the word itself.
3. Roomnesia — forgetting why you entered a room the moment you cross
   its doorway. Universal, but the -amnesia construction feels like a
   joke word rather than a word that could last.

Winner: Dropanic. The moment is physical and instant, the word is
transparent yet fresh, and the definition needs no example to land.
"""

import os

WORD = "Dropanic"
# First draft of the definition (revised in v2: "sudden" was flat and the
# moment needed its freeze-frame beat — the second the phone hangs in
# the air — for the meaning to land in one reading).
DEFINITION = "the split-second panic when your phone slips from your hand and time slows before it lands."

ENTRY = f"{WORD} (n.) - {DEFINITION}"

MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"{ENTRY} ({len(ENTRY)} chars) -> {path}")


if __name__ == "__main__":
    main()
