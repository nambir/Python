"""Notes section slides — Mindmap / flowcharts for training topics."""

from __future__ import annotations

# Notes slide numbers start here (separate from curriculum 1–35)
NOTES_START = 100

NOTES_CSS = """
.nav-hero {
  display: flex; align-items: flex-start; justify-content: space-between; gap: 24px;
  width: min(1400px, calc(100vw - 48px)); margin: 0 auto 8px; flex-wrap: wrap;
}
.nav-hero-main { flex: 1; min-width: 240px; text-align: center; }
.nav-hero-main h1 { font-size: 34px; margin-bottom: 4px; }
.nav-hero-main .sub { font-size: 16px; color: #0066cc; }
.nav-hero-main .org { font-size: 13px; color: #666; margin: 6px 0 0; }
.notes-panel {
  width: min(320px, 100%); flex-shrink: 0; text-align: left;
  background: linear-gradient(180deg, #f8fafc 0%, #eff6ff 100%);
  border: 1px solid #bfdbfe; border-radius: 10px; padding: 12px 14px;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
}
.notes-panel h2 {
  font-size: 14px; color: #1e40af; margin: 0 0 6px; letter-spacing: .4px;
  text-transform: uppercase;
}
.notes-panel p { font-size: 12px; color: #475569; margin: 0 0 10px; line-height: 1.4; }
.notes-panel a.notes-link {
  display: block; padding: 8px 10px; margin: 0 0 6px;
  background: #fff; border: 1px solid #93c5fd; border-radius: 6px;
  color: #0066cc; font-size: 13px; font-weight: 600; text-decoration: none;
}
.notes-panel a.notes-link:hover { background: #dbeafe; }
.notes-panel a.notes-link span { display: block; font-size: 11px; font-weight: 400; color: #64748b; margin-top: 2px; }
.notes-badge {
  display: inline-block; font-size: 10px; font-weight: 700; color: #fff;
  background: #2563eb; border-radius: 999px; padding: 2px 8px; margin-right: 6px;
}

.notes-slide .slide-title { border-bottom-color: #7c3aed; }
.notes-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px;
}
@media (max-width: 900px) {
  .nav-hero { justify-content: center; }
  .nav-hero-main { text-align: center; width: 100%; }
  .notes-panel { width: 100%; max-width: 420px; margin: 0 auto; }
  .notes-grid { grid-template-columns: 1fr; }
}

.mm-card {
  border: 1px solid #e2e8f0; border-radius: 10px; padding: 12px 14px; background: #fff;
}
.mm-card h3 { margin-top: 0; color: #5b21b6; }
.mm-center {
  text-align: center; margin: 8px auto 12px; max-width: 220px;
  background: #ede9fe; border: 2px solid #7c3aed; border-radius: 12px;
  padding: 10px 12px; font-weight: 700; color: #4c1d95; font-size: 13px;
}
.mm-branches {
  display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
}
.mm-branch {
  border-radius: 8px; padding: 8px 10px; font-size: 12px; line-height: 1.4;
  border: 1px solid #cbd5e1; background: #f8fafc;
}
.mm-branch b { display: block; color: #0066cc; margin-bottom: 3px; font-size: 12px; }
.mm-branch.dict { border-color: #93c5fd; background: #eff6ff; }
.mm-branch.dd { border-color: #86efac; background: #f0fdf4; }
.mm-branch.key { border-color: #fcd34d; background: #fffbeb; }
.mm-branch.cm { border-color: #c4b5fd; background: #f5f3ff; }

.flow-box {
  display: flex; flex-direction: column; align-items: center; gap: 6px; font-size: 12px;
}
.flow-q {
  background: #fff7ed; border: 2px solid #f97316; border-radius: 8px;
  padding: 10px 14px; text-align: center; font-weight: 600; color: #9a3412;
  max-width: 300px; line-height: 1.35;
  position: relative;
}
.flow-q::before {
  content: "Decision"; display: block; font-size: 10px; font-weight: 700;
  color: #c2410c; text-transform: uppercase; letter-spacing: .4px; margin-bottom: 4px;
}
.flow-arrow { color: #64748b; font-weight: 700; font-size: 14px; }
.flow-row { display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; width: 100%; }
.flow-ans {
  border-radius: 8px; padding: 8px 10px; max-width: 200px; border: 1px solid #cbd5e1;
  background: #f8fafc; text-align: left; line-height: 1.4;
}
.flow-ans b { display: block; margin-bottom: 2px; color: #0066cc; }
.flow-ans.yes { border-color: #86efac; background: #f0fdf4; }
.flow-ans.no { border-color: #fecaca; background: #fef2f2; }
.flow-legend { margin-top: 10px; font-size: 11px; color: #64748b; text-align: center; }

/* Design 3 — 2x2 decision matrix */
.mx-wrap { display: grid; grid-template-columns: 72px 1fr 1fr; grid-template-rows: auto 1fr 1fr; gap: 8px; margin-top: 8px; font-size: 12px; }
.mx-corner { grid-column: 1; grid-row: 1; }
.mx-colhead { text-align: center; font-weight: 700; color: #1e40af; font-size: 11px; padding: 6px; background: #eff6ff; border-radius: 6px; }
.mx-rowhead {
  writing-mode: horizontal-tb; font-weight: 700; color: #166534; font-size: 11px;
  display: flex; align-items: center; justify-content: center; text-align: center;
  background: #f0fdf4; border-radius: 6px; padding: 6px; line-height: 1.25;
}
.mx-cell {
  border-radius: 8px; padding: 10px; border: 1px solid #cbd5e1; background: #f8fafc; line-height: 1.4;
  min-height: 88px;
}
.mx-cell b { display: block; margin-bottom: 4px; font-size: 13px; }
.mx-cell.a { border-color: #86efac; background: #f0fdf4; }
.mx-cell.a b { color: #166534; }
.mx-cell.b { border-color: #c4b5fd; background: #f5f3ff; }
.mx-cell.b b { color: #5b21b6; }
.mx-cell.c { border-color: #93c5fd; background: #eff6ff; }
.mx-cell.c b { color: #1d4ed8; }
.mx-cell.d { border-color: #fcd34d; background: #fffbeb; }
.mx-cell.d b { color: #a16207; }
.mx-axis { font-size: 10px; color: #64748b; text-align: center; margin-top: 8px; }

/* Design 4 — horizontal path / metro */
.path-track {
  display: flex; align-items: stretch; gap: 0; margin-top: 10px; flex-wrap: wrap; justify-content: center;
}
.path-stop {
  flex: 1 1 140px; max-width: 180px; min-width: 130px;
  border-radius: 10px; padding: 10px; border: 2px solid #cbd5e1; background: #fff;
  font-size: 12px; line-height: 1.4; position: relative;
}
.path-stop .num {
  width: 24px; height: 24px; border-radius: 50%; background: #0066cc; color: #fff;
  font-weight: 700; font-size: 12px; display: flex; align-items: center; justify-content: center;
  margin: 0 auto 8px;
}
.path-stop b { display: block; text-align: center; color: #0066cc; margin-bottom: 4px; }
.path-connector {
  display: flex; align-items: center; color: #94a3b8; font-weight: 700; font-size: 18px; padding: 0 2px;
  align-self: center;
}
.path-stop.s1 { border-color: #93c5fd; }
.path-stop.s2 { border-color: #86efac; }
.path-stop.s2 .num { background: #16a34a; }
.path-stop.s3 { border-color: #c4b5fd; }
.path-stop.s3 .num { background: #7c3aed; }
.path-stop.s4 { border-color: #fcd34d; }
.path-stop.s4 .num { background: #ca8a04; }
@media (max-width: 700px) {
  .path-connector { display: none; }
  .mx-wrap { grid-template-columns: 1fr 1fr; }
  .mx-rowhead { writing-mode: horizontal-tb; }
}
"""


def notes_panel_html() -> str:
    """Right-side Notes box on the Navigation home slide."""
    links = []
    for n, title, blurb, _body in NOTES_CONTENT:
        links.append(
            f'<a class="notes-link" href="#{n}" onclick="goSlide({n}); return false;">'
            f'<span class="notes-badge">Notes</span>{title}'
            f"<span>{blurb}</span></a>"
        )
    return (
        '<aside class="notes-panel" aria-label="Notes">'
        "<h2>Notes</h2>"
        "<p>Quick mindmaps &amp; flowcharts for topics we cover — start here.</p>"
        + "".join(links)
        + "</aside>"
    )


def _mindmap_body() -> str:
    return """
<p>Choose between a plain <code>dict</code>, <code>defaultdict</code>, a safe key check,
or <code>ChainMap</code> using the two styles below.</p>

<div class="notes-grid">
  <div class="mm-card">
    <h3>Flowchart — which tool?</h3>
    <p>Answer each question top &rarr; bottom. Stop when you get a tool.</p>
    <div class="flow-box">
      <div class="flow-q">Do you need to<br>group / tally<br>missing keys?</div>
      <div class="flow-arrow">&darr; Yes &nbsp;&nbsp;&nbsp; No &darr;</div>
      <div class="flow-row">
        <div class="flow-ans yes"><b>Yes &rarr; defaultdict</b>
          Factory fills the gap:<br>
          <code>defaultdict(list)</code><br>
          or <code>defaultdict(int)</code>
        </div>
        <div class="flow-ans no"><b>No &rarr; next question</b>
          Keep going &darr;
        </div>
      </div>
      <div class="flow-q">Looking up across<br>several dict layers?</div>
      <div class="flow-arrow">&darr; Yes &nbsp;&nbsp;&nbsp; No &darr;</div>
      <div class="flow-row">
        <div class="flow-ans yes"><b>Yes &rarr; ChainMap</b>
          <code>ChainMap(Dict1, Dict2)</code><br>
          First match wins.
        </div>
        <div class="flow-ans no"><b>No &rarr; plain dict</b>
          Use <code>{}</code> / <code>dict()</code>.
        </div>
      </div>
      <div class="flow-q">Only checking if a<br>key exists?</div>
      <div class="flow-arrow">&darr;</div>
      <div class="flow-row">
        <div class="flow-ans yes"><b>Safe key check</b>
          <code>"k" in d</code><br>
          or <code>d.get("k")</code><br>
          (does <b>not</b> create a key)
        </div>
        <div class="flow-ans no"><b>Trap on defaultdict</b>
          Avoid <code>if myDict["k"]:</code><br>
          — that <b>creates</b> the key.
        </div>
      </div>
    </div>
  </div>

  <div class="mm-card">
    <h3>Path — walk the stops</h3>
    <p>Same decision, left &rarr; right. Exit at the first stop that fits.</p>
    <div class="path-track" style="flex-direction:column;align-items:stretch;gap:10px">
      <div class="path-stop s1" style="max-width:none">
        <div class="num">1</div>
        <b>Grouping / counting in a loop?</b>
        Yes &rarr; stop here: <code>defaultdict(list)</code> or <code>defaultdict(int)</code><br>
        Example: <code>groups[dept].append(name)</code> — no manual <code>if k not in d</code>.<br>
        No &rarr; go to stop 2
      </div>
      <div class="path-connector" style="justify-content:center">&darr;</div>
      <div class="path-stop s2" style="max-width:none">
        <div class="num">2</div>
        <b>Layered config (overrides + defaults)?</b>
        Yes &rarr; stop here: <code>ChainMap(Dict1, Dict2)</code><br>
        Example: user settings first, then <code>app_defaults</code>. First match wins.<br>
        No &rarr; go to stop 3
      </div>
      <div class="path-connector" style="justify-content:center">&darr;</div>
      <div class="path-stop s3" style="max-width:none">
        <div class="num">3</div>
        <b>Only peek — do not create a key?</b>
        Yes &rarr; stop here: <code>"k" in d</code> or <code>d.get("k")</code><br>
        Especially important with <code>defaultdict</code> (subscript can auto-create).<br>
        No &rarr; go to stop 4
      </div>
      <div class="path-connector" style="justify-content:center">&darr;</div>
      <div class="path-stop s4" style="max-width:none">
        <div class="num">4</div>
        <b>Default home — plain dict</b>
        Use <code>d = {}</code> and set keys yourself: <code>d["a"] = 1</code><br>
        Best for simple records and JSON-like data.
      </div>
    </div>
  </div>
</div>

<h3>Flowchart — defaultdict trap (detail)</h3>
<div class="mm-card">
  <p>When you already chose <code>defaultdict</code>, use this mini-flowchart before reading a key.</p>
  <div class="flow-box">
    <div class="flow-q">Do you intend to<br><b>create or grow</b><br>this key&apos;s group?</div>
    <div class="flow-arrow">&darr; Yes &nbsp;&nbsp;&nbsp; No &darr;</div>
    <div class="flow-row">
      <div class="flow-ans yes"><b>Yes &rarr; use subscript</b>
        <code>myDict["Ravi"].append(101)</code><br>
        Creating the key is what you want.
      </div>
      <div class="flow-ans no"><b>No &rarr; peek safely</b>
        <code>if "Ravi" in myDict:</code><br>
        Never <code>if myDict["Ravi"]:</code> just to check.
      </div>
    </div>
  </div>
</div>

<h3>Path — quick examples</h3>
<div class="path-track">
  <div class="path-stop s1">
    <div class="num">A</div>
    <b>plain dict</b>
    <code>d = {"a": 1}</code><br>
    You own every key.
  </div>
  <div class="path-connector">&rarr;</div>
  <div class="path-stop s2">
    <div class="num">B</div>
    <b>defaultdict</b>
    <code>groups[k].append(v)</code><br>
    Auto empty list/int.
  </div>
  <div class="path-connector">&rarr;</div>
  <div class="path-stop s3">
    <div class="num">C</div>
    <b>key check</b>
    <code>"k" in d</code><br>
    Peek, no create.
  </div>
  <div class="path-connector">&rarr;</div>
  <div class="path-stop s4">
    <div class="num">D</div>
    <b>ChainMap</b>
    <code>ChainMap(D1, D2)</code><br>
    First match wins.
  </div>
</div>

<h3>Cheat sheet</h3>
<table class="data-tbl">
<tr><th>Tool</th><th>When to choose</th><th>Avoid when</th></tr>
<tr><td><code>dict</code></td><td>Simple key/value store you control</td><td>You keep writing <code>if k not in d: d[k]=[]</code></td></tr>
<tr><td><code>defaultdict</code></td><td>Grouping, counters, auto empty list/int</td><td>You only want to <em>check</em> membership (use <code>in</code>)</td></tr>
<tr><td><code>"k" in d</code> / <code>.get</code></td><td>Safe peek — no new key</td><td>You meant to create the group</td></tr>
<tr><td><code>ChainMap</code></td><td>Layered config: overrides + defaults</td><td>You need one merged copy to mutate forever</td></tr>
</table>
"""


# (slide_num, title, short blurb for Notes panel, body html)
NOTES_CONTENT: list[tuple[int, str, str, str]] = [
    (
        NOTES_START,
        "Mindmap",
        "dict · defaultdict · key check · ChainMap",
        _mindmap_body(),
    ),
]


def notes_titles() -> dict[int, str]:
    return {n: title for n, title, _b, _body in NOTES_CONTENT}


def render_notes_slides() -> list[str]:
    """Return list of HTML slide divs for Notes."""
    slides: list[str] = []
    total = len(NOTES_CONTENT)
    for i, (n, title, _blurb, body) in enumerate(NOTES_CONTENT, 1):
        slides.append(
            f'''<div class="slide notes-slide" id="slide-{n}">
<div class="slide-hdr">
  <div class="slide-meta">Notes {i} of {total} &middot; Notes</div>
  <div class="slide-title">{title}</div>
  <div class="slide-sub">Flowchart &amp; path — choose the right mapping tool</div>
</div>
<div class="slide-body">
  <div class="main-split no-code">
    <div class="panel-left">
      {body}
    </div>
  </div>
</div>
</div>'''
        )
    return slides
