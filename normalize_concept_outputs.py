"""Normalize # OUTPUT sections so they match print(), not commented text."""

from __future__ import annotations

from pathlib import Path


def normalize_example(example: str) -> str:
    lines = example.splitlines()
    out: list[str] = []
    in_output = False
    for line in lines:
        if line.startswith("# OUTPUT"):
            in_output = True
            out.append(line)
            continue
        if line.startswith("# INPUT"):
            in_output = False
            out.append(line)
            continue
        if in_output and line.startswith("# "):
            out.append(line[2:])
        elif in_output and line == "#":
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def rewrite_chunk(name: str) -> int:
    module = __import__(f"concept_examples_chunk_{name}")
    changed = 0
    for key, (example, explanation) in list(module.CHUNK.items()):
        fixed = normalize_example(example)
        if fixed != example:
            changed += 1
        module.CHUNK[key] = (fixed, explanation)

    path = Path(f"concept_examples_chunk_{name}.py")
    lines = [
        '"""Self-contained Review base-concept examples."""',
        "",
        "CHUNK = {",
    ]
    for key in sorted(module.CHUNK):
        example, explanation = module.CHUNK[key]
        lines.append(f"    {key!r}: (")
        lines.append(f"        {example!r},")
        lines.append(f"        {explanation!r},")
        lines.append("    ),")
    lines.append("}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return changed


if __name__ == "__main__":
    for chunk in ("a", "b", "c", "d"):
        count = rewrite_chunk(chunk)
        print(f"{chunk}: normalized {count} examples")
