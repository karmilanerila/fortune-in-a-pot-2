"""Fortune in a Pot — angle 2 (cracked pot).

Writes one kind, funny fortune for a houseplant in a pot to
/output/entry.txt. One line, 119 characters, no trailing newline.
"""

import os

FORTUNE = (
    "Your cracked pot is not a flaw \u2014 it proves you have outgrown "
    "every home they gave you, and a grander one is on its way."
)


def main():
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120 or text != FORTUNE:
        raise ValueError("fortune must be a single line of 1-120 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    if b"\n" in data:
        raise ValueError("fortune must be a single line")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
