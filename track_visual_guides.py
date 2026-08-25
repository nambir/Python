"""Per-slide SVG visual guides — each topic gets its own page layout.

White/light paper. Not a shared 6-panel grid. Layouts live in LAYOUT_BY_ID.
"""

from __future__ import annotations

import html as html_mod
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from track_visual_flows import FLOW_BY_ID, compare_pair, layout_kind

FONT = "Segoe UI,Arial,sans-serif"
MONO = "Consolas,Menlo,monospace"

TRACK_LABEL = {
    "dotnet": ".NET",
    "angular": "Angular",
    "sql": "SQL Server",
    "aws": "AWS",
}

BLUE, GREEN, ORANGE, YELLOW = "#dbeafe", "#dcfce7", "#ffedd5", "#fef9c3"
BLUE_INK, GREEN_INK, ORANGE_INK, NAVY = "#1e40af", "#166534", "#9a3412", "#1e3a5f"
PAGE, PANEL, BORDER, MUTED, INK = "#ffffff", "#f8fafc", "#cbd5e1", "#475569", "#0f172a"

ACCENTS = {
    "hero_flow": "#1e3a5f",
    "vs_split": "#0f766e",
    "loop": "#6d28d9",
    "layers": "#1d4ed8",
    "timeline": "#b45309",
    "fork": "#be123c",
    "cards": "#0369a1",
    "before_after": "#15803d",
    "swimlane": "#4338ca",
    "star_story": "#9a3412",
    "code_callout": "#334155",
    "drill": "#7c3aed",
    "containment": "#0e7490",
    "hub": "#c2410c",
    "zigzag": "#166534",
    "matrix": "#1e40af",
}

FILLS = [BLUE, GREEN, ORANGE, YELLOW]
INKS = [BLUE_INK, GREEN_INK, ORANGE_INK, "#854d0e"]

CS_HINTS = {
    "angular": [
        ("Component", "Razor component / UserControl"),
        ("Observable", "IAsyncEnumerable / IObservable"),
        ("Interceptor", "DelegatingHandler / middleware"),
        ("CanActivate", "[Authorize] on the API still required"),
    ],
    "sql": [
        ("JOIN", "LINQ Join / EF Include"),
        ("Stored proc", "FromSqlInterpolated"),
        ("Index", "covering index + query plan"),
        ("BEGIN TRAN", "IDbContextTransaction / SaveChanges"),
    ],
    "aws": [
        ("API Gateway", "reverse proxy + JWT authorizer"),
        ("ECS task", "one running process recipe"),
        ("ECS service", "desired replica count"),
        ("IAM role", "for the task — not the Angular user"),
    ],
    "dotnet": [
        ("Interface", "the contract callers depend on"),
        ("Scoped", "one instance per HTTP request"),
        ("SaveChanges", "the unit of work"),
        ("Middleware", "runs in, then unwinds out"),
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
        dy = 0 if i == 0 else int(size * 1.25)
        parts.append(f'<tspan x="{x:.0f}" dy="{dy}">{_xml(line)}</tspan>')
    return (
        f'<text x="{x:.0f}" y="{y:.0f}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
        f'text-anchor="{anchor}" font-family="{FONT}">{"".join(parts)}</text>'
    )


def _rect(x, y, w, h, *, fill, stroke=None, sw=1.5, rx=12) -> str:
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}"{st}/>'


def _circle(cx, cy, r, *, fill, stroke=None, sw=2) -> str:
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{fill}"{st}/>'


def _arrow(x1, y1, x2, y2, color="#64748b") -> str:
    return (
        f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
        f'stroke="{color}" stroke-width="2.5" marker-end="url(#arrow)"/>'
    )


def _concepts(skill: dict[str, Any]) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for row in skill.get("table_rows") or []:
        if len(row) >= 2:
            out.append((_plain(row[0]), _plain(row[1])))
    if not out:
        for b in skill.get("def_bullets") or []:
            plain = _plain(b)
            if ":" in plain:
                a, c = plain.split(":", 1)
                out.append((a.strip(), c.strip()))
            else:
                out.append((plain[:28], plain))
    if not out:
        for sub in skill.get("subtopics") or []:
            out.append((_plain(sub), _plain(sub)))
    return out[:6]


def _code_lines(skill: dict[str, Any], max_lines: int = 8) -> list[str]:
    raw = skill.get("code") or ""
    lines = [ln.rstrip() for ln in str(raw).splitlines() if ln.strip()]
    if not lines:
        return ["// no sample — walk the diagram out loud"]
    return [ln[:58] for ln in lines[:max_lines]]


def _mistake(skill: dict[str, Any]) -> tuple[str, str, str]:
    m = (skill.get("mistakes") or [None])[0]
    if not m or len(m) < 3:
        return ("Weak answer", "Definition only", "Project story + evidence")
    return (_plain(m[0]), _plain(m[1]), _plain(m[2]))


def _has_word(blob: str, word: str) -> bool:
    return re.search(r"\b" + re.escape(word) + r"\b", blob, flags=re.I) is not None


def _story_flow(skill: dict[str, Any], track: str) -> list[str]:
    sid = skill.get("id") or ""
    if sid in FLOW_BY_ID:
        return list(FLOW_BY_ID[sid])
    labels = [c[0][:22] for c in _concepts(skill)[:4] if c[0]]
    while len(labels) < 4:
        labels.append("…")
    return labels[:4]


def _cs_rows_for(skill: dict[str, Any], track: str) -> list[tuple[str, str]]:
    hints = CS_HINTS.get(track, CS_HINTS["dotnet"])
    blob = " ".join(
        [
            skill.get("title") or "",
            " ".join(skill.get("subtopics") or []),
            " ".join(_plain(b) for b in (skill.get("def_bullets") or [])[:4]),
        ]
    )
    picked = [h for h in hints if _has_word(blob, h[0].split()[0])]
    if len(picked) < 2:
        picked = list(hints)
    return picked[:2]


def _table(x, y, w, headers: list[str], rows: list[list[str]], row_h: int = 36) -> str:
    if not headers:
        headers = ["Idea", "Remember"]
    cols = max(2, min(3, len(headers)))
    headers = headers[:cols]
    col_w = w / cols
    parts = [_rect(x, y, w, row_h, fill=NAVY, stroke=None, rx=8)]
    for i, h in enumerate(headers):
        parts.append(_t(x + i * col_w + 10, y + 24, h[:24], size=12, fill="#fff", weight=700))
    for r, row in enumerate(rows[:5]):
        yy = y + row_h * (r + 1)
        bg = "#ffffff" if r % 2 == 0 else "#eff6ff"
        parts.append(_rect(x, yy, w, row_h, fill=bg, stroke="#e2e8f0", sw=1, rx=0))
        for i in range(cols):
            cell = _plain(row[i] if i < len(row) else "")
            parts.append(_t(x + i * col_w + 10, yy + 24, cell[:32], size=12, fill=INK, weight=500))
    return "".join(parts)


def _when_panel(x, y, w, h, bad_title: str, bad: str, good_title: str, good: str) -> str:
    hw = (w - 14) / 2
    parts = [
        _rect(x, y, hw, h, fill="#fef2f2", stroke="#ef4444", rx=12),
        _t(x + 14, y + 26, "✗  " + bad_title[:26], size=14, fill="#b91c1c", weight=800),
        _ml(x + 14, y + 50, _wrap(bad, 32, 8), size=13, fill="#7f1d1d", weight=500),
    ]
    gx = x + hw + 14
    parts += [
        _rect(gx, y, hw, h, fill="#f0fdf4", stroke="#22c55e", rx=12),
        _t(gx + 14, y + 26, "✓  " + good_title[:26], size=14, fill="#166534", weight=800),
        _ml(gx + 14, y + 50, _wrap(good, 32, 8), size=13, fill="#14532d", weight=500),
    ]
    return "".join(parts)


@dataclass
class Ctx:
    label: str
    sid: str
    title: str
    intro: str
    accent: str
    layout: str
    flow: list[str]
    concepts: list[tuple[str, str]]
    headers: list[str]
    rows: list[list[str]]
    bad_t: str
    bad: str
    good: str
    pick: str
    code: list[str]
    cs: list[tuple[str, str]]
    pair: tuple[str, str, str, str]


def _chrome(c: Ctx) -> str:
    return (
        _rect(0, 0, 1536, 1024, fill=PAGE, stroke=None, rx=0)
        + _rect(0, 0, 1536, 8, fill=c.accent, stroke=None, rx=0)
        + _t(28, 36, f"{c.label}  ·  {c.sid}  ·  {c.layout.replace('_', ' ')}", size=14, fill=c.accent, weight=700)
        + _t(28, 72, c.title[:72], size=32, fill=INK, weight=800)
        + _ml(28, 96, _wrap(c.intro, 150, 2), size=14, fill=MUTED, weight=500)
    )


def _pick_bar(c: Ctx, y: float = 930) -> str:
    return (
        _rect(28, y, 1480, 70, fill=YELLOW, stroke="#ca8a04", rx=12)
        + _t(44, y + 28, "Say this", size=13, fill="#854d0e", weight=800)
        + _ml(44, y + 48, _wrap(c.pick, 140, 1), size=14, fill="#713f12", weight=600)
    )


def _pair_of(c: Ctx) -> tuple[str, str, str, str]:
    if c.pair and c.pair[0]:
        return c.pair
    if len(c.concepts) >= 2:
        return (c.concepts[0][0], c.concepts[0][1], c.concepts[1][0], c.concepts[1][1])
    f = c.flow + ["…", "…"]
    return (f[0], "", f[1], "")


def _lay_hero_flow(c: Ctx) -> str:
    parts = [_chrome(c)]
    boxes = c.flow[:4]
    n = len(boxes)
    gap, x0, y, h = 22, 28, 150, 150
    bw = (1480 - gap * (n - 1)) / n
    for i, lab in enumerate(boxes):
        bx = x0 + i * (bw + gap)
        parts.append(_rect(bx, y, bw, h, fill=FILLS[i], stroke=INKS[i], sw=2, rx=16))
        parts.append(_circle(bx + 28, y + 28, 18, fill=c.accent))
        parts.append(_t(bx + 28, y + 34, str(i + 1), size=16, fill="#fff", weight=800, anchor="middle"))
        parts.append(_ml(bx + 16, y + 78, _wrap(lab, 18, 3), size=18, fill=INKS[i], weight=800))
        if i < n - 1:
            parts.append(_arrow(bx + bw, y + h / 2, bx + bw + gap, y + h / 2, c.accent))
    parts.append(_when_panel(28, 330, 1480, 220, c.bad_t, c.bad, "Do this", c.good))
    parts.append(_rect(28, 570, 900, 340, fill="#f1f5f9", stroke="#94a3b8", rx=14))
    parts.append(_t(48, 600, "Code you can point at", size=15, fill=c.accent, weight=800))
    yy = 630
    for ln in c.code[:10]:
        parts.append(_t(48, yy, ln[:78], size=14, fill=INK, weight=500, family=MONO))
        yy += 22
    parts.append(_rect(948, 570, 560, 340, fill=PANEL, stroke=BORDER, rx=14))
    parts.append(_t(968, 600, "Remember", size=15, fill=c.accent, weight=800))
    for i, (a, b) in enumerate(c.concepts[:4]):
        parts.append(_t(968, 640 + i * 60, a[:28], size=14, fill=INK, weight=800))
        parts.append(_ml(968, 660 + i * 60, _wrap(b, 42, 2), size=12, fill=MUTED))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_vs_split(c: Ctx) -> str:
    a, ad, b, bd = _pair_of(c)
    parts = [_chrome(c)]
    parts.append(_rect(28, 140, 700, 760, fill=BLUE, stroke=BLUE_INK, sw=2, rx=18))
    parts.append(_rect(808, 140, 700, 760, fill=GREEN, stroke=GREEN_INK, sw=2, rx=18))
    parts.append(_circle(768, 420, 36, fill=c.accent))
    parts.append(_t(768, 428, "VS", size=18, fill="#fff", weight=800, anchor="middle"))
    parts.append(_t(48, 190, a[:32], size=26, fill=BLUE_INK, weight=800))
    parts.append(_ml(48, 240, _wrap(ad, 48, 8), size=16, fill="#1e3a5f"))
    parts.append(_t(828, 190, b[:32], size=26, fill=GREEN_INK, weight=800))
    parts.append(_ml(828, 240, _wrap(bd, 48, 8), size=16, fill="#14532d"))
    extra = c.concepts[2:4]
    if extra:
        parts.append(_t(48, 520, extra[0][0][:28], size=15, fill=BLUE_INK, weight=800))
        parts.append(_ml(48, 548, _wrap(extra[0][1], 48, 5), size=14, fill=MUTED))
        if len(extra) > 1:
            parts.append(_t(828, 520, extra[1][0][:28], size=15, fill=GREEN_INK, weight=800))
            parts.append(_ml(828, 548, _wrap(extra[1][1], 48, 5), size=14, fill=MUTED))
    parts.append(_t(48, 780, "✗  " + c.bad_t[:40], size=14, fill="#b91c1c", weight=800))
    parts.append(_ml(48, 808, _wrap(c.bad, 50, 3), size=13, fill="#7f1d1d"))
    parts.append(_t(828, 780, "✓  Do this", size=14, fill="#166534", weight=800))
    parts.append(_ml(828, 808, _wrap(c.good, 50, 3), size=13, fill="#14532d"))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_loop(c: Ctx) -> str:
    parts = [_chrome(c)]
    cx, cy, r = 520, 480, 210
    parts.append(_circle(cx, cy, 70, fill=c.accent))
    parts.append(_ml(cx, cy - 8, _wrap("until exit", 12, 2), size=14, fill="#fff", weight=800, anchor="middle"))
    pos = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    for i, (px, py) in enumerate(pos):
        parts.append(_rect(px - 120, py - 40, 240, 80, fill=FILLS[i], stroke=INKS[i], sw=2, rx=14))
        parts.append(_t(px, py - 8, str(i + 1), size=12, fill=INKS[i], weight=800, anchor="middle"))
        parts.append(_t(px, py + 18, c.flow[i][:22], size=15, fill=INKS[i], weight=800, anchor="middle"))
    parts.append(_arrow(cx + 40, cy - r, cx + r - 40, cy - 20, c.accent))
    parts.append(_arrow(cx + r, cy + 40, cx + 40, cy + r, c.accent))
    parts.append(_arrow(cx - 40, cy + r, cx - r + 40, cy + 20, c.accent))
    parts.append(_arrow(cx - r, cy - 40, cx - 40, cy - r, c.accent))
    parts.append(_rect(860, 140, 648, 760, fill=PANEL, stroke=BORDER, rx=16))
    parts.append(_t(880, 180, "Name the exit", size=18, fill=c.accent, weight=800))
    parts.append(_when_panel(880, 210, 608, 280, c.bad_t, c.bad, "Do this", c.good))
    parts.append(_t(880, 530, "Code", size=15, fill=c.accent, weight=800))
    yy = 560
    for ln in c.code[:8]:
        parts.append(_t(880, yy, ln[:48], size=13, fill=INK, weight=500, family=MONO))
        yy += 20
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_layers(c: Ctx) -> str:
    parts = [_chrome(c)]
    labels = [x[0] for x in c.concepts[:4]] or c.flow
    y = 140
    h = 150
    for i, lab in enumerate(labels[:4]):
        parts.append(_rect(28, y, 1000, h, fill=FILLS[i], stroke=INKS[i], sw=2, rx=16))
        parts.append(_circle(70, y + h / 2, 22, fill=c.accent))
        parts.append(_t(70, y + h / 2 + 6, str(i + 1), size=16, fill="#fff", weight=800, anchor="middle"))
        parts.append(_t(110, y + 48, lab[:40], size=22, fill=INKS[i], weight=800))
        det = c.concepts[i][1] if i < len(c.concepts) else ""
        parts.append(_ml(110, y + 82, _wrap(det, 70, 3), size=14, fill=MUTED))
        if i < 3:
            parts.append(_t(528, y + h + 14, "↓", size=20, fill=c.accent, weight=800, anchor="middle"))
        y += h + 18
    parts.append(_rect(1050, 140, 458, 760, fill=PANEL, stroke=BORDER, rx=16))
    parts.append(_t(1070, 180, "When / when not", size=16, fill=c.accent, weight=800))
    parts.append(_when_panel(1070, 210, 418, 400, c.bad_t, c.bad, "Do this", c.good))
    parts.append(_ml(1070, 650, _wrap(c.pick, 38, 6), size=14, fill="#713f12", weight=600))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_timeline(c: Ctx) -> str:
    parts = [_chrome(c)]
    parts.append(_rect(80, 280, 1376, 8, fill=c.accent, stroke=None, rx=4))
    n = 4
    for i, lab in enumerate(c.flow[:n]):
        x = 140 + i * 340
        parts.append(_circle(x, 284, 34, fill=FILLS[i], stroke=INKS[i], sw=3))
        parts.append(_t(x, 292, str(i + 1), size=20, fill=INKS[i], weight=800, anchor="middle"))
        parts.append(_rect(x - 140, 360, 280, 200, fill=PANEL, stroke=INKS[i], sw=2, rx=14))
        parts.append(_t(x, 400, lab[:22], size=16, fill=INKS[i], weight=800, anchor="middle"))
        det = c.concepts[i][1] if i < len(c.concepts) else ""
        parts.append(_ml(x - 120, 440, _wrap(det, 28, 5), size=13, fill=MUTED))
    parts.append(_when_panel(28, 600, 1480, 300, c.bad_t, c.bad, "Do this", c.good))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_fork(c: Ctx) -> str:
    a, ad, b, bd = _pair_of(c)
    parts = [_chrome(c)]
    parts.append(
        f'<polygon points="768,160 860,250 768,340 676,250" fill="{YELLOW}" stroke="{c.accent}" stroke-width="2.5"/>'
    )
    parts.append(_t(768, 246, "Which path?", size=16, fill=c.accent, weight=800, anchor="middle"))
    parts.append(_t(768, 270, "Say the rule", size=12, fill=MUTED, weight=600, anchor="middle"))
    parts.append(_arrow(720, 330, 380, 400, c.accent))
    parts.append(_arrow(816, 330, 1156, 400, c.accent))
    parts.append(_rect(28, 400, 700, 360, fill=BLUE, stroke=BLUE_INK, sw=2, rx=16))
    parts.append(_rect(808, 400, 700, 360, fill=GREEN, stroke=GREEN_INK, sw=2, rx=16))
    parts.append(_t(48, 450, a[:30], size=22, fill=BLUE_INK, weight=800))
    parts.append(_ml(48, 500, _wrap(ad, 50, 8), size=15, fill="#1e3a5f"))
    parts.append(_t(828, 450, b[:30], size=22, fill=GREEN_INK, weight=800))
    parts.append(_ml(828, 500, _wrap(bd, 50, 8), size=15, fill="#14532d"))
    parts.append(_t(48, 800, "✗  " + c.bad_t[:40], size=14, fill="#b91c1c", weight=800))
    parts.append(_ml(48, 828, _wrap(c.bad, 50, 3), size=13, fill="#7f1d1d"))
    parts.append(_t(828, 800, "✓  " + c.good[:50], size=14, fill="#166534", weight=800))
    parts.append(_ml(828, 828, _wrap(c.good, 50, 3), size=13, fill="#14532d"))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_cards(c: Ctx) -> str:
    parts = [_chrome(c)]
    items = c.concepts[:4] or [(f, f) for f in c.flow]
    coords = [(28, 140), (788, 140), (28, 500), (788, 500)]
    for i, ((x, y), (lab, det)) in enumerate(zip(coords, items)):
        parts.append(_rect(x, y, 720, 330, fill=FILLS[i], stroke=INKS[i], sw=2, rx=18))
        parts.append(_circle(x + 48, y + 48, 26, fill=c.accent))
        parts.append(_t(x + 48, y + 56, str(i + 1), size=20, fill="#fff", weight=800, anchor="middle"))
        parts.append(_t(x + 90, y + 56, lab[:34], size=22, fill=INKS[i], weight=800))
        parts.append(_ml(x + 36, y + 110, _wrap(det, 52, 8), size=16, fill=INK))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_before_after(c: Ctx) -> str:
    parts = [_chrome(c)]
    parts.append(_rect(28, 140, 730, 760, fill="#fef2f2", stroke="#ef4444", sw=2, rx=18))
    parts.append(_rect(778, 140, 730, 760, fill="#f0fdf4", stroke="#22c55e", sw=2, rx=18))
    parts.append(_t(56, 190, "Before — " + c.bad_t[:28], size=24, fill="#b91c1c", weight=800))
    parts.append(_ml(56, 240, _wrap(c.bad, 48, 10), size=18, fill="#7f1d1d"))
    parts.append(_t(56, 560, "What it sounds like", size=14, fill="#b91c1c", weight=800))
    for i, ln in enumerate(c.code[:6]):
        parts.append(_t(56, 600 + i * 24, ln[:52], size=14, fill=INK, weight=500, family=MONO))
    parts.append(_t(806, 190, "After — do this", size=24, fill="#166534", weight=800))
    parts.append(_ml(806, 240, _wrap(c.good, 48, 8), size=18, fill="#14532d"))
    parts.append(_t(806, 520, "Path to say", size=14, fill="#166534", weight=800))
    for i, lab in enumerate(c.flow[:4]):
        parts.append(_rect(806, 550 + i * 70, 670, 58, fill="#fff", stroke=GREEN_INK, rx=10))
        parts.append(_circle(836, 579, 16, fill="#166534"))
        parts.append(_t(836, 585, str(i + 1), size=13, fill="#fff", weight=800, anchor="middle"))
        parts.append(_t(864, 585, lab[:40], size=16, fill="#166534", weight=800))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_swimlane(c: Ctx) -> str:
    parts = [_chrome(c)]
    lanes = c.flow[:4]
    h = 150
    y = 150
    for i, lab in enumerate(lanes):
        parts.append(_rect(28, y, 1480, h, fill=FILLS[i], stroke=INKS[i], sw=2, rx=14))
        parts.append(_rect(28, y, 220, h, fill=c.accent, stroke=None, rx=14))
        parts.append(_t(138, y + 88, lab[:16], size=16, fill="#fff", weight=800, anchor="middle"))
        det = c.concepts[i][1] if i < len(c.concepts) else ""
        parts.append(_ml(270, y + 50, _wrap(det, 90, 4), size=16, fill=INK))
        if i < len(lanes) - 1:
            parts.append(_t(140, y + h + 16, "↓", size=18, fill=c.accent, weight=800, anchor="middle"))
        y += h + 18
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_star_story(c: Ctx) -> str:
    parts = [_chrome(c)]
    tags = ["S — Situation", "T — Task", "A — Action", "R — Result"]
    coords = [(28, 140), (788, 140), (28, 500), (788, 500)]
    for i, ((x, y), tag) in enumerate(zip(coords, tags)):
        lab = c.flow[i] if i < len(c.flow) else tag
        det = c.concepts[i][1] if i < len(c.concepts) else ""
        parts.append(_rect(x, y, 720, 330, fill=FILLS[i], stroke=INKS[i], sw=2, rx=18))
        parts.append(_t(x + 28, y + 48, tag, size=14, fill=INKS[i], weight=800))
        parts.append(_t(x + 28, y + 90, lab[:36], size=22, fill=INK, weight=800))
        parts.append(_ml(x + 28, y + 130, _wrap(det, 50, 7), size=15, fill=MUTED))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_code_callout(c: Ctx) -> str:
    parts = [_chrome(c)]
    parts.append(_rect(28, 140, 780, 760, fill="#f1f5f9", stroke="#94a3b8", rx=16))
    parts.append(_t(48, 178, "Sample", size=14, fill=c.accent, weight=700))
    yy = 220
    for ln in c.code[:16]:
        parts.append(_t(48, yy, ln[:62], size=15, fill=INK, weight=500, family=MONO))
        yy += 28
    y = 140
    for i, (lab, det) in enumerate(c.concepts[:4]):
        parts.append(_rect(828, y, 680, 175, fill=FILLS[i], stroke=INKS[i], sw=2, rx=14))
        parts.append(_circle(858, y + 36, 18, fill=c.accent))
        parts.append(_t(858, y + 42, str(i + 1), size=14, fill="#fff", weight=800, anchor="middle"))
        parts.append(_t(888, y + 42, lab[:30], size=16, fill=INKS[i], weight=800))
        parts.append(_ml(848, y + 72, _wrap(det, 48, 4), size=14, fill=INK))
        y += 190
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_drill(c: Ctx) -> str:
    parts = [_chrome(c)]
    qs = ["What is it?", "Where did you use it?", "Why that choice?", "How do you prove it?", "What would you not claim?"]
    answers = [x[1] for x in c.concepts[:4]] + [c.pick]
    y = 140
    for i, q in enumerate(qs):
        parts.append(_rect(28, y, 1480, 140, fill=FILLS[i % 4], stroke=INKS[i % 4], sw=2, rx=14))
        parts.append(_circle(80, y + 70, 28, fill=c.accent))
        parts.append(_t(80, y + 78, str(i + 1), size=20, fill="#fff", weight=800, anchor="middle"))
        parts.append(_t(130, y + 48, q, size=20, fill=INKS[i % 4], weight=800))
        ans = answers[i] if i < len(answers) else c.flow[min(i, 3)]
        parts.append(_ml(130, y + 82, _wrap(ans, 110, 2), size=16, fill=INK))
        y += 156
    return "".join(parts)


def _lay_containment(c: Ctx) -> str:
    parts = [_chrome(c)]
    boxes = [
        (80, 150, 900, 740, FILLS[0], INKS[0], c.flow[0]),
        (160, 250, 740, 540, FILLS[1], INKS[1], c.flow[1]),
        (250, 360, 560, 330, FILLS[2], INKS[2], c.flow[2]),
        (340, 450, 380, 160, FILLS[3], INKS[3], c.flow[3]),
    ]
    for x, y, w, h, fill, ink, lab in boxes:
        parts.append(_rect(x, y, w, h, fill=fill, stroke=ink, sw=2, rx=18))
        parts.append(_t(x + 20, y + 34, lab[:36], size=18, fill=ink, weight=800))
    parts.append(_rect(1020, 150, 488, 740, fill=PANEL, stroke=BORDER, rx=16))
    parts.append(_t(1040, 190, "When / when not", size=16, fill=c.accent, weight=800))
    parts.append(_when_panel(1040, 220, 448, 360, c.bad_t, c.bad, "Do this", c.good))
    parts.append(_ml(1040, 620, _wrap(c.pick, 38, 8), size=14, fill="#713f12"))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_hub(c: Ctx) -> str:
    parts = [_chrome(c)]
    cx, cy = 520, 500
    parts.append(_circle(cx, cy, 90, fill=c.accent))
    parts.append(_ml(cx, cy - 10, _wrap(c.title[:24], 12, 3), size=14, fill="#fff", weight=800, anchor="middle"))
    sats = [(520, 220), (900, 500), (520, 780), (140, 500)]
    items = c.concepts[:4] or [(f, "") for f in c.flow]
    for i, ((sx, sy), (lab, det)) in enumerate(zip(sats, items)):
        parts.append(_arrow(cx, cy, sx, sy, c.accent))
        parts.append(_rect(sx - 150, sy - 70, 300, 140, fill=FILLS[i], stroke=INKS[i], sw=2, rx=14))
        parts.append(_t(sx, sy - 24, lab[:22], size=15, fill=INKS[i], weight=800, anchor="middle"))
        parts.append(_ml(sx, sy + 8, _wrap(det, 26, 3), size=12, fill=MUTED, anchor="middle"))
    parts.append(_rect(1080, 150, 428, 740, fill=PANEL, stroke=BORDER, rx=16))
    parts.append(_when_panel(1100, 180, 388, 420, c.bad_t, c.bad, "Do this", c.good))
    parts.append(_ml(1100, 640, _wrap(c.pick, 32, 8), size=14, fill="#713f12"))
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_zigzag(c: Ctx) -> str:
    parts = [_chrome(c)]
    xs = [80, 780, 80, 780]
    y = 150
    for i, lab in enumerate(c.flow[:4]):
        x = xs[i]
        parts.append(_rect(x, y, 680, 150, fill=FILLS[i], stroke=INKS[i], sw=2, rx=16))
        parts.append(_circle(x + 40, y + 75, 24, fill=c.accent))
        parts.append(_t(x + 40, y + 82, str(i + 1), size=18, fill="#fff", weight=800, anchor="middle"))
        parts.append(_t(x + 80, y + 55, lab[:32], size=20, fill=INKS[i], weight=800))
        det = c.concepts[i][1] if i < len(c.concepts) else ""
        parts.append(_ml(x + 80, y + 88, _wrap(det, 48, 2), size=14, fill=MUTED))
        if i < 3:
            x2 = xs[i + 1]
            parts.append(_arrow(x + 340, y + 150, x2 + 340, y + 168, c.accent))
        y += 180
    parts.append(_pick_bar(c))
    return "".join(parts)


def _lay_matrix(c: Ctx) -> str:
    parts = [_chrome(c)]
    parts.append(_table(28, 150, 1480, c.headers, c.rows, row_h=70))
    parts.append(_when_panel(28, 620, 1480, 280, c.bad_t, c.bad, "Do this", c.good))
    parts.append(_pick_bar(c))
    return "".join(parts)


LAYOUT_FN = {
    "hero_flow": _lay_hero_flow,
    "vs_split": _lay_vs_split,
    "loop": _lay_loop,
    "layers": _lay_layers,
    "timeline": _lay_timeline,
    "fork": _lay_fork,
    "cards": _lay_cards,
    "before_after": _lay_before_after,
    "swimlane": _lay_swimlane,
    "star_story": _lay_star_story,
    "code_callout": _lay_code_callout,
    "drill": _lay_drill,
    "containment": _lay_containment,
    "hub": _lay_hub,
    "zigzag": _lay_zigzag,
    "matrix": _lay_matrix,
}


def svg_for_skill(n: int, skill: dict[str, Any], *, track: str) -> str:
    sid = skill.get("id") or f"S{n:02d}"
    layout = layout_kind(sid)
    concepts = _concepts(skill)
    pair = compare_pair(sid)
    ctx = Ctx(
        label=TRACK_LABEL.get(track, track.upper()),
        sid=sid,
        title=_plain(skill.get("title") or f"Slide {n}"),
        intro=_plain(skill.get("def_intro") or ""),
        accent=ACCENTS.get(layout, NAVY),
        layout=layout,
        flow=_story_flow(skill, track),
        concepts=concepts,
        headers=[_plain(h) for h in (skill.get("table_headers") or ["Idea", "Remember"])],
        rows=[[_plain(c) for c in r] for r in (skill.get("table_rows") or concepts)],
        bad_t=_mistake(skill)[0],
        bad=_mistake(skill)[1],
        good=_mistake(skill)[2],
        pick=_plain(skill.get("level3") or skill.get("interview") or "Explain with a project story."),
        code=_code_lines(skill),
        cs=_cs_rows_for(skill, track),
        pair=pair if pair else ("", "", "", ""),
    )
    body = LAYOUT_FN.get(layout, _lay_hero_flow)(ctx)
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
        + body
        + "\n</svg>\n"
    )


def write_svg_posters(
    skills: list[dict[str, Any]],
    images_dir: Path,
    *,
    track: str,
) -> dict[int, tuple[str, str, int]]:
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
    <span>Unique layout for this topic (not a shared 6-panel stencil). Click the thumbnail for full size.</span>
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
