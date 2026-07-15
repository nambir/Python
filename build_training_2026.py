"""Generate PythonTraining2026.html slide deck based on Batch 2 plan."""
from pathlib import Path

OUTPUT = Path(__file__).parent / "PythonTraining2026.html"

TOTAL_SLIDES = 21  # 1 navigation + 20 topic sections

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { height: 100%; overflow: hidden; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #fff; color: #1a1a2e; }

.slide { display: none; width: 100%; height: 100vh; padding: 30px 50px 60px 50px; overflow-y: auto; position: relative; }
.slide.active { display: block; }

.slide-hdr { margin-bottom: 16px; }
.slide-meta { font-size: 10px; color: #999; letter-spacing: 1.5px; text-transform: uppercase; }
.slide-title { font-size: 28px; font-weight: 700; color: #1a1a2e; border-bottom: 3px solid #0066cc; padding-bottom: 6px; display: inline-block; }
.slide-sub { font-size: 14px; color: #555; margin-top: 3px; }

h3 { font-size: 16px; color: #0066cc; margin: 14px 0 6px 0; }
h4 { font-size: 14px; color: #333; margin: 10px 0 4px 0; }
p { font-size: 13px; margin-bottom: 6px; line-height: 1.5; }
ul { margin-left: 18px; margin-bottom: 8px; }
li { font-size: 12px; margin-bottom: 2px; line-height: 1.4; }
code { font-family: Consolas, 'Cascadia Mono', monospace; font-size: 12px; background: #f0f7ff; padding: 1px 4px; border-radius: 3px; color: #0000FF; }

.nav-bar { position: fixed; bottom: 0; left: 0; right: 0; height: 44px; background: #f0f0f0; border-top: 1px solid #ccc; display: flex; align-items: center; justify-content: space-between; padding: 0 50px; z-index: 999; }
.nav-bar button { padding: 6px 20px; font-size: 13px; font-weight: 600; border: none; border-radius: 4px; cursor: pointer; }
.nav-bar .btn-prev { background: #666; color: #fff; }
.nav-bar .btn-prev:hover { background: #444; }
.nav-bar .btn-next { background: #0066cc; color: #fff; }
.nav-bar .btn-next:hover { background: #004499; }
.nav-bar .btn-nav { background: #28a745; color: #fff; }
.nav-bar .btn-nav:hover { background: #1e7e34; }
.nav-bar .slide-info { font-size: 12px; color: #555; }

.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
.practice-panel { background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; padding: 14px; }
.practice-panel h3 { margin-top: 0; }
.checklist { list-style: none; margin: 8px 0 0 0; padding: 0; }
.checklist li { padding: 3px 0; font-size: 12px; }
.checklist li::before { content: "\\2610  "; color: #0066cc; }

.nav-content { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: calc(100vh - 44px); padding: 20px; }
.nav-content h1 { font-size: 32px; color: #1a1a2e; margin-bottom: 4px; }
.nav-content .sub { font-size: 16px; color: #0066cc; margin-bottom: 4px; }
.nav-content .org { font-size: 13px; color: #666; margin-bottom: 20px; }
.nav-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; max-width: 900px; width: 100%; }
.nav-section { background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; padding: 14px; max-height: 320px; overflow-y: auto; }
.nav-section h3 { font-size: 13px; color: #1a1a2e; margin-bottom: 8px; border-bottom: 2px solid #0066cc; padding-bottom: 4px; }
.nav-section a { display: block; padding: 3px 0; color: #0066cc; text-decoration: none; font-size: 12px; cursor: pointer; text-align: left; }
.nav-section a:hover { text-decoration: underline; }

@media (max-width: 700px) {
  .slide { padding: 20px 16px 60px; }
  .two-col, .nav-grid { grid-template-columns: 1fr; }
  .nav-bar { padding: 0 16px; }
}
"""

JS = """
let current = 0;
const slideOrder = [0];
for (let i = 1; i <= """ + str(TOTAL_SLIDES - 1) + """; i++) slideOrder.push(i);
const totalTopics = """ + str(TOTAL_SLIDES - 1) + """;

function showSlide(n) {
  if (!slideOrder.includes(n)) return;
  document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
  const el = document.getElementById('slide-' + n);
  if (el) {
    el.classList.add('active');
    current = n;
    el.scrollTop = 0;
    const info = document.getElementById('slideInfo');
    if (info) info.textContent = n === 0 ? 'Navigation' : 'Topic ' + n + ' of ' + totalTopics;
  }
}

function goSlide(n) { showSlide(n); }

function nextSlide() {
  const idx = slideOrder.indexOf(current);
  if (idx < slideOrder.length - 1) showSlide(slideOrder[idx + 1]);
}

function prevSlide() {
  const idx = slideOrder.indexOf(current);
  if (idx > 0) showSlide(slideOrder[idx - 1]);
}

document.addEventListener('keydown', function(e) {
  if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
  if (e.key === 'Home') { e.preventDefault(); showSlide(0); }
});

document.addEventListener('DOMContentLoaded', () => { showSlide(0); });
"""

NAV_BAR = """
<div class="nav-bar">
  <button class="btn-prev" onclick="prevSlide()">&larr; Prev</button>
  <button class="btn-nav" onclick="goSlide(0)">&#9776; Navigation</button>
  <span class="slide-info" id="slideInfo">Navigation</span>
  <button class="btn-next" onclick="nextSlide()">Next &rarr;</button>
</div>
"""


def slide_hdr(n: int, title: str, topic_name: str) -> str:
    sub = topic_name
    return f"""<div class="slide-hdr">
  <div class="slide-meta">Topic {n} &middot; {topic_name}</div>
  <div class="slide-title">{title}</div>
  <div class="slide-sub">{sub}</div>
</div>"""


def topic_slide(n: int, topic_name: str, subtopics: list[str]) -> str:
    learn_html = "<h3>Planned Coverage</h3><ul>" + "".join(
        f"<li>{st}</li>" for st in subtopics
    ) + "</ul>"
    practice_html = """<h3>Practice / Notes</h3>
<ul class="checklist">
  <li>Add code examples you used in class</li>
  <li>Note common interview questions for this topic</li>
  <li>Record tricky edge-cases or caveats</li>
</ul>"""
    return f"""<div class="slide" id="slide-{n}">
{slide_hdr(n, topic_name.title().replace("_", " "), topic_name)}
<div class="two-col">
  <div>{learn_html}</div>
  <div class="practice-panel">
    {practice_html}
  </div>
</div>
</div>"""


TOPICS: list[tuple[str, list[str]]] = [
    ("PYTHON DATATYPES", ["Primitive: int, float, string",
                          "List – mutability, indexing, slicing",
                          "Tuple – immutability, packing/unpacking",
                          "Dictionary – key-value, hashing",
                          "Set & Frozenset – uniqueness, hashing"]),
    ("OPERATORS", ["Arithmetic: + - * / % // **",
                   "Comparison & logical operators",
                   "Identity (is / is not)",
                   "Membership (in / not in)",
                   "Bitwise operators"]),
    ("CONDITIONAL & FLOW CONTROL", ["if / elif / else",
                                    "for loop – iteration, range()",
                                    "while loop – condition, break, continue",
                                    "pass, else clause in loops"]),
    ("COMPREHENSIONS", ["List comprehension",
                        "Set comprehension",
                        "Dictionary comprehension",
                        "Generator expression"]),
    ("PYTHON FUNCTIONS", ["Positional & keyword arguments",
                          "*args and **kwargs",
                          "Recursion",
                          "Anonymous / lambda functions",
                          "Local and global scope (LEGB rule)",
                          "Closures"]),
    ("BUILT-IN FUNCTIONS", ["map(), filter(), reduce()",
                            "zip(), enumerate()",
                            "type(), id(), isinstance()",
                            "range(), len(), sorted(), reversed()"]),
    ("OOP CONCEPTS", ["Class & Object, __init__, self",
                      "Inheritance – single, multiple, MRO",
                      "Encapsulation – private, protected",
                      "Polymorphism – method overriding",
                      "Abstract classes (abc module)",
                      "Dunder / magic methods"]),
    ("DECORATORS", ["Function decorators",
                    "Class decorators",
                    "functools.wraps"]),
    ("DESCRIPTORS", ["__get__, __set__, __delete__",
                     "Property vs descriptor"]),
    ("GENERATORS & ITERATORS", ["Generator functions (yield)",
                                "Generator state – frame object internals",
                                "Iterator protocol (__iter__, __next__)",
                                "itertools module"]),
    ("TYPING", ["Type hints – basic annotations",
                "Optional, Union, List, Dict, Tuple",
                "TypeVar, Generic, Protocol",
                "mypy for static checking"]),
    ("FILE OPERATIONS", ["open(), read, write, append modes",
                         "Context manager with 'with'",
                         "CSV, JSON file handling",
                         "pathlib module"]),
    ("EXCEPTION HANDLING", ["try / except / else / finally",
                            "Built-in exceptions hierarchy",
                            "Custom exceptions",
                            "Raising and re-raising exceptions"]),
    ("REGULAR EXPRESSIONS", ["re module – match, search, findall",
                             "Groups, special sequences",
                             "Lookahead / lookbehind"]),
    ("PYTHON COLLECTIONS", ["Counter, OrderedDict, defaultdict, ChainMap",
                            "namedtuple, deque",
                            "UserDict, UserList, UserString"]),
    ("UNIT TESTING", ["unittest – TestCase, setUp, tearDown",
                      "Order of execution in unit tests",
                      "assert methods",
                      "Mocking – unittest.mock",
                      "pytest basics"]),
    ("THREADING & GIL", ["threading module – Thread, Lock",
                         "Python GIL – what it is and why",
                         "multiprocessing as GIL workaround",
                         "concurrent.futures"]),
    ("CONTEXT MANAGER", ["contextlib.contextmanager",
                         "__enter__ / __exit__ protocol"]),
    ("ASYNC / AWAIT", ["asyncio – event loop basics",
                       "async def, await, coroutines",
                       "asyncio.gather(), asyncio.run()",
                       "async context managers & iterators"]),
    ("VIRTUAL ENVIRONMENT", ["venv – create, activate, deactivate",
                             "pip – install, freeze, requirements.txt",
                             "pyenv for Python version management"]),
]


def build_nav() -> str:
    links = "".join(
        f'<a onclick="goSlide({i + 1})">{i + 1}. {name}</a>'
        for i, (name, _) in enumerate(TOPICS)
    )
    return f"""<div class="slide active" id="slide-0">
<div class="nav-content">
  <h1>Python Training 2026</h1>
  <div class="sub">Batch 2 &middot; Core Language Topics</div>
  <div class="org">Click a topic below to jump to that section</div>
  <div class="nav-grid">
    <div class="nav-section">
      <h3>Topics 1–10</h3>
      {''.join(
        f'<a onclick="goSlide({i + 1})">{i + 1}. {name}</a>'
        for i, (name, _) in enumerate(TOPICS[:10])
      )}
    </div>
    <div class="nav-section">
      <h3>Topics 11–20</h3>
      {''.join(
        f'<a onclick="goSlide({i + 1})">{i + 1}. {name}</a>'
        for i, (name, _) in enumerate(TOPICS[10:], start=10)
      )}
    </div>
  </div>
</div>
</div>"""


def main() -> None:
    slides: list[str] = []
    slides.append(build_nav())
    for idx, (name, subs) in enumerate(TOPICS, start=1):
        slides.append(topic_slide(idx, name, subs))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Training 2026 — Batch 2</title>
  <style>{CSS}</style>
</head>
<body>
{''.join(slides)}
{NAV_BAR}
<script>{JS}</script>
</body>
</html>"""

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Generated {OUTPUT} ({len(slides)} slides)")


if __name__ == "__main__":
    main()

