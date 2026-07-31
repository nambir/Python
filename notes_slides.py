"""MindMap section slides — kid-friendly topic guides for training."""

from __future__ import annotations

import html

from notes_mm_bodies import (
    body_bool_none,
    body_collections,
    body_comprehensions,
    body_dict,
    body_list,
    body_mutable,
    body_numbers,
    body_set,
    body_strings,
    body_tuple,
    body_which_collection,
)

# MindMap slide numbers start here (separate from curriculum 1–35)
NOTES_START = 100

NOTES_CSS = """
.notes-slide .slide-title { border-bottom-color: #7c3aed; }

/* MindMap on homepage — same card style as Week sections */
.nav-section-mindmap {
  grid-column: 1 / -1;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 10px 14px;
}
.nav-section-mindmap h3 {
  font-size: 15px; margin-bottom: 7px; border-bottom: 2px solid #0066cc; padding-bottom: 4px;
  color: #0066cc; font-weight: 700;
}
.nav-section-mindmap .nav-links {
  column-count: 2; column-gap: 24px;
}
@media (max-width: 900px) {
  .nav-section-mindmap .nav-links { column-count: 1; }
}

.dt-intro { font-size: 13px; color: #475569; margin-bottom: 12px; max-width: 720px; }
.dt-legend {
  display: flex; flex-wrap: wrap; gap: 10px 16px; margin: 0 0 14px;
  font-size: 11px; color: #64748b;
}
.dt-legend span { display: inline-flex; align-items: center; gap: 6px; }
.dt-dot { width: 10px; height: 10px; border-radius: 3px; display: inline-block; }
.dt-dot.q { background: #f97316; }
.dt-dot.use { background: #16a34a; }
.dt-dot.peek { background: #ca8a04; }
.dt-dot.layer { background: #7c3aed; }
.dt-dot.plain { background: #2563eb; }

.dt-tree {
  display: flex; flex-direction: column; gap: 0; max-width: 820px;
  border: 1px solid #e2e8f0; border-radius: 12px; overflow: hidden; background: #fff;
}
.dt-start {
  background: linear-gradient(90deg, #4c1d95, #7c3aed);
  color: #fff; padding: 12px 16px; font-weight: 700; font-size: 14px;
}
.dt-start small { display: block; font-weight: 400; opacity: .9; font-size: 12px; margin-top: 2px; }

.dt-row {
  display: grid; grid-template-columns: minmax(280px, 48%) 1fr;
  border-top: 1px solid #e2e8f0; min-height: 0;
  column-gap: 12px;
}
.dt-q {
  padding: 12px 16px; background: #fff7ed; border-right: 3px solid #f97316;
  font-size: 12px; font-weight: 600; color: #9a3412; line-height: 1.35;
  display: grid; grid-template-columns: 1fr 1fr; column-gap: 28px; align-items: center;
}
.dt-q .dt-sit { display: block; }
.dt-q em {
  display: block; font-style: normal; font-weight: 600; color: #9a3412; font-size: 12px;
  margin: 0; line-height: 1.35;
}
.dt-a {
  padding: 12px 14px; font-size: 12px; line-height: 1.45; color: #1e293b;
  display: flex; flex-direction: column; justify-content: center; gap: 4px;
}
.dt-a .pick {
  display: inline-flex; align-items: center; gap: 8px; font-weight: 700; font-size: 13px;
}
.dt-a .pick .tag {
  font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: .3px;
  padding: 2px 7px; border-radius: 999px; color: #fff;
}
.tag-dd { background: #16a34a; }
.tag-cm { background: #7c3aed; }
.tag-key { background: #ca8a04; }
.tag-dict { background: #2563eb; }
.dt-a code { font-size: 11px; }
.dt-a .why { color: #64748b; font-size: 11px; }

.ninode {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin: 16px 0 8px;
}
.ninode-card {
  border-radius: 10px; padding: 12px; border: 1px solid #e2e8f0; background: #fff;
  font-size: 12px; line-height: 1.4; box-shadow: 0 1px 2px rgba(15,23,42,.04);
}
.ninode-card .role {
  font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: .4px;
  margin-bottom: 6px;
}
.ninode-card h4 { margin: 0 0 6px; font-size: 14px; }
.ninode-card.dd { border-top: 3px solid #16a34a; }
.ninode-card.dd .role, .ninode-card.dd h4 { color: #166534; }
.ninode-card.cm { border-top: 3px solid #7c3aed; }
.ninode-card.cm .role, .ninode-card.cm h4 { color: #5b21b6; }
.ninode-card.key { border-top: 3px solid #ca8a04; }
.ninode-card.key .role, .ninode-card.key h4 { color: #a16207; }
.ninode-card.dict { border-top: 3px solid #2563eb; }
.ninode-card.dict .role, .ninode-card.dict h4 { color: #1d4ed8; }

.dt-trap {
  margin: 12px 0; padding: 10px 14px; border-radius: 8px;
  background: #fef2f2; border: 1px solid #fecaca; font-size: 12px; line-height: 1.45; color: #7f1d1d;
}
.dt-trap b { color: #991b1b; }

.mm-sec { margin: 0 0 18px; max-width: 960px; }
.mm-sec h3 {
  margin: 0 0 10px; font-size: 16px; color: #5b21b6; font-weight: 700;
  border-bottom: 2px solid #ddd6fe; padding-bottom: 6px;
}
.mm-sec p { font-size: 13px; color: #334155; line-height: 1.45; margin: 0 0 8px; }
.mm-grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin: 8px 0 4px;
}
.mm-card {
  background: #fff; border: 1px solid #e2e8f0; border-radius: 12px;
  padding: 10px 12px; font-size: 12px; line-height: 1.4; color: #1e293b;
}
.mm-card b { display: block; color: #4c1d95; font-size: 13px; margin-bottom: 4px; }
.mm-card code { font-size: 11px; }
.mm-flow {
  display: flex; flex-wrap: wrap; gap: 8px; align-items: stretch; margin: 8px 0 4px;
}
.mm-step {
  flex: 1 1 140px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px;
  padding: 8px 10px; font-size: 12px; line-height: 1.35; color: #1e293b;
}
.mm-step b { display: block; color: #2563eb; margin-bottom: 2px; font-size: 12px; }
.cheat-tbl .cheat-mean { font-weight: 400; color: #64748b; font-size: 12px; }

/* Section 1 — What is a Dictionary? */
.dict-what {
  display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 4px;
}
.dict-panel {
  background: #fff; border: 1px solid #e2e8f0; border-radius: 14px;
  padding: 18px 20px; min-height: 150px;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
}
.dict-viz {
  border: 1.5px solid #cbd5e1; border-radius: 4px; padding: 14px 18px;
  font-family: ui-monospace, Consolas, monospace; font-size: 14px; line-height: 1.7;
  color: #334155; background: #fafbfc;
}
.dict-viz .kv { display: block; }
.dict-viz .arrow { color: #64748b; margin: 0 8px; }
.dict-remember h4 {
  margin: 0 0 12px; font-size: 16px; color: #1e3a5f; font-weight: 700;
}
.dict-remember .line {
  font-size: 14px; color: #334155; line-height: 1.55; margin: 0 0 6px;
}
.dict-remember .line strong { color: #0f172a; }
.dict-tag {
  display: inline-block; margin-top: 14px;
  background: #e0f2fe; color: #0369a1; font-size: 11px; font-weight: 600;
  padding: 4px 10px; border-radius: 999px;
}

/* Section 2 — Everyday Operations */
.ops-row {
  display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 4px;
}
.ops-row-3 { grid-template-columns: repeat(3, 1fr); }
.ops-row-4 { grid-template-columns: repeat(4, 1fr); }
.mm-card.mm-mem-basic b, .mm-card.mm-mem-iv b { color: #0f766e; }
.mm-card.mm-mem-iv { border-color: #c4b5fd; background: #faf5ff; }
.mm-card.mm-mem-iv b { color: #5b21b6; }
.op-card {
  background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #38bdf8;
  border-radius: 12px; padding: 12px 10px 10px; text-align: center;
  box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
}
.op-ico {
  width: 36px; height: 36px; margin: 0 auto 8px; border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 800; letter-spacing: .3px;
}
.op-ico.new { background: #dbeafe; color: #1d4ed8; font-size: 10px; }
.op-ico.read { background: #e0f2fe; color: #0369a1; font-size: 16px; }
.op-ico.add { background: #dcfce7; color: #15803d; font-size: 18px; }
.op-ico.chg { background: #fef3c7; color: #b45309; font-size: 14px; }
.op-ico.del { background: #fee2e2; color: #b91c1c; font-size: 14px; }
.op-card .op-name { font-size: 13px; font-weight: 700; color: #0f172a; margin-bottom: 8px; }
.op-card .op-code {
  display: block; background: #f1f5f9; border-radius: 6px;
  padding: 6px 4px; font-family: ui-monospace, Consolas, monospace;
  font-size: 11px; color: #334155; word-break: break-all;
}

/* Vertical flowchart under chooser table */
.fc-wrap {
  margin: 18px 0 4px; max-width: 820px;
}
.fc-wrap > .fc-label {
  font-size: 13px; font-weight: 700; color: #5b21b6; margin: 0 0 10px;
}
.fc {
  display: flex; flex-direction: column; align-items: center; gap: 0;
}
.fc-start {
  background: linear-gradient(90deg, #4c1d95, #7c3aed); color: #fff;
  border-radius: 10px; padding: 10px 18px; font-weight: 700; font-size: 13px;
  text-align: center; max-width: 340px; box-shadow: 0 2px 6px rgba(76,29,149,.2);
}
.fc-start small { display: block; font-weight: 400; opacity: .9; font-size: 11px; margin-top: 2px; }
.fc-arrow {
  width: 2px; height: 18px; background: #94a3b8; position: relative; flex-shrink: 0;
}
.fc-arrow::after {
  content: ""; position: absolute; left: 50%; bottom: -1px; transform: translateX(-50%);
  border-left: 5px solid transparent; border-right: 5px solid transparent;
  border-top: 6px solid #94a3b8;
}
.fc-arrow.tall {
  flex: 1 1 auto; height: auto; min-height: 72px;
}
.fc-arrow-lbl {
  font-size: 10px; font-weight: 700; color: #64748b; letter-spacing: .3px;
  margin: 2px 0; flex-shrink: 0;
}
.fc-node {
  display: flex; flex-direction: column; align-items: center;
  width: 100%; max-width: 760px; margin-bottom: 8px;
}
.fc-q-box {
  background: #fff7ed; border: 2px solid #f97316; color: #9a3412;
  border-radius: 10px; padding: 12px 16px; font-size: 13px; font-weight: 600;
  line-height: 1.35; text-align: center; max-width: 300px; margin: 0 auto;
}
.fc-branch {
  display: grid; grid-template-columns: 1fr 56px minmax(240px, 1fr);
  width: 100%; max-width: 760px;
  align-items: stretch; margin: 6px 0 28px; min-height: 120px;
}
.fc-yes {
  grid-column: 3; justify-self: start; align-self: start;
  display: flex; flex-direction: column; align-items: flex-start; gap: 6px;
  padding: 4px 8px 8px 12px;
}
.fc-mid {
  grid-column: 2; display: flex; flex-direction: column; align-items: center;
  justify-content: flex-start; min-height: 100%; padding-top: 2px;
}
.fc-spacer { grid-column: 1; }
.fc-side {
  font-size: 11px; font-weight: 800; letter-spacing: .4px;
}
.fc-side.yes { color: #16a34a; }
.fc-side.no { color: #64748b; }
.fc-h {
  height: 2px; background: #94a3b8; width: 56px; margin: 6px 0 2px;
  position: relative; flex-shrink: 0;
}
.fc-h.right::after {
  content: ""; position: absolute; right: -1px; top: 50%; transform: translateY(-50%);
  border-top: 5px solid transparent; border-bottom: 5px solid transparent;
  border-left: 6px solid #94a3b8;
}
.fc-use {
  border-radius: 12px; padding: 14px 16px; font-size: 13px; line-height: 1.45;
  text-align: left; width: 100%; max-width: 280px; min-width: 220px; min-height: 92px;
  border: 1px solid #e2e8f0; background: #fff;
  box-shadow: 0 2px 6px rgba(15,23,42,.08);
  display: flex; flex-direction: column; justify-content: center; gap: 4px;
}
.fc-use b { display: block; font-size: 14px; margin-bottom: 2px; }
.fc-use code { font-size: 12px; display: block; }
.fc-use .fc-desc {
  display: block; font-size: 12px; font-weight: 500; color: #475569;
  line-height: 1.4; margin: 2px 0 6px;
}
.fc-kid-hint {
  font-size: 13px; color: #475569; margin: 0 0 10px; max-width: 720px;
}
.slide-fc .fc-use {
  max-width: 320px; min-width: 240px; min-height: 110px;
}
.fc-use.key { border-top: 4px solid #ca8a04; }
.fc-use.key b { color: #a16207; }
.fc-use.dd { border-top: 4px solid #16a34a; }
.fc-use.dd b { color: #166534; }
.fc-use.cm { border-top: 4px solid #7c3aed; }
.fc-use.cm b { color: #5b21b6; }
.fc-use.dict { border-top: 4px solid #2563eb; max-width: 300px; min-height: 100px; text-align: center; align-items: center; }
.fc-use.dict b { color: #1d4ed8; }
.fc-end {
  margin-top: 4px;
}

@media (max-width: 900px) {
  .notes-panel { width: 100%; max-width: 420px; margin: 0 auto; }
  .dt-row { grid-template-columns: 1fr; }
  .dt-q { border-right: none; border-bottom: 3px solid #f97316; grid-template-columns: 1fr; }
  .ninode { grid-template-columns: 1fr 1fr; }
  .mm-grid { grid-template-columns: 1fr; }
  .dict-what { grid-template-columns: 1fr; }
  .ops-row { grid-template-columns: 1fr 1fr; }
  .fc-branch { grid-template-columns: 1fr; gap: 10px; min-height: 0; margin-bottom: 20px; }
  .fc-yes, .fc-mid, .fc-spacer { grid-column: 1; justify-self: center; padding: 0; align-items: center; }
  .fc-h { display: none; }
  .fc-use { max-width: 300px; }
}
@media (max-width: 560px) {
  .ninode { grid-template-columns: 1fr; }
  .ops-row { grid-template-columns: 1fr; }
}
"""


def notes_panel_html() -> str:
    """Homepage MindMap block — same card style as Week sections."""
    topics = []
    for i, (n, title, _blurb, _sub, _body) in enumerate(NOTES_CONTENT, 1):
        subs = NOTES_SUBTOPICS.get(n, [])
        sub_html = ""
        if subs:
            items = "".join(
                f'<li><a href="#{n}" onclick="goSlide({n}); return false;">'
                f"{html.escape(s)}</a></li>"
                for s in subs
            )
            sub_html = f'<ul class="nav-subs">{items}</ul>'
        topics.append(
            f'<div class="nav-topic">'
            f'<a class="nav-main" href="#{n}" onclick="goSlide({n}); return false;">'
            f"{i}. {html.escape(title)}</a>"
            f"{sub_html}</div>"
        )
    return (
        '<div class="nav-section nav-section-mindmap" aria-label="MindMap">'
        "<h3>MindMap — Data types</h3>"
        f'<div class="nav-links">{"".join(topics)}</div>'
        "</div>"
    )


# Subtopics under each MindMap link (homepage Week-style dashes)
NOTES_SUBTOPICS: dict[int, list[str]] = {
    100: ["int / float", "/ vs //", "Memory & interview"],
    101: ["Index / slice", "f-string", "Immutable + memory"],
    102: ["True / False", "Truthy / falsy", "None · is None"],
    103: ["Create / CRUD", "Copy vs alias", "Over-allocation"],
    104: ["Fixed record", "Unpacking", "Dict key + memory"],
    105: ["Unique items", "set vs frozenset", "Hash + memory"],
    106: ["Basics · CRUD", "Safe look · helpers", "Chooser + memory"],
    107: ["list vs tuple", "set vs dict", "Chooser flowchart"],
    108: ["Mutable table", "Dict key rule", "Identity vs equality"],
    109: ["Counter · defaultdict", "deque · namedtuple", "ChainMap · OrderedDict"],
    110: ["list / set / dict", "Generator expr", "Memory trade-off"],
}


# (slide_num, title, panel blurb, subtitle, body html)
NOTES_CONTENT: list[tuple[int, str, str, str, str]] = [
    (100, "Numbers", "int · float · / vs //", "Whole & decimal numbers + memory", body_numbers()),
    (101, "Strings", "text · slice · f-string", "Text boxes + memory", body_strings()),
    (102, "Bool & None", "True/False · truthy · None", "Yes/no and nothing + memory", body_bool_none()),
    (103, "List tools", "ordered · mutable · copy", "Row of seats + memory", body_list()),
    (104, "Tuple tools", "fixed · unpack · dict key", "Fixed records + memory", body_tuple()),
    (105, "Set tools", "unique · frozenset", "Unique tags + memory", body_set()),
    (106, "Dict tools", "basics → helpers → pick one", "From dict basics to helpers + memory", body_dict()),
    (107, "Which collection?", "list vs tuple vs set vs dict", "Chooser flowchart + memory", body_which_collection()),
    (108, "Mutable vs immutable", "change? · dict key?", "What can change + memory", body_mutable()),
    (109, "Collections helpers", "Counter · deque · defaultdict…", "collections module + memory", body_collections()),
    (110, "Comprehensions", "list · set · dict · gen", "Short builders + memory", body_comprehensions()),
]


def notes_titles() -> dict[int, str]:
    return {n: title for n, title, *_rest in NOTES_CONTENT}


def render_notes_slides() -> list[str]:
    """Return list of HTML slide divs for MindMap."""
    slides: list[str] = []
    total = len(NOTES_CONTENT)
    for i, (n, title, _blurb, subtitle, body) in enumerate(NOTES_CONTENT, 1):
        slides.append(
            f'''<div class="slide notes-slide" id="slide-{n}">
<div class="slide-hdr">
  <div class="slide-meta">MindMap {i} of {total}</div>
  <div class="slide-title">{title}</div>
  <div class="slide-sub">{subtitle}</div>
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
