"""One-sentence absurd invention pitch: the Reuniter.

The pitch: a tiny drone that lives in the laundry basket and solves
the tiny everyday annoyance of socks vanishing in the wash - it tracks
down every runaway sock and reunites each pair with a dramatic
airport-style announcement, as if the socks had just landed from
opposite ends of the world.

Gate guard: the entry must be UTF-8 text of 1 to 220 characters, a
single sentence on a single line, and not only white space - the same
gate the sealed scorer applies to /output/entry.txt. Refuse to write
anything that fails it, so a bad sentence can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "The Reuniter is a tiny drone that lives in the laundry basket, "
    "interrogates the washing machine about every missing sock, and "
    "reunites each pair with a dramatic airport-style announcement."
)

MIN_CHARS = 1
MAX_CHARS = 220


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    # Exactly one sentence: a single terminal full stop, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    # The file itself carries a trailing newline, so it must fit too.
    if len(text) + 1 > MAX_CHARS:
        raise SystemExit(
            f"entry plus newline is {len(text) + 1} characters, "
            f"must be at most {MAX_CHARS}"
        )
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
