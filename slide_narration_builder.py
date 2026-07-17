"""Compose full slide narrations from every content module used in PythonTraining.html."""

from __future__ import annotations

import html as html_module
import re

from build_training import CONTENT, SLIDE_PROJECT_FILES, _CODE_SNIPPETS, python_vs_csharp_flow
from slide_diagrams import diagram_for
from slide_glossary import glossary_for
from slide_keyword_deepdives import keyword_deepdives_for
from slide_real_life import real_life_for
from slide_scenarios import scenarios_for
from training_beginner import BEGINNER_CONTENT
from training_meta import TRAINING_META

_CONTENT_BY_SLIDE: dict[int, tuple[str, str, str]] = {
    n: (title, learn, practice) for n, title, learn, practice in CONTENT
}
_CODE_MARKER = re.compile(r"<!--CODE:(\d+)-->")


def strip_html(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<br\s*/?>", ". ", text, flags=re.I)
    text = re.sub(r"</p>", ". ", text, flags=re.I)
    text = re.sub(r"</li>", ". ", text, flags=re.I)
    text = re.sub(r"</tr>", ". ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html_module.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tts_sanitize(text: str) -> str:
    """Make symbols and code tokens easier for TTS to read aloud."""
    if not text:
        return ""
    text = text.replace("—", " - ")
    text = text.replace("–", " - ")
    text = text.replace("'", "'")
    text = text.replace(""", '"')
    text = text.replace(""", '"')
    text = text.replace("&amp;", " and ")
    text = text.replace("&lt;", " less than ")
    text = text.replace("&gt;", " greater than ")
    text = re.sub(r"__([a-zA-Z_]+)__", r" dunder \1 dunder ", text)
    text = text.replace("->", " returns ")
    text = text.replace("!=", " not equals ")
    text = text.replace("==", " equals ")
    text = text.replace("//", " floor division ")
    text = text.replace("**", " power ")
    text = text.replace("+=", " plus equals ")
    text = text.replace("-=", " minus equals ")
    text = text.replace("*=", " times equals ")
    text = text.replace("/=", " divided by equals ")
    text = re.sub(r"\bNone\b", "None", text)
    text = re.sub(r"\.py\b", " dot py", text)
    text = re.sub(r"\.pyc\b", " dot pyc", text)
    text = re.sub(r"\.cs\b", " dot cs", text)
    text = re.sub(r"\.dll\b", " dot dll", text)
    text = re.sub(r"\.exe\b", " dot exe", text)
    text = re.sub(r"\.venv\b", " dot venv", text)
    text = re.sub(r"\.toml\b", " dot toml", text)
    text = re.sub(r"\.txt\b", " dot txt", text)
    text = re.sub(r"\.md\b", " dot md", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def glossary_to_speech(html: str) -> str:
    if not html:
        return ""
    rows: list[str] = []
    for match in re.finditer(r"<tr><td>(.*?)</td><td>(.*?)</td>", html, re.S | re.I):
        term = strip_html(match.group(1))
        meaning = strip_html(match.group(2))
        if not term or term.lower() in {"term", "trait", "step", "command", "type", "wrong order"}:
            continue
        rows.append(f"{term}: {meaning}")
    if rows:
        return "Key terms. " + ". ".join(rows)
    plain = strip_html(html)
    return f"Key terms. {plain}" if plain else ""


def code_to_speech(raw: str) -> str:
    if not raw.strip():
        return ""
    spoken: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("# ──"):
            title = stripped.strip("# ─ ").strip()
            if title:
                spoken.append(title)
            continue
        if stripped.startswith("#"):
            spoken.append(stripped.lstrip("# ").strip())
            continue
        spoken.append(stripped)
    if not spoken:
        return ""
    return "Code example. " + ". ".join(spoken)


def split_learn_for_speech(learn: str) -> tuple[str, str]:
    notes_parts: list[str] = []
    code_parts: list[str] = []
    chunks = _CODE_MARKER.split(learn)
    for i, chunk in enumerate(chunks):
        if i % 2 == 0:
            notes_parts.append(chunk)
        else:
            idx = int(chunk)
            if 0 <= idx < len(_CODE_SNIPPETS):
                code_parts.append(code_to_speech(_CODE_SNIPPETS[idx]))
    return strip_html("".join(notes_parts)), " ".join(p for p in code_parts if p)


def practice_to_speech(practice: str) -> str:
    plain = strip_html(practice)
    if not plain:
        return ""
    return f"Practice checklist. {plain}"


def project_files_to_speech(n: int) -> str:
    entries = SLIDE_PROJECT_FILES.get(n)
    if not entries:
        return ""
    files = ", ".join(fname for fname, _cmd in entries)
    cmds = [cmd for _fname, cmd in entries if cmd]
    parts = [f"Practice files in Projects folder: {files}."]
    if cmds:
        parts.append(f"Run with: {cmds[0]}.")
    return " ".join(parts)


def compose_narration(n: int) -> str:
    title, learn, practice = _CONTENT_BY_SLIDE.get(n, (f"Slide {n}", "", ""))
    parts: list[str] = [tts_sanitize(strip_html(title)) + "."]

    meta = TRAINING_META.get(n, {})
    if meta.get("definition"):
        parts.append(tts_sanitize(meta["definition"]))

    glossary = glossary_to_speech(glossary_for(n))
    if glossary:
        parts.append(tts_sanitize(glossary))

    real_life = strip_html(real_life_for(n))
    if real_life:
        parts.append("Real-life example. " + tts_sanitize(real_life))

    if n == 1:
        diagram = strip_html(python_vs_csharp_flow())
    else:
        diagram = strip_html(diagram_for(n))
    if diagram:
        parts.append("Concept diagram. " + tts_sanitize(diagram))

    beginner = BEGINNER_CONTENT.get(n, {})
    for step in beginner.get("steps", []):
        parts.append(
            tts_sanitize(strip_html(step["title"]))
            + ". "
            + tts_sanitize(strip_html(step["body"]))
        )

    deepdives = strip_html(keyword_deepdives_for(n))
    if deepdives:
        parts.append("Keyword deep dive. " + tts_sanitize(deepdives))

    learn_notes, learn_code = split_learn_for_speech(learn)
    if learn_notes:
        parts.append("Main concepts. " + tts_sanitize(learn_notes))
    if learn_code:
        parts.append(tts_sanitize(learn_code))

    scenarios = strip_html(scenarios_for(n))
    if scenarios:
        parts.append("Scenarios — when to use which. " + tts_sanitize(scenarios))

    practice_text = practice_to_speech(practice)
    if practice_text:
        parts.append(tts_sanitize(practice_text))

    project_text = project_files_to_speech(n)
    if project_text:
        parts.append(tts_sanitize(project_text))

    for qa in beginner.get("interview_qa", []):
        parts.append(
            "Interview question: "
            + tts_sanitize(strip_html(qa["q"]))
            + " Answer: "
            + tts_sanitize(strip_html(qa["a"]))
        )

    if meta.get("interview"):
        parts.append(
            "How to explain in interview: " + tts_sanitize(meta["interview"])
        )

    return " ".join(p for p in parts if p)
