"""Slide 10 — Functions + functional programming ideas (GFG)."""


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def add(x: int, y: int) -> int:
    """Pure function — same inputs → same output, no side effects."""
    return x + y


_total = 0


def add_impure(x: int) -> int:
    global _total
    _total += x
    return _total


def apply_twice(fn, value):
    """Higher-order — takes a function as argument."""
    return fn(fn(value))


def total(*args, **kwargs) -> None:
    print("args:", args)
    print("kwargs:", kwargs)


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


def make_multiplier(n: int):
    def multiply(x: int) -> int:
        return x * n

    return multiply


if __name__ == "__main__":
    print(greet("Sangeetha"))
    print("pure add:", add(2, 3), add(2, 3))
    print("impure:", add_impure(5), add_impure(5))
    print("apply_twice:", apply_twice(lambda n: n + 1, 5))
    total(1, 2, 3, tax=0.1)
    print("factorial(5):", factorial(5))
    print("closure *3:", make_multiplier(3)(10))
