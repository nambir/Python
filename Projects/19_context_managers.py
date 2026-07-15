"""Slide 19 — Context Managers practice."""
import time
from contextlib import contextmanager


@contextmanager
def tag(name: str):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


@contextmanager
def timer(label: str):
    start = time.time()
    yield
    print(f"{label}: {time.time() - start:.3f}s")


class Managed:
    def __enter__(self):
        print("setup")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("teardown")
        return False


if __name__ == "__main__":
    with tag("h1"):
        print("Hello")
    with timer("block"):
        sum(range(1_000_000))
    with Managed():
        print("inside managed")
