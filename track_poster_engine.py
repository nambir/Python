"""Interview-track visual guides in the Python poster language.

Look: white cards, colored borders, pill banners, Gantt timelines, event-loop,
padlock, sample output — like images/slide-21-async-await.png and
slide-22-logging.png. Not generic 4-box stencils.
"""

from __future__ import annotations

import html as html_mod
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from track_poster_plans import PANEL_TITLE, widgets_for
from track_poster_style import (
    ARCH,
    BANNER,
    FOOTER_CODE,
    GANTT,
    HUB,
    INKS,
    JOIN_IDS,
    LANE2,
    LOCK,
    MESSY,
    PICK_ROWS,
    PILL_TX,
    PILLS,
    extra_compare,
    extra_levels,
)
from track_visual_flows import FLOW_BY_ID

FONT = "Segoe UI,Arial,sans-serif"
MONO = "Consolas,Menlo,monospace"
PAGE, INK, MUTED, NAVY = "#ffffff", "#0f172a", "#475569", "#1e3a5f"
WORK, WAIT = "#86efac", "#cbd5e1"
WORK_INK, LOCK_RED = "#166534", "#dc2626"

TRACK_LABEL = {"dotnet": ".NET", "angular": "Angular", "sql": "SQL Server", "aws": "AWS"}

CS_TABLE = {
    "angular": [
        ("Angular", "C#"),
        ("async pipe / Observable", "IAsyncEnumerable / Task"),
        ("Interceptor", "DelegatingHandler"),
        ("CanActivate", "[Authorize] still required"),
        ("providedIn root", "singleton DI"),
    ],
    "sql": [
        ("SQL", "C# / EF"),
        ("JOIN", "LINQ Join / Include"),
        ("Stored proc", "FromSqlInterpolated"),
        ("BEGIN TRAN", "IDbContextTransaction"),
        ("Actual plan", "SET STATISTICS IO + SSMS"),
    ],
    "aws": [
        ("AWS", "C#"),
        ("API Gateway", "reverse proxy + JWT"),
        ("ECS task", "one process recipe"),
        ("ECS service", "desired count"),
        ("ALB /health", "Kestrel health"),
    ],
    "dotnet": [
        (".NET", "Say this"),
        ("async Task", "I/O wait; not extra threads"),
        ("Task.WhenAll", "overlap waits"),
        ("Task.Run", "CPU off the request thread"),
        ("Scoped", "one per HTTP request"),
    ],
}

KIND_BANNER = {
    "gantt": "Sync waits idle. Async uses the wait time for other work.",
    "hub": "At each await the pool can take another request.",
    "lock": "Async is for waiting, not for heavy CPU.",
    "messy": "A laundry list is the fail. A drawing is the pass.",
    "join": "INNER drops unmatched left rows. LEFT keeps them as NULL.",
    "nested": "Name the outer box, then what lives inside it.",
    "stack": "Bottom is the foundation. Top is what the caller sees.",
    "decision": "Name both forks, then which one you actually ran.",
    "metrics": "Numbers beat adjectives. Say the count and the unit.",
    "checklist": "Recite do / don't. Stop when the list is short.",
    "branch": "One request, then the hand-off to each sink.",
    "vs": "Preferred form vs the interview trap.",
    "code": "Configure once; point at a real line.",
    "table": "Name the pair, then the reason you pick one.",
    "arch": "Name each box, then the hand-off.",
    "levels": "The scale you must name — not a synonym list.",
    "numbers": "Same work, different cost. Point at the winning row.",
}

TITLES = {
    "gantt": "Sync vs async (the problem)",
    "hub": "The wait loop (one pool)",
    "lock": "When it helps vs when it does not",
    "arch": "The drawing you recite",
    "flow": "The drawing you recite",
    "join": "What the rows actually do",
    "levels": "The scale you must name",
    "table": "Compare — pick with a reason",
    "code": "Minimal setup / sample",
    "branch": "How a record / request travels",
    "messy": "Laundry list vs a drawing",
    "vs": "The trap vs the fix",
    "numbers": "Worked example (numbers)",
    "nested": "Inside the box",
    "stack": "Layers you must name",
    "decision": "The fork that matters",
    "metrics": "Worked example (numbers)",
    "checklist": "Do / don't you can recite",
    "triple": "Three numbers to keep",
    "footer": "Code, pick rule & C#",
}

MAP_SCENE = {
    "flow": "arch",
    "triple": "metrics",
    "checklist": "checklist",
    "nested": "nested",
    "decision": "decision",
    "stack": "stack",
    "metrics": "metrics",
    "join": "join",
    "table": "table",
    "code": "code",
    "vs": "vs",
    "levels": "levels",
    "gantt": "gantt",
    "hub": "hub",
    "lock": "lock",
    "arch": "arch",
    "messy": "messy",
    "branch": "branch",
    "numbers": "numbers",
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
    lines, cur = [], ""
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


def _ml(x, y, lines, *, size, fill, weight=500, anchor="start", family=FONT) -> str:
    parts = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else int(size * 1.15)
        parts.append(f'<tspan x="{x:.0f}" dy="{dy}">{_xml(line)}</tspan>')
    return (
        f'<text x="{x:.0f}" y="{y:.0f}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
        f'text-anchor="{anchor}" font-family="{family}">{"".join(parts)}</text>'
    )


def _rect(x, y, w, h, *, fill, stroke=None, sw=1.6, rx=12) -> str:
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}"{st}/>'


def _circle(cx, cy, r, *, fill, stroke=None, sw=2) -> str:
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{fill}"{st}/>'


def _arrow(x1, y1, x2, y2, color="#64748b", dash=False) -> str:
    d = ' stroke-dasharray="4 3"' if dash else ""
    return (
        f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
        f'stroke="{color}" stroke-width="2.2"{d} marker-end="url(#arrow)"/>'
    )


def _pill(x, y, w, text: str, fill: str, ink: str) -> str:
    return _rect(x, y, w, 28, fill=fill, stroke=None, rx=8) + _t(
        x + 10, y + 19, text[:72], size=11, fill=ink, weight=700
    )


def _lock(cx, cy) -> str:
    return (
        f'<rect x="{cx-8:.0f}" y="{cy:.0f}" width="16" height="14" rx="2" fill="{LOCK_RED}"/>'
        f'<path d="M{cx-6:.0f},{cy:.0f} v-6 a6,6 0 0 1 12,0 v6" fill="none" stroke="{LOCK_RED}" stroke-width="2.5"/>'
    )


def _icon(kind: str, x, y) -> str:
    if kind == "cloud":
        return (
            f'<ellipse cx="{x+16:.0f}" cy="{y+14:.0f}" rx="16" ry="10" fill="#93c5fd"/>'
            f'<ellipse cx="{x+8:.0f}" cy="{y+16:.0f}" rx="10" ry="8" fill="#60a5fa"/>'
            f'<ellipse cx="{x+26:.0f}" cy="{y+16:.0f}" rx="9" ry="7" fill="#3b82f6"/>'
        )
    if kind == "chip":
        return (
            _rect(x + 6, y + 6, 22, 18, fill="#fdba74", stroke="#c2410c", sw=1.4, rx=3)
            + _t(x + 17, y + 19, "CPU", size=7, fill="#7c2d12", weight=800, anchor="middle")
        )
    return (
        _rect(x + 4, y + 10, 12, 12, fill="#c4b5fd", stroke="#6d28d9", rx=2)
        + _rect(x + 14, y + 4, 12, 12, fill="#a78bfa", stroke="#6d28d9", rx=2)
        + _rect(x + 20, y + 14, 12, 12, fill="#8b5cf6", stroke="#6d28d9", rx=2)
    )


def _concepts(skill: dict[str, Any]) -> list[tuple[str, str]]:
    out = []
    for row in skill.get("table_rows") or []:
        if len(row) >= 2:
            out.append((_plain(row[0]), _plain(row[1])))
    return out[:6]


def _code_lines(skill: dict[str, Any], n: int = 7) -> list[str]:
    raw = skill.get("code") or ""
    keep = [ln.rstrip() for ln in str(raw).splitlines() if ln.strip()]
    return [ln[:64] for ln in keep[:n]] or ["# point at the diagram"]


def _mistake(skill: dict[str, Any]) -> tuple[str, str, str]:
    m = (skill.get("mistakes") or [None])[0]
    if not m or len(m) < 3:
        return ("Weak answer", "Definition only", "Project story + evidence")
    return (_plain(m[0]), _plain(m[1]), _plain(m[2]))


def _flow(skill: dict[str, Any]) -> list[str]:
    sid = skill.get("id") or ""
    if sid in FLOW_BY_ID:
        return list(FLOW_BY_ID[sid])
    return [c[0][:20] for c in _concepts(skill)[:4]] or ["A", "B", "C", "D"]


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


def _ctx(skill: dict[str, Any], track: str, n: int) -> P:
    sid = skill.get("id") or f"S{n:02d}"
    bt, bad, good = _mistake(skill)
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
        expected=_plain(skill.get("expected") or ""),
        bad_t=bt,
        bad=bad,
        good=good,
        pick=_plain(skill.get("level3") or ""),
        practice=[_plain(x) for x in (skill.get("practice") or [])][:4],
    )


def _card(x, y, w, h, n, title, ink) -> str:
    return (
        _rect(x, y, w, h, fill="#fff", stroke=ink, sw=2, rx=14)
        + _circle(x + 22, y + 22, 12, fill=ink)
        + _t(x + 22, y + 26, str(n), size=11, fill="#fff", weight=800, anchor="middle")
        + _t(x + 40, y + 27, title[:42], size=14, fill=NAVY, weight=800)
    )


def _table(x, y, w, headers, rows, row_h=32) -> str:
    cols = max(2, min(3, len(headers)))
    headers = headers[:cols]
    cw = w / cols
    chars = max(10, int(cw / 7.0))
    parts = [_rect(x, y, w, 24, fill=NAVY, stroke=None, rx=6)]
    for i, hd in enumerate(headers):
        parts.append(_t(x + i * cw + 8, y + 17, hd[:chars], size=11, fill="#fff", weight=700))
    for r, row in enumerate(rows[:5]):
        yy = y + 24 + row_h * r
        bg = "#ffffff" if r % 2 == 0 else "#f1f5f9"
        if r == len(rows[:5]) - 1 and r >= 2:
            bg = "#dcfce7"
        parts.append(_rect(x, yy, w, row_h, fill=bg, stroke="#e2e8f0", sw=1, rx=0))
        for i in range(cols):
            cell = row[i] if i < len(row) else ""
            parts.append(
                _ml(
                    x + i * cw + 8,
                    yy + 13,
                    _wrap(_plain(str(cell)), chars, 2),
                    size=10,
                    fill=INK,
                    weight=500,
                )
            )
    return "".join(parts)


def _code_box(x, y, w, h, lines, title: str | None = None) -> str:
    parts = [_rect(x, y, w, h, fill="#f8fafc", stroke="#cbd5e1", rx=8)]
    yy = y + 18
    if title:
        parts.append(_t(x + 10, yy, title, size=10, fill="#1e40af", weight=800, family=MONO))
        yy += 16
    n = max(2, int((h - (24 if title else 12)) / 16))
    for ln in lines[:n]:
        parts.append(_t(x + 10, yy, ln[: max(16, int(w / 7.8))], size=11, fill=INK, weight=500, family=MONO))
        yy += 16
    return "".join(parts)


def _gantt(x, y, w, h, g: dict) -> str:
    jobs = g["jobs"]
    parts = [
        _t(x, y + 12, g["sync_name"], size=11, fill=MUTED, weight=700),
        _t(x, y + 86, g["async_name"], size=11, fill=MUTED, weight=700),
    ]
    n = len(jobs)
    bw = (w - 8) / max(n, 1)
    for i, job in enumerate(jobs):
        bx = x + i * bw
        parts.append(_rect(bx, y + 20, bw - 4, 22, fill=WORK, stroke=None, rx=4))
        parts.append(_rect(bx, y + 42, bw - 4, 14, fill=WAIT, stroke=None, rx=3))
        parts.append(_t(bx + 4, y + 36, job[:14], size=10, fill=WORK_INK, weight=700))
        parts.append(_t(bx + 4, y + 53, "(waiting)", size=9, fill=MUTED, weight=500))
    parts.append(_t(x + w - 4, y + 40, f"Total {g['sync_s']}s", size=12, fill=NAVY, weight=800, anchor="end"))
    for i, job in enumerate(jobs):
        parts.append(_rect(x, y + 100 + i * 20, w * 0.46, 16, fill=WORK, stroke=None, rx=4))
        parts.append(_t(x + 6, y + 112 + i * 20, f"{job} (waiting)", size=10, fill=WORK_INK, weight=700))
    parts.append(_t(x + w - 4, y + 118, f"Total {g['async_s']}s", size=12, fill=WORK_INK, weight=800, anchor="end"))
    for t, lab in enumerate(["0s", "1s", "2s", "3s"]):
        parts.append(_t(x + t * (w / 3), y + h - 4, lab, size=10, fill=MUTED, weight=600))
    return "".join(parts)


def _hub(x, y, w, h, center: str, sats: list[str]) -> str:
    cx, cy, r = x + w / 2, y + h / 2 - 4, min(w, h) * 0.15
    parts = [
        _circle(cx, cy, r + 6, fill="#ede9fe", stroke="#7c3aed", sw=2),
        _t(cx, cy + 5, center[:12], size=13, fill="#5b21b6", weight=800, anchor="middle"),
    ]
    pos = [(cx, y + 16), (x + w - 64, cy), (cx, y + h - 18), (x + 64, cy)]
    for (px, py), lab in zip(pos, sats[:4]):
        parts.append(_arrow(cx, cy, px, py, "#7c3aed", dash=True))
        parts.append(_rect(px - 50, py - 13, 100, 26, fill=WORK, stroke=None, rx=8))
        parts.append(_t(px, py + 5, lab[:14], size=11, fill=WORK_INK, weight=700, anchor="middle"))
    return "".join(parts)


def _lock_io(x, y, w, h, io: str, cpu: str) -> str:
    hw = (w - 12) / 2
    parts = [
        _rect(x, y, hw, h, fill="#f0fdf4", stroke="#16a34a", rx=10),
        _t(x + 10, y + 18, "I/O-bound — async helps", size=11, fill=WORK_INK, weight=800),
        _rect(x + 12, y + 34, hw * 0.5, 14, fill=WORK, stroke=None, rx=3),
        _rect(x + 12, y + 52, hw * 0.68, 14, fill=WORK, stroke=None, rx=3),
        _rect(x + 12, y + 70, hw * 0.38, 14, fill=WORK, stroke=None, rx=3),
        _ml(x + 10, y + 100, _wrap(io, 26, 4), size=11, fill=MUTED),
        _rect(x + hw + 12, y, hw, h, fill="#fff7ed", stroke="#ea580c", rx=10),
        _t(x + hw + 22, y + 18, "CPU-bound — does NOT help", size=11, fill="#9a3412", weight=800),
        _rect(x + hw + 24, y + 44, hw - 44, 26, fill="#fdba74", stroke=None, rx=4),
        _t(x + hw + 34, y + 62, "CPU work", size=11, fill="#9a3412", weight=800),
        _lock(x + hw + hw - 28, y + 48),
        _t(x + hw + 24, y + 88, "Loop / thread frozen", size=11, fill=LOCK_RED, weight=700),
        _ml(x + hw + 22, y + 108, _wrap(cpu, 24, 3), size=11, fill=MUTED),
    ]
    return "".join(parts)


def _arch(x, y, w, h, nodes: list[tuple[str, str]], lane2: list[str] | None) -> str:
    n = max(1, len(nodes))
    gap = 10
    bw = (w - gap * (n - 1)) / n
    fills = ["#dbeafe", "#dcfce7", "#ffedd5", "#fef9c3"]
    inks = ["#1e40af", "#166534", "#9a3412", "#854d0e"]
    chars = max(8, int(bw / 7.2))
    bh = 62 if lane2 else min(88, h * 0.55)
    y0 = y + (18 if lane2 else 4)
    parts = []
    if lane2:
        parts.append(_t(x, y + 12, "① User click (sync)", size=10, fill="#1e40af", weight=800))
    for i, (title, sub) in enumerate(nodes):
        bx = x + i * (bw + gap)
        parts.append(_rect(bx, y0, bw, bh, fill=fills[i % 4], stroke=inks[i % 4], sw=1.6, rx=10))
        parts.append(_ml(bx + 8, y0 + 18, _wrap(title, chars, 2), size=11, fill=inks[i % 4], weight=800))
        parts.append(_t(bx + 8, y0 + bh - 12, sub[: chars + 4], size=9, fill=MUTED, weight=500))
        if i < n - 1:
            parts.append(_arrow(bx + bw, y0 + bh / 2, bx + bw + gap, y0 + bh / 2, inks[0]))
    if lane2:
        ly = y0 + bh + 22
        parts.append(_t(x, ly - 6, "② Work that can wait (async)", size=10, fill="#7c3aed", weight=800))
        lw = (w - gap * (len(lane2) - 1)) / max(1, len(lane2))
        lc = max(8, int(lw / 7.2))
        for i, lab in enumerate(lane2):
            bx = x + i * (lw + gap)
            parts.append(_rect(bx, ly + 4, lw, 36, fill="#ede9fe", stroke="#7c3aed", rx=8))
            parts.append(_t(bx + lw / 2, ly + 27, lab[:lc], size=11, fill="#5b21b6", weight=700, anchor="middle"))
            if i < len(lane2) - 1:
                parts.append(_arrow(bx + lw, ly + 22, bx + lw + gap, ly + 22, "#7c3aed"))
    return "".join(parts)


def _join_rows(x, y, w, h) -> str:
    tw = min(150, w * 0.28)
    th = min(96, h * 0.58)
    parts = [_t(x, y + 12, "Orders", size=11, fill=NAVY, weight=800)]
    parts.append(_rect(x, y + 18, tw, th, fill="#fff", stroke="#3b82f6", rx=6))
    for i, oid in enumerate(["101", "102", "103"]):
        parts.append(_t(x + 10, y + 42 + i * 22, f"Id {oid}", size=12, fill=INK, weight=600))
    sx = x + tw + 18
    parts.append(_t(sx, y + 12, "Shipment", size=11, fill=NAVY, weight=800))
    parts.append(_rect(sx, y + 18, tw, th, fill="#fff", stroke="#16a34a", rx=6))
    for i, row in enumerate(["101 → shipped", "103 → shipped"]):
        parts.append(_t(sx + 10, y + 48 + i * 26, row, size=12, fill=INK, weight=600))
    rx = x + 2 * tw + 40
    parts.append(_rect(rx, y + 18, w - (rx - x), th, fill="#eff6ff", stroke="#3b82f6", rx=8))
    parts.append(_t(rx + 10, y + 40, "INNER → 2 rows", size=12, fill="#1e40af", weight=800))
    parts.append(_t(rx + 10, y + 58, "101, 103", size=12, fill=WORK_INK, weight=700))
    parts.append(_t(rx + 10, y + 82, "LEFT → 3 rows", size=12, fill="#166534", weight=800))
    parts.append(_t(rx + 10, y + 100, "101, 102+NULL, 103", size=12, fill="#854d0e", weight=700))
    parts.append(
        _ml(
            x,
            y + th + 36,
            _wrap("102 has no shipment. INNER hides it. LEFT keeps it as NULL.", 52, 2),
            size=11,
            fill=MUTED,
        )
    )
    return "".join(parts)


def _levels(x, y, w, h, rows: list[tuple[str, str, str]]) -> str:
    n = len(rows[:5])
    rh = (h - 6 * (n - 1)) / n
    parts = []
    for i, (lab, color, det) in enumerate(rows[:n]):
        yy = y + i * (rh + 6)
        bar_w = w * (1 - i * 0.05)
        parts.append(_rect(x, yy, bar_w, rh, fill=color, stroke=None, rx=8))
        parts.append(_t(x + 12, yy + rh * 0.42, lab[:28], size=13, fill="#fff", weight=800))
        parts.append(_t(x + 12, yy + rh * 0.78, det[:46], size=10, fill="#f8fafc", weight=500))
    return "".join(parts)


def _branch(x, y, w, h, labels: list[str]) -> str:
    labs = (labels + ["Out A", "Out B"])[:4]
    parts = []
    bw = min(110, (w - 220) / 3)
    y0 = y + h * 0.32
    xs = [x, x + bw + 28, x + 2 * (bw + 28)]
    for i, lab in enumerate(labs[:3]):
        parts.append(_rect(xs[i], y0, bw, 40, fill="#ede9fe" if i else "#dbeafe", stroke="#4f46e5", rx=8))
        parts.append(_t(xs[i] + bw / 2, y0 + 26, lab[:14], size=11, fill="#4f46e5", weight=700, anchor="middle"))
        if i < 2:
            parts.append(_arrow(xs[i] + bw, y0 + 20, xs[i + 1], y0 + 20, "#4f46e5"))
    parts.append(_arrow(xs[2] + bw, y0 + 10, x + w - 110, y + 20, "#4f46e5"))
    parts.append(_arrow(xs[2] + bw, y0 + 30, x + w - 110, y + h - 28, "#4f46e5"))
    sink = labs[3] if len(labs) > 3 else "SQL + observe"
    parts.append(_rect(x + w - 110, y + 8, 100, 32, fill="#dcfce7", stroke="#16a34a", rx=6))
    parts.append(_t(x + w - 60, y + 29, sink[:12], size=10, fill=WORK_INK, weight=700, anchor="middle"))
    parts.append(_rect(x + w - 110, y + h - 40, 100, 32, fill="#ffedd5", stroke="#ea580c", rx=6))
    parts.append(_t(x + w - 60, y + h - 19, "file / sink", size=10, fill="#9a3412", weight=700, anchor="middle"))
    return "".join(parts)


def _messy_clean(x, y, w, h, pills: list[str], clean: list[tuple[str, str]]) -> str:
    hw = (w - 12) / 2
    parts = [
        _rect(x, y, hw, h, fill="#fef2f2", stroke="#ef4444", rx=10),
        _t(x + 10, y + 18, "✗  List every product", size=12, fill="#b91c1c", weight=800),
    ]
    px, py = x + 10, y + 34
    for name in pills[:10]:
        parts.append(_rect(px, py, 68, 22, fill="#fecaca", stroke=None, rx=6))
        parts.append(_t(px + 34, py + 16, name[:10], size=9, fill="#7f1d1d", weight=700, anchor="middle"))
        px += 74
        if px > x + hw - 78:
            px, py = x + 10, py + 28
    parts.append(_rect(x + hw + 12, y, hw, h, fill="#f0fdf4", stroke="#16a34a", rx=10))
    parts.append(_t(x + hw + 22, y + 18, "✓  Draw only what you ran", size=12, fill=WORK_INK, weight=800))
    n = max(1, len(clean[:4]))
    step = (h - 36) / n
    for i, (title, sub) in enumerate(clean[:4]):
        yy = y + 28 + i * step
        parts.append(_rect(x + hw + 22, yy, hw - 28, min(36, step - 8), fill="#fff", stroke="#16a34a", rx=8))
        parts.append(_t(x + hw + 32, yy + 16, title[:22], size=11, fill=WORK_INK, weight=800))
        parts.append(_t(x + hw + 32, yy + 30, sub[:26], size=9, fill=MUTED, weight=500))
        if i < n - 1:
            parts.append(
                _arrow(
                    x + hw + 12 + (hw - 28) / 2,
                    yy + min(36, step - 8),
                    x + hw + 12 + (hw - 28) / 2,
                    yy + step,
                    "#16a34a",
                )
            )
    return "".join(parts)


def _vs(x, y, w, h, bad_t, bad, good) -> str:
    hw = (w - 10) / 2
    return "".join(
        [
            _rect(x, y, hw, h, fill="#fef2f2", stroke="#ef4444", rx=10),
            _t(x + 10, y + 20, "✗  " + bad_t[:28], size=12, fill="#b91c1c", weight=800),
            _ml(x + 10, y + 42, _wrap(bad, max(18, int(hw / 7.2)), 7), size=12, fill="#7f1d1d"),
            _rect(x + hw + 10, y, hw, h, fill="#f0fdf4", stroke="#16a34a", rx=10),
            _t(x + hw + 20, y + 20, "✓  Do this", size=12, fill=WORK_INK, weight=800),
            _ml(x + hw + 20, y + 42, _wrap(good, max(18, int(hw / 7.2)), 7), size=12, fill="#14532d"),
        ]
    )


def _nested(x, y, w, h, labels: list[str]) -> str:
    fills = ["#dbeafe", "#ede9fe", "#dcfce7", "#ffedd5"]
    inks = ["#1e40af", "#5b21b6", "#166534", "#9a3412"]
    parts = []
    n = min(4, max(2, len(labels)))
    for i in range(n):
        inset = 8 + i * 16
        parts.append(
            _rect(
                x + inset,
                y + inset,
                w - 2 * inset,
                h - 2 * inset,
                fill=fills[i],
                stroke=inks[i],
                rx=10,
            )
        )
        parts.append(_t(x + inset + 10, y + inset + 16, labels[i][:28], size=12, fill=inks[i], weight=800))
    return "".join(parts)


def _stack(x, y, w, h, labels: list[str]) -> str:
    labs = (labels + ["Layer"])[:4]
    n = len(labs)
    rh = (h - 8 * (n - 1)) / n
    fills = ["#1e3a5f", "#3b82f6", "#86efac", "#fde68a"]
    inks = ["#fff", "#fff", "#14532d", "#854d0e"]
    parts = []
    for i, lab in enumerate(labs):
        yy = y + i * (rh + 8)
        parts.append(_rect(x, yy, w, rh, fill=fills[i % 4], stroke=None, rx=8))
        parts.append(_t(x + w / 2, yy + rh * 0.58, lab[:32], size=13, fill=inks[i % 4], weight=800, anchor="middle"))
    return "".join(parts)


def _decision(x, y, w, h, left: str, right: str, q: str) -> str:
    cx = x + w / 2
    parts = [
        _rect(cx - 90, y + 4, 180, 36, fill="#ede9fe", stroke="#7c3aed", rx=8),
        _t(cx, y + 28, q[:28], size=12, fill="#5b21b6", weight=800, anchor="middle"),
        _arrow(cx - 20, y + 40, x + w * 0.22, y + 70, "#7c3aed"),
        _arrow(cx + 20, y + 40, x + w * 0.78, y + 70, "#7c3aed"),
        _rect(x, y + 72, w * 0.46, h - 76, fill="#f0fdf4", stroke="#16a34a", rx=10),
        _t(x + 12, y + 94, "Path A", size=11, fill=WORK_INK, weight=800),
        _ml(x + 12, y + 116, _wrap(left, max(16, int(w * 0.4 / 7)), 5), size=12, fill="#14532d"),
        _rect(x + w * 0.54, y + 72, w * 0.46, h - 76, fill="#fff7ed", stroke="#ea580c", rx=10),
        _t(x + w * 0.54 + 12, y + 94, "Path B", size=11, fill="#9a3412", weight=800),
        _ml(x + w * 0.54 + 12, y + 116, _wrap(right, max(16, int(w * 0.4 / 7)), 5), size=12, fill="#7c2d12"),
    ]
    return "".join(parts)


def _metrics(x, y, w, h, items: list[tuple[str, str]]) -> str:
    n = min(3, max(1, len(items)))
    cw = (w - 12 * (n - 1)) / n
    fills = ["#dbeafe", "#dcfce7", "#ffedd5"]
    inks = ["#1e40af", "#166534", "#9a3412"]
    parts = []
    for i, (a, b) in enumerate(items[:n]):
        bx = x + i * (cw + 12)
        parts.append(_rect(bx, y, cw, h, fill=fills[i], stroke=inks[i], rx=10))
        parts.append(_ml(bx + 10, y + 28, _wrap(a, max(8, int(cw / 8)), 2), size=13, fill=inks[i], weight=800))
        parts.append(_ml(bx + 10, y + 70, _wrap(b, max(10, int(cw / 7.2)), 5), size=11, fill=MUTED))
    return "".join(parts)


def _checklist(x, y, w, h, dos: list[str], dont: str) -> str:
    parts = [_t(x, y + 14, "Do", size=12, fill=WORK_INK, weight=800)]
    yy = y + 34
    for line in dos[:4] or ["Name the box", "Then the hand-off"]:
        parts.append(_circle(x + 8, yy - 4, 6, fill="#16a34a"))
        parts.append(_t(x + 8, yy, "✓", size=10, fill="#fff", weight=800, anchor="middle"))
        parts.append(_ml(x + 22, yy - 4, _wrap(line, max(28, int((w - 28) / 7)), 2), size=12, fill=INK))
        yy += 32
    parts.append(_rect(x, y + h - 48, w, 44, fill="#fef2f2", stroke="#ef4444", rx=8))
    parts.append(_t(x + 12, y + h - 22, "Don't  " + dont[:48], size=12, fill="#b91c1c", weight=700))
    return "".join(parts)


def _nodes(p: P) -> list[tuple[str, str]]:
    if p.sid in ARCH:
        return ARCH[p.sid]
    out = []
    for i, lab in enumerate(p.flow[:4]):
        sub = p.concepts[i][1][:24] if i < len(p.concepts) else ""
        out.append((lab[:22], sub))
    return out or [("Start", ""), ("Next", ""), ("Then", ""), ("Done", "")]


def _banner_text(p: P, i: int, kind: str) -> str:
    if (p.sid, i) in BANNER:
        return BANNER[(p.sid, i)]
    if kind in KIND_BANNER:
        return KIND_BANNER[kind]
    if i == 1:
        return (p.intro.split(".")[0] + ".")[:90]
    if p.concepts:
        a, b = p.concepts[(i - 1) % len(p.concepts)]
        return f"{a}: {b}"[:90]
    return (p.pick or p.expected or p.intro)[:90]


def _scene(kind: str, x, y, w, h, p: P) -> str:
    """Dispatch on the planned kind only — never override because of sid membership."""
    if kind == "gantt":
        g = GANTT.get(p.sid) or {
            "jobs": p.flow[:3] or ["A", "B", "C"],
            "sync_s": 3,
            "async_s": 1,
            "sync_name": "One by one",
            "async_name": "Overlap the waits",
        }
        return _gantt(x, y, w, h, g)
    if kind == "hub":
        d = HUB.get(p.sid) or {"center": "loop", "sats": (p.flow + ["A", "B", "C", "D"])[:4]}
        return _hub(x, y, w, h, d["center"], d["sats"])
    if kind == "lock":
        d = LOCK.get(p.sid) or {"io": p.good, "cpu": p.bad}
        return _lock_io(x, y, w, h, d["io"], d["cpu"])
    if kind == "join":
        return _join_rows(x, y, w, h)
    if kind == "levels":
        rows = extra_levels(p.sid)
        if rows:
            return _levels(x, y, w, h, rows)
        fallback = [(a, ["#3b82f6", "#16a34a", "#ea580c", "#7c3aed"][i % 4], b) for i, (a, b) in enumerate(p.concepts[:4])]
        return _levels(x, y, w, h, fallback or [("Level", "#3b82f6", "name it")])
    if kind == "table":
        extra = extra_compare(p.sid)
        if extra:
            body = _table(x, y, w, list(extra[0]), [list(r) for r in extra[1:]])
        else:
            headers = p.headers[:3]
            rows = p.rows[:5] or [[a, b] for a, b in p.concepts[:5]]
            body = _table(x, y, w, headers, rows)
        if p.sid in GANTT and h > 140:
            th = int(h * 0.62)
            snippet = (FOOTER_CODE.get(p.sid) or (p.code, []))[0][:4]
            return body + _code_box(x, y + th + 6, w, h - th - 6, snippet, "Start / overlap")
        return body
    if kind == "code":
        note_h = 22
        return _code_box(x, y, w, h - note_h, p.code) + _t(
            x + 4, y + h - 6, (p.expected or p.pick)[:70], size=11, fill=WORK_INK, weight=700
        )
    if kind == "branch":
        return _branch(x, y, w, h, p.flow[:4])
    if kind == "messy":
        return _messy_clean(x, y, w, h, MESSY.get(p.sid, ["EC2", "S3", "RDS", "Lambda"]), _nodes(p))
    if kind == "vs":
        return _vs(x, y, w, h, p.bad_t, p.bad, p.good)
    if kind == "numbers":
        extra = extra_compare(p.sid)
        if extra:
            return _table(x, y, w, list(extra[0]), [list(r) for r in extra[1:]])
        rows = [[c[0], c[1]] for c in p.concepts[:4]] or [[a, a] for a in p.flow]
        return _table(x, y, w, ["Setup", "Remember"], rows)
    if kind == "nested":
        return _nested(x, y, w, h, p.flow[:4] or [a for a, _ in p.concepts[:4]])
    if kind == "stack":
        return _stack(x, y, w, h, p.flow[:4] or [a for a, _ in p.concepts[:4]])
    if kind == "decision":
        left = p.concepts[0][1] if p.concepts else p.good
        right = p.concepts[1][1] if len(p.concepts) > 1 else p.bad
        q = p.concepts[0][0] if p.concepts else "Which path?"
        if p.sid in LOCK:
            return _lock_io(x, y, w, h, LOCK[p.sid]["io"], LOCK[p.sid]["cpu"])
        return _decision(x, y, w, h, left, right, q)
    if kind == "metrics":
        items = p.concepts[:3] or [(a, a) for a in p.flow[:3]]
        return _metrics(x, y, w, h, items)
    if kind == "checklist":
        return _checklist(x, y, w, h, p.practice or [a for a, _ in p.concepts[:4]], p.bad_t)
    return _arch(x, y, w, h, _nodes(p), LANE2.get(p.sid) if kind == "arch" else None)


def _plan(p: P) -> list[tuple[str, str]]:
    sid = p.sid
    if sid in GANTT:
        return [
            ("gantt", "gantt"),
            ("table", "table"),
            ("hub", "hub"),
            ("lock", "lock"),
            ("numbers", "numbers"),
            ("footer", "footer"),
        ]
    if sid in JOIN_IDS:
        return [
            ("join", "join"),
            ("table", "table"),
            ("code", "code"),
            ("vs", "vs"),
            ("branch", "branch"),
            ("footer", "footer"),
        ]
    if sid in MESSY:
        return [
            ("arch", "arch"),
            ("table", "table"),
            ("messy", "messy"),
            ("code", "code"),
            ("branch", "branch"),
            ("footer", "footer"),
        ]
    scenes: list[tuple[str, str]] = []
    used: set[str] = set()
    for w in widgets_for(sid):
        k = MAP_SCENE.get(w, "arch")
        if k in used:
            continue
        used.add(k)
        scenes.append((w, k))
        if len(scenes) == 5:
            break
    for k in ("table", "code", "vs", "arch", "checklist"):
        if len(scenes) == 5:
            break
        if k not in used:
            used.add(k)
            scenes.append((k, k))
    scenes.append(("footer", "footer"))
    return scenes


def _footer(x, y, w, h, p: P) -> str:
    cw = (w - 30) / 4
    dual = FOOTER_CODE.get(p.sid)
    left, right = (dual[0], dual[1]) if dual else (p.code[:4], p.code[4:] or p.code[:3])
    pick = PICK_ROWS.get(p.track, PICK_ROWS["dotnet"])
    cs = CS_TABLE.get(p.track, CS_TABLE["dotnet"])
    parts = [
        _code_box(x, y, cw, h, left, "# path A"),
        _code_box(x + cw + 10, y, cw, h, right, "# path B"),
        _rect(x + 2 * cw + 20, y, cw, h, fill="#fef9c3", stroke="#ca8a04", rx=10),
        _t(x + 2 * cw + 30, y + 20, "Pick rule (big idea)", size=12, fill="#854d0e", weight=800),
    ]
    yy = y + 40
    for kind, label, advice in pick[:3]:
        parts.append(_icon(kind, x + 2 * cw + 28, yy))
        parts.append(_t(x + 2 * cw + 68, yy + 12, label[:22], size=11, fill="#713f12", weight=800))
        parts.append(_t(x + 2 * cw + 68, yy + 26, advice[:28], size=10, fill="#854d0e", weight=500))
        yy += 44
    tx = x + 3 * cw + 30
    parts.append(_rect(tx, y, cw, h, fill="#f5f3ff", stroke="#7c3aed", rx=10))
    parts.append(_t(tx + 10, y + 20, "Quick C# comparison", size=12, fill="#5b21b6", weight=800))
    parts.append(_rect(tx + 10, y + 32, cw - 20, 22, fill="#5b21b6", stroke=None, rx=4))
    parts.append(_t(tx + 18, y + 48, cs[0][0][:14], size=10, fill="#fff", weight=700))
    parts.append(_t(tx + cw / 2, y + 48, cs[0][1][:14], size=10, fill="#fff", weight=700))
    yy = y + 70
    for a, b in cs[1:5]:
        parts.append(_t(tx + 14, yy, a[:18], size=11, fill=INK, weight=600))
        parts.append(_t(tx + cw / 2, yy, b[:18], size=11, fill="#5b21b6", weight=600))
        yy += 22
    return "".join(parts)


def svg_for_skill(n: int, skill: dict[str, Any], *, track: str) -> str:
    p = _ctx(skill, track, n)
    plan = _plan(p)
    m, g = 16, 12
    header = 62
    top_h, mid_h, foot_h = 268, 268, 390
    y1 = header
    y2 = y1 + top_h + g
    y3 = y2 + mid_h + g
    pw3 = (1536 - 2 * m - 2 * g) / 3
    pw2 = (1536 - 2 * m - g) / 2
    slots = [
        (m, y1, pw3, top_h),
        (m + pw3 + g, y1, pw3, top_h),
        (m + 2 * (pw3 + g), y1, pw3, top_h),
        (m, y2, pw2, mid_h),
        (m + pw2 + g, y2, pw2, mid_h),
        (m, y3, 1536 - 2 * m, foot_h),
    ]
    parts = [
        _rect(0, 0, 1536, 1024, fill=PAGE, stroke=None, rx=0),
        _t(768, 36, f"{p.title}  –  Visual Guide", size=26, fill=NAVY, weight=800, anchor="middle"),
        _t(768, 56, f"{p.label}  ·  {p.sid}", size=12, fill=MUTED, weight=500, anchor="middle"),
    ]
    for i, ((title_key, kind), (x, y, w, h)) in enumerate(zip(plan, slots), 1):
        ink = INKS[(i - 1) % 6]
        title = PANEL_TITLE.get((p.sid, title_key)) or TITLES.get(title_key) or TITLES.get(kind, title_key)
        parts.append(_card(x, y, w, h, i, title, ink))
        parts.append(_pill(x + 12, y + 40, w - 24, _banner_text(p, i, kind), PILLS[(i - 1) % 6], PILL_TX[(i - 1) % 6]))
        inner_y, inner_h = y + 76, h - 88
        if kind == "footer":
            parts.append(_footer(x + 12, inner_y, w - 24, inner_h, p))
        else:
            parts.append(_scene(kind, x + 12, inner_y, w - 24, inner_h, p))
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
    mapping = {}
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
    <span>One-page poster in the Python Visual Guide style: timelines, tables, code, C# map.
      Click the thumbnail to open full size.</span>
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
