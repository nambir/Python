"""Slide 17 — Generators (Real Python patterns)."""
import itertools
from pathlib import Path


def csv_reader(file_name: str):
    """Lazy line reader — does NOT load the whole file into memory."""
    with open(file_name, encoding="utf-8") as f:
        for row in f:
            yield row.rstrip("\n")


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


def nums():
    for n in range(1, 6):
        yield n


def square(seq):
    for n in seq:
        yield n * n


if __name__ == "__main__":
    sample = Path(__file__).with_name("_sample_lines.txt")
    sample.write_text("a\nb\nc\n", encoding="utf-8")

    print("lazy rows:", list(csv_reader(str(sample))))
    print("genexpr:", list(n * n for n in range(5)))

    gen = infinite_sequence()
    print("infinite next:", next(gen), next(gen), next(gen))

    print("pipeline:", list(square(nums())))
    print("islice:", list(itertools.islice(infinite_sequence(), 5)))
    print("chain:", list(itertools.chain([1, 2], [3, 4])))

    sample.unlink(missing_ok=True)
