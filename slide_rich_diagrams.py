"""Rich multi-layer build maps — same visual language as the GIL diagram (Slide 20).

Each curriculum slide gets one primary rich map under Definition.
"""

from __future__ import annotations


def _chips(items: list[str], *, active: int | None = None, active_label: str = "active") -> str:
    parts = []
    for i, text in enumerate(items):
        if active is not None and i == active:
            parts.append(
                f'<div class="rich-chip rich-chip-active">{text}'
                f'<span>{active_label}</span></div>'
            )
        else:
            parts.append(f'<div class="rich-chip">{text}</div>')
    return f'<div class="rich-chips">{"".join(parts)}</div>'


def _gate(title: str, subtitle: str) -> str:
    return (
        f'<div class="rich-gate"><b>{title}</b>'
        f"<span>{subtitle}</span></div>"
    )


def _choice_card(
    *,
    badge: str,
    ok: bool,
    title: str,
    detail: str,
    code: str = "",
    em: str = "",
) -> str:
    kind = "ok" if ok else "notok"
    code_html = f"<code>{code}</code>" if code else ""
    em_html = f"<em>{em}</em>" if em else ""
    return (
        f'<div class="rich-choice-card rich-{kind}">'
        f'<div class="rich-badge rich-badge-{kind}">{badge}</div>'
        f"<b>{title}</b><span>{detail}</span>{code_html}{em_html}</div>"
    )


def rich_map(title: str, stages: list[dict], footer: str = "") -> str:
    """Beautiful layered build map (cores → box → fork style)."""
    blocks: list[str] = [f"<h3>{title}</h3>", '<div class="rich-diagram">']

    for i, stage in enumerate(stages):
        if i:
            blocks.append('<div class="rich-v-arrow">&darr;</div>')

        label = stage.get("label", "")
        blocks.append('<div class="rich-layer">')
        if label:
            blocks.append(f'<div class="rich-layer-label">{label}</div>')

        kind = stage["kind"]

        if kind == "chips":
            blocks.append(_chips(stage["items"], active=stage.get("active")))
            if stage.get("caption"):
                blocks.append(f'<p class="rich-caption">{stage["caption"]}</p>')

        elif kind == "box":
            blocks.append('<div class="rich-box">')
            if stage.get("title"):
                blocks.append(f'<div class="rich-box-title">{stage["title"]}</div>')
            if stage.get("items"):
                blocks.append(
                    _chips(
                        stage["items"],
                        active=stage.get("active"),
                        active_label=stage.get("active_label", "active"),
                    )
                )
            if stage.get("gate"):
                g_title, g_sub = stage["gate"]
                blocks.append(_gate(g_title, g_sub))
            if stage.get("body"):
                blocks.append(f'<p class="rich-caption">{stage["body"]}</p>')
            if stage.get("steps"):
                step_html = "".join(
                    f'<div class="rich-step"><b>{lab}</b><span>{det}</span></div>'
                    for lab, det in stage["steps"]
                )
                blocks.append(f'<div class="rich-steps">{step_html}</div>')
            blocks.append("</div>")
            if stage.get("caption"):
                blocks.append(f'<p class="rich-caption">{stage["caption"]}</p>')
            if stage.get("out"):
                blocks.append(f'<p class="rich-caption rich-out">{stage["out"]}</p>')

        elif kind == "fork":
            if stage.get("question"):
                blocks.append(f'<div class="rich-choice-q">{stage["question"]}</div>')
            left = stage["left"]
            right = stage["right"]
            blocks.append('<div class="rich-choice-row">')
            blocks.append(_choice_card(**left))
            blocks.append('<div class="rich-choice-vs">vs</div>')
            blocks.append(_choice_card(**right))
            blocks.append("</div>")

        elif kind == "grid":
            tiles = "".join(
                f'<div class="rich-tile"><b>{lab}</b><span>{det}</span></div>'
                for lab, det in stage["cells"]
            )
            blocks.append(f'<div class="rich-grid">{tiles}</div>')
            if stage.get("caption"):
                blocks.append(f'<p class="rich-caption">{stage["caption"]}</p>')

        elif kind == "pipeline":
            nodes = []
            for j, (lab, det) in enumerate(stage["steps"]):
                if j:
                    nodes.append('<div class="rich-pipe-arrow">&rarr;</div>')
                nodes.append(
                    f'<div class="rich-pipe-node"><b>{lab}</b><span>{det}</span></div>'
                )
            blocks.append(f'<div class="rich-pipeline">{"".join(nodes)}</div>')
            if stage.get("caption"):
                blocks.append(f'<p class="rich-caption">{stage["caption"]}</p>')

        elif kind == "cycle":
            nodes = []
            for j, (lab, det) in enumerate(stage["steps"]):
                nodes.append(
                    f'<div class="rich-cycle-node"><b>{lab}</b><span>{det}</span></div>'
                )
                if j < len(stage["steps"]) - 1:
                    nodes.append('<div class="rich-pipe-arrow">&rarr;</div>')
                else:
                    nodes.append('<div class="rich-pipe-arrow">&circlearrowleft;</div>')
            blocks.append(f'<div class="rich-pipeline rich-cycle">{"".join(nodes)}</div>')
            if stage.get("caption"):
                blocks.append(f'<p class="rich-caption">{stage["caption"]}</p>')

        else:
            raise ValueError(f"Unknown rich stage kind: {kind}")

        blocks.append("</div>")

    if footer:
        blocks.append(f'<div class="rich-note">{footer}</div>')
    blocks.append("</div>")
    return "\n".join(blocks)


def _gil_visual_sections() -> str:
    """Sections 1–6 of the Threading & GIL visual guide (sharp HTML, not a PNG)."""
    return r'''
  <!-- 1. Hardware -->
  <div class="vg-sec">
    <div class="vg-sec-h"><span class="vg-num">1</span> Hardware: Physical Core vs Logical CPU</div>
    <p class="vg-lead">A core runs instructions. OS puts threads on logical CPUs (time-sliced).</p>
    <div class="vg-chip-box">
      <div class="vg-chip-title">CPU Chip (Example: 4 physical cores, 8 logical CPUs)</div>
      <div class="vg-phys-row">
        <div class="vg-phys">Core 1<br><small>(Physical)</small></div>
        <div class="vg-phys">Core 2<br><small>(Physical)</small></div>
        <div class="vg-phys">Core 3<br><small>(Physical)</small></div>
        <div class="vg-phys">Core 4<br><small>(Physical)</small></div>
      </div>
      <div class="vg-logic-row">
        <div class="vg-logic-pair"><div class="vg-logic">CPU 1</div><div class="vg-logic">CPU 2</div></div>
        <div class="vg-logic-pair"><div class="vg-logic">CPU 3</div><div class="vg-logic">CPU 4</div></div>
        <div class="vg-logic-pair"><div class="vg-logic">CPU 5</div><div class="vg-logic">CPU 6</div></div>
        <div class="vg-logic-pair"><div class="vg-logic">CPU 7</div><div class="vg-logic">CPU 8</div></div>
      </div>
      <div class="vg-sched">
        <b>OS Scheduler</b>
        <span>Places threads on logical CPUs many times per second</span>
      </div>
    </div>
  </div>

  <!-- 2. Process vs Thread -->
  <div class="vg-sec">
    <div class="vg-sec-h"><span class="vg-num">2</span> Process vs Thread (OS Level)</div>
    <p class="vg-lead">Two ways to do “many things at once”</p>
    <table class="vg-tbl">
      <tr><th></th><th>What</th><th>Memory</th><th>Start Cost</th><th>Example</th></tr>
      <tr>
        <td class="vg-td-lab vg-lab-proc">Process</td>
        <td>One running program instance</td>
        <td>Own memory space (isolated)</td>
        <td>Heavier</td>
        <td>3 Python apps = 3 processes</td>
      </tr>
      <tr>
        <td class="vg-td-lab vg-lab-thr">Thread</td>
        <td>One execution path inside a process</td>
        <td>Shares process memory</td>
        <td>Lighter</td>
        <td>Each app can create many threads</td>
      </tr>
    </table>
    <div class="vg-two">
      <div class="vg-panel">
        <div class="vg-panel-h">One Python App (one process, many threads)</div>
        <div class="vg-proc-box">
          <b>Process: python.exe</b> <span>(App 1 — e.g. Flask server)</span>
          <div class="vg-main-thr">Main thread</div>
          <div class="vg-thr-row">
            <div class="vg-thr">Thread-2<br><small>download worker</small></div>
            <div class="vg-thr">Thread-3<br><small>download worker</small></div>
            <div class="vg-thr">Thread-4<br><small>download worker</small></div>
          </div>
          <div class="vg-shared">Shared: variables, files, heap, sockets</div>
        </div>
      </div>
      <div class="vg-panel">
        <div class="vg-panel-h">Three Separate Python Apps (3 processes)</div>
        <div class="vg-apps3">
          <div class="vg-app"><b>App 1</b><code>python api.py</code><div class="vg-app-proc">Process 1<br><small>Own memory, own threads</small></div></div>
          <div class="vg-app"><b>App 2</b><code>python worker.py</code><div class="vg-app-proc">Process 2<br><small>Own memory, own threads</small></div></div>
          <div class="vg-app"><b>App 3</b><code>python notebook</code><div class="vg-app-proc">Process 3<br><small>Own memory, own threads</small></div></div>
        </div>
        <p class="vg-foot">Total: at least <b>3 processes</b> (one per app you launched)</p>
      </div>
    </div>
  </div>

  <!-- 3. GIL -->
  <div class="vg-sec">
    <div class="vg-sec-h"><span class="vg-num">3</span> CPython GIL (Inside One Python Process)</div>
    <p class="vg-lead">GIL limits Python bytecode execution <b>per process</b>, not per machine.</p>
    <div class="vg-two">
      <div class="vg-panel">
        <div class="vg-panel-h">One Python Process, 4 Threads, GIL</div>
        <div class="vg-gil-center">
          <div class="vg-thr-ring">
            <div class="vg-thr">Thread 1</div>
            <div class="vg-thr">Thread 2</div>
            <div class="vg-thr">Thread 3</div>
            <div class="vg-thr">Thread 4</div>
          </div>
          <div class="vg-gil-lock">&#128274; <b>GIL</b></div>
          <div class="vg-callout-y">Only <b>ONE</b> thread runs Python bytecode at a time.<br>(I/O operations often release the GIL)</div>
        </div>
      </div>
      <div class="vg-panel">
        <div class="vg-panel-h">Three Python Apps on 4 Cores (Each has its own GIL)</div>
        <div class="vg-cores4">
          <div class="vg-core-card">
            <div class="vg-core-lab">Core 1</div>
            <div class="vg-mini-proc">Process 1 (App 1)</div>
            <div class="vg-gil-sm">&#128274; GIL #1</div>
            <div class="vg-runner">Python bytecode runner</div>
          </div>
          <div class="vg-core-card">
            <div class="vg-core-lab">Core 2</div>
            <div class="vg-mini-proc">Process 2 (App 2)</div>
            <div class="vg-gil-sm">&#128274; GIL #2</div>
            <div class="vg-runner">Python bytecode runner</div>
          </div>
          <div class="vg-core-card">
            <div class="vg-core-lab">Core 3</div>
            <div class="vg-mini-proc">Process 3 (App 3)</div>
            <div class="vg-gil-sm">&#128274; GIL #3</div>
            <div class="vg-runner">Python bytecode runner</div>
          </div>
          <div class="vg-core-card vg-idle">
            <div class="vg-core-lab">Core 4</div>
            <div class="vg-idle-txt">Idle or other apps</div>
          </div>
        </div>
        <p class="vg-foot">Each process has its <b>OWN GIL</b> → apps can use different cores in parallel for Python CPU work.</p>
      </div>
    </div>
  </div>

  <!-- 4. When threads help -->
  <div class="vg-sec">
    <div class="vg-sec-h"><span class="vg-num">4</span> When Threads Help vs When They Don’t</div>
    <p class="vg-lead">Threads help I/O-bound work. For CPU-bound Python, use processes for real parallelism.</p>
    <div class="vg-two">
      <div class="vg-panel vg-io">
        <div class="vg-panel-h vg-h-io">I/O-bound (Use ThreadPool)</div>
        <p class="vg-ex">Examples: download, DB wait, disk read</p>
        <div class="vg-timeline">
          <div class="vg-tl-row"><span>T1</span><div class="vg-bar"><i class="vg-req">Request</i><i class="vg-wait">(waiting)</i><i class="vg-done">Done</i></div></div>
          <div class="vg-tl-row"><span>T2</span><div class="vg-bar"><i class="vg-req">Request</i><i class="vg-wait">(waiting)</i><i class="vg-done">Done</i></div></div>
          <div class="vg-tl-row"><span>T3</span><div class="vg-bar"><i class="vg-req">Request</i><i class="vg-wait">(waiting)</i><i class="vg-done">Done</i></div></div>
        </div>
        <p class="vg-foot">While one waits, others run. <b>GIL is released during wait.</b></p>
      </div>
      <div class="vg-panel vg-cpu">
        <div class="vg-panel-h vg-h-cpu">CPU-bound (Use ProcessPool)</div>
        <p class="vg-ex">Examples: resize image, heavy loop in pure Python</p>
        <div class="vg-parallel">
          <div class="vg-par"><span>P1</span><div class="vg-cpu-bar">CPU Work</div></div>
          <div class="vg-par"><span>P2</span><div class="vg-cpu-bar">CPU Work</div></div>
          <div class="vg-par"><span>P3</span><div class="vg-cpu-bar">CPU Work</div></div>
          <div class="vg-par"><span>P4</span><div class="vg-cpu-bar">CPU Work</div></div>
        </div>
        <p class="vg-foot">Each process has its own GIL. Runs <b>truly in parallel</b> on cores.</p>
      </div>
    </div>
  </div>

  <!-- 5. Worked example -->
  <div class="vg-sec">
    <div class="vg-sec-h"><span class="vg-num">5</span> Worked Example: 3 Apps + Pools (Numbers)</div>
    <table class="vg-tbl vg-tbl-num">
      <tr><th>Setup</th><th>Processes (typical)</th><th>Threads (typical)</th></tr>
      <tr>
        <td>Open <code>api.py</code>, <code>worker.py</code>, notebook</td>
        <td><b>3</b></td>
        <td>3 main threads (1 each)</td>
      </tr>
      <tr>
        <td><code>api.py</code> uses <code>ThreadPoolExecutor(4)</code></td>
        <td>still <b>1</b> process for api</td>
        <td>1 main + 4 pool = <b>5 threads</b> in api</td>
      </tr>
      <tr>
        <td><code>worker.py</code> uses <code>ProcessPoolExecutor(4)</code></td>
        <td>1 parent + 4 workers = <b>5 processes</b></td>
        <td>Parent has threads; each worker has 1 main thread</td>
      </tr>
      <tr class="vg-total">
        <td><b>Rough total on machine</b></td>
        <td><b>3 + 4 worker children = 7 processes</b></td>
        <td>varies by app</td>
      </tr>
    </table>
    <p class="vg-foot">Counts vary: libraries, servers, Jupyter, IDEs may add more.</p>
  </div>

  <!-- 6. Code & pick -->
  <div class="vg-sec">
    <div class="vg-sec-h"><span class="vg-num">6</span> Code &amp; Pick Guide</div>
    <div class="vg-three">
      <div class="vg-code-col">
        <div class="vg-code vg-code-io"><div class="vg-code-lab">I/O-bound</div><pre># I/O-bound → use threads (one process)
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as pool:
    images = list(pool.map(download, urls))</pre></div>
        <div class="vg-code vg-code-cpu"><div class="vg-code-lab">CPU-bound</div><pre># CPU-bound → use processes (own GIL each)
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=4) as pool:
    out = list(pool.map(heavy_resize, images))</pre></div>
      </div>
      <div class="vg-panel vg-pick">
        <div class="vg-panel-h">Pick Rule (Big Idea)</div>
        <ul>
          <li>Waiting on network / disk → <b>ThreadPool</b></li>
          <li>Crunching Python CPU → <b>ProcessPool</b></li>
          <li>Many separate apps → already separate processes + separate GILs</li>
        </ul>
      </div>
      <div class="vg-panel">
        <div class="vg-panel-h">Quick C# Comparison</div>
        <table class="vg-tbl vg-tbl-sm">
          <tr><th>Idea</th><th>C#</th><th>Python</th></tr>
          <tr><td>Thread</td><td>Thread / Task.Run</td><td><code>threading.Thread</code></td></tr>
          <tr><td>Async I/O</td><td>async / await Task</td><td><code>async</code> / coroutine</td></tr>
          <tr><td>Process</td><td>Process</td><td><code>multiprocessing</code></td></tr>
        </table>
      </div>
    </div>
  </div>
'''


def gil_build_diagram() -> str:
    """Slide 20 — HTML guide on-slide; detached window shows the JPG visual guide."""
    sections = _gil_visual_sections()
    return (
        '''
<div class="vg-guide">
  <div class="vg-title">Threading &amp; GIL (CPython) – Visual Guide</div>
'''
        + sections
        + '''
</div>
'''
    )



# ── All curriculum slides (1–35) ─────────────────────────────────────────────

RICH_DIAGRAMS: dict[int, str] = {
    1: rich_map(
        "Build map — how a .py file runs",
        [
            {
                "kind": "chips",
                "label": "1. You write",
                "items": [".py source", "plain text"],
                "caption": "No separate compile-to-DLL step like C#",
            },
            {
                "kind": "box",
                "label": "2. CPython interpreter",
                "title": "One process &mdash; <code>python app.py</code>",
                "steps": [
                    ("Compiler", "source → bytecode (.pyc)"),
                    ("Virtual machine", "runs bytecode step by step"),
                    ("Libraries", "os · json · pathlib feed the VM"),
                ],
                "gate": ("Result", "running program / output"),
            },
            {
                "kind": "fork",
                "label": "3. Deploy style",
                "question": "How do teams usually ship it?",
                "left": {
                    "badge": "Python",
                    "ok": True,
                    "title": "Source / package / container",
                    "detail": "run with python or image",
                    "code": "pip / docker",
                    "em": "often ships as code + deps",
                },
                "right": {
                    "badge": "C#",
                    "ok": False,
                    "title": "Compiled assembly",
                    "detail": ".dll / .exe then CLR/JIT",
                    "code": "dotnet publish",
                    "em": "build before run",
                },
            },
        ],
        footer="<b>Remember:</b> Python still compiles to bytecode — then the interpreter executes it.",
    ),
    2: rich_map(
        "Build map — setup → verify → run",
        [
            {
                "kind": "chips",
                "label": "1. Install (Windows)",
                "items": ["python.org", "Add to PATH", "pip"],
                "caption": "Miss PATH → <code>python</code> not recognized",
            },
            {
                "kind": "box",
                "label": "2. Verify",
                "title": "Terminal checks",
                "steps": [
                    ("python --version", "interpreter OK"),
                    ("pip --version", "or python -m pip"),
                    ("py -3.12", "pick a version on Windows"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. How do you run code?",
                "question": "Quick test or full program?",
                "left": {
                    "badge": "REPL",
                    "ok": True,
                    "title": "Interactive",
                    "detail": "type python → >>> prompt",
                    "code": ">>> print(1+1)",
                    "em": "experiments only",
                },
                "right": {
                    "badge": "Script / IDE",
                    "ok": True,
                    "title": "File + debugger",
                    "detail": "python hello.py · F5 in Cursor",
                    "code": "if __name__ == '__main__':",
                    "em": "define functions before calling them",
                },
            },
        ],
        footer="<b>Order matters:</b> scripts run top → bottom (unlike C# method order).",
    ),
    3: rich_map(
        "Build map — three learning layers",
        [
            {
                "kind": "chips",
                "label": "1. Open once",
                "items": ["Repo root", "one Cursor window", "Python 3.12"],
            },
            {
                "kind": "box",
                "label": "2. Workspace layers",
                "title": "Theory → short drill → real app",
                "steps": [
                    ("Slides", "PythonTraining.html — concepts"),
                    ("Projects/", "tiny practice files"),
                    ("Python-Set2/", "full demos & apps"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Per project",
                "question": "How do you keep deps clean?",
                "left": {
                    "badge": "Do",
                    "ok": True,
                    "title": "One .venv per project",
                    "detail": "isolate packages",
                    "code": "python -m venv .venv",
                    "em": "+ requirements.txt",
                },
                "right": {
                    "badge": "Avoid",
                    "ok": False,
                    "title": "Global pip install",
                    "detail": "version clashes across apps",
                    "code": "pip install … (system)",
                    "em": "breaks other projects",
                },
            },
        ],
        footer="<b>Goal:</b> read the slide → run a small file → see the same idea in Python-Set2.",
    ),
    4: rich_map(
        "Build map — PEP standards",
        [
            {
                "kind": "chips",
                "label": "1. What is a PEP?",
                "items": ["Proposal", "community standard", "best practice"],
                "caption": "Python Enhancement Proposal = documented rules teams follow",
            },
            {
                "kind": "grid",
                "label": "2. Key PEPs you will use",
                "cells": [
                    ("PEP 8", "style · snake_case · 4 spaces"),
                    ("PEP 257", "docstrings"),
                    ("PEP 20", "Zen · import this"),
                    ("PEP 621", "pyproject.toml"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Enforce it",
                "question": "Humans vs tools?",
                "left": {
                    "badge": "Style",
                    "ok": True,
                    "title": "Readable code",
                    "detail": "naming · indent · imports",
                    "code": "snake_case",
                    "em": "for people",
                },
                "right": {
                    "badge": "CI tools",
                    "ok": True,
                    "title": "Auto-check",
                    "detail": "ruff / Black in pipeline",
                    "code": "pyproject.toml",
                    "em": "for machines",
                },
            },
        ],
        footer="<b>Interview line:</b> PEP 8 + ruff/Black in CI; packaging metadata lives in pyproject.toml.",
    ),
    5: rich_map(
        "Build map — pick a datatype",
        [
            {
                "kind": "chips",
                "label": "1. Two big groups",
                "items": ["Primitives", "Collections"],
                "caption": "One value vs many values",
            },
            {
                "kind": "box",
                "label": "2. The toolbox",
                "title": "What should this variable hold?",
                "items": ["int", "str", "list", "tuple", "dict", "set"],
            },
            {
                "kind": "fork",
                "label": "3. Common choice",
                "question": "Fixed shape or growing list?",
                "left": {
                    "badge": "list",
                    "ok": True,
                    "title": "Growing / editable",
                    "detail": "cart · logs · query rows",
                    "code": "append / sort",
                    "em": "mutable sequence",
                },
                "right": {
                    "badge": "tuple",
                    "ok": True,
                    "title": "Fixed record",
                    "detail": "GPS · (ok, data) return",
                    "code": "hashable key",
                    "em": "protects shared data",
                },
            },
        ],
        footer="<b>Also:</b> dict = lookup by key · set = unique items only.",
    ),
    6: rich_map(
        "Build map — typing layers",
        [
            {
                "kind": "chips",
                "label": "1. Write hints",
                "items": ["param: int", "-> str", "list[str]", "X | None"],
                "caption": "Hints document intent — Python does not enforce them at runtime",
            },
            {
                "kind": "box",
                "label": "2. Who checks?",
                "title": "Static tools before you run",
                "steps": [
                    ("mypy / pyright", "catch type mistakes early"),
                    ("IDE autocomplete", "safer refactors"),
                    ("Pydantic / FastAPI", "optional runtime enforce"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Modern vs old style",
                "question": "Python 3.10+ syntax?",
                "left": {
                    "badge": "Prefer",
                    "ok": True,
                    "title": "Built-ins + |",
                    "detail": "list[str] · dict[str, int]",
                    "code": "str | None",
                    "em": "no typing.List needed",
                },
                "right": {
                    "badge": "Legacy",
                    "ok": False,
                    "title": "typing module",
                    "detail": "List[str] · Optional[str]",
                    "code": "from typing import …",
                    "em": "still valid, more verbose",
                },
            },
        ],
        footer="<b>Trap:</b> wrong types at runtime do not crash — only tools/frameworks catch them.",
    ),
    7: rich_map(
        "Build map — operator families",
        [
            {
                "kind": "chips",
                "label": "1. Math &amp; assign",
                "items": ["+ − * /", "// % **", "= +=", ":="],
                "caption": "<code>/</code> always float in Py3 · <code>//</code> floor · walrus <code>:=</code> assigns in an expression",
            },
            {
                "kind": "grid",
                "label": "2. Compare · logic · membership",
                "cells": [
                    ("Compare", "== != &lt; &gt;"),
                    ("Logic", "and or not"),
                    ("Membership", "in · not in"),
                    ("Identity", "is · is not"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Easy traps",
                "question": "Value or identity?",
                "left": {
                    "badge": "==",
                    "ok": True,
                    "title": "Same value?",
                    "detail": "almost always what you want",
                    "code": "x == 1000",
                    "em": "equality",
                },
                "right": {
                    "badge": "is",
                    "ok": False,
                    "title": "Same object?",
                    "detail": "identity / None checks",
                    "code": "x is None",
                    "em": "not for numbers/strings",
                },
            },
        ],
        footer="<b>Also:</b> <code>-2 ** 2</code> is <code>-(2**2)</code> → −4 · <code>and</code>/<code>or</code> return operands.",
    ),
    8: rich_map(
        "Build map — flow control",
        [
            {
                "kind": "chips",
                "label": "1. Decide or repeat?",
                "items": ["if / elif / else", "for", "while"],
            },
            {
                "kind": "box",
                "label": "2. Loop helpers",
                "title": "Inside a loop",
                "items": ["continue", "break", "pass", "else"],
                "caption": "<code>continue</code>=skip · <code>break</code>=stop · <code>pass</code>=empty stub · <code>for/else</code>=no break",
            },
            {
                "kind": "fork",
                "label": "3. Style choice",
                "question": "Deep nesting or guards?",
                "left": {
                    "badge": "Prefer",
                    "ok": True,
                    "title": "Guard clauses",
                    "detail": "return early on bad input",
                    "code": "if not user: return",
                    "em": "flat happy path",
                },
                "right": {
                    "badge": "Avoid",
                    "ok": False,
                    "title": "Pyramid if/else",
                    "detail": "hard to read &amp; test",
                    "code": "if: if: if:",
                    "em": "nesting tax",
                },
            },
        ],
        footer="<b>Iterate items:</b> <code>for x in items:</code> — not <code>range(len(...))</code> unless you need the index.",
    ),
    9: rich_map(
        "Build map — comprehensions",
        [
            {
                "kind": "chips",
                "label": "1. Same idea, different brackets",
                "items": ["[list]", "{set}", "{k: v}", "(gen)"],
                "caption": "source → expression → optional filter",
            },
            {
                "kind": "pipeline",
                "label": "2. Mental model",
                "steps": [
                    ("for x in …", "source"),
                    ("if …", "optional filter"),
                    ("expr", "build each item"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. When to use",
                "question": "Build a value or do side effects?",
                "left": {
                    "badge": "Yes",
                    "ok": True,
                    "title": "Produce a collection",
                    "detail": "transform / filter into a result",
                    "code": "[x*2 for x in nums]",
                    "em": "or (x for x in …) if lazy",
                },
                "right": {
                    "badge": "No",
                    "ok": False,
                    "title": "Side effects",
                    "detail": "print / log / write file",
                    "code": "for x in nums: …",
                    "em": "use a normal for loop",
                },
            },
        ],
        footer="<b>Readability:</b> one nesting level is fine — deeper → named helper or loop.",
    ),
    10: rich_map(
        "Build map — functions",
        [
            {
                "kind": "chips",
                "label": "1. Anatomy",
                "items": ["def name", "params", "body", "return"],
                "caption": "A callable unit you can pass, store, and reuse",
            },
            {
                "kind": "box",
                "label": "2. Arguments &amp; scope",
                "title": "How values get in / out",
                "steps": [
                    ("pos / kw", "order or name=value"),
                    ("*args **kwargs", "extra packs"),
                    ("LEGB", "Local → Enclosing → Global → Built-in"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Special forms",
                "question": "Named function or tiny expression?",
                "left": {
                    "badge": "def",
                    "ok": True,
                    "title": "Normal function",
                    "detail": "multi-line · docstring · reuse",
                    "code": "def charge(amount):",
                    "em": "default choice",
                },
                "right": {
                    "badge": "lambda",
                    "ok": True,
                    "title": "One-line anonymous",
                    "detail": "key= · map/filter glue",
                    "code": "lambda x: x[1]",
                    "em": "keep it tiny",
                },
            },
        ],
        footer="<b>Also:</b> recursion = function calls itself · higher-order = pass/return functions.",
    ),
    11: rich_map(
        "Build map — built-in toolbox",
        [
            {
                "kind": "chips",
                "label": "1. Transform &amp; filter",
                "items": ["map", "filter", "reduce", "zip"],
            },
            {
                "kind": "grid",
                "label": "2. Everyday helpers",
                "cells": [
                    ("enumerate", "index + value"),
                    ("sorted", "new ordered list"),
                    ("max / min", "extremes"),
                    ("type / id", "inspect object"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Style preference",
                "question": "map/filter or comprehension?",
                "left": {
                    "badge": "Often",
                    "ok": True,
                    "title": "Comprehension",
                    "detail": "clearer to most Python teams",
                    "code": "[f(x) for x in xs]",
                    "em": "readable default",
                },
                "right": {
                    "badge": "Also fine",
                    "ok": True,
                    "title": "map / filter",
                    "detail": "functional style / lazy map",
                    "code": "map(f, xs)",
                    "em": "know both for interviews",
                },
            },
        ],
        footer="<b>zip</b> pairs iterables · <b>enumerate</b> when you need the index.",
    ),
    12: rich_map(
        "Build map — collections module",
        [
            {
                "kind": "chips",
                "label": "1. Beyond list/dict",
                "items": ["Counter", "defaultdict", "deque", "namedtuple"],
            },
            {
                "kind": "grid",
                "label": "2. What each solves",
                "cells": [
                    ("Counter", "tallies / most_common"),
                    ("defaultdict", "auto-create missing keys"),
                    ("deque", "fast left &amp; right ends"),
                    ("namedtuple", "light immutable records"),
                    ("OrderedDict", "remember insert order"),
                    ("ChainMap", "stack of dicts"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Pick quickly",
                "question": "Counting or auto-keys?",
                "left": {
                    "badge": "Counter",
                    "ok": True,
                    "title": "Frequencies",
                    "detail": "words · votes · pie charts",
                    "code": "Counter(words)",
                    "em": ".most_common(n)",
                },
                "right": {
                    "badge": "defaultdict",
                    "ok": True,
                    "title": "Group without KeyError",
                    "detail": "lists/sets per key",
                    "code": "defaultdict(list)",
                    "em": "auto empty container",
                },
            },
        ],
        footer="<b>deque</b> for queues · <b>namedtuple</b> when you want fields without a full class.",
    ),
    13: rich_map(
        "Build map — memory &amp; GC",
        [
            {
                "kind": "chips",
                "label": "1. Names → objects",
                "items": ["name", "reference", "object", "refcount"],
                "caption": "Variables hold references — objects live on the heap",
            },
            {
                "kind": "cycle",
                "label": "2. Lifecycle",
                "steps": [
                    ("Create", "refcount = 1"),
                    ("Share", "refcount ↑"),
                    ("del / rebind", "refcount ↓"),
                    ("Zero", "free soon"),
                ],
                "caption": "CPython frees when refcount hits 0",
            },
            {
                "kind": "fork",
                "label": "3. Hard cases",
                "question": "Simple refs or a cycle?",
                "left": {
                    "badge": "Normal",
                    "ok": True,
                    "title": "Refcount enough",
                    "detail": "A → B, no loop back",
                    "code": "del a",
                    "em": "memory freed",
                },
                "right": {
                    "badge": "Cycle",
                    "ok": False,
                    "title": "Needs gc",
                    "detail": "A ↔ B circular refs",
                    "code": "gc module",
                    "em": "generational collector",
                },
            },
        ],
        footer="<b>Alias trap:</b> <code>b = a</code> for a list shares the object — mutate one, both change.",
    ),
    14: rich_map(
        "Build map — Pydantic validation",
        [
            {
                "kind": "chips",
                "label": "1. Raw input",
                "items": ["JSON", "dict", "form", "query"],
                "caption": "Untrusted data from clients / files",
            },
            {
                "kind": "box",
                "label": "2. Schema stack",
                "title": "BaseModel turns chaos into typed data",
                "steps": [
                    ("BaseModel", "typed fields"),
                    ("Field + validators", "rules &amp; coerce"),
                    ("model_dump()", "clean dict out"),
                ],
                "gate": ("Invalid?", "ValidationError → FastAPI HTTP 422"),
            },
            {
                "kind": "fork",
                "label": "3. Why not plain dict?",
                "question": "Trust the payload?",
                "left": {
                    "badge": "Pydantic",
                    "ok": True,
                    "title": "Validate once",
                    "detail": "types · defaults · errors",
                    "code": "class Order(BaseModel)",
                    "em": "safe for APIs",
                },
                "right": {
                    "badge": "Bare dict",
                    "ok": False,
                    "title": "Hope keys exist",
                    "detail": "KeyError / wrong types later",
                    "code": "data['amount']",
                    "em": "bugs in production",
                },
            },
        ],
        footer="<b>FastAPI:</b> request body → Pydantic model automatically.",
    ),
    15: rich_map(
        "Build map — OOP blocks",
        [
            {
                "kind": "chips",
                "label": "1. Blueprint",
                "items": ["class", "__init__", "self", "methods"],
                "caption": "Class = blueprint · instance = one object in memory",
            },
            {
                "kind": "box",
                "label": "2. Reuse &amp; specialize",
                "title": "Inheritance tree",
                "steps": [
                    ("Account", "deposit / withdraw"),
                    ("SavingsAccount", "inherit + extra rules"),
                    ("override", "same call, different behavior"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Design tools",
                "question": "Force a contract?",
                "left": {
                    "badge": "ABC",
                    "ok": True,
                    "title": "Abstract base",
                    "detail": "subclasses must implement",
                    "code": "@abstractmethod",
                    "em": "polymorphism safety",
                },
                "right": {
                    "badge": "duck typing",
                    "ok": True,
                    "title": "If it quacks…",
                    "detail": "any object with the method works",
                    "code": "obj.pay()",
                    "em": "Pythonic flexibility",
                },
            },
        ],
        footer="<b>Interview:</b> inheritance = reuse · polymorphism = one interface, many behaviors.",
    ),
    16: rich_map(
        "Build map — descriptors",
        [
            {
                "kind": "chips",
                "label": "1. Attribute access",
                "items": ["obj.x", "read", "write", "delete"],
                "caption": "Descriptors intercept how attributes work",
            },
            {
                "kind": "box",
                "label": "2. Protocol",
                "title": "Special methods on a descriptor class",
                "steps": [
                    ("__get__", "read value"),
                    ("__set__", "write / validate"),
                    ("__delete__", "remove"),
                ],
                "gate": ("@property", "built-in descriptor shortcut"),
            },
            {
                "kind": "fork",
                "label": "3. When to use",
                "question": "Simple field or managed attribute?",
                "left": {
                    "badge": "@property",
                    "ok": True,
                    "title": "Most common",
                    "detail": "computed / validated field",
                    "code": "@price.setter",
                    "em": "enough for many cases",
                },
                "right": {
                    "badge": "Descriptor",
                    "ok": True,
                    "title": "Reusable rule",
                    "detail": "same validation on many fields",
                    "code": "class Positive:",
                    "em": "advanced / libraries",
                },
            },
        ],
        footer="<b>Mental model:</b> <code>obj.x</code> may call code — not always a plain dict lookup.",
    ),
    17: rich_map(
        "Build map — generators &amp; iterators",
        [
            {
                "kind": "chips",
                "label": "1. Lazy values",
                "items": ["yield", "pause", "resume", "StopIteration"],
                "caption": "Produce one item at a time — great for huge files",
            },
            {
                "kind": "cycle",
                "label": "2. Pause / resume",
                "steps": [
                    ("yield", "pause + value"),
                    ("next()", "resume"),
                    ("locals live", "state kept"),
                    ("done", "StopIteration"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. List vs generator",
                "question": "Need all items in memory?",
                "left": {
                    "badge": "list",
                    "ok": True,
                    "title": "Eager",
                    "detail": "build everything now",
                    "code": "[line for line in f]",
                    "em": "OK for small data",
                },
                "right": {
                    "badge": "generator",
                    "ok": True,
                    "title": "Lazy",
                    "detail": "one item when asked",
                    "code": "(line for line in f)",
                    "em": "streams / big files",
                },
            },
        ],
        footer="<b>Iterator protocol:</b> <code>__iter__</code> + <code>__next__</code> · <code>for</code> uses it automatically.",
    ),
    18: rich_map(
        "Build map — decorators",
        [
            {
                "kind": "chips",
                "label": "1. Syntax sugar",
                "items": ["@decorator", "wrap", "call", "return"],
                "caption": "<code>@dec</code> means <code>f = dec(f)</code>",
            },
            {
                "kind": "box",
                "label": "2. Wrap timeline",
                "title": "What the wrapper does",
                "steps": [
                    ("before", "log / auth / timer start"),
                    ("call f", "original body"),
                    ("after", "cleanup / log end"),
                ],
                "gate": ("@wraps(f)", "keep name &amp; docstring"),
            },
            {
                "kind": "fork",
                "label": "3. Common uses",
                "question": "Cross-cutting concern?",
                "left": {
                    "badge": "Yes",
                    "ok": True,
                    "title": "Timer / log / retry",
                    "detail": "same wrapper on many functions",
                    "code": "@timer",
                    "em": "DRY behavior",
                },
                "right": {
                    "badge": "Careful",
                    "ok": False,
                    "title": "Hide real logic",
                    "detail": "too much magic in wrappers",
                    "code": "nested @a @b @c",
                    "em": "hard to debug",
                },
            },
        ],
        footer="<b>Factory:</b> <code>@repeat(3)</code> — outer function returns the real decorator.",
    ),
    19: rich_map(
        "Build map — exception path",
        [
            {
                "kind": "chips",
                "label": "1. Something went wrong",
                "items": ["raise", "Exception", "traceback"],
                "caption": "Signal an error instead of returning a magic code",
            },
            {
                "kind": "cycle",
                "label": "2. try ladder",
                "steps": [
                    ("try", "risky code"),
                    ("except", "handle specific"),
                    ("else", "no error"),
                    ("finally", "always"),
                ],
                "caption": "<code>finally</code> runs even on return / re-raise",
            },
            {
                "kind": "fork",
                "label": "3. Catch style",
                "question": "How wide is the net?",
                "left": {
                    "badge": "Prefer",
                    "ok": True,
                    "title": "Specific types",
                    "detail": "ValueError · KeyError · OSError",
                    "code": "except ValueError:",
                    "em": "you know what failed",
                },
                "right": {
                    "badge": "Avoid",
                    "ok": False,
                    "title": "Bare except",
                    "detail": "hides bugs &amp; KeyboardInterrupt",
                    "code": "except:",
                    "em": "too wide",
                },
            },
        ],
        footer="<b>Custom:</b> <code>class ValidationError(Exception)</code> · <code>raise from</code> keeps context.",
    ),
    20: gil_build_diagram(),
    21: rich_map(
        "Build map — async / await",
        [
            {
                "kind": "chips",
                "label": "1. One thread, many waits",
                "items": ["async def", "await", "event loop", "Task"],
                "caption": "Concurrency for I/O — not CPU parallelism",
            },
            {
                "kind": "cycle",
                "label": "2. Event loop",
                "steps": [
                    ("async def", "coroutine"),
                    ("await", "yield control"),
                    ("loop", "run others"),
                    ("gather", "many at once"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. vs threading",
                "question": "Many sockets or shared OS threads?",
                "left": {
                    "badge": "async",
                    "ok": True,
                    "title": "Lots of I/O waits",
                    "detail": "one thread takes turns",
                    "code": "asyncio.gather",
                    "em": "no thread-per-connection",
                },
                "right": {
                    "badge": "threads",
                    "ok": True,
                    "title": "Blocking libs",
                    "detail": "or simple I/O pools",
                    "code": "ThreadPoolExecutor",
                    "em": "or asyncio.to_thread",
                },
            },
        ],
        footer="<b>Trap:</b> blocking CPU / sync I/O inside async freezes the whole loop.",
    ),
    22: rich_map(
        "Build map — logging pipeline",
        [
            {
                "kind": "chips",
                "label": "1. Levels",
                "items": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                "caption": "Filter noise in production — keep DEBUG for local",
            },
            {
                "kind": "box",
                "label": "2. Pipeline",
                "title": "Logger → Handler → Formatter",
                "steps": [
                    ("Logger", "getLogger(__name__)"),
                    ("Handler", "console / RotatingFileHandler"),
                    ("Formatter", "time + level + message"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. print vs logging",
                "question": "Dev toy or production?",
                "left": {
                    "badge": "logging",
                    "ok": True,
                    "title": "Production",
                    "detail": "levels · files · turn off",
                    "code": 'logger.info("x=%s", x)',
                    "em": "prefer %s lazy formatting",
                },
                "right": {
                    "badge": "print",
                    "ok": False,
                    "title": "Quick local only",
                    "detail": "no levels · hard to filter",
                    "code": "print(x)",
                    "em": "not for servers",
                },
            },
        ],
        footer="<b>Exceptions:</b> <code>logger.exception(...)</code> inside except — includes traceback.",
    ),
    23: rich_map(
        "Build map — unit testing",
        [
            {
                "kind": "chips",
                "label": "1. AAA pattern",
                "items": ["Arrange", "Act", "Assert"],
                "caption": "Set up → call code → check result",
            },
            {
                "kind": "cycle",
                "label": "2. Per test lifecycle",
                "steps": [
                    ("setUp", "fixtures"),
                    ("test_…", "act + assert"),
                    ("tearDown", "cleanup"),
                    ("repeat", "next test"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Frameworks",
                "question": "stdlib or pytest?",
                "left": {
                    "badge": "unittest",
                    "ok": True,
                    "title": "Built-in",
                    "detail": "TestCase · assertEqual",
                    "code": "python -m unittest",
                    "em": "familiar to JUnit folks",
                },
                "right": {
                    "badge": "pytest",
                    "ok": True,
                    "title": "Less boilerplate",
                    "detail": "plain assert · fixtures",
                    "code": "pytest -v",
                    "em": "common for new projects",
                },
            },
        ],
        footer="<b>Mock:</b> <code>@patch</code> fakes network/DB so CI stays offline and fast.",
    ),
    24: rich_map(
        "Build map — regular expressions",
        [
            {
                "kind": "chips",
                "label": "1. Pattern engine",
                "items": ["re module", "r'…'", "pattern", "match object"],
                "caption": "Raw strings <code>r'…'</code> = fewer backslash headaches",
            },
            {
                "kind": "grid",
                "label": "2. Toolkit",
                "cells": [
                    ("search", "find anywhere"),
                    ("match", "only at start"),
                    ("findall", "all hits"),
                    ("groups", "(…) capture"),
                    ("sub", "replace"),
                    ("compile", "reuse pattern"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. search vs match",
                "question": "Where can the pattern sit?",
                "left": {
                    "badge": "search",
                    "ok": True,
                    "title": "Anywhere",
                    "detail": "most common choice",
                    "code": "re.search(pat, text)",
                    "em": "first hit",
                },
                "right": {
                    "badge": "match",
                    "ok": False,
                    "title": "Only at start",
                    "detail": "like ^pattern",
                    "code": "re.match(pat, text)",
                    "em": "easy to misuse",
                },
            },
        ],
        footer="<b>Groups:</b> <code>m.group(1)</code> after a successful search/match.",
    ),
    25: rich_map(
        "Build map — file I/O",
        [
            {
                "kind": "chips",
                "label": "1. Locate the file",
                "items": ["pathlib.Path", "open(path)", "text / bytes"],
            },
            {
                "kind": "box",
                "label": "2. Safe open",
                "title": "<code>with</code> auto-closes — even on error",
                "steps": [
                    ("with open(...) as f", "acquire handle"),
                    ("read / write", "use the file"),
                    ("exit with", "close guaranteed"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Tools",
                "question": "Plain text or structured?",
                "left": {
                    "badge": "open / Path",
                    "ok": True,
                    "title": "Lines &amp; bytes",
                    "detail": "logs · configs · binaries",
                    "code": "Path('a') / 'b.txt'",
                    "em": "clean joins",
                },
                "right": {
                    "badge": "csv / json",
                    "ok": True,
                    "title": "Structured data",
                    "detail": "tables · API payloads",
                    "code": "json.load(f)",
                    "em": "stdlib modules",
                },
            },
        ],
        footer="<b>Always</b> prefer <code>with open</code> — never rely on forgetting <code>f.close()</code>.",
    ),
    26: rich_map(
        "Build map — context managers",
        [
            {
                "kind": "chips",
                "label": "1. Acquire → use → release",
                "items": ["with", "__enter__", "body", "__exit__"],
                "caption": "Same idea as C# <code>using</code> — cleanup is guaranteed",
            },
            {
                "kind": "cycle",
                "label": "2. Protocol",
                "steps": [
                    ("with", "start"),
                    ("__enter__", "acquire"),
                    ("body", "use resource"),
                    ("__exit__", "release"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Write your own?",
                "question": "Class or generator helper?",
                "left": {
                    "badge": "class",
                    "ok": True,
                    "title": "__enter__ / __exit__",
                    "detail": "full control",
                    "code": "class DbSession:",
                    "em": "explicit protocol",
                },
                "right": {
                    "badge": "@contextmanager",
                    "ok": True,
                    "title": "Generator style",
                    "detail": "yield the resource",
                    "code": "@contextmanager",
                    "em": "less boilerplate",
                },
            },
        ],
        footer="<b>vs try/finally:</b> <code>with</code> is shorter and harder to forget cleanup.",
    ),
    27: rich_map(
        "Build map — virtual environments",
        [
            {
                "kind": "chips",
                "label": "1. Why isolate?",
                "items": ["per project", "no clashes", "reproducible"],
                "caption": "Never install client libs into the global Python",
            },
            {
                "kind": "box",
                "label": "2. Lifecycle",
                "title": "Create → activate → install → freeze",
                "steps": [
                    ("python -m venv .venv", "create"),
                    ("Activate", "shell uses this Python"),
                    ("pip install …", "project packages only"),
                    ("pip freeze", "requirements.txt"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Global vs .venv",
                "question": "Where do packages go?",
                "left": {
                    "badge": ".venv",
                    "ok": True,
                    "title": "Per project",
                    "detail": "safe · portable recipe",
                    "code": "requirements.txt",
                    "em": "commit the freeze, not .venv/",
                },
                "right": {
                    "badge": "Global",
                    "ok": False,
                    "title": "Shared by all apps",
                    "detail": "version hell",
                    "code": "pip install (system)",
                    "em": "avoid for project work",
                },
            },
        ],
        footer="<b>Git:</b> ignore <code>.venv/</code> — regenerate with <code>pip install -r requirements.txt</code>.",
    ),
    28: rich_map(
        "Build map — FastAPI + SQLAlchemy",
        [
            {
                "kind": "chips",
                "label": "1. One HTTP request",
                "items": ["Route", "Schema", "Service", "ORM", "DB"],
            },
            {
                "kind": "box",
                "label": "2. Layer cake",
                "title": "Keep each layer thin",
                "steps": [
                    ("FastAPI route", "HTTP in/out only"),
                    ("Pydantic schema", "validate request/response"),
                    ("Service", "business rules + transaction"),
                    ("SQLAlchemy", "Session / tables"),
                ],
                "gate": ("Depends(get_db)", "≈ scoped DbContext per request"),
            },
            {
                "kind": "fork",
                "label": "3. Return shape",
                "question": "What leaves the API?",
                "left": {
                    "badge": "Do",
                    "ok": True,
                    "title": "Response model",
                    "detail": "Pydantic / schema out",
                    "code": "response_model=…",
                    "em": "stable JSON contract",
                },
                "right": {
                    "badge": "Avoid",
                    "ok": False,
                    "title": "Raw ORM object",
                    "detail": "leaks DB shape · lazy bugs",
                    "code": "return db_row",
                    "em": "never for public API",
                },
            },
        ],
        footer="<b>C# map:</b> Controller → DTO → Service → DbContext.",
    ),
    29: rich_map(
        "Build map — Python-Set2 portfolio",
        [
            {
                "kind": "chips",
                "label": "1. Why this folder?",
                "items": ["interview demos", "runnable", "topic-sized"],
            },
            {
                "kind": "grid",
                "label": "2. Map of areas",
                "cells": [
                    ("pythonBasics", "core language"),
                    ("google + pandas", "files · regex · data"),
                    ("Django / DRF", "web + REST"),
                    ("Pipecat", "voice AI"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. How to use it",
                "question": "Study path?",
                "left": {
                    "badge": "First",
                    "ok": True,
                    "title": "Match the slide",
                    "detail": "open related module",
                    "code": "MyClass / MyLoops",
                    "em": "theory → code",
                },
                "right": {
                    "badge": "Then",
                    "ok": True,
                    "title": "Change one line",
                    "detail": "prove you understand",
                    "code": "run · tweak · rerun",
                    "em": "interview ready",
                },
            },
        ],
        footer="<b>Goal:</b> every major slide topic has something you can demo live.",
    ),
    30: rich_map(
        "Build map — pythonBasics modules",
        [
            {
                "kind": "chips",
                "label": "1. Topic folders",
                "items": ["MyClass", "MyCollections", "MyLoops", "MyModules"],
            },
            {
                "kind": "grid",
                "label": "2. More modules",
                "cells": [
                    ("MyException", "try / except"),
                    ("MyDebug", "pdb"),
                    ("MyUnitTesting", "unittest / mock"),
                    ("main.py", "entry experiments"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Study loop",
                "question": "How to learn one module?",
                "left": {
                    "badge": "Read",
                    "ok": True,
                    "title": "Matching slide first",
                    "detail": "definition + diagram",
                    "code": "PythonTraining.html",
                    "em": "know the words",
                },
                "right": {
                    "badge": "Run",
                    "ok": True,
                    "title": "Execute the .py",
                    "detail": "then change one line",
                    "code": "python …/car.py",
                    "em": "make it yours",
                },
            },
        ],
        footer="<b>Tip:</b> treat each folder as a mini chapter — don’t skip running the files.",
    ),
    31: rich_map(
        "Build map — Google exercises &amp; Pandas",
        [
            {
                "kind": "chips",
                "label": "1. Two practice tracks",
                "items": ["Google exercises", "Pandas notebook"],
            },
            {
                "kind": "box",
                "label": "2. Skills you practice",
                "title": "Files · regex · tables",
                "steps": [
                    ("babynames", "regex on HTML"),
                    ("copyspecial", "os / shutil"),
                    ("pandas", "read_csv · groupby · charts"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Homework pattern",
                "question": "What is the repeatable flow?",
                "left": {
                    "badge": "Load → Clean",
                    "ok": True,
                    "title": "Get trustworthy data",
                    "detail": "open / read_csv · fix nulls",
                    "code": "dropna / astype",
                    "em": "before analysis",
                },
                "right": {
                    "badge": "Analyze → Explain",
                    "ok": True,
                    "title": "Answer + show",
                    "detail": "groupby · regex extract · chart",
                    "code": "notebook / plot",
                    "em": "stakeholder ready",
                },
            },
        ],
        footer="<b>Interview story:</b> “I cleaned messy files with regex/pandas and explained the chart.”",
    ),
    32: rich_map(
        "Build map — Django &amp; DRF",
        [
            {
                "kind": "chips",
                "label": "1. Web choices",
                "items": ["Django MVT", "DRF API", "FastAPI async"],
            },
            {
                "kind": "box",
                "label": "2. Typical request",
                "title": "URL → view → model → response",
                "steps": [
                    ("URL / router", "find the view"),
                    ("View / ViewSet", "controller logic"),
                    ("Model / ORM", "database"),
                    ("Template or Serializer", "HTML / JSON out"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Django+DRF vs FastAPI",
                "question": "Batteries or async-first?",
                "left": {
                    "badge": "Django + DRF",
                    "ok": True,
                    "title": "Full web stack",
                    "detail": "admin · auth · serializers",
                    "code": "ViewSets",
                    "em": "batteries included",
                },
                "right": {
                    "badge": "FastAPI",
                    "ok": True,
                    "title": "API-first async",
                    "detail": "Pydantic · OpenAPI free",
                    "code": "@app.get",
                    "em": "great for microservices",
                },
            },
        ],
        footer="<b>DRF:</b> Serializers validate like Pydantic; ViewSets cut CRUD boilerplate.",
    ),
    33: rich_map(
        "Build map — Pipecat voice AI",
        [
            {
                "kind": "chips",
                "label": "1. Audio in",
                "items": ["mic", "WebRTC", "frames"],
            },
            {
                "kind": "pipeline",
                "label": "2. Pipeline (order matters)",
                "steps": [
                    ("STT", "speech → text"),
                    ("LLM", "decide reply"),
                    ("TTS", "text → speech"),
                ],
                "caption": "Genuine left→right pipeline — each stage feeds the next",
            },
            {
                "kind": "fork",
                "label": "3. What you demo",
                "question": "POC focus?",
                "left": {
                    "badge": "Pipeline",
                    "ok": True,
                    "title": "End-to-end voice",
                    "detail": "hear → think → speak",
                    "code": "Pipecat frames",
                    "em": "show the loop",
                },
                "right": {
                    "badge": "Swap parts",
                    "ok": True,
                    "title": "Providers",
                    "detail": "change STT/LLM/TTS vendors",
                    "code": "config / adapters",
                    "em": "flexible architecture",
                },
            },
        ],
        footer="<b>Interview:</b> explain STT → LLM → TTS and where latency hides.",
    ),
    34: rich_map(
        "Build map — real project structure",
        [
            {
                "kind": "chips",
                "label": "1. Entry",
                "items": ["main.py", "app factory", "config"],
            },
            {
                "kind": "box",
                "label": "2. Folders that scale",
                "title": "Thin edges · fat services",
                "steps": [
                    ("routes/", "HTTP only"),
                    ("services/", "business logic"),
                    ("schemas / models", "DTOs + ORM"),
                    ("tests/", "pytest at repo root"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Learning path",
                "question": "What next after slides?",
                "left": {
                    "badge": "Build",
                    "ok": True,
                    "title": "One small feature",
                    "detail": "route + service + test",
                    "code": "PR-sized change",
                    "em": "proves the layout",
                },
                "right": {
                    "badge": "Avoid",
                    "ok": False,
                    "title": "God main.py",
                    "detail": "everything in one file",
                    "code": "2000-line script",
                    "em": "hard to test/hire",
                },
            },
        ],
        footer="<b>Rule:</b> routes stay thin — business rules live in services/.",
    ),
    35: rich_map(
        "Build map — C# ↔ Python quick map",
        [
            {
                "kind": "chips",
                "label": "1. Surface syntax",
                "items": ["{ } → indent", "null → None", "this → self"],
            },
            {
                "kind": "grid",
                "label": "2. Everyday equivalents",
                "cells": [
                    ("using (…)", "with …"),
                    ("NuGet", "pip + venv"),
                    ("{ } empty", "pass"),
                    ("NotImplementedException", "NotImplementedError"),
                ],
            },
            {
                "kind": "fork",
                "label": "3. Runtime mindset",
                "question": "Compile first or run source?",
                "left": {
                    "badge": "C#",
                    "ok": True,
                    "title": "Build then run",
                    "detail": "assembly + CLR/JIT",
                    "code": "dotnet build",
                    "em": "no GIL · Parallel OK",
                },
                "right": {
                    "badge": "Python",
                    "ok": True,
                    "title": "Interpreter runs .py",
                    "detail": "bytecode inside CPython",
                    "code": "python app.py",
                    "em": "GIL → threads I/O / processes CPU",
                },
            },
        ],
        footer="<b>Carry-over:</b> your OO + async instincts transfer — syntax and packaging differ.",
    ),
}
