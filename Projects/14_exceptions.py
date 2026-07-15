"""Slide 14 — Exception Handling practice."""


class ValidationError(Exception):
    pass


def set_age(age: int) -> int:
    if age < 0:
        raise ValidationError("Age cannot be negative")
    return age


def parse_int(value: str) -> int:
    try:
        return int(value)
    except ValueError as e:
        print(f"Bad input: {e}")
        raise
    finally:
        print("parse_int finished")


if __name__ == "__main__":
    print("ok:", set_age(30))
    try:
        set_age(-1)
    except ValidationError:
        print("caught ValidationError")
    try:
        parse_int("abc")
    except ValueError:
        print("re-raised ValueError preserved")
