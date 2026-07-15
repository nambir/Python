"""Slide 2 — Setup & Run Python on Windows."""
import sys


def main() -> None:
    print("Python executable:", sys.executable)
    print("Version:", sys.version.split()[0])
    print()
    print("Run this file:")
    print("  python Projects/00_windows_setup.py")
    print()
    print("Other ways to run Python:")
    print("  python              # REPL")
    print("  python hello.py     # script")
    print("  py -3.12 script.py  # Windows launcher")


if __name__ == "__main__":
    main()
