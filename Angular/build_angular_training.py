"""Generate AngularTraining.html from Angular/ source files."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Angular.angular_beginner import BEGINNER_CONTENT
from Angular.angular_content import CONTENT
from Angular.angular_diagrams import diagram_for
from Angular.angular_flowcharts import flowchart_for
from Angular.angular_meta import MODULE_MAP, SECTIONS, SUBTOPICS, TRAINING_META
from Angular.angular_posters import write_angular_posters
from track_visual_guides import make_visual_guide_fn
from training_deck import DeckConfig, build_deck

ANGULAR_DIR = Path(__file__).resolve().parent
TOTAL_SLIDES = len(CONTENT)


def main() -> None:
    posters = write_angular_posters(ANGULAR_DIR / "images")
    cfg = DeckConfig(
        title="Angular Training — Interview",
        total_slides=TOTAL_SLIDES,
        output=ANGULAR_DIR / "AngularTraining.html",
        storage_key="angularTrainingSlide",
        scroll_key="angularTrainingScroll",
    )
    nav_intro = f"""
  <h1>Angular Training</h1>
  <p class="sub">Interview curriculum — {TOTAL_SLIDES} topics (A01–A14) from ClientInterviewExpectations.pdf</p>
  <p class="org">Edit <code>Angular/angular_catalog.py</code> → run <code>python Angular/build_angular_training.py</code></p>
  <p style="font-size:12px;margin-top:8px">Style guide: <a href="AngularSlide_guideline.md">AngularSlide_guideline.md</a>
  · <a href="../ClientInterviewExpectations.pdf">PDF</a>
  · Visual guides: <code>Angular/images/</code></p>
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
        code_lang="typescript",
        flowchart_fn=flowchart_for,
        diagram_fn=diagram_for,
        visual_guide_fn=make_visual_guide_fn(posters),
    )


if __name__ == "__main__":
    main()
