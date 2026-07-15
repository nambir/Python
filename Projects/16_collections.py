"""Slide 16 — Python Collections practice."""
from collections import Counter, defaultdict, deque, namedtuple

WORDS = ["apple", "banana", "apple", "cherry", "banana", "apple"]


def main() -> None:
    print("Counter:", Counter(WORDS))

    groups = defaultdict(list)
    for item, category in [("apple", "fruit"), ("carrot", "veg"), ("banana", "fruit")]:
        groups[category].append(item)
    print("defaultdict:", dict(groups))

    dq = deque([1, 2, 3])
    dq.appendleft(0)
    print("deque:", list(dq))

    Point = namedtuple("Point", ["x", "y"])
    p = Point(10, 20)
    print("namedtuple:", p, p.x, p.y)


if __name__ == "__main__":
    main()
