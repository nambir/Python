"""Narration scripts for PythonTraining.html — spoken at 0.75x via edge-tts MP3."""

NARRATIONS = {
    0: (
        "Welcome to Python Training 2026, Batch 2. "
        "This deck covers 30 slides: core Python topics, real projects in Python-Set2, "
        "and a C-sharp versus Python quick reference. "
        "Use the navigation grid to jump to any slide. "
        "Each slide has an audio player with play, pause, reset, and seek. "
        "Press A to play or pause the current slide. "
        "Slides 1 through 23 cover fundamentals. "
        "Slides 24 through 29 cover portfolio projects. "
        "Slide 30 is the C-sharp versus Python cheat sheet."
    ),
    1: (
        "Slide 1: What is Python? "
        "Python is a high-level, general-purpose language. "
        "Unlike C-sharp, Python is interpreted: CPython reads your dot py file, "
        "compiles it to bytecode, then executes it line by line. "
        "Indentation replaces braces. Dynamic typing means no int x declarations. "
        "Practice with Projects slash 00 underscore python underscore fundamentals dot py."
    ),
    2: (
        "Slide 2: Setup and Run Python on Windows. "
        "Install from python dot org, check Add Python to PATH, "
        "verify with python dash dash version and pip dash dash version. "
        "Run scripts with python hello dot py, quick tests in the REPL, "
        "and use py dash 3 dot 12 when multiple versions are installed. "
        "In Cursor, select the interpreter and press F5 to debug."
    ),
    3: (
        "Slide 3: Python Datatypes. "
        "Primitives store a single value: int, float, str, bool. "
        "Collections store multiple values: list, tuple, set, dict, and frozenset. "
        "Lists are mutable; tuples are immutable and can be dict keys. "
        "Sets enforce uniqueness. Dicts map keys to values — keys must be hashable. "
        "Practice with Projects slash 01 underscore datatypes dot py."
    ),
    4: (
        "Slide 4: Your Training Workspace. "
        "Three layers: this slide deck for theory, Projects folder for short exercises, "
        "and Python-Set2 for full applications. "
        "Use one virtual environment per project and requirements dot txt for dependencies. "
        "Open the repo root in Cursor and select the Python 3 dot 12 interpreter."
    ),
    5: (
        "Slide 5: Operators. "
        "Arithmetic: plus, minus, star, slash, floor slash, percent, double star. "
        "Comparison: equals, not equals, less than. "
        "Logical: and, or, not. Identity is checks same object; in checks membership. "
        "Key trap: slash always returns float in Python 3; floor slash returns whole numbers. "
        "Use is only for None."
    ),
    6: (
        "Slide 6: Conditional and Flow Control. "
        "if, elif, else for branching. for and while for loops. "
        "break exits a loop; continue skips to the next iteration. "
        "pass means this block is intentionally empty for now — a stub. "
        "for-else runs only if the loop finished without break — useful for search patterns."
    ),
    7: (
        "Slide 7: Comprehensions. "
        "Build collections in one expression: list comprehension with square brackets, "
        "set with curly braces, dict with key colon value, "
        "and generator with parentheses for lazy evaluation. "
        "Example: squares equals x times x for x in range 5. "
        "Generators save memory by yielding one item at a time."
    ),
    8: (
        "Slide 8: Python Functions. "
        "Define with def. Support positional and keyword arguments, defaults, "
        "star args for extra positional, double star kwargs for extra keyword. "
        "Never use mutable defaults like def f items equals empty list. "
        "Use None and create a new list inside. LEGB scope: Local, Enclosing, Global, Builtin."
    ),
    9: (
        "Slide 9: Built-in Functions. "
        "map applies a function to every element. filter keeps truthy results. "
        "reduce folds to one value. enumerate gives index and value pairs. "
        "zip pairs iterables. isinstance is preferred over type for inheritance checks. "
        "sorted returns a new list; list dot sort sorts in place."
    ),
    10: (
        "Slide 10: OOP Concepts. "
        "Classes and objects with double underscore init for constructors. "
        "self is like this in C-sharp — explicit first parameter. "
        "Inheritance with Method Resolution Order for multiple parents. "
        "Underscore prefix is convention for internal use. "
        "Abstract base classes enforce interfaces. "
        "double underscore str for readable output, double underscore repr for developers."
    ),
    11: (
        "Slide 11: Decorators. "
        "A decorator wraps a function to add behavior without changing its source. "
        "At timer above def work is syntactic sugar for work equals timer of work. "
        "functools dot wraps preserves name and docstring. "
        "FastAPI uses decorators for routes: at app dot get slash."
    ),
    12: (
        "Slide 12: Descriptors. "
        "Descriptors control attribute access via double underscore get, set, delete. "
        "The property decorator is a built-in descriptor for managed attributes. "
        "Use at score dot setter to validate on assignment. "
        "Custom descriptors power properties, class methods, and static methods internally."
    ),
    13: (
        "Slide 13: Generators and Iterators. "
        "yield pauses a function and resumes on next call. "
        "Generators are memory-efficient for large datasets. "
        "for x in gen calls double underscore next until StopIteration. "
        "itertools provides chain, groupby, and islice for efficient looping."
    ),
    14: (
        "Slide 14: Typing. "
        "Type hints annotate parameters and return types. "
        "def greet name colon str arrow str documents intent. "
        "Optional str means str or None. "
        "Protocol is structural typing — duck typing with static checks. "
        "mypy verifies types before runtime. FastAPI uses hints for validation."
    ),
    15: (
        "Slide 15: File Operations. "
        "Always use with open path encoding utf-8 as f — like C-sharp using. "
        "pathlib dot Path is cleaner than os dot path dot join. "
        "json dot loads and dumps for API data. "
        "csv dot DictReader reads CSV as dictionaries."
    ),
    16: (
        "Slide 16: Exception Handling. "
        "try, except, else, finally. Catch specific exceptions, not bare except. "
        "else runs if no exception; finally always runs for cleanup. "
        "Create custom exceptions like class ValidationError of Exception. "
        "raise from preserves the original traceback."
    ),
    17: (
        "Slide 17: Regular Expressions. "
        "The re module matches patterns in text. "
        "re dot search finds first match anywhere; re dot match only at start. "
        "Groups capture parts with parentheses. "
        "Raw strings r backslash d plus avoid escaping backslashes. "
        "Use regex for log parsing and validation."
    ),
    18: (
        "Slide 18: Python Collections. "
        "Counter counts elements. defaultdict provides default values for missing keys. "
        "deque is a fast double-ended queue with O of 1 appendleft. "
        "namedtuple creates lightweight record types. "
        "ChainMap chains multiple dictionaries."
    ),
    19: (
        "Slide 19: Unit Testing. "
        "pytest uses plain assert — no self dot assertEqual boilerplate. "
        "unittest TestCase provides setUp before each test and tearDown after. "
        "at patch mocks external calls. "
        "Name tests descriptively: test underscore login underscore invalid underscore password."
    ),
    20: (
        "Slide 20: Threading and the GIL. "
        "The Global Interpreter Lock allows only one thread to execute Python bytecode at a time. "
        "Fine for I-O bound work, bad for CPU-heavy math. "
        "Use threading dot Thread plus Lock for shared data. "
        "ProcessPoolExecutor for CPU parallelism; ThreadPoolExecutor for I-O."
    ),
    21: (
        "Slide 21: Context Manager. "
        "with open f as file auto-closes even on exception. "
        "Implement your own with at contextmanager decorator: yield between setup and teardown. "
        "double underscore enter and double underscore exit define the protocol. "
        "Used for files, locks, and database connections."
    ),
    22: (
        "Slide 22: Async and Await. "
        "asyncio runs concurrent I-O-bound tasks on one thread via an event loop. "
        "async def defines coroutines; await pauses until a result. "
        "asyncio dot gather runs multiple coroutines. "
        "FastAPI endpoints can be async def for non-blocking calls. "
        "Do not mix blocking calls in async code."
    ),
    23: (
        "Slide 23: Virtual Environment. "
        "python dash m venv dot venv then activate. "
        "pip install packages inside the venv only. "
        "pip freeze greater than requirements dot txt captures exact versions. "
        "Never install project libraries globally. "
        "pyenv manages multiple Python versions on one machine."
    ),
    24: (
        "Slide 24: Python-Set2 Portfolio Overview. "
        "Six real project areas: pythonBasics for core topics, "
        "google-python-exercises for regex and files, "
        "pandas for data analysis, Django and DRF for web APIs, "
        "and Pipecat for voice AI. "
        "You can demo any area on request in interviews."
    ),
    25: (
        "Slide 25: pythonBasics Topic Modules. "
        "Seven modules: MyClass, MyCollections, MyLoops, MyModules, "
        "MyExceptionHandling, MyDebug, and MyUnitTesting. "
        "Each has runnable scripts for one topic. "
        "Study theory in slides then practice in these folders."
    ),
    26: (
        "Slide 26: Google Exercises and Pandas. "
        "babynames teaches regex on HTML files. "
        "copyspecial covers os and shutil file operations. "
        "Titanic notebook shows read underscore csv, groupby, and missing value handling — "
        "like LINQ on in-memory tables."
    ),
    27: (
        "Slide 27: Django and Django REST. "
        "djangobasics slash meeting underscore planner shows MVT, templates, auth, and JWT API. "
        "DjangoRestBasics slash inventory is a multi-app DRF project with serializers and ViewSets. "
        "Django gives ORM, admin, and auth batteries-included."
    ),
    28: (
        "Slide 28: Pipecat Voice AI POCs. "
        "Voice pipeline is speech-to-text, then LLM, then text-to-speech over WebRTC. "
        "Built in phases: local services first, then Pipecat framework. "
        "voice-bouncer steps through greeting, member ID, and zip code — like an IVR system."
    ),
    29: (
        "Slide 29: Real Project Structure and Learning Path. "
        "Separate concerns: routes thin, services for business logic, "
        "schemas for validation, models for data, tests at project root. "
        "Django uses apps per domain; DRF adds serializers. "
        "Pipecat adds processors for streaming audio instead of JSON."
    ),
    30: (
        "Slide 30: C-sharp versus Python Quick Reference. "
        "Key shifts: no type declarations, indentation over braces, "
        "pass instead of empty curly braces, duck typing over interfaces. "
        "pass equals empty block; NotImplementedException equals NotImplementedError. "
        "None equals null — test with is None. "
        "self equals this but explicit. with equals using. "
        "venv plus pip equals NuGet per project."
    ),
}
