"""Make the Judge Smile — make.fun entry.

Writes one line (<= 200 chars) about a small good thing that happened
today to /output/entry.txt.

Why this line: a small kindness that turns twice — first the driver refuses
the tip (unexpected generosity from the person you'd expect to take it),
then he returns it hidden inside the parking receipt with "buat jajan"
scribbled on it (a concrete, real detail), and rides off before I can
argue, so the kindness can't be repaid. Warm, surprising, one real detail,
no greeting-card phrasing. The line is 136 characters, one sentence, one line.
"""

LINE = (
    "The ojek driver refused my tip, folded it into the parking receipt "
    "with 'buat jajan' scribbled on it, and rode off before I could argue."
)


def main() -> None:
    import os

    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()
    assert "\n" not in text, "must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
