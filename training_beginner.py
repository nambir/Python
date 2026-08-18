"""Beginner step-by-step explanations and interview Q&A for each slide."""

from slide_csharp_popups import csharp_compare_btn
from slide_io import io_split, side_by_side


def _ex_error_diagram() -> str:
    """Three-column NameError / TypeError / ValueError diagram (blue title, code, red message)."""
    return (
        '<div class="ex-row">'
        '<div class="ex-card">'
        '<div class="ex-title">NameError</div>'
        '<div class="ex-code">z * 1</div>'
        '<div class="ex-msg">NameError: name \'z\' is not defined</div>'
        "</div>"
        '<div class="ex-card">'
        '<div class="ex-title">TypeError</div>'
        '<div class="ex-code">10 + "Hello"</div>'
        '<div class="ex-msg">TypeError: unsupported operand type(s) for +:<br>\'int\' and \'str\'</div>'
        "</div>"
        '<div class="ex-card">'
        '<div class="ex-title">ValueError</div>'
        '<div class="ex-code">int("Hello")</div>'
        '<div class="ex-msg">ValueError: invalid literal for int()<br>with base 10: \'Hello\'</div>'
        "</div>"
        "</div>"
    )


def _ex_ladder_path(try_line: str, hit: str) -> str:
    """Same try/except/else/finally ladder; yellow-highlight the path that runs."""

    def block(lines: list[str], active: bool) -> str:
        text = "\n".join(lines)
        if active:
            return f'<mark class="hl-path">{text}</mark>'
        return text

    name = block(
        ['except NameError as err:', '    print("Name Error:", err)'],
        hit == "NameError",
    )
    typ = block(
        ['except TypeError as err:', '    print("Type Error:", err)'],
        hit == "TypeError",
    )
    val = block(
        ['except ValueError as err:', '    print("Value Error:", err)'],
        hit == "ValueError",
    )
    exc = block(
        ['except Exception as err:', '    print("Exception:", err)'],
        hit == "Exception",
    )
    els = block(
        ["else:", '    print("no error — success path")'],
        hit == "else",
    )
    # finally always runs — highlight on every path
    fin = block(
        ["finally:", '    print("cleanup always")'],
        True,
    )
    return (
        '<div class="step-pre">'
        "try:\n"
        f"    {try_line}\n"
        f"{name}\n"
        f"{typ}\n"
        f"{val}\n"
        f"{exc}\n"
        f"{els}\n"
        f"{fin}"
        "</div>"
    )


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
                "body": "Frozenset is like a set but cannot change after creation. It can be a dictionary key.<div class=\"step-pre\">perms = frozenset({\"read\", \"write\"})\n# perms.add(\"admin\")     # AttributeError — cannot change\n\nstore = {}\nstore[frozenset({1, 2})] = \"combo\"   # OK as dict key</div>",
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
                "body": "<div class=\"callout\"><b>{} tip:</b> <code>store = {}</code> creates an empty <b>dictionary</b>, not a set. Empty set is <code>set()</code>. A non-empty set looks like <code>{\"a\", \"b\"}</code> (values only). A dict looks like <code>{\"id\": 1}</code> (key: value).</div><div class=\"step-pre\">store = {}                 # empty DICT (not set!)\nstore[{\"id\": 1}] = \"data\"  # TypeError: unhashable type: 'dict'\nstore[{\"a\", \"b\"}] = \"x\"    # TypeError: unhashable type: 'set'\n\n# Compare:\nempty_dict = {}            # dict\nempty_set = set()          # set\nmy_set = {\"a\", \"b\"}        # set (no colon)\nmy_dict = {\"id\": 1}        # dict (has colon)</div><p class=\"step-result\"><b>Fix:</b> use <code>tuple</code> or <code>frozenset</code> instead of list/set as the <i>key</i>.</p>",
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
                "body": (
                    "<div class=\"callout\"><b>pass</b> = this block is intentionally empty for now. "
                    "It is a <b>stub</b> — define the shape today, add real code later. "
                    "When you implement it, remove <code>pass</code> and write your logic.</div>"
                    "<code>pass</code> does nothing at runtime, but Python accepts it as a valid "
                    "statement when syntax requires an indented body."
                    '<div class="step-pre">'
                    "# stub — implement later\n"
                    "def save_report():\n"
                    "    pass   # this block is empty for now\n"
                    "\n"
                    "# later, replace pass with real code:\n"
                    "# def save_report():\n"
                    '#     with open("report.txt", "w") as f:\n'
                    '#         f.write("data")\n'
                    "\n"
                    "class ValidationError(Exception):\n"
                    "    pass   # empty exception class"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Where else <code>pass</code> can appear</b> — including a common "
                    "<b>bug</b> in <code>except</code> blocks:"
                    "</p>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-good"><span class="mc-lbl">&#10004; OK uses of pass</span>'
                    '<div class="step-pre">'
                    "def save_report():\n"
                    "    pass                 # stub function\n"
                    "\n"
                    "class ValidationError(Exception):\n"
                    "    pass                 # empty exception class\n"
                    "\n"
                    "if True:\n"
                    "    pass                 # TODO placeholder only\n"
                    "\n"
                    "try:\n"
                    "    result = risky()\n"
                    "except ValueError:\n"
                    "    pass                 # rare: ignore ONE known error\n"
                    "    # (prefer log / handle — empty ignore is still risky)"
                    "</div>"
                    '<p style="font-size:11px;margin:6px 8px;line-height:1.4">'
                    "<b>Idea:</b> <code>pass</code> only fills a required empty body. "
                    "Stubs and empty classes are the usual good cases."
                    "</p>"
                    "</div>"
                    '<div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug — bare except: pass</span>'
                    '<div class="step-pre">'
                    "try:\n"
                    "    result = risky()\n"
                    "except:      # catches SystemExit, KeyboardInterrupt!\n"
                    "    pass       # silently swallows ALL exceptions"
                    "</div>"
                    '<p style="font-size:11px;margin:6px 8px;line-height:1.4">'
                    "<b>Why bad:</b> bare <code>except:</code> = <code>BaseException</code> "
                    "(includes Ctrl+C / <code>sys.exit()</code>). "
                    "<code>pass</code> then hides every error — hard to shut down or debug. "
                    "Prefer <code>except ValueError:</code> or <code>except Exception:</code> "
                    "and log / re-raise. See slide <b>Exception Handling</b>."
                    "</p>"
                    "</div>"
                    "</div>"
                    "<p class=\"step-result\"><b>Loop else:</b> runs only if the loop did not hit "
                    "<code>break</code>.</p>"
                    '<div class="step-pre">'
                    "for x in [1, 2, 3]:\n"
                    "    if x == 99:\n"
                    "        break\n"
                    "else:\n"
                    '    print("not found")'
                    "</div>"
                ),
            },
        ],
        "interview_qa": [
            {"q": "How do blocks work without braces?", "a": "Indentation (usually 4 spaces) after a colon defines the block. Dedent ends the block. Mixing tabs and spaces causes <code>IndentationError</code>."},
            {"q": "When is for-else useful?", "a": "Search loops: loop to find an item; if found, <code>break</code>. The <code>else</code> clause runs only when nothing matched — clean 'not found' handling."},
            {"q": "range(5) vs range(2, 10, 2)?", "a": "<code>range(5)</code> → 0–4. <code>range(start, stop, step)</code> — stop is exclusive. <code>range(2, 10, 2)</code> → 2, 4, 6, 8."},
            {"q": "What is pass used for?", "a": "<b>pass = this block is intentionally empty for now.</b> Use it as a stub in an empty <code>def</code>, <code>class</code>, or unfinished branch. Later, remove <code>pass</code> and add your real code. Never use bare <code>except: pass</code> — that swallows Ctrl+C and all errors."},
            {"q": "Is except: pass a valid use of pass?", "a": "<code>pass</code> can appear there as an empty body, but bare <code>except: pass</code> is a <b>bug</b> — it catches <code>BaseException</code> (including <code>KeyboardInterrupt</code> / <code>SystemExit</code>) and hides everything. Catch a specific type, or at least <code>Exception</code>, and log or re-raise."},
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
                "body": "Build a dict from key-value expressions.<div class=\"step-pre\">nums = [1, 2, 3]\nsq_map_dict = {n: n * n for n in nums}\n# {1: 1, 2: 4, 3: 9}\n\nfiltered = {k: v for k, v in sq_map_dict.items() if v &gt; 1}</div>",
            },
            {
                "title": "Step 4 — Generator expression",
                "body": "Parentheses instead of brackets — lazy, yields one item at a time, saves memory.<table class=\"data-tbl\"><tr><th>Feature</th><th>List comp</th><th>Generator</th></tr><tr><td>Syntax</td><td><code>[...]</code></td><td><code>(...)</code></td></tr><tr><td>Memory</td><td>All at once</td><td>One item at a time</td></tr><tr><td>Reusable?</td><td class=\"cell-yes\"><span class=\"yn-yes\"></span>Yes</td><td class=\"cell-no\"><span class=\"yn-no\"></span>Exhausted after one pass</td></tr></table><div class=\"step-pre\">gen = (x * x for x in range(1_000_000))\nnext(gen)   # 0\nnext(gen)   # 1</div>",
            },
            {
                "title": "Step 5 — yield means generator function",
                "body": "<b>Yes:</b> if a function uses <b>yield</b>, it is a <b>GENERATOR</b> function. Calling it returns a generator object (lazy). Same job with <code>return</code> of a list builds everything at once.<div class=\"step-pre\"># WITHOUT yield — normal function, full list in RAM\ndef squares_list(n):\n    out = []\n    for i in range(n):\n        out.append(i * i)\n    return out\n\n# WITH yield — generator function, one value at a time\ndef squares_gen(n):\n    for i in range(n):\n        yield i * i          # pause here; resume on next ask\n\nprint(squares_list(3))       # [0, 1, 4]  — all ready now\nprint(list(squares_gen(3)))  # [0, 1, 4]  — built only when consumed</div><p class=\"step-result\"><b>Hint:</b> <code>list(...)</code> is a Python <b>built-in function</b> (not a keyword). It consumes the generator and builds a normal list so you can see all values.</p><p class=\"step-result\"><b>Also:</b> <code>(x*x for x in ...)</code> is a generator <i>expression</i> (no <code>yield</code> keyword, same lazy idea).</p>",
            },
        ],
        "interview_qa": [
            {"q": "Why use a comprehension over a for loop?", "a": "Shorter and often clearer for simple transforms. <code>[n*n for n in range(10) if n%2==0]</code> is easier to read than a 4-line loop with append."},
            {"q": "List comprehension vs generator expression?", "a": "List builds everything in memory. Generator yields one value at a time — better for large data or pipelines."},
            {"q": "Does the word yield mean generator?", "a": "Yes — <code>yield</code> inside a function makes it a generator function. Without <code>yield</code>, a normal <code>return</code> ends after one result (or a full list)."},
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
                "body": "Anonymous one-expression function — good for short callbacks.<div class=\"step-pre\">multiply_by_two = lambda x: x * 2\nmultiply_by_two(5)   # 10\n\nsorted(pairs, key=lambda p: p[1])</div>",
            },
            {
                "title": "Step 5 — LEGB scope (3 variables, not one)",
                "body": "Python looks up names: <b>L</b>ocal → <b>E</b>nclosing → <b>G</b>lobal → <b>B</b>uiltin. If each level assigns <code>x = ...</code>, you get <b>3 separate variables</b> (3 bindings) that only share the name — not one shared variable.<div class=\"step-pre\">x = \"global\"              # binding 1 — global\n\ndef outer():\n    x = \"enclosing\"       # binding 2 — enclosing\n    def inner():\n        x = \"local\"       # binding 3 — local\n        print(x)          # local\n        print(id(x))      # object identity\n    print(id(x))\n    inner()\n\nprint(id(x))\nouter()\n# three different id() values → three objects</div><p class=\"step-result\"><b><code>id(obj)</code>:</b> unique int for that object while alive (CPython ≈ memory address). Same <code>id</code> means the same object (<code>a is b</code>). Different values of <code>x</code> here → different ids.</p>",
            },
            {
                "title": "Step 6 — Closures",
                "body": "An inner function remembers variables from its enclosing scope even after the outer function returns.<div class=\"step-pre\">def make_multiplier(n):\n    def multiply(x):\n        return x * n\n    return multiply\n\ntimes3 = make_multiplier(3)\ntimes3(10)   # 30</div>",
            },
        ],
        "interview_qa": [
            {"q": "What is wrong with def f(items=[])?", "a": "The default list is created once at definition time and shared across all calls. Use <code>def f(items=None): items = items or []</code> instead."},
            {"q": "What are *args and **kwargs?", "a": "<code>*args</code> is a tuple of extra positional arguments. <code>**kwargs</code> is a dict of extra keyword arguments. Useful for wrappers and decorators."},
            {"q": "What is LEGB?", "a": "Name lookup order: Local (inside function), Enclosing (outer functions), Global (module), Builtin (built-in names like <code>len</code>). If each nested level assigns <code>x = ...</code>, those are <b>three different variables</b> (three bindings), not one shared variable."},
            {"q": "What does id() do?", "a": "<code>id(obj)</code> returns the object’s identity — a unique integer while the object is alive (in CPython related to its memory address). <code>id(a) == id(b)</code> means the same object (same as <code>a is b</code>). <code>==</code> compares values, which can be equal even when ids differ."},
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
                "body": (
                    "A class is a blueprint. An object is an instance. "
                    "<code>__init__</code> initializes state; <code>self</code> refers to the current instance. "
                    "<b>__init__ is optional</b> — only write it when you need starting values."
                    + io_split(
                        'class Dog:\n'
                        '    def __init__(self, name):\n'
                        '        self.name = name\n'
                        '\n'
                        '    def bark(self):\n'
                        '        return f"{self.name} says woof!"\n'
                        '\n'
                        'my_dog = Dog("Rex")\n'
                        'print(my_dog.bark())',
                        {9: "Rex says woof!"},
                    )
                ),
            },
            {
                "title": "Step 2 — Same name: class vs function vs method",
                "body": (
                    "<code>Toy(\"ball\")</code> looks like a function call, but <code>Toy</code> is normally a <b>class</b>. "
                    "If a <b>function</b> later uses the same name, the class is <b>shadowed</b> (Python keeps the last binding). "
                    "A <b>method</b> named <code>Toy</code> does <b>not</b> replace the class."
                    + io_split(
                        'class Toy:\n'
                        '    def __init__(self, name):\n'
                        '        self.name = name\n'
                        '\n'
                        'a = Toy("ball")     # class → object\n'
                        'print(a.name)\n'
                        '\n'
                        'def Toy(name):      # same name — hides the class\n'
                        '    return f"fn:{name}"\n'
                        '\n'
                        'a = Toy("ball")     # now calls the FUNCTION\n'
                        'print(a)',
                        {6: "ball", 12: "fn:ball"},
                    )
                    + io_split(
                        '# Method named Toy — OK; class still works\n'
                        'class Toy:\n'
                        '    def __init__(self, name):\n'
                        '        self.name = name\n'
                        '    def Toy(self):\n'
                        '        return "method Toy"\n'
                        '\n'
                        'a = Toy("ball")     # still creates object\n'
                        'print(a.Toy())',
                        {9: "method Toy"},
                    )
                    + '<p class="step-result"><b>Best practice:</b> PascalCase for classes only. '
                    "Use <code>make_toy()</code> for a helper — never reuse the class name for a function.</p>"
                ),
            },
            {
                "title": "Step 3 — Inheritance: single, multiple & MRO",
                "body": (
                    "A child class inherits from one or more parents. MRO (Method Resolution Order) defines lookup order. "
                    "<code>Pet(Dog, Cat)</code> looks left→right: Dog before Cat, so <code>speak</code> is Dog’s \"woof\". "
                    "<b>Only the first match runs</b> — <code>Cat.speak</code> is <b>not</b> called afterward "
                    "(unless Dog’s method uses <code>super()</code> to continue the chain)."
                    + io_split(
                        'class Animal:\n'
                        '    def speak(self): return "..."\n'
                        '\n'
                        'class Dog(Animal):\n'
                        '    def speak(self): return "woof"\n'
                        '\n'
                        'class Cat(Animal):\n'
                        '    def speak(self): return "meow"\n'
                        '\n'
                        'class Pet(Dog, Cat):\n'
                        '    # multiple inheritance — Dog listed first\n'
                        '    # p.speak() → finds Dog.speak → STOPS (Cat.speak is NOT called)\n'
                        '    pass\n'
                        '\n'
                        'p = Pet()\n'
                        'print(p.speak())                          # only Dog.speak runs\n'
                        'print([c.__name__ for c in Pet.__mro__])  # Cat is next, but unused here',
                        {
                            16: "woof",
                            17: "['Pet', 'Dog', 'Cat', 'Animal', 'object']",
                        },
                    )
                    + '<p class="step-result"><b>Takeaway:</b> Cat is on the MRO list, '
                    "but <code>speak</code> lookup stopped at Dog.</p>"
                ),
            },
            {
                "title": "Step 4 — Encapsulation & _ convention",
                "body": (
                    "Python has <b>no true private fields</b> like C# <code>private</code>. "
                    "Access is by <b>convention</b> and (for <code>__</code>) a rename trick — not a lock."
                    "<p style=\"font-size:12px;margin:6px 0 8px;line-height:1.45\">"
                    "<b>So is encapsulation possible?</b> <b>Yes</b> — you still <b>bundle data + methods</b> "
                    "and mark internals as “don’t touch.” It is <b>soft</b> encapsulation (team discipline), "
                    "not a compiler lock. "
                    "<b>What shows it in the code?</b> "
                    "<code>self._balance</code> / <code>self.__pin</code> (hidden state) + "
                    "<code>deposit()</code> (the allowed way to change balance)."
                    "</p>"
                    "<ul style=\"margin:6px 0 8px 18px;font-size:12px;line-height:1.45\">"
                    "<li><b>Public</b> — normal name (<code>balance</code>): meant for callers to use.</li>"
                    "<li><b>“Private” by convention</b> — one underscore (<code>_balance</code>): "
                    "“internal — please don’t touch from outside.” Still fully reachable.</li>"
                    "<li><b>Name mangling</b> — two underscores (<code>__balance</code>): "
                    "Python renames it to <code>_ClassName__balance</code> so subclasses don’t "
                    "accidentally overwrite it. Stronger against accidents — <b>not security</b>.</li>"
                    "</ul>"
                    "<p style=\"font-size:12px;margin:0 0 8px;line-height:1.45\">"
                    "<b>Security means?</b> A real private field would <b>block</b> outside code. "
                    "In Python you can always write <code>obj._balance</code> or "
                    "<code>obj._BankAccount__balance</code> if you know the mangled name. "
                    "So <code>_</code> / <code>__</code> are for <b>team discipline and avoiding name clashes</b>, "
                    "not for hiding secrets from attackers."
                    "</p>"
                    + io_split(
                        'class BankAccount:\n'
                        '    def __init__(self, balance):\n'
                        '        self.owner = "Anu"           # public — OK to use\n'
                        '        self._balance = balance      # convention: internal\n'
                        '        self.__pin = "1234"         # mangled → _BankAccount__pin\n'
                        '\n'
                        '    def deposit(self, amount):\n'
                        '        self._balance += amount     # class methods OK\n'
                        '\n'
                        'a = BankAccount(100)\n'
                        'print(a.owner)                     # public\n'
                        'print(a._balance)                  # “private” — still works!\n'
                        'try:\n'
                        '    print(a.__pin)                 # mangled — AttributeError\n'
                        'except AttributeError as e:\n'
                        '    print(type(e).__name__ + ":", e)\n'
                        'print(a._BankAccount__pin)         # mangled name — still OK\n'
                        'print([k for k in a.__dict__])     # real attribute names',
                        {
                            11: "Anu",
                            12: "100",
                            16: "AttributeError: 'BankAccount' object has no attribute '__pin'",
                            17: "1234",
                            18: "['owner', '_balance', '_BankAccount__pin']",
                        },
                    )
                    + "<p class=\"step-result\"><b>Takeaway:</b> "
                    "<code>_</code> = please don’t; <code>__</code> = renamed; neither = locked. "
                    "<b>C# contrast:</b> <code>private</code> is enforced by the compiler — "
                    "Python’s <code>_balance</code> is a polite sign on an unlocked door.</p>"
                ),
            },
            {
                "title": "Step 5 — Polymorphism & overriding",
                "body": (
                    "Different classes share the same <b>method shape</b> (here: <code>speak()</code>). "
                    "Child methods <b>override</b> parent methods. "
                    "One function (<code>announce</code>) works with any object that has <code>speak()</code> — "
                    "Python picks the right version at runtime."
                    "<p style=\"font-size:12px;margin:6px 0 8px;line-height:1.45\">"
                    "<b>Interface keyword?</b> Python has <b>no</b> <code>interface</code> keyword like C#. "
                    "Saying “same interface” here means “same public methods” (duck typing), "
                    "not a C# <code>interface IAnimal</code> type. "
                    "Closest formal tool: <code>abc.ABC</code> + <code>@abstractmethod</code> (Step 6)."
                    "</p>"
                    + io_split(
                        'class Animal:\n'
                        '    def speak(self):\n'
                        '        return "..."          # base version\n'
                        '\n'
                        'class Dog(Animal):\n'
                        '    def speak(self):\n'
                        '        return "woof"        # overrides Animal.speak\n'
                        '\n'
                        'class Cat(Animal):\n'
                        '    def speak(self):\n'
                        '        return "meow"        # overrides Animal.speak\n'
                        '\n'
                        'def announce(animal):\n'
                        '    print(animal.speak())  # same call — different result\n'
                        '\n'
                        'announce(Dog())\n'
                        'announce(Cat())\n'
                        'announce(Animal())',
                        {16: "woof", 17: "meow", 18: "..."},
                    )
                    + '<p class="step-result"><b>Takeaway:</b> Same <code>announce()</code> — '
                    "Dog / Cat / Animal each use their own <code>speak()</code>.</p>"
                ),
            },
            {
                "title": "Step 6 — Abstract classes (abc)",
                "body": (
                    "Force subclasses to implement required methods using <code>abc.ABC</code> and "
                    "<code>@abstractmethod</code>. You <b>cannot</b> create <code>Shape()</code> directly — "
                    "only a complete child like <code>Circle</code>."
                    + io_split(
                        'from abc import ABC, abstractmethod\n'
                        '\n'
                        'class Shape(ABC):\n'
                        '    @abstractmethod\n'
                        '    def area(self):\n'
                        '        ...                 # must be implemented by child\n'
                        '\n'
                        'class Circle(Shape):\n'
                        '    def __init__(self, r):\n'
                        '        self.r = r\n'
                        '    def area(self):\n'
                        '        return 3.14 * self.r ** 2\n'
                        '\n'
                        'c = Circle(2)\n'
                        'print(c.area())\n'
                        '\n'
                        'try:\n'
                        '    Shape()                 # incomplete — blocked\n'
                        'except TypeError as e:\n'
                        '    print(type(e).__name__ + ":", e)',
                        {
                            15: "12.56",
                            20: "TypeError: Can't instantiate abstract class Shape without an "
                            "implementation for abstract method 'area'",
                        },
                    )
                    + '<p class="step-result"><b>Takeaway:</b> ABC = blueprint; '
                    "child must fill in every <code>@abstractmethod</code>.</p>"
                ),
            },
            {
                "title": "Step 7 — Dunder methods",
                "body": (
                    "Double-underscore methods customize built-in behavior. "
                    + csharp_compare_btn("dunder-methods")
                    + "<table class=\"data-tbl\"><tr><th>Method</th><th>Triggered by</th><th>Real use</th></tr>"
                    "<tr><td><code>__str__</code></td><td><code>print(obj)</code>, <code>str(obj)</code></td>"
                    "<td>emails, admin UI, friendly logs</td></tr>"
                    "<tr><td><code>__repr__</code></td><td><code>repr(obj)</code>, debugger, lists</td>"
                    "<td>Sentry, <code>logging %r</code>, REPL</td></tr>"
                    "<tr><td><code>__eq__</code></td><td><code>obj == other</code></td>"
                    "<td>compare by id/value, not memory</td></tr>"
                    "<tr><td><code>__len__</code></td><td><code>len(obj)</code></td>"
                    "<td>cart size, item count</td></tr></table>"
                    "<p style=\"font-size:12px;margin:8px 0 6px;line-height:1.45\">"
                    "<b>All four on one production-style model</b> (Order):"
                    "</p>"
                    + io_split(
                        'class Order:\n'
                        '    def __init__(self, order_id, customer, items):\n'
                        '        self.order_id = order_id\n'
                        '        self.customer = customer\n'
                        '        self.items = items          # list of product names\n'
                        '\n'
                        '    def __str__(self):               # users / email / admin\n'
                        '        return (\n'
                        '            f"Order #{self.order_id} for {self.customer} "\n'
                        '            f"— {len(self.items)} item(s)"\n'
                        '        )\n'
                        '\n'
                        '    def __repr__(self):              # developers / logs / Sentry\n'
                        '        return (\n'
                        '            f"Order(order_id={self.order_id!r}, "\n'
                        '            f"customer={self.customer!r}, items={self.items!r})"\n'
                        '        )\n'
                        '\n'
                        '    def __eq__(self, other):         # a == b by order_id\n'
                        '        if not isinstance(other, Order):\n'
                        '            return NotImplemented\n'
                        '        return self.order_id == other.order_id\n'
                        '\n'
                        '    def __len__(self):               # len(order)\n'
                        '        return len(self.items)\n'
                        '\n'
                        'o1 = Order(42, "Anu", ["pen", "notebook"])\n'
                        'o2 = Order(42, "Anu", ["pen"])       # same id → equal\n'
                        'o3 = Order(99, "Ravi", ["mug"])\n'
                        '\n'
                        'print(o1)                           # __str__\n'
                        'print(repr(o1))                     # __repr__\n'
                        'print([o1])                         # list uses __repr__\n'
                        'print(o1 == o2, o1 == o3)           # __eq__\n'
                        'print(len(o1))                      # __len__\n'
                        'print(f"Email: {o1}")               # f-string → __str__',
                        {
                            31: "Order #42 for Anu — 2 item(s)",
                            32: "Order(order_id=42, customer='Anu', items=['pen', 'notebook'])",
                            33: "[Order(order_id=42, customer='Anu', items=['pen', 'notebook'])]",
                            34: "True False",
                            35: "2",
                            36: "Email: Order #42 for Anu — 2 item(s)",
                        },
                    )
                    + "<p style=\"font-size:12px;margin:8px 0 6px;line-height:1.45\">"
                    "<b>With vs without <code>__str__</code>:</b> "
                    "no <code>__str__</code> → ugly default; with it → friendly print."
                    "</p>"
                    "<div class=\"mc-row\">"
                    "<div class=\"mc-col mc-bad\">"
                    "<span class=\"mc-lbl\">Without __str__</span>"
                    + io_split(
                        'class User:\n'
                        '    def __init__(self, name):\n'
                        '        self.name = name\n'
                        '    # no __str__\n'
                        '\n'
                        'u = User("Anu")\n'
                        'print(u)',
                        {7: "&lt;User object at 0x...&gt;"},
                    )
                    + "</div>"
                    "<div class=\"mc-col mc-good\">"
                    "<span class=\"mc-lbl\">With __str__</span>"
                    + io_split(
                        'class User:\n'
                        '    def __init__(self, name):\n'
                        '        self.name = name\n'
                        '    def __str__(self):\n'
                        '        return f"Hello {self.name}"\n'
                        '\n'
                        'u = User("Anu")\n'
                        'print(u)   # uses __str__',
                        {8: "Hello Anu"},
                    )
                    + "</div></div>"
                    "<p class=\"step-result\"><b>Takeaway:</b> "
                    "<code>__str__</code> = humans; <code>__repr__</code> = developers; "
                    "<code>__eq__</code> = meaningful <code>==</code>; <code>__len__</code> = "
                    "<code>len(obj)</code>. Used in real apps on models like Order / User / Invoice.</p>"
                ),
            },
        ],
        "interview_qa": [
            {"q": "What is self in Python?", "a": "The current instance. You must pass it as the first parameter of instance methods. <code>self.name</code> stores data on the object — like <code>this</code> in C#."},
            {"q": "What if a function has the same name as a class?", "a": "Python keeps the <b>last</b> binding of that name. A function named <code>Toy</code> after <code>class Toy</code> shadows the class — <code>Toy(\"ball\")</code> then calls the function, not the constructor. A method <code>def Toy(self)</code> does not replace the class. Best practice: never reuse the class name for a function."},
            {"q": "__str__ vs __repr__?", "a": "<code>__str__</code> is for end users (readable). <code>__repr__</code> is for developers — ideally valid code to recreate the object."},
            {"q": "What is MRO?", "a": "Method Resolution Order — the sequence Python searches base classes. Check with <code>ClassName.__mro__</code> or <code>help(ClassName)</code>."},
            {"q": "How does Python handle encapsulation?", "a": "By convention: <code>_attr</code> means internal. <code>__attr</code> name-mangles to <code>_ClassName__attr</code>. Not true access control — trust and documentation."},
        ],
    },
    18: {
        "steps": [
            {
                "title": "Step 1 — Function decorators",
                "body": 'A decorator wraps a function to add behavior without changing its source. <code>@retry(times=3)</code> means: <code><b>GetEmployees</b> = <b>retry</b>(<b>times</b>=3)(<b>GetEmployees</b>)</code>.<p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Syntactic sugar</b> = a <b>nicer shortcut</b> for something that already has a longer form. Same meaning — just sweeter to write. Example: <code>@retry(times=3)</code> (sugar) is the same as <code><b>GetEmployees</b> = <b>retry</b>(<b>times</b>=3)(<b>GetEmployees</b>)</code> (real work underneath).</p><div class="mc-row"><div class="mc-col mc-good"><span class="mc-lbl">@decorator — sugar (what you write)</span><div class="step-pre"># @decorator  (syntactic sugar)\n@retry(times=3)\ndef GetEmployees(employee_ids, include_inactive=False):\n    return api_call(employee_ids, include_inactive)\n\nGetEmployees([101, 102, 103], include_inactive=True)\n\n# Same idea in general:\n# @decorator\n# def func():\n#     ...</div></div><div class="mc-col mc-good"><span class="mc-lbl">func = decorator(func) — real form</span><div class="step-pre"># func = decorator(func)  (real form)\ndef GetEmployees(employee_ids, include_inactive=False):\n    return api_call(employee_ids, include_inactive)\n\n<b>GetEmployees</b> = <b>retry</b>(<b>times</b>=3)(<b>GetEmployees</b>)\n\nGetEmployees([101, 102, 103], include_inactive=True)\n\n# Same idea in general:\n# def func():\n#     ...\n# func = decorator(func)</div></div></div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Same meaning:</b> both end with <code>GetEmployees</code> pointing to the <b>wrapper</b>. Left is shorter to write; right is what Python does underneath.</p><div class="step-pre">import time\nfrom functools import wraps\n\ndef retry(times=3, delay=0.1):          # 1) FACTORY - takes settings, returns a decorator\n    def decorator(fn):                 # 2) DECORATOR - takes the function, returns wrapper\n        @wraps(fn)\n        def wrapper(*args, **kwargs):  # 3) WRAPPER - runs on each call\n            for attempt in range(times):\n                try:\n                    return fn(*args, **kwargs)\n                except ConnectionError:\n                    if attempt == times - 1:\n                        raise\n                    time.sleep(delay)\n        return wrapper\n    return decorator\n\n@retry(times=3)\ndef GetEmployees(employee_ids, include_inactive=False):\n    return api_call(employee_ids, include_inactive)\n\nGetEmployees([101, 102, 103], include_inactive=True)</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Layers in this code (read top → bottom)</b></p><table class="data-tbl"><tr><th>Line / piece</th><th>What it is</th></tr><tr><td><code>retry(times=3, delay=0.1)</code></td><td>Decorator <b>factory</b> — settings for retry (how many tries, how long to wait)</td></tr><tr><td><code>decorator(fn)</code></td><td>Receives the real function (<code>GetEmployees</code>)</td></tr><tr><td><code>wrapper(*args, **kwargs)</code></td><td>Runs <b>instead of</b> the original when you call it</td></tr><tr><td><code>fn(*args, **kwargs)</code></td><td>Calls the original function, forwarding the same arguments</td></tr><tr><td><code>@retry(times=3)</code></td><td>Applies the decorator: name now points to <code>wrapper</code></td></tr></table><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Diagram — call <code>GetEmployees([101, 102, 103], include_inactive=True)</code></b></p><div class="step-pre">YOU WRITE                                              WHAT ACTUALLY RUNS\n───────────────────────────────────────────            ────────────────────────────────────────\nGetEmployees([101, 102, 103], include_inactive=True)\n    │\n    │  @retry replaced the name with wrapper\n    ▼\nwrapper([101, 102, 103], include_inactive=True)\n    │\n    │  # LIST  → goes into *args   (positional — no name=)\n    │  # BOOL  → goes into **kwargs (keyword — name=value)\n    │\n    │  *args   PACKS  → args   = ([101, 102, 103],)\n    │  #                 ^ tuple with ONE item = the whole list\n    │  #                 args[0] is [101, 102, 103]  (NOT three separate ints)\n    │\n    │  **kwargs PACKS → kwargs = {"include_inactive": True}\n    │  #                 ^ dict: key = param name, value = the bool True\n    │  #                 kwargs["include_inactive"] is True\n    │\n    │  retry loop (times=3)\n    ▼\nfn(*args, **kwargs)\n    │  # UNPACK list from args + bool from kwargs:\n    │  UNPACK → fn([101, 102, 103], include_inactive=True)\n    ▼\napi_call([101, 102, 103], True)   # original GetEmployees body\n\n# if ConnectionError → sleep(0.1), try again (up to 3 times)\n# each retry gets the SAME list (args) AND the SAME bool (kwargs)</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Why <code>kwargs</code> has values here</b><br><code>include_inactive=True</code> is written as <code>name=value</code> — that is a <b>keyword</b> argument, so it goes into <code>**kwargs</code>. The list <code>[101, 102, 103]</code> has no name in front, so it goes into <code>*args</code>.</p><div class="mc-row"><div class="mc-col mc-good"><span class="mc-lbl">PACK — def wrapper(*args, **kwargs)</span><div class="step-pre"># from the retry code\ndef wrapper(*args, **kwargs):\n    ...\n    return fn(*args, **kwargs)\n\n# call: GetEmployees([101, 102, 103], include_inactive=True)\n#\n# LIST [101,102,103]  → *args    (positional)\n# BOOL True           → **kwargs (keyword include_inactive=True)\n#\nargs   = ([101, 102, 103],)            # *args: list lives HERE\n#          └─ one tuple slot = whole list\nkwargs = {"include_inactive": True}    # **kwargs: bool lives HERE\n#          └─ key=name, value=bool</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Explanation:</b> in <code>def</code>, stars <b>PACK</b>. <code>*args</code> = tuple of positionals. <code>**kwargs</code> = dict of keywords (here <code>include_inactive</code> is present).</p></div><div class="mc-col mc-good"><span class="mc-lbl">UNPACK — fn(*args, **kwargs)</span><div class="step-pre"># from the retry code (inside the loop)\nreturn fn(*args, **kwargs)\n\n# same as writing:\nreturn fn([101, 102, 103], include_inactive=True)\n#          └─ from *args (list)   └─ from **kwargs (bool)\n\n# GetEmployees body receives:\nemployee_ids = [101, 102, 103]   # came from args[0]\ninclude_inactive = True          # came from kwargs["include_inactive"]\n\n# every retry forwards BOTH: list in args + bool in kwargs</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Explanation:</b> in a <b>call</b>, stars <b>UNPACK</b>. Original <code>GetEmployees(employee_ids, include_inactive=...)</code> gets the list and the flag exactly as you sent them.</p></div></div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Positional vs keyword — meaning</b><br><b>Positional</b> = pass by <b>order / place</b> (value only, no <code>name=</code>). <b>Keyword</b> = pass by <b>parameter name</b> (<code>name=value</code>). Same value can be either — it depends on <b>how you write the call</b>, not on what the value means.</p><div class="step-pre"># Same value "Alice" — two ways:\n#\n# POSITIONAL — value only, matched by order\nGetEmployees("Alice")\n#             └─ 1st slot → whatever the 1st parameter is\n#\n# KEYWORD — name=value, matched by parameter name\nGetEmployees(employee_name="Alice")\n#             └─ goes to parameter employee_name\n#\n# Your GetEmployees call uses BOTH:\nGetEmployees([101, 102, 103], include_inactive=True)\n#            └───────┬───────┘  └──────────┬─────────┘\n#              positional              keyword\n#              (value only)            (name=value)\n#\n# That is why in the wrapper:\n#   positional → *args    → args   = ([101, 102, 103],)\n#   keyword    → **kwargs → kwargs = {"include_inactive": True}</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>When to use which</b></p><table class="data-tbl"><tr><th>Situation</th><th>Prefer</th><th>Why</th></tr><tr><td>Main required value (id list, text) — meaning is obvious</td><td><b>positional</b></td><td>Short and clear: <code>GetEmployees([101, 102, 103])</code></td></tr><tr><td>Flags / options (<code>True</code>/<code>False</code>, size, date, dept)</td><td><b>keyword</b></td><td>Bare <code>True</code> is unclear — <code>include_inactive=True</code> is safe</td></tr><tr><td>Many arguments, or easy to mix up order</td><td><b>keyword</b></td><td>Names prevent wrong-order bugs</td></tr><tr><td>Skipping optional defaults</td><td><b>keyword</b></td><td>Set only what you need: <code>page_size=50</code></td></tr></table><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Best practice:</b> required main inputs → positional; options/flags → keyword. Example: <code>GetEmployees([101, 102, 103], include_inactive=True, page_size=50)</code>. <b>Yes — keywords are usually clearer and less error-prone</b> for options and anything where order could be confusing. Positional is fine for the obvious first 1–2 required values.</p><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Quick compare — 4 examples each</b></p><table class="data-tbl"><tr><th>Kind</th><th>How you write it</th><th>Matched by</th><th>Examples (4)</th></tr><tr><td><b>Positional</b></td><td>value only</td><td>order / place</td><td>1. <code>[101, 102, 103]</code> — employee id list<br>2. <code>"Alice"</code> — employee name<br>3. <code>42</code> — department id<br>4. <code>True</code> — a flag passed by position</td></tr><tr><td><b>Keyword</b></td><td><code>name=value</code></td><td>parameter name</td><td>1. <code>include_inactive=True</code><br>2. <code>department="HR"</code><br>3. <code>page_size=50</code><br>4. <code>as_of="2026-08-10"</code></td></tr></table><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Same idea in one call (mixed)</b></p><div class="step-pre">GetEmployees([101, 102, 103], department="HR", page_size=50)\n#            └─ positional      └─ keyword         └─ keyword\n#\n# args   = ([101, 102, 103],)\n# kwargs = {"department": "HR", "page_size": 50}</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>*args / **kwargs are NOT decorator-only</b> — same packing idea in normal functions and in decorator wrappers. Side-by-side:</p><div class="mc-row"><div class="mc-col mc-good"><span class="mc-lbl">Normal function — flexible API <button type="button" class="btn-csharp-pop" onclick="openCsharpWin(\'args-kwargs\')" title="Open draggable C# comparison window">C# Comparison</button></span><div class="step-pre">def log(msg, *args, **kwargs):\n    # *args   -> extra positionals (tuple)\n    # **kwargs -> extra keywords (dict)\n    print(msg)\n    print("args  =", args)\n    print("kwargs=", kwargs)\n\nlog("start", 1, 2, level="debug")\n\n# Result:\n# args   = (1, 2)\n# kwargs = {"level": "debug"}\n\n# Use when: helper/API accepts optional extras\n# No decorator — just a flexible function</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Here:</b> <code>log</code> itself uses <code>*args</code>/<code>**kwargs</code> to collect extras the caller passed. Click <b>C# Comparison</b> for <code>params</code> / named args / <code>Dictionary</code>.</p></div><div class="mc-col mc-good"><span class="mc-lbl">Decorator wrapper — forward any call</span><div class="step-pre"># INPUT (from @retry)\ndef wrapper(*args, **kwargs):\n    # PACK whatever GetEmployees got\n    for attempt in range(times):\n        try:\n            return fn(*args, **kwargs)  # UNPACK\n        except ConnectionError:\n            ...\n\nGetEmployees([101, 102, 103], include_inactive=True)\n\n# inside wrapper:\nargs   = ([101, 102, 103],)\nkwargs = {\'include_inactive\': True}\n\n# Use when: one wrapper must work for ANY\n# decorated function signature</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Here:</b> wrapper does not care about the function parameters — it packs and forwards them to the original <code>fn</code>.</p></div></div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Same mechanism, different job:</b> normal = collect extras for <b>this</b> function; decorator = catch <b>any</b> call and replay it into the original function.</p><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Rule: all positionals first, then keywords</b><br>You <b>cannot</b> put a positional argument after a keyword argument — Python raises <code>SyntaxError</code>.</p><div class="mc-row"><div class="mc-col mc-good"><span class="mc-lbl">Valid — positionals, then keyword</span><div class="step-pre">log("start", 1, 2, 3, 4, level="debug")\n#           └─ positionals ─┘  └── keyword ──┘\n\n# inside log:\n# args   = (1, 2, 3, 4)\n# kwargs = {"level": "debug"}</div></div><div class="mc-col mc-bad"><span class="mc-lbl">Invalid — positional after keyword</span><div class="step-pre">log("start", 1, 2, level="debug", 3, 4)\n#                   keyword ↑    ↑ positionals after\n#                   NOT ALLOWED\n\n# SyntaxError: positional argument\n# follows keyword argument</div></div></div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Same rule for your decorated call</b></p><div class="step-pre"># OK\nGetEmployees([101, 102, 103], include_inactive=True)\n\n# NOT OK\nGetEmployees(include_inactive=True, [101, 102, 103])\n#            keyword first ↑         ↑ positional after — SyntaxError</div><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Cheat sheet (for this retry wrapper)</b></p><table class="data-tbl"><tr><th></th><th><code>*</code> (one star)</th><th><code>**</code> (two stars)</th></tr><tr><td><b>What</b></td><td>positional values</td><td>keyword values</td></tr><tr><td><b>In <code>def wrapper</code></b></td><td><code>*args</code> → <b>PACK</b> into tuple</td><td><code>**kwargs</code> → <b>PACK</b> into dict</td></tr><tr><td><b>In <code>fn(...)</code> call</b></td><td><code>*args</code> → <b>UNPACK</b> tuple</td><td><code>**kwargs</code> → <b>UNPACK</b> dict</td></tr><tr><td><b>This call</b></td><td><code>([101, 102, 103],)</code></td><td><code>{"include_inactive": True}</code></td></tr></table><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Why this matters for retry:</b> on attempt 1, 2, or 3, <code>fn(*args, **kwargs)</code> must send the <b>same</b> employee-id list <b>and</b> the same <code>include_inactive=True</code> each time.</p><p style="font-size:12px;margin:6px 0;line-height:1.45"><b>Do not confuse:</b> <code>times=3, delay=0.1</code> are <b>decorator settings</b>. <code>employee_ids</code> / <code>include_inactive</code> are <b>function-call</b> inputs (via <code>*args</code> / <code>**kwargs</code>).</p>',
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
            {
                "q": "Explain decorators in simple terms.",
                "a": (
                    "A decorator is a <b>wrapper</b>. It adds extra work (retry, log, timing) "
                    "around your function, without editing the function body.<br><br>"
                    "<b>Syntactic sugar:</b> <code>@decorator</code> is a nicer shortcut for "
                    "<code>name = decorator(name)</code> — same meaning.<br><br>"
                    "<b>Full code:</b>"
                    '<div class="step-pre">'
                    "import time\n"
                    "from functools import wraps\n\n"
                    "def retry(times=3, delay=0.1):          # 1) FACTORY - takes settings, returns a decorator\n"
                    "    def decorator(fn):                 # 2) DECORATOR - takes the function, returns wrapper\n"
                    "        @wraps(fn)\n"
                    "        def wrapper(*args, **kwargs):  # 3) WRAPPER - runs on each call\n"
                    "            for attempt in range(times):\n"
                    "                try:\n"
                    "                    return fn(*args, **kwargs)\n"
                    "                except ConnectionError:\n"
                    "                    if attempt == times - 1:\n"
                    "                        raise\n"
                    "                    time.sleep(delay)\n"
                    "        return wrapper\n"
                    "    return decorator\n\n"
                    "# SUGAR\n"
                    "@retry(times=3)\n"
                    "def GetEmployees(employee_ids, include_inactive=False):\n"
                    "    return api_call(employee_ids, include_inactive)\n\n"
                    "# REAL FORM (same):\n"
                    "# <b>GetEmployees</b> = <b>retry</b>(<b>times</b>=3)(<b>GetEmployees</b>)\n\n"
                    "GetEmployees([101, 102, 103], include_inactive=True)\n"
                    "# → wrapper runs (retry) → original body"
                    "</div>"
                    "FastAPI’s <code>@app.get('/')</code> is the same idea."
                ),
            },
            {
                "q": "Why use functools.wraps?",
                "a": (
                    "After decorating, the name points to <code>wrapper</code>. "
                    "Without <code>@wraps</code>, the name/docstring become wrong.<br><br>"
                    "<b>Side by side — without vs with wraps:</b>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad"><span class="mc-lbl">Without @wraps — BAD</span>'
                    '<div class="step-pre">'
                    "from functools import wraps\n\n"
                    "def bad(fn):\n"
                    "    def wrapper(*args, **kwargs):\n"
                    "        return fn(*args, **kwargs)\n"
                    "    return wrapper\n\n"
                    "@bad\n"
                    "def GetEmployees(employee_ids):\n"
                    '    """Fetch employees."""\n'
                    "    return api_call(employee_ids)\n\n"
                    "print(GetEmployees.__name__)\n"
                    '# "wrapper"  ← wrong\n\n'
                    "print(GetEmployees.__doc__)\n"
                    "# None       ← lost"
                    "</div></div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">With @wraps — GOOD</span>'
                    '<div class="step-pre">'
                    "from functools import wraps\n\n"
                    "def good(fn):\n"
                    "    @wraps(fn)\n"
                    "    def wrapper(*args, **kwargs):\n"
                    "        return fn(*args, **kwargs)\n"
                    "    return wrapper\n\n"
                    "@good\n"
                    "def GetEmployees(employee_ids):\n"
                    '    """Fetch employees."""\n'
                    "    return api_call(employee_ids)\n\n"
                    "print(GetEmployees.__name__)\n"
                    '# "GetEmployees"  ← correct\n\n'
                    "print(GetEmployees.__doc__)\n"
                    '# "Fetch employees."\n'
                    '# ↑ from the """Fetch employees.""" docstring above\n'
                    "#   @wraps(fn) copied fn.__doc__ onto wrapper"
                    "</div></div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Where does <code>__doc__</code> come from?</b> "
                    "The text in <code>\"\"\"Fetch employees.\"\"\"</code> right under "
                    "<code>def GetEmployees</code> is the docstring — Python stores it as "
                    "<code>GetEmployees.__doc__</code>. "
                    "<code>@wraps(fn)</code> copies that string onto the wrapper, so after "
                    "decorating you still see the same docstring."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>What is a docstring?</b> "
                    '<button type="button" class="btn-csharp-pop" '
                    "onclick=\"openCsharpWin('docstring-xml')\" "
                    'title="Open draggable C# comparison window">C# Comparison</button><br>'
                    "A <b>docstring</b> is a string written as the <b>first statement</b> inside a "
                    "<code>def</code>, <code>class</code>, or module — usually with "
                    "<code>\"\"\"triple quotes\"\"\"</code>. "
                    "It describes <b>what</b> the code does (not how every line works)."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Purpose / use cases:</b><br>"
                    "1. <b>help()</b> — <code>help(GetEmployees)</code> shows the docstring.<br>"
                    "2. <b>IDE tooltips</b> — hover over the name to see the description.<br>"
                    "3. <b>Auto-docs</b> — tools like Sphinx / FastAPI read docstrings for API docs.<br>"
                    "4. <b>Team clarity</b> — next developer knows the function’s job without reading all code.<br>"
                    "5. <b>Debugging / logs</b> — with <code>@wraps</code>, name + docstring stay correct after decorating."
                    "</p>"
                    '<div class="step-pre">'
                    "def GetEmployees(employee_ids):\n"
                    '    """Fetch employees by id list."""   # ← docstring\n'
                    "    return api_call(employee_ids)\n\n"
                    "help(GetEmployees)           # shows the docstring\n"
                    "print(GetEmployees.__doc__)  # Fetch employees by id list."
                    "</div>"
                    "<b>Rule:</b> always use <code>@wraps(fn)</code> on the inner wrapper."
                ),
            },
            {
                "q": "Can a decorator accept arguments?",
                "a": (
                    "Yes — use a <b>decorator factory</b> (returns a decorator).<br><br>"
                    "<b>Full code:</b>"
                    '<div class="step-pre">'
                    "import time\n"
                    "from functools import wraps\n\n"
                    "def retry(times=3, delay=0.1):          # 1) FACTORY - takes settings, returns a decorator\n"
                    "    def decorator(fn):                 # 2) DECORATOR - takes the function, returns wrapper\n"
                    "        @wraps(fn)\n"
                    "        def wrapper(*args, **kwargs):  # 3) WRAPPER - runs on each call\n"
                    "            for attempt in range(times):\n"
                    "                try:\n"
                    "                    return fn(*args, **kwargs)\n"
                    "                except ConnectionError:\n"
                    "                    if attempt == times - 1:\n"
                    "                        raise\n"
                    "                    time.sleep(delay)\n"
                    "        return wrapper\n"
                    "    return decorator\n\n"
                    "@retry(times=3)\n"
                    "def GetEmployees(employee_ids, include_inactive=False):\n"
                    "    return api_call(employee_ids, include_inactive)\n\n"
                    "# means: <b>GetEmployees</b> = <b>retry</b>(<b>times</b>=3)(<b>GetEmployees</b>)\n"
                    "GetEmployees([101, 102, 103], include_inactive=True)\n"
                    "\n"
                    "# times/delay = decorator settings\n"
                    "# *args/**kwargs = call inputs to GetEmployees"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Important:</b> <code>def decorator(fn):</code> is <b>not</b> the factory. "
                    "It is the <b>real decorator</b> (takes the function). "
                    "The <b>factory</b> is outer <code>retry(...)</code> "
                    "(takes settings and <b>returns</b> the decorator)."
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th>Name in code</th><th>What it is</th><th>Takes</th><th>Returns</th></tr>"
                    "<tr><td><code>retry</code></td><td><b>factory</b></td>"
                    "<td>settings (<code>times</code>, <code>delay</code>)</td>"
                    "<td>the decorator</td></tr>"
                    "<tr><td><code>decorator</code></td><td><b>decorator</b></td>"
                    "<td>function (<code>fn</code>)</td>"
                    "<td>the wrapper</td></tr>"
                    "<tr><td><code>wrapper</code></td><td><b>wrapper</b></td>"
                    "<td>call args (<code>*args</code>, <code>**kwargs</code>)</td>"
                    "<td>result of <code>fn</code></td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>How to tell:</b><br>"
                    "• Decorator → takes a <b>function</b>, returns a function (usually wrapper).<br>"
                    "• Factory → takes <b>settings</b>, returns a <b>decorator</b>.<br><br>"
                    "So <code>@retry(times=3)</code> means: "
                    "(1) call factory <code>retry(times=3)</code> → get <code>decorator</code>, "
                    "(2) call <code>decorator(GetEmployees)</code> → get <code>wrapper</code>, "
                    "(3) name <code>GetEmployees</code> points to that wrapper.<br><br>"
                    "<b>Note:</b> the name <code>decorator</code> is only a label — "
                    "you could call it <code>inner</code>. What matters is the <b>job</b>, not the name."
                    "</p>"
                ),
            },
            {
                "q": "Decorator vs inheritance for extending behavior?",
                "a": (
                    "Different jobs — wrap a function vs model is-a types.<br><br>"
                    "<b>Side by side:</b>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-good"><span class="mc-lbl">Decorator — cross-cutting</span>'
                    '<div class="step-pre">'
                    "@retry(times=3)\n"
                    "def GetEmployees(employee_ids):\n"
                    "    return api_call(employee_ids)\n\n"
                    "@log_calls\n"
                    "def SaveReport(path):\n"
                    "    return write(path)\n\n"
                    '@require_auth("admin")\n'
                    "def DeleteUser(user_id):\n"
                    "    return db.delete(user_id)"
                    "</div>"
                    "</div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">Inheritance — is-a types</span>'
                    '<div class="step-pre">'
                    "class BankAccount:\n"
                    "    def __init__(self, balance):\n"
                    "        self.balance = balance\n"
                    "    def deposit(self, amount):\n"
                    "        self.balance += amount\n\n"
                    "class SavingsAccount(BankAccount):\n"
                    "    def add_interest(self, rate):\n"
                    "        self.balance *= (1 + rate)"
                    "</div>"
                    "</div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>What is “cross-cutting”?</b> "
                    "Extra behavior needed by <b>many unrelated functions</b> — "
                    "not part of the core business rule of each one. "
                    "You write it <b>once</b> and attach with <code>@</code>."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Decorator scenarios (why)</b>"
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th>Need</th><th>Example scenario</th><th>Why decorator?</th></tr>"
                    "<tr><td><b>retry</b></td>"
                    "<td>Flaky network: <code>GetEmployees</code>, <code>SendEmail</code>, "
                    "<code>FetchInvoice</code> all fail sometimes</td>"
                    "<td>Same retry loop in every function is copy-paste. "
                    "<code>@retry(times=3)</code> once — business code stays clean.</td></tr>"
                    "<tr><td><b>log</b></td>"
                    "<td>Audit trail: who called <code>SaveReport</code> / "
                    "<code>UpdateSalary</code>, with args and time</td>"
                    "<td>Logging is not “report logic”. "
                    "<code>@log_calls</code> adds start/finish prints without editing each body.</td></tr>"
                    "<tr><td><b>auth</b></td>"
                    "<td>Only admins may <code>DeleteUser</code> or <code>ExportPayroll</code></td>"
                    "<td>Role check is security, not delete logic. "
                    "<code>@require_auth(\"admin\")</code> blocks bad callers in one place.</td></tr>"
                    "<tr><td><b>timing</b></td>"
                    "<td>Slow API: measure <code>run_query</code> / <code>build_report</code></td>"
                    "<td><code>@timer</code> wraps timing around any function without "
                    "mixing clocks into business code.</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Inheritance scenarios (why)</b>"
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th>Need</th><th>Example scenario</th><th>Why inheritance?</th></tr>"
                    "<tr><td><b>is-a type</b></td>"
                    "<td><code>SavingsAccount</code> <b>is a</b> <code>BankAccount</code> — "
                    "has balance + deposit, plus interest</td>"
                    "<td>Child reuses parent fields/methods and adds specialized behavior. "
                    "This is a type hierarchy, not a wrapper around one function.</td></tr>"
                    "<tr><td><b>shared structure</b></td>"
                    "<td><code>Dog</code> / <code>Cat</code> both <b>are</b> <code>Animal</code> "
                    "with <code>speak()</code> overridden</td>"
                    "<td>Common base holds shared state/API; children customize. "
                    "Polymorphism: one list of <code>Animal</code>, different <code>speak()</code>.</td></tr>"
                    "<tr><td><b>specialize behavior</b></td>"
                    "<td><code>AdminUser(User)</code> can do everything a user can, plus admin tools</td>"
                    "<td>Natural “kind of” relationship. Inheritance models the domain, "
                    "not cross-cutting extras like retry.</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Choose:</b><br>"
                    "• Same extra behavior on <b>many unrelated functions</b> "
                    "(retry / log / auth / timing) → <b>decorator</b><br>"
                    "• Related types that <b>share structure</b> (is-a) → <b>inheritance</b><br><br>"
                    "<b>Wrong mix:</b> don’t invent <code>class RetryableGetEmployees(GetEmployees)</code> "
                    "just to add retry — that is cross-cutting, use <code>@retry</code>. "
                    "Don’t use <code>@retry</code> to model “savings is a bank account” — that is inheritance."
                    "</p>"
                ),
            },
        ],
    },
    16: {
        "steps": [
            {
                "title": "Step 1 — What is a descriptor? (security guard)",
                "body": (
                    "Think of a <b>descriptor</b> as a <b>security guard</b> in front of a variable. "
                    "Normally Python gives the value directly; with a descriptor it asks the helper first."
                    '<div class="step-pre">'
                    "Without descriptor:\n"
                    "  person.name  →  \"John\"\n"
                    "\n"
                    "With descriptor:\n"
                    "  person.name\n"
                    "       │\n"
                    "       ▼\n"
                    "  Descriptor (helper)\n"
                    "       │\n"
                    "       ▼\n"
                    "  validate / calculate / return"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Definition:</b> a helper object that controls how an attribute is "
                    "<b>read</b>, <b>written</b>, or <b>deleted</b>."
                    "</p>"
                    "<p style=\"font-size:12px;margin:0 0 6px;line-height:1.45\">"
                    "<b>Why need it?</b> Without it, <code>person.age = -20</code> is stored. "
                    "A descriptor can raise <code>ValueError</code> instead. "
                    "Use for: validate, calculate, restrict, log, type-check."
                    "</p>"
                ),
            },
            {
                "title": "Step 2 — Start with @property (getter + setter)",
                "body": (
                    "Start here — like a C# property. <code>@property</code> + <code>@age.setter</code> creates a built-in "
                    "<b>data</b> descriptor. "
                    "Read → <code>property.__get__</code>; write → <code>property.__set__</code>."
                    + io_split(
                        "class Student:\n"
                        "    def __init__(self):\n"
                        "        self._age = 0\n"
                        "\n"
                        "    @property\n"
                        "    def age(self):                # __get__\n"
                        "        return self._age\n"
                        "\n"
                        "    @age.setter\n"
                        "    def age(self, value):         # __set__\n"
                        "        if value < 0:\n"
                        '            raise ValueError("age cannot be negative")\n'
                        "        self._age = value\n"
                        "\n"
                        "s = Student()\n"
                        "s.age = 20\n"
                        "print(s.age)\n"
                        "try:\n"
                        "    s.age = -5\n"
                        "except ValueError as e:\n"
                        "    print(type(e).__name__)",
                        {17: "20", 21: "ValueError"},
                    )
                    + '<table class="data-tbl" style="margin-top:8px">'
                    "<tr><th>Public name</th><th>Backing store</th><th>Getter</th><th>Setter</th></tr>"
                    "<tr><td><code>price</code></td><td><code>self._price</code></td>"
                    "<td><code>@property</code> / <code>def price</code></td>"
                    "<td><code>@price.setter</code> / <code>def price</code></td></tr>"
                    "<tr><td><code>age</code></td><td><code>self._age</code></td>"
                    "<td><code>@property</code> / <code>def age</code></td>"
                    "<td><code>@age.setter</code> / <code>def age</code></td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Yes — follow the field name.</b> "
                    "Outside code uses <code>p.price</code>; inside, store in <code>self._price</code> "
                    "(leading <code>_</code> = “internal”). "
                    "Never write <code>self.price = …</code> inside the setter — that calls the setter again."
                    "</p>"
                    + '<table class="data-tbl" style="margin-top:8px">'
                    "<tr><th>Remember</th><th>Meaning</th></tr>"
                    "<tr><td>Descriptor</td><td>Helper that controls an attribute</td></tr>"
                    "<tr><td><code>__get__</code></td><td>Runs on read</td></tr>"
                    "<tr><td><code>__set__</code></td><td>Runs on write</td></tr>"
                    "<tr><td>Non-data</td><td>Read helper only</td></tr>"
                    "<tr><td>Data</td><td>Read + write helper</td></tr>"
                    "<tr><td><code>@property</code></td><td>Built-in data descriptor</td></tr>"
                    "</table>"
                    '<p class="step-result"><b>One-line:</b> '
                    "A descriptor sits between your code and an attribute so Python can control "
                    "read / write / delete.</p>"
                ),
            },
            {
                "title": "Step 3 — Same idea with __get__ / __set__",
                "body": (
                    "Same job as <code>@property</code>, but <b>reusable</b>. "
                    "Define the helper <b>once</b>, then attach it at <b>class level</b> "
                    "on every field that needs the same rules "
                    "(<code>price</code>, <code>qty</code>, even another class)."
                    "<br><b>Step A — helper class</b> (get/set logic lives here):"
                    + io_split(
                        "class PositiveNumber:\n"
                        "    def __get__(self, obj, owner):\n"
                        "        ...   # like @property getter\n"
                        "    def __set__(self, obj, value):\n"
                        "        ...   # like @property.setter",
                    )
                    + "<b>Step B — plug into required fields</b> "
                    "(class-level — not inside <code>__init__</code>):"
                    + io_split(
                        "class Product:\n"
                        "    price = PositiveNumber()   # field 1\n"
                        "    qty = PositiveNumber()     # field 2 — same rules\n"
                        "\n"
                        "class Order:\n"
                        "    total = PositiveNumber()   # reuse on another class\n"
                        "\n"
                        "# p.price / p.qty / o.total all ask the same helper",
                    )
                    + '<p class="step-result"><b>vs @property:</b> '
                    "two properties → copy getter/setter twice. "
                    "Descriptor → one class, many <code>field = PositiveNumber()</code> lines. "
                    "See the Real-life side-by-side above.</p>"
                ),
            },
            {
                "title": "Step 4 — Type 1 Non-data vs Type 2 Data",
                "body": (
                    "Only <b>two types</b>. "
                    "Non-data = only <code>__get__</code> (write can bypass). "
                    "Data = <code>__get__</code> + <code>__set__</code> (guard on every write)."
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.5\">"
                    "<b>No setter — how does get still work?</b> "
                    "On <b>read</b> (<code>p.price</code>), if the instance has <b>no</b> "
                    "<code>price</code> in <code>__dict__</code> yet, Python calls "
                    "<code>__get__</code> (default / compute / log). "
                    "On <b>write</b> (<code>p.price = -1</code>), with no <code>__set__</code>, "
                    "Python just does a normal store into <code>p.__dict__['price']</code> — "
                    "the helper is skipped. After that, reads often use the instance value "
                    "and may skip <code>__get__</code> too."
                    "</p>"
                    "<div class=\"mc-row\">"
                    "<div class=\"mc-col mc-bad\">"
                    "<span class=\"mc-lbl\">Type 1 — Non-data (only __get__)</span>"
                    + io_split(
                        "class SoftField:\n"
                        "    def __set_name__(self, owner, name):\n"
                        "        self.name = name\n"
                        "    def __get__(self, obj, owner):\n"
                        '        print("Reading via __get__...")\n'
                        '        return obj.__dict__.get(self.name, "empty")\n'
                        "    # NO __set__ — write is a normal store\n"
                        "\n"
                        "class Product:\n"
                        "    price = SoftField()\n"
                        "\n"
                        "p = Product()\n"
                        "print(p.price)      # no instance value yet → __get__\n"
                        "p.price = -1        # no __set__ → stored in __dict__\n"
                        "print(p.price)      # instance wins (may skip __get__)",
                        {13: "Reading via __get__...\nempty", 15: "-1"},
                    )
                    + '<div class="step-pre" style="font-size:11px;margin:6px 8px">'
                    "Before write:  Class price→SoftField   Instance (empty)\n"
                    "               read → __get__ → 'empty'\n"
                    "After write:   Class price→SoftField   Instance price→-1\n"
                    "               read → instance value (descriptor bypassed)"
                    "</div>"
                    + "</div>"
                    "<div class=\"mc-col mc-good\">"
                    "<span class=\"mc-lbl\">Type 2 — Data (__get__ + __set__)</span>"
                    + io_split(
                        "class PositiveNumber:\n"
                        "    def __set_name__(self, owner, name):\n"
                        "        self.name = name\n"
                        "    def __get__(self, obj, owner):\n"
                        "        return obj.__dict__.get(self.name)\n"
                        "    def __set__(self, obj, value):\n"
                        "        if value < 0:\n"
                        '            raise ValueError("must be >= 0")\n'
                        "        obj.__dict__[self.name] = value\n"
                        "\n"
                        "class Product:\n"
                        "    price = PositiveNumber()\n"
                        "\n"
                        "p = Product()\n"
                        "p.price = 100\n"
                        "print(p.price)\n"
                        "try:\n"
                        "    p.price = -50     # always goes through __set__\n"
                        "except ValueError as e:\n"
                        "    print(type(e).__name__)",
                        {16: "100", 20: "ValueError"},
                    )
                    + "</div></div>"
                    '<table class="data-tbl" style="margin-top:8px">'
                    "<tr><th>Feature</th><th>Non-data</th><th>Data</th></tr>"
                    "<tr><td><code>__get__</code></td><td class=\"cell-yes\">Yes</td><td class=\"cell-yes\">Yes</td></tr>"
                    "<tr><td><code>__set__</code></td><td class=\"cell-no\">No</td><td class=\"cell-yes\">Yes</td></tr>"
                    "<tr><td>Controls write / validate</td><td class=\"cell-no\">No</td><td class=\"cell-yes\">Yes</td></tr>"
                    "<tr><td>Instance var can override</td><td class=\"cell-yes\">Yes</td><td class=\"cell-no\">No</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:8px 0 6px;line-height:1.5\">"
                    "<b>When use non-data?</b> When you only want to customize <b>read</b> "
                    "(default / lazy / log), and it’s OK if a normal assignment "
                    "<b>overrides</b> the helper afterward."
                    "</p>"
                    + io_split(
                        "class DefaultTitle:\n"
                        "    def __get__(self, obj, owner):\n"
                        "        # only runs until someone assigns obj.title = ...\n"
                        "        # usual (with __set_name__ + store): return obj.__dict__.get(self.name)\n"
                        '        return obj.__dict__.get("title", "Untitled")\n'
                        "\n"
                        "class Doc:\n"
                        "    title = DefaultTitle()     # non-data: no __set__\n"
                        "\n"
                        "d = Doc()\n"
                        "print(d.title)        # __get__ → default\n"
                        'd.title = "Report"    # normal write — OK, no validation\n'
                        "print(d.title)        # instance value",
                        {11: "Untitled", 13: "Report"},
                    )
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Real examples of non-data:</b> "
                    "plain functions on a class, <code>@staticmethod</code>, "
                    "<code>@classmethod</code> — they use <code>__get__</code> only, "
                    "so you can still assign an instance attribute of the same name if needed. "
                    "<b>Need validation on every write?</b> Use a <b>data</b> descriptor "
                    "(or <code>@property</code> with a setter)."
                    "</p>"
                    '<p class="step-result"><b>Memory trick:</b> '
                    "Non-data = read helper only (write can override) · "
                    "Data = read + write helper · "
                    "<code>@property</code> with setter = data.</p>"
                ),
            },
            {
                "title": "Step 5 — Why __dict__? (store without recursion)",
                "body": (
                    "Every instance has <code>__dict__</code> — the object’s storage bag "
                    "(name → value). Descriptors must write <b>here</b>, or they call themselves again."
                    + io_split(
                        'class Product:\n'
                        '    def __init__(self, name):\n'
                        '        self.name = name\n'
                        '        self.price = 99\n'
                        '\n'
                        'p = Product("Pen")\n'
                        'print(p.__dict__)\n'
                        'print(p.__dict__["price"])\n'
                        'p.__dict__["price"] = 50\n'
                        'print(p.price)',
                        {
                            7: "{'name': 'Pen', 'price': 99}",
                            8: "99",
                            10: "50",
                        },
                    )
                    + "<div class=\"mc-row\">"
                    "<div class=\"mc-col mc-bad\">"
                    "<span class=\"mc-lbl\">Bug — infinite recursion</span>"
                    + io_split(
                        "def __set__(self, obj, value):\n"
                        "    obj.price = value   # calls __set__ again!",
                    )
                    + "</div>"
                    "<div class=\"mc-col mc-good\">"
                    "<span class=\"mc-lbl\">Fix — write into __dict__</span>"
                    + io_split(
                        "def __set__(self, obj, value):\n"
                        "    obj.__dict__[self.name] = value  # safe store",
                    )
                    + "</div></div>"
                    '<p class="step-result"><b>Takeaway:</b> '
                    "guard = descriptor · cupboard storage = <code>__dict__</code>.</p>"
                ),
            },
        ],
        "interview_qa": [
            {"q": "Is @property a descriptor?", "a": "Yes — start here. Built-in <b>data</b> descriptor: getter → <code>__get__</code>, setter → <code>__set__</code>."},
            {"q": "What is a descriptor in one line?", "a": "A helper object that sits between your code and an attribute and controls how it is read, written, or deleted."},
            {"q": "Non-data vs data descriptor?", "a": "Non-data has only <code>__get__</code> — a normal instance write can bypass it. Data has <code>__set__</code> too — every assignment goes through the helper (can validate)."},
            {"q": "Why use obj.__dict__ inside __set__?", "a": "To store the value without calling the descriptor again. <code>obj.price = value</code> inside <code>__set__</code> causes infinite recursion."},
            {"q": "When custom descriptor instead of @property?", "a": "When the same validation/access logic must be reused across many classes or fields (ORM-style columns)."},
        ],
    },
    17: {
        "steps": [
            {
                "title": "Step 1 — Lazy iterators (why generators exist)",
                "body": "From <a href=\"https://realpython.com/introduction-to-python-generators/\" target=\"_blank\" rel=\"noopener\">Real Python</a>: generators return a <b>lazy iterator</b> — loop like a list, but do <b>not</b> store all contents in memory. Loading a huge CSV with <code>file.read().split()</code> can raise <code>MemoryError</code>; <code>yield</code> one row at a time stays safe.",
            },
            {
                "title": "Step 2 — yield vs return + same function compared",
                "body": "<code>return</code> ends with one result (or a full list). <code>yield</code> marks a <b>generator function</b> — it pauses and can produce many values over time.<div class=\"step-pre\"># WITHOUT yield — returns a complete list\ndef parse_lines_list(f):\n    results = []\n    for line in f:\n        results.append(line.strip())\n    return results\n\n# WITH yield — generator: one line when asked\ndef parse_lines(f):\n    for line in f:\n        yield line.strip()\n\n# Caller looks the same:\n# for row in parse_lines(open(\"data.csv\")):\n#     print(row)</div><p class=\"step-result\">Generator expression (short form, no yield keyword): <code>(line for line in open(path))</code></p>",
            },
            {
                "title": "Step 3 — Infinite sequences & pipelines",
                "body": "Only generators can model infinite sequences safely (memory is finite). You can also chain generators into a pipeline without building giant intermediate lists.<div class=\"step-pre\">def infinite_sequence():\n    n = 0\n    while True:\n        yield n\n        n += 1\n\ngen = infinite_sequence()\nnext(gen); next(gen)   # 0, then 1 — stop manually</div>",
            },
            {
                "title": "Step 4 — Iterator protocol & itertools",
                "body": (
                    "An <b>iterable</b> has <code>__iter__</code> (can start a loop). "
                    "An <b>iterator</b> has <code>__iter__</code> and <code>__next__</code> "
                    "(gives the next value). "
                    "<code>for</code> calls these until <code>StopIteration</code>."
                    "<table class=\"data-tbl\" style=\"margin:6px 0;font-size:12px\">"
                    "<tr><th></th><th>Has</th><th>Example</th></tr>"
                    "<tr><td>Iterable</td><td><code>__iter__</code></td>"
                    "<td><code>list</code>, <code>range</code>, generator function result</td></tr>"
                    "<tr><td>Iterator</td><td><code>__iter__</code> + <code>__next__</code></td>"
                    "<td>what <code>iter(list)</code> returns; generators</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0\"><b>1) Full custom iterator</b> — "
                    "<code>for</code> uses <code>__iter__</code> / <code>__next__</code> for you:</p>"
                    + io_split(
                        "class CountDown:\n"
                        "    def __init__(self, start):\n"
                        "        self.n = start          # CREATE instance var n on this object (copies value of start)\n"
                        "\n"
                        "    def __iter__(self):\n"
                        "        return self          # I am my own iterator\n"
                        "\n"
                        "    def __next__(self):\n"
                        "        if self.n <= 0:        # self.n = this object's current count\n"
                        "            raise StopIteration\n"
                        "        self.n -= 1             # same as self.n = self.n - 1 (count down by 1)\n"
                        "        return self.n + 1     # return old value (after -=1, add 1 back)\n"
                        "\n"
                        "# for calls iter(), then next() until StopIteration\n"
                        "# iter() works because of __iter__; next() works because of __next__\n"
                        "for x in CountDown(3):\n"
                        "    print(x)\n"
                        "\n"
                        "# same idea by hand:\n"
                        "it = iter(CountDown(2))   # calls __iter__\n"
                        "print(next(it))             # calls __next__\n"
                        "print(next(it))             # calls __next__ again",
                        {17: "3\n2\n1", 21: "2", 22: "1"},
                    )
                    + "<p style=\"font-size:12px;margin:8px 0 4px\">"
                    "<b>2) itertools</b> — ready-made lazy helpers "
                    "(no giant intermediate lists):</p>"
                    + io_split(
                        "from itertools import chain, islice\n"
                        "\n"
                        "# chain — stitch iterables as one stream\n"
                        "print(list(chain([1, 2], [3, 4])))\n"
                        "\n"
                        "# islice — take first N from a long/infinite source\n"
                        "print(list(islice(range(100), 5)))\n"
                        "\n"
                        "# combine: first 3 from a chain\n"
                        "print(list(islice(chain(\"ab\", \"cd\"), 3)))",
                        {4: "[1, 2, 3, 4]", 7: "[0, 1, 2, 3, 4]", 10: "['a', 'b', 'c']"},
                    )
                    + '<p class="step-result"><b>Takeaway:</b> '
                    "generators already follow this protocol. "
                    "<code>itertools</code> builds pipelines on top without loading everything.</p>"
                ),
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
                "title": "Step 4 — with vs without mypy",
                "body": (
                    "Same bad call — compare <b>input</b> (command) and <b>output</b> (screen)."
                    '<div class="step-pre">'
                    "from decimal import Decimal\n"
                    "\n"
                    "def charge(amount: Decimal, currency: str) -> str:\n"
                    "    return f\"Charged {amount} {currency}\"\n"
                    "\n"
                    'result = charge("100", 91)  # wrong types\n'
                    "print(result)"
                    "</div>"
                    '<table class="data-tbl">'
                    "<tr><th>Case</th><th>Input</th><th>Output</th></tr>"
                    "<tr>"
                    "<td><b>Without mypy</b></td>"
                    "<td><code>python app.py</code></td>"
                    "<td>Program runs. Hints ignored.<br>"
                    "<code>Charged 100 91</code><br>"
                    "(no automatic type error)</td>"
                    "</tr>"
                    "<tr>"
                    "<td><b>With mypy</b></td>"
                    "<td><code>mypy app.py</code></td>"
                    "<td>Does <b>not</b> run the program. Reports errors, e.g.:<br>"
                    "<code>error: Argument 1 to \"charge\" has incompatible type \"str\"; expected \"Decimal\"</code><br>"
                    "<code>error: Argument 2 to \"charge\" has incompatible type \"int\"; expected \"str\"</code><br>"
                    "<code>Found 2 errors in 1 file (checked 1 source file)</code></td>"
                    "</tr>"
                    "</table>"
                    '<p class="step-result">'
                    "<b>Workflow:</b> <code>pip install mypy</code> → "
                    "<code>mypy app.py</code> (fix if needed) → "
                    "<code>python app.py</code>."
                    "</p>"
                ),
            },
        ],
        "interview_qa": [
            {"q": "Do type hints slow Python down?", "a": "No — they are stored as annotations and ignored at runtime unless you use a validator like Pydantic or FastAPI."},
            {"q": "Optional[str] means what?", "a": "The value can be a <code>str</code> or <code>None</code>. In 3.10+: <code>str | None</code>."},
            {"q": "What is a Protocol?", "a": "Defines an interface by method signatures — any class with matching methods satisfies it, without explicit inheritance."},
            {"q": "Does mypy run automatically when I run python app.py?", "a": "No. <code>python app.py</code> ignores type hints and runs the code. You must run <code>mypy app.py</code> yourself (or in CI) to catch type mismatches before execution."},
            {"q": "Why does mypy flag charge(\"100\", 91) when the hint uses Decimal?", "a": "Because argument types do not match: <code>\"100\"</code> is <code>str</code> (needs <code>Decimal</code>), and <code>91</code> is <code>int</code> (needs <code>str</code>)."},
            {"q": "Why use mypy?", "a": "Finds type mismatches before deployment — like a lightweight compiler check. Without it, Python may still run bad calls."},
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
                "title": "Step 1 — Simplest try / except",
                "body": (
                    "<code>try</code> runs risky code. <code>except</code> runs if an error happens — "
                    "the program can continue instead of crashing."
                    + csharp_compare_btn("try-catch")
                    + side_by_side(
                        "def div(a, b):\n"
                        "    try:\n"
                        "        print(a / b)\n"
                        "    except:\n"
                        "        print(\"Something Went Wrong\")\n"
                        "\n"
                        "div(10, 5)\n"
                        "div(10, 0)",
                        "2.0\n"
                        "Something Went Wrong",
                        left_label="Code",
                        right_label="Output",
                    )
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<code>div(10, 5)</code> prints <code>2.0</code>. "
                    "<code>div(10, 0)</code> hits divide-by-zero — "
                    "<code>except</code> prints <code>Something Went Wrong</code> instead of crashing."
                    "</p>"
                    "<p class=\"step-result\">"
                    "<b>Next steps:</b> learn error <b>types</b>, catch the right one, "
                    "then add <code>else</code> / <code>finally</code>."
                    "</p>"
                ),
            },
            {
                "title": "Step 2 — NameError, TypeError, ValueError",
                "body": (
                    "Each error has a <b>type name</b>. Read the message — it tells you what went wrong."
                    + _ex_error_diagram()
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>NameError</b> = variable/name missing · "
                    "<b>TypeError</b> = wrong types for the operation · "
                    "<b>ValueError</b> = type OK, value not allowed."
                    "</p>"
                    "<p style=\"font-size:12px;margin:8px 0;line-height:1.45\">"
                    "<b>Hierarchy</b> — all inherit from <code>Exception</code>:"
                    "</p>"
                    '<div class="step-pre">'
                    "BaseException\n"
                    " └── Exception\n"
                    "      ├── NameError\n"
                    "      ├── TypeError\n"
                    "      ├── ValueError\n"
                    "      ├── ZeroDivisionError\n"
                    "      └── FileNotFoundError"
                    "</div>"
                    "<p class=\"step-result\">"
                    "<b>Rule:</b> catch the <b>specific</b> type you can handle."
                    "</p>"
                ),
            },
            {
                "title": "Step 3 — Match the right except (not bare except)",
                "body": (
                    "Same ladder for every example: "
                    "<code>try</code> → specific <code>except</code> → "
                    "<code>except Exception</code> → <code>else</code> → <code>finally</code>. "
                    "<mark class=\"hl-path\">Yellow</mark> = path that runs "
                    "(<code>finally</code> is always yellow — it always runs)."
                    + _ex_error_diagram()
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Side by side</b> — same ladder, different <code>try</code> line:"
                    "</p>"
                    '<div class="ex-row">'
                    '<div class="ex-card">'
                    '<div class="ex-title">Path → NameError</div>'
                    + _ex_ladder_path("z * 1", "NameError")
                    + '<p style="font-size:11px;margin:4px 0 0;line-height:1.35">'
                    "Output:<br>"
                    "<code>Name Error: name 'z' is not defined</code><br>"
                    "<code>cleanup always</code>"
                    "</p>"
                    "</div>"
                    '<div class="ex-card">'
                    '<div class="ex-title">Path → TypeError</div>'
                    + _ex_ladder_path('10 + "Hello"', "TypeError")
                    + '<p style="font-size:11px;margin:4px 0 0;line-height:1.35">'
                    "Output:<br>"
                    "<code>Type Error: unsupported operand...</code><br>"
                    "<code>cleanup always</code>"
                    "</p>"
                    "</div>"
                    '<div class="ex-card">'
                    '<div class="ex-title">Path → ValueError</div>'
                    + _ex_ladder_path('int("Hello")', "ValueError")
                    + '<p style="font-size:11px;margin:4px 0 0;line-height:1.35">'
                    "Output:<br>"
                    "<code>Value Error: invalid literal...</code><br>"
                    "<code>cleanup always</code>"
                    "</p>"
                    "</div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:8px 0;line-height:1.45\">"
                    "<b>Correct code</b> — no error → skips all <code>except</code> → "
                    "goes to <code>else</code> → then <code>finally</code>:"
                    "</p>"
                    '<div class="ex-row ex-row-2">'
                    '<div class="ex-card">'
                    '<div class="ex-title">Correct → else (int works)</div>'
                    + _ex_ladder_path('n = int("42")', "else")
                    + '<p style="font-size:11px;margin:4px 0 0;line-height:1.35">'
                    "<b>try</b> succeeds (<code>n = 42</code>) → "
                    "no <code>except</code> · yellow <code>else</code> · yellow <code>finally</code>.<br>"
                    "Output:<br>"
                    "<code>no error — success path</code><br>"
                    "<code>cleanup always</code>"
                    "</p>"
                    "</div>"
                    '<div class="ex-card">'
                    '<div class="ex-title">Path → except Exception (10 / 0)</div>'
                    + _ex_ladder_path("10 / 0", "Exception")
                    + '<p style="font-size:11px;margin:4px 0 0;line-height:1.35">'
                    "<code>ZeroDivisionError</code> is not Name/Type/Value — "
                    "hits <code>except Exception</code>. <code>else</code> skipped.<br>"
                    "Output:<br>"
                    "<code>Exception: division by zero</code><br>"
                    "<code>cleanup always</code>"
                    "</p>"
                    "</div>"
                    "</div>"
                    '<table class="data-tbl">'
                    "<tr><th>Block</th><th>When it runs</th></tr>"
                    "<tr><td><code>except NameError / TypeError / ValueError</code></td>"
                    "<td>Only that specific error</td></tr>"
                    "<tr><td><code>except Exception</code></td>"
                    "<td>Other exceptions not listed above "
                    "(e.g. <code>ZeroDivisionError</code>)</td></tr>"
                    "<tr><td><code>else</code></td>"
                    "<td>Only if <code>try</code> had <b>no</b> exception "
                    "(e.g. <code>int(\"42\")</code>)</td></tr>"
                    "<tr><td><code>finally</code></td>"
                    "<td><b>Always</b> — success or error (cleanup)</td></tr>"
                    "</table>"
                    "<p class=\"step-result\">"
                    "<b>Rule:</b> yellow = path taken. "
                    "Specific <code>except</code> first · "
                    "<code>except Exception</code> next · "
                    "<code>else</code> on success · "
                    "<code>finally</code> always."
                    "</p>"
                ),
            },
            {
                "title": "Step 4 — try, except, else & finally",
                "body": (
                    "Handle errors gracefully. "
                    "<code>else</code> runs only if <code>try</code> succeeds. "
                    "<code>finally</code> always runs (cleanup). "
                    + csharp_compare_btn("try-catch")
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Purpose of <code>else</code>:</b> put <b>success-only</b> work there — "
                    "code that should run after a clean <code>try</code>, but whose own errors "
                    "must <b>not</b> be caught by the same <code>except</code>. "
                    "Keep <code>try</code> small: only the risky lines."
                    "</p>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad"><span class="mc-lbl">Without else — success code inside try</span>'
                    '<div class="step-pre">'
                    "def build_report(n):\n"
                    "    if n &lt; 1:\n"
                    "        raise ValueError(\"n must be >= 1\")\n"
                    "    return f\"Report for {n}\"\n\n"
                    "user_input = \"0\"   # this IS a number\n\n"
                    "try:\n"
                    "    n = int(user_input)        # OK → n = 0\n"
                    "    report = build_report(n)  # raises ValueError\n"
                    "    print(report)\n"
                    "except ValueError:\n"
                    "    print(\"not a number\")    # WRONG message"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>What “handler catches success code too” means:</b> "
                    "one <code>except ValueError</code> covers <b>every</b> line in <code>try</code>. "
                    "<code>int(\"0\")</code> succeeds. Then <code>build_report(0)</code> raises a "
                    "<b>different</b> <code>ValueError</code> (bad report input, not a parse fail). "
                    "Python still jumps to the same handler → prints "
                    "<code>\"not a number\"</code>. The user thinks typing failed. The real bug is hidden."
                    "</p>"
                    "</div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">With else — success code after clean try</span>'
                    '<div class="step-pre">'
                    "user_input = \"42\"\n\n"
                    "try:\n"
                    "    n = int(user_input)       # ONLY risky parse\n"
                    "except ValueError:\n"
                    "    print(\"not a number\")\n"
                    "else:\n"
                    "    # runs ONLY if int() worked\n"
                    "    report = build_report(n)\n"
                    "    print(report)\n"
                    "finally:\n"
                    "    print(\"cleanup always runs\")"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Why:</b> <code>else</code> runs only on success. "
                    "Errors from <code>build_report</code> are <b>not</b> treated as parse errors."
                    "</p>"
                    "</div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Same input, two meanings of ValueError:</b>"
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th>user_input</th><th>int()</th><th>build_report</th>"
                    "<th>Without else (in try)</th><th>With else</th></tr>"
                    "<tr><td><code>\"abc\"</code></td><td>fails</td><td>never runs</td>"
                    "<td><code>not a number</code> ✓</td>"
                    "<td><code>not a number</code> ✓</td></tr>"
                    "<tr><td><code>\"0\"</code></td><td>OK (<code>0</code>)</td>"
                    "<td><code>ValueError</code> (n &lt; 1)</td>"
                    "<td><code>not a number</code> ✗ <b>wrong</b></td>"
                    "<td>real error: <code>n must be &gt;= 1</code> ✓</td></tr>"
                    "<tr><td><code>\"42\"</code></td><td>OK</td><td>OK</td>"
                    "<td>prints report ✓</td><td>prints report ✓</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Why not put success work in <code>finally</code>?</b> "
                    "<code>finally</code> runs on <b>success and failure</b> — it is for cleanup, not “continue only if it worked.”"
                    "</p>"
                    '<div class="step-pre">'
                    "# BAD — success code in finally\n"
                    "try:\n"
                    "    n = int(user_input)\n"
                    "except ValueError:\n"
                    "    print(\"not a number\")\n"
                    "finally:\n"
                    "    report = build_report(n)  # runs even when parse failed!\n"
                    "    print(report)\n"
                    "\n"
                    "# user_input = \"abc\" → except runs, then finally still runs\n"
                    "# → NameError: n was never set  (or wrong report if n existed)"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Also wrong without else</b> — success code after the whole <code>try/except</code> "
                    "(same bug C# would have if <code>catch</code> does not stop):"
                    "</p>"
                    '<div class="step-pre">'
                    "try:\n"
                    "    n = int(user_input)\n"
                    "except ValueError:\n"
                    "    print(\"not a number\")\n"
                    "# This still runs after a failed parse → NameError or wrong use of n\n"
                    "print(f\"parsed: {n}\")"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>How C# handles it (no <code>else</code> keyword):</b> "
                    "early <code>return</code> in <code>catch</code>, then success code after — "
                    "or use <code>int.TryParse</code>. "
                    + csharp_compare_btn("try-catch")
                    + "</p>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-good"><span class="mc-lbl">Python — else</span>'
                    '<div class="step-pre">'
                    "try:\n"
                    "    n = int(user_input)\n"
                    "except ValueError:\n"
                    "    print(\"not a number\")\n"
                    "else:\n"
                    "    report = build_report(n)\n"
                    "    print(report)\n"
                    "finally:\n"
                    "    print(\"cleanup\")"
                    "</div>"
                    "</div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">C# — return in catch (same job)</span>'
                    '<div class="step-pre">'
                    "int n;\n"
                    "try\n"
                    "{\n"
                    "    n = int.Parse(userInput);  // risky\n"
                    "}\n"
                    "catch (FormatException)\n"
                    "{\n"
                    "    Console.WriteLine(\"not a number\");\n"
                    "    return;   // STOP — skip success path\n"
                    "}\n"
                    "finally\n"
                    "{\n"
                    "    Console.WriteLine(\"cleanup\");\n"
                    "}\n"
                    "// Reached only if Parse worked\n"
                    "var report = BuildReport(n);\n"
                    "Console.WriteLine(report);"
                    "</div>"
                    "</div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>C# without <code>return</code></b> has the same bug as Python without <code>else</code> — "
                    "success lines after try/catch still run after a handled error. "
                    "Python uses <code>else</code>; C# uses <code>return</code> (or a flag / <code>TryParse</code>)."
                    "</p>"
                    '<div class="step-pre">'
                    "// C# alternative — often preferred for parse (no exception for bad input)\n"
                    "if (!int.TryParse(userInput, out int n))\n"
                    "{\n"
                    "    Console.WriteLine(\"not a number\");\n"
                    "    return;\n"
                    "}\n"
                    "var report = BuildReport(n);  // only if parse OK\n"
                    "Console.WriteLine(report);"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Walkthrough</b> (with <code>else</code>):"
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th>user_input</th><th>What runs</th><th>Output</th></tr>"
                    "<tr><td><code>\"42\"</code></td>"
                    "<td><code>try</code> OK → <code>else</code> → <code>finally</code></td>"
                    "<td>report printed, then cleanup</td></tr>"
                    "<tr><td><code>\"abc\"</code></td>"
                    "<td><code>except</code> → skip <code>else</code> → <code>finally</code></td>"
                    "<td><code>not a number</code>, then cleanup</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Rule:</b> <code>try</code> = risk · <code>except</code> = handle that risk · "
                    "<code>else</code> = “it worked, continue” · <code>finally</code> = always cleanup.<br>"
                    "<b>C# map:</b> <code>else</code> ≈ code after try/catch + <code>return</code> in catch "
                    "(or <code>TryParse</code>)."
                    "</p>"
                ),
            },
            {
                "title": "Step 5 — Custom exceptions",
                "body": (
                    "Same <code>raise</code> / <code>except</code> machinery. "
                    "The difference is the <b>type name</b> and extra data — "
                    "so callers can catch <b>only</b> your domain rule. "
                    + csharp_compare_btn("raise-reraise")
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Side by side — normal vs custom</b> "
                    "(same <code>set_age(-5)</code> call):"
                    "</p>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad"><span class="mc-lbl">Normal — built-in ValueError</span>'
                    '<div class="step-pre">'
                    "def set_age(age):\n"
                    "    if age &lt; 0:\n"
                    "        raise ValueError(\"must be positive\")\n"
                    "    return age\n"
                    "\n"
                    "try:\n"
                    "    n = int(user_input)   # can also raise ValueError\n"
                    "    set_age(n)\n"
                    "except ValueError:\n"
                    "    print(\"bad input\")   # which one failed?"
                    "</div>"
                    "</div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">Custom — ValidationError</span>'
                    '<div class="step-pre">'
                    "class ValidationError(Exception):\n"
                    "    def __init__(self, field, message):\n"
                    "        self.field = field\n"
                    "        super().__init__(message)\n"
                    "\n"
                    "def set_age(age):\n"
                    "    if age &lt; 0:\n"
                    "        raise ValidationError(\n"
                    "            \"age\", \"must be positive\")\n"
                    "    return age\n"
                    "\n"
                    "try:\n"
                    "    n = int(user_input)\n"
                    "    set_age(n)\n"
                    "except ValidationError as e:\n"
                    "    print(e.field, e)      # age / must be positive\n"
                    "except ValueError:\n"
                    "    print(\"not a number\") # only the parse"
                    "</div>"
                    "</div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>One more realistic example</b> — ATM withdraw: "
                    "bad typed amount vs not enough money. Same mix-up if both are "
                    "<code>ValueError</code>."
                    "</p>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad"><span class="mc-lbl">Normal — one ValueError for both</span>'
                    '<div class="step-pre">'
                    "def withdraw(balance, amount_text):\n"
                    "    amount = float(amount_text)  # \"abc\" → ValueError\n"
                    "    if amount > balance:\n"
                    "        raise ValueError(\"insufficient funds\")\n"
                    "    return balance - amount\n"
                    "\n"
                    "try:\n"
                    "    withdraw(100, amount_text)\n"
                    "except ValueError:\n"
                    "    print(\"withdraw failed\")\n"
                    "    # typed \"abc\"? or only had $100?"
                    "</div>"
                    "</div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">Custom — InsufficientFundsError</span>'
                    '<div class="step-pre">'
                    "class InsufficientFundsError(Exception):\n"
                    "    def __init__(self, balance, amount):\n"
                    "        self.balance = balance\n"
                    "        self.amount = amount\n"
                    "        super().__init__(\n"
                    "            f\"need {amount}, have {balance}\")\n"
                    "\n"
                    "def withdraw(balance, amount_text):\n"
                    "    amount = float(amount_text)\n"
                    "    if amount > balance:\n"
                    "        raise InsufficientFundsError(\n"
                    "            balance, amount)\n"
                    "    return balance - amount\n"
                    "\n"
                    "try:\n"
                    "    withdraw(100, amount_text)\n"
                    "except InsufficientFundsError as e:\n"
                    "    print(f\"short by {e.amount - e.balance}\")\n"
                    "except ValueError:\n"
                    "    print(\"amount is not a number\")"
                    "</div>"
                    "</div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "Same idea as age: parse fail stays <code>ValueError</code>; "
                    "business rule gets its own type + extra fields "
                    "(<code>e.balance</code>, <code>e.amount</code>)."
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th></th><th>Normal (ValueError)</th><th>Custom (ValidationError)</th></tr>"
                    "<tr><td><b>Type name</b></td>"
                    "<td>Built-in — many things raise it</td>"
                    "<td>Yours — only your rule</td></tr>"
                    "<tr><td><b>except</b></td>"
                    "<td><code>except ValueError</code> catches parse "
                    "<b>and</b> age rule — mixed</td>"
                    "<td><code>except ValidationError</code> = age rule only; "
                    "parse stays <code>ValueError</code></td></tr>"
                    "<tr><td><b>Extra data</b></td>"
                    "<td>Message string only</td>"
                    "<td><code>e.field</code> + message (highlight the form field)</td></tr>"
                    "<tr><td><b>Team reads traceback</b></td>"
                    "<td><code>ValueError: must be positive</code> — vague</td>"
                    "<td><code>ValidationError: must be positive</code> — domain rule</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>What is the same?</b> Still <code>raise</code> + <code>try/except</code>. "
                    "Custom is just a new class under <code>Exception</code>.<br>"
                    "<b>What is different?</b> Callers can tell “bad number text” from "
                    "“age rule failed” — and get <code>e.field</code>."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Full custom class</b> (define + raise + catch):"
                    "</p>"
                    '<div class="step-pre">'
                    "class ValidationError(Exception):\n"
                    "    def __init__(self, field, message):\n"
                    "        self.field = field              # extra context for UI / logs\n"
                    "        super().__init__(message)       # standard exception text\n"
                    "\n"
                    "def set_age(age):\n"
                    "    if age &lt; 0:\n"
                    "        raise ValidationError(\"age\", \"must be positive\")\n"
                    "    return age\n"
                    "\n"
                    "try:\n"
                    "    set_age(-5)\n"
                    "except ValidationError as e:\n"
                    "    print(e.field)    # age\n"
                    "    print(e)          # must be positive\n"
                    "\n"
                    "# set_age(30)  → returns 30, no exception"
                    "</div>"
                ),
            },
            {
                "title": "Step 6 — raise & re-raise",
                "body": (
                    "<code>raise</code> throws. Bare <code>raise</code> continues the "
                    "<b>same</b> error. <code>raise ... from ...</code> throws a "
                    "<b>new</b> error and keeps the original as the cause. "
                    + csharp_compare_btn("raise-reraise")
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Side by side — payment checkout</b> "
                    "(amount rule, wrap bank error, log timeout, avoid <code>raise e</code>):"
                    "</p>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-good"><span class="mc-lbl">1 · raise New — throw a NEW error</span>'
                    + side_by_side(
                        "def charge(amount):\n"
                        "    if amount &lt;= 0:\n"
                        "        raise ValueError(\n"
                        '            "Payment amount must be greater than 0"\n'
                        "        )\n"
                        "    return charge_card(amount)\n"
                        "\n"
                        "charge(0)",
                        "Traceback (most recent call last):\n"
                        '  File "app.py", line 8, in &lt;module&gt;\n'
                        "    charge(0)\n"
                        '  File "app.py", line 4, in charge\n'
                        "    raise ValueError(\n"
                        '        "Payment amount must be greater than 0")\n'
                        "ValueError: Payment amount must be greater than 0",
                        left_label="# CODE",
                        right_label=(
                            "Traceback / message — one error, "
                            "site is raise in charge"
                        ),
                    )
                    + "</div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">2 · raise New from e — NEW + keep cause</span>'
                    + side_by_side(
                        "class PaymentError(Exception):\n"
                        "    pass\n"
                        "\n"
                        "try:\n"
                        "    bank_charge(order_id)   # SDK / gateway\n"
                        "except ConnectionError as e:\n"
                        '    raise PaymentError("Payment failed") from e',
                        "Traceback (most recent call last):\n"
                        '  File "app.py", line 6, in &lt;module&gt;\n'
                        "    bank_charge(order_id)\n"
                        "ConnectionError: gateway unreachable\n"
                        "\n"
                        "The above exception was the direct cause of\n"
                        "the following exception:\n"
                        "\n"
                        "Traceback (most recent call last):\n"
                        '  File "app.py", line 8, in &lt;module&gt;\n'
                        '    raise PaymentError("Payment failed") from e\n'
                        "PaymentError: Payment failed",
                        left_label="# CODE",
                        right_label=(
                            "Traceback / message — two blocks: "
                            "bank cause, then API error"
                        ),
                    )
                    + "</div>"
                    "</div>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-good"><span class="mc-lbl">3 · bare raise — SAME error continues</span>'
                    + side_by_side(
                        "try:\n"
                        "    bank_charge(order_id)\n"
                        "except TimeoutError:\n"
                        "    log_error()   # log order id\n"
                        "    raise         # SAME TimeoutError",
                        "Traceback (most recent call last):\n"
                        '  File "app.py", line 3, in &lt;module&gt;\n'
                        "    bank_charge(order_id)\n"
                        "TimeoutError: payment gateway timed out",
                        left_label="# CODE",
                        right_label=(
                            "Traceback / message — raise line is not listed. "
                            "Most recent frame: bank_charge()"
                        ),
                    )
                    + "</div>"
                    '<div class="mc-col mc-bad"><span class="mc-lbl">4 · avoid raise e — same type, NEW traceback</span>'
                    + side_by_side(
                        "try:\n"
                        "    bank_charge(order_id)\n"
                        "except TimeoutError as e:\n"
                        "    log_error()\n"
                        "    raise e    # NOT the same as raise",
                        "Traceback (most recent call last):\n"
                        '  File "app.py", line 6, in &lt;module&gt;\n'
                        "    raise e\n"
                        '  File "app.py", line 3, in &lt;module&gt;\n'
                        "    bank_charge(order_id)\n"
                        "TimeoutError: payment gateway timed out",
                        left_label="# CODE",
                        right_label=(
                            "Traceback / message — same TimeoutError, "
                            "but most recent frame is raise e"
                        ),
                    )
                    + "</div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Better realistic example — payment processing</b> "
                    "(e-commerce checkout). Same four raise patterns, one story — "
                    "<b>ordered by preference</b>:"
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th>Priority</th><th>Case</th><th>Realistic code</th>"
                    "<th>Error thrown to caller</th><th>Original cause kept?</th>"
                    "<th>Recommendation</th></tr>"
                    "<tr>"
                    "<td><b>1</b></td>"
                    "<td><b>New problem</b><br><code>raise New(...)</code></td>"
                    "<td><code>raise ValueError(\"Payment amount must be greater than 0\")</code></td>"
                    "<td>Only the validation error<br>"
                    "<code>ValueError: Payment amount must be greater than 0</code></td>"
                    "<td>No</td>"
                    "<td>&#10004; <b>Very common</b> — new validation / business rule "
                    "(nothing else threw first).</td></tr>"
                    "<tr>"
                    "<td><b>2</b></td>"
                    "<td><b>Wrap existing</b><br><code>raise New from e</code></td>"
                    "<td><code>raise PaymentError(\"Payment failed\") from e</code></td>"
                    "<td><code>PaymentError: Payment failed</code> "
                    "→ original shown as cause</td>"
                    "<td>Yes (<code>__cause__</code>)</td>"
                    "<td>&#10004; <b>Best when changing type</b> — convert SDK/bank "
                    "error into a meaningful API error.</td></tr>"
                    "<tr>"
                    "<td><b>3</b></td>"
                    "<td><b>Rethrow same</b><br><code>raise</code> (bare)</td>"
                    "<td><code>except TimeoutError: log_error(); raise</code></td>"
                    "<td>Original error, unchanged<br>"
                    "<code>TimeoutError: …</code></td>"
                    "<td>Yes (same object, same traceback)</td>"
                    "<td>&#10004; <b>Correct</b> — log order id, then let the same "
                    "error continue.</td></tr>"
                    "<tr>"
                    "<td><b>4</b></td>"
                    "<td><b>Avoid</b><br><code>raise e</code></td>"
                    "<td><code>except TimeoutError as e: raise e</code></td>"
                    "<td>Same error, but traceback is less clean "
                    "(top line is <code>raise e</code>)</td>"
                    "<td>Partial — traceback resets</td>"
                    "<td>&#9888; <b>Generally avoid</b> — use bare <code>raise</code> "
                    "instead.</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Priority / preference (quick pick):</b> "
                    + csharp_compare_btn("raise-reraise")
                    + "</p>"
                    '<table class="data-tbl">'
                    "<tr><th>Priority</th><th>Situation</th>"
                    "<th>Preferred syntax</th>"
                    "<th>Error thrown to caller</th>"
                    "<th>Recommendation</th></tr>"
                    "<tr><td><b>1</b></td>"
                    "<td>Creating a <b>new validation / business error</b></td>"
                    "<td><code>raise ValueError(...)</code> "
                    "or your own exception</td>"
                    "<td><code>ValueError: Invalid age</code></td>"
                    "<td>&#10004; Very common</td></tr>"
                    "<tr><td><b>2</b></td>"
                    "<td><b>Converting / wrapping</b> an existing low-level error</td>"
                    "<td><code>raise MyError(...) from e</code></td>"
                    "<td><code>PaymentError: Payment failed</code> → "
                    "with the original error shown as the cause</td>"
                    "<td>&#10004; Best when changing exception type</td></tr>"
                    "<tr><td><b>3</b></td>"
                    "<td><b>Log and rethrow</b> the same error</td>"
                    "<td><code>raise</code></td>"
                    "<td>The original error, unchanged</td>"
                    "<td>&#10004; Correct</td></tr>"
                    "<tr><td><b>4</b></td>"
                    "<td><code>except … as e: raise e</code></td>"
                    "<td><code>raise e</code></td>"
                    "<td>The original error, but traceback information is less clean</td>"
                    "<td>&#9888; Generally avoid</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>How to read the story:</b><br>"
                    "• Cart amount <code>&lt;= 0</code> → you found the rule → "
                    "<b>Priority 1 — raise New</b> (<code>ValueError</code>).<br>"
                    "• Bank SDK throws a low-level error → wrap for the API → "
                    "<b>Priority 2 — raise PaymentError(...) from e</b>.<br>"
                    "• Gateway <code>TimeoutError</code> → log order id, then "
                    "<b>Priority 3 — bare raise</b> so ops still sees the real timeout.<br>"
                    "• Don’t <code>raise e</code> (Priority 4 / avoid) — "
                    "same timeout message, worse stack."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Pick in one line:</b> "
                    "business rule → <b>raise New</b> · "
                    "wrap SDK/bank error → <b>from e</b> · "
                    "log then continue → <b>bare raise</b> · "
                    "never <b>raise e</b>."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>C# map:</b> <code>raise</code> ≈ <code>throw new ...</code> · "
                    "bare <code>raise</code> ≈ <code>throw;</code> · "
                    "<code>raise New from e</code> ≈ <code>throw new Exception(\"…\", e)</code> "
                    "(<code>InnerException</code>) · "
                    "<code>raise e</code> ≈ <code>throw ex;</code> (also resets stack — avoid)."
                    "</p>"
                ),
            },
        ],
        "interview_qa": [
            {
                "q": "NameError vs TypeError vs ValueError?",
                "a": (
                    "<code>NameError</code> — name not defined (e.g. <code>z</code> never assigned). "
                    "<code>TypeError</code> — wrong types for the operation (e.g. <code>10 + \"Hello\"</code>). "
                    "<code>ValueError</code> — type OK, bad value (e.g. <code>int(\"Hello\")</code>)."
                ),
            },
            {"q": "Why not use bare except?", "a": "It catches everything including <code>KeyboardInterrupt</code> and hides the real bug. Catch specific exceptions you can handle."},
            {
                "q": "What does raise from do?",
                "a": (
                    "Throws a <b>new</b> error and links the original as "
                    "<code>__cause__</code> (C# <code>InnerException</code>). "
                    "Bare <code>raise</code> is different — same error continues, traceback kept. "
                    "Avoid <code>raise e</code> — it resets the traceback."
                ),
            },
            {
                "q": "In what order should you prefer raise patterns?",
                "a": (
                    "<b>1</b> new business/validation → <code>raise New(...)</code>. "
                    "<b>2</b> wrap low-level → <code>raise MyError(...) from e</code>. "
                    "<b>3</b> log then continue → bare <code>raise</code>. "
                    "<b>4</b> avoid <code>raise e</code> (traceback resets)."
                ),
            },
            {
                "q": "When does else run in try/except?",
                "a": (
                    "Only when <code>try</code> finishes with <b>no</b> exception. "
                    "Use it for success-only work so those lines are not covered by the same "
                    "<code>except</code>. If parse fails, <code>else</code> is skipped; "
                    "<code>finally</code> still runs."
                ),
            },
            {
                "q": "finally vs else?",
                "a": (
                    "<code>else</code> = success path only (keep <code>try</code> small). "
                    "<code>finally</code> = always (close files, unlock, cleanup) — "
                    "even after error or <code>return</code>."
                ),
            },
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
                "body": "Dict that remembers insertion order. In Python 3.7+ regular dicts also preserve order — OrderedDict adds extra methods.<div class=\"step-pre\">from collections import OrderedDict\n\nod = OrderedDict()\nod[\"a\"] = 1\nod[\"b\"] = 2\nprint(list(od.keys()))   # ['a', 'b']\nod.move_to_end(\"a\")\nprint(list(od.keys()))   # ['b', 'a']</div>",
            },
            {
                "title": "Step 3 — defaultdict",
                "body": (
                    "Auto-creates a default value for missing keys — great for grouping tickets by assignee."
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad"><span class="mc-lbl">Plain dict — set value</span>'
                    '<div class="step-pre">by_assignee = {}\n'
                    'by_assignee["Ravi"].append(101)\n'
                    '# KeyError: "Ravi" — key does not exist yet\n\n'
                    '# Manual fix every time:\n'
                    'if "Ravi" not in by_assignee:\n'
                    '    by_assignee["Ravi"] = []\n'
                    'by_assignee["Ravi"].append(101)</div></div>'
                    '<div class="mc-col mc-good"><span class="mc-lbl">&#10004; defaultdict(list)</span>'
                    '<div class="step-pre">from collections import defaultdict\n'
                    'by_assignee = defaultdict(list)\n'
                    'by_assignee["Ravi"].append(101)   # OK\n'
                    'by_assignee["Anu"].append(102)   # OK\n'
                    'print(dict(by_assignee))\n'
                    "# {'Ravi': [101], 'Anu': [102]}</div></div></div>"
                    '<p class="step-result"><b>One trap — read this slowly:</b><br>'
                    'You might write <code>if myDict["ghost"]:</code> meaning '
                    '&ldquo;only run if ghost already has tickets.&rdquo;<br>'
                    '<b>But Python checks the condition first.</b> To evaluate '
                    '<code>myDict["ghost"]</code>, it must <b>look up</b> that key — and '
                    '<code>defaultdict</code> creates <code>"ghost": []</code> on lookup.<br>'
                    'The empty list is falsy, so the <code>if</code> body is skipped — '
                    'but the unwanted key is already in the dict.</p>'
                    '<div class="step-pre">from collections import defaultdict\n'
                    'myDict = defaultdict(list)\n'
                    'print(dict(myDict))           # {}\n\n'
                    'if myDict["ghost"]:          # lookup runs FIRST → creates []\n'
                    '    print("has tickets") # never runs — [] is falsy\n\n'
                    'print(dict(myDict))           # {\'ghost\': []}  unwanted key!\n\n'
                    '# Safe — check membership without creating:\n'
                    'if "ghost" in myDict:\n'
                    '    print(myDict["ghost"])</div>'
                    '<div class="step-pre">from collections import defaultdict\n\n'
                    'groups = defaultdict(list)\n'
                    'for name, dept in [("Anu", "IT"), ("Ravi", "HR"), ("Priya", "IT")]:\n'
                    '    groups[dept].append(name)\n'
                    'print(dict(groups))\n'
                    '# {"IT": ["Anu", "Priya"], "HR": ["Ravi"]}</div>'
                ),
            },
            {
                "title": "Step 4 — ChainMap",
                "body": (
                    "Layers multiple dicts into one view. "
                    "<code>ChainMap(Dict1, Dict2)</code> checks <code>Dict1</code> first; "
                    "if the key is missing, it falls through to <code>Dict2</code>. "
                    "It does <b>not</b> copy or merge the dicts — it searches in order."
                    '<div class="step-pre">'
                    "# INPUT\n"
                    "from collections import ChainMap\n\n"
                    'Dict1 = {"color": "blue"}                   # checked first\n'
                    'Dict2 = {"color": "red", "size": "M"}       # fallback\n'
                    'print("Dict1:", Dict1)\n'
                    'print("Dict2:", Dict2)\n\n'
                    "CombinedDict = ChainMap(Dict1, Dict2)  # Dict1 first, then Dict2\n\n"
                    "print(CombinedDict)           # whole ChainMap\n"
                    'print(CombinedDict["color"])  # blue — in Dict1\n'
                    'print(CombinedDict["size"])   # M — not in Dict1 → Dict2\n\n'
                    "# OUTPUT\n"
                    "# Dict1: {'color': 'blue'}\n"
                    "# Dict2: {'color': 'red', 'size': 'M'}\n"
                    "# ChainMap({'color': 'blue'}, {'color': 'red', 'size': 'M'})\n"
                    "# blue\n"
                    "# M"
                    "</div>"
                    '<p class="step-result"><b>Lookup order:</b> '
                    '<code>ChainMap(Dict1, Dict2)</code> → try <code>Dict1</code>, then <code>Dict2</code>. '
                    '<b>First match wins.</b> Real apps: CLI args → env vars → config file defaults.</p>'
                ),
            },
            {
                "title": "Step 5 — namedtuple",
                "body": "Lightweight tuple with named fields — readable and immutable.<div class=\"step-pre\">from collections import namedtuple\n\nPoint = namedtuple(\"Point\", [\"x\", \"y\"])\np = Point(10, 20)\np.x, p.y   # 10, 20\np[0]       # 10 (still indexable)</div>",
            },
            {
                "title": "Step 6 — deque",
                "body": (
                    "Double-ended queue — fast append/pop at both ends. "
                    "<code>maxlen</code> is <b>optional</b>."
                    '<div class="mc-row">'
                    '<div class="mc-col mc-good"><span class="mc-lbl">1) deque() — no max</span>'
                    '<div class="step-pre">'
                    "from collections import deque\n\n"
                    "d = deque([1, 2, 3])      # grows freely\n"
                    "d.append(4)              # right → [1,2,3,4]\n"
                    "d.appendleft(0)          # left  → [0,1,2,3,4]\n"
                    "print(d.popleft())       # 0\n"
                    "print(list(d))           # [1, 2, 3, 4]"
                    "</div></div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">2) deque(maxlen=…) — rolling</span>'
                    '<div class="step-pre">'
                    "from collections import deque\n\n"
                    "d = deque(maxlen=2)      # keep last 2 only\n"
                    'd.append("hi")\n'
                    'd.append("ticket #42")\n'
                    'd.append("bye")          # "hi" dropped\n'
                    "print(list(d))           # ['ticket #42', 'bye']"
                    "</div></div></div>"
                    '<p class="step-result"><b>Rule:</b> <code>deque()</code> = unlimited. '
                    '<code>deque(maxlen=n)</code> = keep last <code>n</code> only.</p>'
                ),
            },
            {
                "title": "Step 7 — UserDict, UserList & UserString",
                "body": (
                    "<b>What they are:</b> wrappers around a real <code>dict</code> / <code>list</code> / <code>str</code> "
                    "stored in <code>.data</code>. Designed so you can <b>subclass and override</b> methods safely.<br><br>"
                    "<b>Why not subclass built-in <code>dict</code>?</b> "
                    "Built-in <code>dict</code> methods are implemented in C. Some call each other "
                    "<i>without</i> going through your Python overrides — so <code>d[\"A\"] = 1</code> "
                    "might bypass your <code>__setitem__</code>. "
                    "<code>UserDict</code> routes through Python methods, so your override always runs.<br><br>"
                    "<b>Line-by-line for the example:</b>"
                    "<div class=\"step-pre\">from collections import UserDict\n\n"
                    "class CaseInsensitiveDict(UserDict):\n"
                    "    def __setitem__(self, key, value):\n"
                    "        # __setitem__ runs for: d[key] = value\n"
                    "        # key.lower() → store under one form (\"Name\" and \"name\" → \"name\")\n"
                    "        super().__setitem__(key.lower(), value)\n"
                    "        # super() = UserDict.__setitem__ → writes into self.data\n\n"
                    "d = CaseInsensitiveDict()\n"
                    "d[\"Name\"] = \"Anu\"     # stored as key \"name\"\n"
                    "d[\"NAME\"] = \"Ravi\"    # same slot — overwrites\n"
                    "print(d[\"name\"])      # Ravi  (lookup still needs care — see tip)\n"
                    "print(d.data)         # {'name': 'Ravi'}  ← real dict inside</div>"
                    "<p class=\"step-result\">"
                    "<b><code>__setitem__(self, key, value)</code>:</b> Python calls this when you write "
                    "<code>d[key] = value</code>.<br>"
                    "<b><code>key.lower()</code>:</b> normalize the key so case does not create different slots.<br>"
                    "<b><code>super().__setitem__(...)</code>:</b> call the parent’s store logic "
                    "(puts the pair into <code>self.data</code>) — do not reinvent storage.<br><br>"
                    "<b>Same idea:</b> <code>UserList</code> (wraps a list in <code>.data</code>), "
                    "<code>UserString</code> (wraps a string). Override methods there the same way."
                    "</p>"
                    "<div class=\"callout\"><b>Tip:</b> for a full case-insensitive dict, also override "
                    "<code>__getitem__</code> / <code>__contains__</code> to <code>.lower()</code> the key on read "
                    "(otherwise <code>d[\"Name\"]</code> after storing <code>\"name\"</code> may miss). "
                    "The example above focuses on write-side normalization.</div>"
                ),
            },
        ],
        "interview_qa": [
            {"q": "When use defaultdict vs normal dict?", "a": "When you would write <code>if key not in d: d[key] = []</code> every time — defaultdict creates the default for you."},
            {"q": "namedtuple vs dataclass?", "a": "namedtuple is immutable and lighter. dataclass is better when you need mutability, defaults, or methods."},
            {"q": "When use deque over list?", "a": "When you need fast <code>appendleft</code>/<code>popleft</code> — queues, BFS, sliding windows. List pop(0) is O(n)."},
            {"q": "What is ChainMap for?", "a": "Layered lookup: <code>ChainMap(Dict1, Dict2)</code> checks Dict1 first, then Dict2. First match wins — no copy/merge."},
            {"q": "Why UserDict instead of subclassing dict?", "a": "Built-in <code>dict</code> methods are in C and may skip your Python overrides. <code>UserDict</code> stores items in <code>.data</code> and calls your <code>__setitem__</code> / <code>__getitem__</code> reliably — safer when customizing behavior (e.g. case-insensitive keys)."},
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
                "title": "Step 1 — CPU core (hardware)",
                "body": (
                    "Before threads: what runs code on your machine. "
                    + csharp_compare_btn("threading-gil")
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Physical core</b> = one CPU unit on the chip that runs instructions.<br>"
                    "<b>Logical CPU</b> = what Task Manager shows (may be 2× cores with hyperthreading).<br>"
                    "<b>OS scheduler</b> = moves <b>threads</b> onto cores — switches very fast."
                    "</p>"
                    '<div class="step-pre">'
                    "Example chip:\n"
                    "  [Core1] [Core2] [Core3] [Core4]   ← physical cores\n"
                    "  OS may show 8 logical CPUs\n"
                    "\n"
                    "Cores run work.\n"
                    "The OS assigns threads to cores."
                    "</div>"
                ),
            },
            {
                "title": "Step 2 — Process vs thread",
                "body": (
                    "<b>Process</b> = one running program (own memory). "
                    "<b>Thread</b> = one execution path inside that program (shared memory)."
                    "<table class=\"data-tbl\">"
                    "<tr><th></th><th>Process</th><th>Thread</th></tr>"
                    "<tr><td><b>Memory</b></td><td>Separate</td><td>Shared in same process</td></tr>"
                    "<tr><td><b>Start cost</b></td><td>Higher</td><td>Lower</td></tr>"
                    "<tr><td><b>Example</b></td><td><code>python api.py</code></td>"
                    "<td><code>threading.Thread(...)</code></td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>3 Python apps open:</b>"
                    "</p>"
                    '<div class="step-pre">'
                    "python api.py      → 1 process, 1 main thread (to start)\n"
                    "python worker.py   → 1 process, 1 main thread\n"
                    "python notebook    → 1 process, 1 main thread\n"
                    "\n"
                    "Minimum total: 3 processes, 3 threads"
                    "</div>"
                    '<div class="callout" style="margin-top:8px">'
                    "<b>Quick picture (metaphor only)</b> — not literal, just to remember:<br>"
                    "• <b>Process</b> = one whole app (separate building)<br>"
                    "• <b>Thread</b> = one worker inside that app (same building, shared desk)<br>"
                    "• <b>3 apps</b> = 3 buildings, each starts with one worker"
                    "</div>"
                ),
            },
            {
                "title": "Step 3 — CPython and the GIL",
                "body": (
                    "<b>GIL</b> (Global Interpreter Lock) = in CPython, only "
                    "<b>one thread</b> runs <b>Python bytecode</b> at a time "
                    "<b>per process</b>."
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "Not one thread for the whole PC — <b>one per Python process</b>. "
                    "During <b>I/O wait</b> (network, disk), the GIL is often released "
                    "so another thread can run."
                    "</p>"
                    '<div class="step-pre">'
                    "One Python process:\n"
                    "  Thread1, Thread2, Thread3, Thread4\n"
                    "              ↓\n"
                    "         [ GIL ]  ← one runs Python bytecode at a time\n"
                    "\n"
                    "Three separate Python apps = three processes = three GILs"
                    "</div>"
                    '<div class="callout" style="margin-top:8px">'
                    "<b>Quick picture (metaphor only)</b><br>"
                    "• One Python app = one <b>interpreter</b><br>"
                    "• GIL = only one thread may execute Python instructions at a time in that interpreter<br>"
                    "• Three apps = three interpreters — they can use different cores at the same time"
                    "</div>"
                ),
            },
            {
                "title": "Step 4 — GIL impact: OK vs not OK",
                "body": (
                    "<b>Purpose of “GIL impact”:</b> decide if "
                    "<b>threads in one process</b> help — or you need "
                    "<b>separate processes</b>. "
                    + csharp_compare_btn("threading-gil")
                    + '<div class="mc-row">'
                    '<div class="mc-col mc-good"><span class="mc-lbl">I/O-bound — OK for threads</span>'
                    '<div class="step-pre">'
                    "Examples: download, wait DB, read file\n"
                    "\n"
                    "While thread waits on network/disk:\n"
                    "  → it releases the GIL\n"
                    "  → another thread can run\n"
                    "\n"
                    "Result: waits overlap → faster overall\n"
                    "Use: ThreadPoolExecutor / threading"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>OK</b> = threads help even with the GIL, because most time is "
                    "<b>waiting</b>, not running Python bytecode."
                    "</p>"
                    "</div>"
                    '<div class="mc-col mc-bad"><span class="mc-lbl">CPU-bound — not OK for threads</span>'
                    '<div class="step-pre">'
                    "Examples: heavy math, image resize in Python\n"
                    "\n"
                    "Threads fight for the same GIL:\n"
                    "  → only one runs Python at a time\n"
                    "  → little/no speedup on multi-core\n"
                    "\n"
                    "Fix: separate processes (each has own GIL)\n"
                    "Use: ProcessPoolExecutor / multiprocessing"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>not OK</b> = threads do not give true parallel Python CPU. "
                    "Use <b>processes</b> to bypass the GIL."
                    "</p>"
                    "</div>"
                    "</div>"
                    '<table class="data-tbl">'
                    "<tr><th></th><th>I/O-bound (OK)</th><th>CPU-bound (not OK)</th></tr>"
                    "<tr><td><b>What the work does</b></td>"
                    "<td>Waits on network / disk / DB</td>"
                    "<td>Crunches numbers in Python</td></tr>"
                    "<tr><td><b>GIL while waiting / working</b></td>"
                    "<td>Released during wait</td>"
                    "<td>Held during Python math</td></tr>"
                    "<tr><td><b>Threads help?</b></td>"
                    "<td class=\"cell-yes\">Yes</td>"
                    "<td class=\"cell-no\">No (for speed)</td></tr>"
                    "<tr><td><b>Use</b></td>"
                    "<td><code>ThreadPoolExecutor</code></td>"
                    "<td><code>ProcessPoolExecutor</code></td></tr>"
                    "</table>"
                    "<p class=\"step-result\">"
                    "<b>One line:</b> waiting → threads OK · heavy Python CPU → processes."
                    "</p>"
                ),
            },
            {
                "title": "Step 5 — “Threads fight for the GIL” — what actually happens",
                "body": (
                    "<b>No exception is raised.</b> Threads competing for the GIL just "
                    "<b>take turns</b> — the cost is <b>time</b>, not an error. "
                    "CPython drops the GIL about every <b>5 ms</b> "
                    "(<code>sys.getswitchinterval()</code>), so CPU-bound threads "
                    "interleave instead of running in parallel."
                    '<div class="step-pre">'
                    "4 CPU-bound threads, one process:\n"
                    "  T1 ▓▓▓░░░░░░░░░\n"
                    "  T2 ░░░▓▓▓░░░░░░   ← only one holds the GIL\n"
                    "  T3 ░░░░░░▓▓▓░░░\n"
                    "  T4 ░░░░░░░░░▓▓▓\n"
                    "\n"
                    "Work is serialized + switching overhead\n"
                    "→ can be SLOWER than one thread. No error."
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>The real dangers are silent</b> — they do not look like the "
                    "GIL at all:"
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th>Problem</th><th>What you actually see</th></tr>"
                    "<tr><td><b>GIL contention</b></td>"
                    "<td class=\"cell-yes\">No exception — just slow</td></tr>"
                    "<tr><td><b>Race on shared data</b></td>"
                    "<td class=\"cell-no\">No exception — a wrong number</td></tr>"
                    "<tr><td><b>Deadlock</b> (two locks, opposite order)</td>"
                    "<td class=\"cell-no\">No exception — hangs forever</td></tr>"
                    "<tr><td>Re-acquiring a plain <code>Lock</code> in one thread</td>"
                    "<td class=\"cell-no\">Hangs — use <code>RLock</code></td></tr>"
                    "<tr><td>Starting the same thread twice</td>"
                    "<td><code>RuntimeError</code>: threads can only be started once</td></tr>"
                    "<tr><td><code>t.join()</code> on the current thread</td>"
                    "<td><code>RuntimeError</code>: cannot join current thread</td></tr>"
                    "</table>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad"><span class="mc-lbl">'
                    "&#10060; Race — wrong result, no error</span>"
                    '<div class="step-pre">'
                    "from concurrent.futures import ThreadPoolExecutor\n"
                    "\n"
                    "counter = 0\n"
                    "\n"
                    "def add_one(x):\n"
                    "    return x + 1\n"
                    "\n"
                    "def bump():\n"
                    "    global counter\n"
                    "    for _ in range(200_000):\n"
                    "        counter = add_one(counter)  # read→call→write\n"
                    "\n"
                    "with ThreadPoolExecutor(max_workers=4) as pool:\n"
                    "    for _ in range(4):\n"
                    "        pool.submit(bump)\n"
                    "\n"
                    "print(counter)\n"
                    "# 754453 ... 706011 ... 639330  (expected 800000)\n"
                    "# different every run, nothing was raised"
                    "</div></div>"
                    '<div class="mc-col mc-good"><span class="mc-lbl">'
                    "&#10004; Fix — a Lock, not a different pool</span>"
                    '<div class="step-pre">'
                    "from concurrent.futures import ThreadPoolExecutor\n"
                    "import threading\n"
                    "\n"
                    "counter = 0\n"
                    "lock = threading.Lock()\n"
                    "\n"
                    "def add_one(x):\n"
                    "    return x + 1\n"
                    "\n"
                    "def bump():\n"
                    "    global counter\n"
                    "    for _ in range(200_000):\n"
                    "        with lock:                  # whole update\n"
                    "            counter = add_one(counter)\n"
                    "\n"
                    "with ThreadPoolExecutor(max_workers=4) as pool:\n"
                    "    for _ in range(4):\n"
                    "        pool.submit(bump)\n"
                    "\n"
                    "print(counter)   # always exactly 800000"
                    "</div></div>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Why <code>add_one()</code> and not plain <code>counter += 1</code>?</b> "
                    "On CPython 3.12 the bare <code>+=</code> loop usually prints the "
                    "<b>right</b> answer, because the GIL tends to switch at loop "
                    "boundaries rather than mid-increment. The bug is still there — it "
                    "just <b>hides</b>. Any call inside the read-modify-write window "
                    "exposes it. <b>That is the scary part:</b> a race can pass every "
                    "test on your machine and fail in production."
                    "</p>"
                    '<div class="callout" style="margin-top:8px">'
                    "<b>Exceptions inside a thread do not reach <code>main</code>.</b><br>"
                    "A raised error kills only <b>that</b> thread — Python prints it via "
                    "<code>threading.excepthook</code> and <code>t.join()</code> still "
                    "returns normally.<br>"
                    "Pools are safer: the error is stored in the <code>Future</code> and "
                    "<b>re-raised when you read the result</b>."
                    "</div>"
                    '<div class="step-pre">'
                    "with ThreadPoolExecutor() as pool:\n"
                    "    fut = pool.submit(risky)\n"
                    "    fut.result()       # ← exception re-raised HERE\n"
                    "\n"
                    "# submit and never read result → swallowed silently\n"
                    "# list(pool.map(...)) surfaces it while iterating"
                    "</div>"
                    "<p class=\"step-result\">"
                    "<b>One line:</b> GIL contention costs speed, never an exception — "
                    "races, deadlocks and swallowed thread errors are the real bugs."
                    "</p>"
                ),
            },
            {
                "title": "Step 6 — Full code: ThreadPool + ProcessPool",
                "body": (
                    "Image resize service — full runnable pattern. "
                    "Download = I/O (threads). Resize = CPU (processes). "
                    + csharp_compare_btn("threading-gil")
                    + "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>1) ThreadPoolExecutor — full download code</b> "
                    "(GIL OK — network wait releases GIL):"
                    "</p>"
                    '<div class="step-pre">'
                    "from concurrent.futures import ThreadPoolExecutor\n"
                    "import urllib.request\n"
                    "\n"
                    "def download(url):\n"
                    "    with urllib.request.urlopen(url, timeout=10) as r:\n"
                    "        return r.read()          # wait on network\n"
                    "\n"
                    "urls = [\n"
                    "    \"http://a/img1.jpg\",\n"
                    "    \"http://b/img2.jpg\",\n"
                    "]\n"
                    "\n"
                    "with ThreadPoolExecutor(max_workers=4) as pool:\n"
                    "    images = list(pool.map(download, urls))\n"
                    "\n"
                    "# OUTPUT\n"
                    "# images → [bytes1, bytes2]  (downloaded concurrently)"
                    "</div>"
                    "<p style=\"font-size:12px;margin:8px 0;line-height:1.45\">"
                    "<b>2) ProcessPoolExecutor — full resize code</b> "
                    "(CPU — each worker process has its own GIL):"
                    "</p>"
                    '<div class="step-pre">'
                    "from concurrent.futures import (ProcessPoolExecutor,\n"
                    "                                ThreadPoolExecutor)\n"
                    "from PIL import Image\n"
                    "import io\n"
                    "\n"
                    "def heavy_resize(data):        # data = one item from images\n"
                    "    img = Image.open(io.BytesIO(data))\n"
                    "    img = img.resize((200, 200))   # CPU pixel work\n"
                    "    out = io.BytesIO()\n"
                    "    img.save(out, format=\"JPEG\")\n"
                    "    return out.getvalue()\n"
                    "\n"
                    "if __name__ == \"__main__\":\n"
                    "    # 1) I/O first — threads. images = [bytes1, bytes2]\n"
                    "    with ThreadPoolExecutor(max_workers=4) as pool:\n"
                    "        images = list(pool.map(download, urls))\n"
                    "\n"
                    "    # 2) then CPU — processes. Feed those bytes in.\n"
                    "    with ProcessPoolExecutor(max_workers=4) as pool:\n"
                    "        out = list(pool.map(heavy_resize, images))\n"
                    "\n"
                    "    # OUTPUT\n"
                    "    # out → [resized1, resized2]  (CPU on multiple cores)"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>What is in <code>images</code>?</b> The list produced by block 1 — "
                    "the <b>raw downloaded JPEG bytes</b>, one <code>bytes</code> object "
                    "per URL. <code>pool.map</code> hands one item to each call, so "
                    "<code>heavy_resize(data)</code> receives one image's bytes."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Why <code>if __name__ == \"__main__\"</code>?</b> "
                    "On Windows, child processes re-import the module — "
                    "the guard stops infinite spawn. Note the download now lives "
                    "<b>inside</b> the guard too: at module level, all 4 children would "
                    "re-run the downloads on import."
                    "</p>"
                    "<p style=\"font-size:12px;margin:10px 0 4px;line-height:1.45\">"
                    "<b>Side by side — same pool, one line moved.</b> "
                    "A child process starts by <b>importing your file</b>, so every "
                    "top-level statement runs again inside that child."
                    "</p>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad">'
                    '<span class="mc-lbl">&#10060; No guard &mdash; pool at module level</span>'
                    '<div class="step-pre">'
                    "# job.py\n"
                    "from concurrent.futures import ProcessPoolExecutor\n"
                    "\n"
                    "def work(n):\n"
                    "    return n * n\n"
                    "\n"
                    "print(\"loading job.py\")      # side effect\n"
                    "with ProcessPoolExecutor(4) as pool:\n"
                    "    print(list(pool.map(work, [1, 2, 3, 4])))\n"
                    "\n"
                    "# OUTPUT (Windows / macOS)\n"
                    "# loading job.py        ← you\n"
                    "# loading job.py        ← child re-import!\n"
                    "# RuntimeError: An attempt has been made to\n"
                    "#   start a new process before the current\n"
                    "#   process has finished its bootstrapping\n"
                    "#   phase     ← raised inside the child\n"
                    "# BrokenProcessPool: A process in the process\n"
                    "#   pool was terminated abruptly\n"
                    "#             ← how your script finally dies"
                    "</div></div>"
                    '<div class="mc-col mc-good">'
                    '<span class="mc-lbl">&#10004; Guarded &mdash; pool inside <code>__main__</code></span>'
                    '<div class="step-pre">'
                    "# job.py\n"
                    "from concurrent.futures import ProcessPoolExecutor\n"
                    "\n"
                    "def work(n):\n"
                    "    return n * n\n"
                    "\n"
                    "if __name__ == \"__main__\":\n"
                    "    print(\"loading job.py\")  # runs once\n"
                    "    with ProcessPoolExecutor(4) as pool:\n"
                    "        print(list(pool.map(work, [1, 2, 3, 4])))\n"
                    "\n"
                    "# OUTPUT\n"
                    "# loading job.py\n"
                    "# [1, 4, 9, 16]\n"
                    "#   ← each worker re-imports job.py to get\n"
                    "#     work(), skips the guard, then runs work()"
                    "</div></div></div>"
                    '<div class="callout" style="margin-top:8px">'
                    "<b>What <code>__name__</code> actually holds.</b> "
                    "In the process <b>you</b> launched (<code>python job.py</code>) it is "
                    "<code>\"__main__\"</code>, so the guarded block runs. In each child "
                    "process the same file is imported under the name "
                    "<code>\"__mp_main__\"</code> — so <code>__name__ == \"__main__\"</code> is "
                    "<code>False</code>, the guarded block is skipped, and only "
                    "<code>import</code>/<code>def</code>/<code>class</code> lines execute."
                    "</div>"
                    "<p style=\"font-size:12px;margin:10px 0 4px;line-height:1.45\">"
                    "<b>“Children import defs only, then run <code>work()</code>” — the life "
                    "of one worker.</b> A worker is a <b>brand-new, empty</b> "
                    "<code>python.exe</code>: it has none of your functions, so it has to load "
                    "your file before it can run anything."
                    "</p>"
                    '<ul class="learn-steps" style="margin:4px 0 8px">'
                    "<li><b>1. Parent sends a name, not code.</b> "
                    "<code>pool.map(work, [1, 2, 3, 4])</code> pickles the "
                    "<b>reference</b> <code>__mp_main__.work</code> plus each argument. "
                    "The body of <code>work</code> is never shipped.</li>"
                    "<li><b>2. Windows starts a fresh interpreter</b> per worker "
                    "(<code>spawn</code>) — empty memory, no <code>work</code> yet.</li>"
                    "<li><b>3. The worker imports your file — “defs only”.</b> It runs "
                    "<code>job.py</code> top to bottom under the name "
                    "<code>__mp_main__</code>. The <code>import</code> lines and "
                    "<code>def work</code> execute, so <code>work</code> now exists. "
                    "The <code>if __name__ == \"__main__\"</code> block is <b>skipped</b>, so "
                    "the prints, the downloads and the pool itself do not re-run.</li>"
                    "<li><b>4. Then it runs <code>work()</code>.</b> The worker resolves the "
                    "pickled name in the module it just imported, calls "
                    "<code>work(1)</code>, and pickles the return value back to the parent.</li>"
                    "</ul>"
                    "<p style=\"font-size:12px;margin:10px 0 4px;line-height:1.45\">"
                    "<b>See it yourself — real console output, without vs with the guard.</b> "
                    "One <code>print</code> at module level (fires on every import) and one "
                    "inside <code>work</code> (fires only when a task runs). Same 2-worker "
                    "pool in both columns:"
                    "</p>"
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad">'
                    '<span class="mc-lbl">&#10060; No guard &mdash; nothing gets done</span>'
                    '<div class="step-pre">'
                    "import os\n"
                    "from concurrent.futures import ProcessPoolExecutor\n"
                    "\n"
                    "print(f\"[import] __name__={__name__!r} \"\n"
                    "      f\"pid={os.getpid()}\")\n"
                    "\n"
                    "def work(n):\n"
                    "    return f\"[task] n={n} pid={os.getpid()}\"\n"
                    "\n"
                    "with ProcessPoolExecutor(2) as pool:      # module level\n"
                    "    for line in pool.map(work, [1, 2]):\n"
                    "        print(line)\n"
                    "\n"
                    "# OUTPUT (Windows)\n"
                    "# [import] __name__='__main__'    pid=29760  ← you\n"
                    "# [import] __name__='__mp_main__' pid=68316  ← worker 1\n"
                    "# RuntimeError: An attempt has been made to start\n"
                    "#   a new process before the current process has\n"
                    "#   finished its bootstrapping phase\n"
                    "#            ← worker 1 re-ran the pool and died\n"
                    "# [import] __name__='__mp_main__' pid=32564  ← worker 2\n"
                    "# RuntimeError: ...same crash in worker 2\n"
                    "# BrokenProcessPool: A process in the process pool\n"
                    "#   was terminated abruptly while the future was\n"
                    "#   running or pending\n"
                    "#            ← what YOUR script finally dies with\n"
                    "#\n"
                    "# NOT ONE [task] line → zero work done"
                    "</div></div>"
                    '<div class="mc-col mc-good">'
                    '<span class="mc-lbl">&#10004; Guarded &mdash; both items processed</span>'
                    '<div class="step-pre">'
                    "import os\n"
                    "from concurrent.futures import ProcessPoolExecutor\n"
                    "\n"
                    "print(f\"[import] __name__={__name__!r} \"\n"
                    "      f\"pid={os.getpid()}\")\n"
                    "\n"
                    "def work(n):\n"
                    "    return f\"[task] n={n} pid={os.getpid()}\"\n"
                    "\n"
                    "if __name__ == \"__main__\":               # guarded\n"
                    "    with ProcessPoolExecutor(2) as pool:\n"
                    "        for line in pool.map(work, [1, 2]):\n"
                    "            print(line)\n"
                    "\n"
                    "# OUTPUT (Windows)\n"
                    "# [import] __name__='__main__'    pid=748    ← you\n"
                    "# [import] __name__='__mp_main__' pid=47364  ← worker 1\n"
                    "# [import] __name__='__mp_main__' pid=31248  ← worker 2\n"
                    "#            ← each worker imported defs only\n"
                    "# [task] n=1 pid=47364\n"
                    "# [task] n=2 pid=47364\n"
                    "#            ← work() ran in a worker process\n"
                    "#\n"
                    "# no error, exit code 0"
                    "</div></div></div>"
                    '<div class="callout" style="margin-top:4px">'
                    "<b>The surprise in that output:</b> <code>[import]</code> prints "
                    "<b>3 times in both columns</b>. The guard does <b>not</b> stop the "
                    "re-import — the worker always re-imports your file. What the guard stops "
                    "is the <b>re-run of your program body</b>. Without it, the child re-runs "
                    "<code>ProcessPoolExecutor(...)</code> itself, tries to spawn "
                    "grandchildren mid-import, and is killed; the parent then reports "
                    "<code>BrokenProcessPool</code>."
                    "</div>"
                    '<table class="data-tbl">'
                    "<tr><th>In the output above</th><th>&#10060; No guard</th>"
                    "<th>&#10004; Guarded</th></tr>"
                    "<tr><td><code>[import]</code> lines (the re-import)</td>"
                    "<td>3 — you + 2 workers</td><td>3 — you + 2 workers "
                    "(<b>same</b>)</td></tr>"
                    "<tr><td>Pool created inside the child?</td>"
                    "<td>yes → <code>RuntimeError</code></td><td>no — guard skips it</td></tr>"
                    "<tr><td><code>[task]</code> lines (actual work)</td>"
                    "<td><b>0</b></td><td><b>2</b>, on worker pids</td></tr>"
                    "<tr><td>How the script ends</td>"
                    "<td><code>BrokenProcessPool</code>, exit code 1</td>"
                    "<td>clean, exit code 0</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "Note the pids in the guarded run: every <code>[task]</code> line shows a "
                    "<b>worker</b> pid, never yours — the real work happens in the children. "
                    "Both items landed on worker 1 here simply because it was free again "
                    "before the second item was handed out."
                    "</p>"
                    '<div class="callout" style="margin-top:4px">'
                    "<b>Consequence of “a name, not code”.</b> The worker must be able to find "
                    "<code>work</code> after importing your file, so the target must be a "
                    "<b>top-level</b> <code>def</code>. A <code>lambda</code>, a function "
                    "nested inside another function, or an instance method of an unpicklable "
                    "object fails with <code>PicklingError: Can't pickle "
                    "&lt;function &lt;lambda&gt;&gt;: attribute lookup &lt;lambda&gt; on "
                    "__main__ failed</code> — pickle looked for the name and there was "
                    "nothing to find."
                    "</div>"
                    '<table class="data-tbl">'
                    "<tr><th>Behaviour</th><th>&#10060; Without guard</th>"
                    "<th>&#10004; With guard</th></tr>"
                    "<tr><td><b>What each child re-runs on import</b></td>"
                    "<td>every top-level line — prints, downloads, and the "
                    "<code>ProcessPoolExecutor</code> itself</td>"
                    "<td>only <code>import</code> and <code>def</code>/<code>class</code></td></tr>"
                    "<tr><td><b>Starting the pool</b></td>"
                    "<td><code>RuntimeError</code> in each child, then "
                    "<code>BrokenProcessPool</code> in the parent (runaway spawn in a frozen "
                    "<code>.exe</code>)</td><td>starts cleanly</td></tr>"
                    "<tr><td><b>Side effects</b> (downloads, DB writes, logs)</td>"
                    "<td>repeated once per child — 4 workers = 4 extra downloads</td>"
                    "<td>run once, in the parent</td></tr>"
                    "<tr><td><b>Windows / macOS</b> (<code>spawn</code> start method)</td>"
                    "<td>broken</td><td>works</td></tr>"
                    "<tr><td><b>Linux</b> (<code>fork</code> start method)</td>"
                    "<td>often appears to work — hides the bug until you ship to Windows</td>"
                    "<td>works, and stays portable</td></tr>"
                    "<tr><td><b><code>import job</code> from a test or another module</b></td>"
                    "<td>the pool spins up during the import</td>"
                    "<td>nothing runs — you import, then call what you need</td></tr>"
                    "<tr><td><b>Threads only</b> (no <code>ProcessPool</code>)</td>"
                    "<td>guard not required — threads share the process, no re-import</td>"
                    "<td>harmless, and still the habit to keep</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Benefit in one sentence:</b> the guard separates "
                    "<b>“this file is being imported”</b> from <b>“this program is "
                    "starting”</b> — child processes get your functions without re-running "
                    "your program. C# gets this for free: <code>static void Main()</code> is "
                    "the entry point, and a new process never re-imports your assembly."
                    "</p>"
                    '<div class="callout" style="margin-top:4px">'
                    "<b>Not only for pools.</b> The guard asks one question — <i>“am I the "
                    "program being run, or am I being imported?”</i> — and pools are just the "
                    "case where getting it wrong <b>crashes</b>. The three you will use daily:"
                    "<br>1. <b>One file, two roles</b> — importable module <i>and</i> runnable "
                    "script, so <code>import job</code> does not execute your program."
                    "<br>2. <b>Entry point</b> — <code>main()</code>, argparse and "
                    "<code>sys.argv</code> live in the guard, not at module level."
                    "<br>3. <b>Test-friendly imports</b> — <code>pytest</code> imports your "
                    "module to collect tests; without the guard, collection runs your program."
                    "<br><span style=\"font-size:11px\">Full list — including "
                    "<code>python -m</code>, uvicorn workers and frozen "
                    "<code>.exe</code> files — in <b>“Purposes of "
                    "<code>if __name__ == \"__main__\"</code>”</b> further down this slide."
                    "</span>"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Why bytes and not an <code>Image</code> object?</b> Arguments are "
                    "<b>pickled</b> and copied to the child process. Plain "
                    "<code>bytes</code> pickle cleanly; open file handles and many "
                    "library objects do not."
                    "</p>"
                    '<table class="data-tbl">'
                    "<tr><th></th><th>ThreadPool</th><th>ProcessPool</th></tr>"
                    "<tr><td><b>Job</b></td><td><code>download</code></td>"
                    "<td><code>heavy_resize</code></td></tr>"
                    "<tr><td><b>Bound</b></td><td>I/O</td><td>CPU</td></tr>"
                    "<tr><td><b>GIL</b></td><td>OK (released while waiting)</td>"
                    "<td>Bypassed (own GIL per process)</td></tr>"
                    "<tr><td><b>Workers</b></td><td>Threads in one process</td>"
                    "<td>Child processes</td></tr>"
                    "</table>"
                ),
            },
            {
                "title": "Step 7 — Count processes/threads + Lock",
                "body": (
                    "<b>How many if you add pools?</b>"
                    '<div class="callout">'
                    "<b>Two rules do all the counting.</b>"
                    "<br><b>1.</b> Every command you launch — <code>python api.py</code> — is "
                    "<b>one process</b>, and a process always starts with <b>exactly one "
                    "thread</b>, its <code>MainThread</code>. So <b>3 apps = 3 processes = 3 "
                    "threads</b>. That is where the “3” comes from: you counted the commands, "
                    "not anything Python did."
                    "<br><b>2.</b> A <b>ThreadPool adds threads inside</b> the process it was "
                    "created in (process count unchanged). A <b>ProcessPool adds whole new "
                    "processes</b>, and each of those brings its own <code>MainThread</code> "
                    "and its own GIL."
                    "</div>"
                    "<p style=\"font-size:12px;margin:8px 0 4px;line-height:1.45\">"
                    "<b>Count it step by step.</b> Say you launched "
                    "<code>python api.py</code> (App1), <code>python worker.py</code> (App2) "
                    "and <code>python notebook.py</code> (App3). Running totals for the whole "
                    "machine:"
                    "</p>"
                    "<table class=\"data-tbl\">"
                    "<tr><th>Step</th><th>App1</th><th>App2</th><th>App3</th>"
                    "<th>Total processes</th><th>Total threads</th></tr>"
                    "<tr><td><b>a.</b> 3 apps, no pools</td>"
                    "<td>1 proc · 1 thread</td><td>1 proc · 1 thread</td>"
                    "<td>1 proc · 1 thread</td><td><b>3</b></td><td><b>3</b></td></tr>"
                    "<tr><td><b>b.</b> App1 adds <code>ThreadPoolExecutor(4)</code>, 4 tasks "
                    "running</td>"
                    "<td>1 proc · <b>5</b> threads<br>(1 main + 4 workers)</td>"
                    "<td>1 proc · 1 thread</td><td>1 proc · 1 thread</td>"
                    "<td>still <b>3</b><br>(threads are not processes)</td>"
                    "<td><b>7</b> = 5 + 1 + 1</td></tr>"
                    "<tr><td><b>c.</b> App2 also adds "
                    "<code>ProcessPoolExecutor(4)</code>, 4 tasks running</td>"
                    "<td>1 proc · 5 threads</td>"
                    "<td><b>5</b> procs · <b>7</b> threads<br>parent: 3 · each child: 1</td>"
                    "<td>1 proc · 1 thread</td>"
                    "<td><b>7</b> = 1 + 5 + 1</td>"
                    "<td><b>13</b> = 5 + 7 + 1</td></tr>"
                    "</table>"
                    "<p style=\"font-size:12px;margin:8px 0 4px;line-height:1.45\">"
                    "<b>Measured on Windows / Python 3.12</b> — one app, printing "
                    "<code>threading.enumerate()</code> at each stage:"
                    "</p>"
                    '<div class="step-pre">'
                    "1. at start                    pid=48900 threads=1\n"
                    "   ['MainThread']\n"
                    "\n"
                    "2. inside ThreadPool(4)        pid=48900 threads=5\n"
                    "   ['MainThread', 'ThreadPoolExecutor-0_0',\n"
                    "    'ThreadPoolExecutor-0_1', 'ThreadPoolExecutor-0_2',\n"
                    "    'ThreadPoolExecutor-0_3']      ← 1 main + 4 workers\n"
                    "\n"
                    "3. after ThreadPool closed     pid=48900 threads=1\n"
                    "   ['MainThread']                 ← workers are gone\n"
                    "\n"
                    "4. inside ProcessPool(4)       pid=48900 threads=3\n"
                    "   ['MainThread', 'QueueFeederThread', 'Thread-1']\n"
                    "   child processes: 4 [31428, 42412, 16184, 64140]\n"
                    "   each child: threads=1 ['MainThread']"
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Where App2’s 7 threads come from.</b> The 4 children are separate "
                    "<code>python.exe</code> processes, each doing your work on its single "
                    "<code>MainThread</code> — that is 4. The parent has 3: its "
                    "<code>MainThread</code> plus two helpers Python created for you — "
                    "<code>QueueFeederThread</code> pickles arguments and writes them into the "
                    "pipe, and the executor’s manager thread reads results back and completes "
                    "your <code>Future</code> objects. 4 + 3 = 7."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Why the old table said “≈ 5”.</b> <code>max_workers=4</code> is a "
                    "<b>ceiling</b>, not a reservation — <code>ThreadPoolExecutor</code> "
                    "creates one thread per submitted task until it hits the ceiling. Submit "
                    "only 2 tasks and you measure <b>3</b> threads "
                    "(<code>['MainThread', 'ThreadPoolExecutor-0_0', "
                    "'ThreadPoolExecutor-0_1']</code>). Leave the <code>with</code> block and "
                    "you are back to 1. Libraries can also add their own threads, so treat 5 "
                    "as “main + up to 4”."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Sanity check in Task Manager:</b> step <b>c</b> shows "
                    "<b>7</b> <code>python.exe</code> entries — App1, App3, App2’s parent and "
                    "App2’s 4 children. Threads never appear there as separate entries; they "
                    "are inside one entry, which is exactly the difference between the two "
                    "columns."
                    "</p>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Lock</b> — when threads share one variable, use "
                    "<code>threading.Lock</code> so two threads don’t update it at the same time:"
                    "</p>"
                    '<div class="step-pre">'
                    "import threading\n"
                    "lock = threading.Lock()\n"
                    "\n"
                    "with lock:\n"
                    "    shared_counter += 1"
                    "</div>"
                    "<p class=\"step-result\">"
                    "<b>Remember:</b> separate apps → separate processes · "
                    "ThreadPool → more threads · ProcessPool → more <b>processes</b>."
                    "</p>"
                ),
            },
            {
                "title": "Step 8 — threading.Thread vs ThreadPoolExecutor",
                "body": (
                    "Both run <b>threads</b> in <b>one process</b>, so the GIL rules from "
                    "Step 3 are identical — good for I/O, no help for CPU. The difference is "
                    "<b>who does the bookkeeping</b>: with <code>threading.Thread</code> you "
                    "create, start, join and collect results yourself; "
                    "<code>ThreadPoolExecutor</code> is a managed pool that hands you "
                    "<b>return values</b>."
                    '<div class="mc-row">'
                    '<div class="mc-col mc-bad">'
                    '<span class="mc-lbl">threading.Thread &mdash; manual, no return value</span>'
                    '<div class="step-pre">'
                    "import threading\n"
                    "\n"
                    "results = []                  # shared state\n"
                    "\n"
                    "def fetch(url):\n"
                    "    results.append(download(url))   # can't return\n"
                    "\n"
                    "threads = [threading.Thread(target=fetch, args=(u,))\n"
                    "           for u in urls]     # 1 thread per URL\n"
                    "for t in threads:\n"
                    "    t.start()\n"
                    "for t in threads:\n"
                    "    t.join()                  # forget this → results\n"
                    "                              # is still incomplete\n"
                    "print(results)                # completion order,\n"
                    "                              # not URL order\n"
                    "# an error inside fetch: that thread dies, the\n"
                    "# traceback is printed, join() still looks fine"
                    "</div></div>"
                    '<div class="mc-col mc-good">'
                    '<span class="mc-lbl">ThreadPoolExecutor &mdash; managed, returns values</span>'
                    '<div class="step-pre">'
                    "from concurrent.futures import ThreadPoolExecutor\n"
                    "\n"
                    "def fetch(url):\n"
                    "    return download(url)      # just return\n"
                    "\n"
                    "with ThreadPoolExecutor(max_workers=4) as pool:\n"
                    "    results = list(pool.map(fetch, urls))\n"
                    "    # 4 threads reused for 100 URLs\n"
                    "# leaving the with block joins everything\n"
                    "\n"
                    "print(results)                # same order as urls\n"
                    "\n"
                    "# an error inside fetch is stored in the Future\n"
                    "# and re-raised where you read the result"
                    "</div></div></div>"
                    '<table class="data-tbl">'
                    "<tr><th></th><th><code>threading.Thread</code></th>"
                    "<th><code>ThreadPoolExecutor</code></th></tr>"
                    "<tr><td><b>Threads created</b></td>"
                    "<td>one per task — 100 tasks = <b>100 threads</b>, each with its own "
                    "stack</td>"
                    "<td><code>max_workers</code> at most, <b>reused</b> for every task</td></tr>"
                    "<tr><td><b>Getting a result</b></td>"
                    "<td>no return value — append to a shared <code>list</code> or "
                    "<code>queue.Queue</code></td>"
                    "<td><code>return</code> it: <code>future.result()</code> or "
                    "<code>pool.map(...)</code></td></tr>"
                    "<tr><td><b>Result order</b></td><td>whatever finishes first</td>"
                    "<td><code>map</code> keeps <b>input order</b>; "
                    "<code>as_completed</code> gives finish order when you want it</td></tr>"
                    "<tr><td><b>Errors</b></td>"
                    "<td>kill that thread only — printed via "
                    "<code>threading.excepthook</code>, and <code>join()</code> still returns "
                    "normally, so bugs pass silently</td>"
                    "<td>stored in the <code>Future</code> and <b>re-raised</b> when you read "
                    "<code>.result()</code></td></tr>"
                    "<tr><td><b>Waiting</b></td>"
                    "<td>you <code>.join()</code> every thread yourself</td>"
                    "<td>the <code>with</code> block joins on exit</td></tr>"
                    "<tr><td><b>Timeout / cancel</b></td><td>nothing built in</td>"
                    "<td><code>result(timeout=5)</code>, <code>future.cancel()</code></td></tr>"
                    "<tr><td><b>Best for</b></td>"
                    "<td>one <b>long-lived</b> background thread — a listener loop, a poller, "
                    "a <code>daemon=True</code> helper that runs for the life of the app</td>"
                    "<td><b>batches of short tasks</b> that return values — downloads, API "
                    "calls, DB reads</td></tr>"
                    "</table>"
                    '<div class="callout">'
                    "<b>Rule of thumb:</b> if the work has an <b>end and a result</b>, use the "
                    "pool. If it is a <b>service that keeps running</b>, use "
                    "<code>threading.Thread(daemon=True)</code> — a pool expects tasks to "
                    "finish, and its <code>with</code> block will not exit until they do."
                    "</div>"
                    "<p style=\"font-size:12px;margin:6px 0;line-height:1.45\">"
                    "<b>Same idea in C#:</b> <code>new Thread(...).Start()</code> is the manual "
                    "version; <code>Task.Run</code> hands work to the managed "
                    "<code>ThreadPool</code>, and <code>await Task.WhenAll(tasks)</code> is the "
                    "<code>pool.map</code> equivalent that gives you the results back."
                    "</p>"
                    "<p class=\"step-result\">"
                    "<b>One line:</b> <code>Thread</code> = you run a thread · "
                    "<code>ThreadPoolExecutor</code> = you submit work and get results, "
                    "errors included."
                    "</p>"
                ),
            },
        ],
        "interview_qa": [
            {
                "q": "What is a process vs a thread?",
                "a": (
                    "<b>Process</b> = one running program with its own memory. "
                    "<b>Thread</b> = a worker inside that program; threads in the same process share memory."
                ),
            },
            {
                "q": "What is the GIL?",
                "a": (
                    "In CPython, only one thread runs Python bytecode at a time <b>per process</b>. "
                    "I/O-bound work still benefits from threads. CPU-bound Python math needs "
                    "<code>multiprocessing</code> / <code>ProcessPoolExecutor</code>."
                ),
            },
            {
                "q": "3 Python apps — how many processes?",
                "a": (
                    "At least <b>3</b> (one per app you started). "
                    "<code>ProcessPoolExecutor</code> adds <b>child processes</b> on top of that."
                ),
            },
            {
                "q": "ThreadPool vs ProcessPool?",
                "a": (
                    "<code>ThreadPoolExecutor</code> for I/O (downloads, API calls). "
                    "<code>ProcessPoolExecutor</code> for CPU-heavy Python work (resize, crunch numbers)."
                ),
            },
            {
                "q": "threading.Thread vs ThreadPoolExecutor?",
                "a": (
                    "Both are threads in one process, so the GIL applies equally. "
                    "<code>Thread</code> is manual — one thread per task, no return value, and "
                    "you <code>join()</code> them yourself; an error just kills that thread. "
                    "<code>ThreadPoolExecutor</code> reuses a fixed number of workers, returns "
                    "values through <code>Future</code>/<code>map</code>, joins on "
                    "<code>with</code> exit, and <b>re-raises</b> errors when you read the "
                    "result. Use <code>Thread</code> for a long-lived background service, the "
                    "pool for batches of short tasks."
                ),
            },
            {
                "q": "Why if __name__ == \"__main__\" for multiprocessing?",
                "a": (
                    "On Windows, child processes re-import the module. Without the guard, "
                    "top-level code runs again in each child — can cause infinite spawn loops."
                ),
            },
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
            {"title": "Step 2 — Validation", "body": "<code>Field(ge=18)</code> = built-in constraint (reject age &lt; 18). <code>@field_validator(\"email\")</code> = custom rule — Pydantic calls it <b>automatically</b> on <code>model_validate</code> / FastAPI body parse (you do not call it yourself). Here <code>return v.lower()</code> <b>normalizes</b> email. For more rules on the same field, add another <code>@field_validator(\"email\")</code> method — they run top→bottom; <code>raise ValueError</code> to reject. Invalid data → <code>ValidationError</code> → FastAPI <b>HTTP 422</b>.<div class=\"step-pre\">user = UserCreate.model_validate(body)\nprint(user.email)   # anu@co.com  (lower_email ran automatically)</div>"},
            {"title": "Step 3 — Serialization", "body": "v2: <code>model_validate(dict)</code> in, <code>model_dump()</code> out. For ORM rows use <code>model_config = {'from_attributes': True}</code>."},
            {"title": "Step 4 — FastAPI integration", "body": "Route parameters typed as Pydantic models auto-parse JSON bodies and return 422 with structured errors — no manual validation boilerplate."},
        ],
        "interview_qa": [
            {"q": "What is Pydantic used for?", "a": "Runtime validation and parsing using type hints — API schemas, config loading, data pipelines. Core of FastAPI request/response models."},
            {"q": "Pydantic vs dataclasses?", "a": "<b>Both</b> turn typed fields into a class. The big difference: <b>dataclasses store</b>; <b>Pydantic validates</b>.<table class=\"data-tbl\"><tr><th></th><th>dataclasses</th><th>Pydantic BaseModel</th></tr><tr><td><b>Job</b></td><td>Bundle fields into an object (stdlib)</td><td>Validate + coerce + export schemas</td></tr><tr><td><b>Type hints</b></td><td>Hints only — <code>age=\"25\"</code> stays a string</td><td>Enforced at runtime — <code>\"25\"</code> → int <code>25</code></td></tr><tr><td><b>Bad data</b></td><td>Usually accepted silently</td><td><code>ValidationError</code> (FastAPI → HTTP 422)</td></tr><tr><td><b>Constraints</b></td><td>You write your own checks</td><td><code>Field(ge=18)</code>, <code>@field_validator</code></td></tr><tr><td><b>API / JSON</b></td><td>Not built for request bodies</td><td>Built for FastAPI schemas</td></tr><tr><td><b>When to use</b></td><td>Internal/simple records inside your app</td><td>API boundaries, config, untrusted input</td></tr></table><div class=\"mc-row\"><div class=\"mc-col mc-bad\"><span class=\"mc-lbl\">dataclasses — no runtime check</span><div class=\"step-pre\">from dataclasses import dataclass\n\n@dataclass\nclass ItemDC:\n    name: str\n    age: int\n\nItemDC(name=\"Anu\", age=\"25\")\n# OK — no check\n# age is still str!</div></div><div class=\"mc-col mc-good\"><span class=\"mc-lbl\">Pydantic — coerce + validate</span><div class=\"step-pre\">from pydantic import BaseModel, Field\n\nclass ItemPyd(BaseModel):\n    name: str\n    age: int = Field(ge=18)\n\nItemPyd(name=\"Anu\", age=\"25\")\n# coerces to int 25\n# ItemPyd(..., age=15)\n# → ValidationError</div></div></div><b>Interview line:</b> dataclasses = structure; Pydantic = structure + validation. Prefer Pydantic at the edge of the system."},
            {"q": "What does @field_validator('email') do?", "a": "Runs custom logic on that field during validation. Common uses: normalize (<code>v.lower()</code>), strip spaces, or <code>raise ValueError</code> to reject bad values. It is not the same as <code>Field(ge=18)</code> — Field is a built-in constraint; the validator is your own rule."},
            {"q": "Why HTTP 422 on bad age?", "a": "<code>Field(ge=18)</code> fails → Pydantic raises <code>ValidationError</code> before the route body runs. FastAPI maps that to <b>422 Unprocessable Entity</b> — the JSON was parsed, but the values break the schema rules."},
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
