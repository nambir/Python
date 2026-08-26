"""Generate DotnetTraining.html from Dotnet/ source files."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Dotnet.dotnet_beginner import BEGINNER_CONTENT
from Dotnet.dotnet_catalog import SKILLS
from Dotnet.dotnet_content import CONTENT
from Dotnet.dotnet_diagrams import diagram_for
from Dotnet.dotnet_flowcharts import flowchart_for
from Dotnet.dotnet_meta import MODULE_MAP, SECTIONS, SUBTOPICS, TRAINING_META
from Dotnet.dotnet_posters import write_dotnet_posters
from track_visual_guides import make_visual_guide_fn
from training_deck import DeckConfig, build_deck

DOTNET_DIR = Path(__file__).resolve().parent
TOTAL_SLIDES = len(CONTENT)


def main() -> None:
    posters = write_dotnet_posters(DOTNET_DIR / "images")
    cfg = DeckConfig(
        title=".NET Training — Skill Depth (D01–D72)",
        total_slides=TOTAL_SLIDES,
        output=DOTNET_DIR / "DotnetTraining.html",
        storage_key="dotnetTrainingSlide",
        scroll_key="dotnetTrainingScroll",
    )
    nav_intro = f"""
  <h1>.NET Training</h1>
  <p class="sub">Full skill-depth curriculum — {TOTAL_SLIDES} topics (D01–D60 matrix + D61–D72 PDF gaps)</p>
  <p class="org">Edit <code>Dotnet/dotnet_catalog_part*.py</code> / <code>dotnet_rich.py</code> → run <code>python Dotnet/build_dotnet_training.py</code></p>
  <p style="font-size:12px;margin-top:8px">Style guide: <a href="DotnetSlide_guideline.md">DotnetSlide_guideline.md</a>
  · <a href="Skill_Depth_Matrix_I25054_Sangeetha_Rajendiran_9.csv">Skill matrix CSV</a>
  · Visual guides: <code>Dotnet/images/</code></p>
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
        flowchart_fn=flowchart_for,
        diagram_fn=diagram_for,
        visual_guide_fn=make_visual_guide_fn(posters),
    )


if __name__ == "__main__":
    main()
