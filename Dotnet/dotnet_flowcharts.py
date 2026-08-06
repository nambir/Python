"""Decision flowcharts for DotnetTraining.html slides."""

from __future__ import annotations

from slide_flowcharts import _render

from Dotnet.dotnet_assemble import FLOWS


def flowchart_for(n: int) -> str:
    data = FLOWS.get(n)
    if not data:
        return ""
    start, sub, questions, fb_title, fb_desc, fb_lines = data
    return _render(start, sub, questions, fb_title, fb_desc, fb_lines)
