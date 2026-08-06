"""Merged skill catalog for DotnetTraining — D01…D60 from Skill Matrix CSV."""

from Dotnet.dotnet_catalog_part1 import SKILLS_PART1
from Dotnet.dotnet_catalog_part2 import SKILLS_PART2

AREA_TITLES = {
    "D1": "D1 — C# Core",
    "D2": "D2 — ASP.NET & Web",
    "D3": "D3 — Data & SQL",
    "D4": "D4 — Engineering Craft",
    "D5": "D5 — Architecture",
    "D6": "D6 — Stories & Impact",
}

SKILLS = list(SKILLS_PART1) + list(SKILLS_PART2)

assert len(SKILLS) == 60
assert [s["id"] for s in SKILLS] == [f"D{i:02d}" for i in range(1, 61)]
