"""One-page "Visual Guide" poster images per slide.

Drop a PNG/JPG into images/, add it to VISUAL_GUIDES, and the slide gets a
thumbnail (opens full size in a new tab) plus a draggable detached window.
"""

from __future__ import annotations

# slide number -> (path relative to the HTML file, short label, pixel width)
VISUAL_GUIDES: dict[int, tuple[str, str, int]] = {
    1: ("images/slide-01-what-is-python.png", "What is Python?", 1536),
    2: ("images/slide-02-setup-windows.png", "Setup & Run on Windows", 1536),
    3: ("images/slide-03-training-workspace.png", "Your Training Workspace", 1536),
    4: ("images/slide-04-pep-standards.png", "PEP Standards", 1536),
    5: ("images/slide-05-datatypes.png", "Python Datatypes", 1536),
    6: ("images/slide-06-typing.png", "Typing (Type Hints)", 1536),
    7: ("images/slide-07-operators.png", "Operators", 1536),
    8: ("images/slide-08-conditional-flow.png", "Conditional & Flow Control", 1536),
    9: ("images/slide-09-comprehensions.png", "Comprehensions", 1536),
    10: ("images/slide-10-functions.png", "Python Functions", 1536),
    11: ("images/slide-11-builtin-functions.png", "Built-in Functions", 1536),
    12: ("images/slide-12-collections.png", "Python Collections", 1536),
    13: ("images/slide-13-memory-gc.png", "Memory Management & GC", 1536),
    14: ("images/slide-14-pydantic.png", "Pydantic", 1536),
    15: ("images/slide-15-oop-concepts.png", "OOP Concepts", 1536),
    16: ("images/slide-16-descriptors.png", "Descriptors", 1536),
    17: ("images/slide-17-generators-iterators.png", "Generators & Iterators", 1536),
    18: ("images/slide-18-decorators.png", "Decorators", 1536),
    19: ("images/slide-19-exception-handling.png", "Exception Handling", 1536),
    20: ("images/slide-20-threading-gil.png", "Threading & GIL (CPython)", 1536),
    21: ("images/slide-21-async-await.png", "Async / Await (asyncio)", 1536),
    22: ("images/slide-22-logging.png", "Logging", 1536),
    23: ("images/slide-23-unit-testing.png", "Unit Testing", 1536),
    24: ("images/slide-24-regex.png", "Regular Expressions", 1536),
    25: ("images/slide-25-file-operations.png", "File Operations", 1536),
    26: ("images/slide-26-context-manager.png", "Context Manager", 1536),
    27: ("images/slide-27-virtual-environment.png", "Virtual Environment", 1536),
    28: ("images/slide-28-fastapi-sqlalchemy.png", "FastAPI with SQLAlchemy", 1536),
    29: ("images/slide-29-portfolio-overview.png", "Python-Set2 Portfolio", 1536),
    30: ("images/slide-30-pythonbasics-modules.png", "pythonBasics Modules", 1536),
    31: ("images/slide-31-google-exercises-pandas.png", "Google Exercises & Pandas", 1536),
    32: ("images/slide-32-django-drf.png", "Django & Django REST", 1536),
    33: ("images/slide-33-pipecat-voice-ai.png", "Pipecat — Voice AI POCs", 1536),
    34: ("images/slide-34-project-structure-path.png", "Project Structure & Path", 1536),
    35: ("images/slide-35-csharp-vs-python.png", "C# vs Python Reference", 1536),
}


def visual_guide_for(n: int) -> str:
    """Thumbnail strip + detached float window for slide n (empty if none)."""
    entry = VISUAL_GUIDES.get(n)
    if not entry:
        return ""
    src, label, native_w = entry
    win_id = f"vguide-{n}"
    title = f"{label} &ndash; Visual Guide"
    return f'''
<div class="vguide-strip">
  <a class="vguide-thumb" href="{src}" target="_blank" rel="noopener noreferrer"
    title="Open the full-size poster in a new tab">
    <img src="{src}" alt="{label} visual guide poster" loading="lazy" decoding="async">
    <span class="vguide-expand" aria-hidden="true">&#x26F6;</span>
  </a>
  <div class="vguide-txt">
    <b>Visual guide &mdash; {label}</b>
    <span>One-page poster: 6 build steps with diagrams, tables and code.
      Click the thumbnail to open it full size in a new tab.</span>
    <button type="button" class="btn-vguide-win" onclick="openCsharpWin('{win_id}')">
      Open in resizable window
    </button>
  </div>
</div>
<div class="csharp-float-win img-float-win" id="csharp-win-{win_id}" role="dialog"
  aria-labelledby="csharp-win-title-{win_id}">
  <div class="csharp-float-hdr">
    <span class="csharp-float-drag" aria-hidden="true">&#8942;&#8942;</span>
    <h4 id="csharp-win-title-{win_id}">{title}</h4>
    <button type="button" class="btn-img-fit" onclick="toggleImgFloatFit(this)"
      title="Image fits the window (scales when you resize)">Fit</button>
    <button type="button" class="csharp-float-close"
      onclick="closeCsharpWin('{win_id}')" aria-label="Close">&times;</button>
  </div>
  <div class="csharp-float-body csharp-float-body-img" style="--native-w:{native_w}px">
    <a href="{src}" target="_blank" rel="noopener noreferrer"
      title="Open full-size image in a new tab">
      <img src="{src}" alt="{label} visual guide poster" loading="lazy" decoding="async">
    </a>
  </div>
  <div class="csharp-float-resize" title="Drag to resize" aria-hidden="true"></div>
</div>
'''
