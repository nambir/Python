"""Definitions and interview scripts for PythonTraining.html slides."""

_UL = '<ul style="margin:6px 0 8px 18px;font-size:12px;line-height:1.5">'


def _def(intro: str, bullets: list[str]) -> str:
    """Readable Definition block: one intro line + bullet list (Descriptors style)."""
    items = "".join(f"<li>{b}</li>" for b in bullets)
    return f"{intro}{_UL}{items}</ul>"


TRAINING_META = {
    1: {
        "definition": _def(
            "Python is a high-level language you run with the <b>interpreter</b> — "
            "no separate compile-to-DLL step like C#.",
            [
                "<b>How it runs:</b> CPython reads <code>.py</code> → builds <b>bytecode</b> "
                "(<code>.pyc</code>) → executes step by step.",
                "<b>vs C#:</b> <code>.cs</code> → compile to assembly (<code>.dll</code>/<code>.exe</code>) "
                "→ CLR/JIT runs IL.",
                "<b>Deploy:</b> Python usually ships as source/package/container; "
                "C# often publishes a DLL or self-contained exe.",
            ],
        ),
        "interview": "A Python .py file can be launched directly with python app.py; CPython compiles it to bytecode (.pyc) and executes it in the interpreter. A C# .cs file is not run directly by JIT — it is compiled to a .NET assembly (.dll/.exe), then CLR/JIT runs the IL. In production, Python is usually deployed as source/package/container, not a DLL. C# commonly publishes a .dll run by dotnet or a self-contained .exe.",
    },
    2: {
        "definition": _def(
            "Set up Python on Windows, verify it works, then run code from REPL, scripts, or an IDE.",
            [
                "<b>Install:</b> python.org → check <b>Add to PATH</b> → "
                "<code>python --version</code> / <code>pip --version</code>.",
                "<b>Run:</b> REPL for quick tests · <code>python file.py</code> for scripts · "
                "Cursor / VS Code / PyCharm as IDE.",
                "<b>Order matters:</b> scripts run top→bottom — define functions before calling them; "
                "put <code>if __name__ == '__main__'</code> at the bottom.",
            ],
        ),
        "interview": "I download from python.org, check 'Add Python to PATH', verify with python --version and pip --version. I run scripts with python hello.py, quick tests in the REPL, and use py -3.12 when multiple versions are installed. In Cursor I select the interpreter and press F5 to debug. Unlike C#, Python script order matters: define functions first, put if __name__ == '__main__' at the bottom.",
    },
    3: {
        "definition": _def(
            "Your training workspace has <b>three layers</b>: slides (theory), "
            "<code>Projects/</code> (short practice), and <code>Python-Set2/</code> (real apps).",
            [
                "<b>Tools:</b> one <b>venv</b> per project · <code>requirements.txt</code> for deps · "
                "Cursor / VS Code as IDE.",
                "<b>Workflow:</b> open repo root → select Python 3.12 → run with "
                "<code>python</code> or <code>pytest</code>.",
                "<b>Goal:</b> learn theory on slides, then prove it with runnable code.",
            ],
        ),
        "interview": "I organize learning in three layers: slides for theory, Projects/ for short exercises, Python-Set2/ for full apps. Each project gets its own venv. I open the repo root in Cursor, select the Python 3.12 interpreter, and run files with python or pytest.",
    },
    4: {
        "definition": _def(
            "<b>PEPs</b> (Python Enhancement Proposals) document language standards and best practices.",
            [
                "<b>Key PEPs:</b> PEP 8 (style) · PEP 257 (docstrings) · type hints · "
                "Zen of Python (<code>import this</code>).",
                "<b>Style:</b> <code>snake_case</code>, 4-space indent — use ruff / Black in CI.",
                "<b>Packaging:</b> modern projects use <code>pyproject.toml</code> for metadata and deps.",
            ],
        ),
        "interview": "I follow PEP 8 with snake_case and 4-space indent, use ruff or Black in CI, and know PEP 20 principles from import this. pyproject.toml is the modern way to declare project metadata and dependencies.",
    },
    5: {
        "definition": _def(
            "Python types fall into two big groups: <b>primitives</b> (one value) and "
            "<b>collections</b> (many values).",
            [
                "<b>Primitives:</b> <code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code>.",
                "<b>Collections:</b> <code>list</code>, <code>tuple</code>, <code>set</code>, <code>dict</code>.",
                "<b>Pick:</b> <code>tuple</code> when shape is fixed / needs to be a dict key · "
                "<code>list</code> when you need append/remove/sort.",
            ],
        ),
        "interview": "I use tuple when the number of items and meaning are fixed — GPS (lat, lng), RGB color, returning (status, data) from a function. Tuple is hashable so it works as dict key. I use list when I need append/remove/sort — todo items, query results, file lines. If someone could accidentally modify shared data, tuple protects it.",
    },
    6: {
        "definition": _def(
            "<b>Type hints</b> document expected types on variables, parameters, and return values — "
            "Python does <b>not</b> enforce them at runtime by default.",
            [
                "<b>Basics:</b> <code>def greet(name: str) -&gt; str:</code> · "
                "<code>age: int = 25</code>.",
                "<b>Compose:</b> <code>Optional[str]</code> / <code>str | None</code> · "
                "<code>list[int]</code> · <code>dict[str, int]</code> · "
                "<code>TypeVar</code> / <code>Protocol</code>.",
                "<b>Check:</b> run <code>mypy app.py</code> (or CI) — "
                "<code>python app.py</code> alone ignores hints.",
            ],
        ),
        "interview": "def greet(name: str) -> str: documents intent without enforcing at runtime. Optional[str] means str or None. Protocol is structural typing — like duck typing with checks. FastAPI uses type hints for automatic validation.",
    },
    7: {
        "definition": _def(
            "<b>Operators</b> perform computation and comparison — arithmetic, logical, identity, "
            "membership, and bitwise.",
            [
                "<b>Arithmetic:</b> <code>+</code> <code>-</code> <code>*</code> <code>/</code> "
                "(always float) · <code>//</code> floor · <code>%</code> · <code>**</code>.",
                "<b>Compare / logic:</b> <code>==</code> <code>!=</code> · "
                "<code>and</code> <code>or</code> <code>not</code>.",
                "<b>Traps:</b> <code>is</code> = identity (use for <code>None</code>) · "
                "<code>==</code> = value · <code>in</code> = membership.",
            ],
        ),
        "interview": "Key traps: / always returns float in Python 3; // is floor division. is checks object identity, == checks value — I use is only for None. in tests membership in collections. Bitwise ops work on integers at the binary level.",
    },
    8: {
        "definition": _def(
            "<b>Flow control</b> directs which code runs — branches, loops, and early exits. "
            "Indentation defines blocks (no braces).",
            [
                "<b>Branch:</b> <code>if</code> / <code>elif</code> / <code>else</code>.",
                "<b>Loop:</b> <code>for</code> (like foreach) · <code>while</code> · "
                "<code>break</code> / <code>continue</code> · <code>pass</code> placeholder.",
                "<b>for…else:</b> <code>else</code> runs only if the loop finished "
                "<b>without</b> <code>break</code> — useful for search.",
            ],
        ),
        "interview": "Indentation defines blocks — no braces. for item in iterable is like foreach. range(5) gives 0–4. while repeats while True. The for-else pattern is useful for search: else runs only if the loop finished without break.",
    },
    9: {
        "definition": _def(
            "<b>Comprehensions</b> build collections in one readable expression "
            "instead of a loop + <code>append</code>.",
            [
                "<b>Forms:</b> list <code>[x for x in items]</code> · "
                "set <code>{x for x in items}</code> · "
                "dict <code>{k: v for k, v in pairs}</code>.",
                "<b>Filter:</b> add <code>if</code> — "
                "<code>[n*n for n in range(10) if n % 2 == 0]</code>.",
                "<b>Generator:</b> <code>(x for x in items)</code> is lazy — "
                "saves memory vs a full list.",
            ],
        ),
        "interview": "Comprehensions are more readable than map/filter for simple transforms. [n*n for n in range(10) if n%2==0] replaces a loop plus append. Generator expressions save memory because they yield one item at a time.",
    },
    10: {
        "definition": _def(
            "Functions are defined with <code>def</code>. Python also supports "
            "<b>functional-programming</b> ideas alongside normal OOP/procedural style.",
            [
                "<b>Core:</b> positional / keyword args · <code>*args</code> / <code>**kwargs</code> · "
                "<code>lambda</code> · LEGB scope · closures.",
                "<b>FP ideas:</b> pure functions · first-class / higher-order functions · "
                "recursion · prefer immutable data where helpful.",
                "<b>Trap:</b> never use mutable defaults — "
                "<code>def f(cart=[])</code> shares one list across calls.",
            ],
        ),
        "interview": "A pure function always returns the same output for the same inputs and has no side effects — easier to test and parallelize. Functions are first-class: I can pass them to sorted(..., key=...) or return them from factories (closures). I avoid mutable defaults like def f(lst=[]).",
    },
    11: {
        "definition": _def(
            "<b>Built-in functions</b> work on iterables and objects — transform, inspect, "
            "and sequence helpers you use every day.",
            [
                "<b>Transform:</b> <code>map</code> · <code>filter</code> · "
                "<code>reduce</code> (functools) · <code>zip</code> · <code>enumerate</code>.",
                "<b>Inspect:</b> <code>type</code> · <code>id</code> · "
                "<code>isinstance</code> (prefer over <code>type() ==</code> for inheritance).",
                "<b>Sequences:</b> <code>range</code> · <code>len</code> · "
                "<code>sorted</code> (new list) · <code>list.sort()</code> (in place) · "
                "<code>reversed</code>.",
            ],
        ),
        "interview": "map applies a function to every element; filter keeps truthy results; reduce folds to one value. enumerate gives (index, value) pairs. isinstance is preferred over type() for inheritance checks. sorted returns a new list; list.sort() sorts in place.",
    },
    12: {
        "definition": _def(
            "The <code>collections</code> module adds specialized containers beyond "
            "plain list / dict / tuple.",
            [
                "<b>Counting / grouping:</b> <code>Counter</code> · "
                "<code>defaultdict</code> (auto-creates missing keys).",
                "<b>Structure:</b> <code>namedtuple</code> (named fields) · "
                "<code>deque</code> (fast ends) · <code>ChainMap</code> (layered dicts).",
                "<b>Note:</b> <code>OrderedDict</code> is less needed in 3.7+ "
                "(normal dict keeps insertion order).",
            ],
        ),
        "interview": "Counter('hello') gives {'h':1,'e':1,'l':2,'o':1}. defaultdict(list) auto-creates empty lists for missing keys — great for grouping. deque appendleft is O(1). namedtuple is lighter than a full class for simple records.",
    },
    13: {
        "definition": _def(
            "Python frees memory with <b>reference counting</b> plus a "
            "<b>generational GC</b> for circular references.",
            [
                "<b>Refcount:</b> when count hits zero, the object is reclaimed immediately.",
                "<b>Cycles:</b> A↔B need the <code>gc</code> module — refcount alone is not enough.",
                "<b>Tools:</b> <code>del</code> removes a name · <code>weakref</code> · "
                "<code>with</code> for resource cleanup — profile before tuning GC.",
            ],
        ),
        "interview": "Most objects die when refcount hits zero. Circular references need gc. del removes a name binding; with handles resource cleanup. I profile before tuning GC.",
    },
    14: {
        "definition": _def(
            "<b>Pydantic</b> validates and parses data using type hints — "
            "the schema layer behind FastAPI.",
            [
                "<b>Core:</b> <code>BaseModel</code> · <code>Field</code> constraints · "
                "validators · <code>model_dump()</code>.",
                "<b>Why?</b> Coercion + clear <code>ValidationError</code> at API boundaries "
                "(FastAPI → HTTP 422).",
                "<b>ORM bridge:</b> <code>from_attributes=True</code> maps SQLAlchemy rows "
                "to response schemas.",
            ],
        ),
        "interview": "Pydantic at API boundaries gives coercion and ValidationError with field paths. FastAPI returns 422 automatically. from_attributes maps ORM rows to response schemas.",
    },
    15: {
        "definition": _def(
            "<b>OOP</b> models entities as <b>classes</b> and <b>objects</b> — "
            "blueprint + instance, like C#.",
            [
                "<b>Basics:</b> <code>__init__</code> · <code>self</code> (like <code>this</code>) · "
                "inheritance · polymorphism (override).",
                "<b>Python extras:</b> multiple inheritance + <b>MRO</b> · "
                "<code>_</code> / <code>__</code> encapsulation convention · "
                "ABC / <code>@abstractmethod</code>.",
                "<b>Dunders:</b> <code>__str__</code> (humans) · <code>__repr__</code> (devs) · "
                "<code>__eq__</code> · <code>__len__</code> · <code>super().__init__()</code>.",
            ],
        ),
        "interview": "self is like this in C#. MRO (Method Resolution Order) determines which parent method runs in multiple inheritance. _prefix is convention for protected/private. @abstractmethod enforces interface. __str__ is user-facing, __repr__ is for developers.",
    },
    16: {
        "definition": _def(
            "A <b>descriptor</b> is a <b>helper object</b> (think: security guard) that controls "
            "how an attribute is <b>read</b>, <b>written</b>, or <b>deleted</b>.",
            [
                "<b>Why?</b> Without it, <code>person.age = -20</code> is stored. "
                "With it, Python asks the helper first and can raise <code>ValueError</code>.",
                "<b>Create in 2 steps:</b> "
                "(1) helper class with <code>__get__</code> / <code>__set__</code> · "
                "(2) attach it — <code>price = PositiveNumber()</code> "
                "(stores a helper, not a number).",
                "<b>Non-data</b> = only <code>__get__</code> (write can bypass).",
                "<b>Data</b> = <code>__get__</code> + <code>__set__</code> "
                "(every write goes through the guard).",
                "<code>@property</code> is a built-in <b>data</b> descriptor.",
            ],
        ),
        "interview": (
            "A descriptor sits between your code and an attribute via __get__/__set__/__delete__. "
            "Non-data has only __get__ — instance assignment can bypass it. "
            "Data has __set__ too — validates every write (e.g. price >= 0). "
            "@property is a built-in data descriptor. Store values in obj.__dict__ inside __set__ "
            "to avoid infinite recursion."
        ),
    },
    17: {
        "definition": _def(
            "<b>Generators</b> return <b>lazy iterators</b> via <code>yield</code> — "
            "loop like a list without storing all values in memory.",
            [
                "<b>Why?</b> <code>file.read().split()</code> on a huge CSV can "
                "<code>MemoryError</code>; <code>yield</code> one row at a time stays safe.",
                "<b>vs return:</b> <code>return</code> ends with one result · "
                "<code>yield</code> pauses and can produce many values.",
                "<b>Also:</b> generator expressions · infinite sequences · pipelines "
                "(Real Python / PEP 255).",
            ],
        ),
        "interview": "Reading a huge CSV with file.read().split() can MemoryError. A generator yields one row at a time. yield pauses and keeps state; return ends the function. I also use generator expressions and chain generators into pipelines.",
    },
    18: {
        "definition": _def(
            "A <b>decorator</b> wraps a function or class to add behavior "
            "<b>without changing its source</b>.",
            [
                "<b>Syntax:</b> <code>@timer</code> above <code>def work()</code> means "
                "<code>work = timer(work)</code>.",
                "<b>How:</b> nested function + closure · use <code>functools.wraps</code> "
                "to keep <code>__name__</code> / <code>__doc__</code>.",
                "<b>Real use:</b> FastAPI routes <code>@app.get('/')</code> · "
                "logging · timing · auth checks.",
            ],
        ),
        "interview": "A decorator is a function that takes a function and returns a modified function. @timer above def work() is syntactic sugar for work = timer(work). functools.wraps preserves __name__ and __doc__. FastAPI uses decorators for routes: @app.get('/').",
    },
    19: {
        "definition": _def(
            "<b>Exceptions</b> signal errors. Handle them with "
            "<code>try</code> / <code>except</code> / <code>else</code> / <code>finally</code>.",
            [
                "<b>Rules:</b> catch <b>specific</b> types — avoid bare <code>except:</code>.",
                "<b>Blocks:</b> <code>else</code> runs if no error · "
                "<code>finally</code> always runs (cleanup).",
                "<b>Custom:</b> <code>class ValidationError(Exception)</code> · "
                "<code>raise</code> / <code>raise from</code> to propagate with context.",
            ],
        ),
        "interview": "Catch specific exceptions, not bare except. else runs if no exception; finally always runs for cleanup. I create custom exceptions like class ValidationError(Exception) for domain errors. raise from preserves the original traceback.",
    },
    20: {
        "definition": _def(
            "Start from <b>cores</b>, then <b>process vs thread</b>, then the CPython <b>GIL</b>.",
            [
                "<b>Process</b> = one app · <b>thread</b> = worker inside it · "
                "3 apps → at least 3 processes.",
                "<b>GIL:</b> one Python bytecode runner per process — I/O releases it.",
                "<b>ThreadPoolExecutor</b> for I/O · <b>ProcessPoolExecutor</b> for CPU · "
                "<code>Lock</code> for shared data.",
            ],
        ),
        "interview": (
            "Process vs thread: separate memory vs shared memory. "
            "GIL is per CPython process — threads for I/O, processes for CPU math. "
            "ThreadPool for downloads; ProcessPool for resize. "
            "Three Python apps = three processes minimum."
        ),
    },
    21: {
        "definition": _def(
            "<b>asyncio</b> runs many I/O-bound tasks on <b>one thread</b> using an event loop — "
            "concurrency, not CPU parallelism.",
            [
                "<b>Keywords:</b> <code>async def</code> (coroutine) · "
                "<code>await</code> (pause until ready) · "
                "<code>asyncio.gather</code> (run many together).",
                "<b>Start:</b> <code>asyncio.run(main())</code> · "
                "also <code>async with</code> / <code>async for</code>.",
                "<b>Trap:</b> don’t call blocking I/O inside async code — "
                "FastAPI can use <code>async def</code> endpoints for non-blocking DB/HTTP.",
            ],
        ),
        "interview": "async is for I/O concurrency, not CPU parallelism. await only inside async def. asyncio.run(main()) starts the loop. FastAPI endpoints can be async def for non-blocking database and HTTP calls. Don't mix blocking calls in async code.",
    },
    22: {
        "definition": _def(
            "The <code>logging</code> module is production output — levels, timestamps, "
            "and routing to files/agents (not <code>print</code>).",
            [
                "<b>Levels:</b> DEBUG → INFO → WARNING → ERROR → CRITICAL.",
                "<b>Pattern:</b> <code>logging.getLogger(__name__)</code> · "
                "INFO in prod · <code>logger.exception</code> inside <code>except</code>.",
                "<b>Handlers:</b> console · <code>RotatingFileHandler</code> · "
                "lazy <code>%</code> formatting.",
            ],
        ),
        "interview": "I use logging.getLogger(__name__), set INFO in prod, logger.exception in except blocks, and lazy % formatting. RotatingFileHandler for disk logs — never print in production services.",
    },
    23: {
        "definition": _def(
            "<b>Unit tests</b> verify one behavior at a time — "
            "<code>unittest</code> or simpler <code>pytest</code>.",
            [
                "<b>unittest:</b> <code>TestCase</code> · <code>setUp</code> / <code>tearDown</code> · "
                "assert methods.",
                "<b>pytest:</b> plain <code>assert</code> · less boilerplate · "
                "great for day-to-day work.",
                "<b>Mocks:</b> <code>unittest.mock</code> / <code>@patch</code> "
                "for external calls (HTTP, DB).",
            ],
        ),
        "interview": "pytest uses plain assert — no self.assertEqual boilerplate. setUp runs before each test; tearDown after. @patch('module.requests.get') mocks external calls. I test one behavior per test and name tests descriptively: test_login_invalid_password.",
    },
    24: {
        "definition": _def(
            "<b>Regular expressions</b> match text patterns with the <code>re</code> module — "
            "validation, parsing, log scraping.",
            [
                "<b>Search:</b> <code>re.search</code> (anywhere) · "
                "<code>re.match</code> (start only) · <code>re.findall</code> (all).",
                "<b>Pieces:</b> groups <code>(\\d+)</code> · "
                "<code>\\d</code> <code>\\w</code> <code>\\s</code> · "
                "lookahead / lookbehind.",
                "<b>Tip:</b> always use raw strings — <code>r'\\d+'</code> — "
                "to avoid backslash headaches.",
            ],
        ),
        "interview": "re.search finds first match anywhere; re.match only at start. Groups capture parts: (\\d+). findall returns all matches. Raw strings r'\\d+' avoid escaping backslashes. I use regex for log parsing and validation.",
    },
    25: {
        "definition": _def(
            "File I/O uses <code>open()</code>, context managers, and helpers for "
            "CSV / JSON / paths.",
            [
                "<b>Safe open:</b> <code>with open(path, encoding='utf-8') as f:</code> "
                "(like C# <code>using</code>) — auto-closes.",
                "<b>Modes:</b> <code>r</code> read · <code>w</code> write · <code>a</code> append.",
                "<b>Helpers:</b> <code>pathlib.Path</code> · <code>json</code> · "
                "<code>csv.DictReader</code>.",
            ],
        ),
        "interview": "I always use with open(path, encoding='utf-8') as f — like C# using. pathlib.Path is cleaner than os.path.join. json.loads/dumps for API data. csv.DictReader reads CSV as dicts.",
    },
    26: {
        "definition": _def(
            "A <b>context manager</b> guarantees setup/teardown — "
            "the <code>with</code> statement triggers it.",
            [
                "<b>Protocol:</b> <code>__enter__</code> / <code>__exit__</code> · "
                "or <code>@contextmanager</code> + one <code>yield</code>.",
                "<b>Why?</b> Files, locks, DB connections close even if an exception occurs.",
                "<b>Custom:</b> setup → <code>yield</code> → teardown; "
                "<code>__exit__</code> can suppress errors by returning <code>True</code>.",
            ],
        ),
        "interview": "with open(f) as file: auto-closes even on exception. I can write my own with @contextmanager: yield once between setup and teardown. __exit__ receives exception info and can suppress errors by returning True.",
    },
    27: {
        "definition": _def(
            "A <b>virtual environment</b> isolates project dependencies so packages "
            "don’t clash across projects.",
            [
                "<b>Create / use:</b> <code>python -m venv .venv</code> → activate → "
                "<code>pip install …</code>.",
                "<b>Pin:</b> <code>pip freeze &gt; requirements.txt</code> · "
                "install with <code>pip install -r requirements.txt</code>.",
                "<b>Rule:</b> never install project packages globally · "
                "pyenv can manage multiple Python versions.",
            ],
        ),
        "interview": "python -m venv .venv then activate. pip freeze > requirements.txt captures exact versions. Never install globally for projects. pyenv lets me switch between Python 3.10 and 3.12 per project.",
    },
    28: {
        "definition": _def(
            "<b>FastAPI + Pydantic + SQLAlchemy</b> is a common production Python API stack.",
            [
                "<b>Layers:</b> routes (HTTP only) · services (business + transactions) · "
                "ORM models · Pydantic schemas.",
                "<b>DI:</b> <code>Depends(get_db)</code> scopes a session per request "
                "(like <code>DbContext</code>).",
                "<b>Rule:</b> keep routes thin — don’t mix SQL and HTTP parsing in one function.",
            ],
        ),
        "interview": "Routes parse HTTP only; services own logic and transactions. Depends(get_db) scopes SQLAlchemy session like DbContext. Separate ORM models from Pydantic API schemas.",
    },
    29: {
        "definition": _def(
            "<code>Python-Set2</code> is your <b>portfolio</b> of six real project areas "
            "you can demo in interviews.",
            [
                "<b>Areas:</b> fundamentals · exercises · pandas · Django · DRF · "
                "Pipecat voice AI.",
                "<b>Why?</b> Proves you didn’t only read slides — you ran and built apps.",
                "<b>Tip:</b> pick one folder and walk through it aloud.",
            ],
        ),
        "interview": "I maintain a structured portfolio: pythonBasics for core topics, google-python-exercises for regex and files, pandas for data, Django/DRF for web APIs, Pipecat for voice AI. I can demo any area on request.",
    },
    30: {
        "definition": _def(
            "<code>pythonBasics/</code> has <b>seven topic modules</b> — each a runnable "
            "mini-lab for one skill.",
            [
                "<b>Modules:</b> MyClass · MyCollections · MyLoops · MyModules · "
                "MyExceptionHandling · MyDebug · MyUnitTesting.",
                "<b>OOP focus:</b> MyClass — inheritance, polymorphism, dunder methods.",
                "<b>How to use:</b> open the folder → run the <code>.py</code> → "
                "explain it in interview language.",
            ],
        ),
        "interview": "MyClass has inheritance, polymorphism, and dunder method examples. MyUnitTesting shows pytest patterns. Each folder maps to a curriculum topic — I studied theory in slides then practiced in these folders.",
    },
    31: {
        "definition": _def(
            "Practice data and text skills with classic exercises plus pandas notebooks.",
            [
                "<b>google-python-exercises:</b> babynames (regex) · copyspecial (files) · "
                "logpuzzle.",
                "<b>pandas:</b> Jupyter notebooks on Titanic / FIFA CSV — "
                "<code>read_csv</code>, <code>groupby</code>, missing values.",
                "<b>Feel:</b> like LINQ on in-memory tables.",
            ],
        ),
        "interview": "babynames/ is my go-to for regex practice. copyspecial/ covers os and shutil. Titanic notebook shows read_csv, groupby, and missing value handling — like LINQ on in-memory tables.",
    },
    32: {
        "definition": _def(
            "Two web stacks in the portfolio: <b>Django MVT</b> and <b>Django REST Framework</b>.",
            [
                "<b>Django:</b> <code>meeting_planner</code> — models, templates, migrations, auth, JWT.",
                "<b>DRF:</b> <code>inventory</code> — serializers, ViewSets, multi-app layout.",
                "<b>Compare:</b> Django = batteries-included web · DRF serializers ≈ "
                "Pydantic schemas in FastAPI.",
            ],
        ),
        "interview": "Django gives ORM, admin, and auth batteries-included. meeting_planner shows real templates and migrations. DRF drink/serializers.py is like Pydantic schemas in FastAPI. I compare both frameworks in interviews.",
    },
    33: {
        "definition": _def(
            "<code>Pipecat-Project/</code> has voice-AI POCs — speech in, LLM, speech out.",
            [
                "<b>Pipeline:</b> STT → LLM → TTS (often over WebRTC).",
                "<b>Phases:</b> quickstart · phase1 (local services) · phase2 (full pipeline) · "
                "voice-bouncer (IVR-style auth).",
                "<b>Demo tip:</b> explain greeting → member ID → zip like a phone IVR.",
            ],
        ),
        "interview": "Voice pipeline is STT → LLM → TTS over WebRTC. I built it in phases — local services first, then Pipecat framework. voice-bouncer steps through greeting, member ID, zip code — like an IVR system.",
    },
    34: {
        "definition": _def(
            "A real Python project <b>separates concerns</b> into clear folders — "
            "thin routes, fat services.",
            [
                "<b>Typical tree:</b> routes · services · schemas · models · tests · config.",
                "<b>Rules:</b> <code>main.py</code> entry · tests outside app · "
                "one job per layer.",
                "<b>Variants:</b> Django apps per domain · DRF serializers · "
                "Pipecat processors for audio streams.",
            ],
        ),
        "interview": "I can draw the tree from memory: main.py entry, routes thin, services for logic, tests/ outside app/. Django uses apps per domain; DRF adds serializers. Pipecat adds processors for streaming audio instead of JSON.",
    },
    35: {
        "definition": _def(
            "Quick map from <b>C# habits</b> to <b>Python</b> — same ideas, different syntax.",
            [
                "<b>Syntax:</b> indentation not braces · <code>elif</code> · "
                "<code>pass</code> ≈ empty <code>{ }</code> · <code>None</code> ≈ <code>null</code>.",
                "<b>OOP / typing:</b> explicit <code>self</code> · duck typing · "
                "type hints optional at runtime.",
                "<b>Tooling:</b> venv + pip ≈ NuGet isolation · "
                "<code>try/except</code> ≈ <code>try/catch</code> · async in both ecosystems.",
            ],
        ),
        "interview": "Key shifts: no type declarations, indentation over braces, pass instead of empty { }, duck typing over interfaces, venv over NuGet global packages. pass ≈ { }; NotImplementedException ≈ NotImplementedError. Similarities: both OOP, both have rich web ecosystems, both use try/except like try/catch.",
    },
}
