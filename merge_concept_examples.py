"""Merge concept_examples_chunk_*.py into python_review_concept_examples.py."""

from __future__ import annotations

from pathlib import Path

from concept_examples_chunk_a import CHUNK as A
from concept_examples_chunk_b import CHUNK as B
from concept_examples_chunk_c import CHUNK as C
from concept_examples_chunk_d import CHUNK as D
from python_review_content import QUESTIONS

OUT = Path(__file__).parent / "python_review_concept_examples.py"

EXPECTED = sorted({c for q in QUESTIONS for c in (q.get("base_concepts") or [])})


def _py_str(text: str) -> str:
    return repr(text)


def main() -> None:
    merged = {}
    for chunk in (A, B, C, D):
        overlap = set(merged) & set(chunk)
        if overlap:
            raise SystemExit(f"Duplicate keys across chunks: {sorted(overlap)}")
        merged.update(chunk)

    missing = [k for k in EXPECTED if k not in merged]
    extra = sorted(set(merged) - set(EXPECTED))
    if missing:
        raise SystemExit(f"Missing concepts: {missing}")
    if extra:
        raise SystemExit(f"Unexpected concepts: {extra}")

    lines = [
        '"""Complete Review base-concept examples with print + matching OUTPUT."""',
        "",
        "CONCEPT_EXAMPLES: dict[str, tuple[str, str]] = {",
    ]
    for name in sorted(merged):
        example, explanation = merged[name]
        lines.append(f"    {_py_str(name)}: (")
        lines.append(f"        {_py_str(example)},")
        lines.append(f"        {_py_str(explanation)},")
        lines.append("    ),")
    lines.extend(
        [
            "}",
            "",
            "",
            "def lookup_concept(name: str) -> tuple[str, str]:",
            '    """Return (example_with_input_output, explanation); fallback if unknown."""',
            "    if name in CONCEPT_EXAMPLES:",
            "        return CONCEPT_EXAMPLES[name]",
            "    return (",
            '        f"# INPUT\\nprint({name!r})\\n\\n# OUTPUT\\n{name}",',
            '        f"Core idea for this question: {name}.",',
            "    )",
            "",
        ]
    )
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} with {len(merged)} concepts")


if __name__ == "__main__":
    main()
