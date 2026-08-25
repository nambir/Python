"""Shared build helper for Angular / SQL / AWS decks."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from interview_track import build_from_skills
from slide_flowcharts import _render
from track_visual_guides import make_visual_guide_fn, write_svg_posters
from training_deck import DeckConfig, build_deck


def flowchart_from(flows: dict):
    def flowchart_for(n: int) -> str:
        data = flows.get(n)
        if not data:
            return ""
        start, sub, questions, fb_title, fb_desc, fb_lines = data
        return _render(start, sub, questions, fb_title, fb_desc, fb_lines)

    return flowchart_for


def build_track(
    *,
    folder: Path,
    html_name: str,
    title: str,
    heading: str,
    sub: str,
    guideline: str,
    skills: list,
    area_titles: dict,
    track: str,
    code_lang: str,
    storage_key: str,
) -> None:
    built = build_from_skills(skills, area_titles)
    posters = write_svg_posters(skills, folder / "images", track=track)
    cfg = DeckConfig(
        title=title,
        total_slides=len(built["CONTENT"]),
        output=folder / html_name,
        storage_key=storage_key,
        scroll_key=storage_key + "Scroll",
    )
    nav_intro = f"""
  <h1>{heading}</h1>
  <p class="sub">{sub}</p>
  <p class="org">Edit the catalog in this folder → run the matching <code>build_*_training.py</code></p>
  <p style="font-size:12px;margin-top:8px">Style: <a href="{guideline}">{guideline}</a>
  · <a href="../ClientInterviewExpectations.pdf">ClientInterviewExpectations.pdf</a>
  · Visual guides: <code>images/</code></p>
"""
    build_deck(
        cfg=cfg,
        content=built["CONTENT"],
        meta=built["TRAINING_META"],
        beginner=built["BEGINNER_CONTENT"],
        module_map=built["MODULE_MAP"],
        sections=built["SECTIONS"],
        subtopics=built["SUBTOPICS"],
        nav_intro=nav_intro,
        code_lang=code_lang,
        flowchart_fn=flowchart_from(built["FLOWS"]),
        visual_guide_fn=make_visual_guide_fn(posters),
    )
    return built
