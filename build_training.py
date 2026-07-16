"""Generate PythonTraining.html — Batch 2 curriculum + Python-Set2 real projects."""
import html
import re
from pathlib import Path
from slide_keyword_deepdives import keyword_deepdives_for
from training_meta import TRAINING_META
from training_beginner import BEGINNER_CONTENT
from slide_glossary import glossary_for
from slide_scenarios import scenarios_for

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
  grid-template-columns: 1fr 1.05fr;
  gap: 28px;
  align-items: start;
}
.main-split.no-code { grid-template-columns: 1fr; max-width: 900px; }
.panel-left { min-width: 0; }
.panel-code { min-width: 0; position: sticky; top: 12px; }
.panel-code .vs-editor + .vs-editor { margin-top: 12px; }

.interview-box { background: #e8f5e9; border-left: 3px solid #28a745; padding: 10px 12px; border-radius: 4px; margin-top: 8px; font-size: 12px; }
.interview-box p { margin: 6px 0 0; color: #1b5e20; line-height: 1.5; }
.interview-box .qa-q { margin-top: 10px; color: #1b5e20; font-style: normal; }
.interview-box .qa-a { margin-top: 4px; margin-left: 8px; color: #2e7d32; font-style: normal; }
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

.nav-content { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: calc(100vh - 44px); padding: 20px; }
.nav-content h1 { font-size: 34px; margin-bottom: 4px; }
.nav-content .sub { font-size: 16px; color: #0066cc; }
.nav-content .org { font-size: 13px; color: #666; margin: 8px 0 24px; }
.nav-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; max-width: 960px; width: 100%; }
.nav-section { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px; max-height: 360px; overflow-y: auto; }
.nav-section h3 { font-size: 13px; margin-bottom: 8px; border-bottom: 2px solid #0066cc; padding-bottom: 4px; }
.nav-section a { display: block; padding: 3px 0; color: #0066cc; font-size: 11px; cursor: pointer; text-decoration: none; }
.nav-section a:hover { text-decoration: underline; }

@media (max-width: 900px) {
  .slide { padding: 16px 16px 56px; }
  .main-split, .nav-grid { grid-template-columns: 1fr; }
  .flow-compare { grid-template-columns: 1fr; }
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
  document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
  const el = document.getElementById('slide-' + n);
  if (el) {
    el.classList.add('active');
    current = n;
    el.scrollTop = 0;
    const info = document.getElementById('slideInfo');
    if (info) info.textContent = n === 0 ? 'Navigation' : 'Slide ' + n + ' of ' + totalTopics;
    updateTimeUI(n);
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
document.addEventListener('keydown', function(e) {
  if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
  if (e.key === 'Home') { e.preventDefault(); showSlide(0); }
  if (e.key === 'a' || e.key === 'A') { e.preventDefault(); togglePlay(current); }
});
document.addEventListener('DOMContentLoaded', () => {
  initAudioPlayers();
  showSlide(0);
});
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

MODULE_MAP = {
    range(1, 24): "Core Topics",
    range(24, 30): "Real Projects · Python-Set2",
    range(30, 31): "Appendix",
    range(31, 36): "Extended Curriculum",
}


def module_for(n):
    for r, name in MODULE_MAP.items():
        if n in r:
            return name
    return "Python Training 2026"


_CODE_SNIPPETS: list[str] = []
_CODE_MARKER = re.compile(r"<!--CODE:(\d+)-->")

_PY_KEYWORDS = {
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class",
    "continue", "def", "del", "elif", "else", "except", "finally", "for", "from",
    "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass",
    "raise", "return", "try", "while", "with", "yield",
}
_PY_BUILTINS = {
    "abs", "all", "any", "bin", "bool", "bytes", "chr", "dict", "enumerate", "filter",
    "float", "format", "frozenset", "getattr", "hasattr", "hash", "hex", "id", "input",
    "int", "isinstance", "issubclass", "iter", "len", "list", "map", "max", "min", "next",
    "object", "oct", "open", "ord", "pow", "print", "range", "repr", "reversed", "round",
    "set", "slice", "sorted", "str", "sum", "super", "tuple", "type", "zip",
}

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


def _span(cls: str, text: str) -> str:
    return f'<span class="{cls}">{html.escape(text)}</span>'


def highlight_line(line: str) -> str:
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        ch = line[i]
        if ch == "#":
            out.append(_span("t-cm", line[i:]))
            break
        if ch in "\"'":
            q = ch
            j = i + 1
            while j < n:
                if line[j] == "\\":
                    j += 2
                    continue
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
        if ch.isalpha() or ch == "_":
            j = i
            while j < n and (line[j].isalnum() or line[j] == "_"):
                j += 1
            word = line[i:j]
            if word in _PY_KEYWORDS:
                cls = "t-kw"
            elif word in _PY_BUILTINS:
                cls = "t-bi"
            else:
                cls = "t-id"
            out.append(_span(cls, word))
            i = j
            continue
        out.append(_span("t-op", ch))
        i += 1
    return "".join(out) if out else "&#160;"


def code(text: str) -> str:
    idx = len(_CODE_SNIPPETS)
    _CODE_SNIPPETS.append(text)
    return f"<!--CODE:{idx}-->"


def code_table(idx: int) -> str:
    raw = _CODE_SNIPPETS[idx]
    rows = []
    for num, line in enumerate(raw.splitlines(), 1):
        rows.append(
            f'<tr><td class="gutter">{num}</td><td class="src">{highlight_line(line)}</td></tr>'
        )
    if not rows:
        rows.append('<tr><td class="gutter">1</td><td class="src">&#160;</td></tr>')
    body = "\n".join(rows)
    return f'<div class="vs-editor"><table class="vs-code"><tbody>\n{body}\n</tbody></table></div>'


def split_learn(learn: str) -> tuple[str, str]:
    """Split learn HTML into notes (no code) and rendered code panels in order."""
    notes_parts: list[str] = []
    code_parts: list[str] = []
    chunks = _CODE_MARKER.split(learn)
    for i, chunk in enumerate(chunks):
        if i % 2 == 0:
            notes_parts.append(chunk)
        else:
            code_parts.append(code_table(int(chunk)))
    return "".join(notes_parts), "\n".join(code_parts)


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
        if n == 1:
            parts.append(python_vs_csharp_flow())
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
    notes_html = glossary_for(n) + scenarios_for(n) + notes_html + interview_box(n)
    has_code = bool(codes_html.strip())
    split_cls = "main-split" if has_code else "main-split no-code"
    code_panel = f'<div class="panel-code">{codes_html}</div>' if has_code else ""
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

# ── DUCK TYPING: behavior matters, not declared type ──
class Dog:
    def speak(self):
        return "Woof!"

def announce(animal):
    return animal.speak()  # works if .speak() exists

print(announce(Dog()))''') + '''
<div class="callout"><b>C# developer tip:</b> <code>python file.py</code> ≈ immediate run (no dotnet build). Replace <code>{ }</code> with indents. Replace <code>null</code> with <code>None</code>.</div>
''', '''
<ul class="checklist">
  <li>Explain interpretation vs compilation in your own words</li>
  <li>Find a <code>.pyc</code> file in <code>__pycache__/</code> after running a script</li>
  <li>Write an if/else block using indentation only</li>
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

(3, "Python Datatypes", '''
''' + code('''# ── STEP 1: Primitive data types ──
age = 25              # int
price = 99.5          # float
name = "Ravi"         # str
is_student = True     # bool

# ── STEP 2: Collection types ──
numbers = [10, 20, 30]                  # list
point = (10, 20)                        # tuple
colors = {"red", "green"}               # set
frozen = frozenset({"read", "write"})   # frozenset
student = {"name": "Ravi", "age": 15}   # dict

# ── STEP 3: List — indexing, slicing, mutability ──
nums = [10, 20, 30, 40]
print(nums[0], nums[-1], nums[1:3])
nums.append(50)

# ── STEP 4: Tuple — packing / unpacking ──
lat, lng = (12.97, 80.22)
ok, val = True, 42    # unpack two values

# ── STEP 5: Set — uniqueness ──
tags = {"python", "code", "python"}
print(tags)           # {'python', 'code'}

# ── STEP 6: Frozenset — immutable set, dict key OK ──
perms = frozenset({"read", "write"})
cache = {perms: "allowed"}

# ── STEP 7-8: Dictionary key : value ──
phone_book = {"Ravi": "99999"}
print(phone_book["Ravi"])

# ── STEP 9-11: Hashable keys ──
grid = {}
grid[(1, 2)] = "cell"
# grid[[1, 2]] = "X"   # TypeError: unhashable type: 'list'
# grid[{"id": 1}] = "x" # TypeError: unhashable type: 'dict'

# ── STEP 12: Tuple and frozenset as keys ──
grid[frozenset({"a", "b"})] = "combo"

# ── STEP 13: Summary — immutable types OK as dict keys ──
# int, float, str, bool, tuple, frozenset → Yes
# list, dict, set → No''') + '''
<div class="tip"><b>Remember:</b> Learn types first, then collections, then <i>why</i> tuple works as a dict key — not the word hashable on day one.</div>
''', '''
<ul class="checklist">
  <li>Step 5–6: Build a set and frozenset; use frozenset as a dict key</li>
  <li>Step 3–4: Slice a list; unpack a tuple into two variables</li>
  <li>Step 10–12: Try <code>grid[[1,2]]</code> vs <code>grid[(1,2)]</code> vs <code>grid[frozenset({1,2})]</code></li>
  <li>Step 13: From memory, fill the summary table</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyCollections/">MyCollections</a>
<a class="file-link" href="Python-Set2/pythonBasics/MyClass/mytypes.py">mytypes.py</a>
'''),

(4, "Your Training Workspace", '''
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
<li><b>Slides 1–2</b> — Python basics and Windows setup (you are here)</li>
<li><b>Slides 3–23</b> — Core topics with <code>Projects/</code> practice files</li>
<li><b>Slides 24–29</b> — Real projects in <code>Python-Set2/</code></li>
<li><b>Slide 30</b> — C# vs Python quick reference</li>
<li><b>Slides 31–35</b> — Extended curriculum (PEP, memory/GC, logging, Pydantic, FastAPI+SQLAlchemy)</li>
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
''', '''
<ul class="checklist">
  <li>Open <code>D:\\Sangeetha\\Python</code> in VS Code / Cursor</li>
  <li>Browse <code>Projects/</code> — one file per topic</li>
  <li>Run <code>python Projects/02_getting_started.py</code></li>
  <li>Explore <code>Python-Set2/pythonBasics/</code></li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/">pythonBasics</a>
'''),

(5, "Operators", '''
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
''', '''
<ul class="checklist">
  <li>Predict results before running each operator</li>
  <li>Compare is vs == with two equal lists</li>
  <li>Try bitwise ops on small integers</li>
</ul>
'''),

(6, "Conditional &amp; Flow Control", '''
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
''', '''
<ul class="checklist">
  <li>Write FizzBuzz (1–20)</li>
  <li>Use for-else to search a list</li>
  <li>Write a stub function with <code>pass</code>, then implement it</li>
  <li>Try <code>if False:</code> vs <code>if True: pass</code> — which runs?</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyLoops/">MyLoops</a>
'''),

(7, "Comprehensions", '''
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

import sys
print(sys.getsizeof(squares))  # ~120 bytes (full list)
print(sys.getsizeof(gen))      # ~200 bytes (generator object)''') + '''
<div class="callout">Prefer comprehensions over manual loops when building collections — they are faster and more Pythonic.</div>
''', '''
<ul class="checklist">
  <li>Build a dict comprehension from a list of tuples</li>
  <li>Compare memory: list vs generator with sys.getsizeof</li>
  <li>Filter a list of names starting with "A"</li>
</ul>
'''),

(8, "Python Functions", '''
''' + code('''# ── BASIC FUNCTION ──
def greet(name, greeting="Hello"):
    """Return a greeting string. greeting has a default value."""
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Hello, Alice!
print(greet("Bob", "Hi"))            # Hi, Bob!

# ── *args (extra positional) and **kwargs (extra keyword) ──
def total(*args, **kwargs):
    print("args:", args)             # tuple: (1, 2, 3)
    print("kwargs:", kwargs)         # dict: {'tax': 0.1}

total(1, 2, 3, tax=0.1)

# ── RECURSION ──
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))  # 120

# ── LAMBDA: anonymous one-liner ──
double = lambda x: x * 2
print(double(5))     # 10

# ── LEGB scope: Local → Enclosing → Global → Builtin ──
x = "global"
def outer():
    x = "enclosing"
    def inner():
        return x     # finds "enclosing" (Enclosing scope)
    return inner
print(outer()())     # enclosing

# ── CLOSURE: inner function remembers outer variable ──
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter(), counter(), counter())  # 1, 2, 3

# ── MUTABLE DEFAULT TRAP (avoid!) ──
def bad(lst=[]):       # DON'T - shared across calls
    lst.append(1)
    return lst

def good(lst=None):     # DO THIS instead
    if lst is None:
        lst = []
    lst.append(1)
    return lst''') + '''
<div class="tip"><b>Mutable default trap:</b> never use <code>def f(lst=[])</code> — use <code>def f(lst=None)</code> and create inside.</div>
''', '''
<ul class="checklist">
  <li>Write a function with *args and **kwargs</li>
  <li>Implement factorial recursively</li>
  <li>Create a closure that counts calls</li>
</ul>
'''),

(9, "Built-in Functions", '''
<table class="data-tbl">
<tr><th>Function</th><th>Purpose</th></tr>
<tr><td>map(fn, iter)</td><td>Apply fn to each item</td></tr>
<tr><td>filter(fn, iter)</td><td>Keep items where fn is True</td></tr>
<tr><td>zip(a, b)</td><td>Pair elements</td></tr>
<tr><td>enumerate(iter)</td><td>Index + value pairs</td></tr>
<tr><td>sorted(iter)</td><td>Return sorted copy</td></tr>
<tr><td>max(iter) / min(iter)</td><td>Largest / smallest item</td></tr>
</table>
''' + code('''from functools import reduce

nums = [1, 2, 3, 4, 5]

# ── map: apply function to each item ──
doubled = list(map(lambda x: x * 2, nums))     # [2,4,6,8,10]
upper = list(map(str.upper, ["a", "b"]))      # ['A','B']

# ── filter: keep items where function is True ──
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2,4]

# ── reduce: fold to single value ──
total = reduce(lambda a, b: a + b, nums)      # 15

# ── zip: pair elements from iterables ──
names = ["Alice", "Bob"]
scores = [95, 88]
pairs = list(zip(names, scores))              # [('Alice',95),('Bob',88)]
score_dict = dict(zip(names, scores))         # {'Alice':95,'Bob':88}

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
''', '''
<ul class="checklist">
  <li>Use map/filter vs list comprehension — compare readability</li>
  <li>Zip two lists into dict</li>
  <li>Sort a list of tuples by second element</li>
</ul>
'''),

(10, "OOP Concepts", '''
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
''', '''
<ul class="checklist">
  <li>Create a class with __init__ and two methods</li>
  <li>Add inheritance — override one method</li>
  <li>Implement __str__ and __repr__</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyClass/">MyClass</a>
<a class="file-link" href="Python-Set2/pythonBasics/MyClass/oops_inheritance_BankAccount.py">BankAccount</a>
'''),

(11, "Decorators", '''
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
''', '''
<ul class="checklist">
  <li>Write a @log decorator that prints args</li>
  <li>Stack two decorators on one function</li>
  <li>See how FastAPI uses @app.get() as a decorator</li>
</ul>
'''),

(12, "Descriptors", '''
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
''', '''
<ul class="checklist">
  <li>Create a @property with validation</li>
  <li>Read about how descriptors power classmethod/staticmethod</li>
</ul>
'''),

(13, "Generators &amp; Iterators", '''
''' + code('''# ── GENERATOR FUNCTION: uses yield instead of return ──
def countdown(n):
    while n > 0:
        yield n           # pause here, return value, resume on next()
        n -= 1

for i in countdown(3):
    print(i)              # 3, 2, 1

# ── ITERATOR PROTOCOL: __iter__ + __next__ ──
class CountUp:
    def __init__(self, max_n):
        self.n = 0
        self.max_n = max_n

    def __iter__(self):
        return self         # iterator returns itself

    def __next__(self):
        if self.n >= self.max_n:
            raise StopIteration   # signals end of iteration
        self.n += 1
        return self.n

for val in CountUp(3):
    print(val)            # 1, 2, 3

# ── ITERABLE vs ITERATOR ──
# Iterable: has __iter__ (list, tuple, generator)
# Iterator: has __iter__ AND __next__

import itertools
# chain: combine iterables
list(itertools.chain([1,2], [3,4]))       # [1,2,3,4]
# islice: take first N from infinite generator
list(itertools.islice(countdown(10), 3))  # [10,9,8]
# groupby: group consecutive equal items
data = [("a",1),("a",2),("b",3)]
{k: list(g) for k,g in itertools.groupby(data, key=lambda x: x[0])}''') + '''
<div class="callout">Resource: <a href="https://hackernoon.com/the-magic-behind-python-generator-functions-bc8eeea54220">Generator frame internals</a></div>
''', '''
<ul class="checklist">
  <li>Convert a list-returning function to yield</li>
  <li>Use itertools.chain on two lists</li>
  <li>Explain difference between iterator and iterable</li>
</ul>
'''),

(14, "Typing", '''
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
''', '''
<ul class="checklist">
  <li>Add type hints to an existing function</li>
  <li>Install and run mypy on one file</li>
  <li>Use Optional for a nullable return</li>
</ul>
'''),

(15, "File Operations", '''
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
''', '''
<ul class="checklist">
  <li>Read and write a text file with with</li>
  <li>Parse a JSON file</li>
  <li>Use pathlib to list .py files in a folder</li>
</ul>
<a class="file-link" href="Python-Set2/google-python-exercises/copyspecial/">copyspecial</a>
<a class="file-link" href="Python-Set2/pandas/titanic.csv">titanic.csv</a>
'''),

(16, "Exception Handling", '''
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
''', '''
<ul class="checklist">
  <li>Catch specific exceptions, not bare except</li>
  <li>Create a custom exception class</li>
  <li>Use try/finally for cleanup</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyExceptionHandling/">MyExceptionHandling</a>
'''),

(17, "Regular Expressions", '''
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
''', '''
<ul class="checklist">
  <li>Extract all emails from a string with regex</li>
  <li>Use groups to parse a date</li>
  <li>Complete babynames/ exercise</li>
</ul>
<a class="file-link" href="Python-Set2/google-python-exercises/babynames/">babynames</a>
'''),

(18, "Python Collections", '''
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

# ── ChainMap: search multiple dicts ──
defaults = {"color": "red", "size": "M"}
user_prefs = {"color": "blue"}
combined = ChainMap(user_prefs, defaults)
print(combined["color"])      # blue (user_prefs first)
print(combined["size"])       # M    (falls through to defaults)''') + '''
''', '''
<ul class="checklist">
  <li>Count word frequency with Counter</li>
  <li>Group items by category with defaultdict</li>
  <li>Use deque as a simple queue</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyCollections/">MyCollections</a>
'''),

(19, "Unit Testing", '''
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
''', '''
<ul class="checklist">
  <li>Write 3 pytest tests for one function</li>
  <li>Mock an external API call with @patch</li>
  <li>Run pytest in MyUnitTesting/</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyUnitTesting/">MyUnitTesting</a>
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
''', '''
<ul class="checklist">
  <li>Run two threads that share a counter with Lock</li>
  <li>Explain when to use threading vs multiprocessing</li>
  <li>Try ThreadPoolExecutor with 4 workers</li>
</ul>
'''),

(21, "Context Manager", '''
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
''', '''
<ul class="checklist">
  <li>Write @contextmanager for timing code blocks</li>
  <li>Implement __enter__/__exit__ class</li>
  <li>Explain how with calls __exit__ on exception</li>
</ul>
'''),

(22, "Async / Await", '''
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
''', '''
<ul class="checklist">
  <li>Write async def with two await calls</li>
  <li>Compare sequential vs asyncio.gather timing</li>
  <li>See async patterns in Pipecat voice pipeline</li>
</ul>
<a class="file-link" href="Python-Set2/Pipecat-Project/">Pipecat-Project</a>
'''),

(23, "Virtual Environment", '''
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
''', '''
<ul class="checklist">
  <li>Create venv in a practice folder</li>
  <li>pip install pytest and run tests</li>
  <li>Generate requirements.txt from current env</li>
</ul>
<span class="run-cmd">cd Python-Set2/pythonBasics && python -m venv venv</span>
'''),

# ── Real Projects (Python-Set2) ─────────────────────────────────────────────

(24, "Python-Set2 — Portfolio Overview", '''
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

(25, "pythonBasics — Topic Modules", '''
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

(26, "Google Exercises &amp; Pandas", '''
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

(27, "Django &amp; Django REST", '''
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

(28, "Pipecat — Voice AI POCs", '''
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

(29, "Real Project Structure &amp; Learning Path", '''
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
<h3>5-week study order</h3>
<table class="data-tbl">
<tr><th>Week</th><th>Focus</th><th>Folder</th></tr>
<tr><td>1</td><td>Datatypes, operators, flow</td><td>pythonBasics/MyCollections, MyLoops</td></tr>
<tr><td>2</td><td>OOP, functions, comprehensions</td><td>MyClass, slides 4–7</td></tr>
<tr><td>3</td><td>Files, regex, exceptions</td><td>google-exercises, MyExceptionHandling</td></tr>
<tr><td>4</td><td>Testing, collections, typing</td><td>MyUnitTesting, pandas/</td></tr>
<tr><td>5</td><td>Web + voice projects</td><td>Django, DRF, Pipecat</td></tr>
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

(30, "C# vs Python — Quick Reference", '''
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
<div class="callout"><strong>35 slides complete!</strong> Basics + setup + 21 core topics + 6 real projects + appendix + 5 extended curriculum topics. Review slides 1–2, 10, 17, 19, 24–28, and 31–35 before interviews.</div>
''', '''
<h4>Final checklist</h4>
<ul class="checklist">
  <li>Completed practice in each Python-Set2 folder</li>
  <li>Can explain GIL, decorators, and async</li>
  <li>Demo-ready on Django and one Pipecat POC</li>
  <li>Reviewed C# vs Python cheat sheet</li>
</ul>
'''),
(31, "PEP Standards", '''
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
''', '''
<ul class="checklist">
  <li>Run <code>import this</code> in REPL and name 3 Zen lines</li>
  <li>Refactor one script to PEP 8 naming (snake_case, 4 spaces)</li>
  <li>Add a one-line docstring to every function in a practice file</li>
</ul>
'''),

(32, "Memory Management & Garbage Collection", '''
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
''', '''
<ul class="checklist">
  <li>Run <code>Projects/32_memory_gc.py</code> and watch refcount change</li>
  <li>Explain difference between <code>del x</code> and <code>x = None</code></li>
  <li>Describe when circular references need the GC</li>
</ul>
'''),

(33, "Logging", '''
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
''', '''
<ul class="checklist">
  <li>Replace <code>print</code> with <code>logging</code> in one practice script</li>
  <li>Configure DEBUG to console and INFO to file</li>
  <li>Use <code>logger.exception()</code> inside an <code>except</code> block once</li>
</ul>
'''),

(34, "Pydantic", '''
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
''', '''
<ul class="checklist">
  <li>Install: <code>pip install pydantic</code></li>
  <li>Run <code>python Projects/34_pydantic_demo.py</code></li>
  <li>Add one <code>field_validator</code> for a business rule</li>
</ul>
'''),

(35, "FastAPI with SQLAlchemy", '''
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
]


def build_nav():
    def links(start, end):
        return "".join(
            f'<a onclick="goSlide({n})">{n}. {t}</a>'
            for n, t, _, _ in CONTENT if start <= n <= end
        )
    return f'''<div class="slide active" id="slide-0">
<div class="nav-content">
  <h1>Python Training 2026</h1>
  <div class="sub">Batch 2 &middot; Core Topics + Real Projects</div>
  <div class="org">Click a topic below to jump to that slide</div>
  {audio_bar(0)}
  <div class="nav-grid">
    <div class="nav-section">
      <h3>Core Topics 1–10</h3>
      {links(1, 10)}
    </div>
    <div class="nav-section">
      <h3>Core Topics 11–17</h3>
      {links(11, 17)}
    </div>
    <div class="nav-section">
      <h3>Core Topics 18–23</h3>
      {links(18, 23)}
    </div>
    <div class="nav-section">
      <h3>Real Projects (Python-Set2)</h3>
      {links(24, 29)}
    </div>
    <div class="nav-section">
      <h3>Appendix</h3>
      {links(30, 30)}
    </div>
    <div class="nav-section">
      <h3>Extended Curriculum</h3>
      {links(31, 35)}
    </div>
  </div>
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
{NAV_BAR}
<script>{JS}</script>
</body>
</html>"""

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Generated {OUTPUT} ({len(html):,} bytes, {len(slides)} slides)")


if __name__ == "__main__":
    main()
