"""Validate that every Review base-concept example prints its shown output."""

from __future__ import annotations

import contextlib
import io

from python_review_concept_examples import CONCEPT_EXAMPLES
from python_review_content import QUESTIONS


def _blocks(example: str) -> list[tuple[str, str]]:
    """Return each (# INPUT code, # OUTPUT text) pair."""
    lines = example.splitlines()
    blocks: list[tuple[str, str]] = []
    index = 0

    while index < len(lines):
        while index < len(lines) and not lines[index].startswith("# INPUT"):
            index += 1
        if index == len(lines):
            break

        input_start = index + 1
        index = input_start
        while index < len(lines) and not lines[index].startswith("# OUTPUT"):
            index += 1
        if index == len(lines):
            raise ValueError("an # INPUT section has no # OUTPUT section")

        code = "\n".join(lines[input_start:index]).strip()
        output_start = index + 1
        index = output_start
        while index < len(lines) and not lines[index].startswith("# INPUT"):
            index += 1
        expected = "\n".join(lines[output_start:index]).strip()
        blocks.append((code, expected))

    return blocks


def _normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def validate() -> list[str]:
    """Return human-readable validation failures."""
    failures: list[str] = []
    used = {concept for question in QUESTIONS for concept in question.get("base_concepts", [])}

    missing = sorted(used - CONCEPT_EXAMPLES.keys())
    extra = sorted(CONCEPT_EXAMPLES.keys() - used)
    if missing:
        failures.append(f"Missing concepts: {missing}")
    if extra:
        failures.append(f"Unused concepts: {extra}")

    for name in sorted(used):
        example, explanation = CONCEPT_EXAMPLES[name]
        if not explanation.strip():
            failures.append(f"{name}: explanation is empty")
        if "print(" not in example:
            failures.append(f"{name}: no print(...) call")

        try:
            blocks = _blocks(example)
        except ValueError as error:
            failures.append(f"{name}: {error}")
            continue

        if not blocks:
            failures.append(f"{name}: no # INPUT / # OUTPUT block")
            continue

        for number, (code, expected) in enumerate(blocks, 1):
            if not code:
                failures.append(f"{name} block {number}: input code is empty")
                continue
            if not expected:
                failures.append(f"{name} block {number}: expected output is empty")
                continue

            stream = io.StringIO()
            namespace: dict[str, object] = {}
            try:
                with contextlib.redirect_stdout(stream):
                    exec(compile(code, f"<concept:{name}:{number}>", "exec"), namespace)
            except Exception as error:  # examples must catch errors they teach
                failures.append(
                    f"{name} block {number}: raised "
                    f"{type(error).__name__}: {error}"
                )
                continue

            actual = _normalize(stream.getvalue())
            wanted = _normalize(expected)
            if actual != wanted:
                failures.append(
                    f"{name} block {number}: output mismatch\n"
                    f"  expected: {wanted!r}\n"
                    f"  actual:   {actual!r}"
                )

    return failures


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n\n".join(problems))
        raise SystemExit(1)
    print(f"Validated {len(CONCEPT_EXAMPLES)} concepts: all printed outputs match.")
