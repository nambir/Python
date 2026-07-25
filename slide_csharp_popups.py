"""C# comparison popups — triggered from glossary / slide content."""

from __future__ import annotations

from collections.abc import Callable

from slide_code import vs_editor


def csharp_compare_btn(popup_id: str, label: str = "C# Comparison") -> str:
    return (
        f'<button type="button" class="btn-csharp-pop" '
        f'onclick="openCsharpWin(\'{popup_id}\')" title="Open draggable C# comparison window">'
        f"{label}</button>"
    )


def _note(text: str) -> str:
    return f'<p class="csharp-pop-note"><b>Bottom line:</b> {text}</p>'


def _py_cs(title_py: str, py: str, title_cs: str, cs: str) -> str:
    return (
        f"<p>{title_py}</p>"
        f"{vs_editor(py, lang='python', compact=True)}"
        f"<p>{title_cs}</p>"
        f"{vs_editor(cs, lang='csharp', compact=True)}"
    )


def _hetero_list_body() -> str:
    py = 'order = [101, "SHIPPED", ["Google", "Amazon"]]'
    cs = """// Does NOT compile:
var nums = new List<int>();
nums.Add(101);
nums.Add("SHIPPED");  // error

// Works, but you lose compile-time type safety:
var mixed = new List<object>
{
    101,
    "SHIPPED",
    new List<string> { "Google", "Amazon" }
};
int id = (int)mixed[0];
string status = (string)mixed[1];"""
    tuple_cs = """var order = (Id: 101, Status: "SHIPPED",
    Vendors: new List<string> { "Google", "Amazon" });
Console.WriteLine(order.Id);"""
    record_cs = """public record Order(int Id, string Status, List<string> Vendors);
var order = new Order(101, "SHIPPED", new() { "Google", "Amazon" });"""
    return f"""
<p>In <b>Python</b>, one <code>list</code> can hold mixed types naturally:</p>
{vs_editor(py, lang="python", compact=True)}
<p>In <b>C#</b>, <code>List&lt;T&gt;</code> is strongly typed — you cannot mix types unless <code>T</code> is <code>object</code>:</p>
{vs_editor(cs, lang="csharp", compact=True)}
<table class="data-tbl csharp-pop-tbl">
<tr><th>Approach</th><th>What it is</th><th>When to use</th></tr>
<tr><td><code>List&lt;object&gt;</code></td><td>Every item stored as <code>object</code> — cast when reading.</td><td>Quick prototype — avoid in new APIs.</td></tr>
<tr><td><code>ValueTuple</code></td><td>Fixed slots, each with a known type — access by name.</td><td>Return 2–4 related values from a method.</td></tr>
<tr><td><code>record</code></td><td>Named reusable type with clear fields.</td><td>DTOs, domain models, API payloads.</td></tr>
</table>
<p><b>ValueTuple example</b> — closest to a single heterogeneous “record”:</p>
{vs_editor(tuple_cs, lang="csharp", compact=True)}
<p><b>Record example</b> — best when the shape is reused:</p>
{vs_editor(record_cs, lang="csharp", compact=True)}
{_note("Python <code>[101, \"SHIPPED\", [...]]</code> maps best to a <b>named ValueTuple</b> or <b>record</b> — not <code>List&lt;object&gt;</code>.")}
"""


def _tuple_body() -> str:
    return (
        _py_cs(
            "Python <b>tuple</b> — fixed record, immutable, hashable:",
            "pin = (12.97, 80.22)\nok, data = fetch_user(10)  # (bool, dict)",
            "C# <b>ValueTuple</b> — fixed fields, typed, value semantics:",
            """var pin = (12.97, 80.22);
var (ok, data) = FetchUser(10);
// Named:
var result = (Ok: true, Data: userDict);""",
        )
        + _note("Use Python tuple for fixed small records and dict keys. C# ValueTuple is the closest match — not <code>List</code>.")
    )


def _hashable_keys_body() -> str:
    return (
        _py_cs(
            "Python dict keys must be <b>hashable</b> (immutable):",
            """coords = (12.97, 80.22)
prices = {coords: 99.5}   # OK — tuple key

# bad = {[1, 2]: 5}     # TypeError: unhashable type: 'list'""",
            "C# <code>Dictionary&lt;TKey,TValue&gt;</code> — key type must be usable as key:",
            """var coords = (12.97, 80.22);
var prices = new Dictionary<(double, double), decimal>
{
    [coords] = 99.5m
};

// List<int> cannot be a Dictionary key type.""",
        )
        + _note("Both languages require stable keys. Python blocks lists/dicts/sets; C# requires proper <code>GetHashCode</code> / equality on <code>TKey</code>.")
    )


def _duck_typing_body() -> str:
    py_normal = """# NORMAL OOP — class has a method (not duck typing yet)
class EmailNotifier:
    def send(self, msg):
        return f"Email: {msg}"

email = EmailNotifier()
email.send("Order shipped")  # you know the type"""

    py_duck = """# DUCK TYPING — notify() does not know the class name
class EmailNotifier:
    def send(self, msg):
        return f"Email: {msg}"

class SmsNotifier:
    def send(self, msg):
        return f"SMS: {msg}"

class SlackNotifier:
    def send(self, msg):
        return f"Slack: {msg}"

def notify(channel, msg):
    return channel.send(msg)  # only needs .send()

notify(EmailNotifier(), "Hi")
notify(SmsNotifier(), "Hi")
notify(SlackNotifier(), "Hi")"""

    cs_interface = """// Idiomatic C# — contract required (NOT duck typing)
interface INotifier
{
    void Send(string msg);
}

class EmailNotifier : INotifier
{
    public void Send(string msg)
        => Console.WriteLine($"Email: {msg}");
}

void Notify(INotifier channel, string msg)
{
    channel.Send(msg);  // must implement INotifier
}"""

    cs_dynamic = """// Closest to Python duck typing — dynamic (rare / avoid in APIs)
dynamic channel = new EmailNotifier();
channel.Send(msg);  // resolved at runtime, no compile-time check"""

    cs_extension = """// Extension method on string — NOT duck typing
public static class NameHelpers
{
    public static string Salutation(this string name, string title)
        => $"{title} {name}".Trim();
}

"Ravi".Salutation("Mr");  // type is still string at compile time"""

    return f"""
<p><b>Key idea (memorize this):</b></p>
<ul>
  <li><b>A class having a method is normal</b> — that is just OOP.</li>
  <li><b>Duck typing</b> is when <b>another function</b> uses that object
      <b>without knowing the class name</b> — only the behavior
      (e.g. “does it have <code>.send()</code>?”).</li>
</ul>
<p>Saying: <i>“If it walks like a duck and quacks like a duck, treat it as a duck.”</i>
In code: if it has <code>.send()</code>, call <code>.send()</code>.</p>

<p><b>1) Python — normal class method</b> (not duck typing yet):</p>
{vs_editor(py_normal, lang="python", compact=True)}

<p><b>2) Python — duck typing</b> (<code>notify</code> accepts any object with <code>.send()</code>):</p>
{vs_editor(py_duck, lang="python", compact=True)}
<p>No shared base class. No <code>interface</code>. Python checks at <b>runtime</b>.</p>

<p><b>3) C# idiomatic — interface contract</b> (closest recommended match, but <b>not</b> duck typing):</p>
{vs_editor(cs_interface, lang="csharp", compact=True)}

<p><b>4) C# <code>dynamic</code></b> — closest to true duck typing (uncommon in production):</p>
{vs_editor(cs_dynamic, lang="csharp", compact=True)}

<p><b>5) C# extension method on <code>string</code></b> — different idea (Salutation example):</p>
{vs_editor(cs_extension, lang="csharp", compact=True)}
<p>Extension methods add a helper to a <b>known type</b> at compile time.
They are <b>not</b> “any object that has the method.”</p>

<table class="data-tbl csharp-pop-tbl">
<tr><th>Idea</th><th>Python</th><th>C#</th></tr>
<tr>
  <td>Class has a method</td>
  <td>Normal OOP — <code>email.send()</code></td>
  <td>Normal OOP — <code>email.Send()</code></td>
</tr>
<tr>
  <td>Duck typing</td>
  <td><code>notify(channel)</code> — any object with <code>.send()</code></td>
  <td>Usually <code>INotifier</code>; or rare <code>dynamic</code></td>
</tr>
<tr>
  <td>Who is allowed?</td>
  <td>Behavior at <b>runtime</b></td>
  <td>Declared type / interface at <b>compile time</b></td>
</tr>
<tr>
  <td>Shared base / interface?</td>
  <td>Not required</td>
  <td>Usually required</td>
</tr>
<tr>
  <td>Extension method on string</td>
  <td>N/A (plain function / method)</td>
  <td>Compile-time helper on fixed type — <b>≠ duck typing</b></td>
</tr>
</table>

{_note(
    "Class method = normal. Duck typing = caller accepts many classes by behavior only. "
    "C# prefers <code>interface</code>; <code>dynamic</code> ≈ Python duck typing but is rare; "
    "extension methods on <code>string</code> are a different concept."
)}
"""


def _indentation_body() -> str:
    return (
        _py_cs(
            "Python — blocks defined by indentation:",
            """if score >= 60:
    print("Pass")
    print("Good job")
else:
    print("Try again")""",
            "C# — blocks defined by braces:",
            """if (score >= 60)
{
    Console.WriteLine("Pass");
    Console.WriteLine("Good job");
}
else
{
    Console.WriteLine("Try again");
}""",
        )
        + _note("Mixing tabs/spaces breaks Python. Use 4 spaces consistently. C# uses <code>{ }</code> — indentation is style only.")
    )


def _dynamic_typing_body() -> str:
    return (
        _py_cs(
            "Python — same variable, different types at runtime:",
            """x = 42
x = "hello"
print(type(x))  # <class 'str'>""",
            "C# — type fixed at compile time (without <code>dynamic</code>):",
            """int x = 42;
// x = "hello";  // compile error

dynamic d = 42;
d = "hello";  // runtime only — loses static checks""",
        )
        + _note("Python checks types at runtime. C# checks at compile time — use type hints + mypy in Python for similar safety.")
    )


def _main_block_body() -> str:
    return (
        _py_cs(
            "Python — run code only when file is executed directly:",
            """def main():
    print("Hello")

if __name__ == "__main__":
    main()""",
            "C# — entry point is always <code>Main</code>:",
            """class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello");
    }
}""",
        )
        + _note("<code>if __name__ == \"__main__\":</code> ≈ C# <code>Main</code>. Put it at the <b>bottom</b> of the file after all <code>def</code> / <code>class</code>.")
    )


def _def_order_body() -> str:
    return (
        _py_cs(
            "Python — file runs top to bottom; name must exist before call:",
            """# Wrong — NameError:
# Add(1, 2)

def Add(x, y):
    print(x + y)

Add(1, 2)  # OK — def ran first""",
            "C# — inside a class, method order usually does not matter:",
            """class Calc
{
    static void Main() => Add(1, 2);  // OK

    static void Add(int x, int y)
        => Console.WriteLine(x + y);
}""",
        )
        + _note("In a <code>.py</code> script, define functions first; put <code>if __name__ == \"__main__\":</code> last.")
    )


def _none_null_body() -> str:
    py = """value = None
if value is None:
    print("empty")

# Not None:
if value is not None:
    print("has a value")"""

    cs = """string? value = null;
if (value == null)
    Console.WriteLine("empty");

// C# 9+ pattern:
if (value is null)
    Console.WriteLine("empty");

// Not null:
if (value != null)
    Console.WriteLine("has a value");

if (value is not null)   // C# 9+
    Console.WriteLine("has a value");"""

    return f"""
<p><b>Python</b> — single <code>None</code> object; test with <code>is</code> / <code>is not</code>:</p>
{vs_editor(py, lang="python", compact=True)}

<p><b>C#</b> — <code>null</code> reference; test with <code>==</code> / <code>!=</code> or <code>is</code> / <code>is not</code>:</p>
{vs_editor(cs, lang="csharp", compact=True)}

<table class="data-tbl csharp-pop-tbl">
<tr><th>Check</th><th>Python</th><th>C#</th></tr>
<tr>
  <td>Is empty / null?</td>
  <td><code>if value is None:</code></td>
  <td><code>if (value == null)</code> or <code>if (value is null)</code></td>
</tr>
<tr>
  <td>Has a value? (not None)</td>
  <td><code>if value is not None:</code></td>
  <td><code>if (value != null)</code> or <code>if (value is not null)</code></td>
</tr>
</table>

{_note(
    "Python: prefer <code>is None</code> / <code>is not None</code> (not <code>== None</code>). "
    "C#: <code>== null</code> / <code>!= null</code>, or C# 9+ <code>is null</code> / <code>is not null</code>."
)}
"""


def _is_vs_equals_body() -> str:
    py = """a = [1, 2]
b = [1, 2]
print(a == b)   # True
print(a is b)   # False"""

    cs = """var a = new[] { 1, 2 };
var b = new[] { 1, 2 };

Console.WriteLine(a == b);     // False
// Console.WriteLine(a is b);  // INVALID — C# "is" needs a type, not another variable
Console.WriteLine(a is int[]); // True  — type check (NOT identity)
Console.WriteLine(ReferenceEquals(a, b)); // False — identity (like Python "is")
Console.WriteLine(a.SequenceEqual(b));    // True  — same values (like Python "==")"""

    return f"""
<p><b>Python</b></p>
{vs_editor(py, lang="python", compact=True)}

<p><b>C#</b> — same data: both arrays are <code>{{1, 2}}</code></p>
{vs_editor(cs, lang="csharp", compact=True)}

<table class="data-tbl csharp-pop-tbl">
<tr><th>Expression</th><th>Python result</th><th>C# result</th></tr>
<tr>
  <td><code>a == b</code></td>
  <td><b>True</b> (same values)</td>
  <td><b>False</b> (arrays: same object? — no)</td>
</tr>
<tr>
  <td><code>a is b</code></td>
  <td><b>False</b> (same object? — no)</td>
  <td><b>Not valid</b> like Python. C# <code>is</code> checks <b>type</b>
  (<code>a is int[]</code> → <b>True</b>). For identity use
  <code>ReferenceEquals(a, b)</code> → <b>False</b></td>
</tr>
</table>

{_note(
    "C# <code>a == b</code> on arrays → <b>False</b>. "
    "C# has no <code>a is b</code> identity check — use <code>ReferenceEquals(a, b)</code> → <b>False</b>. "
    "Same values in C#: <code>SequenceEqual</code> → <b>True</b>."
)}
"""


def _pass_stub_body() -> str:
    return (
        _py_cs(
            "Python — <code>pass</code> = empty block stub:",
            """def save_report():
    pass  # TODO later

class TodoService:
    pass""",
            "C# — empty <code>{ }</code> or throw:",
            """void SaveReport() { }  // empty stub

void SaveReportV2()
    => throw new NotImplementedException();""",
        )
        + _note("<code>pass</code> ≈ empty <code>{ }</code>. <code>NotImplementedError</code> ≈ <code>NotImplementedException</code>.")
    )


def _foreach_body() -> str:
    return (
        _py_cs(
            "Python <code>for … in …</code>:",
            """for item in items:
    print(item)

for i in range(5):
    print(i)  # 0..4""",
            "C# <code>foreach</code> and <code>for</code>:",
            """foreach (var item in items)
    Console.WriteLine(item);

for (int i = 0; i < 5; i++)
    Console.WriteLine(i);""",
        )
        + _note("Python <code>for x in iterable</code> ≈ C# <code>foreach</code>. <code>range(5)</code> ≈ <code>for (int i = 0; i &lt; 5; i++)</code>.")
    )


def _type_hints_body() -> str:
    py = """from decimal import Decimal

def charge(amount: Decimal, currency: str) -> str:
    return f"Charged {amount} {currency}"

# Same bad call in both cases:
result = charge("100", 91)
print(result)"""

    cs = """// C# — compiler blocks wrong types (like mypy, but automatic)
string Charge(decimal amount, string currency)
{
    return $"Charged {amount} {currency}";
}

// Charge("100", 91);  // compile error — will not build
Charge(100.00m, "INR");  // OK"""

    return f"""
<p><b>Same Python code</b> — compare with vs without mypy:</p>
{vs_editor(py, lang="python", compact=True)}
<table class="data-tbl csharp-pop-tbl">
<tr><th>Case</th><th>Input</th><th>Output</th></tr>
<tr>
  <td><b>Without mypy</b></td>
  <td><code>python app.py</code></td>
  <td>Program runs. Hints ignored.<br>
  <code>Charged 100 91</code></td>
</tr>
<tr>
  <td><b>With mypy</b></td>
  <td><code>mypy app.py</code></td>
  <td>Program not executed. Example errors:<br>
  <code>error: Argument 1 … expected "Decimal"</code><br>
  <code>error: Argument 2 … expected "str"</code><br>
  <code>Found 2 errors in 1 file</code></td>
</tr>
</table>
<p><b>C#</b> — types checked at compile time (always, like mypy but built-in):</p>
{vs_editor(cs, lang="csharp", compact=True)}
{_note(
    "mypy is a separate command (<code>pip install mypy</code>). "
    "It does not run when you type <code>python app.py</code>. "
    "C# catches the same mismatch automatically at build time."
)}
"""


def _listcomp_linq_body() -> str:
    return (
        _py_cs(
            "Python list comprehension:",
            """squares = [n * n for n in range(10) if n % 2 == 0]
names = [u.name for u in users if u.active]""",
            "C# LINQ (similar idea):",
            """var squares = Enumerable.Range(0, 10)
    .Where(n => n % 2 == 0)
    .Select(n => n * n)
    .ToList();

var names = users
    .Where(u => u.Active)
    .Select(u => u.Name)
    .ToList();""",
        )
        + _note("Comprehensions ≈ LINQ <code>Where</code> + <code>Select</code>. Generator <code>( )</code> ≈ deferred LINQ without <code>ToList()</code>.")
    )


def _lambda_body() -> str:
    return (
        _py_cs(
            "Python lambda — one expression only:",
            """# 1) Store lambda in a variable, then call it
multiply_by_two = lambda x: x * 2
print(multiply_by_two(5))    # 10  ← how it is used

# Same as:
# def multiply_by_two(x):
#     return x * 2

# 2) Separate example — pass lambda directly (no name needed)
items = [
    {"name": "pen",  "amount": 30},
    {"name": "book", "amount": 10},
    {"name": "bag",  "amount": 50},
]
# key= tells sorted HOW to order each item:
#   r              → one dict from items
#   r["amount"]    → use that number as the sort key
# sorted calls the lambda for each item → 30, 10, 50 → sorts by those
sorted(items, key=lambda r: r["amount"])
# → book(10), pen(30), bag(50)

# Same without lambda:
# def get_amount(r):
#     return r["amount"]
# sorted(items, key=get_amount)""",
            "C# lambda / expression-bodied members:",
            """// 1) Store lambda in a variable, then call it
Func<int, int> multiplyByTwo = x => x * 2;
Console.WriteLine(multiplyByTwo(5));  // 10  ← how it is used

// 2) Separate example — pass lambda directly to OrderBy
// r => r.Amount  = for each item r, sort by its Amount property
items.OrderBy(r => r.Amount);

// Statement lambda:
Action<int> log = n => Console.WriteLine(n);""",
        )
        + _note(
            "<code>multiply_by_two(5)</code> / <code>multiplyByTwo(5)</code> "
            "<b>calls</b> the stored lambda — same idea as a normal function. "
            "For sorting: <code>key=lambda r: r[\"amount\"]</code> means "
            "<b>for each item <code>r</code>, use <code>r[\"amount\"]</code> as the sort value</b> "
            "(same as a named <code>get_amount</code> function). "
            "Python <code>lambda</code> is limited to one expression; use <code>def</code> for multi-line logic."
        )
    )


def _mutable_default_body() -> str:
    return (
        _py_cs(
            "Python trap — default list created once:",
            """# BUG — same list every call:
def add_item(x, items=[]):
    items.append(x)
    return items

# Fix:
def add_item(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items""",
            "C# — default parameter values re-evaluated per call for primitives; reference types share default too if mutable:",
            """// Similar trap with mutable static/list default is rare in C#
// Prefer overloads or optional parameters with null-coalescing:
void AddItem(int x, List<int>? items = null)
{
    items ??= new List<int>();
    items.Add(x);
}""",
        )
        + _note("Never use <code>def f(items=[])</code>. Default objects are created once at function definition time.")
    )


def _self_this_body() -> str:
    return (
        _py_cs(
            "Python — <code>self</code> is explicit first parameter:",
            """class Account:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return self.name""",
            "C# — <code>this</code> is implicit:",
            """class Account
{
    public string Name { get; }
    public Account(string name) => Name = name;
    public string Greet() => Name;
}""",
        )
        + _note("<code>self</code> ≈ <code>this</code> but you must declare it on every instance method in Python.")
    )


def _init_constructor_body() -> str:
    return (
        _py_cs(
            "Python <code>__init__</code> — initializer (not a true constructor):",
            """class User:
    def __init__(self, email):
        self.email = email""",
            "C# constructor — same name as class:",
            """class User
{
    public string Email { get; }
    public User(string email) => Email = email;
}""",
        )
        + _note("<code>__init__</code> sets up the instance after Python creates it. C# constructor runs during <code>new</code>.")
    )


def _inheritance_body() -> str:
    return (
        _py_cs(
            "Python — multiple inheritance allowed:",
            """class Animal:
    def speak(self): return \"...\"

class Dog(Animal):
    def speak(self): return \"Woof\"""",
            "C# — single base class (interfaces for extra contracts):",
            """class Animal { public virtual string Speak() => \"...\"; }
class Dog : Animal
{
    public override string Speak() => \"Woof\";
}

interface IFly { void Fly(); }""",
        )
        + _note("Python MRO resolves multiple bases. C# uses one base class + interfaces. Both support override / polymorphism.")
    )


def _yield_return_body() -> str:
    return (
        _py_cs(
            "Python generator — <code>yield</code> pauses and streams:",
            """def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.strip()""",
            "C# <code>yield return</code> — similar lazy iterator:",
            """IEnumerable<string> ReadLines(string path)
{
    foreach (var line in File.ReadLines(path))
        yield return line.Trim();
}""",
        )
        + _note("<code>yield</code> / <code>yield return</code> both produce lazy sequences — ideal for large files.")
    )


def _decorator_body() -> str:
    return (
        _py_cs(
            "Python decorator — wraps function at runtime:",
            """def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper

@timer
def work(): ...""",
            "C# — attributes + middleware / filters (different mechanism):",
            """[HttpGet(\"/users\")]
public IActionResult GetUsers() { ... }

// Or source generators / interceptors in modern C#
// Decorators are not built-in syntax like Python @""",
        )
        + _note("Python <code>@decorator</code> wraps callables dynamically. C# uses attributes, middleware, and DI — conceptually similar, different syntax.")
    )


def _try_catch_body() -> str:
    return (
        _py_cs(
            "Python — <code>try / except / else / finally</code>:",
            """try:
    save(data)
except PermissionError:
    return 403
except OSError:
    return 500
else:
    log.info(\"ok\")
finally:
    temp.cleanup()""",
            "C# — <code>try / catch / finally</code>:",
            """try
{
    Save(data);
}
catch (UnauthorizedAccessException)
{
    return 403;
}
catch (IOException)
{
    return 500;
}
finally
{
    temp.Cleanup();
}""",
        )
        + _note("<code>except</code> ≈ <code>catch</code>. Python <code>else</code> on try runs if no exception — C# has no direct equivalent.")
    )


def _with_using_body() -> str:
    return (
        _py_cs(
            "Python <code>with</code> — context manager:",
            """with open(\"data.txt\", encoding=\"utf-8\") as f:
    text = f.read()
# f closed here even on error""",
            "C# <code>using</code> — IDisposable:",
            """using var f = File.OpenText(\"data.txt\");
var text = f.ReadToEnd();
// disposed at end of scope

// Classic:
using (var f = File.OpenText(\"data.txt\"))
{
    var text = f.ReadToEnd();
}""",
        )
        + _note("<code>with open(...) as f</code> ≈ <code>using (var f = ...)</code>. Both guarantee cleanup.")
    )


def _async_await_body() -> str:
    return (
        _py_cs(
            "Python asyncio:",
            """async def fetch():
    await asyncio.sleep(1)
    return \"ok\"

async def main():
    results = await asyncio.gather(fetch(), fetch())""",
            "C# async/await:",
            """async Task<string> FetchAsync()
{
    await Task.Delay(1000);
    return \"ok\";
}

var results = await Task.WhenAll(FetchAsync(), FetchAsync());""",
        )
        + _note("Both use <code>await</code>. Do not call blocking I/O inside Python <code>async def</code> — use async libraries.")
    )


def _venv_nuget_body() -> str:
    return (
        _py_cs(
            "Python — isolated env per project:",
            """python -m venv .venv
.venv\\Scripts\\activate
pip install django
pip freeze > requirements.txt""",
            "C# — NuGet packages per project/solution:",
            """dotnet new webapp
dotnet add package Newtonsoft.Json
# packages stored in project/solution, not global SDK""",
        )
        + _note("<code>venv</code> + <code>pip</code> ≈ per-project NuGet restore. Never install Python libs globally for app projects.")
    )


def _property_body() -> str:
    return (
        _py_cs(
            "Python <code>@property</code> — managed attribute:",
            """class Product:
    def __init__(self):
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError(\"bad\")
        self._price = value""",
            "C# auto-property with validation in setter:",
            """class Product
{
    private decimal _price;
    public decimal Price
    {
        get => _price;
        set => _price = value < 0
            ? throw new ArgumentException(\"bad\")
            : value;
    }
}""",
        )
        + _note("Python <code>@property</code> ≈ C# property get/set. Descriptors are the lower-level mechanism behind <code>@property</code>.")
    )


def _namedtuple_body() -> str:
    return (
        _py_cs(
            "Python <code>namedtuple</code> — lightweight record:",
            """from collections import namedtuple
Point = namedtuple(\"Point\", \"x y\")
p = Point(10, 20)
print(p.x, p.y)""",
            "C# <code>record</code> or <code>readonly struct</code>:",
            """public record Point(int X, int Y);
var p = new Point(10, 20);
Console.WriteLine(p.X);""",
        )
        + _note("namedtuple ≈ small immutable record. For APIs, prefer a Pydantic model or dataclass in modern Python.")
    )


_POPUP_BUILDERS: dict[str, tuple[str, Callable[[], str]]] = {
    "hetero-list": ("C# Comparison — Heterogeneous Lists", _hetero_list_body),
    "tuple-record": ("C# Comparison — Tuple vs ValueTuple", _tuple_body),
    "hashable-keys": ("C# Comparison — Dict Keys / Hashable", _hashable_keys_body),
    "duck-typing": ("C# Comparison — Duck Typing vs Interfaces", _duck_typing_body),
    "indentation": ("C# Comparison — Indentation vs Braces", _indentation_body),
    "dynamic-typing": ("C# Comparison — Dynamic vs Static Typing", _dynamic_typing_body),
    "main-block": ("C# Comparison — __main__ vs Main", _main_block_body),
    "def-order": ("C# Comparison — Script Order vs C# Class", _def_order_body),
    "none-null": ("C# Comparison — None vs null", _none_null_body),
    "is-vs-equals": ("C# Comparison — is vs == vs ReferenceEquals", _is_vs_equals_body),
    "pass-stub": ("C# Comparison — pass vs Empty Block", _pass_stub_body),
    "foreach": ("C# Comparison — for-in vs foreach", _foreach_body),
    "type-hints": ("C# Comparison — Type Hints vs C# Types", _type_hints_body),
    "listcomp-linq": ("C# Comparison — Comprehension vs LINQ", _listcomp_linq_body),
    "lambda-expr": ("C# Comparison — lambda vs =>", _lambda_body),
    "mutable-default": ("C# Comparison — Mutable Default Trap", _mutable_default_body),
    "self-this": ("C# Comparison — self vs this", _self_this_body),
    "init-constructor": ("C# Comparison — __init__ vs Constructor", _init_constructor_body),
    "inheritance": ("C# Comparison — Inheritance", _inheritance_body),
    "yield-return": ("C# Comparison — yield vs yield return", _yield_return_body),
    "decorator-attribute": ("C# Comparison — Decorators vs Attributes", _decorator_body),
    "try-catch": ("C# Comparison — try/except vs try/catch", _try_catch_body),
    "with-using": ("C# Comparison — with vs using", _with_using_body),
    "async-await": ("C# Comparison — async/await", _async_await_body),
    "venv-nuget": ("C# Comparison — venv + pip vs NuGet", _venv_nuget_body),
    "property-csharp": ("C# Comparison — @property vs C# Property", _property_body),
    "namedtuple-record": ("C# Comparison — namedtuple vs record", _namedtuple_body),
}


def render_csharp_popups() -> str:
    parts: list[str] = []
    for popup_id, (title, build_body) in _POPUP_BUILDERS.items():
        body = build_body()
        parts.append(
            f'<div class="csharp-float-win" id="csharp-win-{popup_id}" role="dialog" '
            f'aria-labelledby="csharp-win-title-{popup_id}">'
            f'<div class="csharp-float-hdr">'
            f'<span class="csharp-float-drag" aria-hidden="true">&#8942;&#8942;</span>'
            f'<h4 id="csharp-win-title-{popup_id}">{title}</h4>'
            f'<button type="button" class="csharp-float-close" '
            f'onclick="closeCsharpWin(\'{popup_id}\')" aria-label="Close">&times;</button>'
            f"</div>"
            f'<div class="csharp-float-body">{body}</div>'
            f"</div>"
        )
    return "".join(parts)
