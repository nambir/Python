"""Key terms explained tables for every slide in PythonTraining.html."""

from slide_csharp_popups import csharp_compare_btn

GLOSSARY: dict[int, str] = {
    1: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>CPython</td><td>The default Python implementation written in C — what you get when you install Python from python.org. It compiles <code>.py</code> to bytecode and runs it in a VM.</td><td><code>python --version</code></td></tr>
<tr><td>Bytecode</td><td>Intermediate instructions (not machine code) stored in <code>__pycache__/*.pyc</code>. The virtual machine executes these step by step.<br><br><b>What it looks like:</b> inside the <code>.pyc</code> file the bytes are binary (e.g. <code>64 00 00 00 …</code>). When you disassemble, you see readable opcodes like <code>LOAD_NAME</code>, <code>COMPARE_OP</code>.</td><td><code>1010110 0001001 …</code><br><code>LOAD_NAME score</code><br><code>COMPARE_OP &gt;=</code></td></tr>
<tr><td>Interpreter</td><td>The program that reads your <code>.py</code> file, builds bytecode, and executes it. In practice this is CPython.</td><td><code>python hello.py</code></td></tr>
<tr><td>Virtual machine</td><td>Inside the interpreter — the loop that runs bytecode instructions one by one.</td><td>VM box in the diagram</td></tr>
<tr><td>Dynamic typing</td><td>Variables not tied to one type — same name can hold int, then str. __CSHARP_DYNAMIC_BTN__</td><td><code>x = 5; x = "hi"</code></td></tr>
<tr><td>Indentation</td><td>Leading spaces (usually 4) define blocks — no <code>{ }</code> braces. __CSHARP_INDENT_BTN__</td><td><code>if True:</code> + indent</td></tr>
<tr><td>Duck typing</td><td><b>Class has a method</b> = normal. <b>Duck typing</b> = another function uses the object <b>without knowing the class name</b> — only the behavior (e.g. <code>.send()</code>). No interface / shared base required. __CSHARP_DUCK_BTN__</td><td><code>notify(channel, msg)</code></td></tr>
</table>""",
    2: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>PATH</td><td>Windows environment variable listing folders where the OS searches for executables.</td><td><code>python</code> found in PATH</td></tr>
<tr><td>pip</td><td><b>pip = Pip Installs Packages</b>. Python's package installer — downloads libraries from PyPI (like NuGet).</td><td><code>pip install pytest</code></td></tr>
<tr><td>python --version</td><td>Shows the Python interpreter version — the program that runs <code>.py</code> files.</td><td><code>Python 3.12.4</code></td></tr>
<tr><td>pip --version</td><td>Shows the pip installer version, its install path, and which Python version it is connected to.</td><td><code>pip 25.3 ... (python 3.12)</code></td></tr>
<tr><td>REPL</td><td>Read-Eval-Print Loop — interactive shell; type code, see result immediately.</td><td><code>python</code> then <code>2+2</code></td></tr>
<tr><td>Script</td><td>A <code>.py</code> file run from the command line in one shot.</td><td><code>python app.py</code></td></tr>
<tr><td>Interpreter path</td><td>Which Python executable your IDE uses — must match your venv.</td><td>Ctrl+Shift+P → Select Interpreter</td></tr>
<tr><td>py launcher</td><td>Windows <code>py</code> command picks among multiple installed Python versions.</td><td><code>py -3.12 script.py</code></td></tr>
<tr><td>__main__</td><td>Special module name when a file is run directly (not imported). Put this block at the <b>bottom</b> of the file. __CSHARP_MAIN_BTN__</td><td><code>if __name__ == "__main__":</code></td></tr>
<tr><td>Top-to-bottom</td><td>Python executes statements in order. A name must exist <b>before</b> you call it. __CSHARP_ORDER_BTN__</td><td><code>def Add</code> above <code>Add(1,2)</code></td></tr>
<tr><td>NameError</td><td>Raised when you use a name that is not defined yet — common if <code>def</code> is below the call. __CSHARP_ORDER_BTN__</td><td><code>name 'Add' is not defined</code></td></tr>
</table>""",
    5: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>list</td><td>Mutable sequence — grows with <code>append</code>. Homogeneous or heterogeneous OK.</td><td><code>cart.append(item)</code></td></tr>
<tr><td>Homogeneous list</td><td>All items same kind — all ints or all strings.</td><td><code>[90, 85]</code> / <code>["a","b"]</code></td></tr>
<tr><td>Heterogeneous list</td><td>Mixed types in one list — common for records / nested data. __CSHARP_HETERO_BTN__</td><td><code>[101, "SHIPPED", ["Google","Amazon"]]</code></td></tr>
<tr><td>Over-allocation</td><td>List reserves extra capacity. When full, reallocates a bigger array and copies pointers — <code>sizeof</code> jumps.</td><td><code>sys.getsizeof(lst)</code></td></tr>
<tr><td>Tuple</td><td>Fixed ordered record — GPS, RGB, return pairs, dict keys. Often leaner/faster than list for fixed data. __CSHARP_TUPLE_BTN__</td><td><code>(12.97, 80.22)</code></td></tr>
<tr><td>Immutable</td><td>Cannot change in place — no <code>t[0]=5</code>, no append.</td><td><code>TypeError</code> on assign</td></tr>
<tr><td>Mutable</td><td>Can change in place — lists grow/shrink.</td><td><code>items.append(4)</code></td></tr>
<tr><td>(ok, data) pattern</td><td>Function returns a 2-tuple: success flag + payload.</td><td><code>ok, user = fetch(10)</code></td></tr>
<tr><td>Hashable</td><td>Object can be a dict key / set member because its <code>hash()</code> never changes.<br><br><b>Why required:</b> dict uses hash like a locker number to find values fast. If the key mutated, the locker number would change and the value would be lost.<br><br><b>OK:</b> str, int, tuple, frozenset.<br><b>Blocked:</b> list, dict, set → <code>TypeError: unhashable type</code>. __CSHARP_HASHABLE_BTN__</td><td><code>prices[(12.97, 80.22)]</code></td></tr>
<tr><td>{} vs set()</td><td><code>{}</code> = empty <b>dict</b>. Empty set = <code>set()</code>. <code>{1,2}</code> = set. <code>{\"a\":1}</code> = dict.</td><td><code>d={}; s=set()</code></td></tr>
<tr><td>set / frozenset</td><td>Unique items. frozenset is immutable (OK as dict key).</td><td><code>frozenset({1,2})</code></td></tr>
</table>""",
    3: """
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
    7: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Arithmetic</td><td>Math operators: <code>+ - * / // % **</code></td><td><code>17 // 5</code> → 3</td></tr>
<tr><td>Floor division</td><td><code>//</code> divides and rounds down to integer.</td><td><code>7 // 2</code> → 3</td></tr>
<tr><td>Modulo</td><td><code>%</code> returns remainder after division.</td><td><code>17 % 5</code> → 2</td></tr>
<tr><td>Identity (is)</td><td>Same object in memory — not just equal value. __CSHARP_IS_BTN__</td><td><code>a is b</code></td></tr>
<tr><td>Equality (==)</td><td>Same value — different objects can be equal.</td><td><code>[1]==[1]</code> True</td></tr>
<tr><td>Membership (in)</td><td>Test if value exists in a collection.</td><td><code>5 in [1,5,9]</code></td></tr>
<tr><td>None</td><td><b>None</b> = no value (like C# <code>null</code>).<br><br><b>Empty?</b> <code>if x is None:</code><br><b>Has value?</b> <code>if x is not None:</code> — use <code>is</code> / <code>is not</code>, not <code>==</code>.<br><br><b>Why:</b> only one <code>None</code> object exists in Python. __CSHARP_NONE_BTN__</td><td><code>if x is not None:</code></td></tr>
<tr><td>Bitwise</td><td>Operators on binary digits: <code>&amp; | ^ ~ &lt;&lt; &gt;&gt;</code></td><td><code>5 &amp; 3</code> → 1</td></tr>
<tr><td>Assignment operators</td><td>Shorthand in-place update: <code>+= -= *=</code> etc.</td><td><code>n += 5</code></td></tr>
<tr><td>Walrus (:=)</td><td>Assign <b>and</b> use a value in one expression (Python 3.8+).<br><br><b>Without:</b> <code>n = len(x)</code> then <code>if n &gt; 0:</code><br><b>With:</b> <code>if (n := len(x)) &gt; 0:</code> — same <code>n</code> usable in the body.<br><br><b>Use when:</b> value needed in condition + body (avoid calling <code>len</code>/<code>input</code> twice).<br><b>Avoid:</b> every assignment — plain <code>=</code> is clearer.</td><td><code>if (n := len(x)) &gt; 0:</code></td></tr>
</table>""",
    8: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>if / elif / else</td><td>Branch execution based on True/False conditions.</td><td><code>if x &gt; 0:</code></td></tr>
<tr><td>for loop</td><td>Iterate over each item in a sequence (like C# foreach). __CSHARP_FOREACH_BTN__</td><td><code>for i in range(5):</code></td></tr>
<tr><td>while loop</td><td>Repeat while condition is True — watch for infinite loops.</td><td><code>while n &lt; 10:</code></td></tr>
<tr><td>break</td><td>Exit the loop immediately.</td><td><code>break</code> inside for</td></tr>
<tr><td>continue</td><td>Skip rest of <b>this</b> loop iteration — go to next.<br><br><b>Does NOT:</b> same as <code>pass</code> — <code>pass</code> does nothing but stays in same iteration.</td><td><code>continue</code></td></tr>
<tr><td>pass</td><td><b>pass = this block is intentionally empty for now.</b> A stub — define structure today, add real code later. Does nothing at runtime but satisfies syntax.<br><br><b>Use when:</b> stub <code>def</code>, empty <code>class</code>, custom <code>Exception</code>.<br><br><b>Later:</b> remove <code>pass</code> and write your logic.<br><br><b>Does NOT:</b> skip a loop — use <code>continue</code>. __CSHARP_PASS_BTN__</td><td><code>def todo(): pass</code></td></tr>
<tr><td>if True / if False</td><td><code>if True</code> always runs once (TODO stub). <code>if False</code> never runs (disable code temporarily).</td><td><code>if False: old_code()</code></td></tr>
<tr><td>for-else</td><td><code>else</code> on a loop runs only if the loop finished <b>without</b> <code>break</code>.<br><br><b>Not the same as:</b> <code>try/else</code> or <code>if/else</code>.<br><br><b>Use when:</b> search — report "not found" in <code>else</code>.</td><td>search pattern</td></tr>
<tr><td>range</td><td>Generates sequence of numbers — often used with for.</td><td><code>range(3)</code> → 0,1,2</td></tr>
</table>""",
    9: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>List comprehension</td><td>Build a list in one expression with for/if inside <code>[ ]</code>. __CSHARP_LINQ_BTN__</td><td><code>[n*n for n in range(6)]</code></td></tr>
<tr><td>Set comprehension</td><td>Build a unique set with <code>{ }</code> syntax.</td><td><code>{c.lower() for c in s}</code></td></tr>
<tr><td>Dict comprehension</td><td>Build key-value dict in one expression.</td><td><code>{w: len(w) for w in words}</code></td></tr>
<tr><td>Generator expression</td><td>Lazy comprehension with <code>( )</code> — yields one item at a time.</td><td><code>(n*n for n in range(10**6))</code></td></tr>
<tr><td>Lazy evaluation</td><td>Compute values only when needed — saves memory.</td><td><code>next(gen)</code></td></tr>
<tr><td>Filter clause</td><td>Optional <code>if</code> at end of comprehension to keep matching items.</td><td><code>if n % 2 == 0</code></td></tr>
</table>""",
    10: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Pure function</td><td>Same args → same result; no side effects / no hidden I/O (FP).</td><td><code>def add(x,y): return x+y</code></td></tr>
<tr><td>First-class function</td><td>Functions are values — assign, pass, return them.</td><td><code>fn = str.upper</code></td></tr>
<tr><td>Higher-order function</td><td>Takes or returns a function.</td><td><code>sorted(xs, key=fn)</code></td></tr>
<tr><td>def</td><td>Keyword to define a function.</td><td><code>def greet(name):</code></td></tr>
<tr><td>Parameter</td><td>Variable in function definition receiving a value.</td><td><code>def f(x):</code></td></tr>
<tr><td>Argument</td><td>Actual value passed when calling the function.</td><td><code>greet("Ali")</code></td></tr>
<tr><td>Default argument</td><td>Parameter value used if caller omits it.</td><td><code>greeting="Hello"</code></td></tr>
<tr><td>Mutable default trap</td><td><b>Never</b> <code>def f(items=[])</code> — same list reused every call.<br><br><b>Fix:</b> <code>def f(items=None): items = items or []</code><br><br><b>Why:</b> default objects are created once at function definition time. __CSHARP_MUTABLE_DEF_BTN__</td><td><code>def f(x=None):</code></td></tr>
<tr><td>*args</td><td>Collects extra positional arguments as a tuple.</td><td><code>def f(*args):</code></td></tr>
<tr><td>**kwargs</td><td>Collects extra keyword arguments as a dict.</td><td><code>def f(**kw):</code></td></tr>
<tr><td>Lambda</td><td>Anonymous one-line function. __CSHARP_LAMBDA_BTN__</td><td><code>lambda x: x*2</code></td></tr>
<tr><td>Closure</td><td>Inner function remembering variables from outer scope.</td><td>counter pattern</td></tr>
<tr><td>LEGB</td><td>Scope lookup order: Local → Enclosing → Global → Builtin.
  Same name in nested scopes = <b>different variables</b> (different bindings).</td><td><code>print(x)</code> in <code>inner</code></td></tr>
<tr><td>id()</td><td>Object identity — unique int for that object while alive
  (in CPython, related to memory address). Same <code>id</code> ⇒ same object (<code>is</code>).</td><td><code>id(x)</code></td></tr>
</table>

<h3 style="margin-top:16px">LEGB — 3 scopes, 3 variables (not one)</h3>
<p style="font-size:13px;color:#475569;margin:0 0 8px;line-height:1.45">
  When each level does <code>x = ...</code>, Python creates <b>three separate bindings</b>
  that only share the name <code>x</code>. They are <b>not</b> one variable reused.
</p>
<table class="data-tbl" style="margin-top:4px">
<tr><th>Scope</th><th>Binding</th><th>Value</th></tr>
<tr><td><b>Global</b> (module)</td><td><code>x</code></td><td><code>"global"</code></td></tr>
<tr><td><b>Enclosing</b> (<code>outer</code>)</td><td><code>x</code></td><td><code>"enclosing"</code></td></tr>
<tr><td><b>Local</b> (<code>inner</code>)</td><td><code>x</code></td><td><code>"local"</code></td></tr>
</table>
<div class="step-pre" style="margin-top:10px">x = "global"                 # binding 1 — global

def outer():
    x = "enclosing"          # binding 2 — enclosing (outer's local)
    def inner():
        x = "local"          # binding 3 — local to inner
        print(x)             # "local" — LEGB finds Local first
        print("inner id:", id(x))
    print("outer id:", id(x))
    inner()

print("global id:", id(x))
outer()
# Three different id() values → three different objects</div>
<p style="font-size:12px;color:#334155;margin:8px 0 0;line-height:1.45">
  <b>Takeaway:</b> assignment inside a function makes that name <b>local to that function</b>
  (unless <code>global</code> / <code>nonlocal</code>).
  <code>id()</code> answers “which object?” — different ids mean different objects in memory.
</p>
""",
    11: """
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
<tr><td>max / min</td><td>Largest / smallest item; optional <code>key=</code> for custom order.</td><td><code>max(scores, key=scores.get)</code></td></tr>
</table>""",
    15: """
<h3>Key terms explained __CSHARP_OOP_BTN__</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Class</td><td>Blueprint for objects — attributes + methods.</td><td><code>class Dog:</code></td></tr>
<tr><td>Object</td><td>Instance of a class created at runtime.</td><td><code>Dog("Rex")</code></td></tr>
<tr><td>__init__</td><td>Constructor — runs when object is created; sets <code>self</code>. __CSHARP_INIT_BTN__</td><td><code>def __init__(self, name):</code></td></tr>
<tr><td>self</td><td>Reference to current instance (like C# <code>this</code>). __CSHARP_SELF_BTN__</td><td><code>self.name = name</code></td></tr>
<tr><td>Inheritance</td><td>Child class gets parent methods — override to customize. __CSHARP_INHERIT_BTN__</td><td><code>class Dog(Animal):</code></td></tr>
<tr><td>Polymorphism</td><td>Same method call, different behavior per class.</td><td><code>pet.speak()</code></td></tr>
<tr><td>Encapsulation</td><td>Hide internal state — <code>_prefix</code> convention, <code>@property</code>.</td><td><code>self._balance</code></td></tr>
<tr><td>MRO</td><td>Method Resolution Order — which parent method runs first.</td><td><code>Dog.__mro__</code></td></tr>
</table>

<h3 style="margin-top:16px">Same name: class vs function vs method</h3>
<p style="font-size:13px;color:#475569;margin:0 0 8px;line-height:1.45">
  <code>Toy("ball")</code> looks like a function call, but <code>Toy</code> is normally a <b>class</b>
  (creates an object). If you later define a <b>function</b> with the same name, that name is
  <b>shadowed</b> — Python keeps only the <b>last</b> binding. A <b>method</b> named <code>Toy</code>
  inside the class does <b>not</b> replace the class.
</p>
<div class="mc-row">
  <div class="mc-col mc-good">
    <span class="mc-lbl">Class only — Toy("ball") creates an object</span>
    <div class="step-pre">class Toy:
    def __init__(self, name):
        self.name = name

a = Toy("ball")     # class call → new object
print(a.name)       # ball</div>
  </div>
  <div class="mc-col mc-bad">
    <span class="mc-lbl">Function reuses name Toy — class is hidden</span>
    <div class="step-pre">class Toy:
    def __init__(self, name):
        self.name = name

def Toy(name):              # same name — shadows the class
    return f"fn:{name}"

a = Toy("ball")             # calls the FUNCTION
print(a)                    # fn:ball  (not a Toy object)</div>
  </div>
</div>
<div class="step-pre" style="margin-top:10px"># Method named Toy — OK; does NOT replace the class
class Toy:
    def __init__(self, name):
        self.name = name

    def Toy(self):                  # unusual name, but allowed
        return "method Toy"

a = Toy("ball")                     # still creates the object
print(a.Toy())                      # method Toy

# Best practice: PascalCase for classes only
# use make_toy() for a helper — never shadow the class name</div>
<table class="data-tbl" style="margin-top:10px">
<tr><th>Situation</th><th>What <code>Toy(...)</code> does</th></tr>
<tr><td>Only the class exists</td><td>Creates a <b>Toy object</b></td></tr>
<tr><td>A function later uses the name <code>Toy</code></td><td>Calls that <b>function</b> (class hidden)</td></tr>
<tr><td>Method <code>def Toy(self)</code></td><td>Class still works; call method with <code>a.Toy()</code></td></tr>
</table>
""",
    18: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Decorator</td><td>Function wrapping another function to add behavior. __CSHARP_DECORATOR_BTN__</td><td><code>@timer</code></td></tr>
<tr><td>@syntax</td><td>Syntactic sugar — <code>@dec</code> above <code>def f</code> means <code>f = dec(f)</code>.</td><td><code>@app.get("/")</code></td></tr>
<tr><td>Wrapper</td><td>Inner function that calls the original and adds logic.</td><td><code>def wrapper(*a,**k):</code></td></tr>
<tr><td>@wraps</td><td>Preserves original function name and docstring metadata.</td><td><code>@wraps(fn)</code></td></tr>
<tr><td>Stacking</td><td>Multiple decorators applied bottom-up.</td><td><code>@a @b def f</code></td></tr>
<tr><td>Higher-order function</td><td>Function that takes or returns another function.</td><td>decorator pattern</td></tr>
</table>""",
    16: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Descriptor</td><td>Helper object (security guard) that controls how an attribute is read/written/deleted via <code>__get__</code>, <code>__set__</code>, <code>__delete__</code>.</td><td><code>price = PositiveNumber()</code></td></tr>
<tr><td>@property</td><td>Built-in <b>data</b> descriptor — managed attribute. __CSHARP_PROPERTY_BTN__</td><td><code>@property def age:</code></td></tr>
<tr><td>Non-data descriptor</td><td>Only <code>__get__</code> — write can bypass (instance var wins).</td><td>read helper only</td></tr>
<tr><td>Data descriptor</td><td><code>__get__</code> + <code>__set__</code> — every write goes through the helper.</td><td>can validate assignments</td></tr>
<tr><td>Getter</td><td>Method called when attribute is read.</td><td><code>def temp(self): return self._t</code></td></tr>
<tr><td>Setter</td><td>Method called when attribute is assigned — validate here.</td><td><code>@temp.setter</code></td></tr>
<tr><td>Managed attribute</td><td>Looks like field, runs code on get/set.</td><td><code>c.temp = 25</code></td></tr>
</table>""",
    17: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Lazy iterator</td><td>Produces values on demand — does not store the whole sequence (Real Python / PEP 255).</td><td><code>for row in csv_reader(path)</code></td></tr>
<tr><td>Generator</td><td>Function using <code>yield</code> — returns a lazy iterator. __CSHARP_YIELD_BTN__</td><td><code>def gen(): yield 1</code></td></tr>
<tr><td>yield vs return</td><td><code>yield</code> pauses and continues; <code>return</code> ends with one value. __CSHARP_YIELD_BTN__</td><td><code>yield row</code></td></tr>
<tr><td>Generator expression</td><td>Lazy comprehension with <code>( )</code> — like listcomp but no full list.</td><td><code>(n*n for n in range(10**6))</code></td></tr>
<tr><td>MemoryError risk</td><td>Loading entire huge file into a list can crash; yield one line instead.</td><td><code>f.read().split()</code> bad</td></tr>
<tr><td>Iterator / Iterable</td><td>Iterator: <code>__next__</code>. Iterable: can call <code>iter()</code> / use in <code>for</code>.</td><td><code>next(it)</code></td></tr>
<tr><td>StopIteration</td><td>Raised when iterator has no more items.</td><td>end of for-loop</td></tr>
<tr><td>itertools</td><td>Efficient iterator tools — chain, islice, groupby.</td><td><code>itertools.chain</code></td></tr>
</table>""",
    6: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Type hint</td><td>Annotation showing expected types — not enforced at runtime. __CSHARP_HINTS_BTN__</td><td><code>name: str</code></td></tr>
<tr><td>Return type</td><td><code>-&gt;</code> annotation on what function returns.</td><td><code>-&gt; str:</code></td></tr>
<tr><td>Optional</td><td>Value can be the type or <code>None</code>.</td><td><code>Optional[int]</code></td></tr>
<tr><td>Union</td><td>Value can be one of several types.</td><td><code>Union[int, str]</code></td></tr>
<tr><td>mypy</td><td>Command-line type checker (<code>pip install mypy</code>). Does <b>not</b> run with <code>python</code> automatically.<br><br><b>Input:</b> <code>mypy app.py</code> &nbsp; <b>Output:</b> type error lines (program not executed).<br><br><b>Input:</b> <code>python app.py</code> &nbsp; <b>Output:</b> program runs; hints ignored (e.g. may print <code>Charged 100 91</code>).</td><td><code>mypy app.py</code></td></tr>
<tr><td>Generic</td><td>Type parameterized by another type — <code>List[int]</code>.</td><td><code>Dict[str, int]</code></td></tr>
</table>""",
    25: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>open()</td><td>Built-in to open files — always specify <code>encoding="utf-8"</code> for text.</td><td><code>open("f.txt","r")</code></td></tr>
<tr><td>Mode</td><td><code>r</code> read, <code>w</code> write (overwrite), <code>a</code> append, <code>rb</code> binary.</td><td><code>"w"</code></td></tr>
<tr><td>with statement</td><td>Context manager — auto-closes file even on error. __CSHARP_WITH_BTN__</td><td><code>with open(...) as f:</code></td></tr>
<tr><td>JSON</td><td>Text format for structured data — <code>json.loads/dumps</code>.</td><td><code>json.dumps(data)</code></td></tr>
<tr><td>pathlib</td><td>Object-oriented file paths — cleaner than string concat.</td><td><code>Path("a")/"b"</code></td></tr>
<tr><td>encoding</td><td>Character set for text files — UTF-8 handles all languages.</td><td><code>encoding="utf-8"</code></td></tr>
</table>""",
    19: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>try / except</td><td>Attempt code; catch specific errors if they occur (like C# catch). __CSHARP_TRY_BTN__</td><td><code>except ValueError:</code></td></tr>
<tr><td>else</td><td>On <b>try</b>: runs if try block had <b>no</b> exception.<br><br><b>Not the same as:</b> loop <code>for-else</code> (runs if no <code>break</code>).</td><td><code>try: ... else:</code></td></tr>
<tr><td>finally</td><td>Always runs — used for cleanup (close file, release lock).</td><td><code>finally: close()</code></td></tr>
<tr><td>raise</td><td>Throw an exception intentionally.</td><td><code>raise ValueError("bad")</code></td></tr>
<tr><td>Custom exception</td><td>Your own error class inheriting <code>Exception</code>.</td><td><code>class AppError(Exception):</code></td></tr>
<tr><td>Traceback</td><td>Stack trace showing where error occurred.</td><td>printed on crash</td></tr>
</table>""",
    24: r"""
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
    12: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Counter</td><td><b>Counter</b> = dict subclass counting hashable items — one-line frequency tally. __CSHARP_COUNTER_BTN__</td><td><code>Counter("hello")</code></td></tr>
<tr><td>defaultdict</td><td><b>defaultdict</b> = dict with factory for missing keys — no <code>KeyError</code>. __CSHARP_DEFAULTDICT_BTN__</td><td><code>defaultdict(list)</code></td></tr>
<tr><td>deque</td><td><b>deque</b> = double-ended queue — fast append/pop at both ends. <code>maxlen</code> optional. __CSHARP_DEQUE_BTN__</td><td><code>deque()</code> / <code>deque(maxlen=2)</code></td></tr>
<tr><td>namedtuple</td><td><b>namedtuple</b> = tuple with named fields — lightweight record. __CSHARP_NAMEDTUPLE_BTN__</td><td><code>Point(10, 20).x</code></td></tr>
<tr><td>ChainMap</td><td><b>ChainMap</b> = stack dicts — lookup tries each in order (<b>first match wins</b>). Does not merge copies. __CSHARP_CHAINMAP_BTN__</td><td><code>ChainMap(Dict1, Dict2)</code></td></tr>
<tr><td>OrderedDict</td><td><b>OrderedDict</b> = dict remembering insertion order (<b>regular dict since 3.7</b>). __CSHARP_ORDEREDDICT_BTN__</td><td>legacy code</td></tr>
<tr><td>UserDict / UserList / UserString</td><td>Subclass-friendly wrappers. Real data lives in <code>.data</code>.
  Override methods (e.g. <code>__setitem__</code>) safely — unlike subclassing built-in <code>dict</code>/<code>list</code>.</td>
  <td><code>class D(UserDict): ...</code></td></tr>
</table>""",
    23: """
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
    26: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Context manager</td><td>Object defining setup/teardown for <code>with</code> block.</td><td><code>with open(f):</code></td></tr>
<tr><td>__enter__</td><td>Called when entering <code>with</code> — setup, return resource.</td><td>open file</td></tr>
<tr><td>__exit__</td><td>Called when leaving <code>with</code> — cleanup, even on error.</td><td>close file</td></tr>
<tr><td>@contextmanager</td><td>Decorator making generator function into context manager.</td><td><code>yield</code> splits setup/teardown</td></tr>
<tr><td>with statement</td><td>Guarantees cleanup — preferred over manual try/finally. __CSHARP_WITH_BTN__</td><td><code>with lock:</code></td></tr>
</table>""",
    21: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>async def</td><td>Defines a coroutine function — not run until awaited. __CSHARP_ASYNC_BTN__</td><td><code>async def fetch():</code></td></tr>
<tr><td>await</td><td>Pause coroutine until async operation completes. __CSHARP_ASYNC_BTN__</td><td><code>await asyncio.sleep(1)</code></td></tr>
<tr><td>Coroutine</td><td>Cooperative task managed by event loop.</td><td>async function</td></tr>
<tr><td>Event loop</td><td>Schedules and runs coroutines — <code>asyncio.run()</code> starts it.</td><td><code>asyncio.run(main())</code></td></tr>
<tr><td>asyncio.gather</td><td>Run multiple coroutines concurrently, wait for all.</td><td><code>await gather(a(), b())</code></td></tr>
<tr><td>Concurrency</td><td>Multiple tasks making progress — not same as parallel CPU.</td><td>async HTTP calls</td></tr>
</table>""",
    27: r"""
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>venv</td><td>Virtual environment — isolated Python + packages per project. __CSHARP_VENV_BTN__</td><td><code>python -m venv .venv</code></td></tr>
<tr><td>activate</td><td>Switch shell to use venv's Python and pip.</td><td><code>.venv\Scripts\activate</code></td></tr>
<tr><td>pip freeze</td><td>Export installed packages with exact versions.</td><td><code>pip freeze &gt; requirements.txt</code></td></tr>
<tr><td>requirements.txt</td><td>List of dependencies for <code>pip install -r</code>.</td><td>one package per line</td></tr>
<tr><td>pyenv</td><td>Tool to install/switch multiple Python versions on one machine.</td><td><code>pyenv install 3.12</code></td></tr>
<tr><td>.gitignore</td><td>Exclude <code>.venv/</code> from git — never commit virtual envs.</td><td><code>.venv/</code> in file</td></tr>
</table>""",
    29: """
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
    30: """
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
    31: """
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
    32: """
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
    33: """
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
    34: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Separation of concerns</td><td>Split routes, services, models, tests into folders.</td><td>api/ services/ tests/</td></tr>
<tr><td>Entry point</td><td>Main file starting the app — <code>main.py</code> or <code>manage.py</code>.</td><td><code>uvicorn main:app</code></td></tr>
<tr><td>DTO / Schema</td><td>Data Transfer Object — validates API input/output.</td><td>Pydantic, DRF Serializer</td></tr>
<tr><td>Service layer</td><td>Business logic separated from HTTP handlers.</td><td>services/user.py</td></tr>
<tr><td>.env</td><td>Environment variables for secrets — never commit real keys.</td><td><code>DATABASE_URL</code></td></tr>
</table>""",
    35: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Static typing</td><td>C# declares types at compile time — <code>int x = 5</code>. __CSHARP_HINTS_BTN__</td><td>C# variable</td></tr>
<tr><td>Dynamic typing</td><td>Python assigns without type declaration. __CSHARP_DYNAMIC_BTN__</td><td><code>x = 5</code></td></tr>
<tr><td>Interface</td><td>C# contract — Python uses ABC or duck typing instead. __CSHARP_DUCK_BTN__</td><td><code>interface IRepo</code></td></tr>
<tr><td>Null vs None</td><td>C# <code>null</code> — <code>== null</code> / <code>!= null</code> (or <code>is null</code> / <code>is not null</code>).</td><td>Python <code>None</code> — <code>is None</code> / <code>is not None</code>. __CSHARP_NONE_BTN__</td></tr>
<tr><td>pass</td><td>No keyword — use empty <code>{ }</code> for a stub block.<br><br><b>Stronger stub:</b> <code>throw new NotImplementedException()</code>.<br><br><b>Interfaces:</b> declare method without body — no pass needed. __CSHARP_PASS_BTN__</td><td><code>pass</code> = block intentionally empty for now.<br><br><b>Stronger stub:</b> <code>raise NotImplementedError()</code>.</td></tr>
<tr><td>this vs self</td><td><code>this</code> — implicit in instance methods.</td><td><code>self</code> — explicit first parameter. __CSHARP_SELF_BTN__</td></tr>
<tr><td>using vs with</td><td><code>using (var f = ...)</code> — auto dispose.</td><td><code>with open(...) as f:</code> — context manager. __CSHARP_WITH_BTN__</td></tr>
<tr><td>try/catch vs try/except</td><td>Same concept — different keyword in Python. __CSHARP_TRY_BTN__</td><td><code>except ValueError:</code></td></tr>
<tr><td>NuGet vs pip</td><td>C# package manager vs Python package installer. __CSHARP_VENV_BTN__</td><td><code>pip install</code></td></tr>
<tr><td>Task vs coroutine</td><td>C# <code>async Task</code> vs Python <code>async def</code> coroutine. __CSHARP_ASYNC_BTN__</td><td><code>await</code> both</td></tr>
</table>""",
    4: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>PEP</td><td>Python Enhancement Proposal — design doc for language/stdlib.</td><td>PEP 8</td></tr>
<tr><td>PEP 8</td><td>Official style guide — indent, naming, imports.</td><td><code>snake_case</code></td></tr>
<tr><td>PEP 257</td><td>Docstring conventions for modules and functions.</td><td><code>'''Load config.'''</code></td></tr>
<tr><td>Zen of Python</td><td>PEP 20 — guiding principles.</td><td><code>import this</code></td></tr>
<tr><td>pyproject.toml</td><td>Modern project config (PEP 621).</td><td><code>[project]</code></td></tr>
<tr><td>Linter</td><td>Automated style/error checker.</td><td>ruff, flake8</td></tr>
</table>""",
    13: """
<h3>Key terms explained __CSHARP_MEMORY_BTN__</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Reference counting</td><td>Count how many names point to a toy. When count is 0, free it now.</td><td><code>sys.getrefcount</code></td></tr>
<tr><td>Garbage collector</td><td>Extra cleaner for circles (A→B→A) that refcount cannot free alone.</td><td><code>gc.collect()</code></td></tr>
<tr><td>Generation (GC)</td><td>Young vs old buckets — young toys are checked more often (0, 1, 2).</td><td>gen 0, 1, 2</td></tr>
<tr><td>weakref</td><td><b>Soft look</b> at an object. Does <b>not</b> keep it alive.
  Later <code>soft_ref()</code> returns the object or <code>None</code> if it was freed. Good for caches.</td><td><code>weakref.ref(obj)</code></td></tr>
<tr><td>del</td><td><b>Drop a name</b> (strong reference −1). If count hits 0 → free now.
  Does not always free circles (A↔B) — then GC is needed.</td><td><code>del x</code></td></tr>
<tr><td>gc.collect()</td><td><b>Run cyclic GC now</b> (usually automatic). Frees unreachable circles
  that refcount alone cannot. Returns how many objects were collected.</td><td><code>gc.collect()</code></td></tr>
</table>
<p class="gloss-why" style="font-size:13px;color:#475569;margin:8px 0 0;line-height:1.45">
  <b>Why so many words?</b> CPython uses <b>refcount + cyclic GC + weakref</b> together.
  C# mostly says “the GC” (+ <code>WeakReference</code> / <code>using</code>). Open <b>C# Comparison</b> for a term-by-term map
  and full detail on <code>weakref.ref</code>, <code>del</code>, and <code>gc.collect()</code>.
</p>

<h3 style="margin-top:16px">Strong name &amp; strong reference</h3>
<p style="font-size:13px;color:#475569;margin:0 0 10px;line-height:1.45">
  A <b>strong reference</b> is any normal hold that adds <b>+1</b> to the object’s refcount
  (keeps the toy alive). A <b>strong name</b> is the usual case: a variable like <code>a</code>
  that points at the object. Other strong holds work the same way — dict slots, attributes, list items.
  <code>del</code> (or rebinding) drops that hold (−1). When the count hits <b>0</b>, the object is freed <b>now</b>
  (unless a circle keeps counts above 0).
</p>
<table class="data-tbl" style="margin-top:4px">
<tr><th>#</th><th>Scenario</th><th>What is the strong hold?</th><th>What <code>del</code> does</th><th>Freed when?</th></tr>
<tr>
  <td>1</td>
  <td><b>Dict</b></td>
  <td>Value stored under a key — <code>d["ball"] = toy</code> is a strong hold on <code>toy</code>.</td>
  <td><code>del d["ball"]</code> drops that slot (−1).</td>
  <td>If that was the last strong hold → free <b>now</b> (refcount).</td>
</tr>
<tr>
  <td>2</td>
  <td><b>Attribute</b></td>
  <td><code>box.item = toy</code> — the attribute is a strong hold on <code>toy</code>.</td>
  <td><code>del box.item</code> (or <code>box.item = None</code>) drops it (−1).</td>
  <td>Last strong hold gone → free <b>now</b>.</td>
</tr>
<tr>
  <td>3</td>
  <td><b>Big object</b></td>
  <td>A variable name holds a large value — <code>huge = load_report()</code>.</td>
  <td><code>del huge</code> drops the name early so RAM can shrink sooner.</td>
  <td>If nothing else points at it → free <b>now</b>. No <code>gc.collect()</code> needed.</td>
</tr>
<tr>
  <td>4</td>
  <td><b>Circular ref</b></td>
  <td><code>a.other = b</code> and <code>b.other = a</code> — each attribute is still a <b>strong</b> hold.</td>
  <td><code>del a, b</code> drops the <i>names</i>, but A↔B attributes may still hold each other.</td>
  <td>Refcount may stay &gt; 0 → need <b>cyclic GC</b> (<code>gc.collect()</code> or automatic).</td>
</tr>
</table>
<div class="step-pre" style="margin-top:10px"># 1) Dict — strong hold in a slot
d = {"ball": obj}
del d["ball"]            # slot gone → obj freed if nothing else holds it

# 2) Attribute — strong hold on a field
box.item = obj
del box.item             # attribute gone → same idea

# 3) Big object — drop the name when finished
huge = load_report()     # strong name holds a large value
# ... use huge ...
del huge                 # free early (if last strong hold)

# 4) Circular ref — strong holds point at each other
a.other = b; b.other = a
del a, b                 # names gone, but circle may remain → gc.collect()</div>
<p style="font-size:12px;color:#334155;margin:8px 0 0;line-height:1.45">
  <b>Picture:</b> a strong hold = hugging the toy.
  Dict key, attribute, and variable name are all hugs.
  <code>del</code> = let go. Soft look (<code>weakref</code>) = peek without hugging.
</p>

<h4 style="margin:14px 0 6px;color:#1a1a2e">Strong reference vs weak reference</h4>
<p style="font-size:13px;color:#475569;margin:0 0 8px;line-height:1.45">
  <b>Hug</b> = strong reference (keeps the object alive).
  <b>Peek</b> = weak reference (<code>weakref.ref</code> — look later, do <b>not</b> keep it alive by itself).
  There is no special “peek with hug” API — hugging <b>is</b> a normal assignment like <code>b = a</code>.
</p>
<div class="mc-row">
  <div class="mc-col mc-good">
    <span class="mc-lbl">Strong ref — peek WITH hugging</span>
    <div class="step-pre">a = Toy("ball")     # hug #1 (strong name)
b = a               # hug #2 — refcount +1
d["x"] = a          # hug #3 — also strong
box.item = a        # hug #4 — also strong

# each of these KEEPS the toy alive
del a, b
del d["x"]
del box.item        # last hug gone → toy freed now</div>
    <p style="font-size:12px;line-height:1.4;margin:8px 0 0;color:#166534">
      <b>Effect:</b> adds <b>+1</b> to refcount. Object stays in memory while any strong hold remains.
    </p>
  </div>
  <div class="mc-col mc-bad">
    <span class="mc-lbl">Weak ref — peek WITHOUT hugging</span>
    <div class="step-pre">import weakref

a = Toy("ball")              # only strong hug
soft_ref = weakref.ref(a)    # peek — NO strong +1

print(soft_ref())            # Toy ball — still alive (because of a)
del a                        # last hug gone
print(soft_ref())            # None — soft look could not save it</div>
    <p style="font-size:12px;line-height:1.4;margin:8px 0 0;color:#991b1b">
      <b>Effect:</b> does <b>not</b> keep the object alive. Later <code>soft_ref()</code> → object or <code>None</code>.
    </p>
  </div>
</div>
<table class="data-tbl" style="margin-top:10px">
<tr><th></th><th>Strong reference (hug)</th><th>Weak reference (peek)</th></tr>
<tr>
  <td><b>How you make it</b></td>
  <td><code>b = a</code>, <code>d["k"] = a</code>, <code>box.item = a</code></td>
  <td><code>soft_ref = weakref.ref(a)</code></td>
</tr>
<tr>
  <td><b>Refcount</b></td>
  <td><b>+1</b> (keeps object alive)</td>
  <td><b>No</b> strong +1</td>
</tr>
<tr>
  <td><b>Picture</b></td>
  <td>Hug the toy</td>
  <td>Peek / look without hugging</td>
</tr>
<tr>
  <td><b>After last strong hold is gone</b></td>
  <td>Object can be freed (refcount 0)</td>
  <td><code>soft_ref()</code> returns <code>None</code></td>
</tr>
<tr>
  <td><b>Typical use</b></td>
  <td>Normal everyday variables, dicts, attributes</td>
  <td>Caches / maps that must not pin memory forever</td>
</tr>
<tr>
  <td><b>C# twin</b></td>
  <td>Normal variable / field reference</td>
  <td><code>WeakReference&lt;T&gt;</code></td>
</tr>
</table>

<p style="font-size:13px;color:#475569;margin:12px 0 8px;line-height:1.45">
  <b>Is <code>del</code> mandatory on every variable?</b> <b>No.</b>
  When a function ends, local names disappear <b>automatically</b> — same idea as <code>del</code> for those names.
  Do <b>not</b> sprinkle <code>del</code> through normal code. Use it when you need to remove a
  <b>dict key</b> / <b>attribute</b>, or free a <b>big object early</b> inside a long function.
</p>
<div class="mc-row">
  <div class="mc-col mc-good">
    <span class="mc-lbl">del optional — normal everyday code</span>
    <div class="step-pre">def load():
    huge = load_report()   # strong name
    return process(huge)
# function ends → huge gone automatically
# no del needed

def greet(name):
    msg = f"Hi {name}"
    return msg
# msg disappears when greet returns</div>
    <p style="font-size:12px;line-height:1.4;margin:8px 0 0;color:#166534">
      <b>Rule:</b> short functions / locals that go out of scope —
      Python already drops the strong names. Skip <code>del</code>.
    </p>
  </div>
  <div class="mc-col mc-bad">
    <span class="mc-lbl">del useful — when you really need it</span>
    <div class="step-pre"># 1) Remove a dict key / attribute (real job)
del d["temp"]
del box.scratch

# 2) Free a big object EARLY in a long function
def overnight_batch(rows):
    huge = load_all(rows)   # still inside the function
    summary = summarize(huge)
    del huge                # done with data — free RAM now
    # ... more work that takes a long time ...
    return summary</div>
    <p style="font-size:12px;line-height:1.4;margin:8px 0 0;color:#991b1b">
      <b>Rule:</b> still in the same scope, but finished with a large value —
      or you must delete a key/attribute. Then <code>del</code> helps.
    </p>
  </div>
</div>
<table class="data-tbl" style="margin-top:10px">
<tr><th></th><th>del optional (usual)</th><th>del useful / needed</th></tr>
<tr>
  <td><b>When</b></td>
  <td>Function ends; name falls out of scope</td>
  <td>Remove key/attribute, or free early in a long function</td>
</tr>
<tr>
  <td><b>Who drops the hold?</b></td>
  <td>Python — automatically</td>
  <td>You — with <code>del</code> (or rebind / set to <code>None</code>)</td>
</tr>
<tr>
  <td><b>Everyday scripts / APIs?</b></td>
  <td>Yes — this is the default</td>
  <td>Only for keys, attributes, or big early cleanup</td>
</tr>
<tr>
  <td><b>Interview line</b></td>
  <td colspan="2"><code>del</code> is <b>optional</b>. Scope end drops strong names.
  Use <code>del</code> for keys/attributes or to free a large object before a long function finishes.</td>
</tr>
</table>

<h3 style="margin-top:16px">weakref · del · gc.collect — two stories compared</h3>
<p style="font-size:13px;color:#475569;margin:0 0 10px;line-height:1.45">
  Same three tools. Different outcome depending on whether objects hold each other in a <b>circle</b>.
</p>

<div class="mc-row">
  <div class="mc-col mc-good">
    <span class="mc-lbl">A) No circle (simple case)</span>
    <div class="step-pre">import gc, weakref

class Toy:
    def __init__(self, name):
        self.name = name

a = Toy("ball")
soft_ref = weakref.ref(a)   # soft look
print(soft_ref())           # Toy ball — still alive

del a                    # drop the only strong name
print(soft_ref())           # None — freed NOW by refcount

n = gc.collect()         # almost nothing left for GC
print(n)                 # often 0</div>
    <p style="font-size:12px;line-height:1.4;margin:8px 0 0;color:#166534">
      <b>What happened:</b> After <code>del a</code>, refcount hit 0 → object gone immediately.
      <code>gc.collect()</code> was not needed to free it.
    </p>
  </div>
  <div class="mc-col mc-bad">
    <span class="mc-lbl">B) Circle A ↔ B (hard case)</span>
    <div class="step-pre">import gc, weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

a = Node("A")
b = Node("B")
a.other = b
b.other = a              # circle A ↔ B

soft_ref = weakref.ref(a)   # soft look
print(soft_ref())           # Node A — still alive

del a, b                 # drop strong names; circle may remain
print(soft_ref())           # may still be Node A

n = gc.collect()         # cyclic GC breaks the circle
print(n, soft_ref())        # collected count; soft_ref() → None</div>
    <p style="font-size:12px;line-height:1.4;margin:8px 0 0;color:#991b1b">
      <b>What happened:</b> After <code>del</code>, objects still pointed at each other.
      Refcount never hit 0 → need <code>gc.collect()</code> to free the circle.
    </p>
  </div>
</div>

<table class="data-tbl" style="margin-top:12px">
<tr><th>Tool</th><th>Purpose (always)</th><th>A) No circle</th><th>B) Circle A ↔ B</th></tr>
<tr>
  <td><code>weakref.ref(x)</code></td>
  <td>Soft look — does <b>not</b> keep object alive. Later <code>soft_ref()</code> → object or <code>None</code>.</td>
  <td>Watch the toy without holding it.</td>
  <td>Same — still only a soft look.</td>
</tr>
<tr>
  <td><code>del …</code></td>
  <td>Drop strong name(s). Refcount −1. If count hits 0 → free <b>now</b>.</td>
  <td><code>del a</code> → count 0 → <code>soft_ref()</code> becomes <code>None</code> right away.</td>
  <td><code>del a, b</code> → circle still holds them → may <b>not</b> free yet.</td>
</tr>
<tr>
  <td><code>gc.collect()</code></td>
  <td>Run cyclic GC <b>now</b> (usually automatic). Frees unreachable circles.</td>
  <td>Usually collects <b>0</b> for this toy — already gone.</td>
  <td><b>Needed</b> to free A↔B; then <code>soft_ref()</code> becomes <code>None</code>.</td>
</tr>
</table>
<p style="font-size:13px;color:#334155;margin:10px 0 0;line-height:1.45">
  <b>Takeaway:</b>
  <code>weakref</code> = peek without hugging.
  <code>del</code> = let go of the name.
  <code>gc.collect()</code> = call the special cleaner when toys hold each other in a loop.
</p>""",
    22: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>Logger</td><td>Named logging channel — usually <code>__name__</code>.</td><td><code>getLogger(__name__)</code></td></tr>
<tr><td>Log level</td><td>DEBUG, INFO, WARNING, ERROR, CRITICAL.</td><td><code>level=logging.INFO</code></td></tr>
<tr><td>Handler</td><td>Where log records go — console, file, syslog.</td><td>StreamHandler</td></tr>
<tr><td>Formatter</td><td>Pattern for timestamp, level, message.</td><td><code>%(asctime)s</code></td></tr>
<tr><td>RotatingFileHandler</td><td>Log file with size-based rotation.</td><td><code>backupCount=3</code></td></tr>
</table>""",
    14: """
<h3>Key terms explained __CSHARP_PYDANTIC_BTN__</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>BaseModel</td><td>Pydantic schema base class with typed fields.</td><td><code>class User(BaseModel):</code></td></tr>
<tr><td>ValidationError</td><td>Raised when input fails schema rules.</td><td>HTTP 422 in FastAPI</td></tr>
<tr><td>Field()</td><td>Constraints and metadata on a field.</td><td><code>Field(ge=18)</code></td></tr>
<tr><td>field_validator</td><td>Custom rule for a field — runs <b>automatically</b> on validate (normalize or reject).</td><td><code>@field_validator("email")</code></td></tr>
<tr><td>model_dump()</td><td>Export model to dict (Pydantic v2).</td><td><code>user.model_dump()</code></td></tr>
<tr><td>from_attributes</td><td>Build schema from ORM object attributes.</td><td><code>model_config</code></td></tr>
</table>""",
    28: """
<h3>Key terms explained</h3>
<table class="data-tbl term-tbl">
<tr><th>Term</th><th>Meaning</th><th>Quick example</th></tr>
<tr><td>FastAPI</td><td>Modern async-capable web framework.</td><td><code>@app.get()</code></td></tr>
<tr><td>SQLAlchemy</td><td>ORM and SQL toolkit for Python.</td><td><code>Session</code>, <code>Base</code></td></tr>
<tr><td>Depends</td><td>FastAPI dependency injection — DB session, auth.</td><td><code>Depends(get_db)</code></td></tr>
<tr><td>ORM model</td><td>Class mapped to database table.</td><td><code>__tablename__</code></td></tr>
<tr><td>Response model</td><td>Pydantic schema for API output.</td><td><code>response_model=UserRead</code></td></tr>
</table>""",
}


def glossary_for(slide_num: int) -> str:
    text = GLOSSARY.get(slide_num, "")
    for placeholder, popup_id in GLOSSARY_CSHARP_BTNS.items():
        if placeholder in text:
            text = text.replace(placeholder, csharp_compare_btn(popup_id))
    return text


# Placeholder token in glossary HTML → popup id in slide_csharp_popups.py
GLOSSARY_CSHARP_BTNS: dict[str, str] = {
    "__CSHARP_HETERO_BTN__": "hetero-list",
    "__CSHARP_TUPLE_BTN__": "tuple-record",
    "__CSHARP_HASHABLE_BTN__": "hashable-keys",
    "__CSHARP_DUCK_BTN__": "duck-typing",
    "__CSHARP_INDENT_BTN__": "indentation",
    "__CSHARP_DYNAMIC_BTN__": "dynamic-typing",
    "__CSHARP_MAIN_BTN__": "main-block",
    "__CSHARP_ORDER_BTN__": "def-order",
    "__CSHARP_NONE_BTN__": "none-null",
    "__CSHARP_IS_BTN__": "is-vs-equals",
    "__CSHARP_PASS_BTN__": "pass-stub",
    "__CSHARP_FOREACH_BTN__": "foreach",
    "__CSHARP_HINTS_BTN__": "type-hints",
    "__CSHARP_LINQ_BTN__": "listcomp-linq",
    "__CSHARP_LAMBDA_BTN__": "lambda-expr",
    "__CSHARP_MUTABLE_DEF_BTN__": "mutable-default",
    "__CSHARP_SELF_BTN__": "self-this",
    "__CSHARP_INIT_BTN__": "init-constructor",
    "__CSHARP_INHERIT_BTN__": "inheritance",
    "__CSHARP_YIELD_BTN__": "yield-return",
    "__CSHARP_DECORATOR_BTN__": "decorator-attribute",
    "__CSHARP_TRY_BTN__": "try-catch",
    "__CSHARP_WITH_BTN__": "with-using",
    "__CSHARP_ASYNC_BTN__": "async-await",
    "__CSHARP_VENV_BTN__": "venv-nuget",
    "__CSHARP_PROPERTY_BTN__": "property-csharp",
    "__CSHARP_NAMEDTUPLE_BTN__": "namedtuple-record",
    "__CSHARP_COUNTER_BTN__": "counter-linq",
    "__CSHARP_DEFAULTDICT_BTN__": "defaultdict-dict",
    "__CSHARP_DEQUE_BTN__": "deque-linkedlist",
    "__CSHARP_CHAINMAP_BTN__": "chainmap-config",
    "__CSHARP_ORDEREDDICT_BTN__": "ordereddict-dict",
    "__CSHARP_MEMORY_BTN__": "memory-gc",
    "__CSHARP_PYDANTIC_BTN__": "pydantic-validation",
    "__CSHARP_OOP_BTN__": "oop-pillars",
}
