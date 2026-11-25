"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who was just
liquidated to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "Your lucky numbers are 0, 0, 0, and the margin call you ignored at midnight."
)
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160
MAX_WORDS = 20


def validate(text):
    """Check the entry text against the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry text must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if len(text.split()) > MAX_WORDS:
        raise ValueError(
            f"entry text is {len(text.split())} words, over the {MAX_WORDS} limit"
        )
    return True


def main():
    validate(ENTRY_TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open() + explicit chmod 644: the grader runs as a different
    # user, so the output file must be world-readable.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(ENTRY_TEXT)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
