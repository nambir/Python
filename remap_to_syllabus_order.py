"""One-shot: renumber slides to match Week 1–4 syllabus order (no jumps)."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent

# old slide number -> new sequential syllabus order
OLD_TO_NEW: dict[int, int] = {
    1: 1,  # Intro
    2: 2,  # Setup
    4: 3,  # Workspace
    31: 4,  # PEP
    3: 5,  # Datatypes
    14: 6,  # Typing
    5: 7,  # Operators
    6: 8,  # Flow
    7: 9,  # Comprehensions
    8: 10,  # Functions
    9: 11,  # Builtins
    18: 12,  # Collections
    32: 13,  # Memory/GC
    34: 14,  # Pydantic
    10: 15,  # OOP
    12: 16,  # Descriptors
    13: 17,  # Generators
    11: 18,  # Decorators
    16: 19,  # Exceptions
    20: 20,  # Threading & GIL
    22: 21,  # Async
    33: 22,  # Logging
    19: 23,  # Unit Testing
    17: 24,  # Regex
    15: 25,  # Files
    21: 26,  # Context Manager
    23: 27,  # Venv
    35: 28,  # FastAPI+SQLAlchemy
    24: 29,  # Portfolio
    25: 30,  # pythonBasics
    26: 31,  # Google/Pandas
    27: 32,  # Django
    28: 33,  # Pipecat
    29: 34,  # Project structure
    30: 35,  # C# vs Python
}

assert sorted(OLD_TO_NEW.values()) == list(range(1, 36))
assert len(set(OLD_TO_NEW.values())) == 35


def two_phase_keys(text: str) -> str:
    """Remap `N:` dict keys and `(N,` CONTENT keys without collisions."""
    # Phase 1: old -> 1000+old for keys that change OR stay (all of them)
    # Only remap keys that look like top-level slide keys: start of line + spaces + digits + :
    def phase1(m: re.Match) -> str:
        n = int(m.group(2))
        if n in OLD_TO_NEW:
            return f"{m.group(1)}{1000 + n}:"
        return m.group(0)

    text = re.sub(r"^(\s*)(\d+):", phase1, text, flags=re.M)

    def phase2(m: re.Match) -> str:
        n = int(m.group(2))
        if n >= 1000:
            old = n - 1000
            if old in OLD_TO_NEW:
                return f"{m.group(1)}{OLD_TO_NEW[old]}:"
        return m.group(0)

    text = re.sub(r"^(\s*)(\d+):", phase2, text, flags=re.M)
    return text


def remap_dict_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    path.write_text(two_phase_keys(text), encoding="utf-8")
    print(f"  keys remapped: {path.name}")


def remap_build_training() -> None:
    path = ROOT / "build_training.py"
    text = path.read_text(encoding="utf-8")

    marker = "CONTENT = ["
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit("CONTENT not found")
    body_start = idx + len(marker)
    end_m = re.search(r"\n\]\n\n\ndef build_nav", text[body_start:])
    if not end_m:
        raise SystemExit("CONTENT end not found")
    body_end = body_start + end_m.start()
    body = text[body_start:body_end]

    starts = list(re.finditer(r"^\((\d+),", body, re.M))
    chunks: list[tuple[int, str]] = []
    for i, m in enumerate(starts):
        old = int(m.group(1))
        start = m.start()
        end = starts[i + 1].start() if i + 1 < len(starts) else len(body)
        chunk = body[start:end].rstrip() + ",\n\n"
        new = OLD_TO_NEW[old]
        chunk = re.sub(rf"^\({old},", f"({new},", chunk, count=1)
        chunks.append((new, chunk))
    chunks.sort(key=lambda t: t[0])
    new_body = "\n" + "".join(c for _, c in chunks)
    text = text[:body_start] + new_body + text[body_end:]

    # Remap SLIDE_PROJECT_FILES keys (two-phase on that section only)
    m = re.search(r"SLIDE_PROJECT_FILES\s*=\s*\{", text)
    if m:
        start = m.end() - 1
        depth = 0
        i = start
        in_s = None
        esc = False
        while i < len(text):
            ch = text[i]
            if in_s:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == in_s:
                    in_s = None
            else:
                if ch in ('"', "'"):
                    if text[i : i + 3] in ('"""', "'''"):
                        in_s = text[i : i + 3]
                        i += 2
                    else:
                        in_s = ch
                elif ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        end = i + 1
                        break
            i += 1
        block = text[start:end]
        # parse `N: value,` lines
        entries: dict[int, str] = {}
        for em in re.finditer(r"^\s*(\d+)\s*:\s*(.+?),\s*$", block, re.M):
            old = int(em.group(1))
            if old in OLD_TO_NEW:
                entries[OLD_TO_NEW[old]] = em.group(2)
        lines = ["{"]
        for new in sorted(entries):
            lines.append(f"    {new}: {entries[new]},")
        lines.append("}")
        text = text[:start] + "\n".join(lines) + text[end:]

    week_block = """WEEK_SECTIONS: list[tuple[str, list[int]]] = [
    ("Week 1 — Foundations", list(range(1, 12))),
    ("Week 2 — Collections & OOP", list(range(12, 18))),
    ("Week 3 — Advanced Core", list(range(18, 28))),
    ("Week 4 — Web Stack", [28]),
    ("Real Projects (Python-Set2)", list(range(29, 35))),
    ("Appendix", [35]),
]
"""
    text = re.sub(
        r"WEEK_SECTIONS: list\[tuple\[str, list\[int\]\]\] = \[.*?\n\]\n",
        week_block,
        text,
        count=1,
        flags=re.S,
    )

    # Update learning path + study order tables to sequential numbers
    text = text.replace(
        """<li><b>Week 1</b> — Intro, PEP, datatypes, typing, operators, flow, comprehensions, functions, builtins</li>
<li><b>Week 2</b> — Collections, memory/GC, Pydantic, OOP, descriptors, generators</li>
<li><b>Week 3</b> — Decorators, exceptions, threading/async/GIL, logging, unit tests, regex, files</li>
<li><b>Week 4</b> — FastAPI with SQLAlchemy</li>
<li><b>Projects</b> — Python-Set2 portfolio (slides 24–29)</li>
<li><b>Appendix</b> — C# vs Python (slide 30)</li>""",
        """<li><b>Week 1</b> — slides 1–11: Intro, setup, workspace, PEP, datatypes, typing, operators, flow, comprehensions, functions, builtins</li>
<li><b>Week 2</b> — slides 12–17: Collections, memory/GC, Pydantic, OOP, descriptors, generators</li>
<li><b>Week 3</b> — slides 18–27: Decorators, exceptions, threading/async/GIL, logging, tests, regex, files, context, venv</li>
<li><b>Week 4</b> — slide 28: FastAPI with SQLAlchemy</li>
<li><b>Projects</b> — slides 29–34: Python-Set2 portfolio</li>
<li><b>Appendix</b> — slide 35: C# vs Python</li>""",
    )

    text = text.replace(
        """<tr><td>1</td><td>Intro, PEP, datatypes, typing, operators, flow, comprehensions, functions, builtins</td><td>1, 2, 31, 3, 4, 14, 5, 6, 7, 8, 9</td></tr>
<tr><td>2</td><td>Collections, memory/GC, Pydantic, OOP, descriptors, generators</td><td>18, 32, 34, 10, 12, 13</td></tr>
<tr><td>3</td><td>Decorators, exceptions, threading/async/GIL, logging, tests, regex, files</td><td>11, 16, 20, 22, 33, 19, 17, 15 (+ 21, 23)</td></tr>
<tr><td>4</td><td>FastAPI with SQLAlchemy</td><td>35</td></tr>""",
        """<tr><td>1</td><td>Intro, setup, workspace, PEP, datatypes, typing, operators, flow, comprehensions, functions, builtins</td><td>1–11</td></tr>
<tr><td>2</td><td>Collections, memory/GC, Pydantic, OOP, descriptors, generators</td><td>12–17</td></tr>
<tr><td>3</td><td>Decorators, exceptions, threading/async/GIL, logging, tests, regex, files, context, venv</td><td>18–27</td></tr>
<tr><td>4</td><td>FastAPI with SQLAlchemy</td><td>28</td></tr>""",
    )

    # Fix "35 slides complete" / review slide refs if present
    text = re.sub(
        r"Review slides 1–2, 10, 17, 19, 24–28, and 31–35",
        "Review slides 1–2, 15, 23–24, 29–34, and 4 / 13 / 22 / 28",
        text,
    )
    text = text.replace(
        '<div class="callout"><strong>35 slides complete!</strong>',
        '<div class="callout"><strong>35 slides complete — sequential week order!</strong>',
    )

    # Slide 1 special: n == 1 still intro — diagram injection OK
    # topic_intro checks n == 1 for python_vs_csharp_flow — still correct after remap

    path.write_text(text, encoding="utf-8")
    print("  remapped build_training.py CONTENT (sorted) + PROJECT_FILES + WEEK_SECTIONS")


def remap_audio_files() -> None:
    audio = ROOT / "audio"
    if not audio.exists():
        return
    tmp = audio / "_remap_tmp"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    for old, new in OLD_TO_NEW.items():
        src = audio / f"slide-{old:02d}.mp3"
        if src.exists():
            shutil.copy2(src, tmp / f"slide-{new:02d}.mp3")
    z = audio / "slide-00.mp3"
    if z.exists():
        shutil.copy2(z, tmp / "slide-00.mp3")
    for p in audio.glob("slide-*.mp3"):
        p.unlink()
    for p in tmp.glob("*.mp3"):
        shutil.move(str(p), str(audio / p.name))
    tmp.rmdir()
    print("  remapped audio MP3 filenames")


def main() -> None:
    print("Remapping to sequential syllabus order…")
    for name in (
        "training_beginner.py",
        "training_meta.py",
        "slide_glossary.py",
        "slide_scenarios.py",
        "slide_keyword_deepdives.py",
        "slide_narrations.py",
        "csv_curriculum.py",
    ):
        remap_dict_file(ROOT / name)
    remap_build_training()
    remap_audio_files()
    print("Done.")


if __name__ == "__main__":
    main()
