"""CSV curriculum map — Python Training 2026 Batch 2.

Slide numbers in deck vs CSV topic #:
  CSV 1  -> Slide 3  Python Datatypes
  CSV 2  -> Slide 5  Operators
  CSV 3  -> Slide 6  Conditional & Flow Control
  CSV 4  -> Slide 7  Comprehensions
  CSV 5  -> Slide 8  Python Functions
  CSV 6  -> Slide 9  Built-in Functions
  CSV 7  -> Slide 10 OOP Concepts
  CSV 8  -> Slide 11 Decorators
  CSV 9  -> Slide 12 Descriptors
  CSV 10 -> Slide 13 Generators & Iterators
  CSV 11 -> Slide 14 Typing
  CSV 12 -> Slide 15 File Operations
  CSV 13 -> Slide 16 Exception Handling
  CSV 14 -> Slide 17 Regular Expressions
  CSV 15 -> Slide 18 Python Collections
  CSV 16 -> Slide 19 Unit Testing
  CSV 17 -> Slide 20 Threading & GIL
  CSV 18 -> Slide 21 Context Manager
  CSV 19 -> Slide 22 Async / Await
  CSV 20 -> Slide 23 Virtual Environment

Slides 1-2 = intro/setup (not in CSV). Slide 4 = workspace. Slides 24-30 = projects appendix.
Slides 31-35 = extended curriculum (PEP, memory/GC, logging, Pydantic, FastAPI+SQLAlchemy).
"""

CSV_TOPICS: dict[int, list[str]] = {
    5: [
        "Primitive: int, float, str, bool",
        "List — mutability, indexing, slicing",
        "Tuple — immutability, packing/unpacking",
        "Dictionary — key-value, hashing",
        "Set — uniqueness, hashing",
        "Frozenset — immutable set, hashing, dict key",
    ],
    7: [
        "Arithmetic: + - * / % // **",
        "Comparison & logical operators",
        "Identity (is / is not) & membership (in / not in)",
        "Bitwise operators",
        "Assignment operators (+=, -=, *=, …)",
        "Walrus operator (:=)",
    ],
    8: [
        "if / elif / else",
        "for loop — iteration, range()",
        "while loop — condition, break, continue",
        "pass, else clause in loops",
    ],
    9: [
        "List comprehension",
        "Set comprehension",
        "Dictionary comprehension",
        "Generator expression",
    ],
    10: [
        "Positional & keyword arguments",
        "*args and **kwargs",
        "Recursion",
        "Anonymous / lambda functions",
        "Local and global scope (LEGB)",
        "Closures",
    ],
    11: [
        "map(), filter(), reduce()",
        "zip(), enumerate()",
        "type(), id(), isinstance()",
        "range(), len(), sorted(), reversed()",
        "max(), min()",
    ],
    15: [
        "Class & object, __init__, self",
        "Inheritance — single, multiple, MRO",
        "Encapsulation — private, protected (_)",
        "Polymorphism — method overriding",
        "Abstract classes (abc module)",
        "Dunder / magic methods",
    ],
    18: [
        "Function decorators",
        "Class decorators",
        "functools.wraps",
    ],
    16: [
        "__get__, __set__, __delete__",
        "Property vs descriptor",
    ],
    17: [
        "Generator functions (yield)",
        "Generator state / frame internals",
        "Iterator protocol (__iter__, __next__)",
        "itertools module",
    ],
    6: [
        "Type hints — basic annotations",
        "Optional, Union, List, Dict, Tuple",
        "TypeVar, Generic, Protocol",
        "mypy for static checking",
    ],
    25: [
        "open() — read, write, append modes",
        "Context manager with 'with'",
        "CSV, JSON file handling",
        "pathlib module",
    ],
    19: [
        "try / except / else / finally",
        "Built-in exceptions hierarchy",
        "Custom exceptions",
        "Raising and re-raising exceptions",
    ],
    24: [
        "re module — match, search, findall",
        "Groups, special sequences",
        "Lookahead / lookbehind",
    ],
    12: [
        "Counter",
        "OrderedDict",
        "defaultdict",
        "ChainMap",
        "namedtuple",
        "deque",
        "UserDict, UserList, UserString",
    ],
    23: [
        "unittest — TestCase, setUp, tearDown",
        "Order of execution in unit tests",
        "assert methods",
        "Mocking — unittest.mock",
        "pytest basics",
    ],
    20: [
        "threading — Thread, Lock",
        "Python GIL — what and why",
        "multiprocessing as GIL workaround",
        "concurrent.futures",
    ],
    26: [
        "contextlib.contextmanager",
        "__enter__ / __exit__ protocol",
    ],
    21: [
        "asyncio — event loop basics",
        "async def, await, coroutines",
        "asyncio.gather(), asyncio.run()",
        "async context managers & iterators",
    ],
    27: [
        "venv — create, activate, deactivate",
        "pip — install, freeze, requirements.txt",
        "pyenv for Python version management",
    ],
    4: [
        "PEP 8 — style guide (naming, indent, imports)",
        "PEP 257 — docstring conventions",
        "PEP 20 — Zen of Python",
        "PEP 440 / 508 / 621 — versions, deps, pyproject.toml",
    ],
    13: [
        "Reference counting",
        "Garbage collector — circular references",
        "Generational GC (0, 1, 2)",
        "weakref, del, profiling leaks",
    ],
    22: [
        "logging module — levels, loggers, handlers",
        "basicConfig vs module loggers",
        "RotatingFileHandler",
        "logger.exception / exc_info",
    ],
    14: [
        "Pydantic BaseModel",
        "Field constraints & field_validator",
        "model_validate / model_dump (v2)",
        "FastAPI request/response schemas",
    ],
    28: [
        "FastAPI routes & Depends",
        "SQLAlchemy ORM models & Session",
        "Pydantic vs ORM separation",
        "Service layer & session-per-request",
    ],
}
