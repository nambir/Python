"""Python-poster chrome for interview visual guides (1536×1024, 3+2+1).

Learnings from AWS W03/W04 vs Python PNGs:
- Arrow gaps must be ≥28px so the shaft is visible (marker used to eat 12px lines).
- Body type 13px (captions 11, code 12, card title 15).
- Widgets fill inner height (pass h= into table / vs_boxes / code_out / footer3).
- Unique diagram per panel; 3-col footer; interview trap as red ✕ vs green ✓.
"""

from __future__ import annotations

import html as html_mod
import re
from pathlib import Path

W, H = 1536, 1024
FONT = "Segoe UI,Arial,sans-serif"
MONO = "Consolas,Menlo,monospace"
PAGE, INK, MUTED, NAVY = "#ffffff", "#0f172a", "#475569", "#1e3a5f"
INKS = ["#2563eb", "#16a34a", "#4f46e5", "#7c3aed", "#ea580c", "#e11d48"]
PILLS = ["#dbeafe", "#dcfce7", "#ede9fe", "#f3e8ff", "#ffedd5", "#ffe4e6"]
PILL_TX = ["#1e40af", "#166534", "#5b21b6", "#6b21a8", "#9a3412", "#9f1239"]
TBL = ["#1d4ed8", "#15803d", "#4338ca", "#6d28d9", "#c2410c", "#be123c"]


def xml(text: str) -> str:
    return (
        (text or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def wrap(text: str, width: int, max_lines: int) -> list[str]:
    words = (text or "").split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if len(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
            if len(lines) >= max_lines:
                break
    if cur and len(lines) < max_lines:
        lines.append(cur)
    if len(lines) == max_lines and len(" ".join(words)) > width * max_lines:
        last = lines[-1]
        if not last.endswith("…"):
            lines[-1] = last[: max(0, width - 1)].rstrip() + "…"
    return lines or [""]


def t(x, y, text, *, size=12, fill=INK, weight=600, anchor="start", family=FONT) -> str:
    return (
        f'<text x="{x:.0f}" y="{y:.0f}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
        f'text-anchor="{anchor}" font-family="{family}">{xml(text)}</text>'
    )


def ml(x, y, lines, *, size=12, fill=INK, weight=500, family=FONT) -> str:
    parts = []
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else int(size * 1.18)
        parts.append(f'<tspan x="{x:.0f}" dy="{dy}">{xml(line)}</tspan>')
    return (
        f'<text x="{x:.0f}" y="{y:.0f}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
        f'font-family="{family}">{"".join(parts)}</text>'
    )


def rect(x, y, w, h, *, fill, stroke=None, sw=1.6, rx=10) -> str:
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{rx}" fill="{fill}"{st}/>'


def circle(cx, cy, r, *, fill, stroke=None, sw=2) -> str:
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{fill}"{st}/>'


def arrow(x1, y1, x2, y2, color="#64748b", dash=False) -> str:
    """Shaft + head. Short gaps used to draw only the triangle (marker ate a 12px line)."""
    d = ' stroke-dasharray="4 3"' if dash else ""
    return (
        f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
        f'stroke="{color}" stroke-width="2.4" {d} marker-end="url(#arrow)"/>'
    )


def check(cx, cy, r=8) -> str:
    return circle(cx, cy, r, fill="#16a34a") + t(cx, cy + 4, "✓", size=11, fill="#fff", weight=800, anchor="middle")


def cross(cx, cy, r=8) -> str:
    return circle(cx, cy, r, fill="#dc2626") + t(cx, cy + 4, "✕", size=10, fill="#fff", weight=800, anchor="middle")


def lock(cx, cy) -> str:
    return (
        f'<rect x="{cx-8:.0f}" y="{cy:.0f}" width="16" height="13" rx="2" fill="#dc2626"/>'
        f'<path d="M{cx-5:.0f},{cy:.0f} v-5 a5,5 0 0 1 10,0 v5" fill="none" stroke="#dc2626" stroke-width="2.4"/>'
    )


def cloud(x, y) -> str:
    return (
        f'<ellipse cx="{x+16:.0f}" cy="{y+12:.0f}" rx="15" ry="9" fill="#93c5fd"/>'
        f'<ellipse cx="{x+7:.0f}" cy="{y+14:.0f}" rx="9" ry="7" fill="#60a5fa"/>'
        f'<ellipse cx="{x+24:.0f}" cy="{y+14:.0f}" rx="8" ry="6" fill="#3b82f6"/>'
    )


def chip(x, y) -> str:
    return rect(x, y, 28, 20, fill="#fdba74", stroke="#c2410c", sw=1.3, rx=3) + t(
        x + 14, y + 14, "CPU", size=7, fill="#7c2d12", weight=800, anchor="middle"
    )


def slots() -> list[tuple[float, float, float, float]]:
    m, g, header = 16, 12, 58
    top_h, mid_h, foot_h = 268, 268, 398
    y1 = header
    y2 = y1 + top_h + g
    y3 = y2 + mid_h + g
    pw3 = (W - 2 * m - 2 * g) / 3
    pw2 = (W - 2 * m - g) / 2
    return [
        (m, y1, pw3, top_h),
        (m + pw3 + g, y1, pw3, top_h),
        (m + 2 * (pw3 + g), y1, pw3, top_h),
        (m, y2, pw2, mid_h),
        (m + pw2 + g, y2, pw2, mid_h),
        (m, y3, W - 2 * m, foot_h),
    ]


def card(x, y, w, h, n, title, ink) -> str:
    return (
        rect(x, y, w, h, fill="#fff", stroke=ink, sw=1.5, rx=12)
        + circle(x + 22, y + 22, 11, fill=ink)
        + t(x + 22, y + 26, str(n), size=11, fill="#fff", weight=800, anchor="middle")
        + t(x + 40, y + 27, title, size=15, fill=NAVY, weight=800)
    )


def pill(x, y, w, text, fill, ink) -> str:
    return (
        rect(x, y, w, 28, fill=fill, stroke=None, rx=8)
        + t(x + 10, y + 19, text, size=13, fill=ink, weight=700)
    )


def inner(x, y, w, h):
    return x + 12, y + 72, w - 24, h - 84


def table(x, y, w, headers, rows, header_fill="#e2e8f0", row_h=32, last_green=False, header_ink=None, h=None) -> str:
    """Python-logging tables: light header, dark text — not a navy slab."""
    def _light(hx: str) -> bool:
        hx = (hx or "ffffff").lstrip("#")
        if len(hx) < 6:
            return True
        r, g, b = int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16)
        return (r * 0.3 + g * 0.59 + b * 0.11) > 170

    ink = header_ink if header_ink is not None else (NAVY if _light(header_fill) else "#fff")
    cols = len(headers)
    cw = w / cols
    chars = max(9, int(cw / 7.1))
    header_h = 26
    n_rows = max(1, len(rows))
    if h is not None and h > header_h + n_rows * 22:
        row_h = (h - header_h) / n_rows
    parts = [rect(x, y, w, header_h, fill=header_fill, stroke="#cbd5e1", sw=1, rx=4)]
    for i, hd in enumerate(headers):
        parts.append(t(x + i * cw + 8, y + 18, hd[:chars], size=13, fill=ink, weight=700))
    for r, row in enumerate(rows):
        yy = y + header_h + row_h * r
        bg = "#dcfce7" if last_green and r == len(rows) - 1 else ("#ffffff" if r % 2 == 0 else "#f8fafc")
        parts.append(rect(x, yy, w, row_h, fill=bg, stroke="#e2e8f0", sw=1, rx=0))
        text_y = yy + max(14, row_h * 0.38)
        for i in range(cols):
            cell = row[i] if i < len(row) else ""
            parts.append(ml(x + i * cw + 8, text_y, wrap(str(cell), chars, 2), size=13, fill=INK, weight=500))
    return "".join(parts)


def _code_color(ln: str) -> str:
    s = ln.strip()
    if s.startswith(("#", "//")):
        return "#16a34a"
    if s.startswith(("'", '"')) or '="' in ln or "='" in ln:
        return "#b45309"
    for kw in ("def ", "return ", "await ", "async ", "class ", "import ", "FROM ", "COPY ", "RUN ", "ADD "):
        if s.startswith(kw) or f" {kw.strip()} " in f" {s} ":
            return "#1d4ed8"
    return INK


def code_box(x, y, w, h, lines, *, bg="#eef2ff", title=None) -> str:
    parts = [rect(x, y, w, h, fill=bg, stroke="#c7d2fe", rx=8)]
    yy = y + 18
    if title:
        parts.append(t(x + 10, yy, title, size=12, fill="#3730a3", weight=800, family=MONO))
        yy += 20
    shown = list(lines) or [""]
    avail = max(16, y + h - 12 - yy)
    lh = avail / len(shown)
    for ln in shown:
        parts.append(t(x + 10, yy + min(14, lh * 0.55), ln[: max(18, int(w / 8.2))], size=12, fill=_code_color(ln), weight=500, family=MONO))
        yy += lh
    return "".join(parts)


def code_out(x, y, w, h, lines, output: str, *, title=None) -> str:
    """Code on top, sample output line underneath — Logging panel 3."""
    out_h = 32
    gap = 8
    code_h = h - out_h - gap
    return (
        code_box(x, y, w, code_h, lines, title=title)
        + rect(x, y + code_h + gap, w, out_h, fill="#fff", stroke="#cbd5e1", rx=6)
        + t(x + 10, y + code_h + gap + 22, output[: max(20, int(w / 8))], size=12, fill="#334155", weight=500, family=MONO)
    )


def log_bars(x, y, w, h, rows) -> str:
    """Logging 'five levels' pattern: full-width colored bar, label left, detail right."""
    n = max(1, len(rows))
    rh = (h - 6 * (n - 1)) / n
    parts = []
    for i, (lab, color, det) in enumerate(rows):
        yy = y + i * (rh + 6)
        ink = "#fff" if color.lower() not in {"#e2e8f0", "#cbd5e1", "#fde68a", "#fef9c3", "#dcfce7"} else NAVY
        parts.append(rect(x, yy, w, rh, fill=color, stroke=None, rx=6))
        parts.append(t(x + 12, yy + rh * 0.62, lab, size=14, fill=ink, weight=800))
        parts.append(t(x + w - 12, yy + rh * 0.62, det[: max(18, int(w / 9))], size=13, fill=ink, weight=500, anchor="end"))
    return "".join(parts)


def pipe(x, y, w, nodes, sinks=None) -> str:
    """Captioned pipeline like Logging 'how a record travels'. nodes: (title, caption)."""
    n = len(nodes)
    gap = 32
    bw = (w - gap * (n - 1)) / n
    fills = ["#dbeafe", "#e0e7ff", "#ede9fe", "#fef9c3", "#dcfce7"]
    inks = ["#1e40af", "#3730a3", "#6d28d9", "#854d0e", "#166534"]
    parts = []
    y0 = y + 8
    for i, (title, cap) in enumerate(nodes):
        bx = x + i * (bw + gap)
        parts.append(rect(bx, y0, bw, 44, fill=fills[i % 5], stroke=inks[i % 5], sw=1.4, rx=8))
        parts.append(t(bx + bw / 2, y0 + 18, title[: max(8, int(bw / 7))], size=11, fill=inks[i % 5], weight=800, anchor="middle"))
        parts.append(t(bx + bw / 2, y0 + 36, cap[: max(10, int(bw / 6.6))], size=9, fill=MUTED, weight=500, anchor="middle"))
        if i < n - 1:
            parts.append(arrow(bx + bw + 2, y0 + 22, bx + bw + gap - 2, y0 + 22))
    if sinks:
        last_x = x + (n - 1) * (bw + gap) + bw
        mid = y0 + 22
        sw_ = (w * 0.28)
        parts.append(arrow(last_x, mid - 6, x + w - sw_, y + 8))
        parts.append(arrow(last_x, mid + 6, x + w - sw_, y + 70))
        # if nodes already used full width, sinks overlay — callers should pass fewer nodes
    return "".join(parts)


def pipe_split(x, y, w, h, nodes, sink_a, sink_b) -> str:
    """Pipeline then split to two destinations (Logging formatter → console / file)."""
    n = len(nodes)
    gap = 36
    usable = w - 140
    bw = (usable - gap * (n - 1)) / n
    fills = ["#dbeafe", "#e0e7ff", "#ede9fe", "#fef3c7"]
    inks = ["#1e40af", "#3730a3", "#6d28d9", "#854d0e"]
    box_h = max(64, min(96, h * 0.48))
    y0 = y + (h - box_h) / 2
    parts = []
    for i, (title, cap) in enumerate(nodes):
        bx = x + i * (bw + gap)
        parts.append(rect(bx, y0, bw, box_h, fill=fills[i % 4], stroke=inks[i % 4], sw=1.4, rx=8))
        parts.append(t(bx + bw / 2, y0 + box_h * 0.42, title[: max(8, int(bw / 8))], size=13, fill=inks[i % 4], weight=800, anchor="middle"))
        parts.append(t(bx + bw / 2, y0 + box_h * 0.70, cap[: max(10, int(bw / 7))], size=11, fill=MUTED, weight=500, anchor="middle"))
        if i < n - 1:
            parts.append(arrow(bx + bw + 2, y0 + box_h / 2, bx + bw + gap - 2, y0 + box_h / 2))
    lx = x + n * (bw + gap) - gap
    parts.append(arrow(lx + 2, y0 + box_h * 0.28, x + w - 124, y + 24))
    parts.append(arrow(lx + 2, y0 + box_h * 0.72, x + w - 124, y + h - 36))
    parts.append(rect(x + w - 120, y + 8, 114, 40, fill="#dcfce7", stroke="#16a34a", rx=6))
    parts.append(t(x + w - 63, y + 33, sink_a[:16], size=12, fill="#166534", weight=700, anchor="middle"))
    parts.append(rect(x + w - 120, y + h - 48, 114, 40, fill="#fef9c3", stroke="#ca8a04", rx=6))
    parts.append(t(x + w - 63, y + h - 24, sink_b[:16], size=12, fill="#854d0e", weight=700, anchor="middle"))
    return "".join(parts)


def terminal(x, y, w, h, lines) -> str:
    parts = [rect(x, y, w, h, fill="#0f172a", stroke=None, rx=8)]
    shown = list(lines) or [""]
    avail = max(16, h - 24)
    lh = avail / len(shown)
    yy = y + 12 + min(14, lh * 0.45)
    for ln in shown:
        col = "#86efac" if ln.strip().startswith(">") or ln.strip().startswith("$") else "#e2e8f0"
        if "error" in ln.lower() or "unhealthy" in ln.lower() or "cannot" in ln.lower():
            col = "#fca5a5"
        parts.append(t(x + 12, yy, ln[: max(18, int(w / 7.4))], size=12, fill=col, weight=500, family=MONO))
        yy += lh
    return "".join(parts)


def flow_h(x, y, w, labels, fills=None, inks=None) -> str:
    n = len(labels)
    gap = 28
    bw = (w - gap * (n - 1)) / n
    fills = fills or ["#dbeafe", "#dcfce7", "#ffedd5", "#fef9c3", "#ede9fe"]
    inks = inks or ["#1e40af", "#166534", "#9a3412", "#854d0e", "#5b21b6"]
    parts = []
    for i, lab in enumerate(labels):
        bx = x + i * (bw + gap)
        parts.append(rect(bx, y, bw, 48, fill=fills[i % len(fills)], stroke=inks[i % len(inks)], rx=8))
        parts.append(t(bx + bw / 2, y + 32, lab[: max(8, int(bw / 8))], size=13, fill=inks[i % len(inks)], weight=700, anchor="middle"))
        if i < n - 1:
            parts.append(arrow(bx + bw + 2, y + 24, bx + bw + gap - 2, y + 24, inks[0]))
    return "".join(parts)


def flow_v(x, y, w, labels, fill="#dcfce7", ink="#166534", h=None) -> str:
    n = len(labels)
    gap = 16
    if h and n:
        bh = max(28, (h - gap * (n - 1)) / n)
    else:
        bh = 28
    parts = []
    for i, lab in enumerate(labels):
        yy = y + i * (bh + gap)
        parts.append(rect(x, yy, w, bh, fill=fill, stroke=ink, rx=6))
        parts.append(t(x + w / 2, yy + bh * 0.62, lab[: max(12, int(w / 7))], size=12, fill=ink, weight=700, anchor="middle"))
        if i < n - 1:
            parts.append(arrow(x + w / 2, yy + bh, x + w / 2, yy + bh + gap, ink))
    return "".join(parts)


def vs_boxes(x, y, w, h, bad_title, bad_lines, good_title, good_lines) -> str:
    hw = (w - 10) / 2
    inner_y, inner_h = y + 36, h - 46
    chars = max(16, int((hw - 36) / 7.2))

    def _col(cx, fill, stroke, inner_stroke, title, title_fill, lines, icon, ink):
        bits = [
            rect(cx, y, hw, h, fill=fill, stroke=stroke, sw=1.5, rx=8),
            icon(cx + 14, y + 16),
            t(cx + 28, y + 21, title, size=13, fill=title_fill, weight=800),
            rect(cx + 10, inner_y, hw - 20, inner_h, fill="#fff", stroke=inner_stroke, sw=1, rx=6),
        ]
        shown = list(lines) or [""]
        pad = 12
        step = (inner_h - pad) / len(shown)
        for i, ln in enumerate(shown):
            yy = inner_y + pad + i * step + min(16, step * 0.28)
            bits.append(ml(cx + 18, yy, wrap(ln, chars, 2), size=14, fill=ink, weight=500))
        return bits

    gx = x + hw + 10
    return "".join(
        _col(x, "#fef2f2", "#ef4444", "#fecaca", bad_title, "#b91c1c", bad_lines, cross, "#7f1d1d")
        + _col(gx, "#f0fdf4", "#16a34a", "#bbf7d0", good_title, "#166534", good_lines, check, "#14532d")
    )


def bullets(x, y, items, *, color="#2563eb", max_w=40, h=None) -> str:
    parts = []
    shown = list(items) or [""]
    if h and h > 20:
        step = h / len(shown)
        yy = y + max(12, step * 0.35)
        for item in shown:
            lines = wrap(item, max_w, 2)
            parts.append(circle(x + 6, yy - 4, 4, fill=color))
            parts.append(ml(x + 16, yy - 8, lines, size=13, fill=INK, weight=500))
            yy += step
        return "".join(parts)
    yy = y + 12
    for item in shown:
        lines = wrap(item, max_w, 2)
        parts.append(circle(x + 6, yy - 4, 4, fill=color))
        parts.append(ml(x + 16, yy - 8, lines, size=13, fill=INK, weight=500))
        yy += 16 * len(lines) + 12
    return "".join(parts)


def do_dont(x, y, w, h, dos: list[str], donts: list[str]) -> str:
    dos, donts = dos[:4], donts[:3]
    chars = max(20, int((w - 28) / 7.8))
    n = max(1, len(dos) + len(donts))
    title_h = 22
    item_h = max(28, (h - title_h * 2) / n)
    parts = [t(x, y + 16, "Do", size=13, fill="#166534", weight=800)]
    yy = y + title_h + item_h * 0.45
    for d in dos:
        parts.append(check(x + 8, yy - 2, 7))
        parts.append(ml(x + 22, yy - 8, wrap(d, chars, 2), size=13, fill=INK))
        yy += item_h
    parts.append(t(x, yy - item_h * 0.35 + 4, "Don't", size=13, fill="#b91c1c", weight=800))
    yy += title_h * 0.7
    for d in donts:
        parts.append(cross(x + 8, yy - 2, 7))
        parts.append(ml(x + 22, yy - 8, wrap(d, chars, 2), size=13, fill="#7f1d1d"))
        yy += item_h
    return "".join(parts)


def cs_table(x, y, w, rows, h=None, third="AWS") -> str:
    return table(
        x, y, w, ["Concept", "C#", third], rows,
        header_fill="#f3e8ff", header_ink="#6d28d9", row_h=30, h=h,
    )


def footer3(x, y, w, h, left_title, left_body, dos, donts, cs_rows, third="AWS") -> str:
    cw = (w - 24) / 3
    left_x, mid_x, right_x = x, x + cw + 12, x + 2 * cw + 24
    body_y, body_h = y + 28, h - 40
    parts = [
        rect(left_x, y, cw, h, fill="#fff", stroke="#fda4af", sw=1.5, rx=10),
        t(left_x + 12, y + 20, left_title, size=13, fill="#9f1239", weight=800),
        left_body(left_x + 12, body_y, cw - 24, body_h) if callable(left_body) else ml(
            left_x + 12, body_y + 8, wrap(str(left_body), 36, 10), size=13, fill=INK
        ),
        rect(mid_x, y, cw, h, fill="#fff", stroke="#86efac", sw=1.5, rx=10),
        do_dont(mid_x + 12, y + 8, cw - 24, h - 16, dos, donts),
        rect(right_x, y, cw, h, fill="#fff", stroke="#c4b5fd", sw=1.5, rx=10),
        t(right_x + 12, y + 20, "Quick C# comparison", size=13, fill="#6d28d9", weight=800),
        cs_table(right_x + 12, body_y, cw - 24, cs_rows, h=body_h, third=third),
    ]
    return "".join(parts)


def gantt(x, y, w, h, jobs, sync_name, async_name, sync_s, async_s) -> str:
    parts = [
        t(x, y + 12, sync_name, size=11, fill=MUTED, weight=700),
        t(x, y + 88, async_name, size=11, fill=MUTED, weight=700),
    ]
    n = len(jobs)
    bw = (w - 8) / max(n, 1)
    for i, job in enumerate(jobs):
        bx = x + i * bw
        parts.append(rect(bx, y + 20, bw - 4, 22, fill="#86efac", stroke=None, rx=4))
        parts.append(rect(bx, y + 42, bw - 4, 14, fill="#cbd5e1", stroke=None, rx=3))
        parts.append(t(bx + 4, y + 36, job, size=10, fill="#166534", weight=700))
        parts.append(t(bx + 4, y + 53, "(waiting)", size=9, fill=MUTED, weight=500))
    parts.append(t(x + w - 2, y + 40, f"Total {sync_s}", size=12, fill=NAVY, weight=800, anchor="end"))
    for i, job in enumerate(jobs):
        parts.append(rect(x, y + 102 + i * 18, w * 0.48, 15, fill="#86efac", stroke=None, rx=4))
        parts.append(t(x + 6, y + 113 + i * 18, f"{job} (waiting)", size=10, fill="#166534", weight=700))
    parts.append(t(x + w - 2, y + 120, f"Total {async_s}", size=12, fill="#166534", weight=800, anchor="end"))
    for i, lab in enumerate(["0", "1", "2", "3"]):
        parts.append(t(x + i * (w / 3), y + h - 2, lab, size=10, fill=MUTED, weight=600))
    return "".join(parts)


def stack(x, y, w, h, layers) -> str:
    n = len(layers)
    rh = (h - 8 * (n - 1)) / n
    fills = ["#1e3a5f", "#2563eb", "#86efac", "#fde68a"]
    inks = ["#fff", "#fff", "#14532d", "#854d0e"]
    parts = []
    for i, (title, sub) in enumerate(layers):
        yy = y + i * (rh + 8)
        parts.append(rect(x, yy, w, rh, fill=fills[i % 4], stroke=None, rx=8))
        parts.append(t(x + w / 2, yy + rh * 0.42, title, size=13, fill=inks[i % 4], weight=800, anchor="middle"))
        parts.append(t(x + w / 2, yy + rh * 0.72, sub, size=10, fill=inks[i % 4], weight=500, anchor="middle"))
    return "".join(parts)


def levels(x, y, w, h, rows) -> str:
    n = len(rows)
    rh = (h - 6 * (n - 1)) / n
    parts = []
    for i, (lab, color, det) in enumerate(rows):
        yy = y + i * (rh + 6)
        parts.append(rect(x, yy, w * (1 - i * 0.04), rh, fill=color, stroke=None, rx=8))
        parts.append(t(x + 12, yy + rh * 0.42, lab, size=13, fill="#fff", weight=800))
        parts.append(t(x + 12, yy + rh * 0.76, det, size=10, fill="#f8fafc", weight=500))
    return "".join(parts)


def hub(x, y, w, h, center, sats) -> str:
    cx, cy, r = x + w / 2, y + h / 2, min(w, h) * 0.15
    parts = [
        circle(cx, cy, r + 6, fill="#ede9fe", stroke="#7c3aed", sw=2),
        t(cx, cy + 5, center, size=13, fill="#5b21b6", weight=800, anchor="middle"),
    ]
    pos = [(cx, y + 14), (x + w - 58, cy), (cx, y + h - 16), (x + 58, cy)]
    for (px, py), lab in zip(pos, sats[:4]):
        parts.append(arrow(cx, cy, px, py, "#7c3aed", dash=True))
        parts.append(rect(px - 48, py - 12, 96, 24, fill="#86efac", stroke=None, rx=8))
        parts.append(t(px, py + 5, lab, size=11, fill="#166534", weight=700, anchor="middle"))
    return "".join(parts)


def note(x, y, w, text, *, kind="warn") -> str:
    if kind == "ok":
        return rect(x, y, w, 22, fill="#dcfce7", stroke=None, rx=6) + t(x + 8, y + 16, text, size=11, fill="#166534", weight=700)
    if kind == "star":
        return rect(x, y, w, 22, fill="#fef9c3", stroke=None, rx=6) + t(x + 8, y + 16, "★  " + text, size=11, fill="#854d0e", weight=700)
    return rect(x, y, w, 22, fill="#fee2e2", stroke=None, rx=6) + t(x + 8, y + 16, text, size=11, fill="#b91c1c", weight=700)


def header(title: str, sub: str) -> str:
    return t(W / 2, 28, f"{title}  –  Visual Guide", size=24, fill=NAVY, weight=800, anchor="middle") + t(
        W / 2, 48, sub, size=12, fill=MUTED, weight=500, anchor="middle"
    )


def panel(slot, n, title, pill_text, body) -> str:
    x, y, w, h = slot
    ink, pf, pt = INKS[n - 1], PILLS[n - 1], PILL_TX[n - 1]
    ix, iy, iw, ih = inner(x, y, w, h)
    return card(x, y, w, h, n, title, ink) + pill(x + 12, y + 40, w - 24, pill_text, pf, pt) + body(ix, iy, iw, ih)


def svg(title: str, sub: str, parts: list[str]) -> str:
    defs = """
  <defs>
    <marker id="arrow" markerWidth="12" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M0,0 L12,5 L0,10 z" fill="#64748b"/>
    </marker>
  </defs>
"""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n'
        + defs
        + rect(0, 0, W, H, fill=PAGE, stroke=None, rx=0)
        + header(title, sub)
        + "".join(parts)
        + "\n</svg>\n"
    )


def slug(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (title or "").lower()).strip("-")
    return s[:48] or "topic"


def html_esc(s: str) -> str:
    return html_mod.escape(s)


def footer_left_code(lines_a, lines_b):
    """Two stacked code boxes for footer column 1."""
    def draw(x, y, w, h):
        hh = (h - 8) / 2
        return code_box(x, y, w, hh - 4, lines_a) + code_box(x, y + hh, w, hh - 4, lines_b)
    return draw


def write_posters(images_dir: Path, builders: list) -> dict[int, tuple[str, str, int]]:
    """builders: list of (sid, title, zero-arg svg fn). Overwrites slide-*.svg in images_dir."""
    images_dir.mkdir(parents=True, exist_ok=True)
    for old in images_dir.glob("slide-*.svg"):
        old.unlink()
    mapping: dict[int, tuple[str, str, int]] = {}
    for n, (_sid, title, fn) in enumerate(builders, 1):
        name = f"slide-{n:02d}-{slug(title)}.svg"
        (images_dir / name).write_text(fn(), encoding="utf-8")
        mapping[n] = (f"images/{name}", title, 1536)
    return mapping
