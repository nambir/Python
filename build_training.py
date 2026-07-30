"""Generate PythonTraining.html — Batch 2 curriculum + Python-Set2 real projects."""
import html
import re
from pathlib import Path
from slide_keyword_deepdives import keyword_deepdives_for
from training_meta import TRAINING_META
from training_beginner import BEGINNER_CONTENT
from slide_glossary import glossary_for
from slide_scenarios import scenarios_for
from slide_diagrams import diagram_for
from slide_real_life import real_life_for
from slide_csharp_popups import render_csharp_popups
from slide_code import _CODE_SNIPPETS, code, code_table, highlight_line, split_learn

OUTPUT = Path(__file__).parent / "PythonTraining.html"
PROJECTS = Path(__file__).parent / "Projects"
TOTAL_SLIDES = 35

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

/* ── Slide body: left content | right code ── */
.slide-body { display: flex; flex-direction: column; gap: 0; }
.main-split {
  display: grid;
  grid-template-columns: minmax(180px, var(--split-left, 48%)) 12px minmax(240px, 1fr);
  gap: 0;
  align-items: start;
}
.main-split.no-code { grid-template-columns: 1fr; max-width: 900px; }
.panel-left { min-width: 0; padding-right: 8px; }
.panel-code { min-width: 0; position: sticky; top: 12px; padding-left: 8px; }
.panel-code .vs-editor + .vs-editor { margin-top: 12px; }
.panel-code .code-playground + .code-playground { margin-top: 14px; }

.code-playground {
  border: 1px solid #cfe0f5; border-radius: 6px; background: #fff; overflow: hidden;
}
.code-toolbar {
  display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
  padding: 6px 10px; background: #f0f7ff; border-bottom: 1px solid #cfe0f5;
}
.code-toolbar-label { font-size: 12px; font-weight: 700; color: #0066cc; margin-right: auto; }
.btn-run-py, .btn-reset-py {
  padding: 4px 12px; font-size: 12px; font-weight: 600; border: none; border-radius: 4px; cursor: pointer;
}
.btn-run-py { background: #0066cc; color: #fff; }
.btn-run-py:hover { background: #0052a3; }
.btn-run-py:disabled { opacity: .6; cursor: wait; }
.btn-reset-py { background: #fff; color: #555; border: 1px solid #ccc; }
.btn-reset-py:hover { background: #f5f5f5; }
.py-status { font-size: 11px; color: #666; }
.py-editor {
  display: block; width: 100%; min-height: 140px; max-height: none;
  padding: 10px 12px; border: none; resize: both;
  font-family: Consolas, 'Cascadia Mono', 'Courier New', monospace; font-size: 13px; line-height: 1.55;
  color: #000; background: #fff; tab-size: 4; white-space: pre; overflow: auto;
}
.py-editor:focus { outline: 2px solid #b3d1ff; outline-offset: -2px; }
.py-resize-top {
  height: 10px; cursor: ns-resize; flex-shrink: 0;
  background: linear-gradient(to bottom, #dbeafe, #f1f5f9);
  border-top: 1px solid #cbd5e1; border-bottom: 1px solid #e2e8f0;
  position: relative; touch-action: none; user-select: none;
}
.py-resize-top::after {
  content: ""; position: absolute; left: 50%; top: 3px; transform: translateX(-50%);
  width: 36px; height: 3px; border-radius: 2px; background: #94a3b8;
}
.py-resize-top:hover, .py-resize-top.dragging {
  background: linear-gradient(to bottom, #bfdbfe, #e2e8f0);
}
.py-resize-top:hover::after, .py-resize-top.dragging::after { background: #0066cc; }
body.py-height-dragging { cursor: ns-resize; user-select: none; }
.py-output {
  margin: 0; padding: 8px 12px; border-top: 1px solid #e2e8f0;
  background: #0f172a; color: #e2e8f0; font-family: Consolas, monospace; font-size: 12px;
  line-height: 1.45; white-space: pre-wrap; max-height: 180px; overflow: auto;
}
.py-output.err { color: #fecaca; }
.py-highlight { border-top: 1px solid #e2e8f0; padding: 4px 10px 8px; background: #fafafa; }
.py-highlight summary {
  cursor: pointer; font-size: 11px; color: #0066cc; font-weight: 600; padding: 4px 0;
}
.py-highlight .vs-editor { max-height: none; border: none; resize: vertical; overflow: auto; min-height: 120px; }
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

.interview-box { background: #e8f5e9; border-left: 3px solid #28a745; padding: 10px 12px; border-radius: 4px; margin-top: 8px; font-size: 12px; }
.interview-box p { margin: 6px 0 0; color: #1b5e20; line-height: 1.5; }
.interview-box .qa-q { margin-top: 10px; color: #1b5e20; font-style: normal; }
.interview-box .qa-a { margin-top: 4px; margin-left: 8px; color: #2e7d32; font-style: normal; }
.mistake-box { background: #fff5f5; border-left: 3px solid #e53e3e; padding: 10px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; line-height: 1.55; color: #1a1a2e; }
.mistake-box code { background: #ffe4e4; color: #c53030; border-radius: 3px; padding: 0 2px; }
.mistake-title { font-size: 12px; font-weight: 700; margin-bottom: 6px; display: block; }
.mistake-desc { margin-bottom: 8px; }
.mc-row { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 6px; }
.mc-col { border-radius: 5px; overflow: hidden; }
.mc-bad  { border: 1.5px solid #e53e3e; }
.mc-good { border: 1.5px solid #28a745; }
.mc-lbl  { display: block; padding: 3px 8px; font-size: 11px; font-weight: 700; }
.mc-bad  .mc-lbl { background: #fff5f5; color: #c53030; }
.mc-good .mc-lbl { background: #f0fff4; color: #276749; }
.mc-col .step-pre { margin: 0; border-radius: 0; border: none; border-top: 1px solid #e2e8f0; font-size: 11px; padding: 6px 8px; line-height: 1.5; }
.mistake-note { font-size: 11px; color: #555; margin-top: 4px; }
.before-after { display: grid; grid-template-columns: 1fr auto 1fr; gap: 10px; align-items: start; margin: 8px 0 12px; }
.ba-col { border-radius: 6px; overflow: hidden; }
.ba-bad  { border: 1.5px solid #e53e3e; }
.ba-good { border: 1.5px solid #28a745; }
.ba-label { padding: 4px 10px; font-size: 11px; font-weight: 700; }
.ba-bad  .ba-label { background: #fff5f5; color: #c53030; }
.ba-good .ba-label { background: #f0fff4; color: #276749; }
.ba-col .step-pre { margin: 0; border-radius: 0; border: none; border-top: 1px solid #e2e8f0; }
.ba-arrow { display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 700; color: #0066cc; padding-top: 24px; }
.quiz-box { margin: 8px 0 12px; }
.quiz-q { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 12px; margin-bottom: 8px; font-size: 12px; line-height: 1.55; }
.quiz-ans summary { cursor: pointer; color: #0066cc; font-weight: 600; font-size: 11px; padding: 2px 0; user-select: none; margin-top: 6px; display: block; }
.quiz-ans summary:hover { text-decoration: underline; }
.quiz-ans[open] summary { color: #276749; }
.quiz-ans .quiz-reveal { margin-top: 6px; padding: 8px 10px; background: #e8f5e9; border-left: 3px solid #28a745; border-radius: 4px; color: #1b5e20; font-size: 12px; }
.learn-steps { margin: 6px 0 10px 0; padding: 0; list-style: none; }
.learn-steps li { font-size: 12px; line-height: 1.5; margin-bottom: 10px; padding-left: 0; color: #1a1a2e; }
.learn-steps li b { color: #1a1a2e; font-weight: 700; }
.panel-left p { color: #1a1a2e; }
.step-pre { font-family: Consolas, 'Cascadia Mono', monospace; font-size: 11px; background: #f0f7ff; border: none; padding: 8px 10px; border-radius: 3px; margin: 6px 0; white-space: pre-wrap; line-height: 1.45; color: #1a1a2e; }
.step-result { font-size: 12px; color: #555; margin: 4px 0 6px 0; }
.step-result b { color: #1a1a2e; }
.learn-steps .data-tbl td { color: #1a1a2e; }
.cell-yes { color: #2e7d32; font-weight: 600; white-space: nowrap; }
.cell-no { color: #c62828; font-weight: 600; white-space: nowrap; }
.yn-yes::before { content: "\\2713  "; color: #2e7d32; font-weight: 700; }
.yn-no::before { content: "\\2717  "; color: #c62828; font-weight: 700; }

/* ── VS2022-style editor (one <tr> per line) ── */
.vs-editor { background: #fff; overflow: auto; max-height: calc(100vh - 140px); }
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

.tip { background: #fff8e6; border-left: 3px solid #f39c12; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.challenge { background: #e8f5e9; border-left: 3px solid #28a745; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.callout { background: #f0f7ff; border-left: 3px solid #0066cc; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.keyword-box { background: #f8fafc; border-left: 3px solid #0066cc; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; line-height: 1.5; color: #1a1a2e; }
.keyword-box .step-pre { margin-top: 6px; }

.flow-compare { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 10px 0 12px; }
.flow-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 12px; }
.flow-card h4 { font-size: 13px; color: #0066cc; margin: 0 0 8px; }
.flow-steps { display: flex; flex-direction: column; gap: 6px; }
.flow-step { background: #fff; border-left: 3px solid #0066cc; border-radius: 4px; padding: 7px 9px; font-size: 12px; line-height: 1.45; }
.flow-step b { color: #1a1a2e; }
.flow-code { display: block; margin-top: 4px; font-family: Consolas, monospace; font-size: 11px; color: #1a1a2e; background: #f0f7ff; padding: 6px 8px; border-radius: 3px; white-space: pre-wrap; }
.flow-arrow { text-align: center; color: #0066cc; font-weight: 700; font-size: 14px; line-height: 1; }
.flow-note { margin-top: 8px; font-size: 12px; color: #555; }

/* ── Interpreter pipeline diagram (slide 1) ── */
.interp-diagram { margin: 10px 0 14px; }
.interp-row {
  display: flex; align-items: stretch; justify-content: center; gap: 8px; flex-wrap: wrap;
}
.interp-side {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  min-width: 90px; text-align: center;
}
.interp-side .interp-icon {
  width: 52px; height: 52px; border-radius: 8px; border: 1px solid #cbd5e1;
  display: flex; align-items: center; justify-content: center;
  font-size: 22px; background: #fff; margin-bottom: 6px;
}
.interp-side.source .interp-icon { background: #f0f7ff; border-color: #0066cc; }
.interp-side.running .interp-icon { background: #f0fdf4; border-color: #16a34a; }
.interp-side b { display: block; font-size: 12px; color: #1a1a2e; }
.interp-side span { font-size: 10px; color: #555; }
.interp-h-arrow {
  display: flex; align-items: center; color: #64748b; font-weight: 700; font-size: 20px; padding: 0 2px;
}
.interp-box {
  background: #fff7ed; border: 2px solid #f59e0b; border-radius: 10px;
  padding: 18px 14px 10px; position: relative; min-width: 320px; flex: 1; max-width: 520px;
}
.interp-box::before {
  content: "Interpreter";
  position: absolute; top: -11px; left: 50%; transform: translateX(-50%);
  background: #fff7ed; color: #1a1a2e; font-size: 13px; font-weight: 700;
  padding: 0 8px;
}
.interp-inner {
  display: flex; align-items: flex-start; justify-content: center; gap: 8px; flex-wrap: wrap;
}
.interp-col { display: flex; flex-direction: column; align-items: center; gap: 4px; }
.interp-node {
  background: #e2e8f0; border: 1px solid #94a3b8; border-radius: 6px;
  padding: 10px 12px; min-width: 88px; text-align: center; font-size: 12px; font-weight: 700; color: #1a1a2e;
}
.interp-node.compiler { background: #e2e8f0; }
.interp-node.bytecode {
  background: #fef08a; border-color: #ca8a04; border-radius: 4px 12px 4px 4px;
  min-height: 42px; display: flex; align-items: center; justify-content: center;
}
.interp-node.vm { background: #64748b; color: #fff; border-color: #475569; }
.interp-inner-arrow { display: flex; align-items: center; color: #64748b; font-weight: 700; font-size: 18px; padding-top: 10px; }
/* ── Concept diagrams (all slides) ── */
.cdiag { margin: 10px 0 14px; }
.cdiag-row {
  display: flex; align-items: stretch; justify-content: center; gap: 6px; flex-wrap: wrap;
}
.cdiag-node {
  background: #f0f7ff; border: 1.5px solid #0066cc; border-radius: 8px;
  padding: 10px 12px; min-width: 88px; max-width: 140px; text-align: center;
}
.cdiag-node b { display: block; font-size: 12px; color: #1a1a2e; margin-bottom: 4px; }
.cdiag-node span { display: block; font-size: 10px; color: #555; line-height: 1.35; }
.cdiag-arrow {
  display: flex; align-items: center; color: #64748b; font-weight: 700; font-size: 18px; padding: 0 2px;
}
.cdiag-stack { display: flex; flex-direction: column; gap: 6px; max-width: 560px; }
.cdiag-layer {
  background: #fff7ed; border: 1.5px solid #f59e0b; border-radius: 8px;
  padding: 10px 14px; display: flex; gap: 12px; align-items: baseline;
}
.cdiag-layer b { font-size: 12px; color: #1a1a2e; min-width: 140px; }
.cdiag-layer span { font-size: 11px; color: #555; }

.cdiag-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 8px; max-width: 720px;
}
.cdiag-tile {
  background: #f0fdf4; border: 1.5px solid #16a34a; border-radius: 8px;
  padding: 10px 12px; text-align: center;
}
.cdiag-tile b { display: block; font-size: 12px; color: #14532d; margin-bottom: 4px; }
.cdiag-tile span { display: block; font-size: 10px; color: #555; line-height: 1.35; }

.cdiag-tree { max-width: 720px; text-align: center; }
.cdiag-tree-root {
  display: inline-block; background: #eff6ff; border: 2px solid #0066cc; border-radius: 8px;
  padding: 10px 16px; margin: 0 auto;
}
.cdiag-tree-root b { display: block; font-size: 13px; color: #1a1a2e; }
.cdiag-tree-root span { display: block; font-size: 10px; color: #555; margin-top: 3px; }
.cdiag-tree-stem {
  width: 2px; height: 14px; background: #94a3b8; margin: 0 auto;
}
.cdiag-tree-kids {
  display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;
  border-top: 2px solid #cbd5e1; padding-top: 10px; margin-top: 0;
}
.cdiag-tree-child {
  background: #f8fafc; border: 1.5px solid #64748b; border-radius: 8px;
  padding: 8px 12px; min-width: 140px; max-width: 200px; text-align: center;
}
.cdiag-tree-child b { display: block; font-size: 12px; color: #1a1a2e; margin-bottom: 3px; }
.cdiag-tree-child span { display: block; font-size: 10px; color: #555; line-height: 1.35; }

.cdiag-cycle {
  display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 6px;
  max-width: 720px; padding: 8px; background: #faf5ff; border: 1px dashed #a855f7; border-radius: 12px;
}
.cdiag-cycle-node {
  background: #fff; border: 1.5px solid #7c3aed; border-radius: 999px;
  padding: 8px 14px; text-align: center; min-width: 90px;
}
.cdiag-cycle-node b { display: block; font-size: 12px; color: #1a1a2e; }
.cdiag-cycle-node span { display: block; font-size: 10px; color: #555; }
.cdiag-cycle-arrow { color: #7c3aed; font-weight: 700; font-size: 16px; }
.cdiag-cycle-back { font-size: 20px; }

.cdiag-hub { max-width: 720px; text-align: center; }
.cdiag-spokes {
  display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-bottom: 10px;
}
.cdiag-spoke {
  background: #fdf2f8; border: 1.5px solid #db2777; border-radius: 8px;
  padding: 8px 12px; min-width: 110px; max-width: 160px;
}
.cdiag-spoke b { display: block; font-size: 11px; color: #9d174d; margin-bottom: 2px; }
.cdiag-spoke span { display: block; font-size: 10px; color: #555; }
.cdiag-hub-core {
  display: inline-block; background: #831843; color: #fff; border-radius: 10px;
  padding: 12px 20px; box-shadow: 0 2px 8px rgba(131, 24, 67, 0.25);
}
.cdiag-hub-core b { display: block; font-size: 13px; color: #fff; }
.cdiag-hub-core span { display: block; font-size: 10px; color: #fbcfe8; margin-top: 3px; }

.cdiag-fork { max-width: 720px; text-align: center; }
.cdiag-fork-q {
  display: inline-block; background: #ecfeff; border: 2px solid #0891b2; border-radius: 8px;
  padding: 10px 16px; font-size: 13px; color: #155e75;
}
.cdiag-fork-stem { width: 2px; height: 14px; background: #67e8f9; margin: 0 auto; }
.cdiag-fork-arms {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 8px; border-top: 2px solid #a5f3fc; padding-top: 10px;
}
.cdiag-fork-arm {
  background: #fff; border: 1.5px solid #0891b2; border-radius: 8px;
  padding: 10px 12px; text-align: left;
}
.cdiag-fork-arm b { display: block; font-size: 12px; color: #155e75; margin-bottom: 3px; }
.cdiag-fork-arm span { display: block; font-size: 10px; color: #555; line-height: 1.35; }

.cdiag-compare {
  display: grid; grid-template-columns: 1fr auto 1fr; gap: 12px; align-items: start;
  max-width: 720px;
}
.cdiag-compare-col {
  background: #f8fafc; border: 1.5px solid #64748b; border-radius: 8px; padding: 10px 14px;
}
.cdiag-compare-col h4 { font-size: 13px; color: #0066cc; margin: 0 0 6px; }
.cdiag-compare-col ul { margin: 0 0 0 16px; padding: 0; }
.cdiag-compare-col li { font-size: 11px; line-height: 1.45; margin-bottom: 3px; color: #334155; }
.cdiag-compare-vs {
  align-self: center; font-weight: 700; color: #94a3b8; font-size: 12px;
}

.real-life {
  margin: 10px 0 12px; padding: 10px 12px;
  background: #f0fdf4; border-left: 4px solid #16a34a; border-radius: 0 6px 6px 0;
  font-size: 12px; line-height: 1.45; color: #1a1a2e;
}
.real-life b { color: #14532d; }
.real-life .step-pre {
  margin-top: 8px; background: #fff; border: 1px solid #bbf7d0;
  white-space: pre; overflow-x: auto;
}

.interp-libs {
  margin-top: 8px; background: #86efac; border: 1px solid #16a34a; border-radius: 6px;
  padding: 8px 10px; font-size: 11px; font-weight: 700; color: #14532d; text-align: center; min-width: 100px;
}
.interp-v-arrow { color: #16a34a; font-weight: 700; font-size: 14px; line-height: 1; }

.panel-practice { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px 14px; margin-top: 14px; }
.panel-practice h3 { margin-top: 0; font-size: 14px; color: #0066cc; }
.checklist { list-style: none; margin: 0; padding: 0; }
.checklist li { padding: 3px 0; font-size: 12px; }
.checklist li::before { content: "\\2610  "; color: #0066cc; }
.file-link { display: inline-block; margin: 6px 8px 0 0; padding: 5px 12px; background: #0066cc; color: #fff; text-decoration: none; border-radius: 4px; font-size: 11px; font-weight: 600; }
.file-link:hover { background: #004499; }
.project-label { font-size: 12px; margin-top: 10px; margin-bottom: 4px; }
.run-cmd { font-family: Consolas, monospace; background: #2d2d2d; color: #dcdcdc; padding: 8px 12px; border-radius: 4px; font-size: 11px; margin-top: 6px; display: block; }

table.data-tbl, .ref-table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 12px; }
.data-tbl th, .ref-table th { background: #0066cc; color: #fff; padding: 6px 10px; text-align: left; }
.data-tbl td, .ref-table td { padding: 5px 10px; border-bottom: 1px solid #e8e8e8; }
.data-tbl tr:nth-child(even) td, .ref-table tr:nth-child(even) td { background: #f8fafc; }
.term-tbl td:first-child { font-weight: 700; color: #0066cc; white-space: nowrap; width: 120px; }
.term-tbl td:nth-child(3) { font-family: Consolas, monospace; font-size: 11px; color: #333; }
.scenario-tbl td:nth-child(2) { font-weight: 700; color: #0066cc; }
.project-map td:first-child { font-weight: 600; color: #0066cc; }

.tree-mockup { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 12px; margin: 8px 0; font-family: Consolas, monospace; font-size: 11px; line-height: 1.55; }
.tree-mockup .t-indent-1 { padding-left: 16px; }
.tree-mockup .t-indent-2 { padding-left: 32px; }
.tree-mockup .t-folder { color: #0066cc; font-weight: 700; }
.tree-mockup .t-file { color: #1a1a2e; }
.tree-mockup .t-note { color: #888; font-style: italic; font-size: 10px; }

.nav-bar { position: fixed; bottom: 0; left: 0; right: 0; height: 44px; background: #f0f0f0; border-top: 1px solid #ccc; display: flex; align-items: center; justify-content: space-between; padding: 0 48px; z-index: 999; }
.nav-bar button { padding: 6px 20px; font-size: 13px; font-weight: 600; border: none; border-radius: 4px; cursor: pointer; }
.nav-bar .btn-prev { background: #666; color: #fff; }
.nav-bar .btn-next { background: #0066cc; color: #fff; }
.nav-bar .btn-nav { background: #28a745; color: #fff; }
.nav-bar .slide-info { font-size: 12px; color: #555; }

.nav-content { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: calc(100vh - 44px); padding: 12px 16px; }
.nav-content h1 { font-size: 34px; margin-bottom: 4px; }
.nav-content .sub { font-size: 16px; color: #0066cc; }
.nav-content .org { font-size: 13px; color: #666; margin: 6px 0 14px; }
.nav-grid {
  display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 12px;
  max-width: 1400px; width: calc(100vw - 48px);
}
.nav-section { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px 14px; overflow: visible; }
.nav-section-1 { grid-column: span 5; }
.nav-section-2 { grid-column: span 3; }
.nav-section-3 { grid-column: span 4; }
.nav-section-4 { grid-column: span 3; }
.nav-section-5 { grid-column: span 6; }
.nav-section-6 { grid-column: span 3; }
.nav-section-1 .nav-links,
.nav-section-3 .nav-links,
.nav-section-5 .nav-links { column-count: 2; column-gap: 24px; }
.nav-section h3 { font-size: 15px; margin-bottom: 7px; border-bottom: 2px solid #0066cc; padding-bottom: 4px; }
.nav-section a { display: block; padding: 1px 0; color: #0066cc; font-size: 15px; cursor: pointer; text-decoration: none; }
.nav-section a:hover { text-decoration: underline; }
.nav-topic { margin: 0 0 7px; break-inside: avoid; }
.nav-topic a.nav-main { font-weight: 600; }
.nav-subs {
  margin: 2px 0 0 14px; padding: 0; list-style: none;
}
.nav-subs li { line-height: 1.3; padding: 1px 0; }
.nav-subs li::before { content: "– "; color: #64748b; }
.nav-subs li a { display: inline; padding: 0; color: #0066cc; font-size: 15px; font-weight: 400; }

@media (max-width: 900px) {
  .slide { padding: 16px 16px 56px; }
  .main-split, .nav-grid { grid-template-columns: 1fr; }
  .main-split { grid-template-columns: 1fr !important; }
  .split-divider { display: none; }
  .nav-section { grid-column: 1 / -1; }
  .nav-section-1 .nav-links,
  .nav-section-3 .nav-links,
  .nav-section-5 .nav-links { column-count: 1; }
  .flow-compare, .cdiag-compare { grid-template-columns: 1fr; }
  .cdiag-compare-vs { display: none; }
  .panel-code { position: static; }
  .vs-editor { max-height: 50vh; }
  .nav-bar { padding: 0 16px; }
}

/* ── Slide audio player (HTML5 — pause/resume + seek) ── */
.audio-player { margin-top: 10px; max-width: 520px; }
.audio-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.btn-play {
  width: 36px; height: 36px; border: none; border-radius: 50%; background: #0066cc; color: #fff;
  font-size: 14px; cursor: pointer; flex-shrink: 0; line-height: 1;
}
.btn-play:hover { background: #004499; }
.btn-play.playing { background: #28a745; }
.btn-reset {
  width: 30px; height: 30px; border: none; border-radius: 50%; background: #888; color: #fff;
  font-size: 16px; cursor: pointer; flex-shrink: 0;
}
.btn-reset:hover { background: #555; }
.audio-seek {
  flex: 1; min-width: 120px; height: 6px; cursor: pointer; accent-color: #0066cc;
}
.audio-time { font-size: 11px; color: #555; font-family: Consolas, monospace; white-space: nowrap; min-width: 90px; }
.audio-badge {
  font-size: 10px; background: #f0f7ff; color: #0066cc; padding: 2px 8px; border-radius: 10px; font-weight: 600;
}
.nav-content .audio-player { margin: 12px auto 20px; }
.nav-bar .btn-audio-nav {
  background: #0066cc; color: #fff; border: none; padding: 6px 12px; border-radius: 4px;
  font-size: 12px; font-weight: 600; cursor: pointer;
}
.nav-bar .btn-audio-nav:hover { background: #004499; }
.audio-missing { font-size: 11px; color: #c62828; margin-top: 4px; }

/* ── C# comparison — draggable float window ── */
.btn-csharp-pop {
  margin-left: 6px; padding: 2px 9px; font-size: 11px; font-weight: 600;
  border: 1px solid #7c3aed; border-radius: 4px; background: #f5f3ff; color: #5b21b6;
  cursor: pointer; vertical-align: baseline;
}
.btn-csharp-pop:hover { background: #ede9fe; }
.csharp-float-win {
  display: none; position: fixed; left: 80px; top: 72px; width: min(720px, calc(100vw - 24px));
  max-height: calc(100vh - 88px); z-index: 2000;
  background: #fff; border-radius: 10px; border: 1px solid #cbd5e1;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.22);
  flex-direction: column; overflow: hidden;
}
.csharp-float-win.open { display: flex; }
.csharp-float-win.dragging { user-select: none; cursor: grabbing; }
.csharp-float-hdr {
  display: flex; align-items: center; gap: 8px;
  padding: 10px 12px 10px 14px; border-bottom: 1px solid #e2e8f0;
  background: linear-gradient(180deg, #f5f3ff 0%, #ede9fe 100%);
  cursor: grab; flex-shrink: 0; user-select: none;
}
.csharp-float-win.dragging .csharp-float-hdr { cursor: grabbing; }
.csharp-float-drag { color: #7c3aed; font-size: 14px; line-height: 1; letter-spacing: -2px; }
.csharp-float-hdr h4 { margin: 0; flex: 1; font-size: 13px; color: #5b21b6; }
.csharp-float-close {
  width: 28px; height: 28px; border: none; border-radius: 6px; background: #ede9fe;
  color: #5b21b6; font-size: 20px; line-height: 1; cursor: pointer; flex-shrink: 0;
}
.csharp-float-close:hover { background: #ddd6fe; }
.csharp-float-body {
  padding: 14px 16px 16px; font-size: 12px; font-weight: 400; line-height: 1.5; color: #1a1a2e;
  overflow-y: auto; overflow-x: hidden; flex: 1; min-height: 0;
}
.csharp-float-body p { margin-bottom: 8px; font-weight: 400; }
.csharp-float-body b { font-weight: 600; }
.csharp-float-body code { font-weight: 400; font-size: 11px; }
.csharp-pop-note { margin-top: 10px; color: #555; font-size: 11px; font-weight: 400; }
.csharp-pop-note b { font-weight: 600; }
.csharp-float-body .vs-editor { margin: 6px 0 10px; max-height: none; overflow: visible; }
.csharp-float-body .vs-editor-compact { max-height: none; }
.csharp-float-body .vs-editor table.vs-code { font-size: 12px; width: 100%; table-layout: fixed; }
.csharp-float-body .vs-editor table.vs-code td.src { white-space: pre-wrap; word-break: break-word; overflow-wrap: anywhere; }
.csharp-pop-tbl { margin-top: 6px; font-size: 11px; }
.csharp-pop-tbl td { vertical-align: top; }
.csharp-pop-tbl td:first-child { white-space: normal; }
.csharp-diff {
  margin: 0 0 12px; padding: 10px 12px; border: 1px solid #ddd6fe; border-radius: 8px;
  background: linear-gradient(180deg, #faf5ff 0%, #f8fafc 100%);
}
.csharp-diff-label {
  font-size: 11px; font-weight: 700; color: #5b21b6; letter-spacing: .3px;
  text-transform: uppercase; margin-bottom: 8px;
}
.csharp-diff-grid {
  display: grid; grid-template-columns: 1fr auto 1fr; gap: 8px; align-items: stretch;
}
.csharp-diff-col {
  background: #fff; border: 1px solid #e9d5ff; border-radius: 6px; padding: 8px 10px; min-width: 0;
}
.csharp-diff-lang { font-size: 11px; font-weight: 700; color: #0066cc; margin-bottom: 4px; }
.csharp-diff-code {
  font-family: Consolas, 'Cascadia Mono', monospace; font-size: 12px; line-height: 1.45;
  color: #1a1a2e; word-break: break-word;
}
.csharp-diff-vs {
  align-self: center; font-size: 11px; font-weight: 800; color: #7c3aed;
  padding: 4px 2px; writing-mode: horizontal-tb;
}
.csharp-diff-mark {
  background: #fecaca; color: #991b1b; border: 1px solid #f87171;
  border-radius: 3px; padding: 0 3px; font-weight: 700;
}
.csharp-diff-hint { margin: 0 0 12px; font-size: 12px; color: #334155; line-height: 1.45; }
@media (max-width: 700px) {
  .csharp-diff-grid { grid-template-columns: 1fr; }
  .csharp-diff-vs { text-align: center; }
}
"""

JS = """
let current = 0;
let activeSlide = null;
let seekDragging = false;
const slideOrder = [0];
for (let i = 1; i <= """ + str(TOTAL_SLIDES) + """; i++) slideOrder.push(i);
const totalTopics = """ + str(TOTAL_SLIDES) + """;

function fmtTime(sec) {
  if (!isFinite(sec) || sec < 0) sec = 0;
  const m = Math.floor(sec / 60);
  const s = Math.floor(sec % 60);
  return m + ':' + String(s).padStart(2, '0');
}

function getAudio(n) {
  return document.getElementById('audio-' + n);
}

function getPlayBtn(n) {
  return document.getElementById('play-btn-' + n);
}

function setPlayingUI(n, on) {
  const btn = getPlayBtn(n);
  if (btn) {
    btn.classList.toggle('playing', on);
    btn.innerHTML = on ? '&#9646;&#9646;' : '&#9654;';
    btn.title = on ? 'Pause' : 'Play (resumes where you left off)';
  }
}

function updateTimeUI(n) {
  const audio = getAudio(n);
  const timeEl = document.getElementById('time-' + n);
  const seek = document.getElementById('seek-' + n);
  if (!audio || !timeEl) return;
  timeEl.textContent = fmtTime(audio.currentTime) + ' / ' + fmtTime(audio.duration);
  if (seek && !seekDragging && audio.duration) {
    seek.value = Math.round((audio.currentTime / audio.duration) * 1000);
  }
}

function pauseAllExcept(keep) {
  for (let i = 0; i <= """ + str(TOTAL_SLIDES) + """; i++) {
    if (i === keep) continue;
    const a = getAudio(i);
    if (a && !a.paused) a.pause();
    setPlayingUI(i, false);
  }
  if (keep === null) activeSlide = null;
}

function togglePlay(n) {
  const audio = getAudio(n);
  if (!audio) return;
  if (audio.error || (audio.readyState === 0 && !audio.src)) {
    alert('Audio file missing. Run: pip install edge-tts && python generate_audio.py');
    return;
  }
  if (!audio.paused && activeSlide === n) {
    audio.pause();
    setPlayingUI(n, false);
    activeSlide = null;
    return;
  }
  pauseAllExcept(n);
  audio.play().then(() => {
    activeSlide = n;
    setPlayingUI(n, true);
  }).catch(err => {
    console.error(err);
    alert('Could not play audio. Run: python generate_audio.py');
  });
}

function resetAudio(n) {
  const audio = getAudio(n);
  if (!audio) return;
  audio.pause();
  audio.currentTime = 0;
  setPlayingUI(n, false);
  if (activeSlide === n) activeSlide = null;
  updateTimeUI(n);
}

function onSeekDrag(n, val) {
  seekDragging = true;
  const audio = getAudio(n);
  if (!audio || !audio.duration) return;
  audio.currentTime = (parseInt(val, 10) / 1000) * audio.duration;
  updateTimeUI(n);
}

function onSeekCommit(n, val) {
  seekDragging = false;
  onSeekDrag(n, val);
}

function initAudioPlayers() {
  for (let i = 0; i <= """ + str(TOTAL_SLIDES) + """; i++) {
    const audio = getAudio(i);
    if (!audio) continue;
    audio.addEventListener('timeupdate', () => {
      if (activeSlide === i) updateTimeUI(i);
    });
    audio.addEventListener('loadedmetadata', () => updateTimeUI(i));
    audio.addEventListener('ended', () => {
      setPlayingUI(i, false);
      if (activeSlide === i) activeSlide = null;
      updateTimeUI(i);
    });
    audio.addEventListener('error', () => {
      const player = document.getElementById('player-' + i);
      if (player && !player.querySelector('.audio-missing')) {
        const msg = document.createElement('div');
        msg.className = 'audio-missing';
        msg.textContent = 'MP3 missing — run: python generate_audio.py';
        player.appendChild(msg);
      }
    });
  }
}

function showSlide(n) {
  if (!slideOrder.includes(n)) return;
  pauseAllExcept(null);
  endSplitDrag();
  document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
  const el = document.getElementById('slide-' + n);
  if (el) {
    el.classList.add('active');
    current = n;
    el.scrollTop = 0;
    const info = document.getElementById('slideInfo');
    if (info) info.textContent = n === 0 ? 'Navigation' : 'Slide ' + n + ' of ' + totalTopics;
    updateTimeUI(n);
    applySavedSplit(el);
    const hash = n === 0 ? 'nav' : String(n);
    if (location.hash.replace('#', '') !== hash) {
      location.hash = hash;
    }
    try { localStorage.setItem('pythonTrainingSlide', String(n)); } catch (_) {}
  }
}
function goSlide(n) { showSlide(n); }
function nextSlide() {
  const idx = slideOrder.indexOf(current);
  if (idx < slideOrder.length - 1) showSlide(slideOrder[idx + 1]);
}
function prevSlide() {
  const idx = slideOrder.indexOf(current);
  if (idx > 0) showSlide(slideOrder[idx - 1]);
}
window.addEventListener('hashchange', () => {
  const h = (location.hash || '').replace('#', '');
  const n = (h === '' || h === 'nav') ? 0 : (parseInt(h, 10) || 0);
  if (n !== current) showSlide(n);
});
const SPLIT_KEY = 'pythonTrainingSplitLeft';
let splitDragging = null;
function getSavedSplit() {
  const v = parseFloat(localStorage.getItem(SPLIT_KEY) || '');
  return (Number.isFinite(v) && v >= 20 && v <= 75) ? v : 48;
}
function applySplitTo(split, pct) {
  if (!split || split.classList.contains('no-code')) return;
  split.style.setProperty('--split-left', pct + '%');
}
function applySavedSplit(root) {
  const pct = getSavedSplit();
  (root || document).querySelectorAll('.main-split:not(.no-code)').forEach(s => applySplitTo(s, pct));
}
function initSplitDividers() {
  document.querySelectorAll('.split-divider').forEach(div => {
    if (div.dataset.splitReady) return;
    div.dataset.splitReady = '1';
    div.title = 'Drag to resize panels';
    div.addEventListener('pointerdown', e => {
      if (e.button !== 0) return;
      const split = div.closest('.main-split');
      if (!split || split.classList.contains('no-code')) return;
      const rect = split.getBoundingClientRect();
      splitDragging = { split, div, left: rect.left, width: rect.width };
      div.classList.add('dragging');
      document.body.classList.add('split-dragging');
      try { div.setPointerCapture(e.pointerId); } catch (_) {}
      e.preventDefault();
    });
  });
}
document.addEventListener('pointermove', e => {
  if (!splitDragging) return;
  const { split, left, width } = splitDragging;
  if (width < 80) return;
  let pct = ((e.clientX - left) / width) * 100;
  pct = Math.max(20, Math.min(75, pct));
  applySplitTo(split, pct);
  localStorage.setItem(SPLIT_KEY, String(Math.round(pct * 10) / 10));
});
function endSplitDrag() {
  if (!splitDragging) return;
  splitDragging.div.classList.remove('dragging');
  document.body.classList.remove('split-dragging');
  splitDragging = null;
}
document.addEventListener('pointerup', endSplitDrag);
document.addEventListener('pointercancel', endSplitDrag);
let csharpDrag = { active: false, win: null, startX: 0, startY: 0, origLeft: 0, origTop: 0 };

function bringCsharpWinToFront(win) {
  document.querySelectorAll('.csharp-float-win.open').forEach(w => { w.style.zIndex = '2000'; });
  win.style.zIndex = '2010';
}

function centerCsharpWin(win) {
  const w = win.offsetWidth || 720;
  const h = win.offsetHeight || 480;
  win.style.left = Math.max(12, (window.innerWidth - w) / 2) + 'px';
  win.style.top = Math.max(12, (window.innerHeight - h) / 2) + 'px';
}

function openCsharpWin(id) {
  const el = document.getElementById('csharp-win-' + id);
  if (!el) return;
  el.classList.add('open');
  bringCsharpWinToFront(el);
  if (!el.dataset.positioned) {
    centerCsharpWin(el);
    el.dataset.positioned = '1';
  }
}
function openCsharpPop(id) { openCsharpWin(id); }

function closeCsharpWin(id) {
  const el = document.getElementById('csharp-win-' + id);
  if (el) el.classList.remove('open');
}
function closeCsharpPop(id) { closeCsharpWin(id); }

function closeAllCsharpWins() {
  document.querySelectorAll('.csharp-float-win.open').forEach(el => el.classList.remove('open'));
}

function initCsharpFloatWindows() {
  document.querySelectorAll('.csharp-float-win').forEach(win => {
    const hdr = win.querySelector('.csharp-float-hdr');
    if (!hdr) return;
    hdr.addEventListener('mousedown', (e) => {
      if (e.target.closest('.csharp-float-close')) return;
      bringCsharpWinToFront(win);
      csharpDrag.active = true;
      csharpDrag.win = win;
      const rect = win.getBoundingClientRect();
      csharpDrag.startX = e.clientX;
      csharpDrag.startY = e.clientY;
      csharpDrag.origLeft = rect.left;
      csharpDrag.origTop = rect.top;
      win.classList.add('dragging');
      e.preventDefault();
    });
    win.addEventListener('mousedown', () => bringCsharpWinToFront(win));
  });
  document.addEventListener('mousemove', (e) => {
    if (!csharpDrag.active || !csharpDrag.win) return;
    const win = csharpDrag.win;
    const dx = e.clientX - csharpDrag.startX;
    const dy = e.clientY - csharpDrag.startY;
    const w = win.offsetWidth;
    const h = win.offsetHeight;
    const left = Math.min(Math.max(0, csharpDrag.origLeft + dx), window.innerWidth - w);
    const top = Math.min(Math.max(0, csharpDrag.origTop + dy), window.innerHeight - h);
    win.style.left = left + 'px';
    win.style.top = top + 'px';
  });
  document.addEventListener('mouseup', () => {
    if (csharpDrag.win) csharpDrag.win.classList.remove('dragging');
    csharpDrag.active = false;
    csharpDrag.win = null;
  });
}
document.addEventListener('keydown', function(e) {
  const tag = (e.target && e.target.tagName) ? e.target.tagName.toLowerCase() : '';
  if (tag === 'textarea' || tag === 'input' || (e.target && e.target.isContentEditable)) return;
  if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
  if (e.key === 'Home') { e.preventDefault(); showSlide(0); }
  if (e.key === 'a' || e.key === 'A') { e.preventDefault(); togglePlay(current); }
  if (e.key === 'Escape') closeAllCsharpWins();
});
document.addEventListener('DOMContentLoaded', () => {
  try { initAudioPlayers(); } catch (err) { console.warn('audio init', err); }
  try { initCsharpFloatWindows(); } catch (err) { console.warn('csharp init', err); }
  try {
    document.querySelectorAll('.py-editor').forEach(ed => {
      ed.dataset.original = ed.value;
    });
    initPyEditorTopResize();
    initSplitDividers();
    applySavedSplit(document);
  } catch (err) { console.warn('editor init', err); }
  const h = (location.hash || '').replace('#', '');
  let start = 0;
  if (h === 'nav') start = 0;
  else if (h !== '') start = parseInt(h, 10) || 0;
  else {
    try {
      const saved = parseInt(localStorage.getItem('pythonTrainingSlide') || '', 10);
      if (Number.isFinite(saved) && slideOrder.includes(saved)) start = saved;
    } catch (_) {}
  }
  showSlide(start);
});

/* ── In-browser Python (Pyodide) playground ── */
let pyodideReady = null;
let pyHeightDrag = null;
function initPyEditorTopResize() {
  document.querySelectorAll('.py-resize-top').forEach(handle => {
    handle.addEventListener('pointerdown', (e) => {
      if (e.button !== 0) return;
      const target = handle.nextElementSibling;
      if (!target) return;
      const isEditor = target.classList && target.classList.contains('py-editor');
      const isVs = target.classList && target.classList.contains('vs-editor');
      if (!isEditor && !isVs) return;
      e.preventDefault();
      handle.classList.add('dragging');
      document.body.classList.add('py-height-dragging');
      handle.setPointerCapture(e.pointerId);
      pyHeightDrag = {
        handle,
        target,
        startY: e.clientY,
        startH: target.getBoundingClientRect().height,
      };
    });
  });
  window.addEventListener('pointermove', (e) => {
    if (!pyHeightDrag) return;
    const next = Math.max(100, pyHeightDrag.startH + (pyHeightDrag.startY - e.clientY));
    pyHeightDrag.target.style.height = next + 'px';
    pyHeightDrag.target.style.maxHeight = 'none';
  });
  window.addEventListener('pointerup', () => {
    if (!pyHeightDrag) return;
    pyHeightDrag.handle.classList.remove('dragging');
    document.body.classList.remove('py-height-dragging');
    pyHeightDrag = null;
  });
}
function loadPyodideScript() {
  return new Promise((resolve, reject) => {
    if (typeof loadPyodide === 'function') { resolve(); return; }
    const existing = document.querySelector('script[data-pyodide]');
    if (existing) {
      existing.addEventListener('load', () => resolve());
      existing.addEventListener('error', () => reject(new Error('Pyodide script failed to load')));
      return;
    }
    const s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js';
    s.async = true;
    s.dataset.pyodide = '1';
    s.onload = () => resolve();
    s.onerror = () => reject(new Error(
      'Could not load Pyodide from the internet. Open via http://localhost (not file://), or check your network.'
    ));
    document.head.appendChild(s);
  });
}
async function ensurePyodide(statusEl) {
  if (pyodideReady) return pyodideReady;
  if (statusEl) statusEl.textContent = 'Loading Python (first time)…';
  await loadPyodideScript();
  if (typeof loadPyodide !== 'function') {
    throw new Error('Pyodide failed to load. Use http://localhost (not file://) and check your network.');
  }
  pyodideReady = loadPyodide({ indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/' });
  const py = await pyodideReady;
  if (statusEl) statusEl.textContent = 'Python ready';
  return py;
}
function resetPlayground(btn) {
  const box = btn.closest('.code-playground');
  if (!box) return;
  const ed = box.querySelector('.py-editor');
  const out = box.querySelector('.py-output');
  const status = box.querySelector('.py-status');
  if (ed) {
    if (ed.dataset.original == null) ed.dataset.original = ed.defaultValue;
    ed.value = ed.dataset.original;
  }
  if (out) { out.hidden = true; out.textContent = ''; out.classList.remove('err'); }
  if (status) status.textContent = '';
}
async function runPlayground(btn) {
  const box = btn.closest('.code-playground');
  if (!box) return;
  const ed = box.querySelector('.py-editor');
  const out = box.querySelector('.py-output');
  const status = box.querySelector('.py-status');
  if (!ed || !out) return;
  btn.disabled = true;
  out.hidden = false;
  out.classList.remove('err');
  out.textContent = '';
  try {
    const py = await ensurePyodide(status);
    if (status) status.textContent = 'Running…';
    let stdout = [];
    let stderr = [];
    // Pyodide "batched" omits the trailing newline that print() writes — add it back
    // so the black output box matches a normal Python terminal.
    py.setStdout({
      batched: (s) => { stdout.push(s.endsWith('\\n') ? s : (s + '\\n')); },
      isatty: false,
    });
    py.setStderr({
      batched: (s) => { stderr.push(s.endsWith('\\n') ? s : (s + '\\n')); },
      isatty: false,
    });
    try {
      await py.runPythonAsync(ed.value);
      const text = (stdout.join('') + stderr.join('')).replace(/\\n$/, '');
      out.textContent = text || '(ran successfully — no printed output)';
      if (stderr.length) out.classList.add('err');
      if (status) status.textContent = 'Done';
    } catch (err) {
      out.classList.add('err');
      const printed = (stdout.join('') + stderr.join('')).replace(/\\n$/, '');
      out.textContent = (printed ? printed + '\\n' : '') + String(err);
      if (status) status.textContent = 'Error';
    }
  } catch (err) {
    out.classList.add('err');
    out.textContent = String(err);
    if (status) status.textContent = 'Failed to start Python';
  } finally {
    btn.disabled = false;
  }
}
"""

NAV_BAR = """
<div class="nav-bar">
  <button class="btn-prev" onclick="prevSlide()">&larr; Prev</button>
  <button class="btn-nav" onclick="goSlide(0)">&#9776; Navigation</button>
  <button type="button" class="btn-audio-nav" onclick="togglePlay(current)" title="Play / pause current slide audio">&#128266; Audio</button>
  <span class="slide-info" id="slideInfo">Navigation</span>
  <button class="btn-next" onclick="nextSlide()">Next &rarr;</button>
</div>
"""

# Week-based curriculum map — matches Batch 2 syllabus (Weeks 1–4)
WEEK_SECTIONS: list[tuple[str, list[int]]] = [
    ("Week 1 — Foundations", list(range(1, 12))),
    ("Week 2 — Collections & OOP", list(range(12, 18))),
    ("Week 3 — Advanced Core", list(range(18, 28))),
    ("Week 4 — Web Stack", [28]),
    ("Real Projects (Python-Set2)", list(range(29, 35))),
    ("Appendix", [35]),
]

# Syllabus-style subtopics shown under each main nav link (mentor outline)
SLIDE_SUBTOPICS: dict[int, list[str]] = {
    1: ["Advantages vs C#", "Interpreted / bytecode", "Indentation", "Duck typing"],
    2: ["Install & PATH", "pip / versions", "REPL vs script", "IDE (Cursor / VS Code)"],
    3: ["Slides → Projects → Python-Set2", "venv per project"],
    4: ["PEP 8", "PEP 257 docstrings", "PEP 20 Zen", "pyproject.toml"],
    5: [
        "Primitive: int, str, float, bool",
        "List",
        "Tuple",
        "Dict",
        "Set / frozenset",
    ],
    6: ["Type hints", "Optional / Union", "Protocol", "mypy"],
    7: [
        "Arithmetic",
        "Comparison / Relational",
        "Assignment",
        "Logical",
        "Bitwise",
        "Membership (in)",
        "Identity (is)",
        "Walrus (:=)",
    ],
    8: ["if / elif / else", "while", "for", "break / continue / pass"],
    9: ["List", "Set", "Dictionary", "Generator"],
    10: [
        "Positional & keyword args",
        "Recursion",
        "Anonymous (lambda)",
        "Local & global scope",
        "Pure / higher-order functions",
    ],
    11: [
        "map",
        "zip",
        "filter",
        "reduce",
        "enumerate",
        "type / id / range",
        "sorted / max / min",
    ],
    12: ["Counter", "OrderedDict", "defaultdict", "namedtuple", "deque"],
    13: ["Reference counting", "Generational GC", "weakref"],
    14: ["BaseModel", "Field / validators", "model_validate / dump"],
    15: [
        "Class",
        "Inheritance",
        "Encapsulation",
        "Polymorphism",
        "Abstract classes",
    ],
    16: ["__get__ / __set__", "property", "Dunder / magic methods"],
    17: ["yield", "Generator expressions", "Lazy iteration"],
    18: ["@decorator syntax", "functools.wraps", "Common patterns"],
    19: ["try / except / else / finally", "raise / custom exceptions"],
    20: ["Threading", "Multiprocessing", "GIL"],
    21: ["async / await", "asyncio.gather", "Event loop"],
    22: ["Levels (DEBUG→CRITICAL)", "Handlers / formatters", "RotatingFileHandler"],
    23: ["unittest / pytest", "assert", "mock / patch"],
    24: ["re.search / match / findall", "Groups", "Raw strings"],
    25: ["open / with", "pathlib", "json / csv"],
    26: ["with protocol", "@contextmanager", "__enter__ / __exit__"],
    27: ["python -m venv", "activate", "requirements.txt"],
    28: ["Routes + Depends", "Pydantic schemas", "SQLAlchemy ORM", "Service layer"],
    29: ["pythonBasics", "Google exercises", "Pandas", "Django / DRF", "Pipecat"],
    30: ["MyClass", "MyCollections", "MyLoops", "MyModules", "MyUnitTesting"],
    31: ["babynames (regex)", "copyspecial (files)", "Titanic (pandas)"],
    32: ["MVT / templates", "Auth / JWT", "Serializers / ViewSets"],
    33: ["STT → LLM → TTS", "WebRTC", "Voice pipeline phases"],
    34: ["routes / services / schemas", "tests at root", "App-per-domain"],
    35: ["null → None", "using → with", "pass / NotImplementedError", "venv ≈ NuGet"],
}

MODULE_MAP = {
    n: title
    for title, nums in WEEK_SECTIONS
    for n in nums
}


def module_for(n):
    return MODULE_MAP.get(n, "Python Training 2026")


# slide_num -> list of (filename, run_command)
SLIDE_PROJECT_FILES: dict[int, list[tuple[str, str | None]]] = {
    1: [("00_python_fundamentals.py", "python Projects/00_python_fundamentals.py")],
    2: [("00_windows_setup.py", "python Projects/00_windows_setup.py")],
    3: [("01_datatypes.py", "python Projects/01_datatypes.py")],
    4: [("02_getting_started.py", "python Projects/02_getting_started.py")],
    5: [("03_operators.py", "python Projects/03_operators.py")],
    6: [("04_flow_control.py", "python Projects/04_flow_control.py")],
    7: [("05_comprehensions.py", "python Projects/05_comprehensions.py")],
    8: [("06_functions.py", "python Projects/06_functions.py")],
    9: [("07_builtins.py", "python Projects/07_builtins.py")],
    10: [("08_oop.py", "python Projects/08_oop.py")],
    11: [("09_decorators.py", "python Projects/09_decorators.py")],
    12: [("10_descriptors.py", "python Projects/10_descriptors.py")],
    13: [("11_generators.py", "python Projects/11_generators.py")],
    14: [("12_typing.py", "python Projects/12_typing.py")],
    15: [("13_file_operations.py", "python Projects/13_file_operations.py")],
    16: [("14_exceptions.py", "python Projects/14_exceptions.py")],
    17: [("15_regex.py", "python Projects/15_regex.py")],
    18: [("16_collections.py", "python Projects/16_collections.py")],
    19: [("17_unit_testing.py", "pytest Projects/test_17_unit_testing.py -v")],
    20: [("18_threading.py", "python Projects/18_threading.py")],
    21: [("19_context_managers.py", "python Projects/19_context_managers.py")],
    22: [("20_async.py", "python Projects/20_async.py")],
    23: [("21_venv_guide.md", None)],
    24: [("README.md", None)],
    25: [("README.md", None)],
    26: [("README.md", None)],
    27: [("README.md", None)],
    28: [("README.md", None)],
    29: [("README.md", None)],
    30: [("28_csharp_vs_python.md", None)],
    31: [("31_pep_standards.md", None)],
    32: [("32_memory_gc.py", "python Projects/32_memory_gc.py")],
    33: [("33_logging.py", "python Projects/33_logging.py")],
    34: [("34_pydantic_demo.py", "python Projects/34_pydantic_demo.py")],
    35: [("35_fastapi_sqlalchemy.md", None)],
}


def tree_row(indent, icon, name, cls, note=""):
    note_html = f' <span class="t-note">— {note}</span>' if note else ""
    return f'<div class="t-indent-{indent}"><span class="{cls}">{icon} {name}</span>{note_html}</div>'


def tree(rows):
    return f'<div class="tree-mockup">{rows}</div>'


def python_vs_csharp_flow() -> str:
    return '''
<h3>Inside the Python interpreter</h3>
<div class="interp-diagram">
  <div class="interp-row">
    <div class="interp-side source">
      <div class="interp-icon">&#128196;</div>
      <b>Source code</b>
      <span><code>.py</code></span>
    </div>
    <div class="interp-h-arrow">&rarr;</div>
    <div class="interp-box">
      <div class="interp-inner">
        <div class="interp-col">
          <div class="interp-node compiler">Compiler</div>
        </div>
        <div class="interp-inner-arrow">&rarr;</div>
        <div class="interp-col">
          <div class="interp-node bytecode">Byte code</div>
        </div>
        <div class="interp-inner-arrow">&rarr;</div>
        <div class="interp-col">
          <div class="interp-node vm">Virtual machine</div>
          <div class="interp-v-arrow">&uarr;</div>
          <div class="interp-libs">Library modules</div>
        </div>
      </div>
    </div>
    <div class="interp-h-arrow">&rarr;</div>
    <div class="interp-side running">
      <div class="interp-icon">&#128161;</div>
      <b>Running code</b>
      <span>output / result</span>
    </div>
  </div>
  <p class="flow-note"><b>Read it:</b> Source code enters the Interpreter. Inside: Compiler → Byte code → Virtual machine. Library modules feed the Virtual machine. Result is running code.</p>
</div>
<h3>How code runs — Python vs C#</h3>
<div class="flow-compare">
  <div class="flow-card">
    <h4>Python path — interpreter runs <code>.py</code></h4>
    <div class="flow-steps">
      <div class="flow-step"><b>1. Source file</b><code>.py</code><span class="flow-code">score = 75
if score &gt;= 60:
    print("Pass")</span></div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-step"><b>2. Run command</b><span class="flow-code">python app.py</span>The Python interpreter starts and reads the <code>.py</code> file.</div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-step"><b>3. CPython compiles to bytecode</b><code>.pyc</code><span class="flow-code">1010110 0001001 1110001
LOAD_NAME score
COMPARE_OP &gt;=</span></div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-step"><b>4. Interpreter runs bytecode</b><br>CPython executes one bytecode instruction at a time.</div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-step"><b>5. Output</b><span class="flow-code">Pass</span></div>
    </div>
  </div>
  <div class="flow-card">
    <h4>C# path — JIT does not run <code>.cs</code> directly</h4>
    <div class="flow-steps">
      <div class="flow-step"><b>1. Source file</b><code>.cs</code><span class="flow-code">int score = 75;
if (score &gt;= 60)
{
    Console.WriteLine("Pass");
}</span></div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-step"><b>2. Build command</b><span class="flow-code">dotnet build
dotnet publish</span>The C# compiler must compile <code>.cs</code> first.</div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-step"><b>3. Compiler builds assembly</b><code>.dll</code> / <code>.exe</code><span class="flow-code">IL_0001: ldc.i4.s 75
IL_0003: bge.s PASS</span></div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-step"><b>4. .NET runtime runs it</b><br>CLR/JIT turns IL into native machine instructions while the app runs.</div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-step"><b>5. Output</b><span class="flow-code">Pass</span></div>
    </div>
  </div>
</div>
<h3>Production — what goes to the server?</h3>
<table class="data-tbl">
<tr><th>Question</th><th>Python</th><th>C# / .NET</th></tr>
<tr><td>Can the source file run directly?</td><td><span class="cell-yes"><span class="yn-yes"></span>Yes</span> — run <code>python app.py</code>. The interpreter reads <code>.py</code>.</td><td><span class="cell-no"><span class="yn-no"></span>No</span> — <code>.cs</code> must be compiled first.</td></tr>
<tr><td>Intermediate form</td><td><code>.pyc</code> bytecode in <code>__pycache__</code>. It is an internal cache, not the main production package.</td><td><code>.dll</code> / <code>.exe</code> assembly containing IL. This is normally part of the production publish output.</td></tr>
<tr><td>Runtime</td><td>Python interpreter / CPython virtual machine executes bytecode.</td><td>.NET runtime / CLR loads assembly; JIT compiles IL to native machine code.</td></tr>
<tr><td>Typical production artifact</td><td>Project folder or package with <code>.py</code> files + <code>requirements.txt</code>, a virtual environment, or a Docker image.</td><td>Published folder containing <code>MyApp.dll</code> plus dependencies, or a self-contained <code>.exe</code>.</td></tr>
<tr><td>Production command</td><td><code>python -m app</code>, <code>uvicorn app.main:app</code>, <code>gunicorn app:app</code>, or Docker runs one of these.</td><td><code>dotnet MyApp.dll</code>, Windows service, IIS, container, or self-contained <code>MyApp.exe</code>.</td></tr>
<tr><td>Python production deployment</td><td>Usually <code>.py</code> source files + dependencies, often inside Docker. It can also be a <code>.whl</code> package, AWS Lambda zip, zipapp <code>.pyz</code>, or bundled <code>.exe</code> from PyInstaller. Normal Python apps are <b>not</b> DLLs.</td><td>.NET production commonly publishes a <code>.dll</code> run by <code>dotnet</code>, or a self-contained <code>.exe</code>.</td></tr>
</table>
<p class="flow-note"><b>Interview line:</b> A Python <code>.py</code> file can be launched by the Python interpreter; CPython compiles it to bytecode and runs that bytecode. A C# <code>.cs</code> file is not run by JIT directly; it is compiled into a .NET assembly, then CLR/JIT runs the IL. In production, Python is usually deployed as source/package/container, not as a DLL.</p>
'''


def audio_src(n: int) -> str:
    return f"audio/slide-{n:02d}.mp3"


def audio_bar(n: int) -> str:
    src = audio_src(n)
    return f'''<div class="audio-player" id="player-{n}" data-slide="{n}">
  <audio id="audio-{n}" preload="metadata" src="{src}"></audio>
  <div class="audio-controls">
    <button type="button" class="btn-play" id="play-btn-{n}" onclick="togglePlay({n})" title="Play / Pause (resumes where you left off)">&#9654;</button>
    <button type="button" class="btn-reset" onclick="resetAudio({n})" title="Restart from beginning">&#8634;</button>
    <input type="range" class="audio-seek" id="seek-{n}" min="0" max="1000" value="0" step="1"
           aria-label="Seek narration"
           oninput="onSeekDrag({n}, this.value)"
           onchange="onSeekCommit({n}, this.value)">
    <span class="audio-time" id="time-{n}">0:00 / 0:00</span>
    <span class="audio-badge" title="Narration recorded at 0.75x speed">0.75x</span>
  </div>
</div>'''


def slide_hdr(n, title):
    meta = TRAINING_META.get(n, {})
    sub = meta.get("definition", "")[:100]
    if len(meta.get("definition", "")) > 100:
        sub += "…"
    return f'''<div class="slide-hdr">
  <div class="slide-meta">Slide {n} of {TOTAL_SLIDES} &middot; {module_for(n)}</div>
  <div class="slide-title">{title}</div>
  <div class="slide-sub">{sub}</div>
  {audio_bar(n)}
</div>'''


def topic_intro(n):
    meta = TRAINING_META.get(n, {})
    beginner = BEGINNER_CONTENT.get(n, {})
    if not meta and not beginner:
        return ""
    parts = []
    if meta.get("definition"):
        parts.append(f'<h3>Definition</h3><p>{meta["definition"]}</p>')
        # Diagram sits right under Definition, then glossary and real-life example
        if n == 1:
            parts.append(python_vs_csharp_flow())
        parts.append(diagram_for(n))
        parts.append(glossary_for(n))
        parts.append(real_life_for(n))
    else:
        parts.append(diagram_for(n))
        parts.append(glossary_for(n))
        parts.append(real_life_for(n))
    steps = beginner.get("steps", [])
    if steps:
        parts.append('<h3>Step-by-step (beginner friendly)</h3><ul class="learn-steps">')
        for s in steps:
            parts.append(f'<li><b>{s["title"]}</b><br>{s["body"]}</li>')
        parts.append("</ul>")
    kd = keyword_deepdives_for(n)
    if kd:
        parts.append(kd)
    return "".join(parts)


def interview_box(n):
    meta = TRAINING_META.get(n, {})
    beginner = BEGINNER_CONTENT.get(n, {})
    qa = beginner.get("interview_qa", [])
    if qa:
        parts = ['<div class="interview-box"><b>Interview — questions &amp; answers</b>']
        for item in qa:
            parts.append(f'<p class="qa-q"><b>Q:</b> {item["q"]}</p>')
            parts.append(f'<p class="qa-a"><b>A:</b> {item["a"]}</p>')
        parts.append("</div>")
        return "".join(parts)
    if meta.get("interview"):
        return (
            '<div class="interview-box"><b>How to explain in interview:</b>'
            f'<p>&ldquo;{meta["interview"]}&rdquo;</p></div>'
        )
    return ""


def project_refs(n: int) -> str:
    entries = SLIDE_PROJECT_FILES.get(n)
    if not entries:
        return ""
    parts = ['<p class="project-label"><b>Practice files (Projects/):</b></p>']
    for fname, _cmd in entries:
        parts.append(f'<a class="file-link" href="Projects/{fname}">{fname}</a>')
    run_cmd = next((cmd for _f, cmd in entries if cmd), None)
    if run_cmd:
        parts.append(f'<span class="run-cmd">{run_cmd}</span>')
    return "\n".join(parts)


def slide(n, title, learn, practice):
    notes_html, codes_html = split_learn(learn)
    notes_html = scenarios_for(n) + notes_html + interview_box(n)
    has_code = bool(codes_html.strip())
    split_cls = "main-split" if has_code else "main-split no-code"
    code_panel = f'<div class="panel-code">{codes_html}</div>' if has_code else ""
    divider = (
        '<div class="split-divider" role="separator" aria-orientation="vertical" '
        'aria-label="Resize panels"></div>'
        if has_code
        else ""
    )
    return f'''<div class="slide" id="slide-{n}">
{slide_hdr(n, title)}
<div class="slide-body">
  <div class="{split_cls}">
    <div class="panel-left">
      {topic_intro(n)}
      {notes_html}
      <div class="panel-practice">
        <h3>Practice</h3>
        {practice}
        {project_refs(n)}
      </div>
    </div>
    {divider}
    {code_panel}
  </div>
</div>
</div>'''


# ── Slide content: (num, title, learn_html, practice_html) ──────────────────

CONTENT = [
(1, "What is Python?", '''
<h3>Language characteristics</h3>
<table class="data-tbl">
<tr><th>Trait</th><th>What it means</th></tr>
<tr><td>High-level</td><td>Readable syntax — close to plain English, far from machine code</td></tr>
<tr><td>General-purpose</td><td>Web, data, automation, AI, scripting — one language, many domains</td></tr>
<tr><td>Interpreted</td><td>CPython runs your code via bytecode — no manual compile-and-link like C#</td></tr>
<tr><td>Dynamically typed</td><td>No <code>int x</code> declarations — types are checked at runtime</td></tr>
<tr><td>Indentation-based</td><td>Blocks defined by consistent spacing — <b>no curly braces</b></td></tr>
<tr><td>Multi-paradigm</td><td>Procedural, object-oriented, and functional styles in one language</td></tr>
<tr><td>Batteries included</td><td>Rich standard library: os, json, datetime, re, pathlib, etc.</td></tr>
</table>
<h3>Interpreted vs compiled — step by step</h3>
<ul>
<li><b>C# path:</b> <code>.cs</code> → compiler → IL (DLL) → JIT → native machine code → CPU runs it</li>
<li><b>Python path:</b> <code>.py</code> → CPython compiles to <b>bytecode</b> → interpreter VM executes bytecode → result</li>
<li>Python feels instant because you run <code>python file.py</code> without a separate build step — bytecode is cached automatically in <code>__pycache__/</code></li>
<li>Trade-off: generally slower than C#/C++ for CPU-heavy work; faster to write and test</li>
</ul>
''' + code('''# ── INTERPRETATION: how CPython runs this file ──
# Step 1: You save this as .py (source code - human readable)
# Step 2: CPython compiles it to bytecode (.pyc in __pycache__)
# Step 3: The interpreter executes bytecode line by line
# You only type:  python myfile.py

# ── INDENTATION: blocks use spaces, not { } ──
if score >= 60:
    print("Pass")       # 4 spaces = inside the if block
    print("Good job")
else:
    print("Try again")  # 4 spaces = inside the else block

# ── DYNAMIC TYPING: no type declaration ──
x = 42          # x holds an int
x = "hello"     # now x holds a str - same name, new type
print(type(x))  # <class 'str'>

# ── DUCK TYPING: another function uses object without knowing class name ──
# Class having .send() = normal. Duck typing = notify() only needs .send()
# Email / SMS / Slack all work — no shared base class / interface
class EmailNotifier:
    def send(self, msg):
        return f"Email sent: {msg}"

class SmsNotifier:
    def send(self, msg):
        return f"SMS sent: {msg}"

class SlackNotifier:
    def send(self, msg):
        return f"Slack: {msg}"

def notify(channel, msg):
    return channel.send(msg)   # no class name — behavior only

print(notify(EmailNotifier(), "Order #104 shipped"))
print(notify(SmsNotifier(), "OTP 4821"))
print(notify(SlackNotifier(), "Build done"))
# Same idea: anything with .write() can be passed to save(writer, text)''') + '''
<div class="callout"><b>Duck typing (memorize):</b> A class having a method is <b>normal</b>. Duck typing is when another function uses that object <b>without knowing the class name</b> — only the behavior (<code>.send()</code>). C# usually needs <code>interface INotifier</code>. Click <b>C# Comparison</b> on the Duck typing glossary row for the full table (interface vs <code>dynamic</code> vs extension methods).</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; <code>print</code> without parentheses (Python 2 habit)</span><span class="mistake-desc">In Python 3, <code>print</code> is a <b>function</b>. Omitting parentheses is a <code>SyntaxError</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">print "Hello"   # SyntaxError in Python 3</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">print("Hello")  # correct</div></div></div><span class="mistake-note">&#128161; <code>print</code> in Python 2 was a <b>statement</b>. Every Python 3 script must use <code>print()</code>.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; shadowing a built-in name</span><span class="mistake-desc">Naming a variable <code>list</code>, <code>str</code>, or <code>id</code> hides the built-in for the rest of the scope.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">list = [1, 2, 3]
result = list("abc")
# TypeError: int is not callable</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">my_list = [1, 2, 3]
result = list("abc")  # ["a","b","c"]</div></div></div><span class="mistake-note">&#128161; Use a prefix like <code>my_</code> or a descriptive name. Never reuse built-in names as variables.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; assuming Python is purely interpreted (no compilation step)</span><span class="mistake-desc">Python <em>does</em> compile to bytecode (<code>.pyc</code>). Calling it &ldquo;not compiled&rdquo; is imprecise.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Misconception: "Python skips compilation"
# Reality: CPython compiles .py -> bytecode
# then the VM executes bytecode
# .pyc files live in __pycache__/</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Correct mental model:
# source.py --> CPython compiler --> bytecode
#          --> CPython VM --> result
# Run: python file.py  (compile + execute)</div></div></div><span class="mistake-note">&#128161; Bytecode caching (<code>__pycache__/</code>) makes repeated runs faster. The compile step is implicit, not absent.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 4 &mdash; <code>x is 1000</code> vs <code>x == 1000</code></span><span class="mistake-desc"><code>is</code> checks <b>object identity</b> (same memory address), not value equality. Only small ints (-5 to 256) are interned.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">x = 1000
y = 1000
if x is y:
    print("same")  # may print or may not!
                   # CPython-specific behaviour</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">x = 1000
y = 1000
if x == y:
    print("equal")  # always correct</div></div></div><span class="mistake-note">&#128161; Use <code>==</code> for value comparison. Only use <code>is</code> for <code>None</code>, <code>True</code>, <code>False</code>, and identity checks.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Python 2 style</div><div class="step-pre">print "Starting"
xrange(10)         # Python 2 only
raw_input("Name: ")# Python 2 only
print "Done"</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Python 3 style</div><div class="step-pre">print("Starting")
range(10)          # lazy in Python 3
name = input("Name: ")
print("Done")</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> What does <code>type(42)</code> return?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>&lt;class 'int'&gt;</code> &mdash; every Python object has a type. <code>type()</code> returns the class of the object.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> Is Python compiled or interpreted?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Both &mdash; CPython compiles source to <b>bytecode</b> first, then the interpreter VM executes it. The compile step is hidden from the user.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Can you assign a string to a variable that previously held an int?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Yes &mdash; Python is <b>dynamically typed</b>. A variable name is just a label; the type lives on the object.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> What does <code>if __name__ == '__main__':</code> guard against?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">It prevents code from running when the file is <b>imported</b> as a module. Only runs when the file is executed directly.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> What is duck typing?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Using an object based on its <b>behaviour</b> (methods/attributes) rather than its explicit class. &ldquo;If it has a <code>.send()</code>, call it.&rdquo;</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>print</code> without parentheses — valid in Python 3?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No &mdash; <code>print</code> is a <b>function</b> in Python 3. <code>print 'hi'</code> is a <code>SyntaxError</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> Where does Python store compiled bytecode files?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">In <code>__pycache__/</code> as <code>.pyc</code> files. They are regenerated automatically when the source changes.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Explain interpretation vs compilation in your own words</li>
  <li>Find a <code>.pyc</code> file in <code>__pycache__/</code> after running a script</li>
  <li>Write an if/else block using indentation only</li>
  <li>Explain duck typing vs “class has a method” using the <code>notify</code> example</li>
</ul>
'''),

(2, "Setup &amp; Run Python on Windows", '''
<h3>Install Python on Windows</h3>
<table class="data-tbl">
<tr><th>Step</th><th>Action</th></tr>
<tr><td>1</td><td>Go to <b>python.org/downloads</b> — download Python 3.11 or 3.12</td></tr>
<tr><td>2</td><td>Run the installer — check <b>Add python.exe to PATH</b> at the bottom</td></tr>
<tr><td>3</td><td>Click <b>Install Now</b> (includes pip and IDLE)</td></tr>
<tr><td>4</td><td>Open PowerShell or Command Prompt and verify below</td></tr>
</table>
''' + code('''# ── VERIFY INSTALLATION ──
python --version     # Python 3.12.x  (interpreter version)
pip --version        # pip 24.x       (package manager)

# ── WINDOWS PY LAUNCHER (multiple Python versions) ──
py -0p               # list all installed Pythons
py -3.12 --version   # run specific version
py -3.12 script.py   # run script with Python 3.12''') + '''
<h3>IDE setup — VS Code / Cursor</h3>
<ul>
<li>Install the <b>Python extension</b> (Microsoft)</li>
<li>File → Open Folder → <code>D:\\Sangeetha\\Python</code></li>
<li>Ctrl+Shift+P → <b>Python: Select Interpreter</b> → pick 3.12</li>
<li>Open any <code>.py</code> file → click ▶ Run or press <b>F5</b> to debug</li>
</ul>
<h3>Three ways to run Python</h3>
''' + code('''# ── 1. REPL (Read-Eval-Print Loop) ──
# Type: python   then enter interactive mode
>>> 2 + 2
4
>>> name = "Python"
>>> print(f"Hello, {name}")
Hello, Python
>>> exit()          # or Ctrl+Z Enter on Windows

# ── 2. RUN A SCRIPT FILE ──
python Projects/00_windows_setup.py
python D:\\Sangeetha\\Python\\Projects\\02_getting_started.py

# ── 3. ONE-LINER (-c flag) ──
python -c "print('Hello from command line')"

# ── 4. ENTRY-POINT GUARD (like C# Main) ──
def main():
    print("Starting application...")
    print("Only runs when file executed directly")

if __name__ == "__main__":
    main()   # True when: python thisfile.py
             # False when: import thisfile''') + '''
<div class="tip"><b>PATH issue?</b> If <code>python</code> is not recognized, re-run the installer and enable PATH, or use the full path: <code>C:\\Users\\You\\AppData\\Local\\Programs\\Python\\Python312\\python.exe</code></div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; not ticking &ldquo;Add python.exe to PATH&rdquo; during install</span><span class="mistake-desc">Without PATH, <code>python</code> is not recognized in the terminal &mdash; the most common setup failure.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Open PowerShell:
python --version
# 'python' is not recognized as an internal
# or external command ...</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Fix: re-run installer, check "Add python.exe to PATH"
# or add manually:
# $env:PATH += ";C:\\Users\\You\\AppData\\Local\\Programs\\Python\\Python312"
python --version  # Python 3.12.x</div></div></div><span class="mistake-note">&#128161; Alternatively use the Windows <b>py launcher</b>: <code>py --version</code> works even without PATH if the launcher is installed.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; <code>pip install</code> globally instead of inside a venv</span><span class="mistake-desc">Global installs mix package versions across all projects and can break existing tools.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Bad: installs globally
pip install flask
pip install requests
# Now ALL projects share the same versions</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Good: isolate per project
python -m venv .venv
.venv\\Scripts\\activate
pip install flask
# only affects .venv/</div></div></div><span class="mistake-note">&#128161; Always activate a venv before <code>pip install</code>. Check prompt for <code>(.venv)</code> prefix.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; confusing <code>python</code> vs <code>py</code> on Windows</span><span class="mistake-desc">Windows ships a <b>py launcher</b> (<code>py.exe</code>) separate from <code>python.exe</code>. They are different entry points.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># py launcher: picks the version from #! line or -3 flag
py -3.12 script.py
# python: runs whichever python is first in PATH
python script.py</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Use py launcher when you have multiple Python versions:
py -0p          # list all installed Pythons
py -3.12 -m pip install flask
# Use python when inside an activated venv</div></div></div><span class="mistake-note">&#128161; <code>py -3.12</code> is safer on Windows when multiple Python versions are installed.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 4 &mdash; forgetting to regenerate HTML after editing <code>build_training.py</code></span><span class="mistake-desc">The HTML is <b>generated</b> from Python source. Edits to <code>build_training.py</code> are invisible until you regenerate.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Edit build_training.py
# Open PythonTraining.html in browser
# ← changes NOT visible yet!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Edit build_training.py, then:
python build_training.py
# Generated PythonTraining.html
# Now refresh the browser tab</div></div></div><span class="mistake-note">&#128161; Make regeneration a habit: edit → run → refresh. The file is 1 MB+ so a fresh build takes ~1 second.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; No venv (global)</div><div class="step-pre"># Every project shares the same packages:
pip install flask==2.0
pip install flask==3.0
# Second overwrites the first globally!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; With venv (isolated)</div><div class="step-pre">python -m venv .venv
.venv\\Scripts\\activate
pip install flask==3.0
pip freeze > requirements.txt
# Safe — scoped to this project only</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Command to verify Python is installed correctly?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>python --version</code> &mdash; should print <code>Python 3.12.x</code> (or your installed version).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What does <code>py -0p</code> do?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Lists all installed Python interpreters with their full paths (Windows py launcher).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Why should you avoid <code>pip install</code> without activating a venv first?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">It installs packages <b>globally</b>, risking version conflicts between projects.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> What file records all installed packages for reproducibility?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>requirements.txt</code> &mdash; generated with <code>pip freeze &gt; requirements.txt</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> How do you run the training slide regeneration?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>python build_training.py</code> from the workspace root.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> What does the <code>(.venv)</code> prefix in your terminal prompt indicate?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The virtual environment is <b>activated</b> &mdash; <code>pip install</code> goes into <code>.venv/</code>.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Install Python 3.12 — verify <code>python --version</code></li>
  <li>Open this folder in Cursor and select the Python interpreter</li>
  <li>Run <code>python Projects/00_windows_setup.py</code></li>
  <li>Try the REPL: type <code>python</code> then <code>2 + 2</code></li>
</ul>
<span class="run-cmd">python --version</span>
<span class="run-cmd">python Projects/00_windows_setup.py</span>
'''),

(3, "Your Training Workspace", '''
<h3>Folder layout</h3>
''' + tree(
    tree_row(0, "📁", "D:/Sangeetha/Python/", "t-folder", "training root") +
    tree_row(1, "📄", "PythonTraining.html", "t-file", "this slide deck") +
    tree_row(1, "📄", "build_training.py", "t-file", "regenerate HTML") +
    tree_row(1, "📁", "Projects/", "t-folder", "practice files per slide") +
    tree_row(1, "📁", "Python-Set2/", "t-folder", "real hands-on projects") +
    tree_row(2, "📁", "pythonBasics/", "t-folder", "topic modules") +
    tree_row(2, "📄", "hello.py", "t-file", ".py = Python source") +
    tree_row(2, "📄", "requirements.txt", "t-file", "pip package list") +
    tree_row(2, "📁", ".venv/", "t-folder", "virtual env — do not commit")
) + '''
<table class="data-tbl">
<tr><th>File / folder</th><th>Purpose</th></tr>
<tr><td><code>.py</code></td><td>Python source — one module per file</td></tr>
<tr><td><code>.ipynb</code></td><td>Jupyter notebook (see pandas/)</td></tr>
<tr><td><code>requirements.txt</code></td><td>Pip packages for the project</td></tr>
<tr><td><code>.venv/</code></td><td>Isolated environment per project</td></tr>
<tr><td><code>__init__.py</code></td><td>Makes a folder a Python package</td></tr>
</table>
<h3>Learning path</h3>
<ul>
<li><b>Week 1</b> — slides 1–11: Intro, setup, workspace, PEP, datatypes, typing, operators, flow, comprehensions, functions, builtins</li>
<li><b>Week 2</b> — slides 12–17: Collections, memory/GC, Pydantic, OOP, descriptors, generators</li>
<li><b>Week 3</b> — slides 18–27: Decorators, exceptions, threading/async/GIL, logging, tests, regex, files, context, venv</li>
<li><b>Week 4</b> — slide 28: FastAPI with SQLAlchemy</li>
<li><b>Projects</b> — slides 29–34: Python-Set2 portfolio</li>
<li><b>Appendix</b> — slide 35: C# vs Python</li>
</ul>
''' + code('''# ── TYPICAL WORKFLOW ──
# 1. Read slide in PythonTraining.html
# 2. Open matching file in Projects/
# 3. Run and experiment:
python Projects/02_getting_started.py

# 4. Later: practice in Python-Set2/pythonBasics/
cd Python-Set2/pythonBasics/MyClass
python oops_inheritance_BankAccount.py

# ── REGENERATE slides after edits ──
# python build_training.py''') + '''
<div class="callout"><b>C# developer tip:</b> <code>python file.py</code> ≈ <code>dotnet run</code> &middot; <code>pip install</code> ≈ <code>dotnet add package</code> &middot; <code>venv</code> ≈ per-project NuGet isolation</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; hand-editing <code>PythonTraining.html</code> directly</span><span class="mistake-desc">The HTML is <b>generated output</b>. Hand edits are overwritten the next time <code>python build_training.py</code> is run.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Open PythonTraining.html in editor
# Change some text in Slide 5...
# Run: python build_training.py
# ← your edits are GONE</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Always edit the SOURCE:
# build_training.py  (main content)
# slide_*.py         (component modules)
# Then: python build_training.py</div></div></div><span class="mistake-note">&#128161; Think of <code>PythonTraining.html</code> like a compiled binary &mdash; read it, but don&apos;t edit it.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; running scripts from the wrong directory</span><span class="mistake-desc">Python&apos;s relative imports and file paths are relative to the <b>current working directory</b>, not the script location.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># You are in C:\\Users\\You
python D:\\Learning\\Python\\Projects\\05_comprehensions.py
# FileNotFoundError: data.csv not found
# because cwd is C:\\Users\\You, not Projects/</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Change to the project root first:
cd D:\\Learning\\Python
python Projects\\05_comprehensions.py
# or use absolute paths inside scripts</div></div></div><span class="mistake-note">&#128161; Run scripts from the workspace root: <code>cd D:\\Learning\\Python</code>. VS Code&apos;s Run button sets cwd to the file&apos;s folder automatically.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; committing <code>.venv/</code> to git</span><span class="mistake-desc"><code>.venv/</code> can be hundreds of MB and is <b>platform-specific</b>. It should never be in version control.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># .gitignore is missing .venv
git add .
git commit -m "initial"
# Commits hundreds of MB of venv binaries!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># .gitignore should contain:
.venv/
__pycache__/
*.pyc
.env
# Teammates recreate venv with:
# pip install -r requirements.txt</div></div></div><span class="mistake-note">&#128161; Commit only <code>requirements.txt</code>, not the venv itself. Anyone can recreate it with <code>pip install -r requirements.txt</code>.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Edit output directly</div><div class="step-pre"># Dangerous workflow:
1. Open PythonTraining.html
2. Edit HTML manually
3. Refresh browser — looks OK
4. python build_training.py
5. ← all manual edits lost!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Edit source, regenerate</div><div class="step-pre"># Safe workflow:
1. Open build_training.py
2. Find the slide tuple
3. Edit left/right panel HTML
4. python build_training.py
5. Refresh browser — permanent!</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Which file generates <code>PythonTraining.html</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>build_training.py</code> &mdash; run it with <code>python build_training.py</code> after any content change.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> Where are practice files for each slide?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>Projects/</code> &mdash; one <code>.py</code> file per topic (e.g., <code>Projects/05_comprehensions.py</code>).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Should <code>.venv/</code> be committed to git?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No &mdash; add it to <code>.gitignore</code>. Teammates recreate the env from <code>requirements.txt</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> What makes a folder a Python package?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">An <code>__init__.py</code> file inside it (can be empty).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> Python source files use which extension?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>.py</code> for source, <code>.pyc</code> for compiled bytecode (auto-generated in <code>__pycache__/</code>).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> How do you install all dependencies listed in <code>requirements.txt</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>pip install -r requirements.txt</code> (after activating your venv).</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Open <code>D:\\Sangeetha\\Python</code> in VS Code / Cursor</li>
  <li>Browse <code>Projects/</code> — one file per topic</li>
  <li>Run <code>python Projects/02_getting_started.py</code></li>
  <li>Explore <code>Python-Set2/pythonBasics/</code></li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/">pythonBasics</a>
'''),

(4, "PEP Standards", '''
<p>PEPs (Python Enhancement Proposals) document language changes, style guides, and packaging standards. You do not memorize every PEP — know the ones interviewers and teams reference daily.</p>
<table class="ref-table">
<tr><th>PEP</th><th>Topic</th><th>Why it matters</th></tr>
<tr><td>PEP 8</td><td>Style Guide</td><td>4-space indent, snake_case, 79-char lines (soft), imports order</td></tr>
<tr><td>PEP 257</td><td>Docstring Conventions</td><td>Triple-quoted module/class/function docs</td></tr>
<tr><td>PEP 484 / 585</td><td>Type Hints</td><td><code>list[int]</code> instead of <code>List[int]</code> (3.9+)</td></tr>
<tr><td>PEP 20</td><td>Zen of Python</td><td><code>import this</code> — readability counts</td></tr>
<tr><td>PEP 440</td><td>Version Identifiers</td><td><code>1.2.3</code>, pre-release tags in pip</td></tr>
<tr><td>PEP 508</td><td>Dependency Specifiers</td><td><code>package&gt;=1.0,&lt;2</code> in requirements</td></tr>
<tr><td>PEP 517 / 518</td><td>Build System</td><td><code>pyproject.toml</code> for modern packaging</td></tr>
</table>
''' + code('''# ── PEP 8 style (examples) ──
import os
from pathlib import Path

MAX_RETRIES = 3          # constants: UPPER_SNAKE

def load_config(path: str) -> dict:
    """Load JSON config from path (PEP 257 docstring)."""
    ...

class OrderService:      # classes: PascalCase
    def process(self, order_id: int) -> None:
        user_name = "anu"  # variables: snake_case

# ── Zen of Python ──
import this   # PEP 20 — run in REPL once

# ── pyproject.toml (PEP 518 / 621) ──
# [project]
# name = "my-api"
# version = "0.1.0"
# dependencies = ["fastapi>=0.100"]''') + '''
<div class="callout"><b>Interview tip:</b> PEP 8 is convention, not syntax — linters (<code>ruff</code>, <code>flake8</code>) enforce it in CI. Black auto-formats; teams still expect readable names and docstrings.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; <code>camelCase</code> variable names (C#/Java habit)</span><span class="mistake-desc">PEP 8 specifies <b>snake_case</b> for variables and functions. <code>camelCase</code> is reserved for nothing in Python (only PascalCase for classes).</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">firstName = "Anu"
def getUserName():
    maxRetries = 3</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">first_name = "Anu"
def get_user_name():
    max_retries = 3</div></div></div><span class="mistake-note">&#128161; Linters like <code>ruff</code> or <code>pylint</code> flag <code>camelCase</code> variable names as PEP 8 violations (N806).</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; using tabs for indentation</span><span class="mistake-desc">Python allows tabs OR spaces but mixing them causes <code>TabError</code>. PEP 8 mandates <b>4 spaces</b>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def greet():
	print("hello")  # tab
    print("world") # 4 spaces mixed
# TabError: inconsistent use of tabs</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def greet():
    print("hello")  # 4 spaces
    print("world") # 4 spaces
# Clean — no mixing</div></div></div><span class="mistake-note">&#128161; Set your editor to &ldquo;Insert spaces&rdquo; with tab size 4. VS Code / Cursor do this by default for <code>.py</code> files.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; wrong import order</span><span class="mistake-desc">PEP 8 requires three import groups (stdlib → third-party → local) separated by blank lines.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">import os
import flask           # third-party before stdlib
from myapp import db  # local mixed in</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import os              # 1. stdlib
import sys

import flask           # 2. third-party
import requests

from myapp import db  # 3. local</div></div></div><span class="mistake-note">&#128161; <code>isort</code> and <code>ruff --select I</code> auto-sort imports. Most CI pipelines enforce this.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Non-PEP 8 code</div><div class="step-pre">def calcTax(priceVal,taxRate):
    TaxAmount=priceVal*taxRate
    return(TaxAmount)</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; PEP 8 compliant</div><div class="step-pre">def calculate_tax(price: float, tax_rate: float) -> float:
    """Return price * tax_rate."""
    tax_amount = price * tax_rate
    return tax_amount</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> PEP 8 recommended indentation size?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">4 spaces (never tabs, never 2 spaces for Python).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> PEP 8 naming convention for variables and functions?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>snake_case</code> — all lowercase with underscores.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> PEP 8 naming convention for classes?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>PascalCase</code> (also called UpperCamelCase) — e.g., <code>OrderService</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> PEP 8 naming convention for constants?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>UPPER_SNAKE_CASE</code> — e.g., <code>MAX_RETRIES = 3</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> What does <code>import this</code> show?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The <b>Zen of Python</b> (PEP 20) — 19 guiding principles like &ldquo;Readability counts&rdquo;.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> Soft maximum line length per PEP 8?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">79 characters (some teams use 88 or 120 but 79 is the PEP 8 standard).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> Which tool auto-formats Python code to PEP 8?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>black</code> (opinionated formatter), <code>ruff format</code>, or <code>autopep8</code>.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Run <code>import this</code> in REPL and name 3 Zen lines</li>
  <li>Refactor one script to PEP 8 naming (snake_case, 4 spaces)</li>
  <li>Add a one-line docstring to every function in a practice file</li>
</ul>
'''),

(5, "Python Datatypes", '''
<table class="data-tbl">
<tr><th>Type</th><th>Real project use</th><th>Example</th></tr>
<tr><td>list</td><td>Cart items, API rows, log lines — grows over time</td><td><code>cart.append(item)</code></td></tr>
<tr><td>tuple</td><td>GPS, RGB, DB row key, <code>return ok, data</code></td><td><code>(12.97, 80.22)</code></td></tr>
<tr><td>dict</td><td>JSON body, config, username → profile</td><td><code>user["email"]</code></td></tr>
<tr><td>set</td><td>Unique tags, ids already processed</td><td><code>seen.add(order_id)</code></td></tr>
</table>
''' + code('''import sys

# ── STEP 1: Primitives ──
age = 25              # int
price = 99.5          # float
name = "Ravi"         # str
is_active = True      # bool

# ── STEP 1b: int / str memory — Python has NO fixed 4-byte int ──
# C# int = fixed 4 bytes. Python int is a whole OBJECT (~28 bytes)
# and grows for huge values. Strings = base overhead + ~1 byte/char (ASCII).
print(sys.getsizeof(12345))      # ~28  (whole int object)
print(sys.getsizeof(10**100))    # larger — int grows with digits
print(sys.getsizeof(""))         # ~41-49 (empty str base)
print(sys.getsizeof("A"))        # ~42  (+1 byte per ASCII char)
print(sys.getsizeof("P12345"))   # ~47  (base + 6 chars)

# ── STEP 2: List — homogeneous OR heterogeneous ──
scores = [90, 85, 88]                    # list of int
vendors = ["Google", "Amazon", "Azure"]  # list of str
# Heterogeneous = mixed types in one list (valid in Python):
order = [101, "SHIPPED", ["Google", "Amazon"]]
#          int   str        list of str
print(order[0], order[1], order[2][0])   # 101 SHIPPED Google

# ── STEP 3: List memory — over-allocation on append ──
# CPython does NOT grow by +1 each time (that would be slow).
# It allocates extra capacity; when full, reallocates a bigger array
# and copies pointers (~1.125x growth).
cart = []
print("empty list bytes:", sys.getsizeof(cart))
for i in range(8):
    cart.append(i)
    print(f"len={len(cart)}  sizeof={sys.getsizeof(cart)}")
# sizeof jumps in steps — capacity > len until next realloc

# ── STEP 4: Tuple — real scenarios ──
lat_lng = (12.9716, 80.2212)     # GPS — fixed 2 numbers
rgb = (255, 128, 0)              # color channels
employee = ("E102", "Anu", 75000)  # id, name, salary record

def fetch_user(user_id):
    if user_id < 0:
        return False, None       # (ok, data) pattern
    return True, {"id": user_id, "name": "Anu"}

ok, user = fetch_user(10)        # unpack return tuple
cache_key = ("orders", 2026, 7)  # tuple as dict key
grid = {cache_key: 42}

# ── STEP 5: Why tuple is often faster / smaller than list ──
# - Fixed length → no resize / capacity bookkeeping
# - Slightly less memory (no over-allocation buffer)
# - Immutable → safe as dict key; CPython can optimize more
a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
print("list bytes :", sys.getsizeof(a_list))
print("tuple bytes:", sys.getsizeof(a_tuple))  # usually smaller

# ── STEP 6: Set / frozenset / dict ──
tags = {"python", "api", "python"}   # unique → {'python','api'}
perms = frozenset({"read", "write"}) # immutable set → OK as dict key
phone = {"Ravi": "99999", "Priya": "88888"}

# ── WHY dict keys must be IMMUTABLE (hashable) ──
# Dict finds a value using hash(key) → like a locker number.
# If the key could change later, the locker number would change
# and Python could NOT find the value again (data lost / wrong bucket).

# OK — immutable keys (hash never changes):
prices = {}
prices["apple"] = 40          # str
prices[101] = "SKU"           # int
prices[(12.97, 80.22)] = "Chennai warehouse"   # tuple GPS

# FAIL — mutable keys (Python blocks this):
# prices[[12.97, 80.22]] = "warehouse"   # TypeError: unhashable type: 'list'
# prices[{"city": "Chennai"}] = "x"      # TypeError: unhashable type: 'dict'
# prices[{"a", "b"}] = "x"               # TypeError: unhashable type: 'set'

# Imaginary danger if list WERE allowed as a key:
# key = [1, 2]
# data[key] = "secret"
# key.append(3)          # key changed → hash would change
# data[[1, 2]]           # could not find "secret" anymore!
# That is why only immutable types are allowed as keys.
''') + '''
<div class="callout"><b>Why immutable keys only?</b> A dict uses <code>hash(key)</code> to place and find the value quickly (like a locker number). Mutable objects (<code>list</code>, <code>dict</code>, <code>set</code>) can change after you store them — then the hash would no longer match and the value would be lost or unreachable. Immutable keys (<code>str</code>, <code>int</code>, <code>tuple</code>, <code>frozenset</code>) never change, so the locker number stays valid.</div>
<div class="callout"><b>List memory rule:</b> Creating <code>[]</code> reserves a small buffer. Each <code>append</code> fills slots; when capacity is full, Python allocates a <b>larger</b> array and copies references — that is why <code>sys.getsizeof</code> jumps, not +1 every time.</div>
<div class="callout"><b>int / str sizes (vs C#):</b> C# <code>int</code> is a fixed <b>4 bytes</b>; a Python <code>int</code> is a whole object — ~<b>28 bytes</b> for <code>12345</code>, growing for huge values like <code>10**100</code> (built-in BigInteger). A Python <code>str</code> is ~<b>41–49 bytes</b> empty + ~1 byte per ASCII char (<code>"P12345"</code> ≈ 47); C# strings use UTF-16 (~2 bytes/char). So <code>"P12345"</code> costs more than <code>12345</code> mainly because it stores characters.</div>
<h3>List vs Java ArrayList — patient queue</h3>
<p>A Python <b>list</b> is a <b>dynamic array</b> of references — same idea as Java <code>ArrayList</code>. Contiguous slots → fast index access.</p>
<table class="data-tbl">
<tr><th>Operation</th><th>Python List</th><th>Java ArrayList</th></tr>
<tr><td>Access by index</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>Insert at end (<code>append</code>)</td><td>O(1) amortized</td><td>O(1) amortized</td></tr>
<tr><td>Insert at beginning</td><td>O(n)</td><td>O(n)</td></tr>
</table>
<table class="data-tbl">
<tr><th>Hospital queue action</th><th>Code</th><th>What happens</th><th>Cost</th></tr>
<tr><td>Add at <b>end</b></td><td><code>patients.append(new_patient)</code></td><td>Fill next free slot — no shifting</td><td>O(1) amortized</td></tr>
<tr><td>Add at <b>beginning</b></td><td><code>patients.insert(0, new_patient)</code></td><td>Shift every existing record right</td><td>O(n) — slow for 10,000 patients</td></tr>
</table>
<table class="data-tbl">
<tr><th>When to use</th><th>Prefer</th></tr>
<tr><td>Adding records to the end of a queue</td><td><code>list.append(...)</code> — fast</td></tr>
<tr><td>Large FIFO triage (add end / take front)</td><td><code>collections.deque</code> — avoid <code>insert(0)</code> / <code>pop(0)</code></td></tr>
<tr><td>Comparing to Java</td><td>Python list ≈ <code>ArrayList</code> (same cost profile)</td></tr>
</table>
<p>Yes — Python has a deque (<b>double-ended queue</b>) in the <code>collections</code> module. It is <b>not</b> a built-in like <code>list</code>, but it is in the standard library.</p>
<div class="step-pre">from collections import deque

triage = deque()
triage.append("Patient A")   # add at the end — fast
triage.append("Patient B")
next_up = triage.popleft()   # take from the front — also fast</div>
<table class="data-tbl">
<tr><th></th><th><code>list</code></th><th><code>deque</code></th></tr>
<tr><td>Add/remove at <b>end</b></td><td>Fast</td><td>Fast</td></tr>
<tr><td>Add/remove at <b>front</b></td><td>Slow (<code>insert(0)</code> / <code>pop(0)</code>)</td><td>Fast (<code>appendleft</code> / <code>popleft</code>)</td></tr>
<tr><td>Best for</td><td>General lists, random index access</td><td>Queues (first-in, first-out)</td></tr>
</table>
<div class="tip"><b>Conclusion:</b> Use <code>append()</code> for end-of-queue adds. Avoid inserting at the beginning of a large list. For a real waiting-room queue, use <code>collections.deque</code> — fast at both ends, like two doors on a line.</div>
<div class="tip"><b>Tuple vs list:</b> Use <b>tuple</b> for fixed records (GPS, return pairs, cache keys). Use <b>list</b> when size changes (cart, rows, logs). Tuple is typically leaner/faster for fixed data because it never resizes.</div>
<div class="callout"><b>One-item tuple:</b> the <b>comma</b> makes the tuple, not the parentheses.
An API that walks a sequence of readings fails on a scalar float and succeeds on <code>(98.6,)</code>.
Type hints like <code>readings: tuple</code> do <b>not</b> change run-time output — same crash / same result.
<div class="step-pre"># 1) No type hints
def average_temps(readings):
    return sum(readings) / len(readings)

# 2) With type hints — SAME run-time behavior
def average_temps(readings: tuple) -> float:
    return sum(readings) / len(readings)

average_temps(98.6)      # FAIL  → TypeError (even with hints!)
average_temps((98.6,))   # SUCCEED → 98.6
average_temps((98.6, 99.1))  # SUCCEED → 98.85

print(type((98.6)))      # float
print(type((98.6,)))     # tuple</div>
<table class="data-tbl">
<tr><th></th><th>No hints</th><th>With <code>: tuple</code></th></tr>
<tr><td>Run-time output</td><td>Same</td><td>Same</td></tr>
<tr><td>Extra value</td><td>—</td><td>mypy/pyright can warn early</td></tr>
</table>
<b>Example — average one patient's temperature readings:</b>
<div class="step-pre"># INPUT
patient_temps = (98.6, 99.1, 98.9)
result = round(average_temps(patient_temps), 2)
print(result)

# OUTPUT
98.87</div>
</div>
<div class="callout"><b>dict get vs []:</b>
<table class="data-tbl">
<tr><th></th><th><code>d[key]</code></th><th><code>d.get(key)</code></th></tr>
<tr><td>Missing key</td><td><b>KeyError</b></td><td><b>None</b> / default</td></tr>
<tr><td>Use for</td><td>Required fields</td><td>Optional fields</td></tr>
</table>
<div class="step-pre">patient = {"blood_type": "A+"}
print(patient["blood_type"])           # required
print(patient.get("nickname", "N/A"))  # optional</div>
</div>
<div class="callout"><b>Decimal for money:</b> <code>float</code> can be slightly wrong; <code>Decimal</code> is for exact cents.
<div class="step-pre">from decimal import Decimal
print(0.1 + 0.2)
print(Decimal("0.1") + Decimal("0.2"))</div>
</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; aliasing a list instead of copying</span><span class="mistake-desc">Assigning a list to another variable creates an <b>alias</b>, not a copy. Both names point to the same object.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">a = [1, 2, 3]
b = a          # alias — same object
b.append(4)
print(a)       # [1, 2, 3, 4]  ← surprise!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">a = [1, 2, 3]
b = a.copy()   # shallow copy
# or: b = a[:]
# or: b = list(a)
b.append(4)
print(a)       # [1, 2, 3]  ← unchanged</div></div></div><span class="mistake-note">&#128161; Mutable types (<code>list</code>, <code>dict</code>, <code>set</code>) are passed and assigned <b>by reference</b>. Use <code>.copy()</code> or <code>copy.deepcopy()</code> for nested structures.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; using <code>is</code> instead of <code>==</code> for value comparison</span><span class="mistake-desc"><code>is</code> checks <b>identity</b> (same memory address). Only small integers (-5 to 256) and interned strings are guaranteed to be the same object.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">x = 1000
y = 1000
if x is y:
    print("equal")  # may fail outside CPython</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">x = 1000
y = 1000
if x == y:
    print("equal")  # always correct</div></div></div><span class="mistake-note">&#128161; Use <code>is</code> only for <code>None</code>, <code>True</code>, <code>False</code>: <code>if x is None</code>. For everything else use <code>==</code>.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; modifying a list while iterating it</span><span class="mistake-desc">Removing items from a list during a <code>for</code> loop skips elements because indices shift.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">nums = [1, 2, 3, 4, 5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)  # [1, 3, 5] — but misses some!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Build a new list instead:
nums = [1, 2, 3, 4, 5]
nums = [n for n in nums if n % 2 != 0]
print(nums)  # [1, 3, 5]  ← correct</div></div></div><span class="mistake-note">&#128161; Never modify a collection while iterating it. Use a list comprehension, <code>filter()</code>, or iterate a copy.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Mutable alias trap</div><div class="step-pre">cart_a = ["apple", "bread"]
cart_b = cart_a       # alias!
cart_b.append("milk")
print(cart_a)
# ["apple", "bread", "milk"]  surprise!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Safe copy</div><div class="step-pre">cart_a = ["apple", "bread"]
cart_b = cart_a.copy() # independent
cart_b.append("milk")
print(cart_a)
# ["apple", "bread"]  unchanged</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>a = [1,2]; b = a; b.append(3)</code> — what is <code>a</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>[1, 2, 3]</code> &mdash; <code>b = a</code> creates an <b>alias</b>. Both names point to the same list object.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> Which type is immutable: <code>list</code> or <code>tuple</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>tuple</code> &mdash; once created its elements cannot be changed. <code>list</code> is mutable.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>{1, 2, 2, 3}</code> — how many elements?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">3 &mdash; <code>set</code> stores only <b>unique</b> values. The duplicate <code>2</code> is removed.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>type(True)</code> — what is returned?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>&lt;class 'bool'&gt;</code> &mdash; but <code>bool</code> is a subclass of <code>int</code>, so <code>isinstance(True, int)</code> is <code>True</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>d = {'a':1}; d.keys()</code> — is the result a list?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No &mdash; it's a <b>dict_keys view</b>. Use <code>list(d.keys())</code> to convert. Views reflect changes to the dict.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>'hello'[1]</code> — what value?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>'e'</code> &mdash; strings are zero-indexed sequences of characters.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> What does <code>a = [1,2,3]; a[::−1]</code> return?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>[3, 2, 1]</code> &mdash; slice with step <code>-1</code> reverses the sequence without modifying the original.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q8.</b> <code>x = (1,); type(x)</code> — what is the type?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>tuple</code> &mdash; a trailing comma is required to create a single-element tuple. <code>(1)</code> is just an int.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Build a heterogeneous list like <code>[101, "SHIPPED", ["Google", "Amazon"]]</code></li>
  <li>Print <code>sys.getsizeof</code> while appending 0..20 — watch size jump</li>
  <li>Compare <code>sys.getsizeof([1,2,3])</code> vs <code>(1,2,3)</code></li>
  <li>Return <code>(ok, data)</code> from a function and unpack it</li>
  <li>Use a tuple as a dict key; try a list key and catch TypeError</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyCollections/">MyCollections</a>
<a class="file-link" href="Python-Set2/pythonBasics/MyClass/mytypes.py">mytypes.py</a>
'''),

(6, "Typing", '''
''' + code('''from typing import Optional, Union, List, Dict, Tuple

# ── BASIC TYPE HINTS ──
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

# ── Optional: value OR None ──
def find_user(user_id: int) -> Optional[dict]:
    if user_id < 0:
        return None
    return {"id": user_id, "name": "Alice"}

# ── Union: one of several types ──
def process(items: Union[List[int], List[str]]) -> int:
    return len(items)

# ── COLLECTION HINTS ──
def get_scores() -> Dict[str, int]:
    return {"alice": 95, "bob": 88}

def get_point() -> Tuple[int, int]:
    return (10, 20)

# ── VARIABLE ANNOTATIONS ──
count: int = 0
names: List[str] = []

# Type hints are NOT enforced at runtime!
greet(42)        # runs fine - mypy would warn

# Static check:  mypy mymodule.py''') + '''
<div class="tip">Type hints are optional at runtime but help IDEs, documentation, and tools like mypy and FastAPI validation.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; using <code>from typing import List, Dict</code> in Python 3.9+</span><span class="mistake-desc">Since Python 3.9, built-in types (<code>list</code>, <code>dict</code>, <code>tuple</code>) are directly generic. No import needed.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Python 3.9+ — unnecessary import:
from typing import List, Dict, Tuple
def get(items: List[str]) -> Dict[str, int]:</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Python 3.9+ — direct generics:
def get(items: list[str]) -> dict[str, int]:
    ...
# No import needed for list/dict/tuple</div></div></div><span class="mistake-note">&#128161; Still use <code>from typing import</code> for <code>Optional</code>, <code>Union</code>, <code>TypeVar</code>, <code>Callable</code>, <code>Any</code>.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; <code>Optional[str]</code> vs <code>str | None</code> confusion</span><span class="mistake-desc"><code>Optional[X]</code> is exactly <code>Union[X, None]</code>. Python 3.10+ supports the cleaner <code>X | None</code> syntax.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Verbose (still valid, but old-style):
from typing import Optional
def find(id: int) -> Optional[str]:
    ...</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Modern (Python 3.10+):
def find(id: int) -> str | None:
    ...
# Python 3.9 compatible:
from typing import Optional  # still OK</div></div></div><span class="mistake-note">&#128161; Both forms are correct. Prefer <code>str | None</code> in new code targeting Python 3.10+. FastAPI and Pydantic accept both.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; type hints are not enforced at runtime</span><span class="mistake-desc">Python does <b>not</b> raise errors when you pass the wrong type at runtime &mdash; hints are for tools only.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def add(a: int, b: int) -> int:
    return a + b

result = add("hello", " world")
print(result)  # "hello world"  no error!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Use mypy, pyright, or Pydantic for runtime checks:
from pydantic import validate_call

@validate_call
def add(a: int, b: int) -> int:
    return a + b
add("x", 1)  # ValidationError!</div></div></div><span class="mistake-note">&#128161; Type hints are static hints, not runtime guards. Use <code>isinstance()</code>, Pydantic, or <code>@validate_call</code> if you need runtime type enforcement.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; No type hints</div><div class="step-pre">def process(data, threshold, callback):
    results = []
    for item in data:
        if item > threshold:
            results.append(callback(item))
    return results</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; With type hints</div><div class="step-pre">from collections.abc import Callable

def process(
    data: list[float],
    threshold: float,
    callback: Callable[[float], str],
) -> list[str]:
    return [callback(x) for x in data if x > threshold]</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>def f(x: int) -> str:</code> — does Python enforce this at runtime?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No &mdash; type hints are checked by tools like <code>mypy</code> and <code>pyright</code>, not by the Python runtime itself.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> How to annotate a parameter that can be <code>int</code> or <code>None</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>int | None</code> (Python 3.10+) or <code>Optional[int]</code> from <code>typing</code>. Both mean the same thing.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>list[int]</code> vs <code>List[int]</code> — which needs an import?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>List[int]</code> requires <code>from typing import List</code>. <code>list[int]</code> is built-in (Python 3.9+), no import.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> What does <code>Any</code> type hint mean?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Opts out of type checking for that variable &mdash; use sparingly as it defeats the purpose of typing.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>TypeVar</code> is used for?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Defining <b>generic</b> functions and classes that can work with any consistent type.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>from __future__ import annotations</code> does what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Makes all annotations lazy (strings) at runtime &mdash; allows forward references and improves performance in Python 3.7-3.9.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Add type hints to an existing function</li>
  <li>Install and run mypy on one file</li>
  <li>Use Optional for a nullable return</li>
</ul>
'''),

(7, "Operators", '''
<h3>Operator types overview</h3>
<table class="data-tbl">
<tr><th>Type</th><th>Examples</th></tr>
<tr><td>Arithmetic</td><td>+ - * / // % **</td></tr>
<tr><td>Comparison</td><td>== != &lt; &gt; &lt;= &gt;=</td></tr>
<tr><td>Logical</td><td>and or not</td></tr>
<tr><td>Identity</td><td>is / is not</td></tr>
<tr><td>Membership</td><td>in / not in</td></tr>
<tr><td>Assignment</td><td>= += -= *= /= //= %= **= &amp;= |= ^= &lt;&lt;= &gt;&gt;=</td></tr>
<tr><td>Bitwise</td><td>&amp; | ^ ~ &lt;&lt; &gt;&gt;</td></tr>
<tr><td>Walrus</td><td>:= (assign inside expression)</td></tr>
</table>
''' + code('''# ── ARITHMETIC ──
17 / 5    # 3.4   true division (always float in Python 3)
17 // 5   # 3     floor division (rounds down)
17 % 5    # 2     modulo (remainder)
2 ** 8    # 256   exponent (power)

# ── COMPARISON (returns True/False) ──
10 == 10  # True
10 != 5   # True
5 > 3     # True
5 <= 5    # True

# ── LOGICAL ──
True and False   # False
True or False    # True
not True         # False

# ── IDENTITY: is vs == ──
a = [1, 2]
b = a            # same object in memory
c = [1, 2]       # different object, same value
a is b           # True  - same object
a == c           # True  - equal values
a is c           # False - different objects
x = None
x is None        # True  - ALWAYS use is for None

# ── MEMBERSHIP ──
5 in [1, 2, 5]       # True
"py" in "Python"     # True
"Java" not in "Python"  # True

# ── BITWISE (on binary representation) ──
5 & 3    # 1   AND:  101 & 011 = 001
5 | 3    # 7   OR:   101 | 011 = 111
5 ^ 3    # 6   XOR:  101 ^ 011 = 110
~5       # -6  NOT (invert bits)
8 << 1   # 16  left shift (multiply by 2)
8 >> 1   # 4   right shift (divide by 2)

# ── ASSIGNMENT OPERATORS ──
n = 10
n += 5     # 15  (same as n = n + 5)
n -= 3     # 12
n *= 2     # 24
n //= 4    # 6
n **= 2    # 36

# ── WALRUS OPERATOR := (Python 3.8+) ──
# assign AND use value in same expression
data = ["a", "bb", "ccc"]
if (n := len(data)) > 2:
    print(f"Got {n} items")

while (line := input("Name (empty to quit): ")) != "":
    print(f"Hello, {line}")''') + '''
<div class="challenge"><b>Interview trap:</b> <code>is</code> checks identity (same object in memory). Use <code>==</code> for value comparison. Use <code>is None</code>, never <code>== None</code>.</div>
<table class="data-tbl">
<tr><th></th><th><code>==</code></th><th><code>is</code></th></tr>
<tr><td>Means</td><td>Equal <b>values</b></td><td>Same <b>object</b> in memory</td></tr>
<tr><td>Use for</td><td>IDs, names, numbers, strings</td><td><code>None</code> (and rare singletons)</td></tr>
</table>
<div class="step-pre">a = [1, 2]; b = [1, 2]; c = a
print(a == b)  # True
print(a is b)  # False
print(a is c)  # True</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; integer division confusion: <code>/</code> vs <code>//</code></span><span class="mistake-desc">In Python 3, <code>/</code> is always <b>true division</b> (returns float). Use <code>//</code> for integer (floor) division.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Python 3 — surprising for C# developers:
result = 7 / 2
print(result)   # 2.5  not 3 !
print(type(result))  # float</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">result = 7 // 2   # floor division
print(result)    # 3
result = 7 / 2    # true division
print(result)    # 2.5</div></div></div><span class="mistake-note">&#128161; In Python 2, <code>7 / 2</code> returned <code>3</code> (integer division). Python 3 changed this. Use <code>//</code> explicitly for integer results.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; <code>-2 ** 2</code> gives <code>-4</code>, not <code>4</code></span><span class="mistake-desc">The unary minus has <b>lower precedence</b> than <code>**</code>. So <code>-2**2</code> is parsed as <code>-(2**2)</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">result = -2 ** 2
print(result)   # -4  not 4 !</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">result = (-2) ** 2
print(result)   # 4  as expected</div></div></div><span class="mistake-note">&#128161; When negating a base before exponentiation, always wrap in parentheses: <code>(-n) ** exp</code>.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; <code>and</code>/<code>or</code> return operands, not booleans</span><span class="mistake-desc"><code>and</code> and <code>or</code> return one of their <b>operands</b>, not <code>True</code>/<code>False</code>. This enables idioms but can surprise.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">x = "" or "default"
print(x)  # "default"  — might be intentional

y = 0 and some_call()  # some_call() is NOT called
print(y)  # 0</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Explicit intent is clearer:
raw = ""
value = raw if raw else "default"
# or for optional-style:
result = raw or "default"  # OK but document it</div></div></div><span class="mistake-note">&#128161; <code>x = a or b</code> is Pythonic for defaults, but be aware that <em>any</em> falsy <code>a</code> (0, [], {}, &ldquo;&rdquo;) triggers the fallback.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Operator confusion</div><div class="step-pre">total = 100
tax = 18
# Mistake: integer division result
tax_amount = total / 100 * tax
print(tax_amount)  # 18.0 (float)

# Mistake: unary minus and power
val = -3 ** 2
print(val)  # -9 not 9</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Correct operators</div><div class="step-pre">total = 100
tax = 18
tax_amount = total * tax / 100  # 18.0 ✔

# Correct: parenthesise the base
val = (-3) ** 2
print(val)  # 9 ✔

# Floor division when int result needed:
quotient = total // tax  # 5</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>7 // 2</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>3</code> &mdash; floor division truncates toward negative infinity.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>7 % 3</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>1</code> &mdash; modulo: remainder after dividing 7 by 3.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>2 ** 10</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>1024</code> &mdash; <code>**</code> is the exponentiation operator.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>-2 ** 2</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>-4</code> &mdash; parsed as <code>-(2**2)</code> because <code>**</code> binds tighter than unary minus.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>"a" and "b"</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>'b'</code> &mdash; <code>and</code> returns the first falsy value, or the last value if all are truthy.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>5 / 2</code> in Python 3 &mdash; result and type?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>2.5</code>, type <code>float</code> &mdash; Python 3 always performs true division with <code>/</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>not True or False</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>False</code> &mdash; <code>not</code> has highest precedence: <code>(not True) or False</code> = <code>False or False</code> = <code>False</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q8.</b> <code>10 == 10.0</code> &mdash; True or False?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>True</code> &mdash; <code>==</code> compares values across numeric types. <code>10 is 10.0</code> would be <code>False</code>.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Predict results before running each operator</li>
  <li>Compare is vs == with two equal lists</li>
  <li>Try bitwise ops on small integers</li>
</ul>
'''),

(8, "Conditional &amp; Flow Control", '''
''' + code('''# ── IF / ELIF / ELSE ──
score = 75
if score >= 90:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"
print(grade)  # B

# ── FOR LOOP (like C# foreach) ──
for i in range(3):          # 0, 1, 2
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for idx, val in enumerate(["a", "b", "c"]):
    print(idx, val)         # 0 a, 1 b, 2 c

# ── WHILE LOOP ──
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue            # skip print for 3
    print(n)                # 1, 2, 4, 5

# ── BREAK: exit loop early ──
for x in range(10):
    if x == 5:
        break
    print(x)                # 0,1,2,3,4

# ── PASS & if True / if False ──
def save_report():
    pass                    # stub — block empty for now; add code later

class ValidationError(Exception):
    pass                    # empty exception class

if False:
    print("skipped")        # never runs — disable without deleting

if True:
    pass                    # placeholder — replace with real code

# ── FOR-ELSE: else runs if NO break ──
target = 5
for x in [1, 2, 3]:
    if x == target:
        print("found")
        break
else:
    print("not found")      # prints - no break happened''') + '''
<div class="callout"><b>pass</b> = this block is intentionally empty for now. Use it as a <b>stub</b> — later remove <code>pass</code> and add your real code. <b>if False</b> = disable code. <b>if True: pass</b> = TODO only.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; assignment instead of comparison in <code>if</code></span><span class="mistake-desc">Python raises a <code>SyntaxError</code> for <code>if x = 5:</code> because <code>=</code> is assignment, not comparison.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">x = 10
if x = 5:     # SyntaxError
    print("five")</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">x = 10
if x == 5:    # comparison
    print("five")</div></div></div><span class="mistake-note">&#128161; Only the <b>walrus operator</b> <code>:=</code> can assign inside an expression (e.g., <code>if n := len(data):</code>). Regular <code>=</code> is always a statement.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; deep nesting instead of early return (guard clauses)</span><span class="mistake-desc">Deeply nested <code>if/else</code> is hard to read. Guard clauses return early for invalid states, keeping the happy path flat.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def process(user, order):
    if user is not None:
        if user.active:
            if order is not None:
                return order.total
    return 0</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def process(user, order):
    if user is None: return 0
    if not user.active: return 0
    if order is None: return 0
    return order.total  # happy path</div></div></div><span class="mistake-note">&#128161; Guard clauses are the Pythonic pattern for precondition checking. Each guard returns early, leaving the main logic unindented.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; <code>for i in range(len(lst)):</code> when you only need items</span><span class="mistake-desc">Using <code>range(len(...))</code> is verbose when you just need to iterate items. Use the item directly.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">names = ["Anu", "Bob", "Raj"]
for i in range(len(names)):
    print(names[i])</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">names = ["Anu", "Bob", "Raj"]
for name in names:     # direct iteration
    print(name)

# If you need index + value:
for i, name in enumerate(names):
    print(i, name)</div></div></div><span class="mistake-note">&#128161; Only use <code>range(len(...))</code> when you need to <em>modify</em> items by index, or when you need the index for logic beyond simple printing.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Deep nesting</div><div class="step-pre">def validate_order(order):
    if order:
        if order.get("user_id"):
            if order.get("items"):
                if len(order["items"]) > 0:
                    return True
    return False</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Guard clauses (flat)</div><div class="step-pre">def validate_order(order):
    if not order: return False
    if not order.get("user_id"): return False
    if not order.get("items"): return False
    if len(order["items"]) == 0: return False
    return True</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> What does <code>break</code> do inside a <code>for</code> loop?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Immediately exits the loop, skipping any remaining iterations and the <code>else</code> clause.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What does <code>continue</code> do?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Skips the rest of the current iteration and jumps to the next one.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>for x in range(3):</code> iterates over what values?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">0, 1, 2 &mdash; <code>range(n)</code> produces <code>0</code> through <code>n-1</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> When does a <code>for...else</code> block's <code>else</code> run?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">When the loop <b>completes without hitting</b> <code>break</code>. If <code>break</code> is reached, <code>else</code> is skipped.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>pass</code> does what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Nothing &mdash; it&apos;s a no-op placeholder for syntactically required but empty blocks.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> What is a guard clause?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">An early <code>return</code> (or <code>raise</code>) at the top of a function that handles edge cases, keeping the main logic flat.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>while True:</code> loops forever unless it has what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A <code>break</code> statement (or <code>return</code> / exception) somewhere in the body.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q8.</b> Match statement (<code>match x: case 1:</code>) — minimum Python version?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Python 3.10+.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Write FizzBuzz (1–20)</li>
  <li>Use for-else to search a list</li>
  <li>Write a stub function with <code>pass</code>, then implement it</li>
  <li>Try <code>if False:</code> vs <code>if True: pass</code> — which runs?</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyLoops/">MyLoops</a>
'''),

(9, "Comprehensions", '''
''' + code('''# ── LIST COMPREHENSION: [expr for item in iterable if condition] ──
squares = [n * n for n in range(6)]           # [0,1,4,9,16,25]
evens = [n for n in range(10) if n % 2 == 0]  # filter with if

# Equivalent loop (more verbose):
# squares = []
# for n in range(6):
#     squares.append(n * n)

# ── SET COMPREHENSION: unique values ──
unique = {c.lower() for c in "Hello"}         # {'h','e','l','o'}

# ── DICT COMPREHENSION: key-value pairs ──
word_len = {w: len(w) for w in ["hi", "hello"]}  # {'hi':2,'hello':5}

# ── NESTED comprehension ──
matrix = [[i*j for j in range(3)] for i in range(3)]

# ── GENERATOR EXPRESSION: lazy - ( ) not [ ] ──
gen = (n * n for n in range(1_000_000))       # no list in memory
print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 4

# ── yield means GENERATOR FUNCTION ──
# WITHOUT yield: normal function → builds full list, then returns
def squares_list(n):
    out = []
    for i in range(n):
        out.append(i * i)
    return out                    # all values ready at once

# WITH yield: generator function → one value at a time
def squares_gen(n):
    for i in range(n):
        yield i * i               # pause; resume when caller asks again

print(squares_list(3))            # [0, 1, 4]
print(list(squares_gen(3)))       # [0, 1, 4] — same result, lazy build
# list(...) is a built-in function (not a keyword) — consumes the generator into a list

import sys
print(sys.getsizeof(squares))  # ~120 bytes (full list)
print(sys.getsizeof(gen))      # ~200 bytes (generator object)''') + '''
<div class="callout">If the function body uses <b>yield</b> → it is a <b>GENERATOR</b> function. Same loop with <code>return</code> of a list loads everything into RAM; with <code>yield</code> you get one item when asked. A generator <i>expression</i> <code>(...)</code> is the short form (no <code>yield</code> keyword). <b>Hint:</b> <code>list(...)</code> is a Python <b>built-in function</b> (not a keyword).</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; using list comprehension with side effects</span><span class="mistake-desc">Comprehensions should produce a value, not perform side effects like printing or logging. Use a regular <code>for</code> loop for side effects.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Discouraged — side effects in comprehension:
[print(x) for x in items]  # returns [None, None, ...]</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Correct — use a for loop for side effects:
for x in items:
    print(x)

# Comprehension is for building a new collection:
results = [process(x) for x in items]</div></div></div><span class="mistake-note">&#128161; If you only need the side effect, use <code>for</code>. If you need a new collection, use a comprehension. Never mix.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; nested comprehensions that are hard to read</span><span class="mistake-desc">More than one level of nesting in a comprehension makes it nearly unreadable. Extract to a named function.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Hard to read:
matrix = [[1,2],[3,4],[5,6]]
flat = [x for row in matrix for x in row if x % 2 == 0]</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Readable alternative:
def even_elements(matrix):
    for row in matrix:
        for x in row:
            if x % 2 == 0:
                yield x

flat = list(even_elements(matrix))</div></div></div><span class="mistake-note">&#128161; The rule: if a comprehension doesn&apos;t fit in ~80 chars and one mental parse, rewrite it as a generator function.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; list comprehension when a generator suffices</span><span class="mistake-desc">Building a full list in memory before consuming it wastes memory. If you just iterate once, use a generator expression.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Builds entire list in memory before sum:
total = sum([x**2 for x in range(10_000_000)])</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Generator — one item computed at a time:
total = sum(x**2 for x in range(10_000_000))
# Note: no square brackets — that's a generator exp</div></div></div><span class="mistake-note">&#128161; Use <code>(expr for x in iterable)</code> (parentheses) instead of <code>[...]</code> when you only need to iterate once or pass to a consuming function like <code>sum()</code>, <code>max()</code>, <code>join()</code>.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Manual list building</div><div class="step-pre">evens = []
for x in range(20):
    if x % 2 == 0:
        evens.append(x**2)

squares_dict = {}
for x in range(5):
    squares_dict[x] = x**2</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Comprehensions</div><div class="step-pre">evens = [x**2 for x in range(20) if x % 2 == 0]

squares_dict = {x: x**2 for x in range(5)}

# Set comprehension:
unique = {x % 3 for x in range(10)}</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>[x for x in range(5) if x % 2 == 0]</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>[0, 2, 4]</code> &mdash; filters odd numbers, keeps even ones.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>{x: x**2 for x in range(3)}</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>{0: 0, 1: 1, 2: 4}</code> &mdash; dict comprehension: key <code>x</code>, value <code>x²</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>(x**2 for x in range(5))</code> &mdash; what type?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A <b>generator object</b>. No values are computed until iterated.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> Memory: list comprehension vs generator expression?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Generator uses <b>less memory</b> &mdash; it computes one value at a time on demand.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>[x*2 for x in [1,2,3] if x > 1]</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>[4, 6]</code> &mdash; filters items where <code>x &gt; 1</code> (keeping 2 and 3), then doubles them.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> What does the walrus operator <code>:=</code> do in a comprehension?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Assigns a value inside an expression so you can use it both as a condition <em>and</em> a value: <code>[y := f(x), y**2]</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>[x for x in range(5)]</code> vs <code>list(range(5))</code> — which is faster?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>list(range(5))</code> is generally faster since it doesn&apos;t create a lambda/frame overhead for each element.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Build a dict comprehension from a list of tuples</li>
  <li>Compare memory: list vs generator with sys.getsizeof</li>
  <li>Rewrite a list-returning function to use <code>yield</code> and compare</li>
  <li>Filter a list of names starting with "A"</li>
</ul>
'''),

(10, "Python Functions", '''
<p>Mentor resource: <a href="https://www.geeksforgeeks.org/blogs/functional-programming-paradigm/" target="_blank" rel="noopener">GeeksforGeeks — Functional Programming Paradigm</a>. Python supports FP ideas: <b>pure functions</b>, <b>recursion</b>, <b>first-class / higher-order functions</b>, and preferring immutable data where helpful (alongside OOP and procedural styles).</p>
<table class="data-tbl">
<tr><th>FP idea</th><th>Meaning</th><th>Python example</th></tr>
<tr><td>Pure function</td><td>Same args → same result; no side effects</td><td><code>def add(x, y): return x + y</code></td></tr>
<tr><td>First-class</td><td>Functions are values — pass, return, store</td><td><code>ops = [str.upper, str.lower]</code></td></tr>
<tr><td>Higher-order</td><td>Takes or returns a function</td><td><code>sorted(rows, key=lambda r: r[1])</code></td></tr>
<tr><td>Recursion</td><td>Function calls itself (FP often prefers this over loops)</td><td><code>factorial(n)</code></td></tr>
<tr><td>Immutability</td><td>Prefer not mutating shared state</td><td>return new list/tuple instead of changing in place</td></tr>
</table>
''' + code('''# ── BASIC FUNCTION ──
def greet(name, greeting="Hello"):
    """Return a greeting string. greeting has a default value."""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# ── PURE FUNCTION (FP / GFG) — deterministic, no side effects ──
def add(x, y):
    return x + y          # same inputs → always same output

# Impure — mutates global (harder to test / parallelize)
_total = 0
def add_impure(x):
    global _total
    _total += x
    return _total

# ── FIRST-CLASS + HIGHER-ORDER ──
def apply_twice(fn, value):
    return fn(fn(value))  # fn is a function argument

print(apply_twice(lambda n: n + 1, 5))   # 7

# ── *args / **kwargs ──
def total(*args, **kwargs):
    print("args:", args)             # tuple
    print("kwargs:", kwargs)         # dict

total(1, 2, 3, tax=0.1)

# ── RECURSION (FP-style iteration) ──
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))  # 120

# ── LAMBDA ──
multiply_by_two = lambda x: x * 2
print(multiply_by_two(5))

# ── LEGB + CLOSURE ──
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

print(make_multiplier(3)(10))  # 30

# ── MUTABLE DEFAULT TRAP (avoid!) ──
def bad(lst=[]):       # DON'T - shared across calls
    lst.append(1)
    return lst

def good(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst''') + '''
<div class="callout"><b>FP vs OOP (GFG):</b> OOP bundles mutable state in objects. FP prefers pure functions + immutable data — easier to test and safer for concurrency. Python mixes both: use FP tools (<code>map</code>/<code>filter</code>/comprehensions/generators) where they clarify data transforms.</div>
<div class="tip"><b>Mutable default trap:</b> never use <code>def f(lst=[])</code> — use <code>def f(lst=None)</code> and create inside.</div>
<div class="callout"><b>*args / **kwargs:</b> <code>*args</code> = extra positional (<b>tuple</b>); <code>**kwargs</code> = extra named options (<b>dict</b>).
<div class="step-pre">def book(patient_id, doctor_id, *details, **options):
    return patient_id, doctor_id, details, options

print(book("P1", "D9", "Room 2", urgent=True))
# ('P1', 'D9', ('Room 2',), {'urgent': True})</div>
</div>

<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; mutable default argument</span><span class="mistake-desc">Default argument values are evaluated <b>once</b> at function definition time. A mutable default (list, dict) is shared across all calls.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def add_item(item, cart=[]):
    cart.append(item)
    return cart

add_item("apple")   # ["apple"]
add_item("bread")   # ["apple", "bread"] ← shared!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

add_item("apple")   # ["apple"]
add_item("bread")   # ["bread"]  ← fresh</div></div></div><span class="mistake-note">&#128161; Always use <code>None</code> as default for mutable arguments and create a fresh object inside the function body.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; function with no <code>return</code> implicitly returns <code>None</code></span><span class="mistake-desc">Forgetting <code>return</code> means the caller gets <code>None</code> — a silent bug that only appears when the result is used.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def double(x):
    result = x * 2
    # forgot: return result

value = double(5)
print(value * 2)  # TypeError: None * 2</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def double(x):
    result = x * 2
    return result  # explicit return

value = double(5)
print(value * 2)  # 20</div></div></div><span class="mistake-note">&#128161; Add return type hints (<code>-> int</code>) &mdash; type checkers will warn if a code path doesn&apos;t return the declared type.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; misunderstanding <code>*args</code> and <code>**kwargs</code> types</span><span class="mistake-desc">Inside the function, <code>*args</code> is a <b>tuple</b> and <code>**kwargs</code> is a <b>dict</b>. Calling code passes positional / keyword arguments, not the containers.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def show(*args, **kwargs):
    args.append("extra")   # AttributeError!
    kwargs["key"] = 1      # OK — dict supports this</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def show(*args, **kwargs):
    print(type(args))      # &lt;class 'tuple'&gt;
    print(type(kwargs))    # &lt;class 'dict'&gt;
    extra = args + ("extra",)  # tuples are immutable</div></div></div><span class="mistake-note">&#128161; <code>*args</code> is an <b>immutable tuple</b> &mdash; you cannot <code>.append()</code> to it. Convert to a list first if mutation is needed.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Mutable default (bug)</div><div class="step-pre">def register(name, tags=[]):
    tags.append(name)
    return tags

print(register("Anu"))    # ["Anu"]
print(register("Bob"))    # ["Anu", "Bob"] ← wrong!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; None default (correct)</div><div class="step-pre">def register(name, tags=None):
    if tags is None:
        tags = []
    tags.append(name)
    return tags

print(register("Anu"))    # ["Anu"]
print(register("Bob"))    # ["Bob"]  ← correct</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>def f(x=[]):</code> — what is wrong?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The list default is created <b>once</b> at definition time and shared across all calls. Use <code>x=None</code> and create a new list inside.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> A function with no <code>return</code> returns what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>None</code> implicitly. Every Python function returns something &mdash; the default is <code>None</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>*args</code> type inside a function?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>tuple</code> &mdash; positional extra arguments are collected into an immutable tuple.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>**kwargs</code> type inside a function?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>dict</code> &mdash; extra keyword arguments are collected into a dictionary.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> Correct parameter order: positional, *args, keyword-only, **kwargs?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Yes &mdash; <code>def f(pos, *args, keyword_only, **kwargs)</code>. Parameters after <code>*args</code> are keyword-only.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> What is a closure?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A function that <b>remembers variables</b> from its enclosing scope even after the outer function has returned.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>lambda x, y: x + y</code> — how to call it?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>(lambda x, y: x + y)(3, 4)</code> &rarr; <code>7</code>. Or assign: <code>add = lambda x, y: x + y; add(3, 4)</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q8.</b> What is the difference between <code>def</code> and <code>lambda</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>lambda</code> is a single-expression anonymous function. <code>def</code> creates a named function and can have multiple statements.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Write one pure and one impure function — explain the difference</li>
  <li>Pass a function into another function (higher-order)</li>
  <li>Implement factorial recursively</li>
  <li>Create a closure that multiplies by a fixed factor</li>
</ul>
'''),

(11, "Built-in Functions", '''
<p>These builtins are classic <b>higher-order functions</b> (FP): they take other functions as arguments — see <a href="https://www.geeksforgeeks.org/blogs/functional-programming-paradigm/" target="_blank" rel="noopener">Functional Programming Paradigm</a>.</p>
<table class="data-tbl">
<tr><th>Function</th><th>Purpose</th></tr>
<tr><td>map(fn, iter)</td><td>Apply fn to each item</td></tr>
<tr><td>filter(fn, iter)</td><td>Keep items where fn is True</td></tr>
<tr><td>zip(a, b)</td><td>Pair elements from two (or more) iterables</td></tr>
<tr><td>zip(*rows)</td><td>Unpack a list of rows into columns</td></tr>
<tr><td>enumerate(iter)</td><td>Index + value pairs</td></tr>
<tr><td>sorted(iter)</td><td>Return sorted copy</td></tr>
<tr><td>max(iter) / min(iter)</td><td>Largest / smallest item</td></tr>
</table>
''' + code('''# ── filter: keep items that pass a test (run this first) ──
def is_even(n):
    return n % 2 == 0   # True for 2, 4, 6...

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, nums))
print("evens:", evens)

def has_fever(temp):
    return temp > 100

temps = [98.6, 99.1, 101.2, 100.5]
fever = list(filter(has_fever, temps))
print("fever:", fever)


# ── sorted() vs .sort() — trap: .sort() returns None ──
names = ["zion", "amala"]
print(sorted(names))
print(names)
print(names.sort())
print(names)


from functools import reduce

nums = [1, 2, 3, 4, 5]

# ── map: apply function to each item ──
doubled = list(map(lambda x: x * 2, nums))     # [2,4,6,8,10]
upper = list(map(str.upper, ["a", "b"]))      # ['A','B']

# ── reduce: fold to single value ──
total = reduce(lambda a, b: a + b, nums)      # 15

# ── zip: pair elements from iterables ──
names = ["Alice", "Bob"]
scores = [95, 88]
pairs = list(zip(names, scores))              # [('Alice',95),('Bob',88)]
score_dict = dict(zip(names, scores))         # {'Alice':95,'Bob':88}

# ── zip(*rows): unpack rows → columns ──
# * opens the list so zip gets each row as its own argument
readings = [(120, 80, 98.6), (115, 75, 99.1)]
# zip(*readings)  ==  zip((120,80,98.6), (115,75,99.1))
sys_list, dia_list, temps = zip(*readings)
# sys_list → (120, 115)   dia_list → (80, 75)   temps → (98.6, 99.1)

# ── enumerate: index + value ──
for i, v in enumerate(["a", "b", "c"]):
    print(i, v)                               # 0 a, 1 b, 2 c

# ── sorted: new sorted copy ──
sorted_desc = sorted(nums, reverse=True)        # [5,4,3,2,1]
by_len = sorted(["hi", "hello", "hey"], key=len)

# ── type inspection ──
print(type(42))              # <class 'int'>
print(isinstance(42, int))    # True
print(isinstance(42, (int, float)))  # True

# ── max / min ──
prices = [120, 45, 89, 200]
max(prices)                  # 200
min(prices)                  # 45
max(prices, key=lambda p: -p)  # smallest via custom key

scores = {"Anu": 90, "Ravi": 85}
max(scores, key=scores.get)  # "Anu"''') + '''


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; assigning <code>.sort()</code> to a variable</span><span class="mistake-desc"><code>.sort()</code> modifies the list <b>in-place</b> and always returns <code>None</code>. Assigning it to a variable silently discards the list.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">nums = [3, 1, 2]
x = nums.sort()
print(x)       # None  ← lost!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">nums = [3, 1, 2]
x = sorted(nums)
print(x)       # [1, 2, 3]</div></div></div><span class="mistake-note">&#128161; Use <code>sorted()</code> to get a <b>new</b> sorted list as a value. Use <code>.sort()</code> only when you want to mutate in-place and don&apos;t need the result.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; forgetting <code>list()</code> around <code>map()</code> / <code>filter()</code></span><span class="mistake-desc"><code>map()</code> and <code>filter()</code> return <b>lazy iterators</b>, not lists. Printing them shows an object address, not the values.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">nums = [1, 2, 3]
result = map(lambda x: x*2, nums)
print(result)
# &lt;map object at 0x1f3a&gt;</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">nums = [1, 2, 3]
result = list(map(lambda x: x*2, nums))
print(result)
# [2, 4, 6]</div></div></div><span class="mistake-note">&#128161; Wrap with <code>list()</code> to materialise the iterator, or use a comprehension: <code>[x*2 for x in nums]</code>. Same applies to <code>filter()</code>, <code>zip()</code>, and <code>reversed()</code>.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; calling <code>max()</code> / <code>min()</code> on an empty sequence</span><span class="mistake-desc">If the iterable is empty, <code>max()</code> and <code>min()</code> raise a <code>ValueError</code> with no default protection.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">scores = []
best = max(scores)
# ValueError: max() arg is
# an empty sequence</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">scores = []
best = max(scores, default=0)
print(best)    # 0  (safe)

# or guard:
if scores:
    best = max(scores)</div></div></div><span class="mistake-note">&#128161; The <code>default=</code> keyword (Python 3.4+) lets <code>max()</code> / <code>min()</code> return a fallback value instead of crashing.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 4 &mdash; <code>type(x) == int</code> instead of <code>isinstance()</code></span><span class="mistake-desc"><code>type()</code> does an <b>exact</b> match &mdash; it ignores inheritance. Since <code>bool</code> is a subclass of <code>int</code>, <code>type(True) == int</code> returns <code>False</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def is_number(x):
    return type(x) == int

print(is_number(42))    # True
print(is_number(True))  # False ← wrong!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def is_number(x):
    return isinstance(x, int)

print(is_number(42))    # True
print(is_number(True))  # True  ✔</div></div></div><span class="mistake-note">&#128161; <code>isinstance()</code> respects the class hierarchy. It also accepts a tuple: <code>isinstance(x, (int, float))</code> to check multiple types at once.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Non-Pythonic</div><div class="step-pre">result = []
for item in items:
    result.append(item * 2)

idx = 0
for name in names:
    print(idx, name)
    idx += 1

x = my_list.sort()   # x is None!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Pythonic</div><div class="step-pre">result = [item * 2 for item in items]
# or: list(map(lambda x: x*2, items))

for idx, name in enumerate(names):
    print(idx, name)

x = sorted(my_list)  # x is the list</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> What does <code>x = my_list.sort()</code> put in <code>x</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>None</code> &mdash; <code>.sort()</code> mutates in place and returns nothing. Use <code>sorted(my_list)</code> to capture the sorted result in a variable.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>max({&quot;a&quot;: 3, &quot;b&quot;: 7})</code> &mdash; what does it return and why?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>&quot;b&quot;</code> &mdash; iterating a dict yields its <b>keys</b>, so <code>max</code> compares alphabetically. To find the key with the highest <b>value</b>: <code>max(d, key=d.get)</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>isinstance(True, int)</code> &mdash; <code>True</code> or <code>False</code>? Why?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>True</code> &mdash; <code>bool</code> is a subclass of <code>int</code>. <code>type(True) == int</code> is <code>False</code> (exact match only).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> How many pairs does <code>list(zip([1,2,3], [&quot;a&quot;,&quot;b&quot;]))</code> produce?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">2 &mdash; <code>zip()</code> stops at the <b>shortest</b> iterable. The third element is silently dropped.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>list(enumerate([&quot;x&quot;,&quot;y&quot;], start=1))</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>[(1, 'x'), (2, 'y')]</code> &mdash; <code>start=</code> sets the initial counter.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>list(filter(None, [0, 1, False, 2, '', 'hi']))</code> &mdash; what is kept?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>[1, 2, 'hi']</code> &mdash; <code>None</code> as function keeps only <b>truthy</b> values.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>sorted('python')</code> &mdash; what type and what content?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A <b>list</b>: <code>['h','n','o','p','t','y']</code> &mdash; <code>sorted()</code> works on any iterable and returns a new list.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q8.</b> <code>list(map(len, ['hi','hello','hey']))</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>[2, 5, 3]</code> &mdash; <code>map()</code> applies <code>len</code> to each string.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q9.</b> <code>max([3,1,4], key=lambda x: -x)</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>1</code> &mdash; negated values are <code>[-3,-1,-4]</code>; max of those is <code>-1</code>, corresponding to original <code>1</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q10.</b> <code>list(zip(*[[1,2],[3,4],[5,6]]))</code> &mdash; what does <code>*</code> do?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>[(1,3,5),(2,4,6)]</code> &mdash; <code>*</code> unpacks the list so <code>zip</code> gets three separate args, transposing the matrix.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Use map/filter vs list comprehension — compare readability</li>
  <li>Zip two lists into dict</li>
  <li>Use zip(*rows) to turn a list of rows into columns</li>
  <li>Sort a list of tuples by second element</li>
</ul>
'''),

(12, "Python Collections", '''
<table class="data-tbl">
<tr><th>Class</th><th>Use case</th></tr>
<tr><td>Counter</td><td>Count occurrences</td></tr>
<tr><td>defaultdict</td><td>Auto-default for missing keys</td></tr>
<tr><td>deque</td><td>Fast append/pop both ends</td></tr>
<tr><td>namedtuple</td><td>Lightweight record</td></tr>
<tr><td>ChainMap</td><td>Search multiple dicts</td></tr>
</table>
''' + code('''from collections import Counter, defaultdict, deque, namedtuple, ChainMap

# ── Counter: count occurrences ──
word_counts = Counter("hello world")
print(word_counts)            # Counter({'l':3,'o':2,'h':1,...})
print(word_counts.most_common(2))  # top 2

# ── defaultdict: auto-create missing keys ──
groups = defaultdict(list)    # missing key → empty list
groups["fruit"].append("apple")
groups["fruit"].append("banana")
groups["veg"].append("carrot")
print(dict(groups))           # {'fruit':['apple','banana'],'veg':['carrot']}

# ── deque: fast double-ended queue ──
dq = deque([1, 2, 3])
dq.append(4)                  # add right  → [1,2,3,4]
dq.appendleft(0)              # add left   → [0,1,2,3,4]
print(dq.popleft())           # remove left → 0

# ── namedtuple: tuple with named fields ──
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)               # 10 20
print(p[0], p[1])             # index still works

# ── ChainMap: layered lookup (first dict wins) ──
app_defaults = {"color": "red", "size": "M"}
user = {"color": "blue"}
print("app_defaults:", app_defaults)
print("user:", user)
settings = ChainMap(user, app_defaults)   # user first, then app_defaults
print(settings["color"])              # blue — found in user
print(settings["size"])               # M — falls through to app_defaults''') + '''


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; manual counting with <code>dict</code> instead of <code>Counter</code></span><span class="mistake-desc"><code>Counter</code> is the Pythonic tool for frequency counting. Doing it manually is verbose and error-prone.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">words = ["a", "b", "a", "c", "a"]
counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 0  # bug: should be 1 first time!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from collections import Counter
words = ["a", "b", "a", "c", "a"]
counts = Counter(words)
print(counts)         # Counter({'a':3,'b':1,'c':1})
print(counts.most_common(2))  # top 2</div></div></div><span class="mistake-note">&#128161; <code>Counter</code> handles missing keys automatically and provides <code>.most_common(n)</code>, arithmetic operators, and subtraction.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; grouping with plain <code>dict</code> instead of <code>defaultdict(list)</code></span><span class="mistake-desc">When you <code>.append()</code> to a missing key, a normal dict raises <code>KeyError</code>. You must create the empty list yourself first — easy to forget.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">Plain dict — set value</span><div class="step-pre">by_assignee = {}
by_assignee["Ravi"].append(101)
# KeyError: 'Ravi' — key does not exist yet

# Manual fix (verbose):
if "Ravi" not in by_assignee:
    by_assignee["Ravi"] = []
by_assignee["Ravi"].append(101)</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; With defaultdict</span><div class="step-pre">from collections import defaultdict
by_assignee = defaultdict(list)
by_assignee["Ravi"].append(101)   # OK
by_assignee["Anu"].append(102)   # OK
print(dict(by_assignee))
# {'Ravi': [101], 'Anu': [102]}</div></div></div><span class="mistake-note">&#128161; <code>defaultdict(list)</code> calls <code>list()</code> the first time you touch a missing key — you get <code>[]</code> automatically, then <code>.append()</code> works.</span></div>
<div class="mistake-box"><span class="mistake-title">&#9888; One trap &mdash; <code>if myDict["key"]:</code> can create a key by accident</span><span class="mistake-desc">You might think <code>if myDict["ghost"]:</code> means &ldquo;skip if ghost has no tickets.&rdquo; <b>Python evaluates the condition first</b> — looking up <code>myDict["ghost"]</code> creates <code>"ghost": []</code>. The empty list is falsy (if body skipped), but the key is already in the dict.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">Looks safe — adds key anyway</span><div class="step-pre">from collections import defaultdict
myDict = defaultdict(list)
print(dict(myDict))           # {}

if myDict["ghost"]:          # Step 1: lookup → creates "ghost": []
    print("tickets")    # Step 2: [] is falsy → skipped

print(dict(myDict))           # {"ghost": []}  surprise!</div></div><div class="mc-col mc-good"><span class="mc-lbl">Safe check first</span><div class="step-pre">from collections import defaultdict
myDict = defaultdict(list)

if "ghost" in myDict:        # only asks — never creates
    print(myDict["ghost"])

myDict["Ravi"].append(101)   # OK — you mean to use this key
print(dict(myDict))          # {"Ravi": [101]}</div></div></div><span class="mistake-note">&#128161; <b>Rule:</b> <code>"key" in myDict</code> = peek (safe). <code>myDict["key"]</code> = touch (creates missing key). Use <code>myDict[key].append(...)</code> only when you want that group.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; using <code>list</code> as a queue (O(n) <code>popleft</code>)</span><span class="mistake-desc">Removing from the front of a list (<code>list.pop(0)</code>) shifts all elements &mdash; O(n). <code>deque</code> does it in O(1).</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">queue = [1, 2, 3, 4, 5]
queue.pop(0)   # O(n) — shifts every element
queue.pop(0)   # slow for large queues</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from collections import deque
queue = deque([1, 2, 3, 4, 5])
queue.popleft()   # O(1) — fast!
queue.appendleft(0)  # O(1) prepend</div></div></div><span class="mistake-note">&#128161; Use <code>deque</code> whenever you need efficient adds/removes from <b>both ends</b>. Use <code>list</code> for random access by index.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Manual grouping</div><div class="step-pre">records = [("A",1),("B",2),("A",3)]
groups = {}
for k, v in records:
    if k not in groups:
        groups[k] = []
    groups[k].append(v)</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; defaultdict</div><div class="step-pre">from collections import defaultdict
records = [("A",1),("B",2),("A",3)]
groups = defaultdict(list)
for k, v in records:
    groups[k].append(v)
# {'A': [1, 3], 'B': [2]}</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>Counter('aab')</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>Counter({'a': 2, 'b': 1})</code> &mdash; counts each character in the string.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>defaultdict(int)['missing']</code> &mdash; what is returned?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>0</code> &mdash; <code>int()</code> is called as the factory, returning <code>0</code> for any missing key.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>deque</code> vs <code>list</code> for <code>popleft()</code> — which is faster?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>deque</code> &mdash; O(1) vs O(n) for lists, because no element shifting is needed.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>Counter({'a':2}) - Counter({'a':3})</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>Counter()</code> &mdash; Counter subtraction drops zero and negative counts.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>namedtuple</code> vs regular <code>tuple</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">namedtuple has named fields (<code>p.x</code>, <code>p.y</code>) while regular tuples use only index access (<code>p[0]</code>).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>ChainMap(user, app_defaults)['key']</code> — which dict is searched first?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>user</code> &mdash; ChainMap searches maps in order, so the first mapping takes priority.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>deque(maxlen=3)</code> — what happens when you append a 4th item?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The oldest item is automatically removed from the other end &mdash; a rolling window.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Count word frequency with Counter</li>
  <li>Group items by category with defaultdict</li>
  <li>Use deque as a simple queue</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyCollections/">MyCollections</a>
'''),

(13, "Memory Management & Garbage Collection", '''
<p>Python manages memory for you — but understanding references, cycles, and the GC helps debug leaks and performance issues in long-running services.</p>
<table class="ref-table">
<tr><th>Concept</th><th>What happens</th></tr>
<tr><td>Reference counting</td><td>Each object tracks how many names point to it; at zero, memory is freed immediately</td></tr>
<tr><td>Garbage collector (gc)</td><td>Finds circular references reference counting cannot break</td></tr>
<tr><td>Generations 0/1/2</td><td>Young objects collected more often — amortized cost</td></tr>
<tr><td>Immutable interning</td><td>Small ints and some strings may be shared — affects <code>is</code> tests</td></tr>
<tr><td>del</td><td>Removes a name binding — does not guarantee instant destruction</td></tr>
</table>
''' + code('''import sys
import gc

# ── Reference counting ──
a = [1, 2, 3]
print(sys.getrefcount(a))   # approximate count (+ interpreter overhead)

b = a
print(sys.getrefcount(a))   # higher — two names reference same list

del b                       # removes name b, not necessarily the list yet

# ── Circular reference (GC handles this) ──
class Node:
    def __init__(self):
        self.ref = None

x = Node()
y = Node()
x.ref = y
y.ref = x   # cycle — refcount never hits 0 alone
del x, y
gc.collect()  # breaks cycle and reclaims

# ── Weak references (avoid keeping objects alive) ──
import weakref

obj = {"key": "value"}
ref = weakref.ref(obj)
print(ref())        # dict still alive
del obj
print(ref())        # None — object collected''') + '''
<div class="challenge"><b>C# comparison:</b> Python has no <code>IDisposable</code> pattern for every object — use <code>with</code> for files/sockets. GC is always on; you rarely call <code>gc.collect()</code> except when debugging leaks.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; thinking <code>del x</code> immediately frees memory</span><span class="mistake-desc"><code>del x</code> removes the <b>name binding</b>, not the object. Memory is freed only when the reference count drops to zero.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">big_data = load_large_dataset()  # large object
del big_data
# object is NOT freed yet if other references exist
import gc; gc.collect()  # this actually runs GC</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Ensure no other references exist:
big_data = load_large_dataset()
process(big_data)
del big_data   # removes last reference → freed
# OR: use a function scope so object goes out of scope</div></div></div><span class="mistake-note">&#128161; To guarantee cleanup, ensure the object has <b>no remaining references</b>. Scoping (function, <code>with</code> block) is the cleanest approach.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; not using <code>with</code> for files and resources</span><span class="mistake-desc">Without <code>with</code>, a file may stay open if an exception occurs before the explicit <code>.close()</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">f = open("data.txt")
data = f.read()
# if exception happens here, file stays open!
f.close()</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">with open("data.txt", encoding="utf-8") as f:
    data = f.read()
# file is closed automatically, even on exception</div></div></div><span class="mistake-note">&#128161; <code>with</code> calls <code>__exit__</code> (which closes the file) even if an exception is raised inside the block.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; circular references silently staying in memory</span><span class="mistake-desc">Reference counting cannot break cycles. The garbage collector (<code>gc</code> module) handles them, but they can accumulate before collection.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class Node:
    def __init__(self): self.ref = None

a = Node(); b = Node()
a.ref = b; b.ref = a   # cycle!
del a, b
# refcount never hits 0 — GC must clean up</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import weakref

class Node:
    def __init__(self): self.ref = None

a = Node(); b = Node()
a.ref = weakref.ref(b)  # weak ref — no cycle!
del b
print(a.ref())  # None — b was collected</div></div></div><span class="mistake-note">&#128161; Use <code>weakref.ref()</code> for back-references (parent→child is strong, child→parent is weak) to avoid retention cycles.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Manual file management</div><div class="step-pre">f = open("log.txt", "w")
try:
    f.write("step 1\\n")
    f.write("step 2\\n")
finally:
    f.close()   # explicit close needed</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Context manager</div><div class="step-pre">with open("log.txt", "w", encoding="utf-8") as f:
    f.write("step 1\\n")
    f.write("step 2\\n")
# closed automatically — even if exception raised</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> What is reference counting?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Each Python object tracks how many names (variables, list elements, etc.) point to it. When the count reaches 0, the memory is freed immediately.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What defeats pure reference counting?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><b>Circular references</b> &mdash; two objects that refer to each other keep each other's count above zero forever.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>del x</code> — does it immediately free the object's memory?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Only if <code>x</code> was the <b>last reference</b>. Otherwise it just removes the name binding.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> Which module provides manual GC control?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>gc</code> &mdash; <code>gc.collect()</code> runs a full collection cycle. Rarely needed in normal code.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>sys.getrefcount(x)</code> returns?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The number of references to the object (always at least 1 extra because the function argument is itself a reference).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> What is a weak reference?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A reference that does <b>not</b> increment the reference count &mdash; the object can be collected even if a weakref exists.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Run <code>Projects/32_memory_gc.py</code> and watch refcount change</li>
  <li>Explain difference between <code>del x</code> and <code>x = None</code></li>
  <li>Describe when circular references need the GC</li>
</ul>
'''),

(14, "Pydantic", '''
<p>Pydantic validates and parses data using type hints — the backbone of FastAPI request/response models (like DataAnnotations + DTOs in C#).</p>
<table class="ref-table">
<tr><th>Feature</th><th>Purpose</th></tr>
<tr><td>BaseModel</td><td>Define schema with typed fields</td></tr>
<tr><td>Validation</td><td>Coercion + constraints on assign</td></tr>
<tr><td>model_dump()</td><td>Export to dict (v2; was <code>.dict()</code>)</td></tr>
<tr><td>Field()</td><td>Defaults, ge/le, descriptions</td></tr>
<tr><td>model_validator</td><td>Cross-field validation (v2)</td></tr>
</table>
''' + code('''from pydantic import BaseModel, Field, field_validator

class CreateUser(BaseModel):
    email: str
    age: int = Field(ge=18, le=120)
    tags: list[str] = []

    @field_validator("email")
    @classmethod
    def email_must_have_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("invalid email")
        return v.lower()

# ── Parse / validate ──
payload = {"email": "Anu@Example.COM", "age": "25"}  # age str OK
user = CreateUser.model_validate(payload)
print(user.model_dump())
# {'email': 'anu@example.com', 'age': 25, 'tags': []}

# ── Invalid data raises ValidationError ──
try:
    CreateUser.model_validate({"email": "bad", "age": 10})
except Exception as e:
    print(type(e).__name__, e)''') + '''
<div class="callout"><b>FastAPI tie-in:</b> Route parameters typed as Pydantic models auto-validate JSON bodies and return 422 with field errors — no manual <code>if not email</code> checks in every handler.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; using deprecated <code>.dict()</code> in Pydantic v2</span><span class="mistake-desc">Pydantic v2 replaced <code>.dict()</code> with <code>.model_dump()</code>. Using the old method emits a deprecation warning and will break in future versions.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">user = User(name="Anu", age=30)
data = user.dict()   # DeprecationWarning in v2
print(data)</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">user = User(name="Anu", age=30)
data = user.model_dump()     # v2 method
json_str = user.model_dump_json()  # as JSON string</div></div></div><span class="mistake-note">&#128161; Other renames: <code>.parse_obj()</code> → <code>.model_validate()</code>, <code>.schema()</code> → <code>.model_json_schema()</code>.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; confusing required vs optional fields</span><span class="mistake-desc">A field without a default is <b>required</b>. Using <code>= None</code> makes it optional. Forgetting this causes unexpected <code>ValidationError</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float = None  # type mismatch: float but default None

Item(name="x")  # price=None — but type says float!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str             # required
    price: float          # required
    tag: str | None = None  # optional</div></div></div><span class="mistake-note">&#128161; For optional fields use <code>str | None = None</code>. For required fields, declare just the type with no default.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; mutating a frozen Pydantic model</span><span class="mistake-desc">With <code>ConfigDict(frozen=True)</code>, instances are immutable. Trying to set an attribute raises a <code>ValidationError</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">from pydantic import BaseModel, ConfigDict

class Config(BaseModel):
    model_config = ConfigDict(frozen=True)
    host: str

c = Config(host="localhost")
c.host = "remote"  # ValidationError!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from pydantic import BaseModel, ConfigDict

class Config(BaseModel):
    model_config = ConfigDict(frozen=True)
    host: str

c = Config(host="localhost")
# Create new instance instead of mutating:
c2 = c.model_copy(update={"host": "remote"})</div></div></div><span class="mistake-note">&#128161; Frozen models are useful for config objects and hash keys. Use <code>.model_copy(update={})</code> to get a modified copy.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Raw dict validation</div><div class="step-pre">def create_user(data: dict):
    # hope data has correct keys/types
    name = data["name"]        # KeyError risk
    age = int(data.get("age"))  # None cast risk
    return {"name": name, "age": age}</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Pydantic model</div><div class="step-pre">from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

def create_user(data: dict) -> User:
    user = User.model_validate(data)  # validated
    return user
# ValidationError if name or age missing/wrong type</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Pydantic v2 replacement for <code>.dict()</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>.model_dump()</code> &mdash; returns a dict. <code>.model_dump_json()</code> returns a JSON string.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> How to make a Pydantic field required?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Declare it with just a type and no default: <code>name: str</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> How to make a Pydantic field optional?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>name: str | None = None</code> (or <code>Optional[str] = None</code>).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> What does <code>@field_validator('price')</code> do?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Runs a custom validation/transformation function when that field is set.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>model_config = ConfigDict(frozen=True)</code> — what does it do?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Makes model instances <b>immutable</b> &mdash; attributes cannot be changed after creation.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> How to validate from a JSON string in Pydantic v2?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>Model.model_validate_json(json_str)</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> What is <code>Field(...)</code> used for?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Provides metadata: <code>description</code>, <code>gt</code>/<code>lt</code> constraints, <code>alias</code>, <code>default_factory</code>, etc.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Install: <code>pip install pydantic</code></li>
  <li>Run <code>python Projects/34_pydantic_demo.py</code></li>
  <li>Add one <code>field_validator</code> for a business rule</li>
</ul>
'''),

(15, "OOP Concepts", '''
''' + code('''# ── BASE CLASS ──
class Animal:
    def __init__(self, name):
        self.name = name          # instance attribute

    def speak(self):
        raise NotImplementedError("Subclass must implement")

    def __str__(self):
        return f"Animal({self.name})"   # user-friendly

    def __repr__(self):
        return f"Animal(name={self.name!r})"  # developer debug

# ── INHERITANCE: override parent method ──
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# ── POLYMORPHISM: same call, different behavior ──
pets = [Dog("Rex"), Cat("Luna")]
for pet in pets:
    print(pet.speak())

# ── ENCAPSULATION: _protected convention + @property ──
class BankAccount:
    def __init__(self, balance):
        self._balance = balance   # _ = "protected" by convention

    @property
    def balance(self):
        return self._balance      # getter

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

acct = BankAccount(1000)
acct.deposit(500)
print(acct.balance)               # 1500

# ── MRO: Method Resolution Order ──
print(Dog.__mro__)                # search order for methods''') + '''
<div class="callout">MRO (Method Resolution Order): Python searches base classes left-to-right. Use <code>ClassName.__mro__</code> to inspect.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; forgetting <code>self</code> as the first method parameter</span><span class="mistake-desc">Every instance method must have <code>self</code> as its first parameter. Without it, calling the method raises a <code>TypeError</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class Dog:
    def bark(name):   # missing self
        print(f"{name} barks")

d = Dog()
d.bark()   # TypeError: bark() takes 1 argument but 2 given</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):   # self first
        print(f"{self.name} barks")

d = Dog("Rex")
d.bark()   # Rex barks</div></div></div><span class="mistake-note">&#128161; <code>self</code> is just a convention &mdash; Python passes the instance automatically as the first argument. Any name works but <code>self</code> is universal.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; class-level mutable attribute shared by all instances</span><span class="mistake-desc">Mutable class attributes (list, dict) are shared by all instances. Appending to one affects all.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class Student:
    courses = []  # class-level — SHARED!
    def add(self, c): self.courses.append(c)

a = Student(); a.add("Math")
b = Student()
print(b.courses)  # ["Math"] ← b sees a's data!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">class Student:
    def __init__(self):
        self.courses = []  # instance-level
    def add(self, c): self.courses.append(c)

a = Student(); a.add("Math")
b = Student()
print(b.courses)  # []  ← independent</div></div></div><span class="mistake-note">&#128161; Define mutable attributes in <code>__init__</code> using <code>self.attr = ...</code>. Class-level attributes are only safe for immutables (strings, ints) or shared constants.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; not calling <code>super().__init__()</code> in child class</span><span class="mistake-desc">If a child class overrides <code>__init__</code> without calling <code>super().__init__()</code>, the parent&apos;s initialization is skipped.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        # forgot super().__init__(name)

d = Dog("Rex", "Lab")
print(d.name)   # AttributeError!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent init
        self.breed = breed

d = Dog("Rex", "Lab")
print(d.name)    # Rex
print(d.breed)   # Lab</div></div></div><span class="mistake-note">&#128161; Always call <code>super().__init__(...)</code> in child <code>__init__</code> unless you intentionally replace the parent&apos;s setup.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Class attribute (shared)</div><div class="step-pre">class Cart:
    items = []     # shared by ALL Cart instances!

c1 = Cart()
c1.items.append("apple")

c2 = Cart()
print(c2.items)   # ["apple"] — unintended!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Instance attribute</div><div class="step-pre">class Cart:
    def __init__(self):
        self.items = []   # each instance owns its list

c1 = Cart()
c1.items.append("apple")

c2 = Cart()
print(c2.items)   # []  ← correct</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>self</code> in a method refers to?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The <b>instance</b> on which the method is called. Python passes it automatically as the first argument.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>@classmethod</code> receives what as its first argument?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>cls</code> &mdash; the <b>class itself</b>, not an instance. Used for alternative constructors.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>@staticmethod</code> receives?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No implicit first argument &mdash; it&apos;s a plain function namespaced inside the class.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>__str__</code> vs <code>__repr__</code> — which is for developers?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>__repr__</code> is for unambiguous developer representation. <code>__str__</code> is for end-user readable output.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>super().__init__()</code> — when is it needed?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">When inheriting and overriding <code>__init__</code>, to run the <b>parent class&apos;s</b> initialisation code.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>@property</code> turns a method into?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A read-only attribute that can be accessed without calling parentheses: <code>obj.value</code> instead of <code>obj.value()</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> What does <code>ClassName.__mro__</code> show?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The Method Resolution Order &mdash; the order in which Python searches base classes for methods.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q8.</b> Difference between <code>__new__</code> and <code>__init__</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>__new__</code> creates the object; <code>__init__</code> initialises it. Override <code>__new__</code> for immutable types like <code>tuple</code> subclasses.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Create a class with __init__ and two methods</li>
  <li>Add inheritance — override one method</li>
  <li>Implement __str__ and __repr__</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyClass/">MyClass</a>
<a class="file-link" href="Python-Set2/pythonBasics/MyClass/oops_inheritance_BankAccount.py">BankAccount</a>
'''),

(16, "Descriptors", '''
''' + code('''# ── @property: most common descriptor pattern ──
class Celsius:
    def __init__(self):
        self._temp = 0.0          # private storage

    @property                     # getter - called on read
    def temp(self):
        return self._temp

    @temp.setter                  # setter - called on assignment
    def temp(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._temp = value

    @temp.deleter                 # deleter - called on del
    def temp(self):
        del self._temp

c = Celsius()
c.temp = 25                       # calls setter
print(c.temp)                     # calls getter → 25

# c.temp = -300                   # ValueError

# ── READ-ONLY property (no setter) ──
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):               # computed, read-only
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.area)                # 78.54...''') + '''
<p>Custom descriptors implement <code>__get__</code>, <code>__set__</code>, <code>__delete__</code> — @property is the common built-in form.</p>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; storing descriptor data on the descriptor instance</span><span class="mistake-desc">Descriptor data stored on the descriptor itself is <b>shared by all instances</b> of the owner class.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class Validated:
    def __set__(self, obj, value):
        self.value = value  # stored on DESCRIPTOR — shared!
    def __get__(self, obj, cls):
        return self.value

class User:
    age = Validated()

u1 = User(); u1.age = 30
u2 = User(); u2.age = 25
print(u1.age)  # 25 ← wrong!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">class Validated:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, obj, value):
        obj.__dict__[self.name] = value  # on INSTANCE
    def __get__(self, obj, cls):
        if obj is None: return self
        return obj.__dict__.get(self.name)</div></div></div><span class="mistake-note">&#128161; Always store data on <code>obj.__dict__</code> using a key derived from <code>__set_name__</code>.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; <code>__get__</code> not handling the class access case</span><span class="mistake-desc">When a descriptor is accessed on the <b>class</b> (not an instance), <code>obj</code> is <code>None</code>. Not handling this raises <code>AttributeError</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class Positive:
    def __get__(self, obj, cls):
        return obj.__dict__[self.name]  # crashes if obj is None!

print(User.score)  # AttributeError: 'NoneType' has no attribute...</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">class Positive:
    def __get__(self, obj, cls):
        if obj is None:
            return self  # class access → return the descriptor itself
        return obj.__dict__[self.name]</div></div></div><span class="mistake-note">&#128161; The pattern <code>if obj is None: return self</code> is standard for all <code>__get__</code> implementations.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; using a data descriptor when a <code>@property</code> suffices</span><span class="mistake-desc">For per-class validation that doesn&apos;t need reuse, <code>@property</code> is simpler than a full descriptor class.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Overkill for one-off validation:
class PositiveInt:
    def __set_name__(self, owner, name): ...
    def __get__(self, obj, cls): ...
    def __set__(self, obj, value): ...

class Order:
    qty = PositiveInt()</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Simpler for one-off:
class Order:
    def __init__(self, qty):
        self.qty = qty

    @property
    def qty(self): return self._qty

    @qty.setter
    def qty(self, v):
        if v < 0: raise ValueError
        self._qty = v</div></div></div><span class="mistake-note">&#128161; Use a descriptor class when the same validation logic is needed in <b>many different classes</b>. For one class, <code>@property</code> is cleaner.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Repeated property boilerplate</div><div class="step-pre">class Product:
    @property
    def price(self): return self._price
    @price.setter
    def price(self, v):
        if v < 0: raise ValueError("negative")
        self._price = v

class Order:
    @property  # same code repeated!
    def qty(self): return self._qty
    @qty.setter
    def qty(self, v):
        if v < 0: raise ValueError("negative")
        self._qty = v</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Reusable descriptor</div><div class="step-pre">class NonNegative:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, obj, v):
        if v < 0: raise ValueError("negative")
        obj.__dict__[self.name] = v
    def __get__(self, obj, cls):
        if obj is None: return self
        return obj.__dict__.get(self.name)

class Product:
    price = NonNegative()

class Order:
    qty = NonNegative()</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Minimum method needed for a descriptor?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>__get__</code> &mdash; makes it a non-data descriptor.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What makes a data descriptor vs non-data descriptor?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Data descriptor implements both <code>__get__</code> and <code>__set__</code> (and/or <code>__delete__</code>). Non-data has only <code>__get__</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Where should descriptor data be stored?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">On the <b>instance</b> via <code>obj.__dict__[self.name]</code>, not on the descriptor itself.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>__set_name__</code> is called when?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">When the class body is executed (class definition time) &mdash; automatically receives the attribute name.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> Code after <code>if obj is None: return self</code> in <code>__get__</code> handles what case?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">It handles class-level attribute access: <code>MyClass.attr</code> returns the descriptor itself.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>property</code> is what kind of descriptor?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A <b>data descriptor</b> (implements <code>__get__</code>, <code>__set__</code>, and <code>__delete__</code>).</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Create a @property with validation</li>
  <li>Read about how descriptors power classmethod/staticmethod</li>
</ul>
'''),

(17, "Generators &amp; Iterators", '''
<p>Mentor resource: <a href="https://realpython.com/introduction-to-python-generators/" target="_blank" rel="noopener">Real Python — Generators and yield</a> (PEP 255). Generators return a <b>lazy iterator</b> — you can loop like a list, but contents are <b>not</b> stored all in memory.</p>
<table class="data-tbl">
<tr><th>Approach</th><th>What happens</th><th>Risk on huge CSV</th></tr>
<tr><td><code>file.read().split()</code> → list</td><td>Loads <b>entire</b> file into RAM</td><td><code>MemoryError</code></td></tr>
<tr><td><code>for row in open(...): yield row</code></td><td>One line at a time</td><td>Safe — constant memory</td></tr>
<tr><td>Generator expression <code>(row for row in open(...))</code></td><td>Same lazy idea, shorter syntax</td><td>Safe</td></tr>
</table>
''' + code('''# ── BAD: whole file in memory (can MemoryError on huge files) ──
def csv_reader_naive(file_name):
    with open(file_name, encoding="utf-8") as f:
        return f.read().split("\\n")   # list of ALL lines

# ── GOOD: generator function — yield one row at a time (Real Python) ──
def csv_reader(file_name):
    with open(file_name, encoding="utf-8") as f:
        for row in f:
            yield row                 # pause; resume on next()

# Same idea as a generator expression:
# csv_gen = (row for row in open(file_name, encoding="utf-8"))

# ── yield vs return ──
# return → ends function, gives ONE value
# yield  → returns a generator object; each yield produces one item

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)              # 3, 2, 1

# ── Infinite sequence (only possible with generators) ──
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(next(gen), next(gen), next(gen))   # 0 1 2  — stop manually!

# ── Pipeline: chain generators (process stream without giant lists) ──
def nums():
    for n in range(1, 6):
        yield n

def square(seq):
    for n in seq:
        yield n * n

print(list(square(nums())))   # [1, 4, 9, 16, 25]

# ── Iterator protocol: __iter__ + __next__ ──
class CountUp:
    def __init__(self, max_n):
        self.n = 0
        self.max_n = max_n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n >= self.max_n:
            raise StopIteration
        self.n += 1
        return self.n

import itertools
list(itertools.chain([1, 2], [3, 4]))
list(itertools.islice(countdown(10), 3))''') + '''
<div class="callout"><b>Interview line (Real Python):</b> Generators are lazy iterators — great for data streams and files larger than RAM. <code>yield</code> keeps state between calls; <code>return</code> would end after one value.</div>
<div class="callout">Also: <a href="https://hackernoon.com/the-magic-behind-python-generator-functions-bc8eeea54220" target="_blank" rel="noopener">Generator frame internals</a></div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; trying to iterate a generator twice</span><span class="mistake-desc">A generator is exhausted after one full iteration. A second <code>for</code> loop over the same generator produces nothing.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def evens(n):
    for i in range(n):
        if i % 2 == 0: yield i

gen = evens(10)
print(list(gen))  # [0, 2, 4, 6, 8]
print(list(gen))  # []  ← exhausted!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def evens(n):
    for i in range(n):
        if i % 2 == 0: yield i

# Re-create if you need to iterate again:
print(list(evens(10)))
print(list(evens(10)))  # fresh generator</div></div></div><span class="mistake-note">&#128161; Generators are <b>one-pass</b> iterators. Store the results in a list if you need to iterate multiple times.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; building a full list when a generator suffices</span><span class="mistake-desc">Loading a million items into a list before processing wastes memory. A generator computes items on demand.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def process_all(n):
    return [heavy(i) for i in range(n)]  # builds full list

for result in process_all(1_000_000):
    use(result)</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def process_all(n):
    for i in range(n):
        yield heavy(i)  # one at a time

for result in process_all(1_000_000):
    use(result)   # constant memory</div></div></div><span class="mistake-note">&#128161; Use generators for pipelines where intermediate results are consumed immediately. Use lists when you need random access or multiple passes.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; forgetting <code>yield from</code> for sub-generators</span><span class="mistake-desc">To delegate to another generator or iterable, use <code>yield from</code>. Manual iteration loses the <code>send()</code>/<code>throw()</code> channel.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def combined(a, b):
    for item in a: yield item  # verbose
    for item in b: yield item

# Also misses send/throw/return transparency</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def combined(a, b):
    yield from a  # cleaner, preserves protocol
    yield from b

# yield from also works with any iterable:
yield from range(5)</div></div></div><span class="mistake-note">&#128161; <code>yield from expr</code> is a full two-way channel: it forwards <code>send()</code>, <code>throw()</code>, and captures the sub-generator&apos;s <code>return</code> value.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; List-based (high memory)</div><div class="step-pre">def read_large_file(path):
    with open(path) as f:
        return f.readlines()   # entire file in memory!

for line in read_large_file("huge.log"):
    process(line)</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Generator (streaming)</div><div class="step-pre">def read_large_file(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip()  # one line at a time

for line in read_large_file("huge.log"):
    process(line)</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> What keyword makes a function a generator?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>yield</code> &mdash; any function containing <code>yield</code> returns a generator object when called.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What does a generator raise when all values are yielded?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>StopIteration</code> &mdash; consumed by <code>for</code> loops automatically.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Can you iterate a generator twice without re-creating it?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No &mdash; it is <b>exhausted</b> after the first pass. Re-call the generator function to create a new one.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>range(5)</code> vs <code>list(range(5))</code> — memory?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>range(5)</code> is a lazy object (O(1) memory). <code>list(range(5))</code> allocates all 5 ints in memory.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>yield from iterable</code> does what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Yields each item from <code>iterable</code> one at a time, forwarding <code>send()</code>/<code>throw()</code> transparently.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>next(gen)</code> on exhausted generator raises?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>StopIteration</code> &mdash; or returns the default if supplied: <code>next(gen, 'done')</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> What is a generator expression?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>(expr for x in iterable)</code> &mdash; lazy generator using comprehension syntax without square brackets.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Rewrite a list-returning file reader to use <code>yield</code></li>
  <li>Write a generator expression for squares of 0..999_999 and compare memory to a list</li>
  <li>Build a 2-step generator pipeline (filter → transform)</li>
  <li>Use <code>next()</code> on an infinite generator a few times, then stop</li>
</ul>
'''),

(18, "Decorators", '''
''' + code('''from functools import wraps
import time

# ── DECORATOR = function that wraps another function ──
def timer(fn):
    @wraps(fn)                    # preserve fn.__name__ and __doc__
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{fn.__name__}: {elapsed:.3f}s")
        return result
    return wrapper

def log(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__} with {args} {kwargs}")
        return fn(*args, **kwargs)
    return wrapper

# ── @syntax: @timer above def = slow_work = timer(slow_work) ──
@timer
@log                       # stacked: log wraps first, timer outer
def slow_work():
    return sum(range(500_000))

slow_work()

# ── DECORATOR WITH ARGUMENTS (extra level) ──
def repeat(n):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fn(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")''') + '''
<div class="tip"><code>@wraps(fn)</code> preserves the original function name and docstring — always use it in decorators.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; not using <code>@wraps(func)</code></span><span class="mistake-desc">Without <code>@wraps</code>, the wrapped function loses its original <code>__name__</code>, <code>__doc__</code>, and other metadata.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">import functools

def my_dec(func):
    def wrapper(*args, **kwargs):
        print("before")
        return func(*args, **kwargs)
    return wrapper  # wrapper.__name__ == "wrapper"

@my_dec
def greet(): pass
print(greet.__name__)  # "wrapper" ← wrong</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import functools

def my_dec(func):
    @functools.wraps(func)  # preserves metadata
    def wrapper(*args, **kwargs):
        print("before")
        return func(*args, **kwargs)
    return wrapper

@my_dec
def greet(): pass
print(greet.__name__)  # "greet" ← correct</div></div></div><span class="mistake-note">&#128161; Always add <code>@functools.wraps(func)</code> to the inner <code>wrapper</code>. It also ensures <code>help()</code>, <code>inspect</code>, and FastAPI route introspection work correctly.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; decorator stacking order confusion</span><span class="mistake-desc">Decorators apply <b>bottom-up</b>: the decorator closest to the function is applied first.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">@timer
@logger
def process(): ...

# Applied order:
# process = logger(process)  ← first
# process = timer(process)   ← second (outer)
# Confuse this and your timing/logging wraps incorrectly</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Remember: bottom-up execution
@outer_dec    # applied second — wraps the result of inner_dec
@inner_dec    # applied first — wraps the raw function
def my_func(): ...
# Equivalent to: my_func = outer_dec(inner_dec(my_func))</div></div></div><span class="mistake-note">&#128161; Read stacked decorators from <b>bottom to top</b> to understand application order. The bottom-most decorator is closest to the function.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; forgetting <code>()</code> on a decorator factory</span><span class="mistake-desc">A decorator factory is a function that <b>returns</b> a decorator. You must call it with <code>()</code> even if there are no arguments.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">@retry
def call_api(): ...

# If retry is a decorator FACTORY:
def retry(max=3):
    def decorator(func):
        ...
    return decorator

# @retry without () passes the function to retry()
# and retry() returns a decorator, not a function!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Decorator factory — must use ():
@retry(max=3)
def call_api(): ...

# @retry() ← always needed for factories
# even @retry() with no args if retry is a factory</div></div></div><span class="mistake-note">&#128161; If a decorator accepts configuration arguments, it must be called with <code>()</code>. If not called, the function is passed as the first argument to the factory.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Copy-paste boilerplate</div><div class="step-pre">def create_user(data):
    try:
        return db.insert(data)
    except DBError as e:
        logger.error(e); raise

def update_user(id, data):
    try:                         # same boilerplate!
        return db.update(id, data)
    except DBError as e:
        logger.error(e); raise</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Decorator</div><div class="step-pre">import functools

def db_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DBError as e:
            logger.error(e); raise
    return wrapper

@db_errors
def create_user(data): return db.insert(data)

@db_errors
def update_user(id, data): return db.update(id, data)</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>@decorator</code> is syntactic sugar for?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>func = decorator(func)</code> &mdash; the decorator is called with the function and the result replaces the function name.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> Why use <code>@functools.wraps(func)</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Preserves the wrapped function&apos;s <code>__name__</code>, <code>__doc__</code>, and other attributes on the wrapper.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>@dec1 @dec2 def f():</code> — which decorator is applied first?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>dec2</code> (bottom-up). Equivalent to <code>f = dec1(dec2(f))</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> A decorator factory is?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A function that <b>returns a decorator</b>, e.g. <code>@retry(max=3)</code> &mdash; <code>retry</code> is the factory, <code>retry(max=3)</code> returns the actual decorator.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> What does <code>functools.partial</code> do?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Creates a new function with some arguments <b>pre-filled</b>: <code>add5 = partial(add, 5)</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>@property</code> is itself what kind of object?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A built-in <b>descriptor</b> that turns a method into a computed attribute.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> Can a decorator be applied to a class (not just a function)?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Yes &mdash; <code>@dataclass</code> is a class decorator that modifies the class in place.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Write a @log decorator that prints args</li>
  <li>Stack two decorators on one function</li>
  <li>See how FastAPI uses @app.get() as a decorator</li>
</ul>
'''),

(19, "Exception Handling", '''
''' + code('''# ── TRY / EXCEPT / ELSE / FINALLY ──
try:
    result = int("42")          # works
    print("Converted:", result)
except ValueError as e:
    print(f"Bad input: {e}")    # runs only on ValueError
else:
    print("No error occurred")  # runs if no exception
finally:
    print("Always runs")        # cleanup - always executes

# ── MULTIPLE EXCEPT CLAUSES ──
try:
    value = int("abc")
except ValueError:
    print("Not a valid integer")
except TypeError:
    print("Wrong type")

# ── CUSTOM EXCEPTION ──
class ValidationError(Exception):
    """Raised when input fails business validation."""
    pass

def set_age(age: int) -> int:
    if age < 0:
        raise ValidationError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValidationError(f"Age unrealistic: {age}")
    return age

try:
    set_age(-5)
except ValidationError as e:
    print("Validation failed:", e)

# ── RE-RAISE: preserve original traceback ──
try:
    set_age(-1)
except ValidationError:
    raise                     # re-raise same exception''') + '''


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; bare <code>except:</code> catches everything</span><span class="mistake-desc">Bare <code>except:</code> catches <code>BaseException</code> including <code>SystemExit</code> and <code>KeyboardInterrupt</code>, preventing clean program shutdown.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">try:
    result = risky()
except:      # catches SystemExit, KeyboardInterrupt!
    pass       # silently swallows ALL exceptions</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">try:
    result = risky()
except ValueError as e:
    logger.warning("Invalid value: %s", e)
except Exception as e:     # catchall for non-system
    logger.error("Unexpected: %s", e)
    raise</div></div></div><span class="mistake-note">&#128161; Use the most specific exception type first. A bare <code>except</code> should only appear in top-level error boundaries (CLI entry points) and always re-raises or logs.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; <code>raise e</code> vs <code>raise</code> (traceback loss)</span><span class="mistake-desc"><code>raise e</code> in an except block <b>resets the traceback</b> to the current line. <code>raise</code> alone preserves the original location.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">try:
    risky()
except Exception as e:
    raise e   # traceback starts HERE — original lost!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">try:
    risky()
except Exception as e:
    logger.error(e)
    raise     # re-raises with ORIGINAL traceback preserved</div></div></div><span class="mistake-note">&#128161; Use bare <code>raise</code> to re-raise. If you need to raise a different exception, use <code>raise NewError(...) from e</code> to chain them.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; catching too broadly and swallowing errors</span><span class="mistake-desc"><code>except Exception: pass</code> silently discards errors, making debugging nearly impossible.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def load_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        pass   # all errors silently ignored!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">def load_config(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}   # expected: file not created yet
    except json.JSONDecodeError as e:
        raise ValueError(f"Bad config: {path}") from e</div></div></div><span class="mistake-note">&#128161; Only catch exceptions you can <b>handle meaningfully</b>. Let unexpected exceptions propagate so they can be fixed.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Swallowing exceptions</div><div class="step-pre">def get_user(id):
    try:
        return db.query(id)
    except:
        return None   # was it NotFound? DBDown? TypeError?
                      # impossible to tell!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Precise handling</div><div class="step-pre">class NotFoundError(Exception): pass

def get_user(id):
    try:
        return db.query(id)
    except db.NotFound:
        raise NotFoundError(f"User {id} not found")
    except db.ConnectionError:
        raise  # re-raise — caller handles infra errors</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>except Exception</code> vs bare <code>except:</code> — what extra does bare catch?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Bare <code>except:</code> also catches <code>SystemExit</code>, <code>KeyboardInterrupt</code>, and <code>GeneratorExit</code> (all <code>BaseException</code> subclasses).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>raise</code> vs <code>raise e</code> in an except block?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>raise</code> preserves the original traceback. <code>raise e</code> resets the traceback origin to the current line.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>finally</code> block runs when?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Always &mdash; whether an exception was raised, caught, or not. Even after a <code>return</code> in the <code>try</code> block.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>except (TypeError, ValueError):</code> catches?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Either <code>TypeError</code> or <code>ValueError</code> &mdash; any of the listed exception types.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> Custom exception should inherit from?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>Exception</code> (not <code>BaseException</code>), so it&apos;s caught by <code>except Exception:</code> but not by bare <code>except:</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>raise NewError('msg') from original_err</code> does what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Raises <code>NewError</code> while <b>chaining</b> the original exception, preserving both tracebacks in the output.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> What is exception chaining? How to suppress it?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Automatic when an exception is raised inside an except block. Suppress with <code>raise NewError() from None</code>.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Catch specific exceptions, not bare except</li>
  <li>Create a custom exception class</li>
  <li>Use try/finally for cleanup</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyExceptionHandling/">MyExceptionHandling</a>
'''),

(20, "Threading &amp; GIL", '''
<div class="callout"><b>GIL:</b> Global Interpreter Lock — only one thread runs Python bytecode at a time. Good for I/O-bound tasks; use multiprocessing for CPU-bound work.</div>
''' + code('''import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# ── GIL: only one thread runs Python bytecode at a time ──
# Good for I/O-bound (network, disk) | Bad for CPU-bound (math)

counter = 0
lock = threading.Lock()

def unsafe_increment():
    global counter
    counter += 1              # race condition without lock

def safe_increment():
    global counter
    with lock:                # only one thread at a time
        counter += 1

# ── THREADS: lightweight, shared memory ──
threads = [threading.Thread(target=safe_increment) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()                  # wait for all to finish
print("Counter:", counter)    # 100

# ── ThreadPoolExecutor: pool for I/O tasks ──
def fetch(url_id):
  time.sleep(0.1)               # simulate network I/O
  return f"data-{url_id}"

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, range(8)))
print(results)

# CPU-bound heavy math → use ProcessPoolExecutor instead''') + '''


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; using threads for CPU-bound tasks (GIL blocks parallelism)</span><span class="mistake-desc">The GIL allows only one thread to execute Python bytecode at a time. Threads do <b>not</b> speed up CPU-bound work.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">from threading import Thread

def crunch(n):
    return sum(i**2 for i in range(n))

t1 = Thread(target=crunch, args=(10**7,))
t2 = Thread(target=crunch, args=(10**7,))
t1.start(); t2.start()
t1.join(); t2.join()
# NOT faster than sequential due to GIL</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from multiprocessing import Pool

def crunch(n):
    return sum(i**2 for i in range(n))

with Pool(2) as p:
    results = p.map(crunch, [10**7, 10**7])
# Truly parallel — each process has its own GIL</div></div></div><span class="mistake-note">&#128161; Use <code>threading</code> for I/O-bound tasks (network, file, DB). Use <code>multiprocessing</code> or <code>concurrent.futures.ProcessPoolExecutor</code> for CPU-bound work.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; shared mutable state without a <code>Lock</code></span><span class="mistake-desc">Two threads incrementing a shared counter without a lock produce a race condition &mdash; the result is non-deterministic.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">import threading
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # read-modify-write is not atomic!

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()
print(counter)  # not always 200000!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import threading
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1  # protected

# Now counter == 200000 always</div></div></div><span class="mistake-note">&#128161; Any shared mutable state accessed by multiple threads requires a <code>Lock</code>. Prefer <code>threading.local()</code> or <code>queue.Queue</code> to avoid shared state entirely.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; not joining threads before using their results</span><span class="mistake-desc">If the main thread proceeds before worker threads finish, results may be incomplete or incorrect.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">results = []
t = threading.Thread(target=lambda: results.append(compute()))
t.start()
print(results)  # [] — thread hasn't finished yet!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">results = []
t = threading.Thread(target=lambda: results.append(compute()))
t.start()
t.join()         # wait for thread to finish
print(results)  # [computed_value]</div></div></div><span class="mistake-note">&#128161; Always <code>.join()</code> threads before using their results. Use <code>concurrent.futures.ThreadPoolExecutor</code> for cleaner result collection.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; No lock (race condition)</div><div class="step-pre">balance = 1000

def withdraw(amount):
    global balance
    if balance >= amount:
        # gap here — another thread can run!
        balance -= amount

# Two threads withdrawing simultaneously
# can overdraft the account!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; With Lock (thread-safe)</div><div class="step-pre">import threading
balance = 1000
lock = threading.Lock()

def withdraw(amount):
    global balance
    with lock:          # atomic section
        if balance >= amount:
            balance -= amount
            return True
    return False</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> What is the GIL?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The <b>Global Interpreter Lock</b> &mdash; a mutex that allows only one thread to execute Python bytecode at a time.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> Threads are best for?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><b>I/O-bound</b> tasks (network requests, file reads) where threads wait rather than compute.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>multiprocessing</code> is better for?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><b>CPU-bound</b> tasks &mdash; each process gets its own GIL and can run in true parallel.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> What is a race condition?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Two threads read and modify shared data simultaneously, producing non-deterministic results.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>thread.join()</code> does what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Blocks the calling thread until the target thread <b>finishes</b>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>threading.Lock()</code> purpose?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Ensures only <b>one thread</b> at a time can execute the protected code block.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>queue.Queue</code> is thread-safe — why prefer it over a list?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>Queue</code> has internal locking; a plain <code>list</code> does not. <code>.put()</code>/<code>.get()</code> are atomic.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Run two threads that share a counter with Lock</li>
  <li>Explain when to use threading vs multiprocessing</li>
  <li>Try ThreadPoolExecutor with 4 workers</li>
</ul>
'''),

(21, "Async / Await", '''
''' + code('''import asyncio
import time

# ── COROUTINE: async def defines a coroutine function ──
async def fetch_data(n):
    await asyncio.sleep(0.5)    # non-blocking wait (simulates I/O)
    return f"result-{n}"

# ── SEQUENTIAL: one after another (~1.5 sec) ──
async def sequential():
    r1 = await fetch_data(1)
    r2 = await fetch_data(2)
    r3 = await fetch_data(3)
    return [r1, r2, r3]

# ── CONCURRENT: asyncio.gather runs together (~0.5 sec) ──
async def concurrent():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
    )
    return results

async def main():
    start = time.time()
    results = await concurrent()
    print("Results:", results)
    print(f"Time: {time.time()-start:.2f}s")  # ~0.5s not 1.5s

# Start the event loop
asyncio.run(main())

# Rules:
# - await only inside async def
# - asyncio.run() starts the event loop
# - Use async for I/O (HTTP, DB), not CPU-heavy math''') + '''
<div class="tip">Use async for I/O-bound concurrency (HTTP, DB, files). Do not use for CPU-heavy work — use multiprocessing instead.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; calling a coroutine without <code>await</code></span><span class="mistake-desc">Calling an <code>async def</code> function without <code>await</code> returns a <b>coroutine object</b> &mdash; the function body does <b>not</b> run.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">import asyncio

async def fetch():
    return "data"

result = fetch()   # coroutine object — not executed!
print(result)      # &lt;coroutine object fetch at 0x...&gt;</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import asyncio

async def fetch():
    return "data"

async def main():
    result = await fetch()  # now it runs
    print(result)           # "data"

asyncio.run(main())</div></div></div><span class="mistake-note">&#128161; If you forget <code>await</code>, Python will typically warn: <em>RuntimeWarning: coroutine &lsquo;fetch&rsquo; was never awaited</em>.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; using blocking calls inside <code>async def</code></span><span class="mistake-desc">Blocking operations (like <code>time.sleep()</code> or <code>requests.get()</code>) freeze the <b>entire event loop</b>, preventing all other coroutines from running.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">import asyncio, time

async def slow_fetch():
    time.sleep(2)    # BLOCKS the event loop!
    return "data"</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import asyncio, httpx

async def slow_fetch():
    await asyncio.sleep(2)   # yields control
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://api.example.com")
    return resp.json()</div></div></div><span class="mistake-note">&#128161; Use async-native libraries: <code>httpx</code> or <code>aiohttp</code> (not <code>requests</code>), <code>asyncio.sleep()</code> (not <code>time.sleep()</code>), async DB drivers.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; <code>asyncio.run()</code> inside an already running event loop</span><span class="mistake-desc">In Jupyter notebooks and some frameworks, an event loop is already running. Calling <code>asyncio.run()</code> raises <code>RuntimeError</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># In Jupyter notebook:
async def main(): return "done"
asyncio.run(main())
# RuntimeError: This event loop is already running</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># In Jupyter — use await directly:
result = await main()   # no asyncio.run() needed

# In scripts:
asyncio.run(main())     # correct for script entry point</div></div></div><span class="mistake-note">&#128161; In Jupyter, use <code>await</code> directly in cells. In FastAPI, define route handlers as <code>async def</code> and the framework manages the loop.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Blocking in async context</div><div class="step-pre">import time
import asyncio

async def process_items(items):
    results = []
    for item in items:
        time.sleep(0.1)        # blocks loop!
        results.append(item * 2)
    return results</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Non-blocking with gather</div><div class="step-pre">import asyncio

async def process_item(item):
    await asyncio.sleep(0.1)   # yields
    return item * 2

async def process_items(items):
    tasks = [process_item(x) for x in items]
    return await asyncio.gather(*tasks)  # concurrent</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Calling <code>async def f():</code> without <code>await</code> returns?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A <b>coroutine object</b> &mdash; the function body does not run. Python warns: <em>coroutine was never awaited</em>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>await f()</code> — what does <code>await</code> do?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Suspends the current coroutine, yields control to the event loop, and resumes when <code>f()</code> completes.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> How to run a coroutine from synchronous code?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>asyncio.run(coroutine())</code> &mdash; creates an event loop, runs the coroutine, and closes the loop.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>time.sleep()</code> vs <code>asyncio.sleep()</code> in async code?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>asyncio.sleep()</code> <b>yields</b> to the event loop (non-blocking). <code>time.sleep()</code> blocks the entire loop.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>asyncio.gather(*tasks)</code> does what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Runs multiple coroutines <b>concurrently</b> and returns all results when all finish.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> What is the event loop?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A scheduler that manages and runs async tasks &mdash; one coroutine runs at a time but others are resumed when awaited operations complete.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>async for</code> is used with?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Async iterables &mdash; objects implementing <code>__aiter__</code> and <code>__anext__</code>, e.g. async DB cursors, SSE streams.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Write async def with two await calls</li>
  <li>Compare sequential vs asyncio.gather timing</li>
  <li>See async patterns in Pipecat voice pipeline</li>
</ul>
<a class="file-link" href="Python-Set2/Pipecat-Project/">Pipecat-Project</a>
'''),

(22, "Logging", '''
<p>Use the <code>logging</code> module instead of <code>print()</code> in production — levels, timestamps, and handlers map cleanly to observability tools (like Serilog / ILogger in C#).</p>
<table class="ref-table">
<tr><th>Level</th><th>When to use</th></tr>
<tr><td>DEBUG</td><td>Verbose dev detail — off in production usually</td></tr>
<tr><td>INFO</td><td>Normal lifecycle events (startup, request handled)</td></tr>
<tr><td>WARNING</td><td>Something unexpected but recoverable</td></tr>
<tr><td>ERROR</td><td>Operation failed — app continues</td></tr>
<tr><td>CRITICAL</td><td>Serious failure — may abort</td></tr>
</table>
''' + code('''import logging
from logging.handlers import RotatingFileHandler

# ── Basic setup ──
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

log.debug("won't show at INFO level")
log.info("Server started")
log.warning("Disk 85% full")
log.error("Payment gateway timeout", exc_info=False)

# ── Module logger (preferred) ──
logger = logging.getLogger("orders.service")

def charge(order_id: int) -> None:
    logger.info("Charging order %s", order_id)
    try:
        ...
    except TimeoutError:
        logger.exception("Charge failed for %s", order_id)  # includes traceback

# ── File + rotation ──
handler = RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=3)
handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
logger.addHandler(handler)''') + '''
<div class="callout"><b>Rule:</b> <code>logger.info("x=%s", x)</code> — lazy formatting. Avoid f-strings in log calls when the message might be filtered out.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; using <code>print()</code> for application logs</span><span class="mistake-desc"><code>print()</code> has no level, no timestamp, no handler routing, and goes to stdout only. Production code needs structured logging.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">def process(order_id):
    print(f"Processing order {order_id}")
    print(f"ERROR: order not found")  # no severity, no timestamp
    # no way to filter, route, or correlate</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import logging
logger = logging.getLogger(__name__)

def process(order_id):
    logger.info("Processing order %s", order_id)
    logger.error("Order not found: %s", order_id)</div></div></div><span class="mistake-note">&#128161; <code>getLogger(__name__)</code> creates a logger named after the module, making it easy to filter logs by module in production.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; using f-strings in log calls (eager formatting)</span><span class="mistake-desc">F-strings evaluate eagerly even if the log level is disabled. Use <code>%</code>-style args so the message is only formatted if actually logged.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">logger.debug(f"Processing {len(items)} items")  # f-string always evaluated
# Even at WARNING level, len(items) is computed!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">logger.debug("Processing %d items", len(items))
# len(items) only called if DEBUG is enabled</div></div></div><span class="mistake-note">&#128161; This optimization matters in hot code paths. <code>%</code>-style also lets <code>logging</code> include the raw args in <code>LogRecord</code> for structured log handlers.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; not configuring a handler (no output appears)</span><span class="mistake-desc">If you create a logger but don&apos;t configure a handler, log messages silently disappear.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">import logging
logger = logging.getLogger("myapp")
logger.warning("Test")  # nothing appears!
# Because no handler is attached</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)
logger.info("App started")</div></div></div><span class="mistake-note">&#128161; For quick setup, <code>logging.basicConfig()</code> adds a <code>StreamHandler</code> to the root logger. For production, configure file or structured JSON handlers explicitly.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Print statements</div><div class="step-pre">def load_config(path):
    print(f"Loading config from {path}")
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        print(f"ERROR: {e}")</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Proper logging</div><div class="step-pre">import logging
logger = logging.getLogger(__name__)

def load_config(path):
    logger.debug("Loading config from %s", path)
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning("Config not found: %s", path)
        return {}</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> 5 standard log levels from lowest to highest?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">DEBUG &lt; INFO &lt; WARNING &lt; ERROR &lt; CRITICAL.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> Default log level if not configured?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>WARNING</code> &mdash; messages below WARNING (DEBUG, INFO) are suppressed unless the level is lowered.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Difference between module logger and root logger?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Module logger (<code>getLogger(__name__)</code>) is named and per-module; messages propagate to root unless propagation is disabled.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>%(asctime)s</code> in a format string includes?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The <b>timestamp</b> of the log record.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>logger.exception(e)</code> vs <code>logger.error(e)</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>exception()</code> also logs the <b>full traceback</b>. Use it inside an <code>except</code> block.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> Why use <code>%s</code>-style over f-strings in log calls?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Lazy evaluation &mdash; the string is only formatted if the message will actually be emitted at that log level.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>logging.basicConfig()</code> must be called before?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Before the first <code>getLogger()</code> call that produces output. Calling it after has no effect if the root logger already has handlers.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Replace <code>print</code> with <code>logging</code> in one practice script</li>
  <li>Configure DEBUG to console and INFO to file</li>
  <li>Use <code>logger.exception()</code> inside an <code>except</code> block once</li>
</ul>
'''),

(23, "Unit Testing", '''
''' + code('''# ── PYTEST STYLE (recommended) ──
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)

# Run: pytest test_file.py -v

# ── UNITTEST STYLE (built-in) ──
import unittest
from unittest.mock import patch, MagicMock

class TestMath(unittest.TestCase):
    def setUp(self):
        self.n = 10           # runs before EACH test

    def tearDown(self):
        pass                  # runs after EACH test

    def test_double(self):
        self.assertEqual(self.n * 2, 20)

    def test_is_positive(self):
        self.assertTrue(self.n > 0)

# ── MOCK: isolate from external dependencies ──
@patch("builtins.print")
def test_mock_print(mock_print):
    print("hello")
    mock_print.assert_called_once_with("hello")''') + '''
<div class="tip">Test order: setUp → test method → tearDown, repeated per test method in the class.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; tests with shared state (order-dependent tests)</span><span class="mistake-desc">Tests that depend on execution order or shared state are fragile. Each test must be fully independent.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class TestDB(unittest.TestCase):
    db = Database()  # shared across tests!

    def test_insert(self):
        self.db.insert({"id": 1})

    def test_count(self):
        self.assertEqual(self.db.count(), 1)  # only passes if test_insert ran first!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">class TestDB(unittest.TestCase):
    def setUp(self):          # fresh state per test
        self.db = Database()

    def test_insert(self):
        self.db.insert({"id": 1})

    def test_count(self):
        self.db.insert({"id": 1})
        self.assertEqual(self.db.count(), 1)  # self-contained</div></div></div><span class="mistake-note">&#128161; <code>setUp()</code> runs before each test method, creating fresh state. <code>tearDown()</code> runs after each, cleaning up.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; making real HTTP/DB calls in unit tests</span><span class="mistake-desc">Unit tests must be fast and isolated. Real external calls make tests slow, flaky, and dependent on network/DB availability.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class TestUserService(unittest.TestCase):
    def test_get_user(self):
        # makes a real HTTP call!
        service = UserService()
        user = service.get_user(1)
        self.assertEqual(user["name"], "Anu")</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from unittest.mock import patch, MagicMock

class TestUserService(unittest.TestCase):
    @patch("myapp.services.requests.get")
    def test_get_user(self, mock_get):
        mock_get.return_value.json.return_value = {"name": "Anu"}
        user = UserService().get_user(1)
        self.assertEqual(user["name"], "Anu")</div></div></div><span class="mistake-note">&#128161; Use <code>unittest.mock.patch</code> to replace external dependencies with <code>MagicMock</code>. Tests run offline and in milliseconds.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; <code>assertTrue(a == b)</code> instead of <code>assertEqual(a, b)</code></span><span class="mistake-desc"><code>assertEqual</code> produces a much more informative failure message showing both values.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">self.assertTrue(result == 42)
# On failure: "AssertionError: False is not True"
# No information about what result actually was!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">self.assertEqual(result, 42)
# On failure: "AssertionError: 38 != 42"
# Clear — you see both values immediately</div></div></div><span class="mistake-note">&#128161; Use the most specific assertion method: <code>assertEqual</code>, <code>assertIn</code>, <code>assertRaises</code>, <code>assertIsNone</code>, etc. Better failure messages speed up debugging.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; No mock (slow, fragile)</div><div class="step-pre">def test_send_email():
    service = EmailService(smtp_host="smtp.gmail.com")
    result = service.send("test@test.com", "Hi")
    # Makes real SMTP connection!
    # Fails if network is down
    assert result is True</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Mocked (fast, isolated)</div><div class="step-pre">from unittest.mock import patch

def test_send_email():
    with patch("myapp.smtplib.SMTP") as mock_smtp:
        mock_smtp.return_value.__enter__.return_value\\
            .sendmail.return_value = {}
        service = EmailService(smtp_host="host")
        result = service.send("test@test.com", "Hi")
    assert result is True</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>unittest.TestCase</code> method to assert equality?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>assertEqual(a, b)</code> &mdash; fails with a detailed message showing both values.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>@patch('module.func')</code> does what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Replaces <code>func</code> in <code>module</code>&apos;s namespace with a <code>MagicMock</code> for the duration of the test.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>setUp()</code> runs when?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Before <b>each</b> test method in the class.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>tearDown()</code> runs when?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">After <b>each</b> test method &mdash; even if the test fails.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>self.assertRaises(ValueError)</code> — how to use it?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">As a context manager: <code>with self.assertRaises(ValueError): risky()</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> What is a test fixture?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The fixed baseline state (files, DB rows, objects) set up before tests run and torn down after.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>MagicMock().return_value</code> controls what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">What the mock returns when <b>called</b>: <code>mock_fn.return_value = 42</code> makes <code>mock_fn()</code> return <code>42</code>.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Write 3 pytest tests for one function</li>
  <li>Mock an external API call with @patch</li>
  <li>Run pytest in MyUnitTesting/</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyUnitTesting/">MyUnitTesting</a>
'''),

(24, "Regular Expressions", '''
''' + code('''import re

text = "Order 123 placed on 2026-06-16. Contact: alice@example.com"

# ── COMMON PATTERNS ──
# \\d  = digit        \\w  = word char    \\s  = whitespace
# \\D  = non-digit    \\W  = non-word     \\S  = non-space
# +    = one or more  *    = zero or more  ?  = optional
# []   = character class   () = capture group

# ── search: first match anywhere ──
m = re.search(r"\\d+", text)
print(m.group())              # '123'

# ── findall: all matches as list ──
print(re.findall(r"\\d+", text))   # ['123','2026','06','16']

# ── match: only at START of string ──
print(re.match(r"Order", text))    # match object
print(re.match(r"123", text))      # None - not at start

# ── GROUPS: capture parts in parentheses ──
m = re.search(r"(\\d{4})-(\\d{2})-(\\d{2})", "2026-06-16")
print(m.group(0))   # full match: 2026-06-16
print(m.group(1))   # 2026 (year)
print(m.group(2))   # 06   (month)
print(m.group(3))   # 16   (day)

# ── sub: replace matches ──
print(re.sub(r"\\d+", "X", text))  # mask all numbers

# ── EMAIL extraction ──
emails = re.findall(r"[\\w.+-]+@[\\w-]+\\.[\\w.-]+", text)
print(emails)  # ['alice@example.com']''') + '''
<div class="challenge"><b>Interview favorite:</b> babynames exercise — parse baby name files with regex and count frequencies.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; <code>re.match()</code> vs <code>re.search()</code> confusion</span><span class="mistake-desc"><code>re.match()</code> only matches at the <b>start</b> of the string. <code>re.search()</code> scans the whole string.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">import re

text = "Order 42 received"
m = re.match(r'\\d+', text)
print(m)  # None — no digit at position 0!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import re

text = "Order 42 received"
m = re.search(r'\\d+', text)
print(m.group())  # "42" — found anywhere</div></div></div><span class="mistake-note">&#128161; Use <code>re.match()</code> only when the pattern must appear at the beginning. Use <code>re.search()</code> when the position is unknown.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; not using raw strings for regex patterns</span><span class="mistake-desc">Without raw strings, backslashes need double-escaping. <code>'\\d'</code> is a literal <code>d</code> (since <code>\\d</code> is not a Python escape), but <code>'\\n'</code> is a newline &mdash; inconsistent.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">import re
# \\b is a backspace in normal Python string!
re.search("\\bword\\b", text)
# To match word boundary, need double backslash:
re.search("\\\\bword\\\\b", text)</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">import re
# Raw string r"..." — backslashes are literal:
re.search(r"\\bword\\b", text)   # correct
re.search(r"\\d{3}-\\d{4}", text)  # phone pattern</div></div></div><span class="mistake-note">&#128161; Always use raw strings (<code>r"..."</code>) for regex patterns. It prevents accidental escape interpretation.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; greedy vs non-greedy matching</span><span class="mistake-desc"><code>.*</code> is greedy and matches as much as possible. Use <code>.*?</code> (non-greedy) to stop at the first match.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">html = "<b>bold</b> and <i>italic</i>"
m = re.search(r"<.*>", html)
print(m.group())  # "<b>bold</b> and <i>italic</i>"
# greedy — matches from first < to last ></div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">html = "<b>bold</b> and <i>italic</i>"
m = re.search(r"<.*?>", html)  # non-greedy
print(m.group())  # "<b>"
# stops at the first ></div></div></div><span class="mistake-note">&#128161; Add <code>?</code> after a quantifier to make it non-greedy: <code>+?</code>, <code>*?</code>, <code>{n,m}?</code>.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; String manipulation</div><div class="step-pre"># Extract all numbers from a log line
line = "ERROR 2026-07-29 code=404 retries=3"
numbers = []
for part in line.split():
    if part.replace("-","").isdigit():
        numbers.append(part)
# Fragile — misses "code=404"</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Regex</div><div class="step-pre">import re

line = "ERROR 2026-07-29 code=404 retries=3"
numbers = re.findall(r'\\d+', line)
print(numbers)  # ['2026', '07', '29', '404', '3']</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>re.match(r'\\d+', '42abc')</code> vs <code>re.search(r'\\d+', 'abc42')</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>match</code> anchors to the start &mdash; matches <code>'42'</code>. <code>search</code> scans anywhere &mdash; matches <code>'42'</code> in <code>'abc42'</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>r'\\d'</code> matches?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Any decimal digit 0&ndash;9 (<code>\\d</code> = <code>[0-9]</code>).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>re.findall(r'\\d+', 'a1b22c3')</code> &mdash; result?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>['1', '22', '3']</code> &mdash; returns all non-overlapping matches as strings.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>.group(0)</code> returns?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The <b>entire match</b>. <code>.group(1)</code> returns the first captured group.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>re.sub(r'\\s+', ' ', text)</code> does?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Replaces one or more whitespace characters with a single space &mdash; normalises whitespace.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> Raw string <code>r'\\n'</code> vs regular <code>'\\n'</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>r'\\n'</code> is two characters (backslash + n). <code>'\\n'</code> is a newline character.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>re.compile(pattern)</code> — why use it?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Compiles the regex once for reuse. Faster when the same pattern is applied many times in a loop.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Extract all emails from a string with regex</li>
  <li>Use groups to parse a date</li>
  <li>Complete babynames/ exercise</li>
</ul>
<a class="file-link" href="Python-Set2/google-python-exercises/babynames/">babynames</a>
'''),

(25, "File Operations", '''
''' + code('''# ── TEXT FILE: write then read ──
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\\n")
    f.write("Line 2\\n")
# file auto-closed here (even if error)

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()          # entire file as string
    print(content)

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:              # line by line (memory efficient)
        print(line.strip())

# ── JSON: Python dict ↔ JSON string ──
import json
data = {"name": "Alice", "score": 95, "active": True}
json_str = json.dumps(data, indent=2)    # dict → string
parsed = json.loads('{"a": 1, "b": 2}')  # string → dict

with open("data.json", "w") as f:
    json.dump(data, f)          # dict → file

with open("data.json", "r") as f:
    loaded = json.load(f)       # file → dict

# ── pathlib: modern path handling ──
from pathlib import Path
root = Path("Python-Set2")
csv_file = root / "pandas" / "titanic.csv"
print(csv_file.exists())
print(list(Path("Projects").glob("*.py")))  # all .py files''') + '''


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; opening files without <code>with</code></span><span class="mistake-desc">Without <code>with</code>, the file stays open if an exception occurs before the explicit <code>.close()</code>.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">f = open("data.txt")
data = f.read()
# If exception here, f.close() never runs
# File descriptor leaked!
f.close()</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">with open("data.txt", encoding="utf-8") as f:
    data = f.read()
# File closed automatically even if exception raised</div></div></div><span class="mistake-note">&#128161; <code>with</code> calls <code>file.__exit__()</code> which closes the file handle regardless of exceptions.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; not specifying <code>encoding</code></span><span class="mistake-desc">Default encoding is platform-dependent (<code>cp1252</code> on Windows, <code>utf-8</code> on Linux). Omitting it causes <code>UnicodeDecodeError</code> on non-ASCII files.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">with open("data.txt") as f:
    data = f.read()
# Works on Linux (utf-8 default)
# UnicodeDecodeError on Windows with non-ASCII chars!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">with open("data.txt", encoding="utf-8") as f:
    data = f.read()
# Consistent across all platforms</div></div></div><span class="mistake-note">&#128161; Always specify <code>encoding='utf-8'</code> for text files. Use <code>encoding='utf-8-sig'</code> to handle BOM in files saved by Excel/Notepad.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; loading an entire large file into memory</span><span class="mistake-desc">Reading a huge file with <code>f.read()</code> or <code>f.readlines()</code> allocates everything at once. Iterate line by line instead.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">with open("huge.log", encoding="utf-8") as f:
    lines = f.readlines()   # entire file in memory!
for line in lines:
    process(line)</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">with open("huge.log", encoding="utf-8") as f:
    for line in f:            # streaming, O(1) memory
        process(line.rstrip())</div></div></div><span class="mistake-note">&#128161; File objects are iterable. <code>for line in f:</code> reads one line at a time without loading the whole file.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; No encoding, no context manager</div><div class="step-pre">f = open("report.txt", "w")
f.write("Sales: 100\\n")
f.write("Returns: 5\\n")
f.close()  # missing if exception raised</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Safe, explicit</div><div class="step-pre">with open("report.txt", "w", encoding="utf-8") as f:
    f.write("Sales: 100\\n")
    f.write("Returns: 5\\n")
# closed automatically, correct encoding</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>open(file, 'r')</code> vs <code>open(file, 'w')</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>'r'</code> reads (error if not found). <code>'w'</code> writes and <b>overwrites</b> existing content.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>open(file, 'a')</code> mode does?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Opens for writing and <b>appends</b> to the end; does not truncate existing content.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Recommended way to open files?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>with open(..., encoding='utf-8') as f:</code> &mdash; auto-closes and handles exceptions.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>f.readline()</code> vs <code>f.readlines()</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>readline()</code> reads one line. <code>readlines()</code> reads <b>all lines</b> into a list.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>json.dump(data, f)</code> vs <code>json.dumps(data)</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>dump</code> writes to a file object. <code>dumps</code> returns a <b>string</b>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> How to iterate a file line by line without loading all into memory?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>for line in f:</code> &mdash; file objects are iterable and stream one line at a time.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>pathlib.Path('dir').glob('*.py')</code> returns?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">A generator yielding <code>Path</code> objects for all <code>.py</code> files in the directory.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Read and write a text file with with</li>
  <li>Parse a JSON file</li>
  <li>Use pathlib to list .py files in a folder</li>
</ul>
<a class="file-link" href="Python-Set2/google-python-exercises/copyspecial/">copyspecial</a>
<a class="file-link" href="Python-Set2/pandas/titanic.csv">titanic.csv</a>
'''),

(26, "Context Manager", '''
''' + code('''from contextlib import contextmanager
import time

# ── BUILT-IN: with open() auto-closes file ──
with open("temp.txt", "w") as f:
    f.write("Hello")
# f closed here automatically

# ── @contextmanager: generator-based ──
@contextmanager
def tag(name):
    print(f"<{name}>")        # setup (before yield)
    yield                     # body of with block runs here
    print(f"</{name}>")       # teardown (after yield)

with tag("h1"):
    print("Hello World")
# prints: <h1> Hello World </h1>

@contextmanager
def timer(label):
    start = time.time()
    yield
    print(f"{label}: {time.time()-start:.3f}s")

with timer("calculation"):
    sum(range(1_000_000))

# ── CLASS-BASED context manager ──
class Managed:
    def __enter__(self):
        print("  setup")
        return self             # value assigned to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  teardown")
        return False            # False = don't suppress exceptions

with Managed() as m:
    print("  working")''') + '''


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; <code>__exit__</code> returning <code>True</code> suppresses ALL exceptions</span><span class="mistake-desc">If <code>__exit__</code> returns <code>True</code>, any exception raised in the <code>with</code> block is silently swallowed.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">class SuppressAll:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, tb):
        return True  # ALL exceptions silently suppressed!

with SuppressAll():
    1 / 0   # ZeroDivisionError — gone!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">class MyCtx:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, tb):
        if exc_type is ValueError:
            log.warning(exc_val)
            return True   # only suppress ValueError
        return False  # other exceptions propagate</div></div></div><span class="mistake-note">&#128161; Return <code>True</code> <em>only</em> for the specific exception types you intend to suppress. Use <code>contextlib.suppress(ErrorType)</code> for clean single-exception suppression.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; forgetting <code>yield</code> in a <code>@contextmanager</code></span><span class="mistake-desc">A <code>@contextmanager</code> generator must have exactly one <code>yield</code>. Without it, <code>RuntimeError</code> is raised.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">from contextlib import contextmanager

@contextmanager
def managed():
    setup()
    # forgot yield
    teardown()

with managed() as m:  # RuntimeError!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from contextlib import contextmanager

@contextmanager
def managed():
    setup()
    try:
        yield             # hands control to the with-block
    finally:
        teardown()        # runs even if exception raised</div></div></div><span class="mistake-note">&#128161; Wrap the <code>yield</code> in <code>try/finally</code> to guarantee cleanup even when the body raises an exception.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; nesting multiple context managers verbosely</span><span class="mistake-desc">Multiple nested <code>with</code> statements can be combined on one line.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">with open("in.txt", encoding="utf-8") as src:
    with open("out.txt", "w", encoding="utf-8") as dst:
        dst.write(src.read())</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Single with, comma-separated:
with (open("in.txt", encoding="utf-8") as src,
      open("out.txt", "w", encoding="utf-8") as dst):
    dst.write(src.read())</div></div></div><span class="mistake-note">&#128161; Python 3.10+ supports parenthesized context managers. Python 3.1+ supports comma-separated on one line.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Manual resource management</div><div class="step-pre">conn = db.connect()
try:
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
finally:
    conn.close()   # must remember this!</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; @contextmanager</div><div class="step-pre">from contextlib import contextmanager

@contextmanager
def db_connection(url):
    conn = db.connect(url)
    try:
        yield conn
    finally:
        conn.close()

with db_connection(URL) as conn:
    conn.cursor().execute("SELECT 1")</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>__enter__</code> returns?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The value bound to the <code>as</code> variable in the <code>with</code> statement.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>__exit__</code> receives which 3 exception-related args?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>exc_type</code>, <code>exc_val</code>, <code>exc_tb</code> &mdash; all <code>None</code> if no exception was raised.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>__exit__</code> returning <code>True</code> does?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Suppresses the exception &mdash; the code after the <code>with</code> block continues normally.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> <code>@contextlib.contextmanager</code> requires?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Exactly one <code>yield</code> in the generator function body.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> Code after <code>yield</code> in a <code>@contextmanager</code> runs?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">In the <code>__exit__</code> phase &mdash; after the <code>with</code> block body finishes (cleanup code).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> <code>contextlib.suppress(FileNotFoundError)</code> does what?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Creates a context manager that silently ignores <code>FileNotFoundError</code> if raised inside the block.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Write @contextmanager for timing code blocks</li>
  <li>Implement __enter__/__exit__ class</li>
  <li>Explain how with calls __exit__ on exception</li>
</ul>
'''),

(27, "Virtual Environment", '''
''' + code('''# ── CREATE virtual environment ──
# python -m venv .venv
# Creates: .venv/Scripts/python.exe  (Windows)
#          .venv/Lib/site-packages/  (isolated packages)

# ── ACTIVATE (Windows PowerShell) ──
# .venv\\Scripts\\activate
# Prompt shows (.venv) prefix

# ── ACTIVATE (Mac/Linux) ──
# source .venv/bin/activate

# ── INSTALL packages inside venv ──
# pip install requests pandas pytest django

# ── SAVE exact versions to file ──
# pip freeze > requirements.txt
# Example requirements.txt:
# pytest==8.0.0
# requests==2.31.0

# ── INSTALL from requirements (reproducible) ──
# pip install -r requirements.txt

# ── DEACTIVATE when done ──
# deactivate

# ── CHECK which Python is active ──
import sys
print(sys.executable)   # shows path to current Python''') + '''
<div class="callout">Every Python-Set2 project should use its own venv. Never commit <code>venv/</code> to git — add to .gitignore.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; installing packages globally instead of per-project</span><span class="mistake-desc">Global installs pollute the system Python, cause version conflicts, and make projects non-reproducible on other machines.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># No venv activated:
pip install django==4.2
pip install django==5.0   # overwrites 4.2 globally!
# Project A needs 4.2, Project B needs 5.0 — impossible!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Per-project isolation:
cd project_a
python -m venv .venv
.venv\\Scripts\\activate
pip install django==4.2

cd project_b
python -m venv .venv
.venv\\Scripts\\activate
pip install django==5.0</div></div></div><span class="mistake-note">&#128161; Each project gets its own <code>.venv/</code> folder. The venv is cheap to create and completely independent.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; not activating the venv before installing</span><span class="mistake-desc">If you run <code>pip install</code> without activating the venv, packages go into the <b>global</b> Python, not your project venv.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Created venv but forgot to activate:
python -m venv .venv
pip install flask   # WRONG — global install!

# Your venv is empty, global Python is polluted</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># Always activate first:
python -m venv .venv
.venv\\Scripts\\activate    # Windows
# source .venv/bin/activate  # Linux/Mac
pip install flask            # goes into .venv/</div></div></div><span class="mistake-note">&#128161; Check for the <code>(.venv)</code> prefix in your terminal prompt. Without it, <code>pip</code> targets the global Python.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; not updating <code>requirements.txt</code> after installing</span><span class="mistake-desc">If you install packages but don&apos;t update <code>requirements.txt</code>, teammates can&apos;t reproduce your environment.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># Install new package:
pip install httpx
# Forget to update requirements.txt
# Teammate: pip install -r requirements.txt
# ImportError: No module named 'httpx'</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># After every new install:
pip install httpx
pip freeze > requirements.txt
# or use pip-tools for pinned transitive deps:
# pip-compile requirements.in</div></div></div><span class="mistake-note">&#128161; Make <code>pip freeze > requirements.txt</code> a reflex after every <code>pip install</code>. Commit <code>requirements.txt</code> to git.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Global install chaos</div><div class="step-pre"># System Python (bad):
pip install requests flask pytest
# All projects share the same versions
# Upgrading one project can break another</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; Venv workflow</div><div class="step-pre">python -m venv .venv
.venv\\Scripts\\activate
pip install requests flask pytest
pip freeze > requirements.txt
# (.venv) shown in prompt
# Teammate setup:
git clone repo
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Command to create a virtual environment?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>python -m venv .venv</code> &mdash; creates a <code>.venv/</code> folder with isolated Python and pip.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> How to activate on Windows PowerShell?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>.venv\\Scripts\\Activate.ps1</code> (or <code>activate.bat</code> in Command Prompt).</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>pip freeze > requirements.txt</code> does?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Captures all currently installed packages and their versions into <code>requirements.txt</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> Should <code>.venv/</code> be committed to git?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No &mdash; add <code>.venv/</code> to <code>.gitignore</code>. It is platform-specific and large.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>pip install -r requirements.txt</code> does?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Installs all packages listed in <code>requirements.txt</code> at the specified versions.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> What is <code>python -m venv</code> vs just <code>venv</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>python -m venv</code> ensures the <em>correct</em> Python interpreter creates the venv. The bare <code>venv</code> command may not be in PATH.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> Difference between <code>pip freeze</code> and <code>pip list</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>freeze</code> outputs <code>package==version</code> format suitable for <code>requirements.txt</code>. <code>list</code> is a readable table.</div>
    </details>
  </div>
</div>
''', '''
<ul class="checklist">
  <li>Create venv in a practice folder</li>
  <li>pip install pytest and run tests</li>
  <li>Generate requirements.txt from current env</li>
</ul>
<span class="run-cmd">cd Python-Set2/pythonBasics && python -m venv venv</span>
'''),

# ── Real Projects (Python-Set2) ─────────────────────────────────────────────,

(28, "FastAPI with SQLAlchemy", '''
<p>Typical production stack: <b>FastAPI</b> (HTTP + async) + <b>Pydantic</b> (schemas) + <b>SQLAlchemy</b> (ORM / DB) — similar to ASP.NET Core + EF Core.</p>
<table class="ref-table">
<tr><th>Layer</th><th>Responsibility</th></tr>
<tr><td>routes / routers</td><td>HTTP only — thin handlers</td></tr>
<tr><td>schemas (Pydantic)</td><td>API input/output validation</td></tr>
<tr><td>models (SQLAlchemy)</td><td>Database tables and relationships</td></tr>
<tr><td>services</td><td>Business logic, transactions</td></tr>
<tr><td>session / engine</td><td>Connection pool, Unit of Work per request</td></tr>
</table>
''' + code('''# ── Stack overview (simplified) ──
# pip install fastapi uvicorn sqlalchemy pydantic

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class UserORM(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)

class UserCreate(BaseModel):
    email: str

class UserRead(BaseModel):
    id: int
    email: str
    model_config = {"from_attributes": True}  # ORM → schema

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/users", response_model=UserRead)
def create_user(body: UserCreate, db: Session = Depends(get_db)):
    row = UserORM(email=body.email)
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

# Run: uvicorn main:app --reload''') + '''
<div class="callout"><b>Pattern:</b> Never return ORM objects without a response schema. Use <code>Depends(get_db)</code> so each request gets one session, closed in <code>finally</code> — like scoped DbContext in C#.</div>
''', '''
<ul class="checklist">
  <li>Draw layers: route → service → ORM → DB</li>
  <li>Compare SQLAlchemy session to EF Core DbContext</li>
  <li>Read <code>Projects/35_fastapi_sqlalchemy.md</code> for folder layout</li>
</ul>
'''),

(29, "Python-Set2 — Portfolio Overview", '''
<p><b>Python-Set2</b> is your hands-on project library — six areas mapping to this curriculum.</p>
<table class="project-map">
<tr><th>Folder</th><th>Teaches</th><th>Slides</th></tr>
<tr><td>pythonBasics/</td><td>OOP, collections, loops, tests</td><td>3, 5, 9, 17, 18</td></tr>
<tr><td>google-python-exercises/</td><td>Files, regex, algorithms</td><td>14, 16</td></tr>
<tr><td>pandas/</td><td>Jupyter, DataFrames, CSV</td><td>14, data roles</td></tr>
<tr><td>djangobasics/</td><td>Django MVT, auth, JWT</td><td>27</td></tr>
<tr><td>DjangoRestBasics/</td><td>DRF serializers, ViewSets</td><td>27</td></tr>
<tr><td>Pipecat-Project/</td><td>Voice AI, async, WebRTC</td><td>21, 28</td></tr>
</table>
''' + tree(
    tree_row(0, "📁", "Python-Set2/", "t-folder", "portfolio root") +
    tree_row(1, "📁", "pythonBasics/", "t-folder", "7 modules") +
    tree_row(1, "📁", "google-python-exercises/", "t-folder", "4 exercises") +
    tree_row(1, "📁", "pandas/", "t-folder", "Jupyter + CSV") +
    tree_row(1, "📁", "djangobasics/meeting_planner/", "t-folder", "Django + JWT") +
    tree_row(1, "📁", "DjangoRestBasics/inventory/", "t-folder", "DRF API") +
    tree_row(1, "📁", "Pipecat-Project/", "t-folder", "Voice AI POCs")
), '''
''' + code('''# Explore each area:
# python Python-Set2/pythonBasics/MyClass/oops_inheritance_BankAccount.py
# jupyter notebook Python-Set2/pandas/Pandas_TitanicData.ipynb
# cd Python-Set2/djangobasics/meeting_planner && python manage.py runserver''') + '''
<ul class="checklist">
  <li>Open Python-Set2/ in VS Code / Cursor</li>
  <li>Run one script from each top-level folder</li>
  <li>Write a 2-minute walkthrough per folder</li>
</ul>
<a class="file-link" href="Python-Set2/">Python-Set2 root</a>
'''),

(30, "pythonBasics — Topic Modules", '''
<table class="project-map">
<tr><th>Module</th><th>Topics</th><th>Key files</th></tr>
<tr><td>MyClass</td><td>OOP, inheritance, polymorphism</td><td>oops_inheritance_BankAccount.py</td></tr>
<tr><td>MyCollections</td><td>list, dict, set, tuple</td><td>collection demos</td></tr>
<tr><td>MyLoops</td><td>for, while, range</td><td>loop examples</td></tr>
<tr><td>MyModules</td><td>import, packages</td><td>module demos</td></tr>
<tr><td>MyExceptionHandling</td><td>try/except, raise</td><td>error handling</td></tr>
<tr><td>MyDebug</td><td>pdb, logging</td><td>debugging</td></tr>
<tr><td>MyUnitTesting</td><td>pytest, unittest</td><td>test examples</td></tr>
</table>
''' + tree(
    tree_row(0, "📁", "pythonBasics/", "t-folder") +
    tree_row(1, "📁", "MyClass/", "t-folder") +
    tree_row(1, "📁", "MyCollections/", "t-folder") +
    tree_row(1, "📁", "MyLoops/", "t-folder") +
    tree_row(1, "📁", "MyUnitTesting/", "t-folder")
), '''
''' + code('''# Run topic modules:
python Python-Set2/pythonBasics/MyClass/oops_inheritance_BankAccount.py
python Python-Set2/pythonBasics/MyCollections/collections_demo.py
pytest Python-Set2/pythonBasics/MyUnitTesting/ -v''') + '''
<ul class="checklist">
  <li>Run oops_inheritance_BankAccount.py — explain aloud</li>
  <li>Complete one MyCollections exercise</li>
  <li>Write and run one pytest in MyUnitTesting/</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyClass/">MyClass</a>
<a class="file-link" href="Python-Set2/pythonBasics/MyUnitTesting/">MyUnitTesting</a>
'''),

(31, "Google Exercises &amp; Pandas", '''
<h3>google-python-exercises/</h3>
<table class="data-tbl">
<tr><th>Exercise</th><th>Skill</th></tr>
<tr><td>basic/</td><td>Lists, strings, logic</td></tr>
<tr><td>babynames/</td><td>Regex, file parsing</td></tr>
<tr><td>copyspecial/</td><td>os, shutil, filesystem</td></tr>
<tr><td>logpuzzle/</td><td>HTTP, algorithms</td></tr>
</table>
<h3>pandas/</h3>
<ul>
<li><b>MyJupyterBasics.ipynb</b> — DataFrame intro</li>
<li><b>Pandas_TitanicData.ipynb</b> — filtering, groupby</li>
<li><b>Pandas_FIFAData.ipynb</b> — sorting, aggregation</li>
</ul>
''' + code('''# google-python-exercises/babynames/ — regex practice
# pandas/ — data analysis
import pandas as pd
df = pd.read_csv("Python-Set2/pandas/titanic.csv")
df.head()           # first 5 rows
df.groupby("Sex")["Age"].mean()   # group and aggregate''') + '''
''', '''
<ul class="checklist">
  <li>Complete babynames/ regex exercise</li>
  <li>Open Titanic notebook in Jupyter</li>
  <li>Explain one groupby result in plain English</li>
</ul>
<span class="run-cmd">jupyter notebook Python-Set2/pandas/Pandas_TitanicData.ipynb</span>
<a class="file-link" href="Python-Set2/google-python-exercises/babynames/">babynames</a>
<a class="file-link" href="Python-Set2/pandas/Pandas_TitanicData.ipynb">Titanic notebook</a>
'''),

(32, "Django &amp; Django REST", '''
<h3>djangobasics/meeting_planner/</h3>
''' + tree(
    tree_row(0, "📁", "meeting_planner/", "t-folder") +
    tree_row(1, "📄", "manage.py", "t-file") +
    tree_row(1, "📁", "meeting/", "t-folder", "models, views, templates") +
    tree_row(1, "📁", "myauth/", "t-folder", "login views") +
    tree_row(1, "📁", "meetingapi_simplejwt/", "t-folder", "JWT API")
) + '''
<h3>DjangoRestBasics/inventory/</h3>
''' + tree(
    tree_row(0, "📁", "inventory/", "t-folder") +
    tree_row(1, "📁", "drink/", "t-folder", "Model + Serializer + ViewSet") +
    tree_row(1, "📁", "merchant/", "t-folder") +
    tree_row(1, "📁", "supplier/", "t-folder")
) + '''
<div class="challenge"><b>Django vs DRF:</b> Django = full web app (templates, ORM, admin). DRF = REST API layer on top with serializers.</div>
''' + code('''# Django — run development server
# cd Python-Set2/djangobasics/meeting_planner
# python manage.py runserver

# DRF — serializer example pattern:
# class DrinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Drink
#         fields = ['id', 'name', 'price']''') + '''
''', '''
<ul class="checklist">
  <li>cd meeting_planner → python manage.py runserver</li>
  <li>Explore meeting/models.py and migrations/</li>
  <li>Compare drink/serializers.py to Pydantic schemas</li>
</ul>
<span class="run-cmd">cd Python-Set2/djangobasics/meeting_planner && python manage.py runserver</span>
<a class="file-link" href="Python-Set2/djangobasics/meeting_planner/meeting/models.py">Meeting models</a>
<a class="file-link" href="Python-Set2/DjangoRestBasics/inventory/drink/serializers.py">DRF serializers</a>
'''),

(33, "Pipecat — Voice AI POCs", '''
<table class="project-map">
<tr><th>POC</th><th>Purpose</th></tr>
<tr><td>pipecat-quickstart</td><td>Official Pipecat — cloud STT/LLM/TTS</td></tr>
<tr><td>pipecat-voice-phase1</td><td>Local STT/LLM/TTS + simple UI</td></tr>
<tr><td>pipecat-voice-phase2</td><td>Full Pipecat pipeline (steps 1–8)</td></tr>
<tr><td>voice-bouncer</td><td>IVR voice auth (member ID, zip)</td></tr>
<tr><td>Pipecat-Learning/</td><td>HTML tutorials</td></tr>
</table>
<div class="callout"><b>Architecture:</b> STT → LLM → TTS over WebRTC. FastAPI backend + Pipecat processors + browser client.</div>
''' + code('''# Voice AI pipeline (conceptual):
# Audio In → STT (speech-to-text) → LLM (brain) → TTS (text-to-speech) → Audio Out
#
# Run voice-bouncer POC:
# cd Python-Set2/Pipecat-Project/POC/voice-bouncer
# python step1_greeting.py''') + '''
''', '''
<ul class="checklist">
  <li>Read POC/Readme.md for phase overview</li>
  <li>Run voice-bouncer step1_greeting.py</li>
  <li>Open PipeCatLearningContent/PipecatAI.html</li>
</ul>
<a class="file-link" href="Python-Set2/Pipecat-Project/POC/Readme.md">POC Readme</a>
<a class="file-link" href="Python-Set2/Pipecat-Project/POC/voice-bouncer/README.md">voice-bouncer</a>
<a class="file-link" href="Python-Set2/Pipecat-Project/PipeCatLearningContent/PipecatAI.html">PipecatAI guide</a>
'''),

(34, "Real Project Structure &amp; Learning Path", '''
<h3>Production API layout</h3>
''' + tree(
    tree_row(0, "📁", "my-api/", "t-folder") +
    tree_row(1, "📄", "requirements.txt", "t-file") +
    tree_row(1, "📄", ".env.example", "t-file") +
    tree_row(1, "📁", "app/", "t-folder") +
    tree_row(2, "📄", "main.py", "t-file", "entry point") +
    tree_row(2, "📁", "api/routes/", "t-folder", "HTTP handlers") +
    tree_row(2, "📁", "services/", "t-folder", "business logic") +
    tree_row(2, "📁", "schemas/", "t-folder", "Pydantic DTOs") +
    tree_row(1, "📁", "tests/", "t-folder", "pytest")
) + '''
<h3>4-week syllabus order</h3>
<table class="data-tbl">
<tr><th>Week</th><th>Focus</th><th>Slides (syllabus order)</th></tr>
<tr><td>1</td><td>Intro, setup, workspace, PEP, datatypes, typing, operators, flow, comprehensions, functions, builtins</td><td>1–11</td></tr>
<tr><td>2</td><td>Collections, memory/GC, Pydantic, OOP, descriptors, generators</td><td>12–17</td></tr>
<tr><td>3</td><td>Decorators, exceptions, threading/async/GIL, logging, tests, regex, files, context, venv</td><td>18–27</td></tr>
<tr><td>4</td><td>FastAPI with SQLAlchemy</td><td>28</td></tr>
</table>
''' + code('''# Production API layout (FastAPI example):
# my-api/
#   app/main.py          ← entry point
#   app/api/routes/      ← HTTP handlers (thin)
#   app/services/        ← business logic
#   app/schemas/         ← Pydantic DTOs
#   tests/               ← pytest
#
# Run: uvicorn app.main:app --reload''') + '''
''', '''
<ul class="checklist">
  <li>Draw project tree from memory in 2 minutes</li>
  <li>Demo 2–3 Set2 projects in mock interview</li>
  <li>Connect each project to a curriculum slide</li>
</ul>
'''),

(35, "C# vs Python — Quick Reference", '''
<table class="ref-table">
<tr><th>Concept</th><th>C#</th><th>Python</th></tr>
<tr><td>Variable</td><td>int x = 5;</td><td>x = 5</td></tr>
<tr><td>Print</td><td>Console.WriteLine()</td><td>print()</td></tr>
<tr><td>Foreach</td><td>foreach (var i in list)</td><td>for i in list:</td></tr>
<tr><td>Block / braces</td><td>{ }</td><td>Indentation after :</td></tr>
<tr><td>Empty block (stub)</td><td>{ } — empty method or if body</td><td>pass — intentionally empty for now</td></tr>
<tr><td>Not implemented yet</td><td>throw new NotImplementedException();</td><td>raise NotImplementedError()</td></tr>
<tr><td>Class</td><td>class Person { }</td><td>class Person: (use pass if empty)</td></tr>
<tr><td>this / self</td><td>this (implicit in methods)</td><td>self (explicit first parameter)</td></tr>
<tr><td>Null</td><td>null — test: x == null</td><td>None — test: x is None</td></tr>
<tr><td>Equality vs identity</td><td>== value; ReferenceEquals same object</td><td>== value; is same object</td></tr>
<tr><td>else if</td><td>else if</td><td>elif</td></tr>
<tr><td>Boolean</td><td>true / false</td><td>True / False (capital T/F)</td></tr>
<tr><td>Interface</td><td>interface IRepo { void Save(); }</td><td>ABC or duck typing; empty class: pass</td></tr>
<tr><td>Exception</td><td>try / catch / finally</td><td>try / except / finally</td></tr>
<tr><td>Throw</td><td>throw new ArgumentException();</td><td>raise ValueError()</td></tr>
<tr><td>Resource cleanup</td><td>using (var f = File.Open(...))</td><td>with open(...) as f:</td></tr>
<tr><td>Property</td><td>public int Age { get; set; }</td><td>@property decorator</td></tr>
<tr><td>String format</td><td>$"Hello {name}"</td><td>f"Hello {name}"</td></tr>
<tr><td>Namespace / import</td><td>using System.Linq;</td><td>import os</td></tr>
<tr><td>Entry point</td><td>static void Main()</td><td>if __name__ == "__main__":</td></tr>
<tr><td>LINQ / collections</td><td>list.Where(x =&gt; x &gt; 0)</td><td>[x for x in lst if x &gt; 0]</td></tr>
<tr><td>Switch / pattern</td><td>switch (x) { case 1: ... }</td><td>match x: case 1: ... (3.10+)</td></tr>
<tr><td>Package manager</td><td>NuGet / dotnet add package</td><td>pip + requirements.txt</td></tr>
<tr><td>Web API</td><td>[HttpGet] controller</td><td>@app.get() FastAPI / DRF</td></tr>
<tr><td>Async</td><td>async Task&lt;T&gt; + await</td><td>async def + await (coroutine)</td></tr>
</table>
<div class="callout"><b>pass in Python</b> = no single C# keyword. Closest: empty <code>{ }</code> when the block must exist but do nothing yet. Stronger stub: <code>throw new NotImplementedException()</code> ≈ <code>raise NotImplementedError()</code>. C# interfaces/abstract methods declare without a body — Python uses <code>pass</code> inside <code>class</code> or <code>def</code> instead.</div>
''' + code('''# ── C# vs Python side-by-side ──
# C#:  int x = 5;              Python: x = 5
# C#:  Console.WriteLine(x);   Python: print(x)
# C#:  foreach (var i in list)  Python: for i in list:
# C#:  try { } catch (Ex e)    Python: try: except Ex as e:
# C#:  null                     Python: None  (use: x is None)
# C#:  $"Hello {name}"          Python: f"Hello {name}"
# C#:  dotnet add package       Python: pip install package
# C#:  async Task<string>       Python: async def fn() -> str

# ── pass / stub equivalents ──
# C# empty stub:
#   void SaveReport() { }
# Python:
def save_report():
    pass   # intentionally empty for now

# C# not implemented yet:
#   throw new NotImplementedException();
# Python:
def save_report_v2():
    raise NotImplementedError("Implement later")

# C#:  this.Name = name;        Python: self.name = name
# C#:  using (var f = ...)       Python: with open(...) as f:
# C#:  static void Main()        Python: if __name__ == "__main__":''') + '''
<div class="callout"><strong>35 slides complete — sequential week order!</strong> Basics + setup + 21 core topics + 6 real projects + appendix + 5 extended curriculum topics. Review slides 1–2, 15, 23–24, 29–34, and 4 / 13 / 22 / 28 before interviews.</div>


<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; not closing DB sessions (connection pool exhaustion)</span><span class="mistake-desc">SQLAlchemy sessions hold a DB connection. Forgetting to close them exhausts the connection pool under load.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">from myapp.database import SessionLocal

@app.get("/users/{id}")
def get_user(id: int):
    db = SessionLocal()
    user = db.query(User).filter_by(id=id).first()
    return user
    # db.close() never called — connection leaked!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from fastapi import Depends
from myapp.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    # always closed

@app.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter_by(id=id).first()</div></div></div><span class="mistake-note">&#128161; Use FastAPI&apos;s <code>Depends(get_db)</code> pattern &mdash; the dependency&apos;s <code>finally</code> block closes the session after each request.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 2 &mdash; N+1 query problem</span><span class="mistake-desc">Loading a list of orders and then fetching each user separately (one query per order) is the N+1 problem.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre"># 1 query for orders + N queries for users:
orders = db.query(Order).all()
for order in orders:
    user = db.query(User).filter_by(id=order.user_id).first()
    print(order.id, user.name)  # N+1 queries!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre"># 1 query with JOIN:
from sqlalchemy.orm import joinedload

orders = db.query(Order).options(joinedload(Order.user)).all()
for order in orders:
    print(order.id, order.user.name)  # no extra queries</div></div></div><span class="mistake-note">&#128161; Use <code>joinedload()</code>, <code>selectinload()</code>, or explicit JOINs to eagerly load related data in one query.</span></div>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 3 &mdash; exposing SQLAlchemy models directly as response</span><span class="mistake-desc">Returning ORM model instances directly bypasses Pydantic validation, can expose sensitive fields, and causes lazy-loading errors.</span><div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">@app.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter_by(id=id).first()
    # exposes ALL columns including password_hash!</div></div><div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    model_config = ConfigDict(from_attributes=True)

@app.get("/users/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter_by(id=id).first()</div></div></div><span class="mistake-note">&#128161; Always define Pydantic <code>response_model</code> schemas. Set <code>model_config = ConfigDict(from_attributes=True)</code> to convert ORM objects to Pydantic.</span></div>
<h3>Before &rarr; After (Pythonic)</h3>
<div class="before-after">
  <div class="ba-col ba-bad"><div class="ba-label">&#10060; Ad-hoc endpoint (fragile)</div><div class="step-pre">@app.post("/orders")
def create_order(data: dict):   # raw dict
    order = Order(
        user_id=data["user_id"],  # KeyError risk
        total=data["total"]
    )
    db = SessionLocal()
    db.add(order)
    db.commit()
    return order.__dict__         # exposes internals</div></div>
  <div class="ba-arrow">&rarr;</div>
  <div class="ba-col ba-good"><div class="ba-label">&#10004; FastAPI best practice</div><div class="step-pre">class OrderCreate(BaseModel):
    user_id: int
    total: float = Field(gt=0)

class OrderResponse(BaseModel):
    id: int; user_id: int; total: float
    model_config = ConfigDict(from_attributes=True)

@app.post("/orders", response_model=OrderResponse, status_code=201)
def create_order(body: OrderCreate, db: Session = Depends(get_db)):
    order = Order(**body.model_dump())
    db.add(order); db.commit(); db.refresh(order)
    return order</div></div>
</div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> FastAPI&apos;s <code>Depends()</code> is used for?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><b>Dependency injection</b> &mdash; injecting shared resources like DB sessions, auth checks, or config into route handlers.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> <code>response_model</code> in a FastAPI endpoint does?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Validates and <b>serialises</b> the return value against the specified Pydantic model, excluding undeclared fields.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> <code>db.add(obj)</code> then what is needed to persist?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>db.commit()</code> &mdash; <code>add()</code> only stages the object in the session; <code>commit()</code> writes to the database.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q4.</b> SQLAlchemy <code>relationship()</code> lazy loading can cause?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The <b>N+1 query problem</b> &mdash; accessing a related attribute triggers a separate DB query for each parent object.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q5.</b> <code>@app.get</code> vs <code>@app.post</code> &mdash; which is idempotent by HTTP spec?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>GET</code> is idempotent (same result for repeated calls). <code>POST</code> creates resources and is not idempotent.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q6.</b> Pydantic <code>BaseModel</code> vs SQLAlchemy <code>Base</code>?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>BaseModel</code> is for input/output validation and serialisation (DTOs). SQLAlchemy <code>Base</code> is for ORM table mapping.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q7.</b> <code>db.refresh(obj)</code> after commit does?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Reloads the object from the database, populating auto-generated fields like <code>id</code>, <code>created_at</code>.</div>
    </details>
  </div>
</div>
''', '''
<h4>Final checklist</h4>
<ul class="checklist">
  <li>Completed practice in each Python-Set2 folder</li>
  <li>Can explain GIL, decorators, and async</li>
  <li>Demo-ready on Django and one Pipecat POC</li>
  <li>Reviewed C# vs Python cheat sheet</li>
</ul>
'''),


]


def build_nav():
    titles = {n: t for n, t, _, _ in CONTENT}

    def topic_block(n: int) -> str:
        if n not in titles:
            return ""
        subs = SLIDE_SUBTOPICS.get(n, [])
        sub_html = ""
        if subs:
            items = "".join(
                f'<li><a href="#{n}" onclick="goSlide({n}); return false;">{html.escape(s)}</a></li>'
                for s in subs
            )
            sub_html = f'<ul class="nav-subs">{items}</ul>'
        return (
            f'<div class="nav-topic">'
            f'<a class="nav-main" href="#{n}" onclick="goSlide({n}); return false;">{n}. {titles[n]}</a>'
            f"{sub_html}"
            f"</div>"
        )

    def links(nums: list[int]) -> str:
        return "".join(topic_block(n) for n in nums)

    sections = "".join(
        f'''    <div class="nav-section nav-section-{index}">
      <h3>{title}</h3>
      <div class="nav-links">{links(nums)}</div>
    </div>
'''
        for index, (title, nums) in enumerate(WEEK_SECTIONS, 1)
    )
    return f'''<div class="slide active" id="slide-0">
<div class="nav-content">
  <h1>Python Training 2026</h1>
  <div class="sub">Batch 2 &middot; Week-by-week curriculum</div>
  <div class="org">Click a topic below to jump to that slide</div>
  {audio_bar(0)}
  <div class="nav-grid">
{sections}  </div>
</div>
</div>'''


def main():
    slides = [build_nav()]
    for num, title, learn, practice in CONTENT:
        slides.append(slide(num, title, learn, practice))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Python Training 2026 — Batch 2</title>
<style>{CSS}</style>
</head>
<body>
{"".join(slides)}
{render_csharp_popups()}
{NAV_BAR}
<script>{JS}</script>
</body>
</html>"""

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Generated {OUTPUT} ({len(html):,} bytes, {len(slides)} slides)")


if __name__ == "__main__":
    main()
