"""Write one nostalgic childhood-memory sentence to /output/entry.txt.

The sentence must be a single sentence, 1-280 characters, not only
white space. The gate refuses anything outside that range.
"""

import os
import sys

SENTENCE = "Every summer evening my grandmother stood at the kitchen door shelling peas into a tin bowl, and I knew dinner was ready when the smell of fresh rice drifted out and the cicadas got loud enough to drown the radio."

MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_NAME = "entry.txt"


def validate_sentence(sentence):
    """Check the sentence against the competition gate before writing it."""
    stripped = sentence.strip()
    if not stripped:
        raise ValueError("sentence is empty or only white space")
    if "\n" in stripped:
        raise ValueError("sentence must be a single line")
    if not MIN_CHARS <= len(stripped) <= MAX_CHARS:
        raise ValueError(
            "sentence must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(stripped))
        )
    return stripped


def write_entry(sentence, out_dir):
    """Write the validated sentence to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    return path


def main():
    try:
        sentence = validate_sentence(SENTENCE)
    except ValueError as exc:
        print("invalid sentence: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(sentence, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
