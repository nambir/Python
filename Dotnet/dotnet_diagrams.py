"""Concept diagrams for DotnetTraining.html."""

from __future__ import annotations

from Dotnet.dotnet_assemble import DIAGRAMS


def diagram_for(n: int) -> str:
    return DIAGRAMS.get(n, "")
