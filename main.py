"""One Word From Grandma — entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Python stdlib only, deterministic,
no network.
"""

import os

# The word a grandma would text about AI: a little box that talks back.
# Warm, a little confused, funny in one word, tied to the machine.
WORD = "TALKINGBOX"

OUTPUT_FILENAME = "entry.txt"
FALLBACK_DIR = "/output"


def validate(word: str) -> str:
    """Check the entry is exactly one word, 1-30 characters, no padding."""
    if not word or word != word.strip():
        raise ValueError("word must be non-empty and not padded with whitespace")
    if len(word.split()) != 1:
        raise ValueError("word must be exactly one word")
    if not 1 <= len(word) <= 30:
        raise ValueError("word must be 1-30 characters long")
    return word


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR


def entry_path(directory: str) -> str:
    """Path of the entry file inside the resolved output directory."""
    return os.path.join(directory, OUTPUT_FILENAME)


def write_entry(word: str) -> str:
    word = validate(word)
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = entry_path(directory)
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    return path


def main() -> None:
    path = write_entry(WORD)
    print(f"wrote {path}: {WORD}")


if __name__ == "__main__":
    main()
