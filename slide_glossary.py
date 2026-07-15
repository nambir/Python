"""Key terms explained tables for every slide in PythonTraining.html."""

GLOSSARY: dict[int, str] = {
    1: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Interpretation</td><td>Executing source via an <b>interpreter</b> (CPython) instead of compiling to machine code (.exe) first.</td><td><code>python hello.py</code></td></tr>
<tr><td>Interpreter</td><td>Program that reads and runs Python — compiles to bytecode, then executes in a VM loop.</td><td><code>python</code></td></tr>
<tr><td>Bytecode</td><td>Intermediate instructions in <code>__pycache__/*.pyc</code> between <code>.py</code> source and execution.</td><td><code>app.cpython-312.pyc</code></td></tr>
<tr><td>Dynamic typing</td><td>Variables not tied to one type — same name can hold int, then str.</td><td><code>x = 5; x = "hi"</code></td></tr>
<tr><td>Indentation</td><td>Leading spaces (usually 4) define blocks — no <code>{ }</code> braces.</td><td><code>if True:</code> + indent</td></tr>
<tr><td>Duck typing</td><td>Use an object if it has the right behavior — no interface keyword required.</td><td><code>animal.speak()</code></td></tr>
</table>""",
    2: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>PATH</td><td>Windows environment variable listing folders where the OS searches for executables.</td><td><code>python</code> found in PATH</td></tr>
<tr><td>pip</td><td>Python's package installer — downloads libraries from PyPI (like NuGet).</td><td><code>pip install pytest</code></td></tr>
<tr><td>REPL</td><td>Read-Eval-Print Loop — interactive shell; type code, see result immediately.</td><td><code>python</code> then <code>2+2</code></td></tr>
<tr><td>Script</td><td>A <code>.py</code> file run from the command line in one shot.</td><td><code>python app.py</code></td></tr>
<tr><td>Interpreter path</td><td>Which Python executable your IDE uses — must match your venv.</td><td>Ctrl+Shift+P → Select Interpreter</td></tr>
<tr><td>py launcher</td><td>Windows <code>py</code> command picks among multiple installed Python versions.</td><td><code>py -3.12 script.py</code></td></tr>
<tr><td>__main__</td><td>Special module name when a file is run directly (not imported).</td><td><code>if __name__ == "__main__":</code></td></tr>
</table>""",
    3: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Tuple</td><td>Ordered, fixed sequence in parentheses — records, coordinates, return values.</td><td><code>point = (10, 20)</code></td></tr>
<tr><td>Immutable</td><td>Object <b>cannot be changed in place</b> after creation.<br><br><b>Works:</b> read <code>t[0]</code>, slice <code>t[1:3]</code> (new tuple), <code>len</code>, <code>for x in t</code>, <code>x in t</code>, use as dict key.<br><br><b>Does NOT work:</b> <code>t[0] = 5</code>, <code>t.append()</code>, <code>t.pop()</code>, <code>del t[0]</code> → <code>TypeError</code> or <code>AttributeError</code>.<br><br><b>Why blocked:</b> Python must keep hash and size fixed for dict keys and memory safety — if contents could change, cached hash would be wrong.</td><td><code>t[0]=5</code> fails</td></tr>
<tr><td>Mutable</td><td>Can change in place — lists grow/shrink with append/pop.</td><td><code>items.append(4)</code></td></tr>
<tr><td>Slicing</td><td>Sub-sequence via <code>[start:stop:step]</code> — stop is exclusive.</td><td><code>nums[1:4]</code></td></tr>
<tr><td>Packing</td><td>Combine values into one tuple using commas.</td><td><code>a, b = 1, 2</code></td></tr>
<tr><td>Unpacking</td><td>Assign sequence elements to multiple variables at once.</td><td><code>x, y = point</code></td></tr>
<tr><td>Index</td><td>Position starting at 0; <code>-1</code> is last item.</td><td><code>nums[-1]</code></td></tr>
<tr><td>Hashable</td><td>Can be dict key / set member — tuple and frozenset yes; list and set no.</td><td><code>{(1,2): "A"}</code></td></tr>
<tr><td>set</td><td>Mutable collection of unique items — duplicates removed.</td><td><code>{"a", "b"}</code></td></tr>
<tr><td>frozenset</td><td>Immutable set — cannot add/remove. Can be a dict key.</td><td><code>frozenset({1,2})</code></td></tr>
<tr><td>list</td><td>Mutable sequence — use when size or content changes.</td><td><code>cart.append(item)</code></td></tr>
</table>""",
    4: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Projects/</td><td>Folder with one practice <code>.py</code> file per slide topic.</td><td><code>05_comprehensions.py</code></td></tr>
<tr><td>Python-Set2/</td><td>Real multi-file projects — Django, pandas, Pipecat, etc.</td><td><code>pythonBasics/</code></td></tr>
<tr><td>requirements.txt</td><td>Lists pip packages and versions for reproducible installs.</td><td><code>pip install -r requirements.txt</code></td></tr>
<tr><td>.venv/</td><td>Virtual environment folder — isolated Python + packages per project.</td><td><code>python -m venv .venv</code></td></tr>
<tr><td>__init__.py</td><td>Makes a directory a Python <b>package</b> so you can <code>import</code> it.</td><td><code>myapp/__init__.py</code></td></tr>
<tr><td>Module</td><td>Any single <code>.py</code> file containing Python code.</td><td><code>utils.py</code></td></tr>
</table>""",
    5: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Arithmetic</td><td>Math operators: <code>+ - * / // % **</code></td><td><code>17 // 5</code> → 3</td></tr>
<tr><td>Floor division</td><td><code>//</code> divides and rounds down to integer.</td><td><code>7 // 2</code> → 3</td></tr>
<tr><td>Modulo</td><td><code>%</code> returns remainder after division.</td><td><code>17 % 5</code> → 2</td></tr>
<tr><td>Identity (is)</td><td>Same object in memory — not just equal value.</td><td><code>a is b</code></td></tr>
<tr><td>Equality (==)</td><td>Same value — different objects can be equal.</td><td><code>[1]==[1]</code> True</td></tr>
<tr><td>Membership (in)</td><td>Test if value exists in a collection.</td><td><code>5 in [1,5,9]</code></td></tr>
<tr><td>None</td><td><b>None</b> = no value (like C# <code>null</code>).<br><br><b>Test with:</b> <code>if x is None:</code> — use <code>is</code>, not <code>==</code>.<br><br><b>Why:</b> only one <code>None</code> object exists in Python.</td><td><code>if x is None:</code></td></tr>
<tr><td>Bitwise</td><td>Operators on binary digits: <code>&amp; | ^ ~ &lt;&lt; &gt;&gt;</code></td><td><code>5 &amp; 3</code> → 1</td></tr>
</table>""",
    6: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>if / elif / else</td><td>Branch execution based on True/False conditions.</td><td><code>if x &gt; 0:</code></td></tr>
<tr><td>for loop</td><td>Iterate over each item in a sequence (like C# foreach).</td><td><code>for i in range(5):</code></td></tr>
<tr><td>while loop</td><td>Repeat while condition is True — watch for infinite loops.</td><td><code>while n &lt; 10:</code></td></tr>
<tr><td>break</td><td>Exit the loop immediately.</td><td><code>break</code> inside for</td></tr>
<tr><td>continue</td><td>Skip rest of <b>this</b> loop iteration — go to next.<br><br><b>Does NOT:</b> same as <code>pass</code> — <code>pass</code> does nothing but stays in same iteration.</td><td><code>continue</code></td></tr>
<tr><td>pass</td><td><b>pass = this block is intentionally empty for now.</b> A stub — define structure today, add real code later. Does nothing at runtime but satisfies syntax.<br><br><b>Use when:</b> stub <code>def</code>, empty <code>class</code>, custom <code>Exception</code>.<br><br><b>Later:</b> remove <code>pass</code> and write your logic.<br><br><b>Does NOT:</b> skip a loop — use <code>continue</code>.</td><td><code>def todo(): pass</code></td></tr>
<tr><td>if True / if False</td><td><code>if True</code> always runs once (TODO stub). <code>if False</code> never runs (disable code temporarily).</td><td><code>if False: old_code()</code></td></tr>
<tr><td>for-else</td><td><code>else</code> on a loop runs only if the loop finished <b>without</b> <code>break</code>.<br><br><b>Not the same as:</b> <code>try/else</code> or <code>if/else</code>.<br><br><b>Use when:</b> search — report "not found" in <code>else</code>.</td><td>search pattern</td></tr>
<tr><td>range</td><td>Generates sequence of numbers — often used with for.</td><td><code>range(3)</code> → 0,1,2</td></tr>
</table>""",
    7: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>List comprehension</td><td>Build a list in one expression with for/if inside <code>[ ]</code>.</td><td><code>[n*n for n in range(6)]</code></td></tr>
<tr><td>Set comprehension</td><td>Build a unique set with <code>{ }</code> syntax.</td><td><code>{c.lower() for c in s}</code></td></tr>
<tr><td>Dict comprehension</td><td>Build key-value dict in one expression.</td><td><code>{w: len(w) for w in words}</code></td></tr>
<tr><td>Generator expression</td><td>Lazy comprehension with <code>( )</code> — yields one item at a time.</td><td><code>(n*n for n in range(10**6))</code></td></tr>
<tr><td>Lazy evaluation</td><td>Compute values only when needed — saves memory.</td><td><code>next(gen)</code></td></tr>
<tr><td>Filter clause</td><td>Optional <code>if</code> at end of comprehension to keep matching items.</td><td><code>if n % 2 == 0</code></td></tr>
</table>""",
    8: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>def</td><td>Keyword to define a function.</td><td><code>def greet(name):</code></td></tr>
<tr><td>Parameter</td><td>Variable in function definition receiving a value.</td><td><code>def f(x):</code></td></tr>
<tr><td>Argument</td><td>Actual value passed when calling the function.</td><td><code>greet("Ali")</code></td></tr>
<tr><td>Default argument</td><td>Parameter value used if caller omits it.</td><td><code>greeting="Hello"</code></td></tr>
<tr><td>Mutable default trap</td><td><b>Never</b> <code>def f(items=[])</code> — same list reused every call.<br><br><b>Fix:</b> <code>def f(items=None): items = items or []</code><br><br><b>Why:</b> default objects are created once at function definition time.</td><td><code>def f(x=None):</code></td></tr>
<tr><td>*args</td><td>Collects extra positional arguments as a tuple.</td><td><code>def f(*args):</code></td></tr>
<tr><td>**kwargs</td><td>Collects extra keyword arguments as a dict.</td><td><code>def f(**kw):</code></td></tr>
<tr><td>Lambda</td><td>Anonymous one-line function.</td><td><code>lambda x: x*2</code></td></tr>
<tr><td>Closure</td><td>Inner function remembering variables from outer scope.</td><td>counter pattern</td></tr>
<tr><td>LEGB</td><td>Scope lookup order: Local → Enclosing → Global → Builtin.</td><td>name resolution</td></tr>
</table>""",
    9: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>map</td><td>Apply a function to every item — returns iterator.</td><td><code>map(str, [1,2])</code></td></tr>
<tr><td>filter</td><td>Keep items where function returns True.</td><td><code>filter(lambda x: x&gt;0, nums)</code></td></tr>
<tr><td>reduce</td><td>Fold iterable to single value (functools).</td><td><code>reduce(add, nums)</code></td></tr>
<tr><td>zip</td><td>Pair elements from multiple iterables.</td><td><code>zip(names, scores)</code></td></tr>
<tr><td>enumerate</td><td>Yield (index, value) pairs while looping.</td><td><code>enumerate(items)</code></td></tr>
<tr><td>sorted</td><td>Return new sorted list — original unchanged.</td><td><code>sorted(nums)</code></td></tr>
<tr><td>isinstance</td><td>Check if object is instance of type (supports inheritance).</td><td><code>isinstance(x, int)</code></td></tr>
</table>""",
    10: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Class</td><td>Blueprint for objects — attributes + methods.</td><td><code>class Dog:</code></td></tr>
<tr><td>Object</td><td>Instance of a class created at runtime.</td><td><code>Dog("Rex")</code></td></tr>
<tr><td>__init__</td><td>Constructor — runs when object is created; sets <code>self</code>.</td><td><code>def __init__(self, name):</code></td></tr>
<tr><td>self</td><td>Reference to current instance (like C# <code>this</code>).</td><td><code>self.name = name</code></td></tr>
<tr><td>Inheritance</td><td>Child class gets parent methods — override to customize.</td><td><code>class Dog(Animal):</code></td></tr>
<tr><td>Polymorphism</td><td>Same method call, different behavior per class.</td><td><code>pet.speak()</code></td></tr>
<tr><td>Encapsulation</td><td>Hide internal state — <code>_prefix</code> convention, <code>@property</code>.</td><td><code>self._balance</code></td></tr>
<tr><td>MRO</td><td>Method Resolution Order — which parent method runs first.</td><td><code>Dog.__mro__</code></td></tr>
</table>""",
    11: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Decorator</td><td>Function wrapping another function to add behavior.</td><td><code>@timer</code></td></tr>
<tr><td>@syntax</td><td>Syntactic sugar — <code>@dec</code> above <code>def f</code> means <code>f = dec(f)</code>.</td><td><code>@app.get("/")</code></td></tr>
<tr><td>Wrapper</td><td>Inner function that calls the original and adds logic.</td><td><code>def wrapper(*a,**k):</code></td></tr>
<tr><td>@wraps</td><td>Preserves original function name and docstring metadata.</td><td><code>@wraps(fn)</code></td></tr>
<tr><td>Stacking</td><td>Multiple decorators applied bottom-up.</td><td><code>@a @b def f</code></td></tr>
<tr><td>Higher-order function</td><td>Function that takes or returns another function.</td><td>decorator pattern</td></tr>
</table>""",
    12: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Descriptor</td><td>Object defining <code>__get__</code>, <code>__set__</code>, <code>__delete__</code> for attribute access.</td><td>advanced pattern</td></tr>
<tr><td>@property</td><td>Built-in descriptor — read-only or managed attribute.</td><td><code>@property def age:</code></td></tr>
<tr><td>Getter</td><td>Method called when attribute is read.</td><td><code>def temp(self): return self._t</code></td></tr>
<tr><td>Setter</td><td>Method called when attribute is assigned — validate here.</td><td><code>@temp.setter</code></td></tr>
<tr><td>Managed attribute</td><td>Looks like field, runs code on get/set.</td><td><code>c.temp = 25</code></td></tr>
</table>""",
    13: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Generator</td><td>Function using <code>yield</code> — produces values lazily.</td><td><code>def gen(): yield 1</code></td></tr>
<tr><td>yield</td><td>Pause function and return value; resume on next call.</td><td><code>yield n</code></td></tr>
<tr><td>Iterator</td><td>Object with <code>__iter__</code> and <code>__next__</code> — consumed one step at a time.</td><td><code>next(it)</code></td></tr>
<tr><td>Iterable</td><td>Object you can loop over — lists, generators, files.</td><td><code>for x in obj:</code></td></tr>
<tr><td>StopIteration</td><td>Raised when iterator has no more items.</td><td>end of for-loop</td></tr>
<tr><td>itertools</td><td>Standard module with efficient iterator tools.</td><td><code>itertools.chain</code></td></tr>
</table>""",
    14: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Type hint</td><td>Annotation showing expected types — not enforced at runtime.</td><td><code>name: str</code></td></tr>
<tr><td>Return type</td><td><code>-&gt;</code> annotation on what function returns.</td><td><code>-&gt; str:</code></td></tr>
<tr><td>Optional</td><td>Value can be the type or <code>None</code>.</td><td><code>Optional[int]</code></td></tr>
<tr><td>Union</td><td>Value can be one of several types.</td><td><code>Union[int, str]</code></td></tr>
<tr><td>mypy</td><td>Static type checker — finds type errors before runtime.</td><td><code>mypy app.py</code></td></tr>
<tr><td>Generic</td><td>Type parameterized by another type — <code>List[int]</code>.</td><td><code>Dict[str, int]</code></td></tr>
</table>""",
    15: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>open()</td><td>Built-in to open files — always specify <code>encoding="utf-8"</code> for text.</td><td><code>open("f.txt","r")</code></td></tr>
<tr><td>Mode</td><td><code>r</code> read, <code>w</code> write (overwrite), <code>a</code> append, <code>rb</code> binary.</td><td><code>"w"</code></td></tr>
<tr><td>with statement</td><td>Context manager — auto-closes file even on error.</td><td><code>with open(...) as f:</code></td></tr>
<tr><td>JSON</td><td>Text format for structured data — <code>json.loads/dumps</code>.</td><td><code>json.dumps(data)</code></td></tr>
<tr><td>pathlib</td><td>Object-oriented file paths — cleaner than string concat.</td><td><code>Path("a")/"b"</code></td></tr>
<tr><td>encoding</td><td>Character set for text files — UTF-8 handles all languages.</td><td><code>encoding="utf-8"</code></td></tr>
</table>""",
    16: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>try / except</td><td>Attempt code; catch specific errors if they occur (like C# catch).</td><td><code>except ValueError:</code></td></tr>
<tr><td>else</td><td>On <b>try</b>: runs if try block had <b>no</b> exception.<br><br><b>Not the same as:</b> loop <code>for-else</code> (runs if no <code>break</code>).</td><td><code>try: ... else:</code></td></tr>
<tr><td>finally</td><td>Always runs — used for cleanup (close file, release lock).</td><td><code>finally: close()</code></td></tr>
<tr><td>raise</td><td>Throw an exception intentionally.</td><td><code>raise ValueError("bad")</code></td></tr>
<tr><td>Custom exception</td><td>Your own error class inheriting <code>Exception</code>.</td><td><code>class AppError(Exception):</code></td></tr>
<tr><td>Traceback</td><td>Stack trace showing where error occurred.</td><td>printed on crash</td></tr>
</table>""",
    17: r"""
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Regex</td><td>Pattern language for matching text — module <code>re</code>.</td><td><code>r"\d+"</code></td></tr>
<tr><td>Raw string</td><td><code>r"..."</code> — backslashes not escaped (ideal for regex).</td><td><code>r"\d+"</code></td></tr>
<tr><td>search</td><td>Find first match anywhere in string.</td><td><code>re.search(pat, text)</code></td></tr>
<tr><td>match</td><td>Match only at start of string.</td><td><code>re.match(pat, text)</code></td></tr>
<tr><td>findall</td><td>Return list of all non-overlapping matches.</td><td><code>re.findall(r"\d+", s)</code></td></tr>
<tr><td>Group</td><td>Captured substring in parentheses — <code>m.group(1)</code>.</td><td><code>(\d{4})</code></td></tr>
<tr><td>sub</td><td>Replace matches with replacement string.</td><td><code>re.sub(pat, "X", s)</code></td></tr>
</table>""",
    18: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Counter</td><td>Dict subclass counting hashable items.</td><td><code>Counter("hello")</code></td></tr>
<tr><td>defaultdict</td><td>Dict with factory for missing keys — no KeyError.</td><td><code>defaultdict(list)</code></td></tr>
<tr><td>deque</td><td>Double-ended queue — fast append/pop both ends.</td><td><code>deque.appendleft(0)</code></td></tr>
<tr><td>namedtuple</td><td>Tuple with named fields — lightweight record.</td><td><code>Point(10, 20).x</code></td></tr>
<tr><td>ChainMap</td><td>Search multiple dicts as one — first match wins.</td><td>config layering</td></tr>
<tr><td>OrderedDict</td><td>Dict remembering insertion order (built-in since 3.7).</td><td>legacy code</td></tr>
</table>""",
    19: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Unit test</td><td>Automated check of one small unit of code.</td><td><code>assert add(2,3)==5</code></td></tr>
<tr><td>pytest</td><td>Popular test framework — plain <code>assert</code>, no boilerplate.</td><td><code>pytest test_file.py</code></td></tr>
<tr><td>unittest</td><td>Built-in framework — classes, <code>setUp</code>, <code>tearDown</code>.</td><td><code>TestCase</code></td></tr>
<tr><td>assert</td><td>Statement that raises AssertionError if condition is False.</td><td><code>assert x &gt; 0</code></td></tr>
<tr><td>mock / patch</td><td>Replace real dependency with fake for isolated tests.</td><td><code>@patch("requests.get")</code></td></tr>
<tr><td>setUp / tearDown</td><td>Run before/after each test method in a class.</td><td>unittest lifecycle</td></tr>
</table>""",
    20: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Thread</td><td>Lightweight concurrent execution within one process.</td><td><code>threading.Thread</code></td></tr>
<tr><td>GIL</td><td>Global Interpreter Lock — one thread runs Python bytecode at a time.</td><td>CPython limitation</td></tr>
<tr><td>Lock</td><td>Mutex preventing two threads mutating shared data simultaneously.</td><td><code>with lock:</code></td></tr>
<tr><td>I/O-bound</td><td>Waiting on network/disk — threads help despite GIL.</td><td>HTTP requests</td></tr>
<tr><td>CPU-bound</td><td>Heavy computation — use <code>multiprocessing</code> not threads.</td><td>image processing</td></tr>
<tr><td>ThreadPoolExecutor</td><td>Pool of worker threads for parallel I/O tasks.</td><td><code>concurrent.futures</code></td></tr>
</table>""",
    21: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Context manager</td><td>Object defining setup/teardown for <code>with</code> block.</td><td><code>with open(f):</code></td></tr>
<tr><td>__enter__</td><td>Called when entering <code>with</code> — setup, return resource.</td><td>open file</td></tr>
<tr><td>__exit__</td><td>Called when leaving <code>with</code> — cleanup, even on error.</td><td>close file</td></tr>
<tr><td>@contextmanager</td><td>Decorator making generator function into context manager.</td><td><code>yield</code> splits setup/teardown</td></tr>
<tr><td>with statement</td><td>Guarantees cleanup — preferred over manual try/finally.</td><td><code>with lock:</code></td></tr>
</table>""",
    22: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>async def</td><td>Defines a coroutine function — not run until awaited.</td><td><code>async def fetch():</code></td></tr>
<tr><td>await</td><td>Pause coroutine until async operation completes.</td><td><code>await asyncio.sleep(1)</code></td></tr>
<tr><td>Coroutine</td><td>Cooperative task managed by event loop.</td><td>async function</td></tr>
<tr><td>Event loop</td><td>Schedules and runs coroutines — <code>asyncio.run()</code> starts it.</td><td><code>asyncio.run(main())</code></td></tr>
<tr><td>asyncio.gather</td><td>Run multiple coroutines concurrently, wait for all.</td><td><code>await gather(a(), b())</code></td></tr>
<tr><td>Concurrency</td><td>Multiple tasks making progress — not same as parallel CPU.</td><td>async HTTP calls</td></tr>
</table>""",
    23: r"""
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>venv</td><td>Virtual environment — isolated Python + packages per project.</td><td><code>python -m venv .venv</code></td></tr>
<tr><td>activate</td><td>Switch shell to use venv's Python and pip.</td><td><code>.venv\Scripts\activate</code></td></tr>
<tr><td>pip freeze</td><td>Export installed packages with exact versions.</td><td><code>pip freeze &gt; requirements.txt</code></td></tr>
<tr><td>requirements.txt</td><td>List of dependencies for <code>pip install -r</code>.</td><td>one package per line</td></tr>
<tr><td>pyenv</td><td>Tool to install/switch multiple Python versions on one machine.</td><td><code>pyenv install 3.12</code></td></tr>
<tr><td>.gitignore</td><td>Exclude <code>.venv/</code> from git — never commit virtual envs.</td><td><code>.venv/</code> in file</td></tr>
</table>""",
    24: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Portfolio</td><td>Collection of real projects demonstrating skills to interviewers.</td><td>Python-Set2/</td></tr>
<tr><td>pythonBasics/</td><td>Topic modules — OOP, loops, collections, tests.</td><td>MyClass/</td></tr>
<tr><td>google-python-exercises/</td><td>Classic puzzles — regex, files, algorithms.</td><td>babynames/</td></tr>
<tr><td>pandas/</td><td>Data analysis with DataFrames and Jupyter notebooks.</td><td>Titanic notebook</td></tr>
<tr><td>djangobasics/</td><td>Full-stack web app — MVT pattern, ORM, templates.</td><td>meeting_planner/</td></tr>
<tr><td>Pipecat-Project/</td><td>Voice AI pipeline — STT, LLM, TTS over WebRTC.</td><td>voice-bouncer/</td></tr>
</table>""",
    25: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>MyClass</td><td>OOP module — inheritance, polymorphism, dunder methods.</td><td>BankAccount.py</td></tr>
<tr><td>MyCollections</td><td>Hands-on list, dict, set, tuple exercises.</td><td>collection demos</td></tr>
<tr><td>MyLoops</td><td>for, while, range, enumerate practice.</td><td>loop scripts</td></tr>
<tr><td>MyModules</td><td>import system, packages, <code>__name__</code>.</td><td>module demos</td></tr>
<tr><td>MyExceptionHandling</td><td>try/except, raise, custom exceptions.</td><td>error demos</td></tr>
<tr><td>MyUnitTesting</td><td>pytest and unittest examples.</td><td>test_*.py</td></tr>
</table>""",
    26: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>babynames</td><td>Regex exercise parsing baby name data files.</td><td>google-exercises/</td></tr>
<tr><td>copyspecial</td><td>File system exercise — shutil, os, metadata.</td><td>copy by extension</td></tr>
<tr><td>DataFrame</td><td>pandas 2D table — rows and named columns like Excel.</td><td><code>pd.read_csv()</code></td></tr>
<tr><td>groupby</td><td>Split data into groups and aggregate (sum, mean, count).</td><td><code>df.groupby("col")</code></td></tr>
<tr><td>Jupyter</td><td>Interactive notebook — code cells + markdown + charts.</td><td><code>.ipynb</code></td></tr>
<tr><td>CSV</td><td>Comma-separated values file — common data import format.</td><td>titanic.csv</td></tr>
</table>""",
    27: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Django</td><td>Full Python web framework — ORM, admin, auth, templates.</td><td>meeting_planner/</td></tr>
<tr><td>MVT</td><td>Model-View-Template — Django's architecture pattern.</td><td>models.py, views.py</td></tr>
<tr><td>ORM</td><td>Map database tables to Python classes — no raw SQL required.</td><td><code>Meeting.objects.all()</code></td></tr>
<tr><td>Migration</td><td>Version-controlled database schema change files.</td><td><code>python manage.py migrate</code></td></tr>
<tr><td>DRF</td><td>Django REST Framework — serializers + ViewSets for JSON APIs.</td><td>serializers.py</td></tr>
<tr><td>Serializer</td><td>Convert model instances to/from JSON — like Pydantic schemas.</td><td>DrinkSerializer</td></tr>
<tr><td>JWT</td><td>JSON Web Token — stateless API authentication.</td><td>simplejwt/</td></tr>
</table>""",
    28: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>STT</td><td>Speech-to-Text — converts audio to text.</td><td>Whisper, cloud STT</td></tr>
<tr><td>LLM</td><td>Large Language Model — generates conversational responses.</td><td>GPT, local LLM</td></tr>
<tr><td>TTS</td><td>Text-to-Speech — converts text back to audio.</td><td>voice output</td></tr>
<tr><td>WebRTC</td><td>Real-time browser audio/video communication protocol.</td><td>browser mic</td></tr>
<tr><td>Pipecat</td><td>Framework for building voice AI pipelines.</td><td>processors chain</td></tr>
<tr><td>IVR</td><td>Interactive Voice Response — phone menu style flow.</td><td>voice-bouncer/</td></tr>
</table>""",
    29: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Separation of concerns</td><td>Split routes, services, models, tests into folders.</td><td>api/ services/ tests/</td></tr>
<tr><td>Entry point</td><td>Main file starting the app — <code>main.py</code> or <code>manage.py</code>.</td><td><code>uvicorn main:app</code></td></tr>
<tr><td>DTO / Schema</td><td>Data Transfer Object — validates API input/output.</td><td>Pydantic, DRF Serializer</td></tr>
<tr><td>Service layer</td><td>Business logic separated from HTTP handlers.</td><td>services/user.py</td></tr>
<tr><td>.env</td><td>Environment variables for secrets — never commit real keys.</td><td><code>DATABASE_URL</code></td></tr>
</table>""",
    30: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Static typing</td><td>C# declares types at compile time — <code>int x = 5</code>.</td><td>C# variable</td></tr>
<tr><td>Dynamic typing</td><td>Python assigns without type declaration.</td><td><code>x = 5</code></td></tr>
<tr><td>Interface</td><td>C# contract — Python uses ABC or duck typing instead.</td><td><code>interface IRepo</code></td></tr>
<tr><td>Null vs None</td><td>C# <code>null</code> — test with <code>== null</code>.</td><td>Python <code>None</code> — test with <code>is None</code>.</td></tr>
<tr><td>pass</td><td>No keyword — use empty <code>{ }</code> for a stub block.<br><br><b>Stronger stub:</b> <code>throw new NotImplementedException()</code>.<br><br><b>Interfaces:</b> declare method without body — no pass needed.</td><td><code>pass</code> = block intentionally empty for now.<br><br><b>Stronger stub:</b> <code>raise NotImplementedError()</code>.</td></tr>
<tr><td>this vs self</td><td><code>this</code> — implicit in instance methods.</td><td><code>self</code> — explicit first parameter.</td></tr>
<tr><td>using vs with</td><td><code>using (var f = ...)</code> — auto dispose.</td><td><code>with open(...) as f:</code> — context manager.</td></tr>
<tr><td>try/catch vs try/except</td><td>Same concept — different keyword in Python.</td><td><code>except ValueError:</code></td></tr>
<tr><td>NuGet vs pip</td><td>C# package manager vs Python package installer.</td><td><code>pip install</code></td></tr>
<tr><td>Task vs coroutine</td><td>C# <code>async Task</code> vs Python <code>async def</code> coroutine.</td><td><code>await</code> both</td></tr>
</table>""",
}


def glossary_for(slide_num: int) -> str:
    return GLOSSARY.get(slide_num, "")
