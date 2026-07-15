"""Slide 11 — Generators & Iterators practice."""
import itertools


def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


class CountUp:
    def __init__(self, max_n: int):
        self.n = 0
        self.max_n = max_n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max_n:
            raise StopIteration
        self.n += 1
        return self.n


if __name__ == "__main__":
    print("countdown:", list(countdown(3)))
    print("CountUp:", list(CountUp(4)))
    print("islice:", list(itertools.islice(countdown(10), 3)))
    print("chain:", list(itertools.chain([1, 2], [3, 4])))
