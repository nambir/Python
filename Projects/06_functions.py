"""Slide 6 — Python Functions practice."""


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def total(*args, **kwargs) -> None:
    print("args:", args)
    print("kwargs:", kwargs)


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n - 1)


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


if __name__ == "__main__":
    print(greet("Sangeetha"))
    total(1, 2, 3, tax=0.1)
    print("factorial(5):", factorial(5))
    counter = make_counter()
    print("closure:", counter(), counter(), counter())
