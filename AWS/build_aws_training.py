"""Generate AWSTraining.html from AWS/ source files."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from AWS.aws_beginner import BEGINNER_CONTENT
from AWS.aws_catalog import SKILLS
from AWS.aws_content import CONTENT
from AWS.aws_diagrams import diagram_for
from AWS.aws_flowcharts import flowchart_for
from AWS.aws_meta import MODULE_MAP, SECTIONS, SUBTOPICS, TRAINING_META
from AWS.aws_posters import write_aws_posters
from track_visual_guides import make_visual_guide_fn
from training_deck import DeckConfig, build_deck

AWS_DIR = Path(__file__).resolve().parent
TOTAL_SLIDES = len(CONTENT)


def main() -> None:
    posters = write_aws_posters(AWS_DIR / "images")
    cfg = DeckConfig(
        title="AWS Training — Interview",
        total_slides=TOTAL_SLIDES,
        output=AWS_DIR / "AWSTraining.html",
        storage_key="awsTrainingSlide",
        scroll_key="awsTrainingScroll",
    )
    nav_intro = f"""
  <h1>AWS Training</h1>
  <p class="sub">Interview curriculum — {TOTAL_SLIDES} topics (W01–W16) from ClientInterviewExpectations.pdf</p>
  <p class="org">Edit <code>AWS/aws_catalog.py</code> → run <code>python AWS/build_aws_training.py</code></p>
  <p style="font-size:12px;margin-top:8px">Style guide: <a href="AWSSlide_guideline.md">AWSSlide_guideline.md</a>
  · <a href="../ClientInterviewExpectations.pdf">PDF</a>
  · Visual guides: <code>AWS/images/</code></p>
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
        code_lang="dockerfile",
        flowchart_fn=flowchart_for,
        diagram_fn=diagram_for,
        visual_guide_fn=make_visual_guide_fn(posters),
    )


if __name__ == "__main__":
    main()
