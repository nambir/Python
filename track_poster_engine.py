"""Logging-style visual guides: numbered color panels, mixed visuals per slide."""

from __future__ import annotations

import html as html_mod
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from track_poster_plans import (
    COMPARE_EXTRA,
    LEVEL_SETS,
    PANEL_TITLE,
    grid_for,
    widgets_for,
)
from track_visual_flows import FLOW_BY_ID, compare_pair

FONT = "Segoe UI,Arial,sans-serif"
MONO = "Consolas,Menlo,monospace"
PAGE, INK, MUTED, NAVY = "#ffffff", "#0f172a", "#475569", "#1e3a5f"

TRACK_LABEL = {"dotnet": ".NET", "angular": "Angular", "sql": "SQL Server", "aws": "AWS"}

PANEL_INK = ["#2563eb", "#16a34a", "#4f46e5", "#7c3aed", "#ea580c", "#dc2626"]
PANEL_FILL = ["#eff6ff", "#f0fdf4", "#eef2ff", "#f5f3ff", "#fff7ed", "#fef2f2"]

CS_TABLE = {
    "angular": [
        ("Angular", "C# cousin"),
        ("Component", "Razor / UserControl"),
        ("@Input / @Output", "parameters / events"),
        ("Interceptor", "DelegatingHandler"),
        ("CanActivate", "[Authorize] still required"),
        ("Observable", "IAsyncEnumerable / IObservable"),
    ],
    "sql": [
        ("SQL", "C# / EF cousin"),
        ("JOIN", "LINQ Join / Include"),
        ("Stored proc", "FromSqlInterpolated"),
        ("Index / plan", "covering index + actual plan"),
        ("BEGIN TRAN", "IDbContextTransaction"),
        ("Isolation", "TransactionScope / isolation enum"),
    ],
    "aws": [
        ("AWS", "C# cousin"),
        ("API Gateway", "reverse proxy + JWT"),
        ("ECS task", "one process recipe"),
        ("ECS service", "desired replica count"),
        ("IAM role", "task identity — not the SPA user"),
        ("ALB health", "/health on Kestrel"),
    ],
    "dotnet": [
        (".NET idea", "Say it this way"),
        ("Interface", "the contract callers depend on"),
        ("Scoped", "one instance per HTTP request"),
        ("SaveChanges", "the unit of work"),
        ("Middleware", "runs in, then unwinds out"),
        ("ProblemDetails", "stable API error shape"),
    ],
}


def _plain(text: str) -> str:
    s = re.sub(r"<[^>]+>", " ", text or "")
    s = html_mod.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def _xml(text: str) -> str:
    return (
        (text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _slug(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (title or "").lower()).strip("-")
    return s[:48] or "topic"


def _wrap(text: str, width: int, max_lines: int) -> list[str]:
    words = (text or "").split()
    lines: list[str] = []
    cur = ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if len(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
            if len(lines) >= max_lines:
                break
    if cur and len(lines) < max_lines:
        lines.append(cur)
    if len(lines) == max_lines and words:
        last = lines[-1]
        if not last.endswith("…") and len(" ".join(words)) > width * max_lines:
            lines[-1] = last[: max(0, width - 1)].rstrip() + "…"
    return lines or [""]


def _t(x, y, text, *, size, fill, weight=600, anchor="start", family=FONT) -> str:
    return (
        f'<text x="{x:.0f}" y="{y:.0f}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
        f'text-anchor="{anchor}" font-family="{family}">{_xml(text)}</text>'
    )


def _ml(x, y, lines, *, size, fill, weight=500, anchor="start") -> str:
    parts = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else int(size * 1.2)
        parts.append(f'<tspan x="{x:.0f}" dy="{dy}">{_xml(line)}</tspan>')
    return (
        f'<text x="{x:.0f}" y="{y:.0f}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
        f'text-anchor="{anchor}" font-family="{FONT}">{"".join(parts)}</text>'
    )


def _rect(x, y, w, h, *, fill, stroke=None, sw=1.5, rx=10) -> str:
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}"{st}/>'


def _circle(cx, cy, r, *, fill, stroke=None) -> str:
    st = f' stroke="{stroke}" stroke-width="2"' if stroke else ""
    return f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{fill}"{st}/>'


def _arrow(x1, y1, x2, y2, color="#64748b") -> str:
    return (
        f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
        f'stroke="{color}" stroke-width="2.2" marker-end="url(#arrow)"/>'
    )


def _concepts(skill: dict[str, Any]) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for row in skill.get("table_rows") or []:
        if len(row) >= 2:
            out.append((_plain(row[0]), _plain(row[1])))
    return out[:6]


def _code_lines(skill: dict[str, Any], n: int = 8) -> list[str]:
    raw = skill.get("code") or ""
    lines = [ln.rstrip() for ln in str(raw).splitlines() if ln.strip() or ln == ""]
    lines = [ln for ln in str(raw).splitlines()]
    keep = [ln.rstrip() for ln in lines if ln.strip()]
    if not keep:
        return ["# walk the diagram — no sample on this slide"]
    return [ln[:56] for ln in keep[:n]]


def _mistake(skill: dict[str, Any]) -> tuple[str, str, str]:
    m = (skill.get("mistakes") or [None])[0]
    if not m or len(m) < 3:
        return ("Weak answer", "Definition only", "Project story + evidence")
    return (_plain(m[0]), _plain(m[1]), _plain(m[2]))


def _flow(skill: dict[str, Any]) -> list[str]:
    sid = skill.get("id") or ""
    if sid in FLOW_BY_ID:
        return list(FLOW_BY_ID[sid])
    return [c[0][:20] for c in _concepts(skill)[:4]] or ["Step 1", "Step 2", "Step 3", "Step 4"]


@dataclass
class P:
    sid: str
    title: str
    intro: str
    track: str
    label: str
    concepts: list[tuple[str, str]]
    headers: list[str]
    rows: list[list[str]]
    flow: list[str]
    code: list[str]
    expected: str
    bad_t: str
    bad: str
    good: str
    pick: str
    practice: list[str]
    pair: tuple[str, str, str, str] | None
    rotate: int


def _ctx(skill: dict[str, Any], track: str, n: int) -> P:
    sid = skill.get("id") or f"S{n:02d}"
    bt, bad, good = _mistake(skill)
    pair = compare_pair(sid)
    return P(
        sid=sid,
        title=_plain(skill.get("title") or f"Slide {n}"),
        intro=_plain(skill.get("def_intro") or ""),
        track=track,
        label=TRACK_LABEL.get(track, track.upper()),
        concepts=_concepts(skill),
        headers=[_plain(h) for h in (skill.get("table_headers") or ["Idea", "Remember"])],
        rows=[[_plain(c) for c in r] for r in (skill.get("table_rows") or [])],
        flow=_flow(skill),
        code=_code_lines(skill),
        expected=_plain(skill.get("expected") or skill.get("level3") or ""),
        bad_t=bt,
        bad=bad,
        good=good,
        pick=_plain(skill.get("level3") or ""),
        practice=[_plain(x) for x in (skill.get("practice") or [])][:4],
        pair=pair,
        rotate=n,
    )


def _panel(x, y, w, h, n, title, ink, fill) -> str:
    return (
        _rect(x, y, w, h, fill=fill, stroke=ink, sw=2, rx=12)
        + _rect(x, y, 7, h, fill=ink, stroke=None, rx=0)
        + _circle(x + 28, y + 22, 12, fill=ink)
        + _t(x + 28, y + 26, str(n), size=12, fill="#fff", weight=800, anchor="middle")
        + _t(x + 46, y + 27, title[:42], size=13, fill=ink, weight=800)
    )


def _caption(x, y, w, text: str) -> str:
    return _ml(x, y, _wrap(text, max(18, int(w / 7.2)), 2), size=11, fill=MUTED)


def _w_table(x, y, w, h, p: P) -> str:
    extra = COMPARE_EXTRA.get(p.sid)
    if extra:
        headers = list(extra[0])
        rows = [list(r) for r in extra[1:]]
    else:
        headers = p.headers[:3] or ["Idea", "Remember"]
        rows = p.rows[:5] or [[a, b] for a, b in p.concepts[:5]]
    cols = max(2, min(3, len(headers)))
    headers = headers[:cols]
    cw = w / cols
    rh = min(28, max(22, (h - 8) / max(2, len(rows) + 1)))
    parts = [_rect(x, y, w, rh, fill=NAVY, stroke=None, rx=6)]
    for i, hd in enumerate(headers):
        parts.append(_t(x + i * cw + 6, y + rh * 0.7, hd[:18], size=10, fill="#fff", weight=700))
    for r, row in enumerate(rows[:6]):
        yy = y + rh * (r + 1)
        bg = "#ffffff" if r % 2 == 0 else "#e2e8f0"
        parts.append(_rect(x, yy, w, rh, fill=bg, stroke="#cbd5e1", sw=0.8, rx=0))
        for i in range(cols):
            cell = row[i] if i < len(row) else ""
            parts.append(_t(x + i * cw + 6, yy + rh * 0.7, _plain(cell)[:20], size=10, fill=INK, weight=500))
    return "".join(parts)


def _w_levels(x, y, w, h, p: P) -> str:
    rows = LEVEL_SETS.get(p.sid)
    if not rows:
        rows = [(lab, PANEL_INK[i % 6], det[:40]) for i, (lab, det) in enumerate(p.concepts[:4] or [(f, "") for f in p.flow])]
        rows = [(a, b, c) for a, b, c in rows]
    n = max(1, min(5, len(rows)))
    rh = (h - 8 * (n - 1)) / n
    parts = []
    for i, (lab, color, det) in enumerate(rows[:n]):
        yy = y + i * (rh + 8)
        bar_w = w * (1 - i * 0.08)
        parts.append(_rect(x, yy, bar_w, rh, fill=color, stroke=None, rx=8))
        ink = "#fff" if i < 3 else "#fff"
        parts.append(_t(x + 12, yy + rh * 0.45, lab[:22], size=12, fill="#fff", weight=800))
        parts.append(_t(x + 12, yy + rh * 0.78, det[:42], size=10, fill="#f8fafc", weight=500))
    return "".join(parts)


def _w_code(x, y, w, h, p: P) -> str:
    parts = [_rect(x, y, w, h - 36, fill="#f1f5f9", stroke="#94a3b8", rx=8)]
    yy = y + 18
    for ln in p.code[: max(4, int((h - 50) / 16))]:
        parts.append(_t(x + 10, yy, ln[: max(20, int(w / 8))], size=11, fill=INK, weight=500, family=MONO))
        yy += 16
    parts.append(_t(x + 4, y + h - 12, (p.expected or p.pick)[: max(24, int(w / 7))], size=11, fill="#166534", weight=700))
    return "".join(parts)


def _w_flow(x, y, w, h, p: P) -> str:
    boxes = p.flow[:4]
    n = len(boxes)
    gap = 10
    bw = (w - gap * (n - 1)) / n
    bh = min(64, h * 0.38)
    fills = ["#dbeafe", "#dcfce7", "#ffedd5", "#fef9c3"]
    inks = ["#1e40af", "#166534", "#9a3412", "#854d0e"]
    parts = []
    cy = y + bh / 2
    for i, lab in enumerate(boxes):
        bx = x + i * (bw + gap)
        parts.append(_rect(bx, y, bw, bh, fill=fills[i], stroke=inks[i], rx=8))
        parts.append(_ml(bx + bw / 2, y + bh / 2 - 4, _wrap(lab, max(6, int(bw / 8)), 2), size=11, fill=inks[i], weight=800, anchor="middle"))
        if i < n - 1:
            parts.append(_arrow(bx + bw, cy, bx + bw + gap, cy, inks[0]))
    note_y = y + bh + 16
    parts.append(_ml(x, note_y, _wrap("Name each box, then the hand-off. " + (p.pick or ""), max(22, int(w / 7)), 4), size=11, fill=MUTED))
    return "".join(parts)


def _w_vs(x, y, w, h, p: P) -> str:
    hw = (w - 10) / 2
    parts = [
        _rect(x, y, hw, h, fill="#fef2f2", stroke="#ef4444", rx=8),
        _t(x + 8, y + 18, "✗  " + p.bad_t[:22], size=12, fill="#b91c1c", weight=800),
        _ml(x + 8, y + 40, _wrap(p.bad, max(16, int(hw / 7)), 8), size=11, fill="#7f1d1d"),
        _rect(x + hw + 10, y, hw, h, fill="#f0fdf4", stroke="#16a34a", rx=8),
        _t(x + hw + 18, y + 18, "✓  Do this", size=12, fill="#166534", weight=800),
        _ml(x + hw + 18, y + 40, _wrap(p.good, max(16, int(hw / 7)), 8), size=11, fill="#14532d"),
    ]
    return "".join(parts)


def _w_triple(x, y, w, h, p: P) -> str:
    cw = (w - 16) / 3
    titles = ["Remember", "Practice", "C# map"]
    cols = [
        p.concepts[:4] or [(a, a) for a in p.flow],
        [(t, "") for t in (p.practice or [p.pick] or ["Explain with a project story"])],
        [(a, b) for a, b in CS_TABLE.get(p.track, CS_TABLE["dotnet"])[1:5]],
    ]
    parts = []
    for i in range(3):
        cx = x + i * (cw + 8)
        parts.append(_rect(cx, y, cw, h, fill="#fff", stroke="#94a3b8", rx=8))
        parts.append(_t(cx + 8, y + 16, titles[i], size=11, fill=NAVY, weight=800))
        yy = y + 34
        for lab, det in cols[i][:5]:
            parts.append(_t(cx + 8, yy, f"• {lab[:18]}", size=10, fill=INK, weight=700))
            yy += 14
            if det:
                parts.append(_t(cx + 14, yy, det[:22], size=9, fill=MUTED, weight=500))
                yy += 13
    return "".join(parts)


def _w_checklist(x, y, w, h, p: P) -> str:
    dos = p.practice or [c[0] for c in p.concepts[:3]]
    parts = [_t(x, y + 12, "Do", size=12, fill="#166534", weight=800)]
    yy = y + 32
    for d in dos[:3]:
        parts.append(_t(x, yy, "✓  " + d[:48], size=11, fill="#14532d", weight=600))
        yy += 22
    parts.append(_t(x, yy + 8, "Don't", size=12, fill="#b91c1c", weight=800))
    parts.append(_ml(x, yy + 30, _wrap("✗  " + p.bad_t + " — " + p.bad, max(22, int(w / 7)), 5), size=11, fill="#7f1d1d"))
    return "".join(parts)


def _w_stack(x, y, w, h, p: P) -> str:
    layers = [c[0] for c in p.concepts[:4]] or p.flow[:4]
    n = len(layers)
    gap = 6
    lh = (h - gap * (n - 1)) / n
    fills = ["#dbeafe", "#dcfce7", "#ffedd5", "#fef9c3"]
    inks = ["#1e40af", "#166534", "#9a3412", "#854d0e"]
    parts = []
    for i, lab in enumerate(layers):
        yy = y + i * (lh + gap)
        parts.append(_rect(x, yy, w, lh, fill=fills[i % 4], stroke=inks[i % 4], rx=8))
        det = p.concepts[i][1] if i < len(p.concepts) else ""
        parts.append(_t(x + 12, yy + lh * 0.42, lab[:36], size=13, fill=inks[i % 4], weight=800))
        if det:
            parts.append(_t(x + 12, yy + lh * 0.72, det[:48], size=10, fill=MUTED, weight=500))
        if i < n - 1:
            parts.append(_t(x + w / 2, yy + lh + 5, "↓", size=12, fill="#64748b", weight=800, anchor="middle"))
    return "".join(parts)


def _w_nested(x, y, w, h, p: P) -> str:
    labels = p.flow[:4]
    parts = []
    inset = 0
    fills = ["#dbeafe", "#bfdbfe", "#93c5fd", "#60a5fa"]
    for i, lab in enumerate(labels):
        parts.append(
            _rect(x + inset, y + inset, w - 2 * inset, h - 2 * inset, fill=fills[i], stroke="#1e40af", rx=10)
        )
        parts.append(_t(x + inset + 10, y + inset + 18, lab[:28], size=12, fill="#1e3a5f", weight=800))
        inset += min(36, h / 8)
    return "".join(parts)


def _w_join(x, y, w, h, p: P) -> str:
    hw = (w - 70) / 2
    bh = min(90, h * 0.4)
    parts = [
        _rect(x, y, hw, bh, fill="#dbeafe", stroke="#1e40af", rx=8),
        _t(x + hw / 2, y + bh / 2 + 4, "Table A", size=14, fill="#1e40af", weight=800, anchor="middle"),
        _rect(x + hw + 70, y, hw, bh, fill="#dcfce7", stroke="#166534", rx=8),
        _t(x + hw + 70 + hw / 2, y + bh / 2 + 4, "Table B", size=14, fill="#166534", weight=800, anchor="middle"),
        _arrow(x + hw, y + bh / 2, x + hw + 70, y + bh / 2),
        _t(x + hw + 35, y + bh / 2 - 10, "ON key", size=10, fill=NAVY, weight=800, anchor="middle"),
        _rect(x, y + bh + 24, w, h - bh - 28, fill="#fef9c3", stroke="#854d0e", rx=8),
        _t(x + 12, y + bh + 48, "INNER: matches only    LEFT: keep A, NULL on B", size=12, fill="#854d0e", weight=700),
        _ml(x + 12, y + bh + 72, _wrap(p.pick or "Missing ON multiplies rows. WHERE on the right of LEFT JOIN becomes INNER.", max(28, int(w / 7)), 4), size=11, fill=MUTED),
    ]
    return "".join(parts)


def _w_metrics(x, y, w, h, p: P) -> str:
    items = p.concepts[:4] or [(f, "") for f in p.flow]
    coords = [(0, 0), (1, 0), (0, 1), (1, 1)]
    cw, ch = (w - 8) / 2, (h - 8) / 2
    fills = ["#dbeafe", "#dcfce7", "#ffedd5", "#fef9c3"]
    inks = ["#1e40af", "#166534", "#9a3412", "#854d0e"]
    qs = ["What?", "Where?", "Why?", "How / proof?"]
    parts = []
    for i, ((cx, cy), (lab, det)) in enumerate(zip(coords, items)):
        px, py = x + cx * (cw + 8), y + cy * (ch + 8)
        parts.append(_rect(px, py, cw, ch, fill=fills[i], stroke=inks[i], rx=8))
        parts.append(_t(px + 10, py + 18, qs[i] if p.sid.endswith("14") or p.sid.endswith("16") or p.sid.endswith("72") else str(i + 1), size=11, fill=inks[i], weight=800))
        parts.append(_t(px + 10, py + 38, lab[:22], size=13, fill=inks[i], weight=800))
        parts.append(_ml(px + 10, py + 58, _wrap(det or p.pick, max(14, int(cw / 8)), 3), size=10, fill=MUTED))
    return "".join(parts)


def _w_decision(x, y, w, h, p: P) -> str:
    pair = p.pair
    if pair and pair[0]:
        a, ad, b, bd = pair
    elif len(p.concepts) >= 2:
        a, ad = p.concepts[0]
        b, bd = p.concepts[1]
    else:
        a, ad, b, bd = p.flow[0], "", p.flow[1] if len(p.flow) > 1 else "Other", ""
    parts = [
        f'<polygon points="{x + w/2:.0f},{y + 8:.0f} {x + w/2 + 70:.0f},{y + 48:.0f} {x + w/2:.0f},{y + 88:.0f} {x + w/2 - 70:.0f},{y + 48:.0f}" fill="#fef9c3" stroke="#b45309" stroke-width="1.8"/>',
        _t(x + w / 2, y + 52, "Which?", size=12, fill="#b45309", weight=800, anchor="middle"),
        _rect(x, y + 100, w * 0.48, h - 108, fill="#dbeafe", stroke="#1e40af", rx=8),
        _rect(x + w * 0.52, y + 100, w * 0.48, h - 108, fill="#dcfce7", stroke="#166534", rx=8),
        _t(x + 10, y + 122, a[:20], size=12, fill="#1e40af", weight=800),
        _ml(x + 10, y + 144, _wrap(ad, max(14, int(w * 0.06)), 6), size=11, fill=MUTED),
        _t(x + w * 0.52 + 10, y + 122, b[:20], size=12, fill="#166534", weight=800),
        _ml(x + w * 0.52 + 10, y + 144, _wrap(bd, max(14, int(w * 0.06)), 6), size=11, fill=MUTED),
    ]
    return "".join(parts)


WIDGETS = {
    "table": _w_table,
    "levels": _w_levels,
    "code": _w_code,
    "flow": _w_flow,
    "vs": _w_vs,
    "triple": _w_triple,
    "checklist": _w_checklist,
    "stack": _w_stack,
    "nested": _w_nested,
    "join": _w_join,
    "metrics": _w_metrics,
    "decision": _w_decision,
}

DEFAULT_TITLES = {
    "table": "Compare — pick with a reason",
    "levels": "The scale you must name",
    "code": "Minimal setup / sample",
    "flow": "How the pieces connect",
    "vs": "The trap vs the fix",
    "triple": "Practice, C#, remember",
    "checklist": "Good practice",
    "stack": "Inside the system",
    "nested": "What contains what",
    "join": "How rows combine",
    "metrics": "Numbers / interview drill",
    "decision": "When A vs when B",
}

DEFAULT_CAPTION = {
    "table": "Say the criterion, then the choice.",
    "levels": "Set one level; everything below it goes quiet — or name the lifetime.",
    "code": "Configure once; point at a real line.",
    "flow": "Name each box, then the hand-off.",
    "vs": "Preferred form vs the interview trap.",
    "triple": "Recite practice, then the C# cousin.",
    "checklist": "Do / don't you can recite.",
    "stack": "Top to bottom, then the hand-off.",
    "nested": "Outer box owns the inner ones.",
    "join": "ON the key; watch multiplication.",
    "metrics": "What / where / why / how.",
    "decision": "Pick a path with a project example.",
}


def _panel_title(p: P, widget: str) -> str:
    return PANEL_TITLE.get((p.sid, widget)) or DEFAULT_TITLES.get(widget, widget)


def _draw_widget(kind: str, x, y, w, h, p: P) -> str:
    fn = WIDGETS.get(kind, _w_flow)
    return fn(x, y, w, h, p)


def _slots_3x2() -> list[tuple[float, float, float, float]]:
    m, g, header = 16, 10, 78
    pw = (1536 - 2 * m - 2 * g) / 3
    ph = (1024 - header - m - g) / 2
    slots = []
    for r in range(2):
        for c in range(3):
            slots.append((m + c * (pw + g), header + r * (ph + g), pw, ph))
    return slots


def _slots_2x3() -> list[tuple[float, float, float, float]]:
    m, g, header = 16, 10, 78
    pw = (1536 - 2 * m - g) / 2
    ph = (1024 - header - m - 2 * g) / 3
    slots = []
    for r in range(3):
        for c in range(2):
            slots.append((m + c * (pw + g), header + r * (ph + g), pw, ph))
    return slots


def _slots_hero() -> list[tuple[float, float, float, float]]:
    m, g, header = 16, 10, 78
    top_h = 210
    rest = 1024 - header - top_h - g - m
    mid_h = rest * 0.5
    bot_h = rest - mid_h - g
    pw3 = (1536 - 2 * m - 2 * g) / 3
    pw2 = (1536 - 2 * m - g) / 2
    y1 = header
    y2 = header + top_h + g
    y3 = y2 + mid_h + g
    return [
        (m, y1, 1536 - 2 * m, top_h),
        (m, y2, pw3, mid_h),
        (m + pw3 + g, y2, pw3, mid_h),
        (m + 2 * (pw3 + g), y2, pw3, mid_h),
        (m, y3, pw2, bot_h),
        (m + pw2 + g, y3, pw2, bot_h),
    ]


def svg_for_skill(n: int, skill: dict[str, Any], *, track: str) -> str:
    p = _ctx(skill, track, n)
    kinds = widgets_for(p.sid)
    grid = grid_for(p.sid)
    slots = {"3x2": _slots_3x2, "2x3": _slots_2x3, "hero_plus": _slots_hero}[grid]()
    rot = (p.rotate - 1) % 6
    parts = [
        _rect(0, 0, 1536, 1024, fill=PAGE, stroke=None, rx=0),
        _rect(0, 0, 1536, 6, fill=NAVY, stroke=None, rx=0),
        _t(768, 28, f"{p.title}  –  Visual Guide", size=26, fill=NAVY, weight=800, anchor="middle"),
        _t(768, 52, f"{p.label}  ·  {p.sid}  ·  {p.intro[:110]}", size=12, fill=MUTED, weight=500, anchor="middle"),
    ]
    for i, (kind, (x, y, w, h)) in enumerate(zip(kinds, slots), 1):
        ink = PANEL_INK[(i - 1 + rot) % 6]
        fill = PANEL_FILL[(i - 1 + rot) % 6]
        title = _panel_title(p, kind)
        parts.append(_panel(x, y, w, h, i, title, ink, fill))
        cap = DEFAULT_CAPTION.get(kind, "")
        parts.append(_caption(x + 16, y + 42, w - 28, cap))
        inner_y = y + 68
        inner_h = h - 80
        if inner_h > 40:
            parts.append(_draw_widget(kind, x + 14, inner_y, w - 28, inner_h, p))
    defs = """
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="#64748b"/>
    </marker>
  </defs>
"""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024" viewBox="0 0 1536 1024">\n'
        + defs
        + "".join(parts)
        + "\n</svg>\n"
    )


def write_svg_posters(skills, images_dir: Path, *, track: str) -> dict[int, tuple[str, str, int]]:
    images_dir.mkdir(parents=True, exist_ok=True)
    for old in images_dir.glob("slide-*.svg"):
        old.unlink()
    mapping: dict[int, tuple[str, str, int]] = {}
    for n, skill in enumerate(skills, 1):
        slug = _slug(skill.get("title") or f"slide-{n}")
        name = f"slide-{n:02d}-{slug}.svg"
        (images_dir / name).write_text(svg_for_skill(n, skill, track=track), encoding="utf-8")
        mapping[n] = (f"images/{name}", skill.get("title") or f"Slide {n}", 1536)
    return mapping


def _guide_block(win_id: str, src: str, label: str, native_w: int) -> str:
    title = f"{html_mod.escape(label)} &ndash; Visual Guide"
    return f'''
<div class="vguide-strip">
  <a class="vguide-thumb" href="{src}" target="_blank" rel="noopener noreferrer"
    title="Open the full-size poster in a new tab">
    <img src="{src}" alt="{html_mod.escape(label)} visual guide poster" loading="lazy" decoding="async">
    <span class="vguide-expand" aria-hidden="true">&#x26F6;</span>
  </a>
  <div class="vguide-txt">
    <b>Visual guide &mdash; {html_mod.escape(label)}</b>
    <span>One-page poster: mixed diagrams, tables and code (Python Logging standard). Click the thumbnail for full size.</span>
    <button type="button" class="btn-vguide-win" onclick="openCsharpWin('{win_id}')">
      Open in resizable window
    </button>
  </div>
</div>
<div class="csharp-float-win img-float-win" id="csharp-win-{win_id}" role="dialog"
  aria-labelledby="csharp-win-title-{win_id}">
  <div class="csharp-float-hdr">
    <span class="csharp-float-drag" aria-hidden="true">&#8942;&#8942;</span>
    <h4 id="csharp-win-title-{win_id}">{title}</h4>
    <button type="button" class="btn-img-fit" onclick="toggleImgFloatFit(this)"
      title="Image fits the window (scales when you resize)">Fit</button>
    <button type="button" class="csharp-float-close"
      onclick="closeCsharpWin('{win_id}')" aria-label="Close">&times;</button>
  </div>
  <div class="csharp-float-body csharp-float-body-img" style="--native-w:{native_w}px">
    <a href="{src}" target="_blank" rel="noopener noreferrer"
      title="Open full-size image in a new tab">
      <img src="{src}" alt="{html_mod.escape(label)} visual guide poster" loading="lazy" decoding="async">
    </a>
  </div>
  <div class="csharp-float-resize" title="Drag to resize" aria-hidden="true"></div>
</div>
'''


def make_visual_guide_fn(mapping: dict[int, tuple[str, str, int]]) -> Callable[[int], str]:
    def visual_guide_for(n: int) -> str:
        entry = mapping.get(n)
        if not entry:
            return ""
        return _guide_block(f"vguide-{n}", *entry)

    return visual_guide_for
