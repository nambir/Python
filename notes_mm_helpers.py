"""Shared HTML builders for MindMap datatype slides."""

from __future__ import annotations


def sec(title: str, inner: str) -> str:
    return f'<div class="mm-sec"><h3>{title}</h3>{inner}</div>'


def p(text: str) -> str:
    return f"<p>{text}</p>"


def grid(*cards: str) -> str:
    return '<div class="mm-grid">' + "".join(cards) + "</div>"


def card(title: str, body: str) -> str:
    return f'<div class="mm-card"><b>{title}</b>{body}</div>'


def memory(basic: str, interview: str) -> str:
    return sec(
        "Memory &amp; size",
        grid(
            card("Basic (kid view)", basic),
            card("Interview point", interview),
        ),
    )


def what_two(viz_html: str, remember_html: str, tag: str = "") -> str:
    tag_html = f'<span class="dict-tag">{tag}</span>' if tag else ""
    return f"""
<div class="dict-what">
  <div class="dict-panel"><div class="dict-viz">{viz_html}</div></div>
  <div class="dict-panel dict-remember">{remember_html}{tag_html}</div>
</div>
"""


def ops(items: list[tuple[str, str, str, str]]) -> str:
    """items: (ico_class, ico_text, name, code)"""
    parts = []
    for ico_cls, ico_txt, name, code in items:
        parts.append(
            f'<div class="op-card">'
            f'<div class="op-ico {ico_cls}">{ico_txt}</div>'
            f'<div class="op-name">{name}</div>'
            f'<span class="op-code">{code}</span></div>'
        )
    return f'<div class="ops-row ops-row-{len(items)}">' + "".join(parts) + "</div>"


def trap(text: str) -> str:
    return f'<div class="dt-trap">{text}</div>'


def cheat(rows: list[tuple[str, str, str]]) -> str:
    """Two columns: Thing + meaning together, then Code / tip."""
    body = "".join(
        f'<tr><td><b>{a}</b><br><span class="cheat-mean">{b}</span></td>'
        f"<td>{c}</td></tr>"
        for a, b, c in rows
    )
    return (
        '<table class="data-tbl cheat-tbl">'
        "<tr><th>Thing</th><th>Code / tip</th></tr>"
        f"{body}</table>"
    )
