"""Side-by-side INPUT | OUTPUT blocks with line-aligned print results."""

from __future__ import annotations

import re

_STEP_PRE_RE = re.compile(r'<div class="step-pre">(.*?)</div>', re.DOTALL)
_IO_SPLIT_RE = re.compile(
    r"(?:#\s*INPUT[^\n]*\n)"
    r"(?P<code>.*?)"
    r"(?:\n#\s*OUTPUT[^\n]*\n)"
    r"(?P<out>.*)",
    re.DOTALL | re.IGNORECASE,
)
_PRINT_RE = re.compile(r"\b(?:print|announce)\s*\(")


def io_split(
    code: str,
    out_map: dict[int, str] | None = None,
    *,
    line_outputs: list[str] | None = None,
    out_label: str = "# OUTPUT (same line as each print)",
) -> str:
    """Render code left / outputs right, aligned by line number (1-based in out_map)."""
    code = code.replace("\r\n", "\n").rstrip("\n")
    lines = code.split("\n")
    n = len(lines)

    if line_outputs is None:
        aligned = [""] * n
        for i, text in (out_map or {}).items():
            if 1 <= i <= n:
                aligned[i - 1] = text
    else:
        aligned = list(line_outputs)
        if len(aligned) < n:
            aligned.extend([""] * (n - len(aligned)))
        elif len(aligned) > n:
            aligned = aligned[:n]

    return (
        '<div class="io-split">'
        '<div class="io-in">'
        '<span class="io-lbl"># INPUT</span>'
        f'<div class="step-pre">{code}</div>'
        "</div>"
        '<div class="io-split-divider" role="separator" aria-orientation="vertical" '
        'title="Drag to resize INPUT / OUTPUT"></div>'
        '<div class="io-out">'
        f'<span class="io-lbl">{out_label}</span>'
        f'<div class="step-pre">{"\n".join(aligned)}</div>'
        "</div>"
        "</div>"
    )


def _align_outputs(code: str, out_body: str) -> tuple[list[str], str]:
    """Map OUTPUT lines onto code lines; return (aligned, leftover takeaway HTML)."""
    code_lines = code.replace("\r\n", "\n").rstrip("\n").split("\n")
    n = len(code_lines)
    aligned = [""] * n

    data: list[str] = []
    takeaways: list[str] = []
    for line in out_body.replace("\r\n", "\n").rstrip("\n").split("\n"):
        stripped = line.strip()
        if stripped.startswith("#"):
            takeaways.append(line)
        elif stripped:
            data.append(line)
        # blank OUTPUT lines ignored for alignment

    print_idxs = [i for i, line in enumerate(code_lines) if _PRINT_RE.search(line)]

    if print_idxs and data:
        if len(data) <= len(print_idxs):
            for idx, text in zip(print_idxs, data):
                aligned[idx] = text
        else:
            # More output lines than prints (e.g. loop) — stack extras on last print
            for idx, text in zip(print_idxs, data):
                aligned[idx] = text
            extra = data[len(print_idxs) :]
            aligned[print_idxs[-1]] = "\n".join(
                [aligned[print_idxs[-1]], *extra] if aligned[print_idxs[-1]] else extra
            )
    elif data:
        # No print — attach results to last real code line
        last = 0
        for i, line in enumerate(code_lines):
            s = line.strip()
            if s and not s.startswith("#"):
                last = i
        aligned[last] = "\n".join(data)

    leftover = ""
    if takeaways:
        leftover = (
            '<p class="step-result" style="margin-top:6px">'
            + "<br>".join(t.lstrip("# ").strip() for t in takeaways)
            + "</p>"
        )
    return aligned, leftover


def convert_step_pre_inner(inner: str) -> str | None:
    """If inner is # INPUT ... # OUTPUT ..., return io-split HTML; else None."""
    text = inner.strip("\n")
    m = _IO_SPLIT_RE.search(text.lstrip())
    if not m:
        return None
    code = m.group("code").strip("\n")
    out_body = m.group("out")
    aligned, leftover = _align_outputs(code, out_body)
    return io_split(code, line_outputs=aligned) + leftover


def convert_input_output_pres(html: str) -> str:
    """Convert every .step-pre that has # INPUT / # OUTPUT into side-by-side io-split."""

    def _repl(match: re.Match[str]) -> str:
        # Skip step-pre already inside an io-split pane (no # INPUT header in body)
        inner = match.group(1)
        converted = convert_step_pre_inner(inner)
        if converted is None:
            return match.group(0)
        return converted

    return _STEP_PRE_RE.sub(_repl, html)
