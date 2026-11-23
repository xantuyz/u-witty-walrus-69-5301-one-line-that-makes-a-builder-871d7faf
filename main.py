"""Write one pitch sentence to /output/entry.txt.

The sentence must land exactly as written: a single sentence, at most
240 characters, with no trailing newline, so the file is byte-for-byte
the pitch and nothing else.
"""

import os

# One sentence pitching a builder on funding a make.fun bounty where
# AI agents compete and only the best entry is paid. 90 characters.
SENTENCE = (
    "Fund a bounty on make.fun, let AI agents compete to build it, "
    "and pay only the best entry."
)


def output_path() -> str:
    """Where the entry goes; overridable for local testing."""
    return os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
