"""Build ClientInterview/SaranyaAnswers.html from SaranyaAnswers.md (print / Save as PDF)."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import markdown
from slide_code import highlight_csharp_line, vs_editor

HERE = Path(__file__).resolve().parent
MD_PATH = HERE / "SaranyaAnswers.md"
OUT_PATH = HERE / "SaranyaAnswers.html"

MERMAID_PLACEHOLDER = "@@MERMAID_{i}@@"
CODE_PLACEHOLDER = "@@CODE_{i}@@"

_SQL_KEYWORDS = {
    "add", "all", "alter", "and", "as", "asc", "begin", "between", "by", "case",
    "catch", "clustered", "commit", "create", "cross", "declare", "delete", "desc",
    "distinct", "drop", "else", "end", "except", "exec", "execute", "exists", "from",
    "full", "go", "group", "having", "if", "in", "index", "inner", "insert", "into",
    "is", "join", "left", "like", "merge", "nonclustered", "not", "null", "on", "or",
    "order", "outer", "over", "procedure", "raiserror", "return", "right", "rollback",
    "rowcount", "select", "set", "table", "then", "throw", "top", "tran", "transaction",
    "try", "union", "update", "values", "when", "where", "while", "with",
}

CSS = r"""
:root {
  --ink: #0f172a;
  --muted: #475569;
  --navy: #1e3a5f;
  --navy-2: #16324f;
  --line: #cbd5e1;
  --paper: #f8fafc;
  --say: #fff7ed;
  --say-edge: #c2410c;
}
* { box-sizing: border-box; }
html { font-size: 15px; scroll-padding-top: 64px; }
body {
  margin: 0;
  color: var(--ink);
  background: #e2e8f0;
  font-family: "Segoe UI", Calibri, system-ui, sans-serif;
  line-height: 1.45;
}
.toolbar {
  position: sticky; top: 0; z-index: 30;
  display: flex; gap: 10px; align-items: center; flex-wrap: wrap;
  background: var(--navy); color: #fff;
  padding: 10px 18px;
  font-size: 14px;
}
.toolbar b { margin-right: 8px; }
.toolbar button, .toolbar a {
  background: #fff; color: var(--navy); border: 0;
  padding: 6px 12px; border-radius: 6px;
  font-weight: 700; cursor: pointer; text-decoration: none;
  font-size: 13px;
}
.toolbar button:hover, .toolbar a:hover { background: #e0f2fe; }
.layout {
  display: grid;
  grid-template-columns: 252px minmax(0, 1fr);
  gap: 0;
  align-items: start;
  width: 100%;
}
.sidemenu {
  position: sticky;
  top: 52px;
  height: calc(100vh - 52px);
  overflow: auto;
  background: #0f2744;
  color: #e2e8f0;
  padding: 12px 0 28px;
  font-size: 12.5px;
  line-height: 1.35;
}
.sidemenu-title {
  font-weight: 700;
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #93c5fd;
  padding: 6px 14px 10px;
}
.sidemenu a {
  display: block;
  color: #cbd5e1;
  text-decoration: none;
  padding: 5px 14px 5px 14px;
  border-left: 3px solid transparent;
}
.sidemenu a:hover { background: #16324f; color: #fff; }
.sidemenu a.nav-sec {
  font-weight: 700;
  color: #fff;
  margin-top: 10px;
  padding-top: 8px;
  background: #16324f;
  font-size: 12px;
}
.sidemenu a.nav-q { padding-left: 18px; color: #cbd5e1; }
.sidemenu a.active {
  background: #1e40af;
  color: #fff;
  border-left-color: #fb923c;
}
.sheet {
  background: #fff;
  margin: 16px 16px 48px 12px;
  padding: 28px 36px 48px;
  box-shadow: 0 8px 30px rgba(15, 23, 42, 0.12);
  min-width: 0;
}
.toc { display: none; }
h2, h3 { scroll-margin-top: 64px; }
@media (max-width: 640px) {
  .layout { grid-template-columns: 1fr; }
  .sidemenu {
    position: relative;
    top: 0;
    height: auto;
    max-height: 36vh;
  }
}
h1 { font-size: 1.7rem; margin: 0 0 8px; color: var(--navy); }
h2 {
  font-size: 1.25rem;
  color: #fff;
  background: var(--navy);
  padding: 8px 12px;
  margin: 28px 0 14px;
  page-break-after: avoid;
  break-after: avoid;
}
h3 {
  font-size: 1.05rem;
  color: #16324f;
  border-left: 5px solid #c2410c;
  padding: 8px 12px;
  margin: 22px 0 0;
  background: #dbeafe;
  page-break-after: avoid;
  break-after: avoid;
}
h4 {
  font-size: 0.95rem;
  color: #1e40af;
  margin: 14px 0 6px;
  page-break-after: avoid;
}
p { margin: 8px 0; }
strong { color: #0f172a; }
a { color: #1d4ed8; }
hr { border: 0; border-top: 1px solid var(--line); margin: 22px 0; }
table {
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0 14px;
  font-size: 13.5px;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid var(--line);
  padding: 6px 8px;
  text-align: left;
  vertical-align: top;
}
th { background: #e2e8f0; color: var(--navy); }
tr:nth-child(even) td { background: var(--paper); }
table.vs-code tr:nth-child(even) td,
table.vs-code tr:nth-child(odd) td { background: #fff; }
blockquote {
  margin: 0 0 16px;
  padding: 12px 16px;
  background: var(--say);
  border-left: 5px solid var(--say-edge);
  color: #7c2d12;
  line-height: 1.6;
  page-break-inside: avoid;
}
h3 + blockquote { margin-top: 0; }
blockquote p { margin: 0 0 10px; }
blockquote p:last-child { margin-bottom: 0; }
pre, .mermaid, .vs-editor, .mc-row, .shot-wrap {
  page-break-inside: avoid;
  break-inside: avoid;
}
pre {
  background: #fff;
  color: #000;
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  overflow: auto;
  font-size: 12.5px;
  line-height: 1.4;
  font-family: Consolas, "Cascadia Mono", Menlo, monospace;
}
code {
  font-family: Consolas, "Cascadia Mono", Menlo, monospace;
  font-size: 0.92em;
  background: #e2e8f0;
  padding: 1px 5px;
  border-radius: 4px;
}
pre code { background: none; color: inherit; padding: 0; font-size: inherit; }
.vs-editor {
  background: #fff;
  overflow: auto;
  max-height: none;
  border: 1px solid #c9a227;
  border-radius: 4px;
  margin: 10px 0 14px;
}
table.vs-code {
  width: 100%;
  border-collapse: collapse;
  font-family: Consolas, "Cascadia Mono", "Courier New", monospace;
  font-size: 13px;
  line-height: 1.55;
  margin: 0;
}
table.vs-code td { border: 0; padding: 0; background: #fff; }
table.vs-code td.gutter {
  width: 44px; min-width: 44px; padding: 0 10px 0 6px;
  text-align: right; color: #2b91af; user-select: none;
  vertical-align: top; border-right: 2px solid #c9a227; background: #fff;
}
table.vs-code td.src {
  padding: 0 0 0 14px; white-space: pre; vertical-align: top; color: #000;
}
.t-kw, .t-bi { color: #0000ff; }
.t-type { color: #2b91af; }
.t-fn  { color: #74531f; }
.t-cm  { color: #008000; }
.t-str { color: #a31515; }
.t-num { color: #098658; }
.t-op, .t-id { color: #000000; }
.mc-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin: 12px 0 16px;
  align-items: stretch;
}
.mc-col {
  border-radius: 6px;
  overflow: hidden;
  min-width: 0;
  background: #fff;
}
.mc-bad  { border: 1.5px solid #e53e3e; }
.mc-good { border: 1.5px solid #28a745; }
.mc-alt  { border: 1.5px solid #2563eb; }
.mc-lbl  { display: block; padding: 6px 10px; font-size: 12px; font-weight: 700; }
.mc-col p { margin: 8px 10px; }
.mc-col p:has(.mc-lbl), .mc-col > p:first-child { margin: 0; }
.mc-bad  .mc-lbl { background: #fff5f5; color: #c53030; }
.mc-good .mc-lbl { background: #f0fff4; color: #276749; }
.mc-alt  .mc-lbl { background: #eff6ff; color: #1e40af; }
.mc-col .vs-editor { margin: 0; border: none; border-top: 1px solid #e2e8f0; border-radius: 0; }
.mc-col .mermaid { margin: 0; border: none; border-radius: 0; border-top: 1px solid #e2e8f0; }
.mc-col .shot-wrap { margin: 0; }
.mc-col img.shot { border: none; border-radius: 0; }
.mermaid {
  background: #f8fafc;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px 8px;
  margin: 12px 0 16px;
  text-align: center;
}
img.shot {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
  max-height: 420px;
  object-fit: contain;
  object-position: top;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
}
.mc-col img.shot { max-height: 260px; border: none; border-radius: 0; }
.shot-wrap { margin: 12px 0 8px; }
.shot-cap {
  font-size: 12px;
  color: var(--muted);
  margin: 0 0 14px;
}
.how-call {
  font-size: 13px;
  color: #1e3a5f;
  font-weight: 700;
  margin: 12px 0 4px;
}
ul, ol { margin: 6px 0 12px; padding-left: 22px; }
li { margin: 3px 0; }
.toc ul { list-style: none; padding-left: 0; }
.toc li { margin: 4px 0; }
.toc a { text-decoration: none; }
.cover-note {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 18px;
}
@media print {
  body { background: #fff; }
  .toolbar, .sidemenu { display: none !important; }
  .layout { display: block; max-width: none; }
  .sheet {
    max-width: none;
    margin: 0;
    padding: 0;
    box-shadow: none;
  }
  a { color: inherit; text-decoration: none; }
  h2, h3, h4, table, blockquote, pre, .mermaid, .mc-row, .vs-editor { page-break-inside: avoid; }
  h2 { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  h3, th, blockquote, .mermaid, .mc-lbl, .mc-bad, .mc-good,
  .t-kw, .t-type, .t-fn, .t-cm, .t-str, .t-num, .vs-editor, img.shot {
    -webkit-print-color-adjust: exact; print-color-adjust: exact;
  }
  .vs-editor { max-height: none; overflow: visible; }
  .mc-row { grid-template-columns: 1fr 1fr; }
  @page { size: A4; margin: 14mm 12mm 16mm; }
}
@media (max-width: 900px) {
  .mc-row { grid-template-columns: 1fr; }
}
"""

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Saranya — questions and answers</title>
<style>__CSS__</style>
</head>
<body>
<div class="toolbar">
  <b>Saranya answers</b>
  <button type="button" id="btnPrint">Print / Save PDF</button>
  <a href="Saranya.md">Questions list</a>
  <a href="Client1.html">Client1 deck</a>
  <span style="opacity:.85">Wait for diagrams, then print. Enable Background graphics.</span>
</div>
<div class="layout">
<nav class="sidemenu" id="sidemenu">__SIDEMENU__</nav>
<article class="sheet">
__BODY__
</article>
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({
  startOnLoad: true,
  theme: "neutral",
  securityLevel: "loose",
  flowchart: { useMaxWidth: true, htmlLabels: true },
  er: { useMaxWidth: true }
});
const btn = document.getElementById("btnPrint");
btn.addEventListener("click", async () => {
  btn.textContent = "Drawing…";
  try {
    if (window.mermaid && mermaid.run) await mermaid.run();
  } catch (e) {}
  btn.textContent = "Print / Save PDF";
  window.print();
});
const menuLinks = [...document.querySelectorAll(".sidemenu a")];
const byId = new Map(menuLinks.map(a => [a.getAttribute("href").slice(1), a]));
function setActive(id) {
  menuLinks.forEach(a => a.classList.remove("active"));
  const a = byId.get(id);
  if (a) {
    a.classList.add("active");
    a.scrollIntoView({ block: "nearest" });
  }
}
menuLinks.forEach(a => a.addEventListener("click", () => setActive(a.getAttribute("href").slice(1))));
const heads = [...document.querySelectorAll(".sheet h2[id], .sheet h3[id]")];
const io = new IntersectionObserver((entries) => {
  const hit = entries.filter(e => e.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
  if (hit) setActive(hit.target.id);
}, { rootMargin: "-70px 0px -60% 0px", threshold: [0.1, 0.4] });
heads.forEach(h => io.observe(h));
</script>
</body>
</html>
"""


def extract_mermaid(md: str) -> tuple[str, list[str]]:
    blocks: list[str] = []

    def repl(m: re.Match[str]) -> str:
        blocks.append(m.group(1).strip())
        return f"\n\n{MERMAID_PLACEHOLDER.format(i=len(blocks) - 1)}\n\n"

    md = re.sub(
        r"```mermaid\s*\n(.*?)```",
        repl,
        md,
        flags=re.DOTALL,
    )
    return md, blocks


def restore_mermaid(html_body: str, blocks: list[str]) -> str:
    for i, src in enumerate(blocks):
        div = f'<div class="mermaid">\n{src}\n</div>'
        html_body = html_body.replace(f"<p>{MERMAID_PLACEHOLDER.format(i=i)}</p>", div)
        html_body = html_body.replace(MERMAID_PLACEHOLDER.format(i=i), div)
    return html_body


def _span(cls: str, text: str) -> str:
    return f'<span class="{cls}">{html.escape(text)}</span>'


def highlight_sql_line(line: str) -> str:
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i:i + 2] == "--":
            out.append(_span("t-cm", line[i:]))
            break
        if line[i:i + 2] == "/*":
            end = line.find("*/", i + 2)
            if end < 0:
                out.append(_span("t-cm", line[i:]))
                break
            out.append(_span("t-cm", line[i : end + 2]))
            i = end + 2
            continue
        ch = line[i]
        if ch in "\"'":
            q = ch
            j = i + 1
            while j < n:
                if line[j] == q:
                    j += 1
                    break
                j += 1
            out.append(_span("t-str", line[i:j]))
            i = j
            continue
        if ch.isdigit() and (i == 0 or not (line[i - 1].isalnum() or line[i - 1] == "_")):
            j = i
            while j < n and (line[j].isdigit() or line[j] in "._"):
                j += 1
            out.append(_span("t-num", line[i:j]))
            i = j
            continue
        if ch.isalpha() or ch == "_" or ch == "@" or ch == "#":
            j = i + 1
            while j < n and (line[j].isalnum() or line[j] in "_@#"):
                j += 1
            word = line[i:j]
            if word.lstrip("@#").lower() in _SQL_KEYWORDS:
                out.append(_span("t-kw", word))
            elif word[:1] in "@#":
                out.append(_span("t-type", word))
            else:
                out.append(_span("t-id", word))
            i = j
            continue
        out.append(_span("t-op", ch))
        i += 1
    return "".join(out) if out else "&#160;"


def highlight_plain_line(line: str) -> str:
    return html.escape(line) if line else "&#160;"


def _vs_from_lines(text: str, highlight) -> str:
    rows = []
    lines = text.splitlines() or [""]
    for num, line in enumerate(lines, 1):
        rows.append(f'<tr><td class="gutter">{num}</td><td class="src">{highlight(line)}</td></tr>')
    body = "\n".join(rows)
    return f'<div class="vs-editor vs-editor-compact"><table class="vs-code"><tbody>\n{body}\n</tbody></table></div>'


def render_code_block(lang: str, src: str) -> str:
    text = src.rstrip("\n") + "\n"
    key = (lang or "").lower().strip()
    if key in ("csharp", "cs"):
        return vs_editor(text, lang="csharp", compact=True)
    if key in ("typescript", "ts", "javascript", "js"):
        return vs_editor(text, lang="csharp", compact=True)
    if key == "sql":
        return _vs_from_lines(text, highlight_sql_line)
    if key in ("html", "xml"):
        return _vs_from_lines(text, highlight_plain_line)
    if key in ("python", "py"):
        return vs_editor(text, lang="python", compact=True)
    return _vs_from_lines(text, highlight_csharp_line)


def extract_code(md: str) -> tuple[str, list[tuple[str, str]]]:
    blocks: list[tuple[str, str]] = []

    def repl(m: re.Match[str]) -> str:
        lang = (m.group(1) or "").strip()
        src = m.group(2)
        blocks.append((lang, src))
        return f"\n\n{CODE_PLACEHOLDER.format(i=len(blocks) - 1)}\n\n"

    md = re.sub(r"```(\w*)\s*\n(.*?)```", repl, md, flags=re.DOTALL)
    return md, blocks


def restore_code(html_body: str, blocks: list[tuple[str, str]]) -> str:
    for i, (lang, src) in enumerate(blocks):
        editor = render_code_block(lang, src)
        html_body = html_body.replace(f"<p>{CODE_PLACEHOLDER.format(i=i)}</p>", editor)
        html_body = html_body.replace(CODE_PLACEHOLDER.format(i=i), editor)
    return html_body


def _plain(inner: str) -> str:
    text = re.sub(r"<[^>]+>", "", inner)
    return html.unescape(text).strip()


def build_sidemenu(body: str) -> str:
    parts = ['<div class="sidemenu-title">Questions</div>']
    for m in re.finditer(r'<h([23]) id="([^"]+)">(.*?)</h\1>', body, flags=re.DOTALL):
        level, hid, inner = m.group(1), m.group(2), m.group(3)
        label = _plain(inner)
        if level == "2":
            cls = "nav-sec"
        else:
            cls = "nav-q"
            if label.startswith("Q. "):
                label = label[3:]
        parts.append(f'<a class="{cls}" href="#{hid}">{html.escape(label)}</a>')
    return "\n".join(parts)


def main() -> None:
    raw = MD_PATH.read_text(encoding="utf-8")
    md, mermaid_blocks = extract_mermaid(raw)
    md, code_blocks = extract_code(md)
    body = markdown.markdown(
        md,
        extensions=["extra", "sane_lists", "toc", "nl2br", "tables", "md_in_html"],
        extension_configs={"toc": {"permalink": False, "toc_depth": 3}},
    )
    body = restore_mermaid(body, mermaid_blocks)
    body = restore_code(body, code_blocks)
    body = re.sub(
        r"<p>\s*(<span class=\"mc-lbl\">.*?</span>)\s*</p>",
        r"\1",
        body,
    )
    # Markdown > quotes already wrap Say. Do not nest a second blockquote.
    sidemenu = build_sidemenu(body)
    page = (
        HTML.replace("__CSS__", CSS)
        .replace("__SIDEMENU__", sidemenu)
        .replace("__BODY__", body)
    )
    OUT_PATH.write_text(page, encoding="utf-8")
    n_q = sidemenu.count('class="nav-q"')
    print(
        f"Generated {OUT_PATH} ({OUT_PATH.stat().st_size:,} bytes, "
        f"{len(mermaid_blocks)} diagrams, {len(code_blocks)} code editors, {n_q} questions in side menu)"
    )
    print("Preview: open the HTML in a browser. Print / Save PDF after diagrams draw.")


if __name__ == "__main__":
    main()
