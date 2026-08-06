"""Build TRAINING_META / CONTENT / BEGINNER / nav maps from the skill catalog.

Rich handcrafted slides (D01, D06) override generated bodies when present.
"""

from __future__ import annotations

import html
from typing import Any

from slide_code import code
from training_meta import _def

from Dotnet.dotnet_catalog import AREA_TITLES, SKILLS
from Dotnet import dotnet_rich as rich

# Slide number = index in SKILLS (1-based): D01→1 … D60→60
SLIDE_BY_ID = {s["id"]: i for i, s in enumerate(SKILLS, 1)}
ID_BY_SLIDE = {i: s["id"] for i, s in enumerate(SKILLS, 1)}


def _esc(s: str) -> str:
    return html.escape(s, quote=False)


def _quiz_html(quiz: list[tuple[str, str]]) -> str:
    parts = ['<h3>Self-check quiz</h3><div class="quiz-box">']
    for i, (q, a) in enumerate(quiz, 1):
        parts.append(
            f'<div class="quiz-q"><b>Q{i}.</b> {q}'
            f'<details class="quiz-ans"><summary>Show answer</summary>'
            f'<div class="quiz-reveal">{a}</div></details></div>'
        )
    parts.append("</div>")
    return "".join(parts)


def _mistakes_html(mistakes: list[tuple[str, str, str]]) -> str:
    if not mistakes:
        return ""
    parts = ["<h3>Common mistakes</h3>"]
    for i, (title, bad, good) in enumerate(mistakes, 1):
        parts.append(
            f'<div class="mistake-box"><span class="mistake-title">&#10060; Mistake {i} &mdash; {_esc(title)}</span>'
            f'<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span>'
            f'<div class="step-pre">{bad}</div></div>'
            f'<div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span>'
            f'<div class="step-pre">{good}</div></div></div></div>'
        )
    return "".join(parts)


def _table_html(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return ""
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows
    )
    return f'<h3>Quick reference</h3><table class="data-tbl"><tr>{th}</tr>{body}</table>'


def _practice_html(items: list[str], skill_id: str) -> str:
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f"""
<ul class="checklist">
{lis}
</ul>
<a class="file-link" href="Skill_Depth_Matrix_I25054_Sangeetha_Rajendiran_9.csv">Skill matrix {skill_id}</a>
"""


def _learn_html(s: dict[str, Any]) -> str:
    sid = s["id"]
    level3 = _esc(s["level3"])
    item = _esc(s["skill_item"])
    parts = [
        f"<p>Skill matrix <b>{sid}</b> — {item}</p>",
        f'<div class="callout"><b>Level-3 bar:</b> {level3}</div>',
        _table_html(s.get("table_headers") or ["Idea", "Remember"], s.get("table_rows") or []),
        _mistakes_html(s.get("mistakes") or []),
        _quiz_html(s.get("quiz") or []),
    ]
    snippet = s.get("code")
    if snippet:
        parts.append(code(snippet, expected=s.get("expected") or ""))
    return "\n".join(parts)


def _beginner_for(s: dict[str, Any]) -> dict:
    sid = s["id"]
    steps = s.get("steps")
    if not steps:
        bullets = "".join(f"<li>{b}</li>" for b in s["def_bullets"])
        steps = [
            {
                "title": f"Step 1 — What {sid} is about",
                "body": (
                    f"<p>{s['def_intro']}</p><ul style=\"margin:6px 0 0 18px\">{bullets}</ul>"
                ),
            },
            {
                "title": "Step 2 — What a Level-3 answer sounds like",
                "body": (
                    f"<p>The skill matrix expects you to demonstrate:</p>"
                    f'<div class="step-pre">{_esc(s["level3"])}</div>'
                    f'<p class="step-result"><b>Practice:</b> say this out loud in under 60 seconds '
                    f"with one concrete project example.</p>"
                ),
            },
            {
                "title": "Step 3 — Self-check",
                "body": (
                    "<ul style=\"margin:6px 0 0 18px\">"
                    + "".join(f"<li>{p}</li>" for p in (s.get("practice") or ["Explain this skill with one example"]))
                    + "</ul>"
                ),
            },
        ]
    qa = s.get("interview_qa") or [
        {"q": f"Explain {s['title']} for an interviewer.", "a": s["interview"]},
        {
            "q": "What does Level-3 look like for this skill?",
            "a": _esc(s["level3"]),
        },
        {
            "q": "Name one common mistake.",
            "a": (s.get("mistakes") or [("Skipping depth", "shallow answer", "project story")])[0][0]
            if s.get("mistakes")
            else "Giving a definition without a project story.",
        },
    ]
    return {"steps": steps, "interview_qa": qa}


def _flow_for(s: dict[str, Any]) -> tuple | None:
    if s.get("flow"):
        return s["flow"]
    # Generic decision flow from subtopics
    subs = s.get("subtopics") or ["Core idea", "Tradeoff", "Verify"]
    qs = []
    labels = ["key", "dd", "cm"]
    for i, sub in enumerate(subs[:3]):
        qs.append(
            (
                f"Does this situation involve: {sub}?",
                f"Apply: {sub}",
                f"Use the {s['title']} lens — relate it back to {_esc(s['level3'][:120])}.",
                [sub[:40]],
                labels[i % 3],
            )
        )
    return (
        f"I am facing a {s['title']} question",
        f"Skill {s['id']} — decide with a story, not a definition dump",
        qs,
        "Level-3 move",
        s["level3"][:160],
        ["project example", "why it mattered", "how you verified"],
    )


def build_all() -> dict[str, Any]:
    meta: dict[int, dict] = {}
    content: list[tuple] = []
    beginner: dict[int, dict] = {}
    module_map: dict[int, str] = {}
    subtopics: dict[int, list[str]] = {}
    flows: dict[int, tuple] = {}
    diagrams: dict[int, str] = {}

    section_buckets: dict[str, list[int]] = {a: [] for a in AREA_TITLES}

    for i, s in enumerate(SKILLS, 1):
        sid = s["id"]
        area_key = s["area"]
        area_title = AREA_TITLES[area_key]
        section_buckets[area_key].append(i)
        module_map[i] = area_title
        subtopics[i] = list(s.get("subtopics") or [])

        # Rich overrides (full slide bodies)
        rich_slide = rich.RICH.get(sid)
        if rich_slide:
            meta[i] = rich_slide["meta"]
            content.append((i, rich_slide["title"], rich_slide["learn"], rich_slide["practice"]))
            beginner[i] = rich_slide["beginner"]
            if rich_slide.get("flow"):
                flows[i] = rich_slide["flow"]
            if rich_slide.get("diagram"):
                diagrams[i] = rich_slide["diagram"]
            continue

        meta[i] = {
            "definition": _def(s["def_intro"], s["def_bullets"]),
            "interview": s["interview"],
            "skill_id": sid,
            "area": area_title,
        }
        content.append(
            (
                i,
                s["title"],
                _learn_html(s),
                _practice_html(s.get("practice") or [], sid),
            )
        )
        beginner[i] = _beginner_for(s)
        fl = _flow_for(s)
        if fl:
            flows[i] = fl

    sections = [(AREA_TITLES[a], section_buckets[a]) for a in AREA_TITLES if section_buckets[a]]

    return {
        "TRAINING_META": meta,
        "CONTENT": content,
        "BEGINNER_CONTENT": beginner,
        "MODULE_MAP": module_map,
        "SUBTOPICS": subtopics,
        "SECTIONS": sections,
        "FLOWS": flows,
        "DIAGRAMS": diagrams,
    }


_BUILT = build_all()
TRAINING_META = _BUILT["TRAINING_META"]
CONTENT = _BUILT["CONTENT"]
BEGINNER_CONTENT = _BUILT["BEGINNER_CONTENT"]
MODULE_MAP = _BUILT["MODULE_MAP"]
SUBTOPICS = _BUILT["SUBTOPICS"]
SECTIONS = _BUILT["SECTIONS"]
FLOWS = _BUILT["FLOWS"]
DIAGRAMS = _BUILT["DIAGRAMS"]
