#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes exactly one word to /output/entry.txt: the single word a
grandma would text about AI.
"""

import os

WORD = "Computy"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    word = WORD
    # Internal validation mirroring the competition gate:
    # UTF-8 text, 1-30 characters, not only whitespace, exactly one word.
    assert isinstance(word, str)
    encoded = word.encode("utf-8")
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word.strip(), "word must not be only whitespace"
    assert not any(ch.isspace() for ch in word), "word must be a single word"
    assert len(word.split()) == 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
