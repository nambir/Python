"""Generate ClientInterview/Client1.html — same template as PythonTraining.html."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ClientInterview.client1_catalog import AREA_TITLES, SKILLS
from ClientInterview.client1_posters import write_client1_posters
from ClientInterview.client1_visual_guides import make_client1_visual_guide_fn
from interview_track import build_from_skills
from training_deck import DeckConfig, build_deck

CLIENT_DIR = Path(__file__).resolve().parent
TOTAL_SLIDES = len(SKILLS)

_BUILT = build_from_skills(
    SKILLS,
    AREA_TITLES,
    pdf_href="../Client1 Interview questions.pdf",
)

TRAINING_META = _BUILT["TRAINING_META"]
CONTENT = _BUILT["CONTENT"]
BEGINNER_CONTENT = _BUILT["BEGINNER_CONTENT"]
MODULE_MAP = _BUILT["MODULE_MAP"]
SUBTOPICS = _BUILT["SUBTOPICS"]
SECTIONS = _BUILT["SECTIONS"]

EXTRA_CSS = """
.freq-note { font-size: 12px; color: #9a3412; background: #fff7ed; border: 1px solid #fdba74; border-radius: 6px; padding: 8px 12px; margin: 8px 0 12px; line-height: 1.5; }
.nav-content .sub a { color: #0066cc; }
"""


def main() -> None:
    posters = write_client1_posters(CLIENT_DIR / "Client1-Images")
    cfg = DeckConfig(
        title="Client1 — Interview questions",
        total_slides=TOTAL_SLIDES,
        output=CLIENT_DIR / "Client1.html",
        storage_key="client1InterviewSlide",
        scroll_key="client1InterviewScroll",
        accent_note="Questions consolidated from Client1 Interview questions.pdf",
    )
    nav_intro = f"""
  <h1>Client1 — interview questions</h1>
  <p class="sub">Consolidated from ~39 sessions (2024–2026) · {TOTAL_SLIDES} topics (C01–C20)
    · same deck template as <code>PythonTraining.html</code></p>
  <p class="org">Edit <code>ClientInterview/client1_catalog.py</code> or <code>ClientInterview/Client1.md</code>
    → run <code>python ClientInterview/build_client1.py</code></p>
  <div class="freq-note"><b>How they interview:</b> they start from <i>your</i> architecture, then drill
    whatever you named. Highest-frequency technical topics: <b>JWT / refresh</b>,
    <b>DI lifetimes</b>, <b>SOLID/OCP</b>, <b>Repository + Unit of Work</b>,
    <b>Angular interceptor + token storage + guards</b>, <b>SQL isolation / indexes / SP tune</b>,
    <b>microservices + AWS practical</b>. Do not volunteer a tool you cannot implement.</div>
  <p style="font-size:12px;margin-top:8px">
    Study notes: <a href="Client1.md">Client1.md</a>
    · <a href="../Client1 Interview questions.pdf">Questions PDF</a>
    · <a href="../ClientInterviewExpectations.pdf">Expectations PDF</a>
    · Visual guides: <code>ClientInterview/Client1-Images/</code> (unique poster per slide, PythonTraining thumbnail pattern)
    · Related decks:
    <a href="../PythonTraining.html">Python</a> ·
    <a href="../Dotnet/DotnetTraining.html">.NET</a> ·
    <a href="../Angular/AngularTraining.html">Angular</a> ·
    <a href="../Sql/SqlTraining.html">SQL</a> ·
    <a href="../AWS/AWSTraining.html">AWS</a>
  </p>
"""
    build_deck(
        cfg=cfg,
        content=CONTENT,
        meta=TRAINING_META,
        beginner=BEGINNER_CONTENT,
        module_map=MODULE_MAP,
        sections=SECTIONS,
        subtopics=SUBTOPICS,
        nav_intro=nav_intro,
        code_lang="csharp",
        visual_guide_fn=make_client1_visual_guide_fn(posters),
    )
    page = cfg.output.read_text(encoding="utf-8")
    if EXTRA_CSS not in page:
        page = page.replace("</style>", EXTRA_CSS + "</style>", 1)
    page = page.replace(
        '<a class="file-link" href="../Client1 Interview questions.pdf">ClientInterviewExpectations.pdf</a>',
        '<a class="file-link" href="../Client1 Interview questions.pdf">Client1 Interview questions.pdf</a>'
        ' · <a class="file-link" href="../ClientInterviewExpectations.pdf">Expectations PDF</a>',
    )
    cfg.output.write_text(page, encoding="utf-8")
    print(f"Patched extra CSS and PDF links into {cfg.output}")


if __name__ == "__main__":
    main()
