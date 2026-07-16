"""Definitions and interview scripts for PythonTraining.html slides."""

TRAINING_META = {
    1: {
        "definition": "We run the .py file using the Python interpreter. Internally, CPython converts it into bytecode (.pyc) and executes the bytecode step by step. Python is a high-level, general-purpose language. C# .cs files are compiled first into a .NET assembly (.dll/.exe), then the CLR/JIT runs the IL.",
        "interview": "A Python .py file can be launched directly with python app.py; CPython compiles it to bytecode (.pyc) and executes it in the interpreter. A C# .cs file is not run directly by JIT — it is compiled to a .NET assembly (.dll/.exe), then CLR/JIT runs the IL. In production, Python is usually deployed as source/package/container, not a DLL. C# commonly publishes a .dll run by dotnet or a self-contained .exe.",
    },
    2: {
        "definition": "On Windows, install Python from python.org, add it to PATH, verify with python --version, then run code in the REPL, as a script (python file.py), or from Cursor/VS Code with the Python extension. Other popular IDEs include PyCharm (JetBrains), Jupyter, Spyder, Visual Studio, and IDLE. Python scripts run top to bottom — define functions before calling them.",
        "interview": "I download from python.org, check 'Add Python to PATH', verify with python --version and pip --version. I run scripts with python hello.py, quick tests in the REPL, and use py -3.12 when multiple versions are installed. In Cursor I select the interpreter and press F5 to debug. Unlike C#, Python script order matters: define functions first, put if __name__ == '__main__' at the bottom.",
    },
    3: {
        "definition": "Primitive types store a single value — for example int, float, str, and bool. Collection types store multiple values — for example list, tuple, set, and dict. This slide builds step by step: first primitives, then collections, then how dictionaries use keys.",
        "interview": "I use tuple when the number of items and meaning are fixed — GPS (lat, lng), RGB color, returning (status, data) from a function. Tuple is hashable so it works as dict key. I use list when I need append/remove/sort — todo items, query results, file lines. If someone could accidentally modify shared data, tuple protects it.",
    },
    4: {
        "definition": "Your training workspace combines this slide deck, Projects/ practice files (one per topic), and Python-Set2/ real projects. Use a virtual environment per project, requirements.txt for dependencies, and Cursor or VS Code as your main IDE.",
        "interview": "I organize learning in three layers: slides for theory, Projects/ for short exercises, Python-Set2/ for full apps. Each project gets its own venv. I open the repo root in Cursor, select the Python 3.12 interpreter, and run files with python or pytest.",
    },
    5: {
        "definition": "Operators perform computation and comparison: arithmetic (+, -, *, /, //, %, **), comparison (==, !=, <), logical (and, or, not), identity (is), membership (in), and bitwise (&, |, ^, ~, <<, >>).",
        "interview": "Key traps: / always returns float in Python 3; // is floor division. is checks object identity, == checks value — I use is only for None. in tests membership in collections. Bitwise ops work on integers at the binary level.",
    },
    6: {
        "definition": "Flow control directs execution: if/elif/else for branching, for/while for loops, break/continue for loop control, pass as a no-op placeholder, and an optional else on loops that runs when no break occurred.",
        "interview": "Indentation defines blocks — no braces. for item in iterable is like foreach. range(5) gives 0–4. while repeats while True. The for-else pattern is useful for search: else runs only if the loop finished without break.",
    },
    7: {
        "definition": "Comprehensions build collections in one expression: list [x for x in items], set {x for x in items}, dict {k: v for k, v in pairs}, and generator (x for x in items) which is lazy.",
        "interview": "Comprehensions are more readable than map/filter for simple transforms. [n*n for n in range(10) if n%2==0] replaces a loop plus append. Generator expressions save memory because they yield one item at a time.",
    },
    8: {
        "definition": "Functions are defined with def. They support positional and keyword args, defaults, *args (extra positional), **kwargs (extra keyword), recursion, lambda for one-liners, LEGB scope lookup, and closures that capture outer variables.",
        "interview": "I avoid mutable default args like def f(lst=[]) — use None instead. *args is a tuple, **kwargs is a dict. LEGB means Local, Enclosing, Global, Builtin. Closures let inner functions remember outer scope — useful for decorators.",
    },
    9: {
        "definition": "Built-in functions operate on iterables and objects: map/filter/reduce transform data; zip/enumerate pair iterables; type/id/isinstance inspect objects; range/len/sorted/reversed handle sequences.",
        "interview": "map applies a function to every element; filter keeps truthy results; reduce folds to one value. enumerate gives (index, value) pairs. isinstance is preferred over type() for inheritance checks. sorted returns a new list; list.sort() sorts in place.",
    },
    10: {
        "definition": "OOP models entities as classes and objects. Python supports __init__ constructors, single/multiple inheritance with MRO, encapsulation via _ convention, polymorphism via overriding, ABC for abstract classes, and dunder methods for operator overloading.",
        "interview": "self is like this in C#. MRO (Method Resolution Order) determines which parent method runs in multiple inheritance. _prefix is convention for protected/private. @abstractmethod enforces interface. __str__ is user-facing, __repr__ is for developers.",
    },
    11: {
        "definition": "Decorators wrap functions or classes to add behavior without changing their source. They use @syntax, nested functions, closures, and functools.wraps to preserve metadata.",
        "interview": "A decorator is a function that takes a function and returns a modified function. @timer above def work() is syntactic sugar for work = timer(work). functools.wraps preserves __name__ and __doc__. FastAPI uses decorators for routes: @app.get('/').",
    },
    12: {
        "definition": "Descriptors control attribute access via __get__, __set__, __delete__. The @property decorator is a built-in descriptor for managed attributes without explicit getter/setter boilerplate.",
        "interview": "Descriptors power properties, class methods, and static methods internally. @property lets me validate on set: @score.setter def score(self, v): assert v >= 0. Custom descriptors are advanced but show deep Python knowledge.",
    },
    13: {
        "definition": "Generators produce values lazily with yield. Iterators implement __iter__ and __next__. itertools provides efficient looping utilities. Generator frame objects hold suspended state between yields.",
        "interview": "yield pauses a function and resumes on next(). Generators are memory-efficient for large datasets. for x in gen: calls __next__ until StopIteration. itertools.chain, groupby, and islice are common in interviews.",
    },
    14: {
        "definition": "Type hints annotate variables, parameters, and return types. typing provides Optional, Union, List, Dict, TypeVar, Generic, Protocol. mypy statically checks types before runtime.",
        "interview": "def greet(name: str) -> str: documents intent without enforcing at runtime. Optional[str] means str or None. Protocol is structural typing — like duck typing with checks. FastAPI uses type hints for automatic validation.",
    },
    15: {
        "definition": "File operations use open() with modes r/w/a, context managers (with) for safe closing, csv/json modules for structured data, and pathlib for object-oriented path handling.",
        "interview": "I always use with open(path, encoding='utf-8') as f — like C# using. pathlib.Path is cleaner than os.path.join. json.loads/dumps for API data. csv.DictReader reads CSV as dicts.",
    },
    16: {
        "definition": "Exceptions are handled with try/except/else/finally. Python has a hierarchy of built-in exceptions. Custom exceptions inherit from Exception. raise and re-raise propagate errors up the call stack.",
        "interview": "Catch specific exceptions, not bare except. else runs if no exception; finally always runs for cleanup. I create custom exceptions like class ValidationError(Exception) for domain errors. raise from preserves the original traceback.",
    },
    17: {
        "definition": "Regular expressions match patterns in text using the re module: match, search, findall, groups, special sequences (\\d, \\w, \\s), and lookahead/lookbehind for advanced matching.",
        "interview": "re.search finds first match anywhere; re.match only at start. Groups capture parts: (\\d+). findall returns all matches. Raw strings r'\\d+' avoid escaping backslashes. I use regex for log parsing and validation.",
    },
    18: {
        "definition": "collections module extends built-in types: Counter counts elements, defaultdict provides default values, OrderedDict preserves order (less needed in 3.7+), ChainMap chains dicts, namedtuple creates tuple subclasses with names, deque is a fast double-ended queue.",
        "interview": "Counter('hello') gives {'h':1,'e':1,'l':2,'o':1}. defaultdict(list) auto-creates empty lists for missing keys — great for grouping. deque appendleft is O(1). namedtuple is lighter than a full class for simple records.",
    },
    19: {
        "definition": "Unit testing verifies code with unittest (TestCase, setUp, tearDown) or pytest (simpler syntax). assert methods check outcomes. unittest.mock patches dependencies. Tests run in a defined order per class.",
        "interview": "pytest uses plain assert — no self.assertEqual boilerplate. setUp runs before each test; tearDown after. @patch('module.requests.get') mocks external calls. I test one behavior per test and name tests descriptively: test_login_invalid_password.",
    },
    20: {
        "definition": "threading runs concurrent tasks in one process but is limited by the GIL for CPU-bound work. multiprocessing and concurrent.futures bypass or manage this for parallel execution.",
        "interview": "The GIL allows only one thread to execute Python bytecode at a time — fine for I/O, bad for CPU-heavy math. threading.Thread plus Lock prevents race conditions. ProcessPoolExecutor for CPU parallelism; ThreadPoolExecutor for I/O.",
    },
    21: {
        "definition": "Context managers guarantee setup/teardown via __enter__/__exit__ or the @contextmanager decorator. The with statement triggers this protocol — used for files, locks, and database connections.",
        "interview": "with open(f) as file: auto-closes even on exception. I can write my own with @contextmanager: yield once between setup and teardown. __exit__ receives exception info and can suppress errors by returning True.",
    },
    22: {
        "definition": "asyncio runs concurrent I/O-bound tasks on one thread via an event loop. async def defines coroutines; await pauses until a result; asyncio.gather runs multiple coroutines; async with/async for extend context managers and iteration.",
        "interview": "async is for I/O concurrency, not CPU parallelism. await only inside async def. asyncio.run(main()) starts the loop. FastAPI endpoints can be async def for non-blocking database and HTTP calls. Don't mix blocking calls in async code.",
    },
    23: {
        "definition": "Virtual environments isolate project dependencies. venv creates them; pip installs packages; requirements.txt pins versions; pyenv manages multiple Python versions on one machine.",
        "interview": "python -m venv .venv then activate. pip freeze > requirements.txt captures exact versions. Never install globally for projects. pyenv lets me switch between Python 3.10 and 3.12 per project.",
    },
    24: {
        "definition": "Python-Set2 is your portfolio of six real project areas covering fundamentals, exercises, data analysis, Django web apps, REST APIs, and voice AI with Pipecat.",
        "interview": "I maintain a structured portfolio: pythonBasics for core topics, google-python-exercises for regex and files, pandas for data, Django/DRF for web APIs, Pipecat for voice AI. I can demo any area on request.",
    },
    25: {
        "definition": "pythonBasics/ has seven modules — MyClass, MyCollections, MyLoops, MyModules, MyExceptionHandling, MyDebug, MyUnitTesting — each with runnable scripts for one topic.",
        "interview": "MyClass has inheritance, polymorphism, and dunder method examples. MyUnitTesting shows pytest patterns. Each folder maps to a curriculum topic — I studied theory in slides then practiced in these folders.",
    },
    26: {
        "definition": "google-python-exercises/ teaches classic puzzles (babynames, copyspecial, logpuzzle). pandas/ has Jupyter notebooks analyzing Titanic and FIFA CSV datasets.",
        "interview": "babynames/ is my go-to for regex practice. copyspecial/ covers os and shutil. Titanic notebook shows read_csv, groupby, and missing value handling — like LINQ on in-memory tables.",
    },
    27: {
        "definition": "djangobasics/meeting_planner/ is a Django 4 app with MVT, templates, auth, and JWT API. DjangoRestBasics/inventory/ is a multi-app DRF project with serializers and ViewSets.",
        "interview": "Django gives ORM, admin, and auth batteries-included. meeting_planner shows real templates and migrations. DRF drink/serializers.py is like Pydantic schemas in FastAPI. I compare both frameworks in interviews.",
    },
    28: {
        "definition": "Pipecat-Project/ contains voice AI POCs: pipecat-quickstart, phase1 (local STT/LLM/TTS), phase2 (full pipeline), and voice-bouncer (IVR-style auth demo).",
        "interview": "Voice pipeline is STT → LLM → TTS over WebRTC. I built it in phases — local services first, then Pipecat framework. voice-bouncer steps through greeting, member ID, zip code — like an IVR system.",
    },
    29: {
        "definition": "A real Python project separates concerns into folders: routes, services, schemas, models, tests, config. Python-Set2 projects demonstrate both learning structure and production patterns.",
        "interview": "I can draw the tree from memory: main.py entry, routes thin, services for logic, tests/ outside app/. Django uses apps per domain; DRF adds serializers. Pipecat adds processors for streaming audio instead of JSON.",
    },
    30: {
        "definition": "Quick reference mapping C# concepts to Python — syntax, stubs (pass vs { }), null/None, OOP, web, async, and tooling — for developers transitioning between languages.",
        "interview": "Key shifts: no type declarations, indentation over braces, pass instead of empty { }, duck typing over interfaces, venv over NuGet global packages. pass ≈ { }; NotImplementedException ≈ NotImplementedError. Similarities: both OOP, both have rich web ecosystems, both use try/except like try/catch.",
    },
    31: {
        "definition": "PEPs document Python standards — PEP 8 style, PEP 257 docstrings, type hints, Zen of Python, and modern packaging via pyproject.toml.",
        "interview": "I follow PEP 8 with snake_case and 4-space indent, use ruff or Black in CI, and know PEP 20 principles from import this. pyproject.toml is the modern way to declare project metadata and dependencies.",
    },
    32: {
        "definition": "Python uses reference counting plus a generational garbage collector for circular references. Understanding refs, gc, and weakref helps debug memory leaks.",
        "interview": "Most objects die when refcount hits zero. Circular references need gc. del removes a name binding; with handles resource cleanup. I profile before tuning GC.",
    },
    33: {
        "definition": "The logging module provides leveled, configurable output for production — DEBUG through CRITICAL, module loggers, handlers, and rotation.",
        "interview": "I use logging.getLogger(__name__), set INFO in prod, logger.exception in except blocks, and lazy % formatting. RotatingFileHandler for disk logs — never print in production services.",
    },
    34: {
        "definition": "Pydantic validates and parses data with type hints — BaseModel, Field constraints, validators, model_dump — core of FastAPI schemas.",
        "interview": "Pydantic at API boundaries gives coercion and ValidationError with field paths. FastAPI returns 422 automatically. from_attributes maps ORM rows to response schemas.",
    },
    35: {
        "definition": "FastAPI + Pydantic + SQLAlchemy is a common production stack — thin routes, service layer, ORM models, session per request via Depends.",
        "interview": "Routes parse HTTP only; services own logic and transactions. Depends(get_db) scopes SQLAlchemy session like DbContext. Separate ORM models from Pydantic API schemas.",
    },
}
