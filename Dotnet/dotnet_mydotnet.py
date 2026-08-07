"""Parse Dotnet/MyDotnet.md into per-skill project answers (How / Why / Code / Excel)."""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

MYDOTNET_PATH = Path(__file__).resolve().parent / "MyDotnet.md"

_SECTION_RE = re.compile(
    r"^## (D\d{2})\s+[—\-]\s+(.+?)\s*$",
    re.MULTILINE,
)
_FIELD_RE = re.compile(
    r"^\*\*(How|Why|Code|Suggested Self Rating|Excel paste(?: - previous project)?):\*\*\s*(.*)$",
    re.MULTILINE,
)


def _split_code_fence(text: str) -> tuple[str, str]:
    """Return (prose_before_fence, code_inside) from a Code block body."""
    m = re.search(r"```(?:csharp|sql|xml|yaml|text|cs)?\n(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if not m:
        return text.strip(), ""
    before = text[: m.start()].strip()
    return before, m.group(1).strip()


def _bullets(block: str) -> list[str]:
    out: list[str] = []
    for line in block.splitlines():
        s = line.strip()
        if s.startswith("- "):
            out.append(s[2:].strip())
    return out


@lru_cache(maxsize=1)
def load_mydotnet(path: str | None = None) -> dict[str, dict]:
    """Return { 'D01': { title, how, why, code, rating, excel, excel_prev }, ... }."""
    p = Path(path) if path else MYDOTNET_PATH
    raw = p.read_text(encoding="utf-8", errors="replace")
    matches = list(_SECTION_RE.finditer(raw))
    result: dict[str, dict] = {}

    for i, m in enumerate(matches):
        sid = m.group(1)
        title = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        body = raw[start:end]

        fields: dict[str, str] = {}
        field_matches = list(_FIELD_RE.finditer(body))
        for j, fm in enumerate(field_matches):
            key = fm.group(1)
            first = fm.group(2).strip()
            f_start = fm.end()
            f_end = field_matches[j + 1].start() if j + 1 < len(field_matches) else len(body)
            rest = body[f_start:f_end].strip()
            fields[key] = (first + ("\n" + rest if rest else "")).strip()

        how = fields.get("How", "").strip()
        why = fields.get("Why", "").strip()
        code_raw = fields.get("Code", "")
        _, code = _split_code_fence(code_raw) if code_raw else ("", "")
        if not code and code_raw and "```" not in code_raw:
            code = code_raw.strip()
            if code.upper() == "N/A (behavioral)" or code == "N/A":
                code = ""

        excel = _bullets(fields.get("Excel paste", ""))
        excel_prev = _bullets(fields.get("Excel paste - previous project", ""))
        rating = fields.get("Suggested Self Rating", "").strip()

        result[sid] = {
            "id": sid,
            "title": title,
            "how": how,
            "why": why,
            "code": code,
            "rating": rating,
            "excel": excel,
            "excel_prev": excel_prev,
        }
    return result


def answer_for(skill_id: str) -> dict | None:
    return load_mydotnet().get(skill_id)
