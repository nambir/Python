"""Generate PythonReview.html — same look & layout as PythonTraining.html."""

from __future__ import annotations

import html
from collections import defaultdict
from pathlib import Path

from python_review_content import DOCX_LEVEL, DOCX_NAME, DOCX_TITLE, QUESTIONS
from slide_code import vs_editor

OUTPUT = Path(__file__).parent / "PythonReview.html"
CODE_DIR = Path(__file__).parent / "PythonReview"
TOTAL = len(QUESTIONS)

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { height: 100%; overflow: hidden; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #fff; color: #1a1a2e; }

.slide { display: none; width: 100%; height: 100vh; padding: 24px 48px 56px; overflow-y: auto; background: #fff; }
.slide.active { display: block; }

.slide-hdr { margin-bottom: 14px; flex-shrink: 0; }
.slide-meta { font-size: 10px; color: #999; letter-spacing: 1.5px; text-transform: uppercase; }
.slide-title { font-size: 26px; font-weight: 700; color: #1a1a2e; border-bottom: 3px solid #0066cc; padding-bottom: 4px; display: inline-block; }
.slide-sub { font-size: 13px; color: #555; margin-top: 4px; }

h3 { font-size: 15px; color: #0066cc; margin: 10px 0 6px; }
p { font-size: 13px; line-height: 1.5; margin-bottom: 6px; }
ul { margin: 0 0 8px 18px; }
li { font-size: 12px; line-height: 1.45; margin-bottom: 2px; }
code { font-family: Consolas, monospace; font-size: 12px; color: #0000ff; background: #f0f7ff; padding: 1px 4px; border-radius: 3px; }

.slide-body { display: flex; flex-direction: column; gap: 0; }
.main-split {
  display: grid;
  grid-template-columns: minmax(180px, var(--split-left, 48%)) 12px minmax(240px, 1fr);
  gap: 0;
  align-items: start;
}
.main-split.no-code { grid-template-columns: 1fr; max-width: 960px; }
.panel-left { min-width: 0; padding-right: 8px; }
.panel-code { min-width: 0; position: sticky; top: 12px; padding-left: 8px; }
.panel-code .vs-editor + .vs-editor { margin-top: 12px; }
.split-divider {
  width: 12px; cursor: col-resize; align-self: stretch; min-height: 240px;
  position: relative; touch-action: none; user-select: none;
  background: transparent; z-index: 5;
}
.split-divider::before {
  content: ""; position: absolute; left: 5px; top: 0; bottom: 0; width: 2px;
  background: #c5d8ef; border-radius: 1px; transition: background .15s, width .15s, left .15s;
}
.split-divider::after {
  content: "⋮"; position: absolute; left: 50%; top: 48px; transform: translateX(-50%);
  font-size: 14px; line-height: 1; color: #6b8fb8; background: #fff;
  padding: 4px 0; pointer-events: none;
}
.split-divider:hover::before,
.split-divider.dragging::before {
  background: #0066cc; width: 3px; left: 4.5px;
}
.split-divider:hover::after,
.split-divider.dragging::after { color: #0066cc; }
body.split-dragging { cursor: col-resize; user-select: none; }
body.split-dragging iframe, body.split-dragging .vs-editor { pointer-events: none; }
.main-split.no-code .split-divider { display: none; }
.code-toolbar { display: flex; justify-content: flex-end; gap: 8px; margin-bottom: 6px; }
.btn-code-expand {
  padding: 4px 12px; font-size: 11px; font-weight: 600; border: 1px solid #0066cc;
  border-radius: 4px; background: #f0f7ff; color: #0066cc; cursor: pointer;
}
.btn-code-expand:hover { background: #0066cc; color: #fff; }
.code-backdrop {
  display: none; position: fixed; inset: 0; background: rgba(15, 23, 42, 0.4);
  z-index: 1090;
}
.code-backdrop.active { display: block; }
.panel-code.expanded {
  position: fixed; top: 16px; left: 24px; right: 24px; bottom: 56px;
  z-index: 1100; background: #fff; padding: 12px 14px;
  border: 1px solid #cfe0f5; border-radius: 8px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.22);
  overflow: auto;
}
.panel-code.expanded .vs-editor {
  max-height: calc(100vh - 130px); overflow: auto;
}
.panel-code.expanded table.vs-code td.src {
  white-space: pre-wrap; word-break: break-word; overflow-wrap: anywhere;
}

.badge {
  display: inline-block; font-size: 10px; font-weight: 700; letter-spacing: .4px;
  padding: 2px 8px; border-radius: 4px; margin-right: 8px; text-transform: uppercase;
  vertical-align: middle;
}
.badge-coding { background: #e8f0fe; color: #0066cc; border: 1px solid #b3d1ff; }
.badge-reasoning { background: #fff8e6; color: #b45309; border: 1px solid #f5d78e; }
.badge-integration { background: #f3e8ff; color: #7e22ce; border: 1px solid #e9d5ff; }

.interview-box { background: #e8f5e9; border-left: 3px solid #28a745; padding: 10px 12px; border-radius: 4px; margin-top: 8px; font-size: 12px; }
.interview-box p { margin: 6px 0 0; color: #1b5e20; line-height: 1.5; }
.interview-box .qa-q { margin-top: 10px; color: #1b5e20; font-style: normal; }
.interview-box .qa-a { margin-top: 4px; margin-left: 8px; color: #2e7d32; font-style: normal; }

.callout { background: #f0f7ff; border-left: 3px solid #0066cc; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.tip { background: #fff8e6; border-left: 3px solid #f39c12; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.challenge { background: #e8f5e9; border-left: 3px solid #28a745; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.keyword-box { background: #f8fafc; border-left: 3px solid #0066cc; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; line-height: 1.5; color: #1a1a2e; }

.data-tbl { width: 100%; border-collapse: collapse; margin: 6px 0 10px; font-size: 12px; }
.data-tbl th { background: #0066cc; color: #fff; text-align: left; padding: 6px 8px; font-weight: 600; }
.data-tbl td { border: 1px solid #e2e8f0; padding: 6px 8px; vertical-align: top; color: #1a1a2e; }
.data-tbl tr:nth-child(even) td { background: #f8fafc; }

.vs-editor { background: #fff; overflow: auto; max-height: calc(100vh - 140px); border: 1px solid #e2e8f0; border-radius: 4px; }
table.vs-code { width: 100%; border-collapse: collapse; font-family: Consolas, 'Cascadia Mono', 'Courier New', monospace; font-size: 13px; line-height: 1.55; }
table.vs-code td.gutter { width: 44px; min-width: 44px; padding: 0 10px 0 6px; text-align: right; color: #2b91af; user-select: none; vertical-align: top; border-right: 2px solid #c9a227; background: #fff; }
table.vs-code td.src { padding: 0 0 0 14px; white-space: pre; vertical-align: top; color: #000; }
.t-kw  { color: #0000ff; }
.t-bi  { color: #0000ff; }
.t-cm  { color: #008000; }
.t-str { color: #a31515; }
.t-num { color: #098658; }
.t-op  { color: #000000; }
.t-id  { color: #000000; }

.file-link {
  display: inline-block; margin: 4px 8px 4px 0; padding: 5px 10px; background: #0066cc; color: #fff;
  text-decoration: none; border-radius: 4px; font-size: 12px; font-weight: 600;
}
.file-link:hover { background: #0052a3; }
.run-cmd { display: inline-block; font-family: Consolas, monospace; font-size: 11px; color: #555; background: #f0f7ff; padding: 4px 8px; border-radius: 3px; }

.q-doc { margin-bottom: 12px; }
.q-doc .q-sub { font-size: 14px; font-weight: 700; color: #1a1a2e; margin: 0 0 8px; }
.q-doc .q-prompt { font-size: 13px; line-height: 1.5; margin-bottom: 8px; color: #1a1a2e; }
.q-doc .q-prompt b { color: #1a1a2e; }
.q-doc .vs-editor { max-height: none; margin: 6px 0 10px; }
.q-doc .expected { background: #fff8e6; border-left: 3px solid #f39c12; padding: 8px 12px; border-radius: 4px; margin: 8px 0 12px; font-size: 12px; }
.solution-label { font-size: 15px; color: #0066cc; margin: 4px 0 6px; font-weight: 700; }
.panel-code.expanded .q-doc .vs-editor,
.panel-code.expanded .vs-editor { max-height: none; }
.panel-code.expanded .q-doc table.vs-code td.src,
.panel-code.expanded table.vs-code td.src {
  white-space: pre-wrap; word-break: break-word; overflow-wrap: anywhere;
}

.panel-practice { margin-top: 10px; }
.checklist { margin: 0 0 8px 18px; }
.checklist li { font-size: 12px; margin-bottom: 3px; }

.nav-bar {
  position: fixed; bottom: 0; left: 0; right: 0; height: 44px; background: #f0f0f0;
  border-top: 1px solid #ccc; display: flex; align-items: center; justify-content: space-between;
  padding: 0 48px; z-index: 999;
}
.nav-bar button { padding: 6px 20px; font-size: 13px; font-weight: 600; border: none; border-radius: 4px; cursor: pointer; }
.nav-bar .btn-prev { background: #666; color: #fff; }
.nav-bar .btn-next { background: #0066cc; color: #fff; }
.nav-bar .btn-nav { background: #28a745; color: #fff; }
.nav-bar .slide-info { font-size: 12px; color: #555; }

.nav-content { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: calc(100vh - 44px); padding: 12px 16px; }
.nav-content h1 { font-size: 34px; margin-bottom: 4px; }
.nav-content .sub { font-size: 16px; color: #0066cc; }
.nav-content .org { font-size: 13px; color: #666; margin: 6px 0 14px; text-align: center; max-width: 800px; }
.nav-grid {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;
  max-width: 1400px; width: calc(100vw - 48px);
}
.nav-section { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; overflow: visible; }
.nav-section h3 { font-size: 14px; margin-bottom: 6px; border-bottom: 2px solid #0066cc; padding-bottom: 4px; color: #0066cc; }
.nav-section a { display: block; padding: 2px 0; color: #0066cc; font-size: 12px; cursor: pointer; text-decoration: none; font-weight: 600; }
.nav-section a:hover { text-decoration: underline; }
.nav-topic { margin: 0 0 6px; }
.nav-subs { margin: 2px 0 0 12px; padding: 0; list-style: none; }
.nav-subs li { font-size: 11px; color: #555; padding: 1px 0; font-weight: 400; }
.nav-subs li::before { content: "- "; color: #64748b; }

.intro-card {
  max-width: 900px; width: 100%; background: #f0f7ff; border-left: 3px solid #0066cc;
  border-radius: 4px; padding: 12px 14px; margin-bottom: 16px; text-align: left; font-size: 13px;
}
.intro-card h3 { margin-top: 0; color: #0066cc; }
.intro-card li { font-size: 12px; }

@media (max-width: 900px) {
  .slide { padding: 16px 16px 56px; }
  .main-split, .nav-grid { grid-template-columns: 1fr; }
  .main-split { grid-template-columns: 1fr !important; }
  .split-divider { display: none; }
  .panel-left, .panel-code { padding: 0; }
  .panel-code { position: static; }
  .vs-editor { max-height: 50vh; }
  .nav-bar { padding: 0 16px; }
}
"""

JS = f"""
let current = 0;
const total = {TOTAL};
const SPLIT_KEY = 'pythonReviewSplitLeft';
let splitDragging = null;

function getSavedSplit() {{
  const v = parseFloat(localStorage.getItem(SPLIT_KEY) || '');
  return (Number.isFinite(v) && v >= 20 && v <= 75) ? v : 48;
}}
function applySplitTo(split, pct) {{
  if (!split || split.classList.contains('no-code')) return;
  split.style.setProperty('--split-left', pct + '%');
}}
function applySavedSplit(root) {{
  const pct = getSavedSplit();
  (root || document).querySelectorAll('.main-split:not(.no-code)').forEach(s => applySplitTo(s, pct));
}}
function initSplitDividers() {{
  document.querySelectorAll('.split-divider').forEach(div => {{
    if (div.dataset.splitReady) return;
    div.dataset.splitReady = '1';
    div.title = 'Drag to resize panels';
    div.addEventListener('pointerdown', e => {{
      if (e.button !== 0) return;
      const split = div.closest('.main-split');
      if (!split || split.classList.contains('no-code')) return;
      const rect = split.getBoundingClientRect();
      splitDragging = {{ split, div, left: rect.left, width: rect.width }};
      div.classList.add('dragging');
      document.body.classList.add('split-dragging');
      try {{ div.setPointerCapture(e.pointerId); }} catch (_) {{}}
      e.preventDefault();
    }});
  }});
}}
document.addEventListener('pointermove', e => {{
  if (!splitDragging) return;
  const {{ split, left, width }} = splitDragging;
  if (width < 80) return;
  let pct = ((e.clientX - left) / width) * 100;
  pct = Math.max(20, Math.min(75, pct));
  applySplitTo(split, pct);
  localStorage.setItem(SPLIT_KEY, String(Math.round(pct * 10) / 10));
}});
function endSplitDrag() {{
  if (!splitDragging) return;
  splitDragging.div.classList.remove('dragging');
  document.body.classList.remove('split-dragging');
  splitDragging = null;
}}
document.addEventListener('pointerup', endSplitDrag);
document.addEventListener('pointercancel', endSplitDrag);

function collapseCodePanels() {{
  document.querySelectorAll('.panel-code.expanded').forEach(panel => {{
    panel.classList.remove('expanded');
    const btn = panel.querySelector('.btn-code-expand');
    if (btn) btn.textContent = 'Expand';
  }});
  const bd = document.getElementById('codeBackdrop');
  if (bd) bd.classList.remove('active');
}}
function toggleCodeExpand(btn) {{
  const panel = btn.closest('.panel-code');
  if (!panel) return;
  const willExpand = !panel.classList.contains('expanded');
  collapseCodePanels();
  if (willExpand) {{
    panel.classList.add('expanded');
    btn.textContent = 'Collapse';
    const bd = document.getElementById('codeBackdrop');
    if (bd) bd.classList.add('active');
  }}
}}
function show(n) {{
  collapseCodePanels();
  endSplitDrag();
  document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
  const el = document.getElementById('slide-' + n);
  if (!el) return;
  el.classList.add('active');
  current = n;
  const info = document.getElementById('slideInfo');
  if (info) {{
    info.textContent = n === 0 ? 'Navigation' : ('Slide ' + n + ' of ' + total);
  }}
  location.hash = n === 0 ? 'nav' : String(n);
  applySavedSplit(el);
}}
function nextSlide() {{ show(Math.min(current + 1, total)); }}
function prevSlide() {{ show(Math.max(current - 1, 0)); }}
function goSlide(n) {{ show(n); }}
document.addEventListener('keydown', e => {{
  if (e.key === 'Escape') {{ collapseCodePanels(); return; }}
  if (e.key === 'ArrowRight') nextSlide();
  if (e.key === 'ArrowLeft') prevSlide();
  if (e.key === 'Home') show(0);
}});
window.addEventListener('DOMContentLoaded', () => {{
  initSplitDividers();
  applySavedSplit(document);
  const h = location.hash.replace('#','');
  if (h === 'nav' || h === '') show(0);
  else show(parseInt(h, 10) || 0);
}});
"""

NAV_BAR = """
<div id="codeBackdrop" class="code-backdrop" onclick="collapseCodePanels()"></div>
<div class="nav-bar">
  <button class="btn-prev" onclick="prevSlide()">&larr; Prev</button>
  <button class="btn-nav" onclick="goSlide(0)">&#9776; Navigation</button>
  <span class="slide-info" id="slideInfo">Navigation</span>
  <button class="btn-next" onclick="nextSlide()">Next &rarr;</button>
</div>
"""


def esc(text: str) -> str:
    return html.escape(text or "", quote=False)


def kind_badge(kind: str) -> str:
    return f'<span class="badge badge-{esc(kind)}">{esc(kind.title())}</span>'


def load_code(code_file: str | None) -> str:
    if not code_file:
        return ""
    path = CODE_DIR / code_file
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def concepts_list(concepts: list[str]) -> str:
    if not concepts:
        return ""
    items = "".join(f"<li>{esc(c)}</li>" for c in concepts)
    return f"<h3>Base concepts you need</h3><ul>{items}</ul>"


def review_vs_editor(text: str) -> str:
    """VS-style code block with two blank lines after the last code line."""
    padded = (text or "").rstrip("\n") + "\n\n\n"
    return vs_editor(padded, lang="python")


def question_doc_block(q: dict, *, include_stub: bool = True) -> str:
    """Full practice-doc question content (subsection, prompt, stub, expected)."""
    parts: list[str] = ['<div class="q-doc">']
    subsection = (q.get("subsection") or "").strip()
    if subsection:
        parts.append(f'<div class="q-sub">{esc(subsection)}</div>')
    kind = (q.get("kind") or "").title()
    prompt = (q.get("prompt_full") or q.get("question") or "").strip()
    parts.append(
        f'<p class="q-prompt"><b>{esc(q["id"])} ({esc(kind)}):</b> {esc(prompt)}</p>'
    )
    stub = (q.get("code_stub") or "").strip()
    if include_stub and stub:
        parts.append("<h3>Question stub</h3>")
        parts.append(review_vs_editor(stub))
    expected = (q.get("expected_output") or "").strip()
    if expected:
        # Doc already prefixes with "Expected Output:"
        label, _, rest = expected.partition(":")
        if rest:
            parts.append(
                f'<div class="expected"><b>{esc(label.strip())}:</b> {esc(rest.strip())}</div>'
            )
        else:
            parts.append(f'<div class="expected">{esc(expected)}</div>')
    parts.append("</div>")
    return "".join(parts)


def question_slide(num: int, q: dict) -> str:
    code_file = q.get("code_file")
    raw = load_code(code_file)
    has_code = bool(raw.strip())
    has_stub = bool((q.get("code_stub") or "").strip())
    # Right panel when we have solution code or a question stub to show
    show_right = has_code or has_stub
    split_cls = "main-split" if show_right else "main-split no-code"

    interview = ['<div class="interview-box"><b>Interview — related questions</b>']
    for item in q.get("interview_qa", []):
        interview.append(f'<p class="qa-q"><b>Q:</b> {esc(item["q"])}</p>')
        interview.append(f'<p class="qa-a"><b>A:</b> {esc(item["a"])}</p>')
    interview.append("</div>")

    deep = q.get("topic_deepdive") or ""
    practice = ""
    if code_file:
        practice = (
            '<div class="panel-practice">'
            "<h3>Practice</h3>"
            f'<a class="file-link" href="PythonReview/{esc(code_file)}">{esc(code_file)}</a>'
            f'<span class="run-cmd">python PythonReview/{esc(code_file)}</span>'
            "</div>"
        )

    code_panel = ""
    if show_right:
        body_parts = [
            '<div class="panel-code">',
            '<div class="code-toolbar">',
            '<button type="button" class="btn-code-expand" onclick="toggleCodeExpand(this)">Expand</button>',
            "</div>",
            question_doc_block(q, include_stub=True),
        ]
        if has_code:
            body_parts.append('<div class="solution-label">Solution</div>')
            body_parts.append(review_vs_editor(raw))
        body_parts.append("</div>")
        code_panel = "".join(body_parts)

    # Left keeps teaching notes; for reasoning-only, also show full doc question
    question_heading = "Learning notes"
    question_body = ""
    if show_right:
        question_body = (
            f'<p>{esc(q["question"])}</p>'
            f'<div class="callout"><b>Learning intent:</b> {esc(q["learn_intent"])}</div>'
        )
    else:
        question_heading = "Definition / Question"
        question_body = (
            question_doc_block(q, include_stub=False)
            + f'<div class="callout"><b>Learning intent:</b> {esc(q["learn_intent"])}</div>'
        )

    left = f"""
      <h3>{question_heading}</h3>
      {question_body}
      {concepts_list(q.get("base_concepts", []))}
      <h3>Model answer / approach</h3>
      <div class="challenge">{esc(q["answer"])}</div>
      <h3>Deeper understanding</h3>
      <div class="keyword-box">{deep}</div>
      {"".join(interview)}
      {practice}
"""

    sub_meta = q.get("subsection") or q.get("section", "")
    divider = '<div class="split-divider" role="separator" aria-orientation="vertical" aria-label="Resize panels"></div>' if show_right else ""
    return f'''<div class="slide" id="slide-{num}">
<div class="slide-hdr">
  <div class="slide-meta">Slide {num} of {TOTAL} &middot; {esc(sub_meta)} &middot; {esc(q["id"])}</div>
  <div class="slide-title">{kind_badge(q["kind"])}{esc(q["id"])}: {esc(q["title"])}</div>
  <div class="slide-sub">Source: {esc(DOCX_NAME)} — {esc(DOCX_LEVEL)}</div>
</div>
<div class="slide-body">
  <div class="{split_cls}">
    <div class="panel-left">{left}</div>
    {divider}
    {code_panel}
  </div>
</div>
</div>'''


def build_nav() -> str:
    by_section: dict[str, list[tuple[int, dict]]] = defaultdict(list)
    for i, q in enumerate(QUESTIONS, 1):
        by_section[q["section"]].append((i, q))

    sections = []
    for section, items in by_section.items():
        topics = []
        for n, q in items:
            kind = q["kind"]
            topics.append(
                f'<div class="nav-topic">'
                f'<a onclick="goSlide({n})">{esc(q["id"])}. {esc(q["title"])}</a>'
                f'<ul class="nav-subs"><li>{esc(kind)}</li></ul>'
                f"</div>"
            )
        sections.append(
            f'<div class="nav-section"><h3>{esc(section)}</h3>{"".join(topics)}</div>'
        )

    return f'''<div class="slide active" id="slide-0">
<div class="nav-content">
  <h1>Python Review</h1>
  <div class="sub">{esc(DOCX_TITLE)}</div>
  <div class="org">{esc(DOCX_LEVEL)}</div>
  <div class="intro-card">
    <h3>Introduction</h3>
    <p>This deck follows the practice document <code>{esc(DOCX_NAME)}</code>.</p>
    <p>Same look as <code>PythonTraining.html</code> — left teaching panel, right VS-style code for coding questions.</p>
    <ul class="checklist">
      <li><b>{TOTAL}</b> question slides from the document</li>
      <li>Each slide: question, learning intent, base concepts, answer, deep dive, interview Q&amp;A</li>
      <li>Coding solutions live in <code>PythonReview/</code> and appear in the right panel</li>
      <li>Drag the center divider to widen the code panel; Expand still opens full-screen</li>
      <li>Use ← → keys, or Prev / Next / Navigation</li>
    </ul>
  </div>
  <div class="org">Click a topic below to jump to that slide</div>
  <div class="nav-grid">
{"".join(sections)}
  </div>
</div>
</div>'''


def main() -> None:
    slides = [build_nav()]
    for i, q in enumerate(QUESTIONS, 1):
        slides.append(question_slide(i, q))

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Python Review — {html.escape(DOCX_TITLE)}</title>
<style>{CSS}</style>
</head>
<body>
{"".join(slides)}
{NAV_BAR}
<script>{JS}</script>
</body>
</html>"""
    OUTPUT.write_text(page, encoding="utf-8")
    print(f"Generated {OUTPUT} ({len(page):,} bytes, {TOTAL + 1} slides)")


if __name__ == "__main__":
    main()
