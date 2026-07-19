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


# Keys = sequential slide numbers (syllabus order)
DIAGRAMS: dict[int, str] = {
    1: "",  # interpreter diagram already injected for slide 1
    2: stack(
        "First-day setup checklist",
        [
            ("1. Install", "python.org — check Add to PATH"),
            ("2. Verify", "python --version  ·  pip --version"),
            ("3. IDE", "Cursor / VS Code — select interpreter"),
            ("4. Run", "python file.py  or  F5 debug"),
        ],
        "If python works but pip fails, use <code>python -m pip</code>.",
    ),
    3: tree(
        "Training workspace",
        ("Repo root", "one Cursor window"),
        [
            ("Slides", "PythonTraining.html — theory"),
            ("Projects/", "short drills per topic"),
            ("Python-Set2/", "full apps & demos"),
        ],
    ),
    4: grid(
        "PEP standards map",
        [
            ("PEP 8", "style / snake_case"),
            ("PEP 257", "docstrings"),
            ("PEP 20", "Zen · import this"),
            ("PEP 621", "pyproject.toml"),
            ("ruff / Black", "CI auto-check"),
        ],
    ),
    5: fork(
        "Which datatype?",
        "What do you need to store?",
        [
            ("One value", "int · str · float · bool"),
            ("Growing / mixed", "list []"),
            ("Fixed record", "tuple () — hashable"),
            ("Lookup / unique", "dict {} · set"),
        ],
        "Cart/logs → list. GPS / (ok, data) → tuple.",
    ),
    6: stack(
        "Typing layers",
        [
            ("Write hints", "def charge(amount: Decimal) -> str"),
            ("Static check", "mypy / pyright before run"),
            ("Runtime (optional)", "Pydantic / FastAPI enforce"),
            ("Docs & IDE", "autocomplete + clearer APIs"),
        ],
        "Hints alone do not change runtime — checkers / frameworks enforce them.",
    ),
    7: grid(
        "Operator families",
        [
            ("Arithmetic", "+ − * / // % **"),
            ("Compare", "== != &lt; &gt;"),
            ("Assign", "= += :="),
            ("Logic", "and or not"),
            ("Membership", "in · not in"),
            ("Identity", "is · is not"),
            ("Bitwise", "&amp; | ^ ~ &lt;&lt; &gt;&gt;"),
            ("Walrus", "n := len(x)"),
        ],
    ),
    8: fork(
        "Flow control choices",
        "What should the program do next?",
        [
            ("Branch", "if / elif / else"),
            ("Repeat", "for · while"),
            ("Skip / stop", "continue · break"),
            ("Stub", "pass (empty block)"),
        ],
    ),
    9: grid(
        "Comprehension shapes",
        [
            ("List", "[x for x in …]"),
            ("Set", "{x for x in …}"),
            ("Dict", "{k: v for …}"),
            ("Generator", "(x for x in …) lazy"),
        ],
        "Same idea: source → expression → optional filter. Shape = brackets.",
    ),
    10: hub(
        "Function anatomy",
        ("def name(...)", "callable unit"),
        [
            ("Args", "pos / kw / *args / **kwargs"),
            ("Scope", "LEGB lookup"),
            ("return", "value out"),
            ("lambda", "one-line anonymous"),
            ("Recursion", "fn calls itself"),
            ("Higher-order", "pass / return fn"),
        ],
    ),
    11: grid(
        "Built-in toolbox",
        [
            ("map", "transform each"),
            ("filter", "keep matches"),
            ("reduce", "fold to one"),
            ("zip", "pair iterables"),
            ("enumerate", "index + value"),
            ("sorted", "new ordered list"),
            ("max / min", "extreme values"),
            ("type / id", "inspect object"),
        ],
    ),
    12: grid(
        "collections module",
        [
            ("Counter", "tallies / pie charts"),
            ("defaultdict", "auto-create keys"),
            ("deque", "fast left/right ends"),
            ("namedtuple", "light records"),
            ("OrderedDict", "remember insert order"),
            ("ChainMap", "stack of dicts"),
        ],
    ),
    13: cycle(
        "Object memory lifecycle",
        [
            ("Create", "refcount = 1"),
            ("Share names", "refcount ↑"),
            ("del / rebind", "refcount ↓"),
            ("Zero", "free now"),
        ],
        "Circular refs need <code>gc</code> (generational collector).",
    ),
    14: stack(
        "Pydantic validation stack",
        [
            ("Raw input", "JSON / dict / form"),
            ("BaseModel", "typed schema"),
            ("Field + validators", "rules &amp; coerce"),
            ("model_dump", "clean dict out"),
        ],
        "Invalid → ValidationError (FastAPI → HTTP 422).",
    ),
    15: tree(
        "OOP building blocks",
        ("class Account", "blueprint + __init__ + self"),
        [
            ("SavingsAccount", "inherit — reuse deposit/withdraw"),
            ("override month_end", "polymorphism — same call, different behavior"),
            ("ABC / abstract", "force subclasses to implement"),
        ],
    ),
    16: hub(
        "Descriptor protocol",
        ("obj.x", "attribute access"),
        [
            ("__get__", "read"),
            ("__set__", "write / validate"),
            ("__delete__", "remove"),
            ("@property", "built-in descriptor"),
        ],
    ),
    17: cycle(
        "Generator pause / resume",
        [
            ("yield", "pause + value"),
            ("next()", "resume"),
            ("locals live", "state kept"),
            ("StopIteration", "done"),
        ],
        "Lazy — one item at a time; great for huge files.",
    ),
    18: hub(
        "Decorator wrap",
        ("@decorator", "f = wrap(f)"),
        [
            ("before", "log / auth / timer start"),
            ("call f", "original body"),
            ("after", "cleanup / log end"),
            ("wraps", "keep name &amp; docstring"),
        ],
    ),
    19: cycle(
        "Exception path",
        [
            ("try", "risky code"),
            ("except", "handle"),
            ("else", "no error"),
            ("finally", "always"),
        ],
        "<code>finally</code> runs even if you return or raise again.",
    ),
    20: fork(
        "Concurrency — pick the tool",
        "What is the work waiting on?",
        [
            ("I/O wait", "threading · ThreadPoolExecutor (GIL OK)"),
            ("CPU heavy", "multiprocessing · ProcessPoolExecutor"),
            ("Many sockets", "asyncio (see next slide)"),
        ],
        "GIL = one Python bytecode thread at a time.",
    ),
    21: cycle(
        "Async event loop",
        [
            ("async def", "coroutine"),
            ("await", "yield control"),
            ("event loop", "schedule others"),
            ("gather", "many at once"),
        ],
        "Do not call blocking I/O inside async code.",
    ),
    22: stack(
        "Logging pipeline",
        [
            ("Logger", "getLogger(__name__)"),
            ("Level filter", "DEBUG → CRITICAL"),
            ("Handler", "console / RotatingFileHandler"),
            ("Formatter", "time + level + message"),
        ],
        'Prefer <code>logger.info("x=%s", x)</code> over f-strings when filtered.',
    ),
    23: cycle(
        "Unit test cycle",
        [
            ("Arrange", "setUp / fixtures"),
            ("Act", "call code"),
            ("Assert", "assert / assertEqual"),
            ("Cleanup", "tearDown"),
        ],
        "Mock external APIs with <code>@patch</code> so CI stays offline.",
    ),
    24: hub(
        "Regex toolkit",
        ("re module", "pattern engine"),
        [
            ("search", "find anywhere"),
            ("match", "only at start"),
            ("findall", "all hits"),
            ("groups", "(…) capture"),
            ("sub", "replace"),
            ("raw r'…'", "fewer \\\\ escapes"),
        ],
    ),
    25: stack(
        "File I/O layers",
        [
            ("Locate", "pathlib.Path / open path"),
            ("with open", "auto-close (even on error)"),
            ("Read / write", "text or bytes"),
            ("Structured", "csv · json modules"),
        ],
    ),
    26: cycle(
        "Context manager protocol",
        [
            ("with", "start"),
            ("__enter__", "acquire"),
            ("body", "use resource"),
            ("__exit__", "release"),
        ],
        "Same idea as C# <code>using</code> — cleanup is guaranteed.",
    ),
    27: stack(
        "Virtual environment",
        [
            ("Create", "python -m venv .venv"),
            ("Activate", "isolate this project"),
            ("Install", "pip install …"),
            ("Freeze", "pip freeze &gt; requirements.txt"),
        ],
        "Never install project libs into the global Python.",
    ),
    28: stack(
        "FastAPI + SQLAlchemy layers",
        [
            ("Route (FastAPI)", "HTTP in/out — thin"),
            ("Schema (Pydantic)", "validate request/response"),
            ("Service", "business rules + transaction"),
            ("ORM (SQLAlchemy)", "tables / Session"),
            ("Database", "SQLite / Postgres / …"),
        ],
        "Depends(get_db) ≈ scoped DbContext per request.",
    ),
    29: tree(
        "Portfolio map",
        ("Python-Set2", "interview demos"),
        [
            ("pythonBasics", "core language topics"),
            ("google + pandas", "files, regex, data"),
            ("Django / DRF", "web + REST"),
            ("Pipecat", "voice AI"),
        ],
    ),
    30: grid(
        "pythonBasics modules",
        [
            ("MyClass", "OOP"),
            ("MyCollections", "list/dict/set"),
            ("MyLoops", "flow control"),
            ("MyModules", "import / packages"),
            ("MyException", "try/except"),
            ("MyDebug", "pdb"),
            ("MyUnitTesting", "unittest / mock"),
        ],
    ),
    31: compare(
        "Practice tracks",
        ("Google exercises", ["babynames — regex on HTML", "copyspecial — os / shutil"]),
        ("Pandas notebook", ["read_csv", "dropna / groupby", "charts for stakeholders"]),
    ),
    32: compare(
        "Web stack choices",
        ("Django + DRF", ["MVT + admin + auth", "Serializers / ViewSets", "batteries included"]),
        ("FastAPI", ["async routes", "Pydantic built-in", "OpenAPI docs free"]),
    ),
    33: flow(
        "Voice AI pipeline",
        [
            ("Audio in", "mic / WebRTC"),
            ("STT", "speech → text"),
            ("LLM", "decide reply"),
            ("TTS", "text → speech"),
        ],
        "Genuine pipeline — order matters (kept as left→right).",
    ),
    34: stack(
        "Project layout",
        [
            ("main / entry", "start app"),
            ("routes/", "HTTP only — thin"),
            ("services/", "business logic"),
            ("schemas / models", "DTOs + ORM"),
            ("tests/", "pytest at repo root"),
        ],
    ),
    35: compare(
        "C# ↔ Python quick map",
        ("C#", ["{ } braces", "null", "this", "using (…)", "NuGet"]),
        ("Python", ["indent + :", "None / is None", "self", "with …", "pip + venv"]),
        "Empty stub: C# { } ≈ Python <code>pass</code>. Stronger: NotImplementedException ≈ NotImplementedError.",
    ),
}


def diagram_for(n: int) -> str:
    return DIAGRAMS.get(n, "")
