# Slide 30 — C# vs Python Quick Reference

| Concept | C# | Python |
|---------|-----|--------|
| Variable | `int x = 5;` | `x = 5` |
| Print | `Console.WriteLine()` | `print()` |
| Foreach | `foreach (var i in list)` | `for i in list:` |
| Block / braces | `{ }` | Indentation after `:` |
| Empty block (stub) | `{ }` — empty method or if body | `pass` — intentionally empty for now |
| Not implemented yet | `throw new NotImplementedException();` | `raise NotImplementedError()` |
| Class | `class Person { }` | `class Person:` (use `pass` if empty) |
| this / self | `this` (implicit in methods) | `self` (explicit first parameter) |
| Null | `null` — test: `x == null` | `None` — test: `x is None` |
| Equality vs identity | `==` value; `ReferenceEquals` same object | `==` value; `is` same object |
| else if | `else if` | `elif` |
| Boolean | `true` / `false` | `True` / `False` |
| Interface | `interface IRepo { void Save(); }` | ABC or duck typing; empty class: `pass` |
| Exception | `try` / `catch` / `finally` | `try` / `except` / `finally` |
| Throw | `throw new ArgumentException();` | `raise ValueError()` |
| Resource cleanup | `using (var f = File.Open(...))` | `with open(...) as f:` |
| Property | `public int Age { get; set; }` | `@property` decorator |
| String format | `$"Hello {name}"` | `f"Hello {name}"` |
| Namespace / import | `using System.Linq;` | `import os` |
| Entry point | `static void Main()` | `if __name__ == "__main__":` |
| LINQ / collections | `list.Where(x => x > 0)` | `[x for x in lst if x > 0]` |
| Switch / pattern | `switch (x) { case 1: ... }` | `match x: case 1: ...` (3.10+) |
| Package manager | NuGet / `dotnet add package` | `pip` + `requirements.txt` |
| Web API | `[HttpGet]` controller | `@app.get()` FastAPI / DRF |
| Async | `async Task<T>` + `await` | `async def` + `await` (coroutine) |

## pass — no single C# keyword

| Python | C# equivalent | When |
|--------|---------------|------|
| `pass` | `{ }` | Block must exist but do nothing yet |
| `raise NotImplementedError()` | `throw new NotImplementedException()` | Method exists but must not be called yet |
| `class Foo: pass` | `class Foo { }` | Empty class placeholder |
| `def save(): pass` | `void Save() { }` | Empty method stub |

C# interfaces and abstract methods declare without a body — Python uses `pass` inside `class` or `def` instead.

See slide 30 in `PythonTraining.html` for the full table and code examples.
