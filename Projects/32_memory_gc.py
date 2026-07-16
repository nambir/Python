"""Slide 32 — Memory management & garbage collection practice."""
import gc
import sys
import weakref


class Node:
    def __init__(self, name: str):
        self.name = name
        self.ref = None


def demo_refcount() -> None:
    a = [1, 2, 3]
    print("refcount (approx):", sys.getrefcount(a))
    b = a
    print("after b = a:", sys.getrefcount(a))
    del b


def demo_cycle() -> None:
    x = Node("x")
    y = Node("y")
    x.ref = y
    y.ref = x
    del x, y
    collected = gc.collect()
    print("gc.collect() freed objects:", collected)


def demo_weakref() -> None:
    obj = {"key": "value"}
    ref = weakref.ref(obj)
    print("alive:", ref() is not None)
    del obj
    print("after del:", ref())


if __name__ == "__main__":
    demo_refcount()
    demo_cycle()
    demo_weakref()
