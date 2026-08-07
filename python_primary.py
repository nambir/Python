"""Plain-language primary descriptions for Python training slides 1–35.

Each description introduces the topic, gives practical context or an analogy,
and states the slide's main learning focus. HTML emphasis is allowed.
"""

# slide number → short primary description (HTML allowed: <b>, <code>)
PRIMARY: dict[int, str] = {
    1: (
        "<b>Python</b> is a high-level, general-purpose programming language designed to make "
        "code readable and productive. It is interpreted by a Python runtime and is widely used "
        "for automation, web applications, data work, testing, and artificial intelligence. "
        "This slide primarily focuses on what Python is, where it is used, and why its clear "
        "syntax makes it approachable."
    ),
    2: (
        "Setting up Python on Windows means installing a Python 3 interpreter, making the "
        "<code>python</code> command available, and choosing an editor or terminal in which to "
        "run code. The <b>REPL</b>, or <b>Read-Eval-Print Loop</b>, is like a scratchpad that "
        "runs one instruction at a time, while a <code>.py</code> file runs a saved program. "
        "This slide primarily focuses on installing Python correctly and running the first "
        "commands and scripts."
    ),
    3: (
        "A training workspace is the organized set of folders, source files, examples, and "
        "commands used throughout the course. Think of it as a labeled toolbox: each topic has "
        "a predictable place, so code is easy to find, run, and revisit. This slide primarily "
        "focuses on navigating the repository and using its learning materials consistently."
    ),
    4: (
        "<b>PEP</b> means <b>Python Enhancement Proposal</b>, a document that records a Python "
        "design, process, or community convention. For example, PEP 8 is the widely followed "
        "style guide, while PEP 20 summarizes the design philosophy known as the Zen of Python. "
        "This slide primarily focuses on writing consistent, readable Python by following the "
        "most relevant PEP guidance."
    ),
    5: (
        "Python datatypes describe the kinds of values a program can store and the operations "
        "those values support, such as numbers, strings, booleans, lists, tuples, sets, "
        "dictionaries, and <code>None</code>. A datatype is like a label on a container: it tells "
        "Python whether the contents can be added, searched, changed, or compared. This slide "
        "primarily focuses on choosing and using Python's core built-in types."
    ),
    6: (
        "Python typing uses annotations such as <code>name: str</code> and "
        "<code>list[int]</code> to describe the values code expects and returns. Python remains "
        "dynamically typed at runtime, but type checkers and editors can use these hints like "
        "road signs to catch mismatches earlier. This slide primarily focuses on readable type "
        "hints for variables, parameters, return values, and common containers."
    ),
    7: (
        "Operators are symbols or keywords that calculate values, compare data, combine "
        "conditions, assign results, or test membership and identity. Examples include "
        "<code>+</code>, <code>==</code>, <code>and</code>, <code>in</code>, and "
        "<code>is</code>; importantly, equality asks whether values match, while identity asks "
        "whether two names refer to the same object. This slide primarily focuses on selecting "
        "the correct arithmetic, comparison, logical, membership, and identity operators."
    ),
    8: (
        "Conditional and flow-control statements decide which instructions run and how often "
        "they repeat. <code>if</code>/<code>elif</code>/<code>else</code> act like route choices, "
        "while <code>for</code>, <code>while</code>, <code>break</code>, and "
        "<code>continue</code> control the journey through repeated work. This slide primarily "
        "focuses on expressing decisions and loops clearly without unnecessary complexity."
    ),
    9: (
        "A comprehension is a compact Python expression that builds a collection from an "
        "iterable, optionally transforming and filtering its items. It is similar to a small "
        "assembly line: take each item, keep it if a condition passes, and place the transformed "
        "result into a list, set, or dictionary. This slide primarily focuses on readable list, "
        "set, and dictionary comprehensions and when a normal loop is clearer."
    ),
    10: (
        "A Python function is a named, reusable block of behavior that can accept inputs and "
        "return a result. Functions are like small machines: arguments go in, local work happens, "
        "and a return value may come out; parameters, scope, defaults, and "
        "<code>*args</code>/<code>**kwargs</code> define how that machine is used. This slide "
        "primarily focuses on designing and calling clear, reusable functions."
    ),
    11: (
        "Built-in functions are ready-made operations supplied by Python, including "
        "<code>len</code>, <code>range</code>, <code>sum</code>, <code>sorted</code>, "
        "<code>enumerate</code>, and <code>zip</code>. They are standard tools already in the "
        "toolbox, so using them is usually clearer and safer than rebuilding the same behavior. "
        "This slide primarily focuses on the built-ins that simplify everyday iteration, "
        "conversion, inspection, and aggregation."
    ),
    12: (
        "Python collections store groups of values: a list is roughly a changeable row of seats, "
        "a tuple is a fixed row, a set keeps unique items, and a dictionary is a group of labeled "
        "boxes mapping keys to values. Each collection has different rules for order, mutation, "
        "duplicates, and lookup. This slide primarily focuses on choosing the right collection "
        "and using its common operations."
    ),
    13: (
        "Memory management is how Python creates, tracks, and releases objects while a program "
        "runs. CPython primarily uses reference counting and also has a cyclic garbage collector "
        "to reclaim groups of unreachable objects that refer to one another, much like clearing "
        "unused boxes even when they contain links to each other. This slide primarily focuses "
        "on object references, lifetimes, garbage collection, and avoiding needless memory use."
    ),
    14: (
        "<b>Pydantic</b> is a Python library that validates and converts data by using type "
        "annotations to define models. It acts like a checkpoint at a program boundary: incoming "
        "data is checked, normalized where appropriate, or rejected with structured validation "
        "errors. This slide primarily focuses on creating Pydantic models for dependable settings, "
        "request data, and serialized output."
    ),
    15: (
        "<b>OOP</b> means <b>Object-Oriented Programming</b>, an approach that groups data and "
        "behavior into objects created from classes. Encapsulation protects responsibilities, "
        "inheritance can reuse or specialize behavior, and polymorphism lets different objects "
        "respond through a common interface. This slide primarily focuses on applying classes, "
        "objects, composition, inheritance, and polymorphism appropriately in Python."
    ),
    16: (
        "A descriptor is an object that controls how an attribute is read, assigned, or deleted "
        "through methods such as <code>__get__</code>, <code>__set__</code>, and "
        "<code>__delete__</code>. It is like placing a gatekeeper in front of an attribute, and "
        "it powers familiar features such as methods and <code>property</code>. This slide "
        "primarily focuses on Python's attribute-access protocol and practical descriptor use."
    ),
    17: (
        "An iterator produces one item at a time through the iteration protocol, while a generator "
        "is a convenient way to create an iterator with <code>yield</code>. Like a ticket dispenser, "
        "it supplies the next value only when requested instead of preparing every value in memory "
        "up front. This slide primarily focuses on lazy iteration, <code>iter</code>, "
        "<code>next</code>, generator functions, and generator expressions."
    ),
    18: (
        "A decorator is a callable that wraps or replaces another function or class to add behavior "
        "without editing its core implementation. It is like placing a reusable security or logging "
        "checkpoint around many doors, and the <code>@name</code> syntax applies that wrapper "
        "clearly. This slide primarily focuses on writing decorators that preserve metadata and "
        "handle arguments correctly."
    ),
    19: (
        "Exception handling lets a program detect and respond to abnormal conditions without "
        "treating every failure as a crash. <code>try</code>, <code>except</code>, "
        "<code>else</code>, <code>finally</code>, and <code>raise</code> separate normal work "
        "from recovery and cleanup, like an emergency plan for expected failure modes. This slide "
        "primarily focuses on catching specific exceptions, preserving useful context, and avoiding "
        "silent error handling."
    ),
    20: (
        "Threading allows multiple threads of execution to make progress within one process, "
        "especially while work is waiting for input or output. The <b>GIL</b>, or "
        "<b>Global Interpreter Lock</b>, means that in standard CPython builds only one thread "
        "normally executes Python bytecode at a time, so threads do not usually speed up "
        "CPU-heavy Python code. This slide primarily focuses on thread-safe I/O concurrency, "
        "shared-state risks, and the practical effect of the GIL."
    ),
    21: (
        "<code>async</code>/<code>await</code> provide cooperative concurrency for tasks that "
        "spend time waiting on network, database, or file operations. The idea is like not holding "
        "a waiter at the kitchen while food cooks: an awaiting task yields control so the event "
        "loop can serve other work, but this does not automatically make CPU-heavy work parallel. "
        "This slide primarily focuses on coroutines, tasks, the event loop, and non-blocking I/O."
    ),
    22: (
        "Logging records structured information about what an application is doing and why a "
        "failure occurred. Unlike scattered <code>print</code> calls, Python's logging system "
        "supports severity levels, named loggers, formatting, handlers, and destinations, much "
        "like a searchable operational diary. This slide primarily focuses on useful log messages, "
        "appropriate levels, exception details, and safe configuration."
    ),
    23: (
        "Unit testing checks a small unit of behavior in isolation and reports whether its actual "
        "result matches the expected result. A test is like a repeatable quality inspection; "
        "fixtures arrange inputs, assertions verify outcomes, and mocks replace selected external "
        "collaborators when isolation is necessary. This slide primarily focuses on reliable tests, "
        "clear test cases, and sensible use of <code>unittest</code> and mocking."
    ),
    24: (
        "A regular expression is a pattern language for finding, validating, splitting, or replacing "
        "text. It behaves like a flexible text stencil, but metacharacters, groups, quantifiers, "
        "and escaping must be used carefully so the pattern says exactly what is intended. This "
        "slide primarily focuses on readable Python <code>re</code> patterns and common matching "
        "operations."
    ),
    25: (
        "File operations let a program create, read, write, append, and navigate persistent data "
        "on disk. Opening a file is like borrowing a resource from the operating system, so the "
        "program should choose the correct text or binary mode, encoding, and ensure the handle "
        "is closed. This slide primarily focuses on safe file access, paths, encodings, and common "
        "read/write patterns."
    ),
    26: (
        "A context manager defines setup and cleanup around a block used with the "
        "<code>with</code> statement. It works like checking out and automatically returning a "
        "shared resource, ensuring cleanup occurs even when an exception interrupts the block. "
        "This slide primarily focuses on using and creating context managers for files, locks, "
        "connections, and other managed resources."
    ),
    27: (
        "A virtual environment is an isolated Python installation context with its own packages "
        "and dependency versions. It is like giving each project a separate toolbox so installing "
        "a library for one project does not unexpectedly change another. This slide primarily "
        "focuses on creating, activating, using, and reproducing virtual environments."
    ),
    28: (
        "<b>FastAPI</b> is a Python web framework for building typed "
        "<b>APIs</b>—<b>Application Programming Interfaces</b>—and <b>SQLAlchemy</b> is a toolkit "
        "for working with relational databases through SQL expressions and object mappings. "
        "Together they connect validated HTTP requests to database operations, but sessions, "
        "transactions, dependencies, and response models still need clear boundaries. This slide "
        "primarily focuses on a safe request-to-database flow using FastAPI and SQLAlchemy."
    ),
    29: (
        "The <b>Python-Set2 portfolio</b> is a collection of small programs that demonstrates "
        "Python language skills through runnable examples. Think of it as a practical evidence "
        "folder: each module shows a concept being applied rather than only described. This slide "
        "primarily focuses on the portfolio's scope, organization, and demonstrated capabilities."
    ),
    30: (
        "The <b>pythonBasics topic modules</b> are focused examples covering language fundamentals "
        "such as collections, loops, classes, exceptions, modules, debugging, and testing. Each "
        "module is like a short lab that isolates one idea so it can be run, changed, and understood "
        "independently. This slide primarily focuses on mapping those modules to the foundational "
        "Python skills they practice."
    ),
    31: (
        "The Google exercises provide problem-solving practice, while <b>Pandas</b> is a Python "
        "library for loading, cleaning, transforming, and analyzing table-shaped data. A Pandas "
        "<code>DataFrame</code> is roughly a programmable spreadsheet table with labeled rows and "
        "columns. This slide primarily focuses on combining coding exercises with practical data "
        "manipulation skills."
    ),
    32: (
        "<b>Django</b> is a full-featured Python web framework, and <b>Django REST Framework</b> "
        "adds tools for building REST-style APIs—Application Programming Interfaces organized "
        "around HTTP resources and operations. Django supplies models, routing, views, templates, "
        "authentication, and administration, while the REST framework adds serializers, API views, "
        "permissions, and browsable endpoints. This slide primarily focuses on how these layers "
        "work together to build database-backed web applications and APIs."
    ),
    33: (
        "<b>Pipecat</b> is an open-source framework for building real-time voice and multimodal "
        "artificial-intelligence pipelines. Its pipeline is like a live conversation assembly line "
        "that can connect audio transport, speech recognition, a language model, and speech "
        "synthesis while handling events and interruptions. This slide primarily focuses on the "
        "voice AI proof-of-concepts and what their components demonstrate."
    ),
    34: (
        "A real Python project structure separates application code, tests, configuration, "
        "dependencies, documentation, and entry points by responsibility. Like organizing rooms "
        "in a workshop, clear boundaries make a project easier to test, maintain, package, and "
        "extend as learning moves from exercises to production work. This slide primarily focuses "
        "on a practical project layout and the next stages of the learning path."
    ),
    35: (
        "C# and Python are general-purpose languages with different defaults: C# is commonly "
        "statically typed and compiled for the .NET runtime, while Python is dynamically typed "
        "and commonly executed by an interpreter such as CPython. Similar ideas—variables, "
        "collections, classes, exceptions, asynchronous work, and APIs—use different syntax and "
        "runtime rules, so direct line-by-line translation can be misleading. This slide primarily "
        "focuses on quick conceptual equivalents and the differences developers must remember."
    ),
}


def primary_for(n: int) -> str:
    """Return the primary description for a slide number, or an empty string."""
    return PRIMARY.get(n, "")
