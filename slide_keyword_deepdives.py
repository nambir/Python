"""Pass-style 'Python keywords explained' blocks — one section per slide."""

KEYWORD_DEEPDIVES: dict[int, str] = {
    1: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Indentation</b> = the block structure in Python. No <code>{ }</code> braces — spaces after <code>:</code> define what belongs to <code>if</code>, <code>for</code>, <code>def</code>.<br><b>Use when:</b> every control-flow block.<br><b>Trap:</b> mixing tabs and spaces → <code>IndentationError</code>.</div>
<div class="keyword-box"><b>Dynamic typing</b> = a variable name can point to different types over time.<br><b>Example:</b> <code>x = 5</code> then <code>x = "hi"</code> — legal.<br><b>Not like C#:</b> no <code>int x</code> declaration required.</div>
<div class="keyword-box"><b>Duck typing</b> = another function uses an object <b>without knowing the class name</b> — only the behavior.<br><b>Normal:</b> a class having <code>.send()</code> is just OOP.<br><b>Duck typing:</b> <code>notify(channel, msg)</code> accepts Email / SMS / Slack if each has <code>.send()</code> — no interface.<br><b>Saying:</b> if it walks like a duck and quacks like a duck, treat it as a duck.</div>
""",
    2: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>if __name__ == "__main__":</b> = run this code only when the file is executed directly, not when imported.<br><b>Use when:</b> script entry point (like C# <code>Main</code>).<br><b>Strategy:</b> put all <code>def</code> / <code>class</code> above this block — Python runs top to bottom.<br><div class="step-pre">def Add(x, y):\n    print(f\"Answer is={x + y}\")\n\nif __name__ == \"__main__\":\n    Add(1, 2)</div></div>
<div class="keyword-box"><b>NameError</b> = name used before it exists.<br><b>Trap:</b> call <code>Add(1, 2)</code> above <code>def Add</code> → <code>name 'Add' is not defined</code>.<br><b>C# contrast:</b> method order inside a class usually does not matter; in a Python script file, order does.<br><br><span class="cell-no"><span class="yn-no"></span>Wrong — will not work</span><div class="step-pre">if __name__ == "__main__":
    print("hai")
    Add(1, 2)      # NameError: name 'Add' is not defined

def Add(x, y):
    print(f"Answer is={x + y}")</div>
<span class="cell-yes"><span class="yn-yes"></span>Correct — define first, call later</span><div class="step-pre">def Add(x, y):
    print(f"Answer is={x + y}")

if __name__ == "__main__":
    print("hai")
    Add(1, 2)</div></div>
<div class="keyword-box"><b>REPL</b> = Read-Eval-Print Loop. Type one line, see result immediately.<br><b>Use when:</b> quick experiments.<br><b>Not for:</b> full applications — use a <code>.py</code> script.</div>
""",
    5: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Immutable</b> = cannot change in place after creation.<br><b>Works:</b> read, slice, dict key (tuple, frozenset).<br><b>Fails:</b> <code>t[0]=5</code>, <code>append</code> → <code>TypeError</code>.</div>
<div class="keyword-box"><b>frozenset</b> = set that cannot change — can be a dict key.<br><b>vs set:</b> set is mutable → not hashable as dict key.</div>
""",
    3: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>__init__.py</b> = marks a folder as a Python <b>package</b> so you can <code>import myapp.utils</code>.<br><b>Can be empty</b> — often just <code>pass</code> or a one-line docstring.</div>
<div class="keyword-box"><b>.venv/</b> = isolated Python + packages per project.<br><b>Rule:</b> never install project libraries globally — one venv per app.</div>
""",
    7: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>None</b> = Python's "no value" (like C# <code>null</code>).<br><b>Test with:</b> <code>if x is None:</code> — never <code>x == None</code>.<br><b>Why is:</b> there is only one <code>None</code> object in memory.</div>
<div class="keyword-box"><b>==</b> = same value. &nbsp; <b>is</b> = same object in memory.<br><div class="step-pre">a = [1, 2]; b = [1, 2]\na == b   # True\na is b   # False</div><b>Use is for:</b> <code>None</code> only (in practice).</div>
<div class="keyword-box"><b>//</b> = floor division (whole number result). <b>/</b> = true division (always float in Python 3).<br><b>Example:</b> <code>10 / 4</code> → <code>2.5</code>, <code>10 // 4</code> → <code>2</code>.</div>
<div class="keyword-box"><b>in</b> = membership test — works on lists, strings, dict keys, sets.<br><b>Example:</b> <code>"py" in "python"</code> → <code>True</code>.</div>
<div class="keyword-box"><b>+=</b> and friends = in-place assignment.<br><b>Example:</b> <code>n += 5</code> same as <code>n = n + 5</code>. Works on numbers, strings, lists.</div>
<div class="keyword-box"><b>:=</b> walrus — assign inside an expression (Python 3.8+).<br>
<div class="step-pre"># without walrus
n = len(data)
if n &gt; 0:
    print(n)

# with walrus — assign + test together
if (n := len(data)) &gt; 0:
    print(n)</div>
<b>Use when:</b> you need the value in the condition <b>and</b> in the body.<br>
<b>Real use:</b> invoice line count, <code>while (line := input(...)) != "":</code>, match checks.<br>
<b>Avoid:</b> using <code>:=</code> for every assignment — normal <code>=</code> is clearer then.</div>
""",
    8: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>pass</b> = this block is intentionally empty for now (stub). Remove <code>pass</code> when you add real code.</div>
<div class="keyword-box"><b>continue</b> = skip rest of this loop iteration, go to next.<br><b>pass</b> = do nothing here but stay in the same iteration.<br><b>Does NOT:</b> use <code>pass</code> to skip a loop — use <code>continue</code>.</div>
<div class="keyword-box"><b>for-else / while-else</b> = <code>else</code> runs only if the loop finished <b>without</b> <code>break</code>.<br><b>Classic use:</b> search loop — <code>else: print("not found")</code>.</div>
<div class="keyword-box"><b>elif</b> = else-if — test another condition only if previous branches failed.<br><b>Only one branch</b> of <code>if / elif / else</code> runs.</div>
""",
    9: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>[...]</b> list comprehension = build full list in memory now.<br><b>(...)</b> generator expression = produce one item at a time, lazy.<br><b>Use generator when:</b> large data — saves memory.</div>
<div class="keyword-box"><b>Comprehension filter</b> — trailing <code>if</code> keeps matching items only.<br><b>Example:</b> <code>[x for x in nums if x % 2 == 0]</code></div>
""",
    10: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Mutable default trap</b> — never <code>def f(items=[])</code>.<br><b>Why:</b> the same list is reused on every call.<br><div class="step-pre">def f(items=None):\n    if items is None:\n        items = []\n    items.append(1)\n    return items</div></div>
<div class="keyword-box"><b>*args</b> = extra positional arguments as a <b>tuple</b>.<br><b>**kwargs</b> = extra keyword arguments as a <b>dict</b>.<br><b>Use when:</b> wrapper functions, decorators, flexible APIs.</div>
<div class="keyword-box"><b>lambda</b> = one-expression anonymous function.<br><b>Use when:</b> short <code>key=</code> or <code>map</code> callbacks.<br><b>Prefer def when:</b> more than one line or statements needed.</div>
<div class="keyword-box"><b>LEGB</b> = name lookup: Local → Enclosing → Global → Builtin.<br><b>Closures</b> = inner function remembers outer variables after outer returns.</div>
""",
    11: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>filter()</b> = keep only items that pass your test. "
        "Think of a <b>bouncer</b>: True means keep, False means skip. "
        "Use a small <code>def</code> for the test — easier than <code>None</code> or <code>strip</code>.</div>
<div class="keyword-box"><b>sorted()</b> = returns <b>new</b> sorted list; original unchanged.<br><b>.sort()</b> = sorts list <b>in place</b>; returns <code>None</code>.<br><b>Trap:</b> <code>x = lst.sort()</code> makes <code>x</code> None.</div>
<div class="keyword-box"><b>enumerate()</b> = gives <code>(index, value)</code> pairs — avoid manual <code>range(len())</code>.<br><b>zip()</b> = pair items from two sequences together.</div>
<div class="keyword-box"><b>isinstance()</b> = type check that respects inheritance — prefer over <code>type(x) == int</code>.</div>
<div class="keyword-box"><b>max()</b> / <b>min()</b> = largest / smallest item.<br><b>On dict:</b> compares keys by default — use <code>key=dict.get</code> for values.<br><b>Empty:</b> <code>max(items, default=0)</code> avoids ValueError.</div>
""",
    15: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>self</b> = the current object instance — like C# <code>this</code>, but you must write it explicitly as the first parameter.<br><b>Example:</b> <code>def __init__(self, name): self.name = name</code></div>
<div class="keyword-box"><b>__init__</b> = constructor — runs when object is created. Not a type name — initializes <code>self</code>.</div>
<div class="keyword-box"><b>__str__</b> = user-friendly print text. <b>__repr__</b> = developer/debug representation.<br><b>Rule:</b> <code>print(obj)</code> uses <code>__str__</code>.</div>
<div class="keyword-box"><b>MRO</b> = Method Resolution Order — which parent class method runs in multiple inheritance.<br><b>Check:</b> <code>ClassName.__mro__</code></div>
""",
    18: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>@decorator</b> = syntactic sugar: <code>@dec</code> above <code>def f</code> means <code>f = dec(f)</code>.<br><b>Use when:</b> add logging, timing, auth, route registration without changing <code>f</code>'s body.</div>
<div class="keyword-box"><b>@wraps(func)</b> = keep original function <code>__name__</code> and <code>__doc__</code> on the wrapper.<br><b>Always use</b> with custom decorators.</div>
""",
    16: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>@property</b> = attribute that runs code on get/set but looks like a field.<br><b>Use when:</b> validate on assign: <code>@score.setter</code>.<br><b>Looks like:</b> <code>obj.score = 5</code> — runs setter logic.</div>
<div class="keyword-box"><b>Descriptor</b> = object with <code>__get__</code> / <code>__set__</code> — powers <code>@property</code> internally.</div>
""",
    17: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>yield</b> = pause function, return one value, resume on next call.<br><b>return</b> = end function completely.<br><b>Generator</b> = any function containing <code>yield</code>.</div>
<div class="keyword-box"><b>Iterator protocol</b> = <code>__iter__</code> + <code>__next__</code> — <code>for</code> loops call these under the hood.<br><b>StopIteration</b> = signal that iteration ended.</div>
""",
    6: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Type hints</b> = documentation for humans and tools — <b>not enforced at runtime</b> by default.<br><b>Example:</b> <code>def f(x: int) -> str:</code></div>
<div class="keyword-box"><b>Optional[T]</b> = value can be <code>T</code> or <code>None</code>.<br><b>mypy</b> = static checker that catches type mistakes before you run the app.</div>
""",
    25: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>with</b> = guaranteed setup and cleanup — like C# <code>using</code>.<br><b>Works even on error</b> — file closes, lock releases.<br><div class="step-pre">with open("f.txt", encoding="utf-8") as f:\n    data = f.read()</div></div>
<div class="keyword-box"><b>encoding="utf-8"</b> = always set for text files on Windows — avoids garbled characters.</div>
""",
    19: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>try / except / else / finally</b><br><b>except:</b> handle error.<br><b>else:</b> runs if <b>no</b> exception in try (not the same as loop else!).<br><b>finally:</b> always runs — cleanup.</div>
<div class="keyword-box"><b>raise</b> = throw an exception. <b>raise ... from ...</b> = chain cause for debugging.<br><b>Custom Exception</b> = <code>class AppError(Exception): pass</code></div>
""",
    24: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>r"..."</b> raw string = backslashes are literal — use for regex patterns.<br><b>Example:</b> <code>r"\\d+"</code> not <code>"\\\\d+"</code>.</div>
<div class="keyword-box"><b>re.search</b> = find pattern anywhere. <b>re.match</b> = only at string start — common beginner trap.</div>
""",
    12: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>defaultdict(list)</b> = auto-creates empty list for missing keys — replaces <code>if key not in d: d[key]=[]</code> pattern.</div>
<div class="keyword-box"><b>namedtuple</b> = tuple with named fields — <code>Point(10,20).x</code> instead of <code>[0]</code>.<br><b>Counter</b> = count occurrences like a frequency table.</div>
<div class="keyword-box"><b>UserDict / UserList</b> = subclass-friendly wrappers — safer to extend than built-in <code>dict</code>/<code>list</code> directly.</div>
""",
    23: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>assert</b> = statement (pytest) or method (unittest) — fails test if condition is false.<br><b>pytest</b> = plain <code>assert x == 5</code> — no <code>self.assertEqual</code> boilerplate.</div>
<div class="keyword-box"><b>@patch</b> = replace real dependency (HTTP, DB) with fake during test — test one unit in isolation.</div>
""",
    20: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>GIL</b> (Global Interpreter Lock) = only one thread runs Python bytecode at a time in CPython.<br><b>Good for:</b> I/O (network, disk).<br><b>Bad for:</b> CPU-heavy math in threads — use <code>multiprocessing</code>.</div>
<div class="keyword-box"><b>Lock</b> = mutex — only one thread enters critical section at a time.<br><div class="step-pre">with lock:\n    shared_counter += 1</div></div>
""",
    26: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Context manager protocol</b> = <code>__enter__</code> at start of <code>with</code>, <code>__exit__</code> at end (even on error).<br><b>@contextmanager</b> = write one with <code>yield</code> between setup and teardown.</div>
""",
    21: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>async def</b> = defines a coroutine — does not run until awaited.<br><b>await</b> = pause until I/O completes — only valid inside <code>async def</code>.</div>
<div class="keyword-box"><b>asyncio.run(main())</b> = start the event loop once from synchronous code.<br><b>Trap:</b> never use <code>time.sleep</code> in async code — use <code>await asyncio.sleep</code>.</div>
""",
    27: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>venv</b> = isolated Python environment per project.<br><b>pip freeze &gt; requirements.txt</b> = pin exact versions for teammates and deployment.</div>
<div class="keyword-box"><b>pyenv</b> = pick Python <b>version</b> (3.10 vs 3.12). <b>venv</b> = pick project <b>packages</b>. Use both together.</div>
""",
    29: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Portfolio structure</b> = separate folders per domain (basics, web, data, voice).<br><b>Each project:</b> own <code>.venv</code> + <code>requirements.txt</code> + README entry point.</div>
""",
    30: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Module vs package</b> = one <code>.py</code> file vs folder with <code>__init__.py</code>.<br><b>pythonBasics/</b> = one runnable script per curriculum topic.</div>
""",
    31: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Jupyter notebook</b> = mix code + output + markdown cells — great for data exploration (pandas).</div>
""",
    32: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Django MVT</b> = Model-View-Template — batteries-included web framework.<br><b>DRF serializer</b> = validate and shape JSON like Pydantic in FastAPI.</div>
""",
    33: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Voice pipeline</b> = STT → LLM → TTS. <b>Pipecat</b> = framework for streaming audio processors (not JSON REST).</div>
""",
    34: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Thin routes, fat services</b> = HTTP layer only parses request; business logic lives in <code>services/</code>.<br><b>tests/</b> at project root — pytest discovers <code>test_*.py</code>.</div>
""",
    35: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>pass</b> (Python) has no C# keyword.<br><b>Closest:</b> empty <code>{ }</code> — valid block, does nothing.<br><b>Stub not ready:</b> <code>throw new NotImplementedException()</code> ≈ <code>raise NotImplementedError()</code>.<br><b>C# interface:</b> <code>void Save();</code> — no body. Python: <code>def save(self): pass</code>.</div>
<div class="keyword-box"><b>None</b> (Python) = <code>null</code> (C#). Test with <code>is None</code>, not <code>== None</code>.<br><b>Indentation</b> replaces braces. <b>venv</b> replaces global NuGet installs.<br><b>try/except</b> ≈ try/catch. <b>with</b> ≈ using.</div>
<div class="keyword-box"><b>self</b> = <code>this</code> — but you must declare it: <code>def method(self, x):</code>.<br><b>elif</b> = <code>else if</code>. <b>True/False</b> are capitalized (not <code>true</code>/<code>false</code>).</div>
""",
    4: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>PEP 8</b> = style convention, not syntax. <b>snake_case</b> functions, <b>PascalCase</b> classes, 4 spaces.<br><b>import this</b> = Zen of Python (PEP 20).</div>
<div class="keyword-box"><b>pyproject.toml</b> = modern project metadata + dependencies (PEP 621). Replaces setup.py for many projects.</div>
""",
    13: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>sys.getrefcount</b> = approximate reference count (debugging only).<br><b>gc.collect()</b> = force garbage collection — use when hunting circular-reference leaks.</div>
<div class="keyword-box"><b>del name</b> removes the binding — object lives if other references exist.<br><b>with</b> = deterministic cleanup for files/sockets (not every object).</div>
""",
    22: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>logging.getLogger(__name__)</b> = one logger per module — configure hierarchy from root.<br><b>logger.exception()</b> = ERROR level + full traceback — only inside <code>except</code>.</div>
<div class="keyword-box"><b>Lazy logging:</b> <code>logger.info("id=%s", user_id)</code> — do not use f-string if message may be filtered.</div>
""",
    14: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>BaseModel</b> = schema with validation on create.<br><b>model_validate(dict)</b> in, <b>model_dump()</b> out (Pydantic v2).</div>
<div class="keyword-box"><b>Field(ge=18)</b> = constraint at declaration.<br><b>@field_validator</b> = custom cross-field or format rules.</div>
""",
    28: """
<h3>Python keywords — deeper look</h3>
<div class="keyword-box"><b>Depends(get_db)</b> = inject scoped SQLAlchemy session per request — commit/close in generator <code>finally</code>.</div>
<div class="keyword-box"><b>response_model=UserRead</b> = Pydantic output schema — never return raw ORM without filtering fields.<br><b>from_attributes=True</b> = build schema from ORM row.</div>
""",
}


def keyword_deepdives_for(n: int) -> str:
    return KEYWORD_DEEPDIVES.get(n, "")
