"""Slide 7 — Built-in Functions practice."""
from functools import reduce

nums = [1, 2, 3, 4]

if __name__ == "__main__":
    print("map:", list(map(lambda x: x * 2, nums)))
    print("filter:", list(filter(lambda x: x % 2 == 0, nums)))
    print("reduce:", reduce(lambda a, b: a + b, nums))
    print("zip dict:", dict(zip(["a", "b"], [1, 2])))
    print("sorted tuples:", sorted([(1, "z"), (2, "a")], key=lambda t: t[1]))
    print("max:", max(nums), "min:", min(nums))
    for i, v in enumerate(["a", "b"]):
        print("enumerate:", i, v)
