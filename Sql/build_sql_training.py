"""Generate SqlTraining.html from Sql/ source files."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Sql.sql_beginner import BEGINNER_CONTENT
from Sql.sql_catalog import SKILLS
from Sql.sql_content import CONTENT
from Sql.sql_diagrams import diagram_for
from Sql.sql_flowcharts import flowchart_for
from Sql.sql_meta import MODULE_MAP, SECTIONS, SUBTOPICS, TRAINING_META
from track_visual_guides import make_visual_guide_fn, write_svg_posters
from training_deck import DeckConfig, build_deck

SQL_DIR = Path(__file__).resolve().parent
TOTAL_SLIDES = len(CONTENT)


def main() -> None:
    posters = write_svg_posters(SKILLS, SQL_DIR / "images", track="sql")
    cfg = DeckConfig(
        title="SQL Training — Interview",
        total_slides=TOTAL_SLIDES,
        output=SQL_DIR / "SqlTraining.html",
        storage_key="sqlTrainingSlide",
        scroll_key="sqlTrainingScroll",
    )
    nav_intro = f"""
  <h1>SQL Training</h1>
  <p class="sub">Interview curriculum — {TOTAL_SLIDES} topics (S01–S14) from ClientInterviewExpectations.pdf</p>
  <p class="org">Edit <code>Sql/sql_catalog.py</code> → run <code>python Sql/build_sql_training.py</code></p>
  <p style="font-size:12px;margin-top:8px">Style guide: <a href="SqlSlide_guideline.md">SqlSlide_guideline.md</a>
  · <a href="../ClientInterviewExpectations.pdf">PDF</a>
  · Visual guides: <code>Sql/images/</code></p>
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
        code_lang="sql",
        flowchart_fn=flowchart_for,
        diagram_fn=diagram_for,
        visual_guide_fn=make_visual_guide_fn(posters),
    )


if __name__ == "__main__":
    main()
