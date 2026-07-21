"""Beginner step-by-step explanations and interview Q&A for each slide."""

BEGINNER_CONTENT: dict[int, dict] = {
    1: {
        "steps": [
            {"title": "Step 1 — What is Python?", "body": "Python is a language you write in text files ending in <code>.py</code>. You run them with the <code>python</code> command — no separate compile step like C#."},
            {"title": "Step 2 — Interpreted, not machine code", "body": "CPython reads your file, builds <b>bytecode</b> (<code>.pyc</code>), then executes that bytecode step by step. That is why we call Python <b>interpreted</b>."},
            {"title": "Step 3 — Indentation = blocks", "body": "Instead of <code>{ }</code> braces, Python uses <b>indentation</b> (usually 4 spaces) after <code>if</code>, <code>for</code>, <code>def</code>."},
            {"title": "Step 4 — Dynamic typing", "body": "You do not write <code>int x</code>. A variable can hold a number, then a string — Python checks types at runtime."},
            {
                "title": "Step 5 — Duck typing (real example)",
                "body": (
                    "<b>Key idea:</b> A class having a method is <b>normal</b>. "
                    "<b>Duck typing</b> is when <b>another function</b> uses that object "
                    "<b>without knowing the class name</b> — only the behavior.<br><br>"
                    "<b>1) Normal:</b> you know the class and call its method."
                    '<div class="step-pre">'
                    "class EmailNotifier:\n"
                    "    def send(self, msg):\n"
                    '        return f"Email: {msg}"\n'
                    "\n"
                    "email = EmailNotifier()\n"
                    'email.send("Order shipped")  # you know it is EmailNotifier'
                    "</div>"
                    "<b>2) Duck typing:</b> <code>notify</code> does not care about the class name — "
                    "Email, SMS, or Slack all work if they have <code>.send()</code>."
                    '<div class="step-pre">'
                    "class EmailNotifier:\n"
                    "    def send(self, msg):\n"
                    '        return f"Email: {msg}"\n'
                    "\n"
                    "class SmsNotifier:\n"
                    "    def send(self, msg):\n"
                    '        return f"SMS: {msg}"\n'
                    "\n"
                    "class SlackNotifier:\n"
                    "    def send(self, msg):\n"
                    '        return f"Slack: {msg}"\n'
                    "\n"
                    "def notify(channel, msg):\n"
                    "    return channel.send(msg)  # no class name — only needs .send()\n"
                    "\n"
                    'notify(EmailNotifier(), "Hi")\n'
                    'notify(SmsNotifier(), "Hi")\n'
                    'notify(SlackNotifier(), "Hi")'
                    "</div>"
                    '<p class="step-result">'
                    "<b>Remember:</b> “If it walks like a duck and quacks like a duck, treat it as a duck.” "
                    "In code: if it has <code>.send()</code>, call <code>.send()</code>. "
                    "No shared base class / interface required. "
                    "Same idea: <code>save(writer, text)</code> works with any object that has <code>.write()</code>."
                    "</p>"
                ),
            },
        ],
        "interview_qa": [
            {"q": "Is Python compiled or interpreted?", "a": "We run the <code>.py</code> file using the Python interpreter. Internally, CPython converts it into bytecode (<code>.pyc</code>) and executes the bytecode step by step. So Python is both compiled to bytecode and interpreted by the Python virtual machine."},
            {"q": "How is Python different from C#?", "a": "No mandatory type declarations, indentation instead of braces, and duck typing — if it has <code>.send()</code>, treat it as a notifier. C# usually requires an interface; Python checks behavior at runtime."},
            {"q": "What is duck typing — how is it different from a class that has a method?", "a": "A class having a method is normal OOP. Duck typing is when another function (like <code>notify(channel, msg)</code>) uses the object without knowing the class name — only that it has the needed behavior (<code>.send()</code>). Email, SMS, Slack all work with no shared base class. C# usually needs <code>interface INotifier</code>."},
            {"q": "Give a realistic duck typing example.", "a": "A <code>notify(channel, msg)</code> function that calls <code>channel.send(msg)</code>. Email, SMS, or Slack classes all work if they implement <code>send</code> — no shared base class required."},
        ],
    },
    2: {
        "steps": [
            {"title": "Step 1 — Install Python", "body": "Download from python.org. On Windows, check <b>Add Python to PATH</b> so <code>python</code> works in PowerShell."},
            {"title": "Step 2 — Verify install", "body": "Run <code>python --version</code> and <code>pip --version</code>. If both work, Python and the package installer are ready.<table class=\"data-tbl\"><tr><th>Command</th><th>Example from your screen</th><th>Meaning</th></tr><tr><td><code>python --version</code></td><td><code>Python 3.12.4</code></td><td>This is the <b>Python interpreter version</b> — the program that runs <code>.py</code> files.</td></tr><tr><td><code>pip --version</code></td><td><code>pip 25.3 ... (python 3.12)</code></td><td>This is the <b>pip installer version</b>, plus the Python version and folder that pip is connected to.</td></tr></table><div class=\"callout\"><b>pip = Pip Installs Packages</b>. It downloads Python libraries from PyPI, like NuGet downloads packages for .NET.</div>"},
            {"title": "Step 3 — Three ways to run code", "body": "<b>REPL</b> — type <code>python</code> and try <code>2+2</code>. <b>Script</b> — <code>python hello.py</code>. <b>IDE</b> — you will mainly use <b>Cursor</b> or <b>VS Code</b>: open the folder, select the interpreter, and press F5 to debug. Other famous Python IDEs/editors: <b>PyCharm</b>, <b>Jupyter Notebook/Lab</b>, <b>Spyder</b>, <b>Visual Studio</b>, and built-in <b>IDLE</b>.<div class=\"step-pre\">C:\\Users\\SangeethaLocalAccoun&gt;python\nPython 3.12.4 ... on win32\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n&gt;&gt;&gt; 2+2\n4\n&gt;&gt;&gt; exit()</div><p class=\"step-result\"><b>Meaning:</b> <code>&gt;&gt;&gt;</code> is the Python REPL prompt. It waits for one Python expression or statement, runs it immediately, and prints the result.</p>"},
            {"title": "Step 4 — Multiple Python versions", "body": "On Windows use <code>py -3.12 script.py</code> to pick a version when more than one is installed."},
            {
                "title": "Step 5 — Define functions before you call them (not like C#)",
                "body": "Python runs a script <b>top to bottom</b>. When it reaches a call like <code>Add(1, 2)</code>, the name <code>Add</code> must already exist. If <code>def Add</code> is below the call, you get <code>NameError: name 'Add' is not defined</code>.<div class=\"callout\"><b>C# difference:</b> Inside a C# class, method order usually does <b>not</b> matter — the compiler sees the whole type first. In a Python <code>.py</code> file, execution order <b>does</b> matter.</div><table class=\"data-tbl\"><tr><th>Wrong order</th><th>Correct strategy</th></tr><tr><td><div class=\"step-pre\">if __name__ == \"__main__\":\n    Add(1, 2)   # NameError!\n\ndef Add(x, y):\n    print(f\"Answer is={x + y}\")</div></td><td><div class=\"step-pre\">def Add(x, y):\n    print(f\"Answer is={x + y}\")\n\nif __name__ == \"__main__\":\n    print(\"hai\")\n    Add(1, 2)</div></td></tr></table><p class=\"step-result\"><b>Strategy:</b> put all <code>def</code> / <code>class</code> at the top; put <code>if __name__ == \"__main__\":</code> at the bottom (like C# <code>Main</code> entry point).</p>",
            },
        ],
        "interview_qa": [
            {"q": "How do you set up Python on a new Windows machine?", "a": "Install from python.org with PATH enabled, verify with <code>python --version</code> and <code>pip --version</code>, create a project folder, optionally <code>python -m venv .venv</code>, and select that interpreter in the IDE."},
            {"q": "What is the difference between python --version and pip --version?", "a": "<code>python --version</code> shows the Python interpreter version, for example <code>Python 3.12.4</code>. <code>pip --version</code> shows the pip package installer version, for example <code>pip 25.3</code>, plus the Python version and install path it belongs to. <b>pip</b> means <b>Pip Installs Packages</b>."},
            {"q": "What is the REPL?", "a": "Read-Eval-Print Loop — an interactive shell. Type one line, see the result immediately. Good for quick experiments, not for full apps."},
            {"q": "Why do I get NameError if I put Add below if __name__?", "a": "Python executes the file top to bottom. When <code>Add(1, 2)</code> runs, <code>def Add</code> has not run yet, so the name does not exist. In C#, method order inside a class usually does not matter because the compiler compiles the whole type first. Strategy: define functions first; put <code>if __name__ == \"__main__\":</code> at the bottom."},
        ],
    },
    5: {
        "steps": [
            {
                "title": "Step 1 — What are Python data types?",
                "body": "A data type tells Python what kind of value is stored. Primitives hold one value.<div class=\"step-pre\">age = 25          # int\nprice = 99.5      # float\nname = \"Ravi\"     # str\nis_student = True # bool</div>",
            },
            {
                "title": "Step 2 — Collection data types",
                "body": "Collections hold multiple values.<table class=\"data-tbl\"><tr><th>Type</th><th>Symbol</th><th>Can change?</th></tr><tr><td>List</td><td><code>[]</code></td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td></tr><tr><td>Tuple</td><td><code>()</code></td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td></tr><tr><td>Set</td><td><code>{a, b}</code></td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td></tr><tr><td>Frozenset</td><td><code>frozenset()</code></td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td></tr><tr><td>Dictionary</td><td><code>{key: value}</code></td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Values can change</td></tr></table>",
            },
            {
                "title": "Step 3 — List: homogeneous, heterogeneous, memory",
                "body": "Lists can hold one type or mixed types. Memory grows in <b>jumps</b> (over-allocation), not +1 byte per append.<div class=\"step-pre\">scores = [90, 85, 88]                 # homogeneous ints\nvendors = [\"Google\", \"Amazon\"]       # homogeneous strs\norder = [101, \"SHIPPED\", [\"Google\", \"Amazon\"]]  # heterogeneous\n\nimport sys\ncart = []\nfor i in range(8):\n    cart.append(i)\n    print(len(cart), sys.getsizeof(cart))  # sizeof jumps</div><p class=\"step-result\"><b>Why jumps?</b> When capacity is full, CPython allocates a larger array and copies references — fewer expensive reallocations.</p>",
            },
            {
                "title": "Step 4 — Tuple: real scenarios + why often faster",
                "body": "Tuples are fixed records — GPS, RGB, return pairs, dict keys.<div class=\"step-pre\">lat_lng = (12.97, 80.22)           # GPS\ndef fetch(id):\n    return True, {\"name\": \"Anu\"}   # (ok, data)\nok, user = fetch(10)\n\n# Usually leaner than list — no capacity buffer / resize logic\nimport sys\nprint(sys.getsizeof([1,2,3]), sys.getsizeof((1,2,3)))</div><p class=\"step-result\"><b>Performance:</b> tuple is fixed → no append bookkeeping → typically less memory and slightly faster iteration for fixed data.</p>",
            },
            {
                "title": "Step 5 — Set: uniqueness",
                "body": "A set keeps only unique items — duplicates are removed automatically.<div class=\"step-pre\">tags = {\"python\", \"code\", \"python\"}\nprint(tags)              # {'python', 'code'}\n\"python\" in tags         # True — fast membership</div>",
            },
            {
                "title": "Step 6 — Frozenset: immutable set",
                "body": "Frozenset is like a set but cannot change after creation. It can be a dictionary key.<div class=\"step-pre\">perms = frozenset({\"read\", \"write\"})\n# perms.add(\"admin\")     # AttributeError — cannot change\n\ncache = {}\ncache[frozenset({1, 2})] = \"combo\"   # OK as dict key</div>",
            },
            {
                "title": "Step 7 — What is a dictionary?",
                "body": "A dictionary stores key : value pairs.<div class=\"step-pre\">student = {\"name\": \"Ravi\", \"age\": 15}\nstudent[\"name\"]          # Ravi</div>",
            },
            {
                "title": "Step 8 — What is a dictionary key?",
                "body": "A key finds a value quickly — like a phone book.<div class=\"step-pre\">phone_book = {\"Ravi\": \"99999\", \"Priya\": \"88888\"}</div><p class=\"step-result\"><b>Key → Value:</b> <code>Ravi → 99999</code></p>",
            },
            {
                "title": "Step 9 — Why keys must be immutable (the locker rule)",
                "body": "A dictionary finds values using <code>hash(key)</code> — like assigning a <b>locker number</b>. That number must stay the same forever after you store the value.<div class=\"callout\"><b>If the key could change</b> (mutable), the locker number would change too — Python could not find your value again. So only <b>immutable</b> types are allowed as keys.</div><table class=\"data-tbl\"><tr><th>Allowed keys</th><th>Blocked keys</th></tr><tr><td><code>int</code>, <code>str</code>, <code>tuple</code>, <code>frozenset</code>, <code>bool</code>, <code>float</code></td><td><code>list</code>, <code>dict</code>, <code>set</code></td></tr></table>",
            },
            {
                "title": "Step 10 — Example: list key fails (and why)",
                "body": "<div class=\"step-pre\">prices = {}\nprices[(12.97, 80.22)] = \"Chennai\"   # tuple OK\nprices[[12.97, 80.22]] = \"Chennai\"   # list → TypeError</div><p class=\"step-result\"><b>Output:</b> <code>TypeError: unhashable type: 'list'</code></p><p><b>Thought experiment:</b> if a list key were allowed:</p><div class=\"step-pre\">key = [1, 2]\ndata[key] = \"secret\"\nkey.append(3)      # key changed → hash would change\n# data[[1, 2]] would no longer find \"secret\"</div><p class=\"step-result\">Python blocks this problem by refusing mutable keys up front.</p>",
            },
            {
                "title": "Step 11 — dict and set also fail as keys",
                "body": "<div class=\"callout\"><b>Name tip:</b> <code>cache</code> is only a <b>variable name</b> (we chose it because this dict acts like a cache). It is not a special Python keyword.</div><div class=\"callout\"><b>{} tip:</b> <code>cache = {}</code> creates an empty <b>dictionary</b>, not a set. Empty set is <code>set()</code>. A non-empty set looks like <code>{\"a\", \"b\"}</code> (values only). A dict looks like <code>{\"id\": 1}</code> (key: value).</div><div class=\"step-pre\">cache = {}                 # empty DICT (not set!)\ncache[{\"id\": 1}] = \"data\"  # TypeError: unhashable type: 'dict'\ncache[{\"a\", \"b\"}] = \"x\"    # TypeError: unhashable type: 'set'\n\n# Compare:\nempty_dict = {}            # dict\nempty_set = set()          # set\nmy_set = {\"a\", \"b\"}        # set (no colon)\nmy_dict = {\"id\": 1}        # dict (has colon)</div><p class=\"step-result\"><b>Fix:</b> use <code>tuple</code> or <code>frozenset</code> instead of list/set as the <i>key</i>.</p>",
            },
            {
                "title": "Step 12 — Tuple and frozenset as keys (safe)",
                "body": "<div class=\"step-pre\">grid = {}\ngrid[(1, 2)] = \"cell\"                      # tuple — hash fixed\ngrid[frozenset({\"read\", \"write\"})] = \"ok\"  # frozenset — hash fixed</div><p class=\"step-result\">Real use: GPS cell <code>(lat, lng)</code>, cache key <code>(\"orders\", 2026, 7)</code>, permission set as frozenset.</p>",
            },
            {
                "title": "Step 13 — Summary",
                "body": "<table class=\"data-tbl\"><tr><th>Data type</th><th>Mutable?</th><th>Dict key?</th></tr><tr><td>int, float, str, bool</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td></tr><tr><td>tuple</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td></tr><tr><td>frozenset</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td></tr><tr><td>list</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td></tr><tr><td>dict</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td></tr><tr><td>set</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td></tr></table>",
            },
        ],
        "interview_qa": [
            {"q": "What is the difference between list and tuple?", "a": "List can append, slice, and change items — use for carts, rows, logs. Tuple is fixed — GPS, RGB, <code>return ok, data</code>, dict keys. Tuple usually uses less memory (no over-allocation) and is slightly faster for fixed-size data."},
            {"q": "How does list memory grow on append?", "a": "CPython over-allocates capacity. When the buffer is full, it allocates a larger array (~1.125×) and copies references. That is why <code>sys.getsizeof</code> jumps in steps instead of growing by one item each time."},
            {"q": "Can a list hold mixed types?", "a": "Yes. Homogeneous: <code>[1, 2, 3]</code> or <code>[\"a\", \"b\"]</code>. Heterogeneous: <code>[101, \"SHIPPED\", [\"Google\", \"Amazon\"]]</code> — int, str, and nested list together."},
            {"q": "Give real tuple use cases.", "a": "GPS <code>(lat, lng)</code>, RGB color, employee record <code>(id, name, salary)</code>, function return <code>(ok, data)</code>, and composite dict keys like <code>(\"orders\", 2026, 7)</code>."},
            {"q": "Why can't you use a list as a dict key?", "a": "Dicts locate values with <code>hash(key)</code> (like a locker number). A list can change after insert (<code>append</code>), so its hash would change and the value could not be found. Python raises <code>TypeError: unhashable type: 'list'</code>. Use a <code>tuple</code> instead: <code>prices[(12.97, 80.22)]</code>."},
            {"q": "Why must dictionary keys be immutable?", "a": "Because the hash of the key must stay stable for the lifetime of the entry. Immutable types (<code>str</code>, <code>int</code>, <code>tuple</code>, <code>frozenset</code>) never change → safe. Mutable types (<code>list</code>, <code>dict</code>, <code>set</code>) can change → blocked."},
            {"q": "What types can be dictionary keys?", "a": "Immutable / hashable types: <code>int</code>, <code>str</code>, <code>tuple</code>, <code>frozenset</code>, <code>bool</code>, <code>float</code>. Not <code>list</code>, <code>dict</code>, or mutable <code>set</code>."},
            {"q": "What is the difference between set and frozenset?", "a": "<code>set</code> is mutable — add/remove items. <code>frozenset</code> is immutable like tuple. Use frozenset when you need a set as a dict key."},
        ],
    },
    3: {
        "steps": [
            {"title": "Step 1 — Three learning layers", "body": "<b>Slides</b> = theory. <b>Projects/</b> = short exercises per topic. <b>Python-Set2/</b> = real multi-file apps."},
            {"title": "Step 2 — One venv per project", "body": "Run <code>python -m venv .venv</code> so each project has its own packages — do not install everything globally."},
            {"title": "Step 3 — Open root in Cursor", "body": "Open <code>D:/Sangeetha/Python/</code>, select Python 3.12 interpreter, run files with <code>python Projects/xx_topic.py</code>."},
            {"title": "Step 4 — Regenerate slides after edits", "body": "Edit <code>build_training.py</code> or <code>training_beginner.py</code>, then run <code>python build_training.py</code> — never hand-edit <code>PythonTraining.html</code>."},
        ],
        "interview_qa": [
            {"q": "How do you organize your Python learning workspace?", "a": "Theory in slides, drills in Projects/, production patterns in Python-Set2. Each real project gets its own venv and requirements.txt."},
        ],
    },
    7: {
        "steps": [
            {
                "title": "Step 1 — Arithmetic (+ - * / % // **)",
                "body": "Python arithmetic operators work on numbers and some sequences.<div class=\"step-pre\">a, b = 10, 4\na + b    # 14\na - b    # 6\na * b    # 40\na / b    # 2.5  (always float in Python 3)\na % b    # 2   (remainder)\na // b   # 2   (floor division)\na ** b   # 10000  (power)</div><p class=\"step-result\"><b>Key rule:</b> <code>/</code> always returns float. Use <code>//</code> when you need whole-number division.</p>",
            },
            {
                "title": "Step 2 — Comparison & Logical",
                "body": "Comparison operators return <code>True</code> or <code>False</code>. Logical operators combine conditions.<table class=\"data-tbl\"><tr><th>Comparison</th><th>Meaning</th></tr><tr><td><code>==</code></td><td>equal value</td></tr><tr><td><code>!=</code></td><td>not equal</td></tr><tr><td><code>&lt;</code> <code>&gt;</code> <code>&lt;=</code> <code>&gt;=</code></td><td>ordering</td></tr></table><div class=\"step-pre\">age = 20\nage &gt;= 18 and age &lt; 65   # True\nnot (age &lt; 18)              # True\nscore &gt; 90 or bonus == True  # short-circuit OR</div>",
            },
            {
                "title": "Step 3 — Identity (is / is not) & Membership (in / not in)",
                "body": "<code>is</code> checks same object in memory — not just equal values. Use <code>is</code> for <code>None</code>.<div class=\"step-pre\">a = [1, 2]\nb = [1, 2]\na == b      # True  (same values)\na is b      # False (different list objects)\n\nx = None\nif x is None:\n    print(\"no value\")\n\n3 in [1, 2, 3]       # True\n\"py\" in \"python\"     # True\n\"z\" not in \"abc\"     # True</div>",
            },
            {
                "title": "Step 4 — Bitwise",
                "body": "Bitwise operators work on integer bits — common in flags, permissions, and low-level math.<div class=\"step-pre\">a, b = 5, 3   # 5 = 101, 3 = 011\na &amp; b   # 1   (AND)\na | b   # 7   (OR)\na ^ b   # 6   (XOR)\n~a      # -6  (NOT)\na &lt;&lt; 1  # 10  (left shift)\na &gt;&gt; 1  # 2   (right shift)</div><p class=\"step-result\"><b>Use case:</b> combine permission flags with <code>|</code>, test with <code>&amp;</code>.</p>",
            },
            {
                "title": "Step 5 — Assignment operators (+=, -=, …)",
                "body": "Shorthand updates a variable in place — same idea as C# <code>+=</code>.<div class=\"step-pre\">n = 10\nn += 5     # 15  (n = n + 5)\nn -= 3     # 12\nn *= 2     # 24\nn //= 4    # 6\nn **= 2    # 36\n\nflags = 0\nflags |= 4   # set bit\nflags &amp;= ~2  # clear bit</div><p class=\"step-result\"><b>All forms:</b> <code>= += -= *= /= //= %= **= &amp;= |= ^= &lt;&lt;= &gt;&gt;=</code></p>",
            },
            {
                "title": "Step 6 — Walrus operator (:=)",
                "body": "Python 3.8+ — assign a value <b>and</b> use it inside the same expression (named after eyes looking like walrus tusks).<div class=\"step-pre\">data = [\"a\", \"bb\", \"ccc\"]\nif (n := len(data)) &gt; 2:\n    print(f\"Got {n} items\")\n\n# classic pattern: read until empty\nwhile (line := input(\"Name: \")) != \"\":\n    print(f\"Hello, {line}\")</div><p class=\"step-result\"><b>Use when:</b> you need the assigned value twice — avoids calling <code>len(data)</code> or <code>input()</code> twice.</p>",
            },
        ],
        "interview_qa": [
            {"q": "What is the difference between == and is?", "a": "<code>==</code> compares values. <code>is</code> compares object identity (same memory address). Two equal lists can be <code>==</code> but not <code>is</code>. Use <code>is</code> for <code>None</code>."},
            {"q": "What is a common division trap in Python 3?", "a": "<code>10 / 4</code> returns <code>2.5</code> (float). Use <code>//</code> for floor division (<code>2</code>) when you need integers."},
            {"q": "What does // vs % do together?", "a": "For integers: <code>a == (a // b) * b + (a % b)</code>. Example: <code>10 // 4 = 2</code>, <code>10 % 4 = 2</code>."},
            {"q": "What is None and how do you test for it?", "a": "<code>None</code> means no value. Always use <code>if x is None:</code> — not <code>x == None</code>. There is only one <code>None</code> object in Python."},
            {"q": "When would you use bitwise operators?", "a": "Feature flags, network masks, fast multiply/divide by powers of 2 with shifts, or when working with binary protocols."},
            {"q": "What does += do?", "a": "<code>n += 5</code> is equivalent to <code>n = n + 5</code> — updates in place. Works for numbers, strings (<code>s += \"x\"</code>), and lists (<code>lst += [1]</code>)."},
            {"q": "When should you use the walrus operator :=?", "a": "When you assign a value and immediately need it in a condition or loop — e.g. <code>if (n := len(items)) &gt; 0:</code>. Do not overuse; readability first."},
        ],
    },
    8: {
        "steps": [
            {
                "title": "Step 1 — if / elif / else",
                "body": "Run exactly one branch based on conditions. Indentation defines the block — no braces.<div class=\"step-pre\">score = 85\nif score &gt;= 90:\n    grade = \"A\"\nelif score &gt;= 75:\n    grade = \"B\"\nelse:\n    grade = \"C\"</div><p class=\"step-result\"><b>Result:</b> <code>grade = \"B\"</code></p>",
            },
            {
                "title": "Step 2 — for loop iteration & range()",
                "body": "<code>for item in sequence:</code> visits each element. <code>range()</code> builds a sequence of integers.<div class=\"step-pre\">for fruit in [\"apple\", \"mango\"]:\n    print(fruit)\n\nfor i in range(5):       # 0, 1, 2, 3, 4\n    print(i)\n\nfor i in range(2, 10, 2):  # 2, 4, 6, 8\n    print(i)</div>",
            },
            {
                "title": "Step 3 — while loop, break & continue",
                "body": "<code>while</code> repeats until the condition is false. <code>break</code> exits; <code>continue</code> skips to the next iteration.<div class=\"step-pre\">n = 0\nwhile n &lt; 5:\n    n += 1\n    if n == 3:\n        continue   # skip printing 3\n    if n == 5:\n        break      # stop at 5\n    print(n)</div><p class=\"step-result\"><b>Output:</b> <code>1</code>, <code>2</code>, <code>4</code></p>",
            },
            {
                "title": "Step 4 — pass & else clause in loops",
                "body": "<div class=\"callout\"><b>pass</b> = this block is intentionally empty for now. It is a <b>stub</b> — define the shape today, add real code later. When you implement it, remove <code>pass</code> and write your logic.</div><code>pass</code> does nothing at runtime, but Python accepts it as a valid statement when syntax requires an indented body.<div class=\"step-pre\"># stub — implement later\ndef save_report():\n    pass   # this block is empty for now\n\n# later, replace pass with real code:\n# def save_report():\n#     with open(\"report.txt\", \"w\") as f:\n#         f.write(\"data\")\n\nclass ValidationError(Exception):\n    pass   # empty exception class</div><p class=\"step-result\"><b>Loop else:</b> runs only if the loop did not hit <code>break</code>.</p><div class=\"step-pre\">for x in [1, 2, 3]:\n    if x == 99:\n        break\nelse:\n    print(\"not found\")</div>",
            },
        ],
        "interview_qa": [
            {"q": "How do blocks work without braces?", "a": "Indentation (usually 4 spaces) after a colon defines the block. Dedent ends the block. Mixing tabs and spaces causes <code>IndentationError</code>."},
            {"q": "When is for-else useful?", "a": "Search loops: loop to find an item; if found, <code>break</code>. The <code>else</code> clause runs only when nothing matched — clean 'not found' handling."},
            {"q": "range(5) vs range(2, 10, 2)?", "a": "<code>range(5)</code> → 0–4. <code>range(start, stop, step)</code> — stop is exclusive. <code>range(2, 10, 2)</code> → 2, 4, 6, 8."},
            {"q": "What is pass used for?", "a": "<b>pass = this block is intentionally empty for now.</b> Use it as a stub in an empty <code>def</code>, <code>class</code>, or unfinished branch. Later, remove <code>pass</code> and add your real code."},
            {"q": "What is the difference between if True and if False?", "a": "<code>if True:</code> block always runs once — usually a TODO stub with <code>pass</code>. <code>if False:</code> block never runs — used to temporarily disable code without deleting it."},
            {"q": "When should you NOT use if True: pass?", "a": "In finished production code — write the real logic directly, or use a proper <code>def</code> stub with a docstring. Remove <code>if True</code> once you implement the block."},
            {"q": "continue vs pass in a loop?", "a": "<code>continue</code> skips to the next iteration. <code>pass</code> does nothing but stays in the current iteration. Never use <code>pass</code> to skip loop items."},
        ],
    },
    9: {
        "steps": [
            {
                "title": "Step 1 — List comprehension",
                "body": "Build a new list in one expression — replaces loop + <code>append</code>.<div class=\"step-pre\">squares = [x * x for x in range(5)]\n# [0, 1, 4, 9, 16]\n\nevens = [x for x in range(10) if x % 2 == 0]\n# [0, 2, 4, 6, 8]</div><p class=\"step-result\"><b>Read it:</b> \"give me x*x for each x in range(5)\"</p>",
            },
            {
                "title": "Step 2 — Set comprehension",
                "body": "Same syntax with curly braces — automatically removes duplicates.<div class=\"step-pre\">words = [\"hi\", \"bye\", \"hi\"]\nunique = {w.upper() for w in words}\n# {\"HI\", \"BYE\"}</div>",
            },
            {
                "title": "Step 3 — Dictionary comprehension",
                "body": "Build a dict from key-value expressions.<div class=\"step-pre\">nums = [1, 2, 3]\nsq_map = {n: n * n for n in nums}\n# {1: 1, 2: 4, 3: 9}\n\nfiltered = {k: v for k, v in sq_map.items() if v &gt; 1}</div>",
            },
            {
                "title": "Step 4 — Generator expression",
                "body": "Parentheses instead of brackets — lazy, yields one item at a time, saves memory.<table class=\"data-tbl\"><tr><th>Feature</th><th>List comp</th><th>Generator</th></tr><tr><td>Syntax</td><td><code>[...]</code></td><td><code>(...)</code></td></tr><tr><td>Memory</td><td>All at once</td><td>One item at a time</td></tr><tr><td>Reusable?</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td><td class=\"cell-no\"><span class=\"yn-no\"></span>Exhausted after one pass</td></tr></table><div class=\"step-pre\">gen = (x * x for x in range(1_000_000))\nnext(gen)   # 0\nnext(gen)   # 1</div>",
            },
        ],
        "interview_qa": [
            {"q": "Why use a comprehension over a for loop?", "a": "Shorter and often clearer for simple transforms. <code>[n*n for n in range(10) if n%2==0]</code> is easier to read than a 4-line loop with append."},
            {"q": "List comprehension vs generator expression?", "a": "List builds everything in memory. Generator yields one value at a time — better for large data or pipelines."},
            {"q": "Can comprehensions have nested loops?", "a": "Yes: <code>[(x, y) for x in range(3) for y in range(2)]</code> — same order as nested for loops."},
            {"q": "When should you NOT use a comprehension?", "a": "When logic is complex, has side effects, or needs multiple statements — use a regular for loop for readability."},
        ],
    },
    10: {
        "steps": [
            {
                "title": "Step 1 — Positional & Keyword args",
                "body": "Positional args are matched by order. Keyword args are matched by name. Defaults go in the signature.<div class=\"step-pre\">def greet(name, excited=False):\n    msg = f\"Hello, {name}!\"\n    return msg + \"!!!\" if excited else msg\n\ngreet(\"Anu\")                  # positional\ngreet(name=\"Anu\", excited=True)  # keyword</div>",
            },
            {
                "title": "Step 2 — *args & **kwargs",
                "body": "<div class=\"callout\"><b>Mutable default trap</b> — never <code>def f(items=[])</code>. The same list is created once and shared across all calls. Use <code>items=None</code> and create a new list inside.</div><code>*args</code> collects extra positional args as a tuple. <code>**kwargs</code> collects extra keyword args as a dict.<div class=\"step-pre\">def log(msg, *args, **kwargs):\n    print(msg, args, kwargs)\n\nlog(\"start\", 1, 2, level=\"debug\")\n# start (1, 2) {'level': 'debug'}</div>",
            },
            {
                "title": "Step 3 — Recursion & functional style",
                "body": "FP often uses recursion instead of loops. A function calls itself until a base case.<div class=\"step-pre\">def factorial(n):\n    if n &lt;= 1:\n        return 1\n    return n * factorial(n - 1)\n\nfactorial(5)   # 120</div><p class=\"step-result\"><b>Warning:</b> deep recursion can hit <code>RecursionError</code> — Python default limit ~1000.</p>",
            },
            {
                "title": "Step 3b — Pure & higher-order functions (FP)",
                "body": "From the <a href=\"https://www.geeksforgeeks.org/blogs/functional-programming-paradigm/\" target=\"_blank\" rel=\"noopener\">Functional Programming paradigm</a>: a <b>pure</b> function always returns the same output for the same inputs and has no side effects. <b>Higher-order</b> functions take or return functions.<div class=\"step-pre\">def add(x, y):          # pure\n    return x + y\n\ndef apply_twice(fn, v): # higher-order\n    return fn(fn(v))\n\napply_twice(lambda n: n + 1, 5)  # 7</div>",
            },
            {
                "title": "Step 4 — Lambda",
                "body": "Anonymous one-expression function — good for short callbacks.<div class=\"step-pre\">double = lambda x: x * 2\ndouble(5)   # 10\n\nsorted(pairs, key=lambda p: p[1])</div>",
            },
            {
                "title": "Step 5 — LEGB scope",
                "body": "Python looks up names in order: Local → Enclosing → Global → Builtin.<div class=\"step-pre\">x = \"global\"\n\ndef outer():\n    x = \"enclosing\"\n    def inner():\n        x = \"local\"\n        print(x)   # local\n    inner()\n\nouter()</div>",
            },
            {
                "title": "Step 6 — Closures",
                "body": "An inner function remembers variables from its enclosing scope even after the outer function returns.<div class=\"step-pre\">def make_multiplier(n):\n    def multiply(x):\n        return x * n\n    return multiply\n\ntimes3 = make_multiplier(3)\ntimes3(10)   # 30</div>",
            },
        ],
        "interview_qa": [
            {"q": "What is wrong with def f(items=[])?", "a": "The default list is created once at definition time and shared across all calls. Use <code>def f(items=None): items = items or []</code> instead."},
            {"q": "What are *args and **kwargs?", "a": "<code>*args</code> is a tuple of extra positional arguments. <code>**kwargs</code> is a dict of extra keyword arguments. Useful for wrappers and decorators."},
            {"q": "What is LEGB?", "a": "Name lookup order: Local (inside function), Enclosing (outer functions), Global (module), Builtin (built-in names like <code>len</code>)."},
            {"q": "Lambda vs def?", "a": "Lambda is limited to one expression, no statements. Use <code>def</code> for anything non-trivial — lambdas are for short keys and callbacks."},
            {"q": "What is a pure function?", "a": "Same arguments always produce the same result, and it does not modify globals, mutate inputs, or do hidden I/O. Easier to test and safe for concurrency (FP / GeeksforGeeks)."},
            {"q": "What is a higher-order function?", "a": "A function that takes another function as an argument or returns a function — e.g. <code>sorted(items, key=fn)</code>, <code>map</code>, <code>filter</code>, or a decorator factory."},
        ],
    },
    11: {
        "steps": [
            {
                "title": "Step 1 — map, filter & reduce",
                "body": "<code>map</code> applies a function to every item. <code>filter</code> keeps truthy results. <code>reduce</code> folds a sequence (from <code>functools</code>).<div class=\"step-pre\">nums = [1, 2, 3, 4]\nlist(map(lambda x: x * 2, nums))     # [2, 4, 6, 8]\nlist(filter(lambda x: x % 2 == 0, nums))  # [2, 4]\n\nfrom functools import reduce\nreduce(lambda a, b: a + b, nums)   # 10</div>",
            },
            {
                "title": "Step 2 — zip & enumerate",
                "body": "<code>zip</code> pairs items from multiple sequences. <code>enumerate</code> adds an index.<div class=\"step-pre\">names = [\"Anu\", \"Ravi\"]\nscores = [90, 85]\nlist(zip(names, scores))\n# [(\"Anu\", 90), (\"Ravi\", 85)]\n\nfor i, name in enumerate(names, start=1):\n    print(i, name)</div>",
            },
            {
                "title": "Step 3 — type, id & isinstance",
                "body": "<code>type(x)</code> returns the exact class. <code>id(x)</code> returns memory address. Prefer <code>isinstance</code> for type checks.<div class=\"step-pre\">x = 42\ntype(x)              # &lt;class 'int'&gt;\nid(x)                # unique object id\nisinstance(x, int)   # True\nisinstance(True, int)  # True — bool is subclass of int</div>",
            },
            {
                "title": "Step 4 — range, len, sorted & reversed",
                "body": "Common sequence utilities — know which mutate vs return new objects.<table class=\"data-tbl\"><tr><th>Function</th><th>Returns</th><th>Mutates?</th></tr><tr><td><code>len(x)</code></td><td>count</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td></tr><tr><td><code>sorted(x)</code></td><td>new list</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td></tr><tr><td><code>reversed(x)</code></td><td>iterator</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No</td></tr><tr><td><code>list.sort()</code></td><td><code>None</code></td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td></tr></table><div class=\"step-pre\">len([10, 20, 30])           # 3\nsorted([3, 1, 2])             # [1, 2, 3]\nlist(reversed(\"abc\"))         # ['c', 'b', 'a']</div>",
            },
            {
                "title": "Step 5 — max & min",
                "body": "<code>max()</code> and <code>min()</code> find the largest and smallest item — with optional <code>key=</code> for custom ordering.<div class=\"step-pre\">prices = [120, 45, 89, 200]\nmax(prices)                 # 200\nmin(prices)                 # 45\n\nscores = {\"Anu\": 90, \"Ravi\": 85}\nmax(scores, key=scores.get)  # \"Anu\" (highest score)\nmin(scores, key=scores.get)  # \"Ravi\"\n\nmax([], default=0)           # 0 — empty safe</div>",
            },
        ],
        "interview_qa": [
            {"q": "sorted() vs list.sort()?", "a": "<code>sorted()</code> returns a new sorted list; original unchanged. <code>.sort()</code> mutates in place and returns <code>None</code>. Never assign <code>x = lst.sort()</code>."},
            {"q": "When do you use enumerate?", "a": "When you need both index and value: <code>for i, item in enumerate(items):</code> instead of manual <code>range(len(items))</code>."},
            {"q": "isinstance vs type() == ?", "a": "<code>isinstance(x, int)</code> respects inheritance (<code>True</code> for bool). <code>type(x) == int</code> is exact match only."},
            {"q": "map vs list comprehension?", "a": "Comprehensions are more Pythonic and readable. <code>map</code> is useful with existing functions: <code>map(str.strip, lines)</code>."},
            {"q": "max/min on empty iterable?", "a": "Without <code>default=</code>, raises <code>ValueError</code>. Use <code>max(items, default=0)</code> when empty is possible."},
            {"q": "max on a dict — what does it return?", "a": "By default compares <b>keys</b>. Use <code>max(d, key=d.get)</code> to find the key with the largest value."},
        ],
    },
    15: {
        "steps": [
            {
                "title": "Step 1 — Class, Object, __init__ & self",
                "body": "A class is a blueprint. An object is an instance. <code>__init__</code> initializes state; <code>self</code> refers to the current instance.<div class=\"step-pre\">class Dog:\n    def __init__(self, name):\n        self.name = name\n\n    def bark(self):\n        return f\"{self.name} says woof!\"\n\nmy_dog = Dog(\"Rex\")\nmy_dog.bark()</div><p class=\"step-result\"><b>Output:</b> <code>Rex says woof!</code></p>",
            },
            {
                "title": "Step 2 — Inheritance: single, multiple & MRO",
                "body": "A child class inherits from one or more parents. MRO (Method Resolution Order) defines lookup order.<div class=\"step-pre\">class Animal:\n    def speak(self): return \"...\"\n\nclass Dog(Animal):\n    def speak(self): return \"woof\"\n\nclass Cat(Animal):\n    def speak(self): return \"meow\"\n\nclass Pet(Dog, Cat): pass\n\nPet.__mro__   # lookup order</div>",
            },
            {
                "title": "Step 3 — Encapsulation & _ convention",
                "body": "Python has no true private fields. A single leading underscore signals \"internal use\" by convention.<div class=\"step-pre\">class BankAccount:\n    def __init__(self, balance):\n        self._balance = balance   # convention: don't touch\n\n    def deposit(self, amount):\n        self._balance += amount</div><p class=\"step-result\"><b>Note:</b> <code>__name</code> triggers name mangling — stronger but not security.</p>",
            },
            {
                "title": "Step 4 — Polymorphism & overriding",
                "body": "Different classes share the same interface. Child methods override parent methods.<div class=\"step-pre\">def announce(animal):\n    print(animal.speak())\n\nannounce(Dog())   # woof\nannounce(Cat())   # meow</div>",
            },
            {
                "title": "Step 5 — Abstract classes (abc)",
                "body": "Force subclasses to implement required methods using <code>abc.ABC</code> and <code>@abstractmethod</code>.<div class=\"step-pre\">from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self): ...\n\nclass Circle(Shape):\n    def __init__(self, r): self.r = r\n    def area(self): return 3.14 * self.r ** 2</div>",
            },
            {
                "title": "Step 6 — Dunder methods",
                "body": "Double-underscore methods customize built-in behavior.<table class=\"data-tbl\"><tr><th>Method</th><th>Triggered by</th></tr><tr><td><code>__str__</code></td><td><code>print(obj)</code>, <code>str(obj)</code></td></tr><tr><td><code>__repr__</code></td><td><code>repr(obj)</code>, debugger</td></tr><tr><td><code>__eq__</code></td><td><code>obj == other</code></td></tr><tr><td><code>__len__</code></td><td><code>len(obj)</code></td></tr></table>",
            },
        ],
        "interview_qa": [
            {"q": "What is self in Python?", "a": "The current instance. You must pass it as the first parameter of instance methods. <code>self.name</code> stores data on the object — like <code>this</code> in C#."},
            {"q": "__str__ vs __repr__?", "a": "<code>__str__</code> is for end users (readable). <code>__repr__</code> is for developers — ideally valid code to recreate the object."},
            {"q": "What is MRO?", "a": "Method Resolution Order — the sequence Python searches base classes. Check with <code>ClassName.__mro__</code> or <code>help(ClassName)</code>."},
            {"q": "How does Python handle encapsulation?", "a": "By convention: <code>_attr</code> means internal. <code>__attr</code> name-mangles to <code>_ClassName__attr</code>. Not true access control — trust and documentation."},
        ],
    },
    18: {
        "steps": [
            {
                "title": "Step 1 — Function decorators",
                "body": "A decorator wraps a function to add behavior without changing its source. <code>@decorator</code> is syntactic sugar for <code>func = decorator(func)</code>.<div class=\"step-pre\">import time\n\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        print(f\"took {time.time()-start:.2f}s\")\n        return result\n    return wrapper\n\n@timer\ndef work():\n    time.sleep(0.1)</div>",
            },
            {
                "title": "Step 2 — Class decorators",
                "body": "A decorator can wrap a class — modify or register it before use.<div class=\"step-pre\">def add_repr(cls):\n    def __repr__(self):\n        return f\"{cls.__name__}()\"\n    cls.__repr__ = __repr__\n    return cls\n\n@add_repr\nclass User:\n    pass\n\nUser()   # repr: User()</div>",
            },
            {
                "title": "Step 3 — functools.wraps",
                "body": "Without <code>@wraps</code>, the wrapper hides the original function's name and docstring.<div class=\"step-pre\">from functools import wraps\n\ndef my_decorator(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs)\n    return wrapper\n\n@my_decorator\ndef greet():\n    \"\"\"Say hello\"\"\"\n    pass\n\ngreet.__name__   # greet (not wrapper)\ngreet.__doc__    # Say hello</div>",
            },
        ],
        "interview_qa": [
            {"q": "Explain decorators in simple terms.", "a": "A decorator is a function that takes a function and returns a new function with extra behavior. FastAPI uses <code>@app.get('/')</code> to register routes."},
            {"q": "Why use functools.wraps?", "a": "Without it, the wrapped function loses its original <code>__name__</code> and <code>__doc__</code> — bad for debugging, introspection, and docs."},
            {"q": "Can a decorator accept arguments?", "a": "Yes — use a factory: <code>def repeat(n): def decorator(func): ... return decorator</code>. Then <code>@repeat(3)</code>."},
            {"q": "Decorator vs inheritance for extending behavior?", "a": "Decorators compose behavior around a single function at runtime. Inheritance models is-a relationships between types."},
        ],
    },
    16: {
        "steps": [
            {
                "title": "Step 1 — __get__, __set__ & __delete__",
                "body": "A descriptor is an object with at least one of these methods. It controls what happens when an attribute is accessed on a class.<div class=\"step-pre\">class Validator:\n    def __init__(self, name):\n        self.name = name\n\n    def __get__(self, obj, objtype=None):\n        return obj.__dict__.get(self.name)\n\n    def __set__(self, obj, value):\n        if value &lt; 0:\n            raise ValueError(\"must be &gt;= 0\")\n        obj.__dict__[self.name] = value</div>",
            },
            {
                "title": "Step 2 — Property vs descriptor",
                "body": "<code>@property</code> is a built-in descriptor — simpler for most cases. Custom descriptors give full control.<table class=\"data-tbl\"><tr><th>Approach</th><th>Best for</th></tr><tr><td><code>@property</code></td><td>Computed or validated attributes on one class</td></tr><tr><td>Custom descriptor</td><td>Reusable attribute logic across many classes</td></tr></table><div class=\"step-pre\">class Score:\n    def __init__(self):\n        self._value = 0\n\n    @property\n    def value(self):\n        return self._value\n\n    @value.setter\n    def value(self, v):\n        if v &lt; 0: raise ValueError\n        self._value = v</div>",
            },
        ],
        "interview_qa": [
            {"q": "What is @property for?", "a": "Expose a computed or validated attribute without explicit get/set methods. Callers use <code>obj.score</code> instead of <code>obj.get_score()</code>."},
            {"q": "What is a descriptor?", "a": "An object with <code>__get__</code>, <code>__set__</code>, or <code>__delete__</code> that intercepts attribute access. Python uses descriptors for <code>property</code>, <code>classmethod</code>, and <code>staticmethod</code>."},
            {"q": "When write a custom descriptor instead of @property?", "a": "When the same access logic must be reused across multiple classes or attributes — e.g. typed fields, lazy loading, or cached values."},
        ],
    },
    17: {
        "steps": [
            {
                "title": "Step 1 — Lazy iterators (why generators exist)",
                "body": "From <a href=\"https://realpython.com/introduction-to-python-generators/\" target=\"_blank\" rel=\"noopener\">Real Python</a>: generators return a <b>lazy iterator</b> — loop like a list, but do <b>not</b> store all contents in memory. Loading a huge CSV with <code>file.read().split()</code> can raise <code>MemoryError</code>; <code>yield</code> one row at a time stays safe.",
            },
            {
                "title": "Step 2 — yield vs return + generator expressions",
                "body": "<code>return</code> ends the function with one value. <code>yield</code> produces a generator object and pauses between values.<div class=\"step-pre\">def csv_reader(path):\n    with open(path, encoding=\"utf-8\") as f:\n        for row in f:\n            yield row\n\n# Generator expression (same idea, shorter):\nrows = (line for line in open(path, encoding=\"utf-8\"))</div>",
            },
            {
                "title": "Step 3 — Infinite sequences & pipelines",
                "body": "Only generators can model infinite sequences safely (memory is finite). You can also chain generators into a pipeline without building giant intermediate lists.<div class=\"step-pre\">def infinite_sequence():\n    n = 0\n    while True:\n        yield n\n        n += 1\n\ngen = infinite_sequence()\nnext(gen); next(gen)   # 0, then 1 — stop manually</div>",
            },
            {
                "title": "Step 4 — Iterator protocol & itertools",
                "body": "An iterable has <code>__iter__</code>. An iterator has <code>__iter__</code> and <code>__next__</code>. <code>for</code> uses this until <code>StopIteration</code>.<div class=\"step-pre\">from itertools import chain, islice\nlist(chain([1, 2], [3, 4]))\nlist(islice(range(100), 5))</div>",
            },
        ],
        "interview_qa": [
            {"q": "Generator vs list?", "a": "A list stores all values at once. A generator produces one value at a time — lower memory, lazy evaluation (Real Python)."},
            {"q": "When does a file reader MemoryError?", "a": "When you load the whole file into a list (<code>read().split()</code>). Fix: <code>for line in f: yield line</code> so only one line is in memory."},
            {"q": "What does yield do?", "a": "Pauses the function, returns a value to the caller, and saves state. Next <code>next()</code> or loop iteration resumes after the yield. Using <code>return</code> instead ends after one value."},
            {"q": "What is a generator expression?", "a": "Like a list comprehension but with parentheses: <code>(x*x for x in range(10**6))</code> — lazy, does not build the full list."},
            {"q": "What is StopIteration?", "a": "Raised when a generator is exhausted. <code>for</code> loops catch it automatically to end iteration."},
        ],
    },
    6: {
        "steps": [
            {
                "title": "Step 1 — Basic type hints",
                "body": "Type hints document expected types. Python does not enforce them at runtime by default.<div class=\"step-pre\">def greet(name: str) -&gt; str:\n    return f\"Hello, {name}\"\n\ndef add(a: int, b: int) -&gt; int:\n    return a + b\n\nage: int = 25\nname: str = \"Ravi\"</div>",
            },
            {
                "title": "Step 2 — Optional, Union, List, Dict & Tuple",
                "body": "Compose types for real-world data. Python 3.10+ allows <code>X | Y</code> instead of <code>Union[X, Y]</code>.<div class=\"step-pre\">from typing import Optional, List, Dict, Tuple\n\ndef find_user(id: int) -&gt; Optional[str]:\n    return None   # or a name\n\ndef process(items: List[int]) -&gt; Dict[str, int]:\n    return {\"count\": len(items)}\n\nPoint = Tuple[float, float]</div>",
            },
            {
                "title": "Step 3 — TypeVar, Generic & Protocol",
                "body": "Generics make reusable typed containers. Protocols define structural typing (duck typing with types).<div class=\"step-pre\">from typing import TypeVar, Generic, Protocol\n\nT = TypeVar(\"T\")\n\nclass Stack(Generic[T]):\n    def push(self, item: T) -&gt; None: ...\n\nclass Drawable(Protocol):\n    def draw(self) -&gt; None: ...</div>",
            },
            {
                "title": "Step 4 — mypy",
                "body": "Static type checker — catches type errors before runtime.<div class=\"step-pre\"># terminal\nmypy my_module.py\nmypy --strict my_project/</div><p class=\"step-result\"><b>Tip:</b> run mypy in CI alongside pytest to catch mismatches early.</p>",
            },
        ],
        "interview_qa": [
            {"q": "Do type hints slow Python down?", "a": "No — they are stored as annotations and ignored at runtime unless you use a validator like Pydantic or FastAPI."},
            {"q": "Optional[str] means what?", "a": "The value can be a <code>str</code> or <code>None</code>. In 3.10+: <code>str | None</code>."},
            {"q": "What is a Protocol?", "a": "Defines an interface by method signatures — any class with matching methods satisfies it, without explicit inheritance."},
            {"q": "Why use mypy?", "a": "Finds type mismatches, missing returns, and wrong argument types before deployment — like a lightweight compiler check."},
        ],
    },
    25: {
        "steps": [
            {
                "title": "Step 1 — open, read, write & append modes",
                "body": "File modes control how a file is opened. Always specify <code>encoding=\"utf-8\"</code> on Windows.<table class=\"data-tbl\"><tr><th>Mode</th><th>Action</th></tr><tr><td><code>\"r\"</code></td><td>read (default)</td></tr><tr><td><code>\"w\"</code></td><td>write — overwrites</td></tr><tr><td><code>\"a\"</code></td><td>append — adds to end</td></tr><tr><td><code>\"r+\"</code></td><td>read and write</td></tr></table><div class=\"step-pre\">f = open(\"log.txt\", \"a\", encoding=\"utf-8\")\nf.write(\"new line\\n\")\nf.close()</div>",
            },
            {
                "title": "Step 2 — with context manager",
                "body": "<code>with</code> guarantees the file closes even if an error occurs — like C# <code>using</code>.<div class=\"step-pre\">with open(\"data.txt\", \"r\", encoding=\"utf-8\") as f:\n    content = f.read()\n\nwith open(\"out.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"Hello\\n\")</div>",
            },
            {
                "title": "Step 3 — CSV & JSON",
                "body": "Structured data formats — CSV for spreadsheets, JSON for APIs and config.<div class=\"step-pre\">import json, csv\n\nwith open(\"data.json\", encoding=\"utf-8\") as f:\n    data = json.load(f)\n\nwith open(\"rows.csv\", encoding=\"utf-8\") as f:\n    for row in csv.DictReader(f):\n        print(row[\"name\"])</div>",
            },
            {
                "title": "Step 4 — pathlib",
                "body": "Object-oriented paths — cleaner than string concatenation.<div class=\"step-pre\">from pathlib import Path\n\nroot = Path(\"data\")\nfile = root / \"report.txt\"\nfile.write_text(\"summary\", encoding=\"utf-8\")\nfile.read_text(encoding=\"utf-8\")\n\nfor p in root.glob(\"*.csv\"):\n    print(p.name)</div>",
            },
        ],
        "interview_qa": [
            {"q": "Why with open() instead of open() alone?", "a": "Guarantees the file is closed. If an exception happens inside the block, the file still closes — prevents leaks and locked files on Windows."},
            {"q": "json.load vs json.loads?", "a": "<code>json.load(f)</code> reads from a file object. <code>json.loads(s)</code> parses a string. Same pattern for <code>dump</code>/<code>dumps</code>."},
            {"q": "pathlib vs os.path?", "a": "<code>Path</code> uses <code>/</code> operator, has <code>.read_text()</code>, <code>.glob()</code>, and works cross-platform. Preferred in modern Python."},
            {"q": "Why encoding=utf-8 on Windows?", "a": "Windows default encoding may not be UTF-8. Explicit encoding avoids <code>UnicodeDecodeError</code> with non-ASCII text."},
        ],
    },
    19: {
        "steps": [
            {
                "title": "Step 1 — try, except, else & finally",
                "body": "Handle errors gracefully. <code>else</code> runs if no exception. <code>finally</code> always runs.<div class=\"step-pre\">try:\n    result = int(user_input)\nexcept ValueError:\n    print(\"not a number\")\nelse:\n    print(f\"parsed: {result}\")\nfinally:\n    print(\"cleanup always runs\")</div>",
            },
            {
                "title": "Step 2 — Built-in exception hierarchy",
                "body": "All exceptions inherit from <code>BaseException</code>. Catch specific types, not everything.<div class=\"step-pre\">BaseException\n └── Exception\n      ├── ValueError\n      ├── TypeError\n      ├── FileNotFoundError\n      └── KeyError</div><p class=\"step-result\"><b>Rule:</b> catch the most specific exception you can handle.</p>",
            },
            {
                "title": "Step 3 — Custom exceptions",
                "body": "Define domain-specific errors your team understands.<div class=\"step-pre\">class ValidationError(Exception):\n    def __init__(self, field, message):\n        self.field = field\n        super().__init__(message)\n\ndef set_age(age):\n    if age &lt; 0:\n        raise ValidationError(\"age\", \"must be positive\")</div>",
            },
            {
                "title": "Step 4 — raise & re-raise",
                "body": "<code>raise</code> throws an exception. <code>raise ... from ...</code> chains the original cause.<div class=\"step-pre\">try:\n    data = json.loads(raw)\nexcept json.JSONDecodeError as e:\n    raise ValueError(\"bad config\") from e\n\n# bare re-raise inside except:\nexcept FileNotFoundError:\n    log_error()\n    raise   # preserves traceback</div>",
            },
        ],
        "interview_qa": [
            {"q": "Why not use bare except?", "a": "It catches everything including <code>KeyboardInterrupt</code> and hides the real bug. Catch specific exceptions you can handle."},
            {"q": "What does raise from do?", "a": "Chains exceptions — the new error keeps a link to the original cause in the traceback (<code>__cause__</code>)."},
            {"q": "When does else run in try/except?", "a": "Only when the <code>try</code> block completes without raising any exception."},
            {"q": "finally vs else?", "a": "<code>else</code> runs on success only. <code>finally</code> runs always — use for cleanup like closing connections."},
        ],
    },
    24: {
        "steps": [
            {
                "title": "Step 1 — re.match, re.search & re.findall",
                "body": "Three ways to find patterns in text.<table class=\"data-tbl\"><tr><th>Function</th><th>Where it searches</th><th>Returns</th></tr><tr><td><code>match</code></td><td>start of string only</td><td>Match or None</td></tr><tr><td><code>search</code></td><td>anywhere in string</td><td>Match or None</td></tr><tr><td><code>findall</code></td><td>anywhere</td><td>list of all matches</td></tr></table><div class=\"step-pre\">import re\ntext = \"Order 42 done\"\nre.search(r\"\\d+\", text).group()    # \"42\"\nre.findall(r\"\\d+\", \"a1 b22\")      # [\"1\", \"22\"]</div>",
            },
            {
                "title": "Step 2 — Groups & special sequences",
                "body": "Parentheses capture parts. Special sequences match common patterns.<div class=\"step-pre\">import re\nm = re.search(r\"(\\d{3})-(\\d{4})\", \"555-1234\")\nm.group(0)   # full match: 555-1234\nm.group(1)   # 555\nm.group(2)   # 1234\n\n# special: \\d digit, \\w word, \\s space, . any char\n# use raw strings: r\"\\d+\"</div>",
            },
            {
                "title": "Step 3 — Lookahead & lookbehind",
                "body": "Assert what comes before or after a position without including it in the match.<div class=\"step-pre\">import re\n\n# positive lookahead: digit followed by \"px\"\nre.findall(r\"\\d+(?=px)\", \"10px 20em\")\n# [\"10\"]\n\n# lookbehind: digits preceded by $\nre.findall(r\"(?&lt;=\\$)\\d+\", \"$50 and $100\")\n# [\"50\", \"100\"]</div>",
            },
        ],
        "interview_qa": [
            {"q": "search vs match?", "a": "<code>re.search</code> scans the whole string. <code>re.match</code> only checks the beginning — often surprises beginners."},
            {"q": "Why raw strings for regex?", "a": "<code>r\"\\d\"</code> is one backslash + d. Without <code>r</code>, you need <code>\"\\\\d\"</code> — easy to get wrong."},
            {"q": "What is a capturing group?", "a": "Parentheses <code>(...)</code> in a pattern capture matched text. Access with <code>.group(1)</code>, <code>.group(2)</code>, etc."},
            {"q": "What is lookahead?", "a": "A zero-width assertion — checks what follows without consuming it. <code>(?=...)</code> positive, <code>(?!...)</code> negative."},
        ],
    },
    12: {
        "steps": [
            {
                "title": "Step 1 — Counter",
                "body": "Counts hashable elements — like a frequency table.<div class=\"step-pre\">from collections import Counter\n\nc = Counter(\"hello\")\n# Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})\nc.most_common(2)   # [('l', 2), ('o', 1)]\nc[\"l\"]             # 2</div>",
            },
            {
                "title": "Step 2 — OrderedDict",
                "body": "Dict that remembers insertion order. In Python 3.7+ regular dicts also preserve order — OrderedDict adds extra methods.<div class=\"step-pre\">from collections import OrderedDict\n\nod = OrderedDict()\nod[\"a\"] = 1\nod[\"b\"] = 2\nlist(od.keys())   # [\"a\", \"b\"]\nod.move_to_end(\"a\")</div>",
            },
            {
                "title": "Step 3 — defaultdict",
                "body": "Auto-creates a default value for missing keys — great for grouping.<div class=\"step-pre\">from collections import defaultdict\n\ngroups = defaultdict(list)\nfor name, dept in [(\"Anu\", \"IT\"), (\"Ravi\", \"HR\"), (\"Priya\", \"IT\")]:\n    groups[dept].append(name)\n# {\"IT\": [\"Anu\", \"Priya\"], \"HR\": [\"Ravi\"]}</div>",
            },
            {
                "title": "Step 4 — ChainMap",
                "body": "Treats multiple dicts as one — searches in order, first match wins.<div class=\"step-pre\">from collections import ChainMap\n\ndefaults = {\"color\": \"red\", \"size\": \"M\"}\nuser = {\"color\": \"blue\"}\nsettings = ChainMap(user, defaults)\nsettings[\"color\"]   # blue (user wins)\nsettings[\"size\"]    # M (from defaults)</div>",
            },
            {
                "title": "Step 5 — namedtuple",
                "body": "Lightweight tuple with named fields — readable and immutable.<div class=\"step-pre\">from collections import namedtuple\n\nPoint = namedtuple(\"Point\", [\"x\", \"y\"])\np = Point(10, 20)\np.x, p.y   # 10, 20\np[0]       # 10 (still indexable)</div>",
            },
            {
                "title": "Step 6 — deque",
                "body": "Double-ended queue — fast append/pop from both ends.<div class=\"step-pre\">from collections import deque\n\nd = deque([1, 2, 3])\nd.appendleft(0)    # deque([0, 1, 2, 3])\nd.pop()            # 3\nd.popleft()        # 0</div>",
            },
            {
                "title": "Step 7 — UserDict, UserList & UserString",
                "body": "Subclass-friendly wrappers — override methods without breaking built-in internals.<div class=\"step-pre\">from collections import UserDict\n\nclass CaseInsensitiveDict(UserDict):\n    def __setitem__(self, key, value):\n        super().__setitem__(key.lower(), value)</div><p class=\"step-result\"><b>Why:</b> safer to subclass than built-in <code>dict</code> directly.</p>",
            },
        ],
        "interview_qa": [
            {"q": "When use defaultdict vs normal dict?", "a": "When you would write <code>if key not in d: d[key] = []</code> every time — defaultdict creates the default for you."},
            {"q": "namedtuple vs dataclass?", "a": "namedtuple is immutable and lighter. dataclass is better when you need mutability, defaults, or methods."},
            {"q": "When use deque over list?", "a": "When you need fast <code>appendleft</code>/<code>popleft</code> — queues, BFS, sliding windows. List pop(0) is O(n)."},
            {"q": "What is ChainMap for?", "a": "Layered config: defaults + user overrides + env vars. Lookup walks dicts left to right."},
        ],
    },
    23: {
        "steps": [
            {
                "title": "Step 1 — unittest TestCase, setUp & tearDown",
                "body": "Class-based tests in the standard library — familiar if you know JUnit or NUnit.<div class=\"step-pre\">import unittest\n\nclass TestMath(unittest.TestCase):\n    def setUp(self):\n        self.nums = [1, 2, 3]\n\n    def tearDown(self):\n        pass   # cleanup after each test\n\n    def test_sum(self):\n        self.assertEqual(sum(self.nums), 6)</div>",
            },
            {
                "title": "Step 2 — Order of execution",
                "body": "For each test method: setUp → test → tearDown. Class-level: setUpClass → tests → tearDownClass.<div class=\"step-pre\"># per test:\n# 1. setUp()\n# 2. test_something()\n# 3. tearDown()\n\n# class level (once):\n# setUpClass() ... tearDownClass()</div>",
            },
            {
                "title": "Step 3 — Assert methods",
                "body": "unittest provides many assertion helpers beyond plain <code>assert</code>.<table class=\"data-tbl\"><tr><th>Method</th><th>Checks</th></tr><tr><td><code>assertEqual(a, b)</code></td><td>a == b</td></tr><tr><td><code>assertTrue(x)</code></td><td>bool(x) is True</td></tr><tr><td><code>assertIn(a, b)</code></td><td>a in b</td></tr><tr><td><code>assertRaises(Exc)</code></td><td>exception raised</td></tr></table>",
            },
            {
                "title": "Step 4 — unittest.mock",
                "body": "Replace real dependencies with fakes — essential for isolating unit tests.<div class=\"step-pre\">from unittest.mock import patch, MagicMock\n\n@patch(\"myapp.requests.get\")\ndef test_fetch(mock_get):\n    mock_get.return_value.json.return_value = {\"ok\": True}\n    result = fetch_data()\n    assert result[\"ok\"] is True\n    mock_get.assert_called_once()</div>",
            },
            {
                "title": "Step 5 — pytest basics",
                "body": "Plain functions with <code>assert</code> — less boilerplate, powerful fixtures.<div class=\"step-pre\"># test_math.py\ndef test_add():\n    assert 2 + 2 == 4\n\ndef test_divide():\n    assert 10 / 2 == 5\n\n# run: pytest test_math.py -v</div>",
            },
        ],
        "interview_qa": [
            {"q": "pytest vs unittest?", "a": "pytest uses plain assert and less boilerplate. unittest is in the standard library and class-based. Many teams prefer pytest for new projects."},
            {"q": "What makes a good test name?", "a": "Describes behavior: <code>test_login_rejects_empty_password</code> — not <code>test1</code>."},
            {"q": "Why mock external calls?", "a": "Tests should be fast, deterministic, and not depend on network or database. Mock <code>requests.get</code> to return fake data."},
            {"q": "setUp vs setUpClass?", "a": "<code>setUp</code> runs before each test. <code>setUpClass</code> runs once before all tests in the class — for expensive shared setup."},
        ],
    },
    20: {
        "steps": [
            {
                "title": "Step 1 — threading.Thread & Lock",
                "body": "Threads share memory within one process. Use <code>Lock</code> to prevent race conditions.<div class=\"step-pre\">import threading\n\ncounter = 0\nlock = threading.Lock()\n\ndef increment():\n    global counter\n    with lock:\n        counter += 1\n\nt = threading.Thread(target=increment)\nt.start()\nt.join()</div>",
            },
            {
                "title": "Step 2 — GIL",
                "body": "Global Interpreter Lock — only one thread executes Python bytecode at a time in CPython.<table class=\"data-tbl\"><tr><th>Task type</th><th>Threads help?</th></tr><tr><td>I/O-bound (network, disk)</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td></tr><tr><td>CPU-bound (math, parsing)</td><td class=\"cell-no\"><span class=\"yn-no\"></span>No — use multiprocessing</td></tr></table><p class=\"step-result\"><b>Why I/O works:</b> threads release the GIL while waiting on I/O.</p>",
            },
            {
                "title": "Step 3 — multiprocessing workaround",
                "body": "Separate processes bypass the GIL — each has its own Python interpreter and memory.<div class=\"step-pre\">from multiprocessing import Process\n\ndef heavy(n):\n    print(sum(i*i for i in range(n)))\n\nif __name__ == \"__main__\":\n    p = Process(target=heavy, args=(1_000_000,))\n    p.start()\n    p.join()</div>",
            },
            {
                "title": "Step 4 — concurrent.futures",
                "body": "High-level API for thread and process pools.<div class=\"step-pre\">from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor\n\nwith ThreadPoolExecutor(max_workers=4) as pool:\n    results = list(pool.map(fetch_url, urls))\n\nwith ProcessPoolExecutor() as pool:\n    results = list(pool.map(compute, big_jobs))</div>",
            },
        ],
        "interview_qa": [
            {"q": "What is the GIL?", "a": "A lock in CPython so only one thread executes Python bytecode at a time. I/O-bound tasks still benefit from threads; CPU-bound tasks need multiprocessing."},
            {"q": "Thread vs process?", "a": "Thread: shared memory, lightweight, GIL-limited for CPU. Process: separate memory, heavier, true parallelism for CPU work."},
            {"q": "Why if __name__ == \"__main__\" for multiprocessing?", "a": "On Windows, child processes re-import the module. Without the guard, code at module level runs again in each child — causing infinite spawn loops."},
            {"q": "ThreadPoolExecutor vs manual threads?", "a": "Executor manages a pool, queues work, and returns futures. Cleaner than manually creating and joining many threads."},
        ],
    },
    26: {
        "steps": [
            {
                "title": "Step 1 — contextlib.contextmanager",
                "body": "Write a context manager with <code>yield</code> between setup and teardown — no full class needed.<div class=\"step-pre\">from contextlib import contextmanager\n\n@contextmanager\ndef temp_file(path):\n    f = open(path, \"w\", encoding=\"utf-8\")\n    try:\n        yield f\n    finally:\n        f.close()\n\nwith temp_file(\"out.txt\") as f:\n    f.write(\"data\")</div>",
            },
            {
                "title": "Step 2 — __enter__ & __exit__",
                "body": "The protocol behind <code>with</code>. <code>__enter__</code> runs at start; <code>__exit__</code> runs at end (even on error).<div class=\"step-pre\">class ManagedResource:\n    def __enter__(self):\n        print(\"acquire\")\n        return self\n\n    def __exit__(self, exc_type, exc, tb):\n        print(\"release\")\n        return False   # don't suppress exceptions\n\nwith ManagedResource() as r:\n    print(\"working\")</div>",
            },
        ],
        "interview_qa": [
            {"q": "How does with work under the hood?", "a": "It calls the object's <code>__enter__</code> method, runs your block, then <code>__exit__</code> always runs for cleanup."},
            {"q": "contextmanager vs class-based?", "a": "<code>@contextmanager</code> is shorter for simple setup/teardown. A class is better when you need complex state or reusable configuration."},
            {"q": "What does __exit__ return True do?", "a": "Suppresses the exception — rare and use carefully. Returning <code>False</code> or <code>None</code> lets the exception propagate."},
            {"q": "What objects are context managers?", "a": "Files (<code>open</code>), locks (<code>threading.Lock</code>), database connections, and anything with <code>__enter__</code>/<code>__exit__</code>."},
        ],
    },
    21: {
        "steps": [
            {
                "title": "Step 1 — asyncio event loop",
                "body": "The loop schedules and runs coroutines cooperatively on one thread — ideal for many concurrent I/O waits.<div class=\"step-pre\">import asyncio\n\nasync def main():\n    print(\"start\")\n    await asyncio.sleep(1)\n    print(\"done\")\n\nasyncio.run(main())   # creates and runs the loop</div>",
            },
            {
                "title": "Step 2 — async def, await & coroutines",
                "body": "<code>async def</code> defines a coroutine. <code>await</code> pauses until that operation completes — only inside <code>async def</code>.<div class=\"step-pre\">async def fetch(url):\n    await asyncio.sleep(0.5)   # simulate I/O\n    return f\"data from {url}\"\n\nasync def main():\n    result = await fetch(\"api/users\")\n    print(result)</div>",
            },
            {
                "title": "Step 3 — asyncio.gather & asyncio.run",
                "body": "<code>gather</code> runs multiple coroutines concurrently. <code>run</code> is the entry point.<div class=\"step-pre\">async def main():\n    results = await asyncio.gather(\n        fetch(\"/a\"),\n        fetch(\"/b\"),\n        fetch(\"/c\"),\n    )\n    print(results)\n\nasyncio.run(main())</div>",
            },
            {
                "title": "Step 4 — Async context managers & iterators",
                "body": "Async versions of <code>with</code> and <code>for</code> for non-blocking I/O resources.<div class=\"step-pre\">class AsyncResource:\n    async def __aenter__(self):\n        await connect()\n        return self\n    async def __aexit__(self, *args):\n        await disconnect()\n\nasync def main():\n    async with AsyncResource() as r:\n        async for item in r.stream():\n            process(item)</div>",
            },
        ],
        "interview_qa": [
            {"q": "async vs threading?", "a": "Threading uses OS threads and the GIL. Async uses one thread and cooperatively switches during awaits — great for many concurrent I/O connections."},
            {"q": "Can you use time.sleep in async code?", "a": "No — it blocks the whole event loop. Use <code>await asyncio.sleep()</code> instead."},
            {"q": "When NOT to use async?", "a": "CPU-heavy work blocks the loop. Use threads, multiprocessing, or run CPU work in <code>asyncio.to_thread()</code>."},
            {"q": "What does asyncio.gather do?", "a": "Runs multiple coroutines concurrently and returns results in order. If one fails, others may still complete depending on options."},
        ],
    },
    27: {
        "steps": [
            {
                "title": "Step 1 — venv: create, activate & deactivate",
                "body": "An isolated Python environment per project — separate packages from system Python.<div class=\"step-pre\"># create\npython -m venv .venv\n\n# activate (Windows PowerShell)\n.venv\\Scripts\\activate\n\n# activate (Linux/Mac)\nsource .venv/bin/activate\n\n# deactivate\ndeactivate</div><p class=\"step-result\"><b>Prompt shows:</b> <code>(.venv)</code> when active.</p>",
            },
            {
                "title": "Step 2 — pip install, freeze & requirements.txt",
                "body": "Install packages into the active venv. Freeze pins exact versions for teammates and CI.<div class=\"step-pre\">pip install pytest requests\npip list\npip freeze &gt; requirements.txt\n\n# teammate setup:\npip install -r requirements.txt</div>",
            },
            {
                "title": "Step 3 — pyenv",
                "body": "Manage multiple Python versions on one machine — switch per project or directory.<div class=\"step-pre\"># install pyenv, then:\npyenv install 3.12.0\npyenv local 3.12.0    # .python-version file\npython --version      # 3.12.0\n\n# combine with venv:\npython -m venv .venv</div><p class=\"step-result\"><b>pyenv</b> picks the Python version. <b>venv</b> isolates packages for that project.</p>",
            },
        ],
        "interview_qa": [
            {"q": "Why use a virtual environment?", "a": "Project A might need Django 4, project B needs Django 5. venv isolates packages so they do not conflict."},
            {"q": "requirements.txt vs pyproject.toml?", "a": "<code>requirements.txt</code> is a flat pinned list from <code>pip freeze</code>. <code>pyproject.toml</code> is modern metadata + dependencies for tools like poetry or pip."},
            {"q": "pyenv vs venv?", "a": "pyenv switches Python interpreter versions. venv creates an isolated package environment for one project. Use both together."},
            {"q": "What happens if you forget to activate venv?", "a": "<code>pip install</code> may install to global Python — version conflicts across projects. Always check for <code>(.venv)</code> in prompt."},
        ],
    },
    29: {
        "steps": [
            {"title": "Step 1 — Portfolio overview", "body": "Python-Set2 has six areas: basics, exercises, pandas, Django, DRF, Pipecat voice AI."},
            {"title": "Step 2 — Learning path", "body": "Slides → Projects/ drills → Set2 real apps. Each area maps to interview talking points."},
            {"title": "Step 3 — Demo readiness", "body": "Pick 2–3 folders you can open and explain in a mock interview — structure, entry point, tests."},
        ],
        "interview_qa": [
            {"q": "How do you present your Python portfolio?", "a": "I walk through pythonBasics for fundamentals, google-python-exercises for files/regex, Django/DRF for web APIs, and Pipecat for voice AI — each with a clear entry file."},
        ],
    },
    30: {
        "steps": [
            {"title": "Step 1 — pythonBasics modules", "body": "Seven folders: MyClass, MyCollections, MyLoops, MyModules, MyExceptionHandling, MyDebug, MyUnitTesting."},
            {"title": "Step 2 — One topic per folder", "body": "Each has runnable scripts — study slides first, then run and modify the matching folder."},
            {"title": "Step 3 — MyClass focus", "body": "Inheritance, polymorphism, dunder methods — core OOP interview material."},
        ],
        "interview_qa": [
            {"q": "What is in pythonBasics?", "a": "Focused modules per curriculum topic — MyUnitTesting shows pytest patterns; MyClass shows OOP with real runnable examples."},
        ],
    },
    31: {
        "steps": [
            {"title": "Step 1 — google-python-exercises", "body": "Classic puzzles: babynames (regex), copyspecial (files), logpuzzle — small focused scripts."},
            {"title": "Step 2 — pandas notebooks", "body": "Titanic and FIFA CSV analysis — <code>read_csv</code>, <code>groupby</code>, missing values."},
            {"title": "Step 3 — Data skills", "body": "Like LINQ on in-memory tables — filter, group, aggregate without a database."},
        ],
        "interview_qa": [
            {"q": "How did you practice data analysis?", "a": "Jupyter notebooks on Titanic — load CSV, clean nulls, groupby survival rates. Shows pandas fluency beyond toy scripts."},
        ],
    },
    32: {
        "steps": [
            {"title": "Step 1 — Django meeting_planner", "body": "Full MVT app — models, templates, migrations, auth."},
            {"title": "Step 2 — DRF inventory", "body": "REST API with serializers and ViewSets — JSON in/out like Web API projects in C#."},
            {"title": "Step 3 — Compare frameworks", "body": "Django batteries-included vs FastAPI lightweight + type hints — know when to pick each."},
        ],
        "interview_qa": [
            {"q": "Django vs DRF vs FastAPI?", "a": "Django for full web apps with admin and ORM. DRF adds REST on Django. FastAPI for modern async APIs with Pydantic validation — I have examples of both."},
        ],
    },
    33: {
        "steps": [
            {"title": "Step 1 — Voice pipeline", "body": "Speech-to-text → LLM → text-to-speech, often over WebRTC for real-time audio."},
            {"title": "Step 2 — Pipecat phases", "body": "phase1 local services, phase2 full pipeline, voice-bouncer IVR-style auth demo."},
            {"title": "Step 3 — Built incrementally", "body": "Local STT/TTS first, then framework integration — shows systematic debugging."},
        ],
        "interview_qa": [
            {"q": "Explain your voice AI project.", "a": "Pipecat pipeline: audio in, STT to text, LLM for logic, TTS back to audio. voice-bouncer simulates IVR — greeting, member ID, zip validation."},
        ],
    },
    34: {
        "steps": [
            {"title": "Step 1 — Folder conventions", "body": "Separate routes, services, models, tests, config — thin routes, fat services."},
            {"title": "Step 2 — Entry point", "body": "<code>main.py</code> or <code>manage.py</code> — know where execution starts."},
            {"title": "Step 3 — Tests outside app", "body": "<code>tests/</code> folder at project root — pytest discovers <code>test_*.py</code>."},
        ],
        "interview_qa": [
            {"q": "How do you structure a Python project?", "a": "main entry, routes thin, business logic in services, schemas/models separate, tests/ at root. Django uses apps per domain; Pipecat uses processors for audio streams."},
        ],
    },
    35: {
        "steps": [
            {"title": "Step 1 — Syntax shifts", "body": "No <code>int x</code> declarations, indentation not braces, <code>self</code> not <code>this</code> (but same idea). <code>elif</code> not <code>else if</code>. <code>True</code>/<code>False</code> are capitalized."},
            {"title": "Step 2 — pass & empty blocks", "body": "<div class=\"callout\"><b>pass</b> has no single C# keyword.</div><b>Closest:</b> empty <code>{ }</code> when a method or block must exist but do nothing yet.<br><b>Stronger stub:</b> <code>throw new NotImplementedException()</code> ≈ <code>raise NotImplementedError()</code>.<br><b>C# interfaces</b> declare methods without a body — Python uses <code>pass</code> inside <code>class</code> or <code>def</code> instead.<div class=\"step-pre\"># Python stub\ndef save_report():\n    pass\n\n# C# equivalent\n# void SaveReport() { }</div>"},
            {"title": "Step 3 — Type system & null", "body": "Duck typing default; type hints optional. C# interfaces → Python ABC or duck typing.<br><b>Null trap:</b> C# <code>x == null</code> → Python <code>x is None</code> (not <code>== None</code>).<br><b>Identity:</b> C# <code>ReferenceEquals</code> → Python <code>is</code>."},
            {"title": "Step 4 — Tooling & patterns", "body": "<code>venv</code> + <code>pip</code> ≈ NuGet per project. <code>pytest</code> ≈ xUnit. Django/FastAPI ≈ ASP.NET.<br><b>using</b> ≈ <code>with</code>. LINQ <code>.Where()</code> ≈ list comprehension. <code>Main()</code> ≈ <code>if __name__ == \"__main__\":</code>."},
            {"title": "Step 5 — Similarities", "body": "Both OOP, both rich web stacks, try/except ≈ try/catch, both strong for APIs and automation. <code>async</code>/<code>await</code> exist in both — Python uses coroutines instead of <code>Task&lt;T&gt;</code>."},
        ],
        "interview_qa": [
            {"q": "What is the C# equivalent of pass?", "a": "No exact keyword. Empty <code>{ }</code> for a stub block. <code>throw new NotImplementedException()</code> ≈ <code>raise NotImplementedError()</code> when the method must exist but is not ready. C# interfaces use declaration without body — Python uses <code>pass</code> in <code>def</code> or <code>class</code>."},
            {"q": "Coming from C#, what surprised you in Python?", "a": "Indentation as syntax, dynamic typing, mutable default argument trap, and that <code>is</code> vs <code>==</code> matters. Similarities: OOP, exceptions, and large package ecosystems."},
            {"q": "null vs None — how do you test?", "a": "C#: <code>if (x == null)</code>. Python: <code>if x is None:</code> — use <code>is</code>, not <code>==</code>, because there is only one <code>None</code> object."},
            {"q": "this vs self?", "a": "Same role — current instance. C# <code>this</code> is implicit in instance methods. Python requires <code>self</code> as the first parameter explicitly: <code>def greet(self):</code>."},
        ],
    },
    4: {
        "steps": [
            {"title": "Step 1 — What is a PEP?", "body": "PEP = Python Enhancement Proposal — design documents for language features, style, and packaging. Some are informational; others become official standards."},
            {"title": "Step 2 — PEP 8 style", "body": "4-space indent, <code>snake_case</code> for functions/variables, <code>PascalCase</code> for classes, imports grouped (stdlib → third-party → local). Linters enforce this in CI."},
            {"title": "Step 3 — PEP 257 & type hints", "body": "Docstrings describe modules, classes, and public functions. PEP 484/585 define type hints — use <code>list[int]</code> in Python 3.9+."},
            {"title": "Step 4 — Packaging PEPs", "body": "PEP 440 (versions), 508 (dependency specifiers), 518/621 (<code>pyproject.toml</code>) — how modern Python projects declare dependencies."},
        ],
        "interview_qa": [
            {"q": "What is PEP 8?", "a": "The official Python style guide — naming, indentation, line length, import order. Not enforced by the interpreter; teams use ruff, flake8, or Black."},
            {"q": "What is the Zen of Python?", "a": "PEP 20 — aphorisms like 'Readability counts' and 'Explicit is better than implicit'. Run <code>import this</code> in the REPL."},
            {"q": "PEP 8 vs a linter?", "a": "PEP 8 is the document; linters automate checks. Black formats code; ruff/flake8 report violations. CI fails on style drift."},
        ],
    },
    13: {
        "steps": [
            {"title": "Step 1 — Reference counting", "body": "Every object tracks how many references point to it. When count hits zero, memory is reclaimed immediately — fast for most objects."},
            {"title": "Step 2 — Garbage collector", "body": "Circular references (A→B→A) keep refcounts &gt; 0 forever. The <code>gc</code> module periodically finds and breaks these cycles."},
            {"title": "Step 3 — Generations", "body": "GC uses three generations — young objects collected often, old objects rarely. Tuning is rare; know it exists for leak debugging."},
            {"title": "Step 4 — Practical tips", "body": "<code>del</code> removes a name, not necessarily the object. Use <code>with</code> for files. Long-lived caches can cause memory growth — profile before optimizing."},
        ],
        "interview_qa": [
            {"q": "How does Python free memory?", "a": "Primarily reference counting — when no names reference an object, it is freed. A generational GC handles circular references."},
            {"q": "What is a circular reference?", "a": "Two or more objects reference each other so refcounts never reach zero. Example: parent/child nodes pointing at each other — needs <code>gc.collect()</code> or weakref."},
            {"q": "del x vs x = None?", "a": "<code>del x</code> removes the name from the namespace. <code>x = None</code> rebinds to None but keeps the name. Neither guarantees instant destruction if other references exist."},
        ],
    },
    22: {
        "steps": [
            {"title": "Step 1 — Why not print()?", "body": "Production needs levels, timestamps, and routing to files/agents. <code>logging</code> is the standard library solution — like ILogger in .NET."},
            {"title": "Step 2 — Levels", "body": "DEBUG &lt; INFO &lt; WARNING &lt; ERROR &lt; CRITICAL. Set root level to INFO in prod; DEBUG only when troubleshooting."},
            {"title": "Step 3 — Logger per module", "body": "<code>logger = logging.getLogger(__name__)</code> — hierarchical names (<code>app.orders.service</code>) map to configuration."},
            {"title": "Step 4 — Handlers & format", "body": "Console handler for dev, RotatingFileHandler for disk. Use <code>%</code> formatting in log calls — not f-strings — for lazy evaluation."},
        ],
        "interview_qa": [
            {"q": "logging vs print?", "a": "Logging has levels, can filter, add timestamps, route to files/syslog, and disable debug noise in production without code changes."},
            {"q": "Why logger.info('x=%s', x) instead of f-string?", "a": "Lazy formatting — if INFO is filtered out, the string is never built. f-strings always evaluate immediately."},
            {"q": "How do you log an exception with traceback?", "a": "Inside <code>except</code>: <code>logger.exception('message')</code> or <code>logger.error('msg', exc_info=True)</code>."},
        ],
    },
    14: {
        "steps": [
            {"title": "Step 1 — BaseModel", "body": "Subclass <code>BaseModel</code> with typed fields — Pydantic validates on construction and coercion (e.g. string <code>'25'</code> → int <code>25</code>)."},
            {"title": "Step 2 — Validation", "body": "<code>Field(ge=18)</code> for constraints. <code>@field_validator</code> for custom rules. Invalid data raises <code>ValidationError</code> with field paths."},
            {"title": "Step 3 — Serialization", "body": "v2: <code>model_validate(dict)</code> in, <code>model_dump()</code> out. For ORM rows use <code>model_config = {'from_attributes': True}</code>."},
            {"title": "Step 4 — FastAPI integration", "body": "Route parameters typed as Pydantic models auto-parse JSON bodies and return 422 with structured errors — no manual validation boilerplate."},
        ],
        "interview_qa": [
            {"q": "What is Pydantic used for?", "a": "Runtime validation and parsing using type hints — API schemas, config loading, data pipelines. Core of FastAPI request/response models."},
            {"q": "Pydantic vs dataclasses?", "a": "Dataclasses structure data; Pydantic validates, coerces types, and gives rich errors. Use Pydantic at API boundaries."},
            {"q": "What happens on validation failure?", "a": "<code>ValidationError</code> with a list of errors per field — FastAPI converts this to HTTP 422 JSON for clients."},
        ],
    },
    28: {
        "steps": [
            {"title": "Step 1 — Layered stack", "body": "FastAPI (HTTP) + Pydantic (schemas) + SQLAlchemy (ORM) + database. Routes stay thin; services own transactions and business rules."},
            {"title": "Step 2 — Session per request", "body": "<code>Depends(get_db)</code> yields a SQLAlchemy session, commits on success, closes in <code>finally</code> — like scoped DbContext in EF Core."},
            {"title": "Step 3 — ORM vs schema", "body": "ORM models map tables; Pydantic schemas map API contracts. Never expose ORM internals directly — use response models."},
            {"title": "Step 4 — Async note", "body": "FastAPI supports async routes; use async SQLAlchemy (2.0 style) or run sync ORM in thread pool for I/O-bound DB work."},
        ],
        "interview_qa": [
            {"q": "How does FastAPI + SQLAlchemy compare to ASP.NET + EF?", "a": "FastAPI ≈ minimal Web API; Pydantic ≈ DTO validation; SQLAlchemy session ≈ DbContext; Depends ≈ DI scoped services."},
            {"q": "Where does business logic live?", "a": "In a service layer — not in route handlers. Routes parse HTTP, call service, return schema. Keeps tests and reuse clean."},
            {"q": "Why separate Pydantic from SQLAlchemy models?", "a": "API shape ≠ database shape — hide internal columns, version APIs, and validate input without leaking ORM details."},
        ],
    },
}
