"""Slide 15 — Regular Expressions practice."""
import re

TEXT = "Order 123 placed on 2026-06-16. Contact: alice@example.com bob@test.org"


def main() -> None:
    print("digits:", re.findall(r"\d+", TEXT))
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", TEXT)
    if m:
        print("date year:", m.group(1))
    print("masked:", re.sub(r"\d+", "X", TEXT))
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", TEXT)
    print("emails:", emails)


if __name__ == "__main__":
    main()
