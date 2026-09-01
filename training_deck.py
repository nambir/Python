"""Shared HTML deck builder for PythonTraining.html and DotnetTraining.html."""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from build_training import CSS
from slide_code import highlight_csharp_step_pres, mark_important_in_step_pres, split_learn
from slide_io import convert_input_output_pres


@dataclass
class DeckConfig:
    title: str
    total_slides: int
    output: Path
    storage_key: str = "trainingSlide"
    scroll_key: str = "trainingScroll"
    accent_note: str = ""
    extra_slide_nums: list[int] = field(default_factory=list)
    show_audio: bool = False
    show_mindmap: bool = False
    mindmap_start: int | None = None
    mindmap_titles: dict[int, str] = field(default_factory=dict)


def make_nav_bar(cfg: DeckConfig) -> str:
    mindmap_btn = ""
    if cfg.show_mindmap and cfg.mindmap_start is not None:
        mindmap_btn = (
            f'<button type="button" class="btn-nav" style="background:#7c3aed" '
            f'onclick="goSlide({cfg.mindmap_start})" title="Open MindMap">'
            f"&#128200; MindMap</button>"
        )
    audio_btn = ""
    if cfg.show_audio:
        audio_btn = (
            '<button type="button" class="btn-audio-nav" onclick="togglePlay(current)" '
            'title="Play / pause current slide audio">&#128266; Audio</button>'
        )
    return f"""
<div class="nav-bar">
  <button class="btn-prev" onclick="prevSlide()">&larr; Prev</button>
  <button class="btn-nav" onclick="goSlide(0)">&#9776; Navigation</button>
  {mindmap_btn}
  {audio_btn}
  <span class="slide-info" id="slideInfo">Navigation</span>
  <button class="btn-next" onclick="nextSlide()">Next &rarr;</button>
</div>
"""


def make_deck_js(cfg: DeckConfig) -> str:
    extra = "".join(f"slideOrder.push({n});\n" for n in cfg.extra_slide_nums)
    notes_titles = json.dumps(cfg.mindmap_titles)
    notes_start = cfg.mindmap_start if cfg.mindmap_start is not None else 99999
    audio_block = ""
    if cfg.show_audio:
        audio_block = r"""
function fmtTime(sec) {
  if (!isFinite(sec) || sec < 0) sec = 0;
  const m = Math.floor(sec / 60);
  const s = Math.floor(sec % 60);
  return m + ':' + String(s).padStart(2, '0');
}
function getAudio(n) { return document.getElementById('audio-' + n); }
function getPlayBtn(n) { return document.getElementById('play-btn-' + n); }
function setPlayingUI(n, on) {
  const btn = getPlayBtn(n);
  if (btn) {
    btn.classList.toggle('playing', on);
    btn.innerHTML = on ? '&#9646;&#9646;' : '&#9654;';
  }
}
function updateTimeUI(n) {
  const audio = getAudio(n);
  const timeEl = document.getElementById('time-' + n);
  const seek = document.getElementById('seek-' + n);
  if (!audio || !timeEl) return;
  timeEl.textContent = fmtTime(audio.currentTime) + ' / ' + fmtTime(audio.duration);
  if (seek && audio.duration) seek.value = Math.round((audio.currentTime / audio.duration) * 1000);
}
let activeSlide = null;
function pauseAllExcept(keep) {
  slideOrder.forEach(i => {
    if (i === keep) return;
    const a = getAudio(i);
    if (a && !a.paused) a.pause();
    setPlayingUI(i, false);
  });
  if (keep === null) activeSlide = null;
}
function togglePlay(n) {
  const audio = getAudio(n);
  if (!audio) return;
  if (!audio.paused && activeSlide === n) { audio.pause(); setPlayingUI(n, false); activeSlide = null; return; }
  pauseAllExcept(n);
  audio.play().then(() => { activeSlide = n; setPlayingUI(n, true); }).catch(console.error);
}
function resetAudio(n) {
  const audio = getAudio(n);
  if (!audio) return;
  audio.pause(); audio.currentTime = 0; setPlayingUI(n, false);
  if (activeSlide === n) activeSlide = null;
  updateTimeUI(n);
}
function initAudioPlayers() {
  slideOrder.forEach(i => {
    const audio = getAudio(i);
    if (!audio) return;
    audio.addEventListener('timeupdate', () => { if (activeSlide === i) updateTimeUI(i); });
    audio.addEventListener('loadedmetadata', () => updateTimeUI(i));
    audio.addEventListener('ended', () => { setPlayingUI(i, false); if (activeSlide === i) activeSlide = null; });
  });
}
"""
    else:
        audio_block = "function initAudioPlayers() {}"

    split_key = (
        cfg.storage_key.replace("Slide", "SplitLeft")
        if "Slide" in cfg.storage_key
        else f"{cfg.storage_key}SplitLeft"
    )
    io_split_key = (
        cfg.storage_key.replace("Slide", "IoSplitLeft")
        if "Slide" in cfg.storage_key
        else f"{cfg.storage_key}IoSplitLeft"
    )

    return f"""
let current = 0;
const slideOrder = [0];
for (let i = 1; i <= {cfg.total_slides}; i++) slideOrder.push(i);
{extra}const totalTopics = {cfg.total_slides};
const notesTitles = {notes_titles};
const notesStart = {notes_start};
const SCROLL_KEY = '{cfg.scroll_key}';
const STORAGE_KEY = '{cfg.storage_key}';
let slideShowCount = 0;
{audio_block}

function saveSlideScroll(n, top) {{
  try {{
    const map = JSON.parse(sessionStorage.getItem(SCROLL_KEY) || '{{}}');
    map[String(n)] = Math.max(0, Math.round(top));
    sessionStorage.setItem(SCROLL_KEY, JSON.stringify(map));
  }} catch (_) {{}}
}}
function getSavedSlideScroll(n) {{
  try {{
    const map = JSON.parse(sessionStorage.getItem(SCROLL_KEY) || '{{}}');
    const v = parseInt(map[String(n)], 10);
    return Number.isFinite(v) && v >= 0 ? v : 0;
  }} catch (_) {{ return 0; }}
}}

function showSlide(n) {{
  if (!slideOrder.includes(n)) return;
  document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
  const el = document.getElementById('slide-' + n);
  if (el) {{
    el.classList.add('active');
    current = n;
    const info = document.getElementById('slideInfo');
    if (info) {{
      if (n === 0) info.textContent = 'Navigation';
      else if (n >= notesStart) info.textContent = 'MindMap · ' + (notesTitles[n] || n);
      else info.textContent = 'Slide ' + n + ' of ' + totalTopics;
    }}
    applySavedSplit(el);
    applySavedIoSplits(el);
    applySavedMcSplits(el);
    const hash = n === 0 ? 'nav' : String(n);
    if (location.hash.replace('#', '') !== hash) location.hash = hash;
    try {{ localStorage.setItem(STORAGE_KEY, String(n)); }} catch (_) {{}}
    const isFirstPaint = slideShowCount === 0;
    slideShowCount += 1;
    if (isFirstPaint || current === n) {{
      const y = getSavedSlideScroll(n);
      requestAnimationFrame(() => {{ el.scrollTop = y; }});
    }} else {{
      el.scrollTop = 0;
      saveSlideScroll(n, 0);
    }}
  }}
}}
function goSlide(n) {{ showSlide(n); }}
function nextSlide() {{
  const idx = slideOrder.indexOf(current);
  if (idx < slideOrder.length - 1) showSlide(slideOrder[idx + 1]);
}}
function prevSlide() {{
  const idx = slideOrder.indexOf(current);
  if (idx > 0) showSlide(slideOrder[idx - 1]);
}}
window.addEventListener('hashchange', () => {{
  const h = (location.hash || '').replace('#', '');
  const n = (h === '' || h === 'nav') ? 0 : (parseInt(h, 10) || 0);
  if (n !== current) showSlide(n);
}});
document.addEventListener('scroll', e => {{
  const slide = e.target.closest && e.target.closest('.slide.active');
  if (slide) saveSlideScroll(current, slide.scrollTop);
}}, true);

const SPLIT_KEY = '{split_key}';
let splitDragging = null;
function getSavedSplit() {{
  const v = parseFloat(localStorage.getItem(SPLIT_KEY) || '');
  // 5%–98%: code panel can collapse; divider stays so you can pull it back
  return (Number.isFinite(v) && v >= 5 && v <= 98) ? v : 48;
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
    div.title = 'Drag to resize — drag right to collapse code (bar stays so you can pull back)';
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
  pct = Math.max(5, Math.min(98, pct));
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

const IO_SPLIT_KEY = '{io_split_key}';
let ioSplitDragging = null;
function applyIoSplitTo(split, pct) {{ if (split) split.style.setProperty('--io-left', pct + '%'); }}
function applySavedIoSplits(root) {{
  const pct = parseFloat(localStorage.getItem(IO_SPLIT_KEY) || '58');
  (root || document).querySelectorAll('.io-split').forEach(s => applyIoSplitTo(s, pct));
}}
function initIoSplitDividers() {{
  document.querySelectorAll('.io-split-divider').forEach(div => {{
    if (div.dataset.ioSplitReady) return;
    div.dataset.ioSplitReady = '1';
    div.addEventListener('pointerdown', e => {{
      if (e.button !== 0) return;
      const split = div.closest('.io-split');
      if (!split) return;
      const rect = split.getBoundingClientRect();
      ioSplitDragging = {{ split, div, left: rect.left, width: rect.width }};
      div.classList.add('dragging');
      document.body.classList.add('io-split-dragging');
      e.preventDefault();
    }});
  }});
}}
document.addEventListener('pointermove', e => {{
  if (!ioSplitDragging) return;
  const {{ split, left, width }} = ioSplitDragging;
  if (width < 60) return;
  let pct = ((e.clientX - left) / width) * 100;
  pct = Math.max(20, Math.min(85, pct));
  applyIoSplitTo(split, pct);
  localStorage.setItem(IO_SPLIT_KEY, String(Math.round(pct * 10) / 10));
}});
function endIoSplitDrag() {{
  if (!ioSplitDragging) return;
  ioSplitDragging.div.classList.remove('dragging');
  document.body.classList.remove('io-split-dragging');
  ioSplitDragging = null;
}}
document.addEventListener('pointerup', endIoSplitDrag);
document.addEventListener('pointercancel', endIoSplitDrag);

const MC_SPLIT_KEY = 'trainingMcSplitLeft';
let mcRowDragging = null;
function applyMcSplitTo(row, pct) {{ if (row) row.style.setProperty('--mc-left', pct + '%'); }}
function applySavedMcSplits(root) {{
  const pct = parseFloat(localStorage.getItem(MC_SPLIT_KEY) || '50');
  (root || document).querySelectorAll('.mc-row').forEach(r => applyMcSplitTo(r, pct));
}}
function initMcRowDividers() {{
  document.querySelectorAll('.mc-row').forEach(row => {{
    const cols = [...row.children].filter(el => el.classList.contains('mc-col'));
    if (cols.length !== 2) return;
    let div = row.querySelector(':scope > .mc-row-divider');
    if (!div) {{
      div = document.createElement('div');
      div.className = 'mc-row-divider';
      div.title = 'Drag to resize';
      row.insertBefore(div, cols[1]);
    }}
    if (div.dataset.mcSplitReady) return;
    div.dataset.mcSplitReady = '1';
    div.addEventListener('pointerdown', e => {{
      if (e.button !== 0) return;
      const rect = row.getBoundingClientRect();
      mcRowDragging = {{ row, div, left: rect.left, width: rect.width }};
      div.classList.add('dragging');
      document.body.classList.add('mc-row-dragging');
      e.preventDefault();
    }});
  }});
}}
document.addEventListener('pointermove', e => {{
  if (!mcRowDragging) return;
  const {{ row, left, width }} = mcRowDragging;
  if (width < 60) return;
  let pct = ((e.clientX - left) / width) * 100;
  pct = Math.max(20, Math.min(85, pct));
  applyMcSplitTo(row, pct);
  localStorage.setItem(MC_SPLIT_KEY, String(Math.round(pct * 10) / 10));
}});
function endMcRowDrag() {{
  if (!mcRowDragging) return;
  mcRowDragging.div.classList.remove('dragging');
  document.body.classList.remove('mc-row-dragging');
  mcRowDragging = null;
}}
document.addEventListener('pointerup', endMcRowDrag);
document.addEventListener('pointercancel', endMcRowDrag);

function resetPlayground(btn) {{
  const box = btn.closest('.code-playground');
  if (!box) return;
  const ed = box.querySelector('.py-editor');
  const out = box.querySelector('.py-output');
  const status = box.querySelector('.py-status');
  if (ed) {{
    if (ed.dataset.original == null) ed.dataset.original = ed.defaultValue;
    ed.value = ed.dataset.original;
  }}
  if (out) {{
    out.classList.remove('err');
    if (ed && ed.dataset.expected) {{
      out.hidden = false;
      out.textContent = ed.dataset.expected;
    }} else {{
      out.hidden = true;
      out.textContent = '';
    }}
  }}
  if (status && box.dataset.lang === 'csharp') {{
    status.textContent = 'Expected below · ▶ Run = live execution';
  }} else if (status) {{
    status.textContent = '';
  }}
}}
function showExpectedOutput(btn) {{
  const box = btn.closest('.code-playground');
  if (!box) return;
  const ed = box.querySelector('.py-editor');
  const out = box.querySelector('.py-output');
  const status = box.querySelector('.py-status');
  const outLabel = box.querySelector('.py-output-label');
  if (!out) return;
  const exp = (ed && ed.dataset.expected) || out.textContent || '';
  out.hidden = false;
  out.classList.remove('err');
  out.textContent = exp || '(no expected output for this sample)';
  if (outLabel) outLabel.textContent = 'OUTPUT (expected)';
  if (status) status.textContent = 'Showing expected OUTPUT';
}}
function copyPlayground(btn) {{
  const box = btn.closest('.code-playground');
  if (!box) return;
  const ed = box.querySelector('.py-editor');
  const status = box.querySelector('.py-status');
  if (!ed) return;
  navigator.clipboard.writeText(ed.value).then(() => {{
    if (status) status.textContent = 'Copied!';
    setTimeout(() => {{
      if (status && box.dataset.lang === 'csharp')
        status.textContent = 'Expected below · ▶ Run = live execution';
    }}, 1200);
  }}).catch(() => {{
    if (status) status.textContent = 'Copy failed — select text manually';
  }});
}}
function _wrapForMono(code) {{
  const stripped = code.replace(/\\/\\/.*$/gm, '').replace(/\\/\\*[\\s\\S]*?\\*\\//g, '').trim();
  if (/\\b(class|struct|namespace|interface|record)\\s+\\w/.test(stripped) ||
      /\\bstatic\\s+(void|async\\s+Task)\\s+Main\\b/.test(stripped)) return code;
  const lines = code.split('\\n'), usings = [], body = [];
  for (const l of lines) {{
    if (/^\\s*using\\s+[\\w.]+\\s*;/.test(l)) usings.push(l.trim()); else body.push(l);
  }}
  ['using System;','using System.Collections.Generic;','using System.Linq;'].forEach(u => {{
    if (!usings.some(e => e.replace(/\\s+/g,'') === u.replace(/\\s+/g,''))) usings.push(u);
  }});
  return usings.join('\\n') + '\\n\\nclass Program {{\\n  static void Main() {{\\n' +
    body.map(l => '    ' + l).join('\\n') + '\\n  }}\\n}}';
}}
async function runCsharpPlayground(btn) {{
  const box = btn.closest('.code-playground');
  if (!box) return;
  const ed = box.querySelector('.py-editor');
  const out = box.querySelector('.py-output');
  const status = box.querySelector('.py-status');
  const outLabel = box.querySelector('.py-output-label');
  if (!ed) return;
  const code = ed.value.trim();
  if (!code) {{ if (status) status.textContent = 'No code to run'; return; }}
  btn.disabled = true;
  btn.textContent = '⏳ Running…';
  if (status) status.textContent = 'Compiling & running C# code…';
  if (out) {{ out.hidden = false; out.textContent = '⏳ Running…'; out.classList.remove('err'); }}
  if (outLabel) outLabel.textContent = 'OUTPUT (live)';
  const ac = new AbortController();
  const tid = setTimeout(() => ac.abort(), 30000);
  const execCode = _wrapForMono(code);
  try {{
    const resp = await fetch('https://wandbox.org/api/compile.json', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      signal: ac.signal,
      body: JSON.stringify({{ code: execCode, compiler: 'mono-6.12.0.199' }})
    }});
    clearTimeout(tid);
    if (!resp.ok) throw new Error('API ' + resp.status);
    const data = await resp.json();
    const stdout = data.program_output || '';
    const stderr = data.compiler_error || data.compiler_output || data.program_error || '';
    if (out) {{
      out.hidden = false;
      const txt = (stdout + stderr).trim();
      if (stderr && !stdout) {{ out.classList.add('err'); out.textContent = stderr.trim(); }}
      else {{ out.classList.remove('err'); out.textContent = txt || '(no output)'; }}
    }}
    if (status) status.textContent = (!stderr || stdout) ? '✓ Execution complete' : '✗ Compilation/runtime error';
  }} catch (e) {{
    clearTimeout(tid);
    const msg = (e.name === 'AbortError') ? 'Timed out' : 'API unavailable';
    if (out) {{ out.hidden = false; out.classList.add('err'); out.textContent = msg + ' — opening SharpLab as fallback'; }}
    if (status) status.textContent = msg + ' — falling back to SharpLab…';
    try {{ await navigator.clipboard.writeText(code); }} catch(_) {{}}
    setTimeout(() => window.open('https://sharplab.io/', '_blank', 'noopener'), 800);
  }} finally {{
    btn.disabled = false;
    btn.textContent = '▶ Run';
  }}
}}
function openSharpLabDirect(btn) {{
  const box = btn.closest('.code-playground');
  if (!box) return;
  const ed = box.querySelector('.py-editor');
  if (!ed) return;
  navigator.clipboard.writeText(ed.value).catch(() => {{}});
  window.open('https://sharplab.io/', '_blank', 'noopener');
}}
// Back-compat alias if any older markup still calls openSharpLab
async function openSharpLab(btn) {{ return runCsharpPlayground(btn); }}
let pyHeightDrag = null;
function initPyEditorTopResize() {{
  document.querySelectorAll('.py-resize-top').forEach(handle => {{
    if (handle.dataset.resizeReady) return;
    handle.dataset.resizeReady = '1';
    handle.addEventListener('pointerdown', e => {{
      if (e.button !== 0) return;
      const target = handle.nextElementSibling;
      if (!target) return;
      const isEditor = target.classList && target.classList.contains('py-editor');
      const isVs = target.classList && target.classList.contains('vs-editor');
      if (!isEditor && !isVs) return;
      const startY = e.clientY;
      const startH = target.getBoundingClientRect().height;
      pyHeightDrag = {{ target, startY, startH, handle }};
      handle.classList.add('dragging');
      document.body.classList.add('py-height-dragging');
      e.preventDefault();
    }});
  }});
}}
document.addEventListener('pointermove', e => {{
  if (!pyHeightDrag) return;
  const dy = e.clientY - pyHeightDrag.startY;
  const h = Math.max(120, pyHeightDrag.startH + dy);
  pyHeightDrag.target.style.height = h + 'px';
  pyHeightDrag.target.style.maxHeight = 'none';
}});
document.addEventListener('pointerup', () => {{
  if (!pyHeightDrag) return;
  pyHeightDrag.handle.classList.remove('dragging');
  document.body.classList.remove('py-height-dragging');
  pyHeightDrag = null;
}});

let csharpDrag = {{ active: false, win: null, startX: 0, startY: 0, origLeft: 0, origTop: 0 }};
let csharpResize = {{ active: false, win: null, startX: 0, startY: 0, origW: 0, origH: 0 }};
function bringCsharpWinToFront(win) {{
  document.querySelectorAll('.csharp-float-win.open').forEach(w => {{ w.style.zIndex = '2000'; }});
  win.style.zIndex = '2010';
}}
function centerCsharpWin(win) {{
  const w = win.offsetWidth || 720;
  const h = win.offsetHeight || 480;
  win.style.left = Math.max(12, (window.innerWidth - w) / 2) + 'px';
  win.style.top = Math.max(12, (window.innerHeight - h) / 2) + 'px';
}}
function openCsharpWin(id) {{
  const el = document.getElementById('csharp-win-' + id);
  if (!el) return;
  el.classList.add('open');
  bringCsharpWinToFront(el);
  if (!el.dataset.positioned) {{
    centerCsharpWin(el);
    el.dataset.positioned = '1';
  }}
}}
function closeCsharpWin(id) {{
  const el = document.getElementById('csharp-win-' + id);
  if (el) el.classList.remove('open');
}}
function closeAllCsharpWins() {{
  document.querySelectorAll('.csharp-float-win.open').forEach(el => el.classList.remove('open'));
}}
function toggleImgFloatFit(btn) {{
  const win = btn.closest('.csharp-float-win');
  if (!win) return;
  const body = win.querySelector('.csharp-float-body-img');
  if (!body) return;
  const full = body.classList.toggle('img-fullsize');
  btn.textContent = full ? '100%' : 'Fit';
}}
function initCsharpFloatWindows() {{
  document.querySelectorAll('.csharp-float-win').forEach(win => {{
    if (win.dataset.csharpInit === '1') return;
    win.dataset.csharpInit = '1';
    const hdr = win.querySelector('.csharp-float-hdr');
    if (hdr) {{
      hdr.addEventListener('pointerdown', (e) => {{
        if (e.button !== 0) return;
        if (e.target.closest('.csharp-float-close')) return;
        if (e.target.closest('.csharp-float-resize')) return;
        bringCsharpWinToFront(win);
        csharpDrag.active = true;
        csharpDrag.win = win;
        const rect = win.getBoundingClientRect();
        csharpDrag.startX = e.clientX;
        csharpDrag.startY = e.clientY;
        csharpDrag.origLeft = rect.left;
        csharpDrag.origTop = rect.top;
        win.classList.add('dragging');
        try {{ hdr.setPointerCapture(e.pointerId); }} catch (_) {{}}
        e.preventDefault();
      }});
    }}
    const handle = win.querySelector('.csharp-float-resize');
    if (handle) {{
      handle.addEventListener('pointerdown', (e) => {{
        if (e.button !== 0) return;
        bringCsharpWinToFront(win);
        csharpResize.active = true;
        csharpResize.win = win;
        const rect = win.getBoundingClientRect();
        csharpResize.startX = e.clientX;
        csharpResize.startY = e.clientY;
        csharpResize.origW = rect.width;
        csharpResize.origH = rect.height;
        win.classList.add('resizing');
        try {{ handle.setPointerCapture(e.pointerId); }} catch (_) {{}}
        e.preventDefault();
        e.stopPropagation();
      }});
    }}
  }});
  document.addEventListener('pointermove', (e) => {{
    if (csharpDrag.active && csharpDrag.win) {{
      const win = csharpDrag.win;
      const dx = e.clientX - csharpDrag.startX;
      const dy = e.clientY - csharpDrag.startY;
      const w = win.offsetWidth;
      const h = win.offsetHeight;
      const left = Math.min(Math.max(0, csharpDrag.origLeft + dx), Math.max(0, window.innerWidth - w));
      const top = Math.min(Math.max(0, csharpDrag.origTop + dy), Math.max(0, window.innerHeight - h));
      win.style.left = left + 'px';
      win.style.top = top + 'px';
      return;
    }}
    if (csharpResize.active && csharpResize.win) {{
      const win = csharpResize.win;
      const dx = e.clientX - csharpResize.startX;
      const dy = e.clientY - csharpResize.startY;
      const rect = win.getBoundingClientRect();
      const maxW = Math.max(360, window.innerWidth - rect.left - 8);
      const maxH = Math.max(240, window.innerHeight - rect.top - 8);
      win.style.width = Math.min(Math.max(360, csharpResize.origW + dx), maxW) + 'px';
      win.style.height = Math.min(Math.max(240, csharpResize.origH + dy), maxH) + 'px';
      win.style.maxWidth = 'none';
      win.style.maxHeight = 'none';
    }}
  }});
  const endCsharpPointer = () => {{
    if (csharpDrag.win) csharpDrag.win.classList.remove('dragging');
    if (csharpResize.win) csharpResize.win.classList.remove('resizing');
    csharpDrag.active = false;
    csharpDrag.win = null;
    csharpResize.active = false;
    csharpResize.win = null;
  }};
  document.addEventListener('pointerup', endCsharpPointer);
  document.addEventListener('pointercancel', endCsharpPointer);
}}
document.addEventListener('keydown', (e) => {{
  if (e.key === 'Escape') closeAllCsharpWins();
}});

document.addEventListener('DOMContentLoaded', () => {{
  try {{ initAudioPlayers(); }} catch (err) {{ console.warn('audio init', err); }}
  try {{ initCsharpFloatWindows(); }} catch (err) {{ console.warn('vguide init', err); }}
  try {{
    document.querySelectorAll('.py-editor').forEach(ed => {{
      ed.dataset.original = ed.value;
    }});
    initPyEditorTopResize();
    initSplitDividers();
    applySavedSplit(document);
    initIoSplitDividers();
    applySavedIoSplits(document);
    initMcRowDividers();
    applySavedMcSplits(document);
  }} catch (err) {{ console.warn('layout init', err); }}
  const h = (location.hash || '').replace('#', '');
  let start = (h === '' || h === 'nav') ? 0 : (parseInt(h, 10) || 0);
  if (!start) {{
    try {{
      const saved = parseInt(localStorage.getItem(STORAGE_KEY) || '', 10);
      if (Number.isFinite(saved)) start = saved;
    }} catch (_) {{}}
  }}
  showSlide(start);
}});
"""


def slide_hdr(
    n: int,
    title: str,
    *,
    total_slides: int,
    module_label: str,
    definition: str = "",
    show_audio: bool = False,
) -> str:
    audio = ""
    if show_audio:
        audio = f"""<div class="audio-player" id="player-{n}" data-slide="{n}">
  <audio id="audio-{n}" preload="metadata" src="audio/slide-{n:02d}.mp3"></audio>
</div>"""
    return f'''<div class="slide-hdr">
  <div class="slide-meta">Slide {n} of {total_slides} &middot; {html.escape(module_label)}</div>
  <div class="slide-title">{html.escape(title)}</div>
  {audio}
</div>'''


def topic_intro(
    n: int,
    *,
    meta: dict,
    beginner: dict,
    extra_blocks: list[str] | None = None,
    flowchart_fn=None,
    diagram_fn=None,
    visual_guide_fn=None,
) -> str:
    parts: list[str] = []
    if meta.get("primary"):
        parts.append(
            f'<div class="callout"><b>What this primarily describes:</b> {meta["primary"]}</div>'
        )
    if meta.get("definition"):
        parts.append(f'<h3>Definition</h3><div class="def-block">{meta["definition"]}</div>')
        if visual_guide_fn:
            vg = visual_guide_fn(n)
            if vg:
                parts.append(vg)
        if flowchart_fn:
            fc = flowchart_fn(n)
            if fc:
                parts.append(fc)
        if diagram_fn:
            dg = diagram_fn(n)
            if dg:
                parts.append(dg)
    elif visual_guide_fn:
        vg = visual_guide_fn(n)
        if vg:
            parts.append(vg)
    for block in extra_blocks or []:
        parts.append(block)
    steps = beginner.get("steps", [])
    if steps:
        parts.append('<h3>Step-by-step (beginner friendly)</h3><ul class="learn-steps">')
        for s in steps:
            parts.append(f'<li><b>{s["title"]}</b><br>{s["body"]}</li>')
        parts.append("</ul>")
    return "".join(parts)


def interview_box(n: int, *, meta: dict, beginner: dict) -> str:
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


def render_slide(
    n: int,
    title: str,
    learn: str,
    practice: str,
    *,
    cfg: DeckConfig,
    meta: dict,
    beginner: dict,
    module_label: str,
    extra_left: str = "",
    code_lang: str = "python",
    flowchart_fn=None,
    diagram_fn=None,
    visual_guide_fn=None,
) -> str:
    notes_html, codes_html = split_learn(learn, lang=code_lang)
    notes_html = extra_left + notes_html + interview_box(n, meta=meta, beginner=beginner)
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
{slide_hdr(n, title, total_slides=cfg.total_slides, module_label=module_label, definition=meta.get("definition", ""), show_audio=cfg.show_audio)}
<div class="slide-body">
  <div class="{split_cls}">
    <div class="panel-left">
      {topic_intro(n, meta=meta, beginner=beginner, flowchart_fn=flowchart_fn, diagram_fn=diagram_fn, visual_guide_fn=visual_guide_fn)}
      {notes_html}
      <div class="panel-practice">
        <h3>Practice</h3>
        {practice}
      </div>
    </div>
    {divider}
    {code_panel}
  </div>
</div>
</div>'''


def build_nav(
    *,
    cfg: DeckConfig,
    titles: dict[int, str],
    sections: list[tuple[str, list[int]]],
    subtopics: dict[int, list[str]] | None = None,
    nav_intro: str = "",
) -> str:
    subtopics = subtopics or {}

    def topic_block(n: int) -> str:
        if n not in titles:
            return ""
        subs = subtopics.get(n, [])
        sub_html = ""
        if subs:
            items = "".join(
                f'<li><a href="#{n}" onclick="goSlide({n}); return false;">{html.escape(s)}</a></li>'
                for s in subs
            )
            sub_html = f'<ul class="nav-subs">{items}</ul>'
        return (
            f'<div class="nav-topic">'
            f'<a class="nav-main" href="#{n}" onclick="goSlide({n}); return false;">'
            f"{n}. {html.escape(titles[n])}</a>"
            f"{sub_html}</div>"
        )

    n_sec = len(sections)
    # 6-section decks use CSS .nav-section-1 … 6 spans (Python / full Dotnet matrix).
    use_css_spans = n_sec == 6
    if n_sec == 1:
        spans = [12]
    elif n_sec == 2:
        spans = [6, 6]
    elif n_sec == 3:
        spans = [4, 4, 4]
    elif n_sec == 7:
        spans = [3, 3, 3, 3, 4, 5, 3]
    elif use_css_spans:
        spans = [None] * n_sec
    else:
        spans = [max(3, 12 // n_sec)] * n_sec

    def _section_div(index: int, title: str, nums: list[int]) -> str:
        span = spans[index - 1]
        style = "" if span is None else f' style="grid-column: span {span}"'
        return (
            f'    <div class="nav-section nav-section-{index}"{style}>\n'
            f"      <h3>{html.escape(title)}</h3>\n"
            f'      <div class="nav-links">{"".join(topic_block(n) for n in nums)}</div>\n'
            f"    </div>\n"
        )

    section_html = "".join(
        _section_div(index, title, nums)
        for index, (title, nums) in enumerate(sections, 1)
    )
    intro = nav_intro or f"""
  <h1>{html.escape(cfg.title)}</h1>
  <p class="sub">Skill-depth curriculum — review deck</p>
"""
    return f'''<div class="slide active" id="slide-0">
<div class="nav-content">
{intro}
  <div class="nav-grid">
{section_html}  </div>
</div>
</div>'''


def build_deck(
    *,
    cfg: DeckConfig,
    content: list[tuple[int, str, str, str]],
    meta: dict[int, dict],
    beginner: dict[int, dict],
    module_map: dict[int, str],
    sections: list[tuple[str, list[int]]],
    subtopics: dict[int, list[str]] | None = None,
    nav_intro: str = "",
    code_lang: str = "python",
    extra_left_for: dict[int, str] | None = None,
    flowchart_fn=None,
    diagram_fn=None,
    visual_guide_fn=None,
) -> None:
    titles = {n: t for n, t, _, _ in content}
    slides = [build_nav(cfg=cfg, titles=titles, sections=sections, subtopics=subtopics, nav_intro=nav_intro)]
    for num, title, learn, practice in content:
        slides.append(
            render_slide(
                num,
                title,
                learn,
                practice,
                cfg=cfg,
                meta=meta.get(num, {}),
                beginner=beginner.get(num, {}),
                module_label=module_map.get(num, "Core"),
                extra_left=(extra_left_for or {}).get(num, ""),
                code_lang=code_lang,
                flowchart_fn=flowchart_fn,
                diagram_fn=diagram_fn,
                visual_guide_fn=visual_guide_fn,
            )
        )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(cfg.title)}</title>
<style>{CSS}</style>
</head>
<body>
{"".join(slides)}
{make_nav_bar(cfg)}
<script>{make_deck_js(cfg)}</script>
</body>
</html>"""

    page = convert_input_output_pres(page)
    if code_lang == "csharp":
        page = highlight_csharp_step_pres(page)
    page = mark_important_in_step_pres(page)
    cfg.output.parent.mkdir(parents=True, exist_ok=True)
    cfg.output.write_text(page, encoding="utf-8")
    print(f"Generated {cfg.output} ({len(page):,} bytes, {cfg.total_slides} slides)")
