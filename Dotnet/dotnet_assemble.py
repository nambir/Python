"""Build TRAINING_META / CONTENT / BEGINNER / nav maps from the skill catalog.

Rich handcrafted slides (D01, D06) override generated bodies when present.
All other slides follow the D01 teaching pattern:
  subtopic explain → before/after → project story from MyDotnet.md.
"""

from __future__ import annotations

import html
from typing import Any

from slide_code import code
from training_meta import _def

from Dotnet.dotnet_catalog import AREA_TITLES, SKILLS
from Dotnet.dotnet_mydotnet import answer_for
from Dotnet.dotnet_primary import primary_for
from Dotnet import dotnet_rich as rich

# Slide number = index in SKILLS (1-based): D01→1 … D72→72
SLIDE_BY_ID = {s["id"]: i for i, s in enumerate(SKILLS, 1)}
ID_BY_SLIDE = {i: s["id"] for i, s in enumerate(SKILLS, 1)}


def _esc(s: str) -> str:
    return html.escape(s or "", quote=False)


def _esc_pre(s: str) -> str:
    """Escape for step-pre, keep newlines."""
    return html.escape(s or "", quote=False)


def _before_after(
    before: str,
    after: str,
    *,
    before_lbl: str = "Before",
    after_lbl: str = "After",
) -> str:
    return (
        '<div class="mc-row">'
        f'<div class="mc-col mc-bad"><span class="mc-lbl">&#10060; {before_lbl}</span>'
        f'<div class="step-pre">{before}</div></div>'
        f'<div class="mc-col mc-good"><span class="mc-lbl">&#10004; {after_lbl}</span>'
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


def _practice_html(items: list[str], skill_id: str) -> str:
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f"""
<ul class="checklist">
{lis}
</ul>
<a class="file-link" href="Skill_Depth_Matrix_I25054_Sangeetha_Rajendiran_9.csv">Skill matrix {skill_id}</a>
· <a class="file-link" href="MyDotnet.md">MyDotnet answers ({skill_id})</a>
"""


def _project_box(ans: dict | None, sid: str) -> str:
    if not ans:
        return ""
    how = _esc(ans.get("how") or "")
    why = _esc(ans.get("why") or "")
    code_snip = ans.get("code") or ""
    rating = _esc(ans.get("rating") or "")
    parts = [
        f'<div class="callout"><b>My project ({sid}):</b> {_esc(ans.get("title") or "")}</div>',
        f"<p><b>How:</b> {how}</p>" if how else "",
        f"<p><b>Why:</b> {why}</p>" if why else "",
    ]
    if code_snip:
        parts.append(f'<div class="step-pre">{_esc_pre(code_snip)}</div>')
    if rating:
        parts.append(f'<p class="step-result"><b>Self rating:</b> {rating}</p>')
    return "\n".join(p for p in parts if p)


def _how_it_works(label: str, before: str, after: str, concepts: list) -> str:
    """Keyword box explaining the before→after fix (D01 SqlParameter style)."""
    c0 = concepts[0][0] if concepts else "idea"
    c1 = concepts[1][0] if len(concepts) > 1 else "fix"
    return f"""
<div class="keyword-box">
<b>How the fix works — { _esc(label) }</b>
<ol style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li><b>Problem trigger:</b> the Before path hits <code>{_esc(c0)}</code> the wrong way
(see red box).</li>
<li><b>What goes wrong:</b> {_esc_pre(before[:160])}{"…" if len(before) > 160 else ""}</li>
<li><b>After path:</b> apply <code>{_esc(c1)}</code> / the green fix so behavior matches Level-3.</li>
<li><b>What you gain:</b> {_esc_pre(after[:160])}{"…" if len(after) > 160 else ""}</li>
</ol>
</div>
"""


def _subtopic_sections(s: dict[str, Any], ans: dict | None) -> str:
    """One numbered section per concept: explain + before/after."""
    concepts = []
    # Recover concepts from table_rows or def_bullets
    rows = s.get("table_rows") or []
    for row in rows:
        if len(row) >= 2:
            label = re_strip_code(row[0])
            concepts.append((label, row[1]))
    if not concepts:
        for b in s.get("def_bullets") or []:
            # "<b>Label:</b> detail"
            if "</b>" in b:
                label = b.split("</b>", 1)[0].replace("<b>", "").rstrip(":")
                detail = b.split("</b>", 1)[1].lstrip(": ").strip()
                concepts.append((label, detail))
            else:
                concepts.append((b[:40], b))

    mistakes = list(s.get("mistakes") or [])
    # Pad mistakes so each concept can show a before/after
    while len(mistakes) < len(concepts):
        mistakes.append(
            (
                f"{concepts[len(mistakes)][0]} done poorly",
                f"// BEFORE — weak {concepts[len(mistakes)][0]}\n"
                f"// definition only, no project story",
                f"// AFTER — Level-3\n"
                f"// explain {concepts[len(mistakes)][0]} with How/Why from my project",
            )
        )

    parts: list[str] = []
    how = (ans or {}).get("how") or ""
    why = (ans or {}).get("why") or ""

    for i, ((label, detail), mistake) in enumerate(zip(concepts, mistakes), 1):
        _title, bad, good = mistake
        # Prefer MyDotnet project snippet as the green "After" for the first subtopic
        if i == 1 and ans and ans.get("code"):
            good = ans["code"]
            risk = (ans.get("why") or "missing the production pattern")[:140]
            bad = (
                f"// BEFORE — without the project fix\n"
                f"// Risk: {risk}\n"
                f"// definition-only / wrong pattern"
            )
        project_why = ""
        if how and i == 1:
            project_why = f"<p><b>Why it matters in my project:</b> {_esc(how)}</p>"
        elif why and i == 2:
            project_why = f"<p><b>Why it matters in my project:</b> {_esc(why)}</p>"
        elif (ans or {}).get("excel") and i == 3:
            tip = (ans or {})["excel"][0] if (ans or {}).get("excel") else ""
            if tip:
                project_why = f"<p><b>Interview tip:</b> {_esc(tip)}</p>"

        parts.append(
            f"<h3>{i}. {_esc(label)} — full example</h3>"
            f"<p><b>What it means:</b> {detail}</p>"
            f"{project_why}"
            + _before_after(_esc_pre(bad), _esc_pre(good))
            + (
                _how_it_works(label, bad, good, concepts)
                if i == 1
                else f'<p class="step-result"><b>Takeaway:</b> {_esc(label)} — '
                f"explain with a project story, not only a definition.</p>"
            )
        )
    return "\n".join(parts)


def re_strip_code(cell: str) -> str:
    t = cell.replace("<code>", "").replace("</code>", "")
    return html.unescape(t)


def _learn_html(s: dict[str, Any]) -> str:
    sid = s["id"]
    ans = answer_for(sid)
    level3 = _esc(s["level3"])
    item = _esc(s["skill_item"])
    angle = ""
    if ans and ans.get("how"):
        short = ans["how"]
        if len(short) > 140:
            short = short[:137] + "…"
        angle = (
            f' <span style="color:#64748b">(Project angle from MyDotnet: '
            f"{_esc(short)})</span>"
        )

    parts = [
        f"<p>Skill matrix <b>{sid}</b> — {item}.{angle}</p>",
        f'<div class="callout"><b>Level-3 bar:</b> {level3}</div>',
        _table_html(s.get("table_headers") or ["Idea", "Remember"], s.get("table_rows") or []),
        _subtopic_sections(s, ans),
        "<h3>My project story (from MyDotnet.md)</h3>",
        _project_box(ans, sid),
    ]

    # Extra excel bullets as interview checklist
    if ans and ans.get("excel"):
        bullets = "".join(f"<li>{_esc(b)}</li>" for b in ans["excel"][:8])
        parts.append(
            "<h3>Excel / assessor talking points</h3>"
            f'<ul style="margin:6px 0 0 18px;font-size:12px;line-height:1.5">{bullets}</ul>'
        )
    if ans and ans.get("excel_prev"):
        bullets = "".join(f"<li>{_esc(b)}</li>" for b in ans["excel_prev"][:6])
        parts.append(
            "<h3>Previous-project depth (if asked)</h3>"
            f'<ul style="margin:6px 0 0 18px;font-size:12px;line-height:1.5">{bullets}</ul>'
        )

    quiz = list(s.get("quiz") or [])
    # Prefer project-flavored quiz Q1
    if ans and ans.get("how"):
        quiz = [
            (
                f"Where did <b>{sid}</b> show up in your project?",
                _esc(ans["how"]),
            ),
            (
                "What was the Before → After fix?",
                _esc((ans.get("why") or s["level3"])),
            ),
            (
                "What does Level-3 expect?",
                level3,
            ),
        ]
    parts.append(_quiz_html(quiz))

    snippet = s.get("code")
    if snippet:
        parts.append(code(snippet, expected=s.get("expected") or ""))
    elif ans and ans.get("code") and len(ans["code"]) < 1200:
        # Show project snippet in playground when catalog has no runnable demo
        parts.append(
            code(
                "// From MyDotnet.md — project example (may need your namespaces)\n"
                + ans["code"],
                expected="",
            )
        )

    return "\n".join(parts)


def _beginner_for(s: dict[str, Any]) -> dict:
    sid = s["id"]
    ans = answer_for(sid)
    if s.get("steps"):
        steps = s["steps"]
    else:
        steps = []
        rows = s.get("table_rows") or []
        concepts = []
        for row in rows:
            if len(row) >= 2:
                concepts.append((re_strip_code(row[0]), row[1]))
        mistakes = list(s.get("mistakes") or [])
        while len(mistakes) < max(len(concepts), 1):
            idx = len(mistakes)
            lab = concepts[idx][0] if idx < len(concepts) else s["title"]
            mistakes.append(
                (
                    lab,
                    f"// BEFORE — skip {lab}",
                    f"// AFTER — apply {lab} with a project example",
                )
            )

        for i, ((label, detail), mistake) in enumerate(zip(concepts[:4], mistakes[:4]), 1):
            _t, bad, good = mistake
            if i == 1 and ans and ans.get("code"):
                good = ans["code"]
                risk = (ans.get("why") or "missing the production pattern")[:140]
                bad = (
                    f"// BEFORE — without the project fix\n"
                    f"// Risk: {risk}\n"
                    f"// definition-only / wrong pattern"
                )
            body = (
                f"<p><b>What it means:</b> {detail}</p>"
                + _before_after(_esc_pre(bad), _esc_pre(good))
            )
            if i == 1 and ans and ans.get("how"):
                body += (
                    f'<div class="keyword-box"><b>How this maps to my project</b>'
                    f"<ol style=\"margin:6px 0 0 18px;font-size:12px;line-height:1.55\">"
                    f"<li><b>How:</b> {_esc(ans['how'])}</li>"
                    f"<li><b>Why:</b> {_esc(ans.get('why') or '')}</li>"
                    f"<li><b>After code:</b> use the green box / MyDotnet snippet.</li>"
                    f"</ol></div>"
                )
            body += (
                f'<p class="step-result"><b>Takeaway:</b> {_esc(label)} — '
                f"pair the definition with Before → After.</p>"
            )
            steps.append({"title": f"Step {i} — {label} (before/after)", "body": body})

        if ans and ans.get("code"):
            steps.append(
                {
                    "title": f"Step {len(steps) + 1} — Project code (MyDotnet)",
                    "body": (
                        f"<p>Concrete snippet from <code>MyDotnet.md</code> for <b>{sid}</b>:</p>"
                        f'<div class="step-pre">{_esc_pre(ans["code"])}</div>'
                        f'<p class="step-result"><b>Practice:</b> explain this snippet in 30 seconds.</p>'
                    ),
                }
            )
        if not steps:
            steps = [
                {
                    "title": f"Step 1 — What {sid} is about",
                    "body": f"<p>{s['def_intro']}</p>",
                }
            ]

    qa = s.get("interview_qa")
    if not qa:
        qa = []
        if ans and ans.get("how"):
            qa.append(
                {
                    "q": f"Where did you use {s['title']} in your project?",
                    "a": _esc(ans["how"])
                    + (" " + _esc(ans["why"]) if ans.get("why") else ""),
                }
            )
        qa.append(
            {
                "q": f"Explain {s['title']} for an interviewer.",
                "a": s["interview"],
            }
        )
        qa.append(
            {
                "q": "What does Level-3 look like for this skill?",
                "a": _esc(s["level3"]),
            }
        )
        if ans and ans.get("excel"):
            qa.append(
                {
                    "q": "Give your assessor talking points.",
                    "a": " ".join(_esc(b) for b in ans["excel"][:4]),
                }
            )
    return {"steps": steps, "interview_qa": qa}


def _meta_interview(s: dict[str, Any], ans: dict | None) -> str:
    if ans and ans.get("how"):
        parts = [ans["how"]]
        if ans.get("why"):
            parts.append(ans["why"])
        if ans.get("excel"):
            parts.append(ans["excel"][0])
        return " ".join(parts)
    return s["interview"]


def _flow_for(s: dict[str, Any]) -> tuple | None:
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
        ans = answer_for(sid)

        rich_slide = rich.RICH.get(sid)
        primary = primary_for(sid)
        if rich_slide:
            meta[i] = dict(rich_slide["meta"])
            if primary:
                meta[i]["primary"] = primary
            learn = rich_slide["learn"]
            if isinstance(learn, tuple):
                learn = "".join(learn)
            # Keep handcrafted D01/D06 depth, but always attach MyDotnet project story + Excel points
            if "My project story (from MyDotnet.md)" not in learn and ans:
                learn = (
                    learn
                    + "<h3>My project story (from MyDotnet.md)</h3>"
                    + _project_box(ans, sid)
                )
                if ans.get("excel"):
                    bullets = "".join(f"<li>{_esc(b)}</li>" for b in ans["excel"][:8])
                    learn += (
                        "<h3>Excel / assessor talking points</h3>"
                        f'<ul style="margin:6px 0 0 18px;font-size:12px;line-height:1.5">{bullets}</ul>'
                    )
            practice = rich_slide["practice"]
            if "MyDotnet.md" not in practice:
                practice = (
                    practice.rstrip()
                    + f'\n· <a class="file-link" href="MyDotnet.md">MyDotnet answers ({sid})</a>\n'
                )
            content.append((i, rich_slide["title"], learn, practice))
            beginner[i] = rich_slide["beginner"]
            if rich_slide.get("subtopics"):
                subtopics[i] = list(rich_slide["subtopics"])
            if rich_slide.get("flow"):
                flows[i] = rich_slide["flow"]
            if rich_slide.get("diagram"):
                diagrams[i] = rich_slide["diagram"]
            continue

        meta[i] = {
            "definition": _def(s["def_intro"], s["def_bullets"]),
            "interview": _meta_interview(s, ans),
            "skill_id": sid,
            "area": area_title,
        }
        if primary:
            meta[i]["primary"] = primary
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
