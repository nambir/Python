"""Slide 5 — Comprehensions practice."""
import sys

squares = [n * n for n in range(6)]
evens = [n for n in range(10) if n % 2 == 0]
unique = {c.lower() for c in "Hello"}
word_len = {w: len(w) for w in ["hi", "hello"]}
gen = (n * n for n in range(1_000_000))

if __name__ == "__main__":
    print("squares:", squares)
    print("evens:", evens)
    print("unique:", unique)
    print("word_len:", word_len)
    print("next(gen):", next(gen))
    print("list size vs generator:", sys.getsizeof(squares), sys.getsizeof(gen))
