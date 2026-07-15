"""Slide 13 — File Operations practice."""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
TEXT_FILE = DATA_DIR / "sample.txt"
JSON_FILE = DATA_DIR / "sample.json"


def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)

    TEXT_FILE.write_text("Hello\nPython Training\n", encoding="utf-8")
    print("text lines:")
    for line in TEXT_FILE.read_text(encoding="utf-8").splitlines():
        print(" ", line)

    payload = {"name": "Alice", "score": 95}
    JSON_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print("json:", json.loads(JSON_FILE.read_text(encoding="utf-8")))

    py_files = list(Path(__file__).parent.glob("*.py"))
    print(f"found {len(py_files)} .py files in Projects/")


if __name__ == "__main__":
    main()
