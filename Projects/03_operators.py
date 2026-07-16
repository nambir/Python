"""Slide 3 — Operators practice."""

if __name__ == "__main__":
    print("17 / 5 =", 17 / 5)
    print("17 // 5 =", 17 // 5)
    print("17 % 5 =", 17 % 5)
    print("2 ** 8 =", 2 ** 8)

    a = [1, 2]
    b = a
    c = [1, 2]
    print("a is b:", a is b)
    print("a == c:", a == c)
    print("a is c:", a is c)
    print("5 in [1, 2, 5]:", 5 in [1, 2, 5])
    print("5 & 3 =", 5 & 3)

    n = 10
    n += 5
    print("n += 5 ->", n)

    data = ["a", "bb", "ccc"]
    if (count := len(data)) > 2:
        print("walrus count:", count)
