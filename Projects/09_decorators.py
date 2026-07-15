"""Slide 9 — Decorators practice."""
import time
from functools import wraps


def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__}: {time.time() - start:.3f}s")
        return result

    return wrapper


def log(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"calling {fn.__name__} args={args} kwargs={kwargs}")
        return fn(*args, **kwargs)

    return wrapper


@timer
@log
def slow_work():
    return sum(range(500_000))


if __name__ == "__main__":
    print("result:", slow_work())
