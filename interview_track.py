"""Build an interview training deck from a skill catalog (Angular / SQL / AWS).

Mirrors Dotnet/dotnet_assemble.py without MyDotnet.md.
"""

from __future__ import annotations

import html
import re
from typing import Any, Callable

from slide_code import code
from training_meta import _def


def skill_entry(
    skill_id: str,
    area: str,
    title: str,
    skill_item: str,
    level3: str,
    subtopics: list[str],
    def_intro: str,
    concepts: list[tuple[str, str]],
    interview: str,
    mistake: tuple[str, str, str],
    code_src: str | None = None,
    expected: str = "",
) -> dict[str, Any]:
    """One consistently structured teaching entry."""
    return {
        "id": skill_id,
        "area": area,
        "title": title,
        "skill_item": skill_item,
        "level3": level3,
        "subtopics": subtopics,
        "def_intro": def_intro,
        "def_bullets": [f"<b>{label}:</b> {detail}" for label, detail in concepts],
        "interview": interview,
        "table_headers": ["Idea", "Remember"],
        "table_rows": [[f"<code>{label}</code>", detail] for label, detail in concepts],
        "mistakes": [mistake],
        "quiz": [
            (
                f"What is the practical purpose of <code>{concepts[0][0]}</code>?",
                concepts[0][1],
            ),
            (
                f"When does <code>{concepts[1][0]}</code> matter?",
                concepts[1][1],
            ),
            (
                "What evidence demonstrates interview-ready skill here?",
                level3,
            ),
        ],
        "practice": [
            f"Explain <code>{concepts[0][0]}</code> with a project example.",
            f"Compare <code>{concepts[1][0]}</code> with an alternative.",
            f"Answer the Interview 5 for: {level3}",
        ],
        "code": code_src,
        "expected": expected,
        "steps": None,
    }


def _esc(s: str) -> str:
    return html.escape(s or "", quote=False)


def _esc_pre(s: str) -> str:
    return html.escape(s or "", quote=False)


def _before_after(before: str, after: str) -> str:
    return (
        '<div class="mc-row">'
        f'<div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Before</span>'
        f'<div class="step-pre">{before}</div></div>'
        f'<div class="mc-col mc-good"><span class="mc-lbl">&#10004; After</span>'
        f'<div class="step-pre">{after}</div></div>'
        "</div>"
    )


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


def _table_html(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return ""
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows
    )
    return f'<h3>Quick reference</h3><table class="data-tbl"><tr>{th}</tr>{body}</table>'


def re_strip_code(cell: str) -> str:
    t = cell.replace("<code>", "").replace("</code>", "")
    return html.unescape(t)


def _five_box() -> str:
    return """
<div class="callout"><b>Interview 5 — answer all five before you mention this in the interview:</b>
<ol style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li><b>What is it?</b></li>
<li><b>Where did you use it?</b> (actual project)</li>
<li><b>Why did you use it?</b> (design decision)</li>
<li><b>How did you implement it?</b> (hands-on)</li>
<li><b>What problem did it solve?</b></li>
</ol>
</div>
"""


def _learn_html(s: dict[str, Any], *, pdf_href: str) -> str:
    sid = s["id"]
    level3 = _esc(s["level3"])
    item = _esc(s["skill_item"])
    concepts: list[tuple[str, str]] = []
    for row in s.get("table_rows") or []:
        if len(row) >= 2:
            concepts.append((re_strip_code(row[0]), row[1]))
    mistakes = list(s.get("mistakes") or [])
    while len(mistakes) < len(concepts):
        lab = concepts[len(mistakes)][0]
        mistakes.append(
            (
                f"{lab} done poorly",
                f"// BEFORE — definition only for {lab}",
                f"// AFTER — project story for {lab}",
            )
        )

    parts = [
        f"<p>Interview prep <b>{sid}</b> — {item}.</p>",
        f'<div class="callout"><b>Interview bar:</b> {level3}</div>',
        _five_box(),
        _table_html(s.get("table_headers") or ["Idea", "Remember"], s.get("table_rows") or []),
    ]
    for i, ((label, detail), mistake) in enumerate(zip(concepts, mistakes), 1):
        _title, bad, good = mistake
        parts.append(
            f"<h3>{i}. {_esc(label)} — full example</h3>"
            f"<p>{detail}</p>"
            + _before_after(_esc_pre(bad), _esc_pre(good))
            + (
                f'<p class="step-result"><b>Takeaway:</b> {_esc(label)} — '
                f"explain with a project story, not only a definition.</p>"
            )
        )
    parts.append(_quiz_html(list(s.get("quiz") or [])))
    snippet = s.get("code")
    if snippet:
        parts.append(code(snippet, expected=s.get("expected") or ""))
    return "\n".join(parts)


def _practice_html(items: list[str], skill_id: str, *, pdf_href: str) -> str:
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f"""
<ul class="checklist">
{lis}
<li>Speak the Interview 5 for <b>{skill_id}</b> out loud (60 seconds).</li>
</ul>
<a class="file-link" href="{pdf_href}">ClientInterviewExpectations.pdf</a>
"""


def _renumber_steps(steps: list[dict]) -> list[dict]:
    out = []
    for i, step in enumerate(steps, 1):
        title = step.get("title") or f"Step {i}"
        title = re.sub(r"^Step\s+\d+\s*[—–-]\s*", f"Step {i} — ", title, count=1)
        if not re.match(r"^Step\s+\d+", title):
            title = f"Step {i} — {title}"
        out.append({**step, "title": title})
    return out


def _beginner_for(s: dict[str, Any]) -> dict:
    steps = list(s.get("steps") or [])
    if not steps:
        concepts: list[tuple[str, str]] = []
        for row in s.get("table_rows") or []:
            if len(row) >= 2:
                concepts.append((re_strip_code(row[0]), row[1]))
        mistakes = list(s.get("mistakes") or [])
        while len(mistakes) < max(len(concepts), 1):
            idx = len(mistakes)
            lab = concepts[idx][0] if idx < len(concepts) else s["title"]
            mistakes.append(
                (lab, f"// BEFORE — skip {lab}", f"// AFTER — apply {lab} with a project example")
            )
        for i, ((label, detail), mistake) in enumerate(zip(concepts[:4], mistakes[:4]), 1):
            _t, bad, good = mistake
            body = (
                f"<p>{detail}</p>"
                + _before_after(_esc_pre(bad), _esc_pre(good))
                + f'<p class="step-result"><b>Takeaway:</b> {_esc(label)} — pair definition with Before → After.</p>'
            )
            steps.append({"title": f"Step {i} — {label} (before/after)", "body": body})
        if not steps:
            steps = [{"title": f"Step 1 — What {s['id']} is about", "body": f"<p>{s['def_intro']}</p>"}]
    steps = list(s.get("prepend_steps") or []) + steps
    steps.extend(s.get("extra_steps") or [])
    steps = _renumber_steps(steps)
    qa = s.get("interview_qa") or [
        {"q": f"Explain {s['title']} for an interviewer.", "a": s["interview"]},
        {"q": "What does interview-ready look like for this skill?", "a": _esc(s["level3"])},
        {
            "q": "Give the Interview 5 in one breath.",
            "a": "What it is, where I used it, why we chose it, how I implemented it, and the problem it solved.",
        },
    ]
    return {"steps": steps, "interview_qa": qa}


def _flow_for(s: dict[str, Any]) -> tuple:
    if s.get("flow"):
        return s["flow"]
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
        "Interview-ready move",
        s["level3"][:160],
        ["project example", "why it mattered", "how you verified"],
    )


def build_from_skills(
    skills: list[dict[str, Any]],
    area_titles: dict[str, str],
    *,
    pdf_href: str = "../ClientInterviewExpectations.pdf",
    primary_fn: Callable[[str], str] | None = None,
) -> dict[str, Any]:
    meta: dict[int, dict] = {}
    content: list[tuple] = []
    beginner: dict[int, dict] = {}
    module_map: dict[int, str] = {}
    subtopics: dict[int, list[str]] = {}
    flows: dict[int, tuple] = {}
    diagrams: dict[int, str] = {}
    section_buckets: dict[str, list[int]] = {k: [] for k in area_titles}

    for i, s in enumerate(skills, 1):
        sid = s["id"]
        area = s["area"]
        area_title = area_titles.get(area, area)
        section_buckets.setdefault(area, []).append(i)
        module_map[i] = area_title
        if s.get("subtopics"):
            subtopics[i] = list(s["subtopics"])
        primary = (primary_fn(sid) if primary_fn else "") or (
            f"<b>{_esc(s['title'])}</b> — {_esc(s['skill_item'])}."
        )
        meta[i] = {
            "definition": _def(s["def_intro"], s["def_bullets"]),
            "interview": s["interview"],
            "skill_id": sid,
            "area": area_title,
            "primary": primary,
        }
        content.append(
            (
                i,
                s["title"],
                _learn_html(s, pdf_href=pdf_href),
                _practice_html(s.get("practice") or [], sid, pdf_href=pdf_href),
            )
        )
        beginner[i] = _beginner_for(s)
        flows[i] = _flow_for(s)

    sections = [(area_titles[a], section_buckets[a]) for a in area_titles if section_buckets.get(a)]
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
