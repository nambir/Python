from slide_flowcharts import _render

from Angular.angular_assemble import FLOWS


def flowchart_for(n: int) -> str:
    data = FLOWS.get(n)
    if not data:
        return ""
    start, sub, questions, fb_title, fb_desc, fb_lines = data
    return _render(start, sub, questions, fb_title, fb_desc, fb_lines)
