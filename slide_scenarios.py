"""When-to-use-which scenario tables for every slide."""

SCENARIOS: dict[int, str] = {
    1: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Choose</th><th>Why</th></tr>
<tr><td>Quick scripts, automation, data analysis</td><td><b>Python</b></td><td>Fast to write, rich libraries, no compile step</td></tr>
<tr><td>Hard real-time, OS drivers, max CPU speed</td><td><b>C / C++ / Rust</b></td><td>Compiled to native machine code</td></tr>
<tr><td>Enterprise web on .NET stack</td><td><b>C#</b></td><td>Static typing, Visual Studio, ASP.NET ecosystem</td></tr>
<tr><td>Prototyping ML / AI pipelines</td><td><b>Python</b></td><td>NumPy, pandas, PyTorch, Jupyter</td></tr>
<tr><td>Mobile iOS native app</td><td><b>Swift</b></td><td>Python not primary for iOS UI</td></tr>
<tr><td>Config files, glue between systems</td><td><b>Python</b></td><td>Readable, batteries included, easy subprocess</td></tr>
</table>
<div class="callout"><b>Rule of thumb:</b> Python wins when <b>developer speed</b> and <b>library breadth</b> matter more than raw runtime performance.</div>""",
    2: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Try one line, explore an API</td><td><b>REPL</b></td><td>Instant feedback — type <code>python</code>, experiment</td></tr>
<tr><td>Check Python and package installer setup</td><td><b>python --version + pip --version</b></td><td><code>python</code> shows interpreter version; <code>pip</code> shows installer version and linked Python path</td></tr>
<tr><td>Run a complete program repeatedly</td><td><b>Script</b></td><td><code>python app.py</code> — reproducible, shareable</td></tr>
<tr><td>Debug with breakpoints, step through</td><td><b>Cursor / VS Code (F5)</b></td><td>Daily choice: Cursor or VS Code. Other famous options: PyCharm, Jupyter Notebook/Lab, Spyder, Visual Studio, IDLE.</td></tr>
<tr><td>One-off command in CI/CD pipeline</td><td><b>python -c</b></td><td>Inline without creating a file</td></tr>
<tr><td>Multiple Python versions on one PC</td><td><b>py launcher</b></td><td><code>py -3.12 script.py</code> picks version</td></tr>
<tr><td>Library imported by other modules</td><td><b>Module + __main__ guard</b></td><td>Runnable directly OR importable safely</td></tr>
<tr><td>Avoid NameError for your own functions</td><td><b>defs first, main last</b></td><td>Define <code>Add</code> above; call it inside <code>if __name__ == "__main__":</code> at bottom — unlike C# class method order</td></tr>
</table>""",
    5: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>GPS coordinate, RGB color, employee record</td><td><b>tuple</b></td><td>Fixed fields — should not change accidentally</td></tr>
<tr><td>API returns success + payload</td><td><b>tuple</b> <code>(ok, data)</code></td><td>Caller unpacks; clear contract</td></tr>
<tr><td>Composite cache / grid key</td><td><b>tuple</b></td><td>Hashable — list as key raises TypeError</td></tr>
<tr><td>Need slightly less memory / fixed iteration</td><td><b>tuple</b></td><td>No over-allocation or resize bookkeeping</td></tr>
<tr><td>Shopping cart, todo list, log lines</td><td><b>list</b></td><td>append, pop, sort — size changes</td></tr>
<tr><td>Mix int + status + nested vendors</td><td><b>heterogeneous list</b></td><td><code>[101, "SHIPPED", ["Google","Amazon"]]</code></td></tr>
<tr><td>Watch list capacity grow</td><td><b>sys.getsizeof</b> while appending</td><td>See over-allocation jumps</td></tr>
<tr><td>Lookup by unique key</td><td><b>dict</b></td><td>O(1) key-value access</td></tr>
<tr><td>Remove duplicates / membership</td><td><b>set</b></td><td>Only unique items kept</td></tr>
<tr><td>Immutable set as dict key</td><td><b>frozenset</b></td><td>Like set but hashable</td></tr>
</table>
<div class="callout"><b>Rule of thumb:</b> Fixed length + fixed meaning → <b>tuple</b>. Growing / mixed working data → <b>list</b>.</div>""",
    3: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Learn one concept in 10 minutes</td><td><b>Projects/</b></td><td>Single file per slide — quick run</td></tr>
<tr><td>Build a real app with many files</td><td><b>Python-Set2/</b></td><td>Django, DRF, pandas, Pipecat projects</td></tr>
<tr><td>Review theory before interview</td><td><b>PythonTraining.html</b></td><td>Definitions, terms, code side-by-side</td></tr>
<tr><td>Regenerate slides after edits</td><td><b>build_training.py</b></td><td>Source of truth for HTML deck</td></tr>
<tr><td>Isolated dependencies per project</td><td><b>.venv/ per folder</b></td><td>Avoid global pip conflicts</td></tr>
</table>""",
    7: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Division needing decimal result</td><td><b>/</b></td><td>Always float in Python 3: <code>7/2 → 3.5</code></td></tr>
<tr><td>Division needing whole pages/buckets</td><td><b>//</b></td><td>Floor division: <code>7//2 → 3</code></td></tr>
<tr><td>Check if value is in a collection</td><td><b>in</b></td><td><code>5 in [1,5,9]</code> — membership</td></tr>
<tr><td>Check if two names point to same object</td><td><b>is</b></td><td>Identity — use <code>is None</code>, never <code>== None</code></td></tr>
<tr><td>Check if two lists have same contents</td><td><b>==</b></td><td>Value equality — different objects OK</td></tr>
<tr><td>Combine permission flags in binary</td><td><b>bitwise &amp; | ^</b></td><td>Low-level flags on integers</td></tr>
<tr><td>Logical AND across conditions</td><td><b>and</b></td><td>Both must be True</td></tr>
</table>""",
    8: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>2–3 distinct branches (grade, status)</td><td><b>if / elif / else</b></td><td>Clear mutually exclusive paths</td></tr>
<tr><td>Loop over known collection</td><td><b>for</b></td><td>Like C# foreach — <code>for x in items</code></td></tr>
<tr><td>Loop until condition becomes false</td><td><b>while</b></td><td>Read until EOF, retry until success</td></tr>
<tr><td>Skip one iteration, continue loop</td><td><b>continue</b></td><td>Skip invalid rows in a file</td></tr>
<tr><td>Exit loop early when found</td><td><b>break</b></td><td>Search — stop when match found</td></tr>
<tr><td>Empty block placeholder (stub)</td><td><b>pass</b></td><td>Python requires a body after <code>if</code>/<code>def</code>/<code>class</code></td></tr>
<tr><td>Stub function — empty for now, code added later</td><td><b>pass</b></td><td>Block intentionally empty — remove pass when implemented</td></tr>
<tr><td>Empty custom exception class</td><td><b>class E(Exception): pass</b></td><td>Valid empty body — type exists for <code>raise</code> / <code>except</code></td></tr>
<tr><td>Ignore one known error (rare)</td><td><b>except ValueError: pass</b></td><td>Specific type only — still prefer log / handle</td></tr>
<tr><td>&#10060; Swallow everything</td><td><b>except: pass</b></td><td><b>Bug</b> — catches <code>BaseException</code> (Ctrl+C / exit) and hides all errors</td></tr>
<tr><td>Temporarily disable code without deleting</td><td><b>if False:</b></td><td>Block never runs — easy to turn back on</td></tr>
<tr><td>Learning / TODO block (remove later)</td><td><b>if True: pass</b></td><td>Placeholder only — not for production</td></tr>
<tr><td>Search list, report if not found</td><td><b>for-else</b></td><td><code>else</code> runs only if no <code>break</code></td></tr>
<tr><td>Fixed count (0 to N-1)</td><td><b>range(N)</b></td><td><code>for i in range(10)</code></td></tr>
</table>""",
    9: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Build list from transform + filter</td><td><b>list comprehension</b></td><td>Readable one-liner vs loop+append</td></tr>
<tr><td>Build unique values from iterable</td><td><b>set comprehension</b></td><td>Automatic deduplication</td></tr>
<tr><td>Build dict from two lists</td><td><b>dict comprehension</b></td><td><code>{k:v for k,v in pairs}</code></td></tr>
<tr><td>Huge dataset — only need one at a time</td><td><b>generator expression</b></td><td>Lazy — no full list in memory</td></tr>
<tr><td>Side effects in loop (print, DB write)</td><td><b>plain for loop</b></td><td>Comprehensions should not have side effects</td></tr>
<tr><td>Complex nested logic hard to read</td><td><b>plain for loop</b></td><td>Readability over cleverness</td></tr>
</table>""",
    10: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Logic with no side effects / easy to test</td><td><b>pure function</b></td><td>Same inputs → same output (FP)</td></tr>
<tr><td>Pass/return functions (sorted key, factory)</td><td><b>higher-order / first-class</b></td><td><code>sorted(..., key=fn)</code></td></tr>
<tr><td>Reusable logic with a name</td><td><b>def function</b></td><td>DRY — call from many places</td></tr>
<tr><td>Optional parameter with default</td><td><b>default arg</b></td><td><code>greet(name, msg="Hi")</code></td></tr>
<tr><td>Unknown number of positional args</td><td><b>*args</b></td><td>Wrapper functions, decorators</td></tr>
<tr><td>Unknown keyword options</td><td><b>**kwargs</b></td><td>Forwarding to another API</td></tr>
<tr><td>One-line throwaway transform</td><td><b>lambda</b></td><td><code>sorted(items, key=lambda x: x[1])</code></td></tr>
<tr><td>Function remembering state between calls</td><td><b>closure</b></td><td>Counter, cache, factory pattern</td></tr>
<tr><td>Tree/graph recursion (factorial, folders)</td><td><b>recursion</b></td><td>Problem defined in terms of itself</td></tr>
<tr><td>Default mutable list argument</td><td><b>None trick</b></td><td><code>def f(lst=None)</code> — never <code>lst=[]</code></td></tr>
</table>""",
    11: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Transform every item same way</td><td><b>map</b> or list comp</td><td><code>[x*2 for x in nums]</code> more Pythonic</td></tr>
<tr><td>Keep items matching condition</td><td><b>filter</b> or list comp</td><td><code>[x for x in nums if x&gt;0]</code></td></tr>
<tr><td>Fold list to single value (sum, product)</td><td><b>reduce</b></td><td><code>reduce(add, nums)</code></td></tr>
<tr><td>Pair two lists into tuples/dict</td><td><b>zip</b></td><td><code>dict(zip(keys, vals))</code></td></tr>
<tr><td>Need index while looping</td><td><b>enumerate</b></td><td><code>for i, v in enumerate(items)</code></td></tr>
<tr><td>Sort without mutating original</td><td><b>sorted()</b></td><td>Returns new list — original unchanged</td></tr>
<tr><td>Sort list in place</td><td><b>list.sort()</b></td><td>Mutates the list — no copy</td></tr>
<tr><td>Check type with inheritance</td><td><b>isinstance</b></td><td>Better than <code>type(x)==int</code></td></tr>
</table>""",
    15: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Model real entity (User, Order, Dog)</td><td><b>class</b></td><td>Bundle data + behavior</td></tr>
<tr><td>Shared behavior, different implementations</td><td><b>inheritance + override</b></td><td>Dog/Cat both <code>speak()</code></td></tr>
<tr><td>Hide internal state, expose read-only</td><td><b>@property</b></td><td><code>balance</code> getter without direct access</td></tr>
<tr><td>Mark "don't touch" internal field</td><td><b>_underscore</b></td><td>Convention for protected (not enforced)</td></tr>
<tr><td>Force child to implement method</td><td><b>ABC + @abstractmethod</b></td><td>Interface-like contract</td></tr>
<tr><td>User-friendly print vs debug repr</td><td><b>__str__ / __repr__</b></td><td><code>print(obj)</code> vs REPL display</td></tr>
<tr><td>Multiple inheritance diamond problem</td><td><b>MRO</b></td><td>Check <code>Class.__mro__</code> for order</td></tr>
</table>""",
    18: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Add logging/timing without changing function body</td><td><b>decorator</b></td><td>Cross-cutting concern — wrap any function</td></tr>
<tr><td>Register HTTP route (FastAPI/Flask)</td><td><b>@app.get()</b></td><td>Framework uses decorators for routing</td></tr>
<tr><td>Enforce auth before handler runs</td><td><b>@login_required</b></td><td>Decorator checks then calls original</td></tr>
<tr><td>Cache expensive function results</td><td><b>@lru_cache</b></td><td>Built-in functools decorator</td></tr>
<tr><td>Stack multiple behaviors</td><td><b>nested decorators</b></td><td><code>@a @b def f</code> — order matters</td></tr>
<tr><td>Decorator needs configuration</td><td><b>decorator factory</b></td><td><code>@repeat(3)</code> — extra wrapper level</td></tr>
</table>""",
    16: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Validate value on assignment</td><td><b>@property setter</b></td><td>Reject negative temperature, age</td></tr>
<tr><td>Computed read-only field (area, full name)</td><td><b>@property</b> only</td><td>No setter — derived from other fields</td></tr>
<tr><td>Custom get/set/delete on attribute</td><td><b>descriptor class</b></td><td>Advanced — <code>__get__</code>, <code>__set__</code></td></tr>
<tr><td>Simple field with validation</td><td><b>@property</b></td><td>Prefer over full descriptor — less boilerplate</td></tr>
<tr><td>ORM field lazy-loading from DB</td><td><b>descriptor</b></td><td>Framework-level attribute control</td></tr>
</table>""",
    17: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Huge CSV — avoid MemoryError</td><td><b>yield one row</b></td><td>Not <code>read().split()</code> into a giant list (Real Python)</td></tr>
<tr><td>Read huge file line by line</td><td><b>generator (yield)</b></td><td>One line in memory at a time</td></tr>
<tr><td>Infinite sequence (counters, streams)</td><td><b>generator</b></td><td>Never materialize full list</td></tr>
<tr><td>Short lazy transform</td><td><b>generator expression</b></td><td><code>(parse(l) for l in f)</code></td></tr>
<tr><td>Pipeline of transformations</td><td><b>chained generators / itertools</b></td><td>No giant intermediate lists</td></tr>
<tr><td>Need random access by index</td><td><b>list</b></td><td>Generators are one-pass — no <code>gen[5]</code></td></tr>
<tr><td>Need len() or reuse multiple times</td><td><b>list</b></td><td>Generators consumed once</td></tr>
</table>""",
    6: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Document API for teammates/IDE</td><td><b>type hints</b></td><td>Autocomplete, readability — no runtime cost</td></tr>
<tr><td>Catch type bugs before deploy</td><td><b>mypy</b></td><td>Static analysis in CI</td></tr>
<tr><td>Value can be missing</td><td><b>Optional[T]</b></td><td><code>Optional[str]</code> = str or None</td></tr>
<tr><td>Accept int or str input</td><td><b>Union[int, str]</b></td><td>Document allowed alternatives</td></tr>
<tr><td>FastAPI / Pydantic validation</td><td><b>type hints</b></td><td>Framework enforces at request time</td></tr>
<tr><td>Quick throwaway script</td><td><b>skip hints</b></td><td>OK for learning — add in production code</td></tr>
</table>""",
    25: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Read/write text config, logs</td><td><b>open() + with</b></td><td>Auto-close; always set <code>encoding=utf-8</code></td></tr>
<tr><td>API data, config as structured JSON</td><td><b>json module</b></td><td><code>loads</code>/<code>dumps</code> between str and dict</td></tr>
<tr><td>Build paths across OS (Windows/Linux)</td><td><b>pathlib.Path</b></td><td><code>Path("a")/"b"</code> — cleaner than os.path</td></tr>
<tr><td>Tabular data export (Excel interop)</td><td><b>csv module</b></td><td>Row-by-row read/write</td></tr>
<tr><td>Binary files (images, PDF)</td><td><b>open("rb"/"wb")</b></td><td>Bytes mode — not text decoding</td></tr>
<tr><td>Always close file even on crash</td><td><b>with statement</b></td><td>Context manager guarantees cleanup</td></tr>
</table>""",
    19: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Expected failure (bad user input)</td><td><b>try/except ValueError</b></td><td>Catch specific type — not bare <code>except:</code></td></tr>
<tr><td>Cleanup must run (close file, release lock)</td><td><b>finally</b> or <code>with</code></td><td>Runs even if exception raised</td></tr>
<tr><td>Business rule violation</td><td><b>custom exception</b></td><td><code>raise ValidationError("...")</code></td></tr>
<tr><td>Re-raise after logging</td><td><b>raise</b> (bare)</td><td>Preserves original traceback</td></tr>
<tr><td>Expected success path logging</td><td><b>try/else</b></td><td><code>else</code> only when no exception</td></tr>
<tr><td>Let crash for programming bugs</td><td><b>don't catch</b></td><td>KeyError, AttributeError = fix the code</td></tr>
</table>""",
    24: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Extract emails, phone numbers from text</td><td><b>re.findall</b></td><td>Pattern match across string</td></tr>
<tr><td>Validate format (date, postal code)</td><td><b>re.match + groups</b></td><td>Full match at start with capture groups</td></tr>
<tr><td>Replace/mask sensitive data in logs</td><td><b>re.sub</b></td><td>Redact digits, emails</td></tr>
<tr><td>Simple substring check</td><td><b>in operator</b></td><td>Faster/simpler — no regex needed</td></tr>
<tr><td>Parse structured file (CSV, JSON)</td><td><b>csv/json modules</b></td><td>Don't regex what has a proper parser</td></tr>
<tr><td>Complex nested HTML</td><td><b>BeautifulSoup</b></td><td>Regex on HTML breaks — use HTML parser</td></tr>
</table>""",
    12: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Count word/char frequency</td><td><b>Counter</b></td><td>One line vs manual dict counting</td></tr>
<tr><td>Group items by category</td><td><b>defaultdict(list)</b></td><td>Auto-creates empty list for new key</td></tr>
<tr><td>Queue with fast push/pop both ends</td><td><b>deque</b></td><td>O(1) appendleft — list is O(n) at front</td></tr>
<tr><td>Lightweight record (x, y) with names</td><td><b>namedtuple</b></td><td>Lighter than full class for data-only</td></tr>
<tr><td>Merge config: env + file + defaults</td><td><b>ChainMap</b></td><td>Search dicts in order</td></tr>
<tr><td>Need to mutate grouped data</td><td><b>defaultdict</b></td><td>Counter is for counting only</td></tr>
</table>""",
    23: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Quick project tests, simple asserts</td><td><b>pytest</b></td><td>Less boilerplate — plain <code>assert</code></td></tr>
<tr><td>Enterprise setup/teardown suites</td><td><b>unittest.TestCase</b></td><td>setUp/tearDown per test method</td></tr>
<tr><td>Mock external API or database</td><td><b>unittest.mock.patch</b></td><td>Isolate unit under test</td></tr>
<tr><td>Test one behavior per test</td><td><b>single assert focus</b></td><td>Easier to find what broke</td></tr>
<tr><td>Integration test (real DB)</td><td><b>pytest + fixtures</b></td><td>Separate from fast unit tests</td></tr>
<tr><td>Run all tests in CI</td><td><b>pytest -v</b></td><td>Discover and run test_*.py automatically</td></tr>
</table>""",
    20: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Many HTTP requests, file downloads</td><td><b>threading / ThreadPool</b></td><td>I/O-bound — GIL released during wait</td></tr>
<tr><td>Heavy math, image processing, ML training</td><td><b>multiprocessing</b></td><td>CPU-bound — bypass GIL with separate processes</td></tr>
<tr><td>Shared counter without race condition</td><td><b>threading.Lock</b></td><td>Mutex around critical section</td></tr>
<tr><td>Simple parallel I/O tasks</td><td><b>ThreadPoolExecutor</b></td><td>Pool manages thread lifecycle</td></tr>
<tr><td>Parallel CPU on all cores</td><td><b>ProcessPoolExecutor</b></td><td>True parallelism — separate memory</td></tr>
<tr><td>Async HTTP (thousands of connections)</td><td><b>asyncio</b></td><td>Even better than threads for I/O scale</td></tr>
</table>""",
    26: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Open file and guarantee close</td><td><b>with open()</b></td><td>Built-in context manager</td></tr>
<tr><td>Acquire lock, auto-release</td><td><b>with lock:</b></td><td>Lock is a context manager</td></tr>
<tr><td>DB connection commit/rollback</td><td><b>with connection:</b></td><td>Transaction boundary</td></tr>
<tr><td>Quick custom setup/teardown</td><td><b>@contextmanager</b></td><td>Generator with yield — less code than class</td></tr>
<tr><td>Reusable resource class (pool, session)</td><td><b>__enter__/__exit__ class</b></td><td>Full control over lifecycle</td></tr>
<tr><td>Manual try/finally everywhere</td><td><b>avoid — use with</b></td><td>with is cleaner and safer</td></tr>
</table>""",
    21: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Thousands of concurrent HTTP/API calls</td><td><b>asyncio</b></td><td>Single thread, non-blocking I/O</td></tr>
<tr><td>Sequential awaits (each depends on prior)</td><td><b>await one by one</b></td><td>When step 2 needs result of step 1</td></tr>
<tr><td>Independent I/O tasks in parallel</td><td><b>asyncio.gather</b></td><td>All run concurrently — ~1x slowest</td></tr>
<tr><td>CPU-heavy image resize loop</td><td><b>multiprocessing</b></td><td>async does NOT help CPU-bound work</td></tr>
<tr><td>FastAPI endpoint calling DB + HTTP</td><td><b>async def route</b></td><td>Non-blocking while waiting</td></tr>
<tr><td>Simple script with one request</td><td><b>sync requests</b></td><td>async overhead not worth it</td></tr>
</table>""",
    27: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Scenario</th><th>Use</th><th>Why</th></tr>
<tr><td>Every project with dependencies</td><td><b>venv per project</b></td><td>Isolate packages — no global conflicts</td></tr>
<tr><td>Share exact versions with team/CI</td><td><b>requirements.txt</b></td><td><code>pip freeze</code> pins versions</td></tr>
<tr><td>Install from requirements on new machine</td><td><b>pip install -r</b></td><td>Reproducible environment</td></tr>
<tr><td>Multiple Python versions on one laptop</td><td><b>pyenv</b></td><td>Switch 3.10 vs 3.12 per project</td></tr>
<tr><td>Commit venv folder to git</td><td><b>never</b></td><td>Add <code>.venv/</code> to .gitignore</td></tr>
<tr><td>Global pip install for everything</td><td><b>avoid</b></td><td>Project A breaks Project B</td></tr>
</table>""",
    29: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Goal</th><th>Start here</th><th>Why</th></tr>
<tr><td>Learn OOP, loops, collections</td><td><b>pythonBasics/</b></td><td>Small focused modules per topic</td></tr>
<tr><td>Practice regex and file parsing</td><td><b>google-python-exercises/</b></td><td>babynames, copyspecial puzzles</td></tr>
<tr><td>Data analysis interview prep</td><td><b>pandas/</b></td><td>Titanic/FIFA notebooks — groupby, filter</td></tr>
<tr><td>Full-stack web demo</td><td><b>djangobasics/</b></td><td>MVT, ORM, templates, auth</td></tr>
<tr><td>REST API demo</td><td><b>DjangoRestBasics/</b></td><td>Serializers, ViewSets, JSON</td></tr>
<tr><td>Voice AI / async interview story</td><td><b>Pipecat-Project/</b></td><td>STT → LLM → TTS pipeline</td></tr>
</table>""",
    30: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Topic to practice</th><th>Module</th><th>Why</th></tr>
<tr><td>OOP, inheritance, BankAccount</td><td><b>MyClass/</b></td><td>Real class hierarchies</td></tr>
<tr><td>list, dict, set, tuple drills</td><td><b>MyCollections/</b></td><td>Matches slide 3 datatypes</td></tr>
<tr><td>for, while, range, enumerate</td><td><b>MyLoops/</b></td><td>Matches slide 6 flow control</td></tr>
<tr><td>import, packages, __name__</td><td><b>MyModules/</b></td><td>How Python finds code</td></tr>
<tr><td>try/except, raise custom errors</td><td><b>MyExceptionHandling/</b></td><td>Matches slide 16</td></tr>
<tr><td>pytest, unittest patterns</td><td><b>MyUnitTesting/</b></td><td>Matches slide 19</td></tr>
</table>""",
    31: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Task</th><th>Tool</th><th>Why</th></tr>
<tr><td>Parse text file with regex patterns</td><td><b>babynames/</b></td><td>Classic interview regex exercise</td></tr>
<tr><td>Copy files by extension/metadata</td><td><b>copyspecial/</b></td><td>os, shutil — file system skills</td></tr>
<tr><td>Explore CSV data interactively</td><td><b>pandas + Jupyter</b></td><td>DataFrame, head(), describe()</td></tr>
<tr><td>Group passengers by class, get avg age</td><td><b>groupby</b></td><td>Titanic notebook pattern</td></tr>
<tr><td>Sort players by goals scored</td><td><b>FIFA notebook</b></td><td>sort_values, aggregation</td></tr>
<tr><td>Production ETL pipeline</td><td><b>pandas script</b></td><td>Notebook for explore, .py for automate</td></tr>
</table>""",
    32: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Need</th><th>Choose</th><th>Why</th></tr>
<tr><td>Admin UI, templates, ORM, auth built-in</td><td><b>Django</b></td><td>Batteries-included web framework</td></tr>
<tr><td>JSON API only — no HTML pages</td><td><b>Django REST Framework</b></td><td>Serializers + ViewSets on top of Django</td></tr>
<tr><td>Lightweight API, async, type hints</td><td><b>FastAPI</b></td><td>Alternative — not in Set2 but common in interviews</td></tr>
<tr><td>Define database tables as classes</td><td><b>Django models.py</b></td><td>ORM migrations handle schema</td></tr>
<tr><td>Validate request/response JSON shape</td><td><b>DRF Serializer</b></td><td>Like Pydantic — to/from JSON</td></tr>
<tr><td>Stateless mobile app authentication</td><td><b>JWT (simplejwt)</b></td><td>Token-based — no server session</td></tr>
</table>""",
    33: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Use case</th><th>POC</th><th>Why</th></tr>
<tr><td>Learn Pipecat cloud pipeline basics</td><td><b>pipecat-quickstart</b></td><td>Official minimal example</td></tr>
<tr><td>Local STT/LLM/TTS without cloud</td><td><b>pipecat-voice-phase1</b></td><td>All services on your machine</td></tr>
<tr><td>Full production-style pipeline</td><td><b>pipecat-voice-phase2</b></td><td>Steps 1–8 end-to-end</td></tr>
<tr><td>IVR-style voice authentication demo</td><td><b>voice-bouncer</b></td><td>Member ID, zip code flow</td></tr>
<tr><td>Study architecture before coding</td><td><b>PipecatAI.html</b></td><td>Learning content in repo</td></tr>
<tr><td>CPU-heavy local LLM inference</td><td><b>phase1 local models</b></td><td>Avoid cloud API costs in dev</td></tr>
</table>""",
    34: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Project type</th><th>Structure</th><th>Why</th></tr>
<tr><td>FastAPI / Flask REST API</td><td><b>routes + services + schemas</b></td><td>Thin handlers, logic in services</td></tr>
<tr><td>Django web app</td><td><b>apps per domain</b></td><td>meeting/, myauth/ — Django convention</td></tr>
<tr><td>DRF JSON API</td><td><b>models + serializers + viewsets</b></td><td>DRF layered pattern</td></tr>
<tr><td>Voice AI pipeline</td><td><b>processors chain</b></td><td>Pipecat — audio in → audio out</td></tr>
<tr><td>Week 1–2 learning</td><td><b>Projects/ + slides 1–10</b></td><td>Fundamentals before big projects</td></tr>
<tr><td>Interview demo ready</td><td><b>one Set2 project deep</b></td><td>Depth beats breadth — know one well</td></tr>
</table>""",
    35: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Situation</th><th>Python approach</th><th>C# equivalent</th></tr>
<tr><td>Declare a variable</td><td><code>x = 5</code> — no type keyword</td><td><code>int x = 5;</code></td></tr>
<tr><td>Empty stub method</td><td><code>def save(): pass</code></td><td><code>void Save() { }</code></td></tr>
<tr><td>Not implemented yet</td><td><code>raise NotImplementedError()</code></td><td><code>throw new NotImplementedException()</code></td></tr>
<tr><td>Check for null</td><td><code>if x is None:</code></td><td><code>if (x == null)</code></td></tr>
<tr><td>Current instance</td><td><code>self.name</code> in <code>def f(self):</code></td><td><code>this.Name</code> in instance method</td></tr>
<tr><td>Auto-close file</td><td><code>with open(...) as f:</code></td><td><code>using (var f = ...)</code></td></tr>
<tr><td>Loop a collection</td><td><code>for i in list:</code></td><td><code>foreach (var i in list)</code></td></tr>
<tr><td>Handle errors</td><td><code>try: ... except Ex:</code></td><td><code>try { } catch (Ex)</code></td></tr>
<tr><td>Install a library</td><td><code>pip install pkg</code></td><td><code>dotnet add package</code></td></tr>
<tr><td>Async HTTP call</td><td><code>async def</code> + <code>await</code></td><td><code>async Task</code> + <code>await</code></td></tr>
<tr><td>Define interface contract</td><td>ABC or duck typing</td><td><code>interface IRepo</code></td></tr>
</table>""",
    4: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Situation</th><th>Approach</th><th>Tool / PEP</th></tr>
<tr><td>New team project</td><td>Agree on PEP 8 + formatter in CI</td><td>Black / ruff</td></tr>
<tr><td>Public API function</td><td>One-line docstring + type hints</td><td>PEP 257, 484</td></tr>
<tr><td>Package version bump</td><td>Semantic versioning in pyproject</td><td>PEP 440</td></tr>
<tr><td>Interview "Python philosophy"</td><td>Cite Zen principles</td><td><code>import this</code></td></tr>
</table>""",
    13: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Situation</th><th>Approach</th><th>Why</th></tr>
<tr><td>Long-running worker memory grows</td><td>Profile + check caches holding refs</td><td>Refcount won't free if referenced</td></tr>
<tr><td>Parent/child mutual refs</td><td>weakref or break cycle on delete</td><td>GC may delay collection</td></tr>
<tr><td>Debug "object still alive?"</td><td><code>sys.getrefcount</code>, <code>gc.get_referrers</code></td><td>Find unexpected references</td></tr>
<tr><td>File handle cleanup</td><td><code>with open(...) as f</code></td><td>Deterministic — not GC-dependent</td></tr>
</table>""",
    22: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Situation</th><th>Level</th><th>Pattern</th></tr>
<tr><td>Request handled OK</td><td>INFO</td><td><code>logger.info("order %s created", id)</code></td></tr>
<tr><td>Retry succeeded</td><td>WARNING</td><td>Recoverable anomaly</td></tr>
<tr><td>Payment failed</td><td>ERROR</td><td><code>logger.exception(...)</code> in except</td></tr>
<tr><td>Local debugging</td><td>DEBUG</td><td>Console only — off in prod</td></tr>
<tr><td>Disk fills up</td><td>RotatingFileHandler</td><td>maxBytes + backupCount</td></tr>
</table>""",
    14: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Boundary</th><th>Use Pydantic?</th><th>Example</th></tr>
<tr><td>HTTP JSON body</td><td class="cell-yes"><span class="yn-yes"></span>Yes</td><td>FastAPI <code>UserCreate</code></td></tr>
<tr><td>Internal helper</td><td class="cell-no"><span class="yn-no"></span>Usually plain types</td><td><code>def add(a: int, b: int)</code></td></tr>
<tr><td>Config from env/file</td><td class="cell-yes"><span class="yn-yes"></span>Yes</td><td><code>Settings(BaseModel)</code></td></tr>
<tr><td>ORM row to client</td><td class="cell-yes"><span class="yn-yes"></span>Response schema</td><td><code>from_attributes=True</code></td></tr>
</table>""",
    28: """
<h3>When to use which — scenarios</h3>
<table class="data-tbl scenario-tbl">
<tr><th>Need</th><th>Layer</th><th>Technology</th></tr>
<tr><td>HTTP routing</td><td>routes</td><td>FastAPI <code>@app.post</code></td></tr>
<tr><td>Input validation</td><td>schemas</td><td>Pydantic <code>BaseModel</code></td></tr>
<tr><td>Persist data</td><td>models + session</td><td>SQLAlchemy ORM</td></tr>
<tr><td>Business rules</td><td>services</td><td>Plain Python module</td></tr>
<tr><td>Full MVC web + admin</td><td>Django app</td><td>Prefer Django over raw FastAPI</td></tr>
</table>""",
}


def scenarios_for(slide_num: int) -> str:
    return SCENARIOS.get(slide_num, "")
