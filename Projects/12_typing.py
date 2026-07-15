"""Slide 12 — Typing practice."""
from typing import List, Optional, Union


def greet(name: str) -> str:
    return f"Hello, {name}"


def find_user(user_id: int) -> Optional[dict]:
    if user_id < 0:
        return None
    return {"id": user_id, "name": "Alice"}


def process(items: Union[List[int], List[str]]) -> int:
    return len(items)


if __name__ == "__main__":
    print(greet("Python"))
    print(find_user(1))
    print(process([1, 2, 3]))
    print("Run static check: mypy Projects/12_typing.py")
