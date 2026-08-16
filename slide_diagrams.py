"""Concept diagrams for every slide — varied layouts (not only left→right flow).

Slide 1 keeps the dedicated interpreter diagram in build_training.py.
"""

from __future__ import annotations


def _note(note: str) -> str:
    return f'<p class="flow-note">{note}</p>' if note else ""


def flow(title: str, steps: list[tuple[str, str]], note: str = "") -> str:
    """Horizontal pipeline — use only when order truly matters."""
    nodes = []
    for i, (label, detail) in enumerate(steps):
        if i:
            nodes.append('<div class="cdiag-arrow">&rarr;</div>')
        nodes.append(
            f'<div class="cdiag-node"><b>{label}</b><span>{detail}</span></div>'
        )
    return f'''
<h3>{title}</h3>
<div class="cdiag">
  <div class="cdiag-row">{"".join(nodes)}</div>
  {_note(note)}
</div>
'''


def stack(title: str, layers: list[tuple[str, str]], note: str = "") -> str:
    """Vertical layers (architecture / priority)."""
    rows = "".join(
        f'<div class="cdiag-layer"><b>{lab}</b><span>{det}</span></div>'
        for lab, det in layers
    )
    return f'''
<h3>{title}</h3>
<div class="cdiag cdiag-stack">{rows}{_note(note)}</div>
'''


def grid(title: str, cells: list[tuple[str, str]], note: str = "") -> str:
    """Category tiles — families / toolbox (no implied order)."""
    tiles = "".join(
        f'<div class="cdiag-tile"><b>{lab}</b><span>{det}</span></div>'
        for lab, det in cells
    )
    return f'''
<h3>{title}</h3>
<div class="cdiag">
  <div class="cdiag-grid">{tiles}</div>
  {_note(note)}
</div>
'''


def tree(title: str, root: tuple[str, str], children: list[tuple[str, str]], note: str = "") -> str:
    """Hierarchy — parent with children underneath."""
    kids = "".join(
        f'<div class="cdiag-tree-child"><b>{lab}</b><span>{det}</span></div>'
        for lab, det in children
    )
    return f'''
<h3>{title}</h3>
<div class="cdiag cdiag-tree">
  <div class="cdiag-tree-root"><b>{root[0]}</b><span>{root[1]}</span></div>
  <div class="cdiag-tree-stem"></div>
  <div class="cdiag-tree-kids">{kids}</div>
  {_note(note)}
</div>
'''


def cycle(title: str, steps: list[tuple[str, str]], note: str = "") -> str:
    """Circular / looping process."""
    parts = []
    for i, (lab, det) in enumerate(steps):
        parts.append(f'<div class="cdiag-cycle-node"><b>{lab}</b><span>{det}</span></div>')
        if i < len(steps) - 1:
            parts.append('<div class="cdiag-cycle-arrow">&rarr;</div>')
        else:
            parts.append('<div class="cdiag-cycle-arrow cdiag-cycle-back">&circlearrowleft;</div>')
    return f'''
<h3>{title}</h3>
<div class="cdiag">
  <div class="cdiag-cycle">{"".join(parts)}</div>
  {_note(note)}
</div>
'''


def hub(title: str, center: tuple[str, str], spokes: list[tuple[str, str]], note: str = "") -> str:
    """Center concept with surrounding related ideas."""
    around = "".join(
        f'<div class="cdiag-spoke"><b>{lab}</b><span>{det}</span></div>'
        for lab, det in spokes
    )
    return f'''
<h3>{title}</h3>
<div class="cdiag cdiag-hub">
  <div class="cdiag-spokes">{around}</div>
  <div class="cdiag-hub-core"><b>{center[0]}</b><span>{center[1]}</span></div>
  {_note(note)}
</div>
'''


def fork(title: str, question: str, branches: list[tuple[str, str]], note: str = "") -> str:
    """Decision / branch diagram."""
    arms = "".join(
        f'<div class="cdiag-fork-arm"><b>{lab}</b><span>{det}</span></div>'
        for lab, det in branches
    )
    return f'''
<h3>{title}</h3>
<div class="cdiag cdiag-fork">
  <div class="cdiag-fork-q"><b>{question}</b></div>
  <div class="cdiag-fork-stem"></div>
  <div class="cdiag-fork-arms">{arms}</div>
  {_note(note)}
</div>
'''


def compare(title: str, left: tuple[str, list[str]], right: tuple[str, list[str]], note: str = "") -> str:
    """Side-by-side comparison."""
    left_items = "".join(f"<li>{x}</li>" for x in left[1])
    right_items = "".join(f"<li>{x}</li>" for x in right[1])
    return f'''
<h3>{title}</h3>
<div class="cdiag cdiag-compare">
  <div class="cdiag-compare-col">
    <h4>{left[0]}</h4>
    <ul>{left_items}</ul>
  </div>
  <div class="cdiag-compare-vs">vs</div>
  <div class="cdiag-compare-col">
    <h4>{right[0]}</h4>
    <ul>{right_items}</ul>
  </div>
  {_note(note)}
</div>
'''


# Primary concept diagrams — rich build maps (same style as GIL diagram)
from slide_rich_diagrams import RICH_DIAGRAMS  # noqa: E402

DIAGRAMS: dict[int, str] = RICH_DIAGRAMS


def diagram_for(n: int) -> str:
    """Primary concept diagram + optional learning helper diagram."""
    primary = DIAGRAMS.get(n, "")
    helper = EXTRA_DIAGRAMS.get(n, "")
    return primary + helper


# Second diagram per slide — traps, when-to-use, or before/after (complements primary)
EXTRA_DIAGRAMS: dict[int, str] = {
    1: grid(
        "Why teams pick Python",
        [
            ("Fast to write", "few lines vs C#"),
            ("Batteries included", "os · json · pathlib"),
            ("Duck typing", "if it has .send(), use it"),
            ("Huge ecosystem", "pip / PyPI"),
        ],
    ),
    2: compare(
        "Three ways to run code",
        ("REPL", ["Type python", ">>> prompt", "Quick experiments"]),
        ("Script / IDE", ["python hello.py", "F5 in Cursor", "Full programs"]),
        "Define functions first — scripts run top to bottom (unlike C# method order).",
    ),
    3: stack(
        "Study loop (repeat each topic)",
        [
            ("1. Read slide", "definition + diagram"),
            ("2. Run Projects/", "short practice file"),
            ("3. Open Python-Set2", "same idea in a real folder"),
        ],
    ),
    4: compare(
        "Style vs packaging",
        ("Style (humans)", ["PEP 8 naming", "PEP 257 docstrings", "PEP 20 Zen"]),
        ("Packaging (tools)", ["PEP 621 pyproject.toml", "ruff / Black in CI"]),
    ),
    5: compare(
        "Mutable vs immutable",
        ("Can change", ["list", "dict", "set"]),
        ("Cannot change", ["tuple", "frozenset", "str / int"]),
        "Only immutable values can be dict keys (hash must stay stable).",
    ),
    6: compare(
        "Hints vs runtime",
        ("Type hints alone", ["Documentation", "IDE help", "mypy can check"]),
        ("Enforced at runtime", ["Pydantic models", "FastAPI params"]),
        "Without mypy: python app.py still runs charge(\"100\", 91). With mypy: errors reported first.",
    ),
    7: fork(
        "Pick the right check",
        "What are you testing?",
        [
            ("Same value?", "=="),
            ("Same object / None?", "is  (use is None)"),
            ("Inside a collection?", "in"),
            ("Whole numbers only?", "// floor division"),
        ],
    ),
    8: compare(
        "Loop helpers",
        ("break / continue", ["break = leave loop", "continue = next item"]),
        ("pass / for-else", ["pass = empty stub", "else runs if no break"]),
    ),
    9: compare(
        "Comprehension vs loop",
        ("Loop (verbose)", ["net = []", "for g, tax in …:", "  if g > 0: append"]),
        ("Comprehension", ["[g - tax for … if g > 0]", "Same result, shorter"]),
        "Huge data → use generator ( ) so RAM stays low.",
    ),
    10: compare(
        "Pure vs side-effect",
        ("Pure function", ["Same in → same out", "No globals changed", "Easy to test"]),
        ("Impure", ["Prints / writes DB", "Depends on time", "Harder to test"]),
    ),
    11: fork(
        "Which built-in?",
        "What do you need?",
        [
            ("Transform each", "map / listcomp"),
            ("Keep some", "filter"),
            ("Pair two lists", "zip"),
            ("Index + value", "enumerate"),
            ("One answer", "reduce / max / min"),
        ],
    ),
    12: fork(
        "Which collection helper?",
        "What problem?",
        [
            ("Count items", "Counter"),
            ("Missing key default", "defaultdict"),
            ("Queue both ends", "deque"),
            ("Named fields", "namedtuple"),
        ],
    ),
    13: compare(
        "Who frees memory?",
        ("Reference counting", ["del / rebind", "count → 0", "freed immediately"]),
        ("Garbage collector", ["Breaks cycles", "A↔B both live", "gc.collect()"]),
    ),
    14: compare(
        "Hand checks vs Pydantic",
        ("Manual ifs", ["if not email:", "if age < 18:", "easy to miss"]),
        ("BaseModel", ["types + Field", "validators", "HTTP 422 errors"]),
    ),
    15: compare(
        "Reuse strategies",
        ("Inheritance", ["SavingsAccount(Account)", "Is-a relationship", "Override methods"]),
        ("Composition", ["Account has Logger", "Has-a relationship", "Often clearer"]),
    ),
    16: compare(
        "property vs custom descriptor",
        ("@property", ["One class", "Simple get/set", "Most common"]),
        ("Custom descriptor", ["Reuse across models", "__get__/__set__", "ORM-style fields"]),
    ),
    17: compare(
        "List vs generator",
        ("List in memory", ["[…] stores all", "Fast random access", "Can MemoryError"]),
        ("Generator", ["yield one-by-one", "Tiny RAM", "One pass"]),
    ),
    18: stack(
        "What a decorator adds",
        [
            ("Before call", "auth · timer start · retry setup"),
            ("Original function", "your real work"),
            ("After call", "log result · cleanup"),
        ],
        "Remember: @timer above def f means f = timer(f).",
    ),
    19: fork(
        "Exception strategy",
        "What went wrong?",
        [
            ("Known error", "except ValueError: …"),
            ("Several types", "except (OSError, KeyError):"),
            ("Cleanup always", "finally: …"),
            ("Avoid", "bare except:  (hides bugs)"),
        ],
    ),
    20: compare(
        "GIL impact — purpose: can threads help?",
        (
            "I/O-bound (OK)",
            [
                "Download / wait DB / file",
                "Threads fine — waits overlap",
                "Threads release GIL while waiting",
                "Use ThreadPoolExecutor",
            ],
        ),
        (
            "CPU-bound (not OK)",
            [
                "Heavy math / image resize",
                "Threads do not speed Python CPU",
                "Use processes — bypass GIL",
                "Use ProcessPoolExecutor",
            ],
        ),
        note="OK = waiting work · not OK = heavy Python CPU in one process",
    ),
    21: compare(
        "Sync vs async",
        ("Sync def", ["One call waits", "Simple", "Blocks the thread"]),
        ("async def + await", ["Yield while waiting", "Many tasks", "One event loop"]),
    ),
    22: compare(
        "print vs logging",
        ("print", ["Dev only", "No levels", "Hard to turn off"]),
        ("logging", ["DEBUG→CRITICAL", "File + console", "logger.exception"]),
    ),
    23: compare(
        "unittest vs pytest",
        ("unittest", ["TestCase class", "self.assertEqual", "setUp / tearDown"]),
        ("pytest", ["Plain assert", "Fixtures", "Less boilerplate"]),
    ),
    24: compare(
        "search vs match",
        ("re.search", ["Find anywhere", "First hit", "Most common"]),
        ("re.match", ["Only at start", "Like ^pattern", "Easy to misuse"]),
    ),
    25: compare(
        "open vs pathlib",
        ("open + with", ["with open(path) as f:", "Auto-close", "Read/write bytes/text"]),
        ("pathlib.Path", ["Path(\"a\") / \"b\"", "mkdir · exists", "Cleaner joins"]),
    ),
    26: compare(
        "with vs try/finally",
        ("try/finally", ["Manual cleanup", "Easy to forget", "More lines"]),
        ("with / contextmgr", ["__enter__/__exit__", "Always releases", "C# using-like"]),
    ),
    27: compare(
        "Global Python vs venv",
        ("Global install", ["Shared by all apps", "Version clashes", "Risky"]),
        ("Per-project .venv", ["Isolated packages", "requirements.txt", "Safe for clients"]),
    ),
    28: flow(
        "One API request",
        [
            ("HTTP", "route"),
            ("Pydantic", "validate"),
            ("Service", "logic"),
            ("SQLAlchemy", "DB"),
            ("Schema out", "JSON"),
        ],
        "Never return raw ORM — use a response model.",
    ),
    29: flow(
        "Interview demo path",
        [
            ("Basics OOP", "MyClass"),
            ("Regex / files", "google exercises"),
            ("Web API", "Django / DRF"),
            ("Voice AI", "Pipecat"),
        ],
    ),
    30: stack(
        "How to use a module",
        [
            ("Open matching slide", "theory first"),
            ("Run the .py script", "see output"),
            ("Change one line", "confirm you understand"),
        ],
    ),
    31: stack(
        "Data homework pattern",
        [
            ("Load", "read_csv / open file"),
            ("Clean", "nulls · types"),
            ("Analyze", "groupby / regex extract"),
            ("Explain", "notebook / chart"),
        ],
    ),
    32: stack(
        "Typical web request",
        [
            ("URL → view / ViewSet", "controller"),
            ("Model / ORM", "data"),
            ("Template or Serializer", "HTML / JSON out"),
        ],
    ),
    33: hub(
        "Pipecat building blocks",
        ("Pipeline", "audio in → out"),
        [
            ("STT", "speech→text"),
            ("LLM", "decide"),
            ("TTS", "text→speech"),
            ("WebRTC", "browser audio"),
        ],
    ),
    34: fork(
        "Where does this code go?",
        "What is the code doing?",
        [
            ("HTTP only", "routes/"),
            ("Business rule", "services/"),
            ("Shape of data", "schemas/"),
            ("DB table", "models/"),
            ("Verify behavior", "tests/"),
        ],
    ),
    35: grid(
        "Stub & null tips",
        [
            ("pass", "empty block for now"),
            ("NotImplementedError", "must implement later"),
            ("None", "like null — use is None"),
            ("self", "like this (explicit)"),
        ],
    ),
}