"""Merged skill catalog for DotnetTraining — D01…D72 (matrix + PDF gaps)."""

from Dotnet.dotnet_catalog_part1 import SKILLS_PART1
from Dotnet.dotnet_catalog_part2 import SKILLS_PART2
from Dotnet.dotnet_catalog_part3 import SKILLS_PART3

AREA_TITLES = {
    "D1": "D1 — C# Core",
    "D2": "D2 — ASP.NET & Web",
    "D3": "D3 — Data & SQL",
    "D4": "D4 — Engineering Craft",
    "D5": "D5 — Architecture",
    "D6": "D6 — Stories & Impact",
    "D7": "D7 — PDF gaps",
}

SKILLS = list(SKILLS_PART1) + list(SKILLS_PART2) + list(SKILLS_PART3)

assert len(SKILLS) == 72
assert [s["id"] for s in SKILLS] == [f"D{i:02d}" for i in range(1, 73)]
