"""Plain-language primary descriptions for Python training slides 1–35.

Each description uses simple words, explains jargon when needed, and states
what the learner will take away. HTML emphasis is allowed.
"""

# slide number → short primary description (HTML allowed: <b>, <code>)
PRIMARY: dict[int, str] = {
    1: (
        "<b>Python</b> is a language for writing programs in <code>.py</code> files. "
        "You run them with the <code>python</code> command — no separate compile step like C#. "
        "Teams use it for automation, web apps, data work, testing, and AI. "
        "This slide shows what Python is and why the syntax is easy to read."
    ),
    2: (
        "Install Python 3 on Windows, check <code>python --version</code>, then run code. "
        "Three ways: the <b>REPL</b> (type one line at a time — like a scratchpad), "
        "a <code>.py</code> script (<code>python file.py</code>), or an IDE. "
        "This slide shows first-day setup and your first commands."
    ),
    3: (
        "Your course repo has three layers: slides (theory), <code>Projects/</code> (short practice), "
        "and <code>Python-Set2/</code> (real apps). Think of it as a labeled toolbox — "
        "each topic has a predictable place. "
        "This slide shows how to find and run the learning materials."
    ),
    4: (
        "<b>PEP</b> = <b>Python Enhancement Proposal</b> — official notes on Python design and style. "
        "PEP 8 is the naming/spacing guide; PEP 20 is the Zen of Python (<code>import this</code>). "
        "This slide shows how to write code others can read and maintain."
    ),
    5: (
        "A <b>datatype</b> tells Python what kind of value you store: "
        "<code>int</code>, <code>float</code>, <code>str</code>, <code>bool</code>, "
        "<code>list</code>, <code>tuple</code>, <code>set</code>, <code>dict</code>, or <code>None</code>. "
        "Pick the right container — list when it must grow, tuple when fixed, dict for key → value. "
        "This slide shows core types and when to use each."
    ),
    6: (
        "Type hints like <code>name: str</code> and <code>age: int</code> document what you expect. "
        "Python does <b>not</b> enforce them at run time by default — tools like mypy can check them for you. "
        "This slide shows hints on variables, parameters, returns, and common containers."
    ),
    7: (
        "Operators do math (<code>+</code>, <code>//</code>), compare (<code>==</code>, <code>!=</code>), "
        "combine conditions (<code>and</code>, <code>or</code>), and test membership (<code>in</code>) "
        "or identity (<code>is</code>). "
        "<code>==</code> asks “same value?”; <code>is</code> asks “same object in memory?” "
        "This slide shows which operator to use when."
    ),
    8: (
        "<code>if</code> / <code>elif</code> / <code>else</code> choose which code runs. "
        "<code>for</code> and <code>while</code> repeat work; <code>break</code> stops a loop, "
        "<code>continue</code> skips to the next round. "
        "This slide shows clear branches and loops."
    ),
    9: (
        "A <b>comprehension</b> builds a list, set, or dict in one line — "
        "for example <code>[x * x for x in range(5)]</code>. "
        "Add <code>if</code> to filter items. Use when readable; use a normal loop when clearer. "
        "This slide shows list, set, and dict comprehensions."
    ),
    10: (
        "A <b>function</b> is a named reusable block: pass arguments in, do work, "
        "optionally <code>return</code> a result. "
        "Defaults, <code>*args</code>, and <code>**kwargs</code> handle flexible calls. "
        "This slide shows how to write and call functions."
    ),
    11: (
        "Python ships ready-made <b>built-in</b> functions: <code>len</code>, <code>range</code>, "
        "<code>sum</code>, <code>sorted</code>, <code>enumerate</code>, <code>zip</code>, and more. "
        "Use them instead of rewriting the same logic. "
        "This slide covers the built-ins you will use most often."
    ),
    12: (
        "<b>Collections</b> hold groups of values: "
        "<code>list</code> (changeable), <code>tuple</code> (fixed), "
        "<code>set</code> (unique items), <code>dict</code> (key → value). "
        "The <code>collections</code> module adds helpers like <code>Counter</code> and <code>deque</code>. "
        "This slide shows how to pick and use the right collection."
    ),
    13: (
        "Python tracks how many names point to each object (<b>reference counting</b>). "
        "When nothing points to an object, memory can be freed. "
        "A <b>garbage collector</b> also handles circular references (A points to B, B points to A). "
        "This slide shows object lifetimes and how to avoid wasting memory."
    ),
    14: (
        "<b>Pydantic</b> checks incoming data against a model you define with type annotations. "
        "Wrong types or missing fields raise clear errors — like a checkpoint at an API door. "
        "FastAPI uses Pydantic to validate JSON bodies automatically. "
        "This slide shows models for settings and request data."
    ),
    15: (
        "<b>OOP</b> = <b>Object-Oriented Programming</b>: group data and behavior in <b>classes</b>, "
        "create <b>objects</b> from them. "
        "Inheritance reuses code; polymorphism lets different types respond the same way. "
        "This slide shows classes, objects, and when to use inheritance vs composition."
    ),
    16: (
        "A <b>descriptor</b> controls what happens when you read, write, or delete an attribute "
        "(<code>__get__</code>, <code>__set__</code>). "
        "It powers <code>@property</code> and similar patterns — a gatekeeper on an attribute. "
        "This slide shows how Python customizes attribute access."
    ),
    17: (
        "A <b>generator</b> gives one value at a time with <code>yield</code> — "
        "it does not store everything in memory first. "
        "<code>for</code> calls <code>iter()</code> and <code>next()</code> until done — "
        "same idea as <code>range(5)</code> (lazy) vs <code>list(range(5))</code> (all at once). "
        "This slide shows lazy iteration, generators, and generator expressions."
    ),
    18: (
        "A <b>decorator</b> adds extra steps <b>around</b> a function — like timing or logging — "
        "without you rewriting the function body. "
        "<code>@timer</code> above <code>def work():</code> is shorthand for "
        "<code>work = timer(work)</code>: <code>timer</code> receives <code>work</code>, "
        "returns a new function that still runs <code>work</code>, plus the extra behavior. "
        "This slide shows how to write decorators and keep the original function&apos;s name and docstring."
    ),
    19: (
        "<code>try</code> / <code>except</code> catches errors so your program can recover instead of crashing. "
        "<code>finally</code> always runs for cleanup; <code>raise</code> throws your own error. "
        "Catch specific errors — not every error with a bare <code>except:</code>. "
        "This slide shows safe exception handling."
    ),
    20: (
        "<b>Threading</b> and <b>processes</b> let programs overlap work. "
        "A <b>process</b> is one running app; a <b>thread</b> is a worker inside it. "
        "CPython's <b>GIL</b> limits Python bytecode to one thread per process — "
        "threads help I/O; <code>ProcessPoolExecutor</code> helps CPU. "
        "This slide builds from cores → process/thread → GIL → pools."
    ),
    21: (
        "<code>async</code> / <code>await</code> lets one thread juggle many waiting tasks (network, database) "
        "without blocking. "
        "Like a waiter serving other tables while food cooks — not the same as parallel CPU work. "
        "This slide shows coroutines, tasks, and the event loop."
    ),
    22: (
        "<b>Logging</b> writes messages with levels (DEBUG, INFO, WARNING, ERROR) to files or console — "
        "better than scattered <code>print</code> calls in production. "
        "You can filter by level and send logs to different destinations. "
        "This slide shows useful logging setup."
    ),
    23: (
        "A <b>unit test</b> checks one small piece of code automatically: set up inputs, run the code, "
        "assert the result matches. "
        "Fixtures prepare test data; mocks fake external dependencies. "
        "This slide shows <code>unittest</code> and mocking basics."
    ),
    24: (
        "A <b>regular expression</b> is a text pattern for find, split, or replace "
        "(<code>re.search</code>, <code>re.sub</code>). "
        "Powerful but easy to get wrong — start with simple patterns. "
        "This slide shows common <code>re</code> usage."
    ),
    25: (
        "File operations read and write data on disk with <code>open()</code>. "
        "Use text mode + <code>encoding=&quot;utf-8&quot;</code> for text files; "
        "always close the file (or use <code>with</code> so Python closes it for you). "
        "This slide shows safe read/write patterns."
    ),
    26: (
        "<code>with open(...) as f:</code> runs setup, your code, then cleanup automatically — "
        "even if an error happens. That is a <b>context manager</b>. "
        "You can write your own for locks, DB connections, and other resources. "
        "This slide shows <code>with</code> and how to create context managers."
    ),
    27: (
        "A <b>virtual environment</b> (<code>venv</code>) gives each project its own installed packages — "
        "so <code>pip install</code> in one project does not break another. "
        "Activate it, install deps, save versions in <code>requirements.txt</code>. "
        "This slide shows create, activate, and reproduce environments."
    ),
    28: (
        "<b>FastAPI</b> builds HTTP APIs with typed routes and automatic validation. "
        "<b>SQLAlchemy</b> talks to a relational database using Python objects. "
        "Together: request → validate → query DB → return JSON. "
        "This slide shows a safe request-to-database flow."
    ),
    29: (
        "The <b>Python-Set2 portfolio</b> is a folder of runnable projects — "
        "basics, Google exercises, Pandas, Django, voice AI POCs. "
        "Each module proves a skill beyond reading slides. "
        "This slide maps what is in the portfolio and where to start."
    ),
    30: (
        "The <b>pythonBasics</b> modules are small focused examples — "
        "<code>MyClass</code>, <code>MyCollections</code>, <code>MyLoops</code>, and more. "
        "One idea per folder you can run, change, and break safely. "
        "This slide maps each module to the topic it practices."
    ),
    31: (
        "<b>Google exercises</b> are coding puzzles for practice. "
        "<b>Pandas</b> loads and analyzes table-shaped data — a <code>DataFrame</code> is like a spreadsheet in code. "
        "This slide combines puzzle practice with real data manipulation."
    ),
    32: (
        "<b>Django</b> is a full web framework (models, views, admin, auth). "
        "<b>Django REST Framework</b> adds API endpoints with serializers and permissions. "
        "This slide shows how the layers fit together for a database-backed web app."
    ),
    33: (
        "<b>Pipecat</b> builds real-time voice AI pipelines: "
        "microphone → speech-to-text → language model → text-to-speech. "
        "This slide introduces the voice POC projects and what each piece does."
    ),
    34: (
        "A real project separates code, tests, config, and dependencies into clear folders — "
        "easier to test, maintain, and grow. "
        "This slide shows a practical layout and the path from exercises to production-style work."
    ),
    35: (
        "C# and Python solve similar problems with different syntax and runtimes. "
        "C# compiles for .NET; Python runs with an interpreter. "
        "<code>this</code> → <code>self</code>, <code>null</code> → <code>None</code>, braces → indentation. "
        "This slide is a quick map for developers coming from C#."
    ),
}


def primary_for(n: int) -> str:
    """Return the primary description for a slide number, or an empty string."""
    return PRIMARY.get(n, "")
