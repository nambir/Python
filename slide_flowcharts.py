"""Decision flowcharts under Definition on every curriculum slide.

Kid-friendly questions + explicit YES boxes (same YES→right / NO→down style).
"""

from __future__ import annotations

# (question, yes_title, yes_plain_desc, yes_code_lines, color_key)
# color_key: key | dd | cm | dict
FlowQ = tuple[str, str, str, list[str], str]


def _render(
    start: str,
    start_sub: str,
    questions: list[FlowQ],
    fallback_title: str,
    fallback_desc: str,
    fallback_lines: list[str],
) -> str:
    nodes = []
    for q, yes_title, yes_desc, codes, color in questions:
        code_html = "".join(f"<code>{c}</code>" for c in codes)
        nodes.append(
            f'''
      <div class="fc-node">
        <div class="fc-q-box">{q}</div>
        <div class="fc-branch">
          <div class="fc-spacer"></div>
          <div class="fc-mid"><div class="fc-arrow tall"></div><span class="fc-arrow-lbl">NO</span></div>
          <div class="fc-yes">
            <span class="fc-side yes">YES</span>
            <div class="fc-h right"></div>
            <div class="fc-use {color}">
              <b>{yes_title}</b>
              <span class="fc-desc">{yes_desc}</span>
              {code_html}
            </div>
          </div>
        </div>
      </div>'''
        )
    fb = "".join(f"<code>{c}</code>" for c in fallback_lines)
    return f'''
<h3>Decision flowchart</h3>
<p class="fc-kid-hint">Read from the top. If the answer is <b>YES</b>, stop at that box. If <b>NO</b>, go down.</p>
<div class="fc-wrap slide-fc">
  <div class="fc">
    <div class="fc-start">{start}<small>{start_sub}</small></div>
    <div class="fc-arrow"></div>
    {"".join(nodes)}
    <div class="fc-arrow"></div>
    <div class="fc-use dict fc-end">
      <b>{fallback_title}</b>
      <span class="fc-desc">{fallback_desc}</span>
      {fb}
    </div>
  </div>
</div>
'''


# Per-slide flowchart content (curriculum 1–35) — kid-friendly wording
FLOWS: dict[int, tuple[str, str, list[FlowQ], str, str, list[str]]] = {
    1: (
        "I want to run some Python",
        "Like turning on a machine that reads your recipe",
        [
            (
                "Do you only want to try one tiny line right now?",
                "Use the REPL",
                "A playground: type one line, see the answer at once.",
                ["python", ">>> 2 + 2"],
                "key",
            ),
            (
                "Do you have a whole program saved in a file?",
                "Run a script",
                "Tell Python: “read this file and do everything inside.”",
                ["python app.py"],
                "dd",
            ),
            (
                "Do you want to press buttons and debug in an editor?",
                "Use Cursor / VS Code",
                "Pick the Python brain (interpreter), then press F5 to run.",
                ["F5 · select interpreter"],
                "cm",
            ),
        ],
        "How Python works inside",
        "Your .py file becomes bytecode, then the virtual machine runs it step by step.",
        [".py → .pyc → run"],
    ),
    2: (
        "I am setting up Python on Windows",
        "Install → check → run",
        [
            (
                "Is this a brand-new computer with no Python?",
                "Install from python.org",
                "Download the installer. Tick “Add Python to PATH” so the terminal finds it.",
                ["Add to PATH ✓"],
                "key",
            ),
            (
                "Do you want to check that install worked?",
                "Ask for the version",
                "If these print a number, Python and pip are ready.",
                ["python --version", "pip --version"],
                "dd",
            ),
            (
                "Do you have more than one Python version?",
                "Use the py launcher",
                "Pick which Python to use, like choosing which tool from a toolbox.",
                ["py -3.12 app.py"],
                "cm",
            ),
        ],
        "Order matters",
        "Write def first. Call it later. Put the main starting door at the bottom.",
        ["def first → then if __name__ == '__main__'"],
    ),
    3: (
        "I want to know where to practice",
        "Three shelves: slides, short drills, big projects",
        [
            (
                "Are you learning the idea first?",
                "Open Training slides",
                "Read the picture stories here — theory and examples.",
                ["PythonTraining.html"],
                "key",
            ),
            (
                "Do you want a short homework file?",
                "Use Projects/",
                "Small practice files — one topic at a time.",
                ["Projects/ folder"],
                "dd",
            ),
            (
                "Do you want a real mini-app?",
                "Open Python-Set2/",
                "Bigger folders. Give each project its own venv sandbox.",
                ["venv per project"],
                "cm",
            ),
        ],
        "Always",
        "Keep packages in a project sandbox so toys from one project don’t break another.",
        ["venv + requirements.txt"],
    ),
    4: (
        "I want my code to look neat",
        "PEP = the house rules for Python style",
        [
            (
                "Are you naming things or lining up spaces?",
                "Follow PEP 8",
                "snake_case names. Use 4 spaces (not tabs).",
                ["snake_case", "4 spaces"],
                "key",
            ),
            (
                "Are you writing the comment at the top of a function?",
                "Follow PEP 257",
                "A short note that says what the function is for.",
                ['"""what this does"""'],
                "dd",
            ),
            (
                "Do you want the big ideas behind Python?",
                "Read the Zen (PEP 20)",
                "Simple rules like: be clear, not tricky.",
                ["explicit > implicit"],
                "cm",
            ),
        ],
        "Project helpers",
        "Tools can check style for you later (ruff / black / pyproject.toml).",
        ["pyproject.toml"],
    ),
    5: (
        "I need a box to store something",
        "First pick the kind of box",
        [
            (
                "Is it just one simple thing (number, text, yes/no)?",
                "Use a primitive",
                "One value in one hand: int, float, str, or bool.",
                ["age = 25", 'name = "Ravi"'],
                "key",
            ),
            (
                "Is it a growing row you can change (cart, list of scores)?",
                "Use a list",
                "Seats in a row. You can add, remove, or change seats.",
                ["[90, 85, 88]"],
                "dd",
            ),
            (
                "Is it a fixed record that must not change (GPS point)?",
                "Use a tuple",
                "A sealed pack. Good as a dict label too.",
                ["(12.97, 80.22)"],
                "cm",
            ),
            (
                "Do you only care about unique tags (no duplicates)?",
                "Use a set",
                "A bag of stickers. Same sticker twice becomes once.",
                ['{"red", "blue"}'],
                "key",
            ),
            (
                "Do you look things up by a name (label → value)?",
                "Use a dict",
                "Labeled boxes: open the label, get what is inside.",
                ['{"red": 3}'],
                "dict",
            ),
        ],
        "Still unsure?",
        "Open MindMap → Which collection? for a bigger chooser.",
        ["MindMap · Which collection?"],
    ),
    6: (
        "I want to write what type something should be",
        "Hints help the editor — Python still runs without checking them",
        [
            (
                "Is it a normal list or dict of known types?",
                "Use built-in hints",
                "Write the box type next to the name.",
                ["list[int]", "dict[str, int]"],
                "key",
            ),
            (
                "Could the value be missing?",
                "Allow None",
                "Means: text, or nothing.",
                ["str | None"],
                "dd",
            ),
            (
                "Do you only care that it has a certain method?",
                "Use a Protocol",
                "“If it can .send(), I can use it” — duck typing with a name.",
                ["class Writer(Protocol)"],
                "cm",
            ),
        ],
        "Remember",
        "Hints are sticky notes for tools (mypy). Wrong types may still run.",
        ["mypy checks · runtime does not enforce"],
    ),
    7: (
        "I need a math or compare sign",
        "Pick the sign that matches the job",
        [
            (
                "Do you want a normal divide that can make a decimal?",
                "Use /",
                "True division. 7/2 becomes 3.5.",
                ["7 / 2  →  3.5"],
                "key",
            ),
            (
                "Do you want whole pieces only (no leftover as decimal)?",
                "Use //",
                "Floor division. How many full groups fit.",
                ["7 // 2  →  3"],
                "dd",
            ),
            (
                "Do you ask “is this the exact same object in memory?”",
                "Use is",
                "Best for None / True / False checks.",
                ["x is None"],
                "cm",
            ),
            (
                "Do you ask “do these hold the same value?”",
                "Use ==",
                "Compares the contents, not the locker number.",
                ["a == b"],
                "dict",
            ),
        ],
        "Also useful",
        "Ask “is this item inside my collection?” with in.",
        ["x in items"],
    ),
    8: (
        "I need to choose what happens next",
        "Branch, loop, skip, or stop",
        [
            (
                "Do you need different paths (if this, else that)?",
                "Use if / elif / else",
                "Like a fork in the road. Indentation shows the path.",
                ["if ok:", "elif …:", "else:"],
                "key",
            ),
            (
                "Do you walk every item in a bag?",
                "Use for",
                "Pick one toy, do something, pick the next…",
                ["for x in items:"],
                "dd",
            ),
            (
                "Do you keep going while a light is still on?",
                "Use while",
                "Repeat until the condition becomes false.",
                ["while running:"],
                "cm",
            ),
            (
                "Do you need to stop early or skip one turn?",
                "Use break / continue",
                "break = leave the loop. continue = skip to next item.",
                ["break · continue · pass"],
                "dict",
            ),
        ],
        "Bonus",
        "A loop can have else — it runs only if you never break.",
        ["for … else:"],
    ),
    9: (
        "I want to build a new collection in one short line",
        "Comprehension = “make a new bag from an old bag”",
        [
            (
                "Do you need the full list kept in memory now?",
                "List comprehension",
                "Builds every answer and stores them all.",
                ["[n * n for n in nums]"],
                "key",
            ),
            (
                "Do you only want unique answers?",
                "Set comprehension",
                "Duplicates disappear by themselves.",
                ["{n % 2 for n in nums}"],
                "dd",
            ),
            (
                "Do you need label → value pairs?",
                "Dict comprehension",
                "Make many labeled boxes in one go.",
                ["{n: n * n for n in nums}"],
                "cm",
            ),
            (
                "Is the data huge and you only need one piece at a time?",
                "Generator expression",
                "Lazy: makes the next answer only when you ask.",
                ["(n * n for n in nums)"],
                "dict",
            ),
        ],
        "Don’t",
        "Don’t print or save files inside a comprehension — use a normal for loop.",
        ["for loops for side effects"],
    ),
    10: (
        "I want a reusable recipe (function)",
        "Write once, call many times",
        [
            (
                "Do you need a named recipe with steps?",
                "Write a def",
                "Give it a name, inputs, and a return value.",
                ["def add(a, b):", "    return a + b"],
                "key",
            ),
            (
                "Do you get extra unnamed extras?",
                "Use *args",
                "Collect leftover positional toys into a tuple.",
                ["def f(*args):"],
                "dd",
            ),
            (
                "Do you get extra named extras?",
                "Use **kwargs",
                "Collect leftover name=value toys into a dict.",
                ["def f(**kwargs):"],
                "cm",
            ),
            (
                "Is it a tiny one-line helper?",
                "Use lambda",
                "A nameless mini-function for simple jobs.",
                ["lambda x: x * 2"],
                "dict",
            ),
        ],
        "Danger",
        "Never use a mutable default like def f(items=[]). It shares one list forever.",
        ["use items=None instead"],
    ),
    11: (
        "I want a ready-made helper",
        "Built-ins that walk or inspect collections",
        [
            (
                "Do you want to change every item the same way?",
                "Use map",
                "Apply one function to each toy in the bag.",
                ["map(fn, items)"],
                "key",
            ),
            (
                "Do you want to keep only some items?",
                "Use filter",
                "Keep the ones that pass a yes/no test.",
                ["filter(fn, items)"],
                "dd",
            ),
            (
                "Do you want to walk two bags side by side?",
                "Use zip",
                "Pair item 0 with item 0, item 1 with item 1…",
                ["zip(names, scores)"],
                "cm",
            ),
            (
                "Do you also need the seat number?",
                "Use enumerate",
                "Gives (index, value) together.",
                ["enumerate(items)"],
                "dict",
            ),
        ],
        "Sorting",
        "sorted(a) makes a new list. a.sort() changes the same list.",
        ["sorted(a) · a.sort()"],
    ),
    12: (
        "I need a special collection helper",
        "Extra tools on top of normal list/dict",
        [
            (
                "Do you need to count how many times each thing appears?",
                "Use Counter",
                "Like tally marks for each word or color.",
                ["Counter(words)", ".most_common()"],
                "key",
            ),
            (
                "Are you sorting items into groups inside a loop?",
                "Use defaultdict",
                "Empty group appears by itself when you need it — then add the item.",
                ["defaultdict(list)", "groups[k].append(v)"],
                "dd",
            ),
            (
                "Do you need fast add/remove at both ends (front and back)?",
                "Use deque",
                "A line where people can join at the front or the back quickly.",
                ["deque()", "deque(maxlen=n)"],
                "cm",
            ),
            (
                "Do you want a tiny fixed record with names (x, y)?",
                "Use namedtuple",
                "A tuple you can call by field name — light and clear.",
                ["Point = namedtuple(...)", "Point(1, 2)"],
                "dict",
            ),
        ],
        "Two layers of settings",
        "Look in your dict first, then a backup dict — without copying everything.",
        ["ChainMap(Dict1, Dict2)"],
    ),
    13: (
        "Python is cleaning up memory",
        "Throw away toys nobody is holding",
        [
            (
                "Did the last name pointing at an object go away?",
                "Reference counting",
                "When nobody holds it, Python frees it right away (in CPython).",
                ["del x", "x = None"],
                "key",
            ),
            (
                "Do two objects point at each other in a circle?",
                "Generational GC",
                "A special cleaner finds circles that refcount alone can’t free.",
                ["gc module", "circular refs"],
                "dd",
            ),
            (
                "Do you want a soft link that does not keep the object alive?",
                "Use weakref",
                "A sticky note that says “look over there” without owning the toy.",
                ["weakref.ref(obj)"],
                "cm",
            ),
        ],
        "Finding leaks",
        "If memory grows forever, measure it — don’t guess.",
        ["tracemalloc · gc.get_referrers"],
    ),
    14: (
        "I need to check data shapes",
        "Pydantic = a bouncer for your fields",
        [
            (
                "Do you declare named fields with types?",
                "Use BaseModel",
                "Write the form: name, age, email…",
                ["class User(BaseModel):"],
                "key",
            ),
            (
                "Do you need rules or defaults?",
                "Field + validators",
                "“Age must be ≥ 0” and similar checks.",
                ["Field(...)", "field_validator"],
                "dd",
            ),
            (
                "Do you have raw input (dict / JSON) to turn into a model?",
                "model_validate",
                "Parse and check in one step.",
                ["User.model_validate(data)"],
                "cm",
            ),
        ],
        "Send it out",
        "Turn the model back into a plain dict when you need JSON.",
        ["model_dump()"],
    ),
    15: (
        "I want to model real things as objects",
        "Class = blueprint · object = one real thing",
        [
            (
                "Do you need a blueprint and then make copies?",
                "Write a class",
                "Blueprint first, then create instances.",
                ["class Car:", "c = Car()"],
                "key",
            ),
            (
                "Should a child reuse a parent’s abilities?",
                "Use inheritance",
                "Child gets parent skills, then can add more.",
                ["class Child(Parent):"],
                "dd",
            ),
            (
                "Should some details stay private?",
                "Encapsulation",
                "Hide insides with _name and @property doors.",
                ["_private", "@property"],
                "cm",
            ),
            (
                "Should the same call act differently for different objects?",
                "Polymorphism",
                "Same .speak() — dog woofs, cat meows.",
                ["override · duck typing"],
                "dict",
            ),
        ],
        "Hide the hard parts",
        "Abstraction: show a simple button, hide the messy wires (ABC).",
        ["ABC + @abstractmethod"],
    ),
    16: (
        "I want to control how attributes are read/written",
        "Doors and rules for object fields",
        [
            (
                "Is it a simple get/set with a little logic?",
                "Use @property",
                "Looks like a field, runs a function underneath.",
                ["@property", "@x.setter"],
                "key",
            ),
            (
                "Do many classes share the same field rule?",
                "Use a descriptor",
                "A reusable “field object” with __get__ / __set__.",
                ["__get__", "__set__"],
                "dd",
            ),
            (
                "Do you customize print / compare / length?",
                "Use dunder methods",
                "Magic names that Python calls for you.",
                ["__str__", "__eq__", "__len__"],
                "cm",
            ),
        ],
        "Link",
        "property is built on the descriptor idea.",
        ["descriptor protocol"],
    ),
    17: (
        "I want values one at a time (not all at once)",
        "Generators save memory — like a vending machine",
        [
            (
                "Do you need to pause and give the next value later?",
                "Use yield",
                "Function sleeps, hands you one item, wakes when you ask again.",
                ["def gen():", "    yield x"],
                "key",
            ),
            (
                "Do you want a one-line lazy stream?",
                "Generator expression",
                "Same idea as a list comp, but does not build the whole list.",
                ["(n * n for n in nums)"],
                "dd",
            ),
            (
                "Do you build your own walker?",
                "Iterator protocol",
                "__iter__ and __next__ — “give me the next, please.”",
                ["__iter__", "__next__"],
                "cm",
            ),
        ],
        "Why it matters",
        "Huge data: don’t load everything — pull one piece at a time.",
        ["lazy · low memory"],
    ),
    18: (
        "I want to wrap a function with extra behavior",
        "Decorator = gift wrap around a gift",
        [
            (
                "Add timing, logging, or permission checks?",
                "Use @decorator",
                "Put @name above the function — wrapping happens for you.",
                ["@timer", "def work():"],
                "key",
            ),
            (
                "Keep the original function’s name/docs?",
                "Use functools.wraps",
                "So help() and logs still show the real name.",
                ["@wraps(fn)"],
                "dd",
            ),
            (
                "Does the decorator need settings (like retry 3 times)?",
                "Decorator factory",
                "A function that builds the wrapper with your options.",
                ["@retry(3)"],
                "cm",
            ),
        ],
        "Shape",
        "Outer function takes fn, returns a new wrapper function.",
        ["def outer(fn): return wrapper"],
    ),
    19: (
        "Something went wrong while running",
        "Catch the problem so the program doesn’t explode",
        [
            (
                "Do you know which error might happen?",
                "try / except",
                "Try the risky step. If that error appears, handle it kindly.",
                ["try:", "except ValueError:"],
                "key",
            ),
            (
                "Must you always clean up (close file / lock)?",
                "finally (and else)",
                "finally runs whether it worked or failed.",
                ["finally:", "else:  # no error"],
                "dd",
            ),
            (
                "Do you need to shout that something is wrong?",
                "raise",
                "Throw an error on purpose with a clear message.",
                ["raise ValueError('bad age')"],
                "cm",
            ),
        ],
        "Your own error type",
        "Make a custom Exception subclass for your app’s problems.",
        ["class AppError(Exception):"],
    ),
    20: (
        "I want work to happen “at the same time”",
        "Threads vs processes — and the GIL gate",
        [
            (
                "Is the program mostly waiting (network, disk)?",
                "Use threading",
                "While one waits, another can run. Good for I/O.",
                ["threading.Thread"],
                "key",
            ),
            (
                "Is the program crunching heavy CPU math?",
                "Use multiprocessing",
                "Separate processes — better for pure CPU work.",
                ["Process", "Pool"],
                "dd",
            ),
            (
                "Wonder why two threads don’t both burn CPU hard?",
                "Remember the GIL",
                "CPython mostly runs one bytecode thread at a time.",
                ["GIL · one at a time"],
                "cm",
            ),
        ],
        "Simple rule",
        "Waiting a lot → threads. Heavy math → processes.",
        ["I/O → threads · CPU → processes"],
    ),
    21: (
        "Many waits, one friendly style",
        "async/await — take turns while waiting",
        [
            (
                "Lots of network waits in one program?",
                "Write async def + await",
                "Pause this task while waiting; let others run.",
                ["async def fetch():", "    await ..."],
                "key",
            ),
            (
                "Run many async jobs together?",
                "asyncio.gather",
                "Start a group of tasks and wait for all.",
                ["await gather(t1, t2)"],
                "dd",
            ),
            (
                "Who decides whose turn it is?",
                "The event loop",
                "A traffic officer for async tasks.",
                ["asyncio.run(main())"],
                "cm",
            ),
        ],
        "Rule",
        "You can only await inside an async function.",
        ["await only in async def"],
    ),
    22: (
        "I want a diary of what the app did",
        "Logging = write messages with importance levels",
        [
            (
                "Do you need to choose how serious the note is?",
                "Pick a level",
                "DEBUG (chatty) up to CRITICAL (fire alarm).",
                ["DEBUG → INFO → WARNING → ERROR → CRITICAL"],
                "key",
            ),
            (
                "Where should messages go?",
                "Add handlers",
                "Screen, file, or rotating files that don’t grow forever.",
                ["StreamHandler", "RotatingFileHandler"],
                "dd",
            ),
            (
                "Do you want a clear message format?",
                "Use a formatter",
                "Show time, level, and text the same way every time.",
                ["%(levelname)s %(message)s"],
                "cm",
            ),
        ],
        "Prefer logging",
        "In real apps, logging beats print — you can filter and save it.",
        ["logging > print"],
    ),
    23: (
        "I want to prove the code works",
        "Tests = practice questions for your functions",
        [
            (
                "Simple checks with assert?",
                "Use pytest",
                "Write a test function; assert the answer is right.",
                ["assert result == 1"],
                "key",
            ),
            (
                "Prefer class-style tests?",
                "Use unittest",
                "TestCase methods and self.assertEqual…",
                ["unittest.TestCase"],
                "dd",
            ),
            (
                "Need a fake helper so tests stay small?",
                "Use mock / patch",
                "Pretend the network/database answered — don’t call the real one.",
                ["@patch('mod.fn')"],
                "cm",
            ),
        ],
        "Good habit",
        "Test what users see (behavior), not every private detail.",
        ["test behavior"],
    ),
    24: (
        "I need to find patterns in text",
        "Regex = a search pattern language",
        [
            (
                "Find the pattern anywhere in the text?",
                "re.search",
                "Hunt through the whole string.",
                ["re.search(pat, text)"],
                "key",
            ),
            (
                "Must the match start at the beginning?",
                "re.match",
                "Only checks from the start of the string.",
                ["re.match(pat, text)"],
                "dd",
            ),
            (
                "Want every match as a list?",
                "re.findall",
                "Collect all the pieces that fit.",
                ["re.findall(pat, text)"],
                "cm",
            ),
        ],
        "Tip",
        "Use raw strings so backslashes stay happy: r'\\d+'.",
        [r"r'\d+'"],
    ),
    25: (
        "I need to read or write a file",
        "Open carefully and always close",
        [
            (
                "Simple text file?",
                "with open(...)",
                "with is a promise: the file closes even if something fails.",
                ["with open(path) as f:"],
                "key",
            ),
            (
                "Building paths on Windows and Mac?",
                "Use pathlib",
                "Join folders with / — works across operating systems.",
                ["Path('a') / 'b.txt'"],
                "dd",
            ),
            (
                "JSON or CSV data?",
                "json / csv modules",
                "Turn files into dicts/lists and back.",
                ["json.load", "csv.DictReader"],
                "cm",
            ),
        ],
        "Golden rule",
        "Always prefer with so you don’t leave files open.",
        ["with closes for you"],
    ),
    26: (
        "I need auto cleanup (setup + teardown)",
        "Context manager = borrow, then put back",
        [
            (
                "Does the object already support with?",
                "Just use with",
                "Files, locks, DB connections often work this way.",
                ["with lock:", "with conn:"],
                "key",
            ),
            (
                "Want to write a small with helper?",
                "@contextmanager",
                "yield in the middle; finally cleans up.",
                ["@contextmanager", "yield"],
                "dd",
            ),
            (
                "Prefer a class with enter/exit?",
                "__enter__ / __exit__",
                "The official protocol methods for with.",
                ["__enter__", "__exit__"],
                "cm",
            ),
        ],
        "Goal",
        "Always release the toy (file/lock) — even when an error happens.",
        ["safe cleanup"],
    ),
    27: (
        "I want a private toy box for packages",
        "venv = sandbox so projects don’t fight",
        [
            (
                "Create a new sandbox?",
                "python -m venv",
                "Makes a .venv folder for this project only.",
                ["python -m venv .venv"],
                "key",
            ),
            (
                "Turn the sandbox on?",
                "Activate",
                "Your terminal now uses this project’s Python and pip.",
                [r".venv\Scripts\activate"],
                "dd",
            ),
            (
                "Save the list of packages?",
                "requirements.txt",
                "A shopping list so others can install the same toys.",
                ["pip freeze > requirements.txt"],
                "cm",
            ),
        ],
        "Rule",
        "One project → one venv. Don’t install everything globally.",
        ["one venv per project"],
    ),
    28: (
        "I am building an API with a database",
        "Routes talk HTTP · schemas check data · ORM talks DB",
        [
            (
                "Need a web address that runs code?",
                "FastAPI route",
                "Decorate a function: GET/POST and path.",
                ["@app.get", "Depends"],
                "key",
            ),
            (
                "Need to check request/response shape?",
                "Pydantic schema",
                "The form that data must fill.",
                ["BaseModel"],
                "dd",
            ),
            (
                "Need to save/load rows in a database?",
                "SQLAlchemy ORM",
                "Python classes map to tables.",
                ["Session", "models"],
                "cm",
            ),
        ],
        "Layer cake",
        "Keep routes thin: routes → services → schemas/models.",
        ["clear layers"],
    ),
    29: (
        "I am exploring the portfolio repo",
        "Python-Set2 has many practice worlds",
        [
            (
                "Want OOP / basics drills?",
                "pythonBasics",
                "Folders like MyClass and MyCollections.",
                ["MyClass/", "MyCollections/"],
                "key",
            ),
            (
                "Want data tables and exercises?",
                "Pandas / Google exercises",
                "Titanic, babynames, file drills.",
                ["Pandas", "babynames"],
                "dd",
            ),
            (
                "Want web or voice apps?",
                "Django · Pipecat",
                "Bigger apps: APIs and voice pipelines.",
                ["DRF", "WebRTC"],
                "cm",
            ),
        ],
        "Learning path",
        "Basics first → small projects → full apps.",
        ["step by step"],
    ),
    30: (
        "I am inside pythonBasics",
        "Pick the folder that matches today’s topic",
        [
            (
                "Learning classes and inheritance?",
                "Open MyClass/",
                "Real class samples you can run.",
                ["MyClass/"],
                "key",
            ),
            (
                "Learning list/dict/set code?",
                "Open MyCollections/",
                "Hands-on collection scripts.",
                ["MyCollections/"],
                "dd",
            ),
            (
                "Learning tests?",
                "Open MyUnitTesting/",
                "unittest and mock examples.",
                ["MyUnitTesting/"],
                "cm",
            ),
        ],
        "How to use",
        "Open the folder, run the .py files, change them, run again.",
        ["read · run · tweak"],
    ),
    31: (
        "I want practice with real data files",
        "Exercises that feel like real chores",
        [
            (
                "Finding names with patterns?",
                "babynames (regex)",
                "Search text files with regular expressions.",
                ["re on files"],
                "key",
            ),
            (
                "Copying special files around?",
                "copyspecial",
                "Use os/shutil to move and copy safely.",
                ["shutil", "os"],
                "dd",
            ),
            (
                "Tables, groups, charts?",
                "Pandas Titanic",
                "Load a CSV, clean it, group, and explore.",
                ["DataFrame", "groupby"],
                "cm",
            ),
        ],
        "Skill loop",
        "Read → clean → analyze → explain.",
        ["data workflow"],
    ),
    32: (
        "I want a full website / API in Python",
        "Django for pages · DRF for JSON APIs",
        [
            (
                "Need HTML pages from the server?",
                "Django MVT",
                "Models, views, templates — classic website style.",
                ["templates", "views"],
                "key",
            ),
            (
                "Need JSON for a frontend app?",
                "Django REST Framework",
                "Serializers turn models into JSON and back.",
                ["Serializer", "ViewSet"],
                "dd",
            ),
            (
                "Need login or tokens?",
                "Auth / JWT",
                "Decide who is allowed to see or change data.",
                ["permissions", "JWT"],
                "cm",
            ),
        ],
        "Flow",
        "models → serializers → views/viewsets.",
        ["clear pipeline"],
    ),
    33: (
        "I want a talking voice pipeline",
        "Hear → think → speak",
        [
            (
                "Turn sound into words?",
                "STT (speech to text)",
                "Microphone audio becomes text.",
                ["audio → text"],
                "key",
            ),
            (
                "Think of a reply?",
                "LLM step",
                "Send the text to a model, get an answer.",
                ["prompt → reply"],
                "dd",
            ),
            (
                "Turn the reply back into sound?",
                "TTS + WebRTC",
                "Text becomes audio you can play live.",
                ["text → audio"],
                "cm",
            ),
        ],
        "Whole pipe",
        "STT → LLM → TTS (Pipecat-style).",
        ["voice pipeline"],
    ),
    34: (
        "I want a clean real-project layout",
        "Folders that tell a story",
        [
            (
                "Where do HTTP routes live?",
                "routes / services / schemas",
                "Keep each job in its own room.",
                ["app-per-domain"],
                "key",
            ),
            (
                "Where do tests live?",
                "tests/ near the root",
                "So pytest can find them easily.",
                ["pytest discovery"],
                "dd",
            ),
            (
                "What should I learn next?",
                "Follow the learning path",
                "Basics → API → deploy — don’t skip steps.",
                ["step ladder"],
                "cm",
            ),
        ],
        "Habit",
        "Small modules, clear borders, easy tests.",
        ["keep it simple"],
    ),
    35: (
        "I know C# and I’m mapping ideas to Python",
        "Same ideas, different spelling",
        [
            (
                "Do types need to be written always?",
                "C# often yes · Python optional hints",
                "Python can run without type words; hints help tools.",
                ["list[int] optional"],
                "key",
            ),
            (
                "How do you make a code block?",
                "{} in C# · indent in Python",
                "Spaces show what belongs inside.",
                ["4 spaces · PEP 8"],
                "dd",
            ),
            (
                "What is null called here?",
                "None",
                "Check with is None — not == null habits.",
                ["x is None"],
                "cm",
            ),
        ],
        "Mindset",
        "Translate the idea first, then learn the Python spelling.",
        ["ideas first · syntax second"],
    ),
}


def flowchart_for(n: int) -> str:
    data = FLOWS.get(n)
    if not data:
        return ""
    start, sub, questions, fb_title, fb_desc, fb_lines = data
    return _render(start, sub, questions, fb_title, fb_desc, fb_lines)
