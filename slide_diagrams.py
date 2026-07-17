"""Concept flow diagrams for every slide — injected under Definition."""

from __future__ import annotations


def flow(title: str, steps: list[tuple[str, str]], note: str = "") -> str:
    """Horizontal concept diagram (Source → … → Result style)."""
    nodes = []
    for i, (label, detail) in enumerate(steps):
        if i:
            nodes.append('<div class="cdiag-arrow">&rarr;</div>')
        nodes.append(
            f'<div class="cdiag-node"><b>{label}</b><span>{detail}</span></div>'
        )
    note_html = f'<p class="flow-note">{note}</p>' if note else ""
    return f'''
<h3>{title}</h3>
<div class="cdiag">
  <div class="cdiag-row">
    {"".join(nodes)}
  </div>
  {note_html}
</div>
'''


def stack(title: str, layers: list[tuple[str, str]], note: str = "") -> str:
    """Vertical layered diagram."""
    rows = "".join(
        f'<div class="cdiag-layer"><b>{lab}</b><span>{det}</span></div>'
        for lab, det in layers
    )
    note_html = f'<p class="flow-note">{note}</p>' if note else ""
    return f'''
<h3>{title}</h3>
<div class="cdiag cdiag-stack">
  {rows}
  {note_html}
</div>
'''


# Keys = NEW sequential slide numbers (syllabus order)
DIAGRAMS: dict[int, str] = {
    1: "",  # full interpreter diagram already injected for slide 1
    2: flow(
        "Setup path",
        [
            ("Install Python", "python.org / Store"),
            ("Check versions", "python --version"),
            ("pip ready", "pip --version"),
            ("Open IDE", "Cursor / VS Code"),
            ("Run .py", "python file.py"),
        ],
        "If python works but pip fails, repair PATH or use <code>python -m pip</code>.",
    ),
    3: flow(
        "Training workspace flow",
        [
            ("Read slide", "PythonTraining.html"),
            ("Open practice", "Projects/"),
            ("Run & edit", "python …"),
            ("Go deeper", "Python-Set2/"),
        ],
    ),
    4: flow(
        "PEP standards map",
        [
            ("PEP 8", "style / naming"),
            ("PEP 257", "docstrings"),
            ("PEP 20", "Zen / import this"),
            ("PEP 621", "pyproject.toml"),
            ("Linters", "ruff / Black"),
        ],
    ),
    5: flow(
        "Choose a datatype",
        [
            ("Primitives", "int str float bool"),
            ("list", "grows / mixed OK"),
            ("tuple", "fixed record"),
            ("dict / set", "lookup / unique"),
        ],
        "Cart/logs → list. GPS / (ok, data) → tuple. Watch list memory jump on append (over-allocation).",
    ),
    6: flow(
        "Typing workflow",
        [
            ("Write hints", "x: int"),
            ("Optional tools", "mypy / pyright"),
            ("Catch bugs", "before runtime"),
            ("Docs", "clearer APIs"),
        ],
        "Hints do not change runtime by themselves — checkers enforce them.",
    ),
    7: flow(
        "Operator families",
        [
            ("Arithmetic", "+ - * / // % **"),
            ("Compare", "== != < >"),
            ("Assign", "= += :="),
            ("Logic", "and or not"),
            ("Bits / in / is", "& | in is"),
        ],
    ),
    8: flow(
        "Flow control",
        [
            ("Condition", "if / elif / else"),
            ("Iterate", "for / while"),
            ("Control", "break / continue"),
            ("Stub", "pass"),
        ],
    ),
    9: flow(
        "Comprehension pipeline",
        [
            ("Source", "iterable"),
            ("Transform", "expression"),
            ("Filter", "optional if"),
            ("Result", "list / set / dict / gen"),
        ],
    ),
    10: flow(
        "Function call path",
        [
            ("def", "define"),
            ("Args", "pos / kw / *args"),
            ("Body", "LEGB lookup"),
            ("return", "value out"),
        ],
    ),
    11: flow(
        "Built-in toolbox",
        [
            ("Transform", "map / filter"),
            ("Combine", "zip / enumerate"),
            ("Reduce", "reduce / max / min"),
            ("Inspect", "type / id / isinstance"),
        ],
    ),
    12: flow(
        "collections module",
        [
            ("Counter", "counts"),
            ("defaultdict", "auto keys"),
            ("deque", "fast ends"),
            ("namedtuple", "fields"),
            ("OrderedDict", "order"),
        ],
    ),
    13: flow(
        "Memory lifecycle",
        [
            ("Create object", "refcount +1"),
            ("More names", "refcount ↑"),
            ("del / rebind", "refcount ↓"),
            ("Zero refs", "free now"),
            ("Cycles", "gc.collect"),
        ],
    ),
    14: flow(
        "Pydantic validation",
        [
            ("Raw JSON/dict", "input"),
            ("BaseModel", "schema"),
            ("Validate", "Field / validators"),
            ("model_dump", "clean dict"),
        ],
        "Invalid data → ValidationError (FastAPI → HTTP 422).",
    ),
    15: flow(
        "OOP building blocks",
        [
            ("class", "blueprint"),
            ("__init__", "create"),
            ("self", "instance"),
            ("inherit", "reuse"),
            ("override", "polymorphism"),
        ],
    ),
    16: flow(
        "Descriptor protocol",
        [
            ("attr access", "obj.x"),
            ("__get__", "read"),
            ("__set__", "write"),
            ("@property", "common case"),
        ],
    ),
    17: flow(
        "Generator execution",
        [
            ("def + yield", "pause"),
            ("next()", "resume"),
            ("state kept", "locals live"),
            ("StopIteration", "done"),
        ],
    ),
    18: flow(
        "Decorator wrap",
        [
            ("Original fn", "f"),
            ("@decorator", "wrap"),
            ("Call site", "f()"),
            ("Wrapper runs", "before/after"),
        ],
        "Use <code>functools.wraps</code> to keep the original name/doc.",
    ),
    19: flow(
        "Exception path",
        [
            ("try", "risky code"),
            ("except", "handle"),
            ("else", "no error"),
            ("finally", "always"),
        ],
    ),
    20: stack(
        "Concurrency choices",
        [
            ("threading", "I/O wait — shared memory; limited by GIL for CPU"),
            ("multiprocessing", "CPU work — separate processes"),
            ("concurrent.futures", "ThreadPool / ProcessPool helpers"),
        ],
    ),
    21: flow(
        "Async event loop",
        [
            ("async def", "coroutine"),
            ("await", "yield control"),
            ("event loop", "schedule"),
            ("gather", "run many"),
        ],
    ),
    22: flow(
        "Logging pipeline",
        [
            ("Logger", "getLogger"),
            ("Level", "DEBUG→CRITICAL"),
            ("Handler", "console / file"),
            ("Formatter", "time + msg"),
        ],
    ),
    23: flow(
        "Unit test cycle",
        [
            ("Arrange", "setUp"),
            ("Act", "call code"),
            ("Assert", "assert*"),
            ("Cleanup", "tearDown"),
        ],
    ),
    24: flow(
        "Regex workflow",
        [
            ("Pattern", "r'…'"),
            ("Compile/search", "re module"),
            ("Match/groups", "extract"),
            ("Replace/split", "transform"),
        ],
    ),
    25: flow(
        "File I/O",
        [
            ("open/path", "locate"),
            ("with", "auto-close"),
            ("read/write", "bytes/text"),
            ("CSV/JSON", "structured"),
        ],
    ),
    26: flow(
        "Context manager",
        [
            ("with expr", "enter"),
            ("__enter__", "acquire"),
            ("body", "use resource"),
            ("__exit__", "release"),
        ],
    ),
    27: flow(
        "Virtual environment",
        [
            ("python -m venv", "create"),
            ("activate", "isolate"),
            ("pip install", "packages"),
            ("freeze", "requirements.txt"),
        ],
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
    29: flow(
        "Portfolio path",
        [
            ("pythonBasics", "fundamentals"),
            ("exercises", "files/regex"),
            ("pandas", "data"),
            ("Django/DRF", "web"),
            ("Pipecat", "voice AI"),
        ],
    ),
    30: flow(
        "pythonBasics modules",
        [
            ("MyClass", "OOP"),
            ("MyCollections", "data"),
            ("MyLoops", "flow"),
            ("MyException", "errors"),
            ("MyUnitTesting", "pytest"),
        ],
    ),
    31: flow(
        "Data practice path",
        [
            ("google exercises", "files + regex"),
            ("CSV load", "pandas"),
            ("clean / groupby", "analyze"),
            ("notebook", "explain results"),
        ],
    ),
    32: flow(
        "Web frameworks",
        [
            ("Django", "full MVT + admin"),
            ("DRF", "REST on Django"),
            ("FastAPI", "async APIs + Pydantic"),
        ],
    ),
    33: flow(
        "Voice AI pipeline",
        [
            ("Audio in", "mic / WebRTC"),
            ("STT", "speech→text"),
            ("LLM", "logic"),
            ("TTS", "text→speech"),
        ],
    ),
    34: stack(
        "Project layout",
        [
            ("main / entry", "start app"),
            ("routes", "HTTP only"),
            ("services", "business logic"),
            ("schemas / models", "DTOs + ORM"),
            ("tests/", "pytest"),
        ],
    ),
    35: flow(
        "C# → Python map",
        [
            ("{ }", "indent + :"),
            ("null", "None / is None"),
            ("this", "self"),
            ("using", "with"),
            ("NuGet", "pip + venv"),
        ],
    ),
}


def diagram_for(n: int) -> str:
    return DIAGRAMS.get(n, "")
