"""Hand-authored .NET visual guides D01–D24.

Chrome: 1536×1024, slots + panel + svg, unique visual per panel.
Footer C# comparison uses third=\"Interview\".
"""

from __future__ import annotations

from poster_lib import (
    INK,
    MUTED,
    NAVY,
    TBL,
    bullets,
    code_box,
    code_out,
    flow_h,
    flow_v,
    footer3,
    footer_left_code,
    hub,
    log_bars,
    ml,
    note,
    panel,
    pipe_split,
    rect,
    slots,
    stack,
    svg,
    t,
    table,
    terminal,
    vs_boxes,
    wrap,
)


def d01():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w,
            ["Criterion", "Value type", "Reference type"],
            [
                ("Stored", "bits in the variable", "arrow to the heap"),
                ("Copy", "copies the bits", "copies the arrow"),
                ("Examples", "int, bool, small struct", "class, string, List<T>"),
                ("Identity", "equal by value", "equal by object identity"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        hw = (w - 12) / 2
        return (
            rect(x, y, hw, h, fill="#eff6ff", stroke="#2563eb", rx=10)
            + t(x + 10, y + 22, "int a = b", size=13, fill="#1e40af", weight=800)
            + ml(x + 10, y + 48, wrap("Assignment copies the value. Changing a does not change b.", 18, 5), size=12, fill=INK)
            + rect(x + hw + 12, y, hw, h, fill="#f0fdf4", stroke="#16a34a", rx=10)
            + t(x + hw + 22, y + 22, "order = other", size=13, fill="#166534", weight=800)
            + ml(x + hw + 22, y + 48, wrap("Assignment copies the reference. Both names share one mutable object.", 18, 5), size=12, fill=INK)
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Boxing is an allocation, not a cast", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 36, w, ["int 42", "object / iface", "heap box", "GC pressure"])
            + note(x, y + h - 24, w, "Hot loop + List<object> silently boxes every Add.", kind="warn")
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Box every measurement",
            [
                "List<object> values = new();",
                "values.Add(42);  // boxed",
                "Profiler shows allocs, not 'just int'.",
            ],
            "Keep the value typed",
            [
                "List<int> values = new();",
                "values.Add(42);  // no box",
                "Prove with benchmark / allocs.",
            ],
        )

    def p5(x, y, w, h):
        return (
            t(x, y + 6, "Struct only when copy is cheap", size=12, fill=NAVY, weight=800)
            + table(
                x, y + 24, w,
                ["Choose", "When"],
                [
                    ("struct", "small, immutable, value semantics"),
                    ("class", "identity, shared mutation, large payload"),
                    ("record struct", "value equality without class overhead"),
                ],
                header_fill=TBL[1],
                h=h - 24,
            )
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say this",
            footer_left_code(
                ["int n = 42;", "object o = n;  // boxes"],
                ["List<int> values = new();", "values.Add(42);  // no box"],
            ),
            [
                "Name a place boxing or struct size hit a hot path",
                "Prove with profiler or BenchmarkDotNet, not intuition",
            ],
            [
                "Box every measurement in List<object>",
                "Pick struct because it 'feels faster'",
            ],
            [
                ("Value copy", "struct / int assignment", "name copy cost"),
                ("Share state", "class reference", "two names, one object"),
                ("Boxing", "value → object / iface", "alloc — show evidence"),
                ("Struct rule", "small + immutable", "identity → class"),
            ],
            third="Interview",
        )

    return svg(
        "C# Type System",
        "Dotnet · D01  ·  Value vs reference — boxing is an allocation",
        [
            panel(s[0], 1, "Value vs reference", "Copy the bits, or copy the arrow.", p1),
            panel(s[1], 2, "What assignment does", "int copies. A class name shares the object.", p2),
            panel(s[2], 3, "How boxing happens", "int to object (or interface) allocates a box.", p3),
            panel(s[3], 4, "The interview trap", "List<object> boxes every int you Add.", p4),
            panel(s[4], 5, "When a struct is honest", "Small, immutable, value semantics — else class.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Name boxing with evidence, not slogans.", p6),
        ],
    )


def d02():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Declare Where / Select (recipe)", "Enumerate — foreach / Any / Count", "Delegates run against live data"],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w,
            ["", "IEnumerable", "IQueryable"],
            [
                ("Runs", "in-process delegates", "provider (often SQL)"),
                ("Holds", "a recipe over objects", "an expression tree"),
                ("Cost", "CPU in your process", "round trip + plan"),
                ("Watch", "multiple enumeration", "SQL generated twice"),
            ],
            header_fill="#dcfce7",
            last_green=True,
            h=h,
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "var numbers = new List<int> { 1, 2, 3 };",
                "var evens = numbers.Where(n => n % 2 == 0);",
                "numbers.Add(4);",
                'Console.WriteLine(string.Join(",", evens));',
            ],
            "2,4   — query was a recipe, not a snapshot",
            title="deferred — Add happens before enumerate",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Enumerate twice",
            [
                "if (query.Any())",
                "  foreach (var x in query)",
                "Any + foreach = two executions.",
            ],
            "Materialize once",
            [
                "var items = query.ToList();",
                "if (items.Count > 0)",
                "  foreach (var x in items)",
            ],
        )

    def p5(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("LINQ", "operators"),
                ("Recipe", "not results"),
                ("Enumerate", "now it runs"),
            ],
            "ToList snapshot",
            "Re-run on change",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                ["var evens = numbers.Where(...);", "numbers.Add(4);  // still in recipe"],
                ["var items = query.ToList();", "// one execution, stable snapshot"],
            ),
            [
                "Say where it runs: memory vs provider",
                "Watch Any + foreach on an expensive query",
            ],
            [
                "Treat LINQ as frozen results",
                "Enumerate an IQueryable twice 'because it is cached'",
            ],
            [
                ("Deferred", "Where returns recipe", "executes on enumerate"),
                ("IEnumerable", "delegates in-process", "CPU, not SQL"),
                ("IQueryable", "expression tree", "provider translates"),
                ("ToList", "materialize once", "when snapshot is required"),
            ],
            third="Interview",
        )

    return svg(
        "LINQ Execution Internals",
        "Dotnet · D02  ·  A query is a recipe until you enumerate it",
        [
            panel(s[0], 1, "When it actually runs", "Declare stores a recipe. Enumeration executes it.", p1),
            panel(s[1], 2, "Memory vs provider", "IEnumerable runs here. IQueryable often becomes SQL.", p2),
            panel(s[2], 3, "Deferred in one snippet", "Add(4) after Where still appears in the output.", p3),
            panel(s[3], 4, "The interview trap", "Any() then foreach runs the query twice.", p4),
            panel(s[4], 5, "Recipe or snapshot", "ToList when you need one execution.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Name execution site, then enumeration count.", p6),
        ],
    )


def d03():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w,
            ["Keyword", "Direction", "Safe example"],
            [
                ("out", "producer / covariance", "IEnumerable<Dog> as IEnumerable<Animal>"),
                ("in", "consumer / contravariance", "Action<Animal> as Action<Dog>"),
                ("(none)", "invariant", "List<T> — read and write T"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "Producer can widen; List cannot", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["List<Dog>", "IEnumerable<Dog>", "IEnumerable<Animal>"])
            + note(x, y + h - 24, w, "Reading Dog as Animal is safe. Adding a Cat through List<Animal> is not.", kind="star")
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Assume List<T> is covariant",
            [
                "List<Dog> dogs = new();",
                "List<Animal> animals = dogs;",
                "// rejected — would allow Add(Cat)",
            ],
            "Use a producer view",
            [
                "IEnumerable<Animal> animals =",
                "    new List<Dog>();",
                "Safe: you can only read.",
            ],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "IEnumerable<string> words =",
                '    new[] { "safe", "variance" };',
                "IEnumerable<object> objects = words;",
                "Console.WriteLine(objects.Count());",
            ],
            "2   — string is object; you never write through objects",
            title="out T on IEnumerable",
        )

    def p5(x, y, w, h):
        return hub(x, y, w, h, "T", ["out produce", "in consume", "List write", "IEnumerable read"])

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Direction",
            footer_left_code(
                ["IEnumerable<Animal> a =", "    new List<Dog>();  // out"],
                ["// List<Animal> a = dogs;", "// compile error — invariant"],
            ),
            [
                "Explain by direction: produce vs consume",
                "Why List<T> stays invariant — the Cat story",
            ],
            [
                "Recite in/out with no example",
                "Claim List<Dog> is a List<Animal>",
            ],
            [
                ("Generics", "List<T> type-safe", "no casts on the hot path"),
                ("out", "IEnumerable<out T>", "producer may widen"),
                ("in", "Action<in T>", "consumer may narrow"),
                ("Invariant", "List<T>", "read + write both need T"),
            ],
            third="Interview",
        )

    return svg(
        "Generics and Variance",
        "Dotnet · D03  ·  Producers can be covariant. List<T> cannot.",
        [
            panel(s[0], 1, "Three contracts", "out produces. in consumes. List stays invariant.", p1),
            panel(s[1], 2, "The safe widening", "Dogs as animals through IEnumerable — not List.", p2),
            panel(s[2], 3, "The interview trap", "List<Animal> = dogs would let you Add a Cat.", p3),
            panel(s[3], 4, "Covariance you can run", "IEnumerable<object> from strings is a read-only view.", p4),
            panel(s[4], 5, "T in four roles", "Say produce, consume, write, read — then stop.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Direction first. Then the Cat story.", p6),
        ],
    )


def d04():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            ["Domain throws OrderClosedException", "Global handler maps known types", "ProblemDetails + correlation ID"],
            fill="#ffedd5",
            ink="#9a3412",
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Destroy the stack",
            [
                "catch (Exception ex)",
                "{ throw ex; }",
                "Reset stack — ops lose the origin.",
            ],
            "Preserve the stack",
            [
                "catch { throw; }",
                "or catch and wrap with InnerException",
                "bare throw; keeps the trace.",
            ],
        )

    def p3(x, y, w, h):
        return table(
            x, y, w,
            ["Use", "Do not use"],
            [
                ("Exceptional failure", "ordinary validation branching"),
                ("Domain type + data", "one generic Exception everywhere"),
                ("Map once at the boundary", "catch-log-swallow in every method"),
            ],
            header_fill=TBL[4],
            h=h,
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "try {",
                '  throw new InvalidOperationException("order closed");',
                "}",
                "catch (InvalidOperationException ex) {",
                '  Console.WriteLine($"Handled: {ex.Message}");',
                "}",
            ],
            "Handled: order closed",
            title="catch the type you can act on",
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("known domain", "#16a34a", "map to 409 / 422 — log once"),
                ("known infra", "#2563eb", "503 / retryable — no secrets"),
                ("unexpected", "#dc2626", "500 + correlation — hide internals"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Boundary",
            footer_left_code(
                ["catch { throw; }  // keep stack", "// wrap: throw new OrderEx(ex);"],
                ["// global handler → ProblemDetails", "// unexpected: id + 500, log once"],
            ),
            [
                "Throw meaning at the domain; map at the edge",
                "Unexpected: correlation ID, log once, no internals",
            ],
            [
                "throw ex; and call it handling",
                "Catch Exception in every service method",
            ],
            [
                ("Throw", "exceptions for failures", "not if/else flow"),
                ("Custom", "domain exception type", "stable meaning for clients"),
                ("Global", "IExceptionHandler / mw", "one map to ProblemDetails"),
                ("Rethrow", "bare throw;", "preserve the original stack"),
            ],
            third="Interview",
        )

    return svg(
        "Exception Handling Strategy",
        "Dotnet · D04  ·  Throw meaning. Map once. Keep the stack.",
        [
            panel(s[0], 1, "One consistent API error", "Domain throws. Boundary maps. Clients see a contract.", p1),
            panel(s[1], 2, "The interview trap", "throw ex; wipes the stack ops need.", p2),
            panel(s[2], 3, "When to throw at all", "Failures, not validation ifs. Map once, not everywhere.", p3),
            panel(s[3], 4, "Catch what you can handle", "Typed catch at the seam that can recover.", p4),
            panel(s[4], 5, "Three buckets at the edge", "Known domain, known infra, unexpected.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Strategy + global handler + throw;", p6),
        ],
    )


def d05():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Gen 0", "#94a3b8", "short-lived — cheap collect"),
                ("Gen 1", "#3b82f6", "survived one collection"),
                ("Gen 2", "#1d4ed8", "long-lived — expensive pause"),
                ("LOH", "#dc2626", "large objects — fragmentation"),
            ],
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "Survive → promote. Roots keep you old.", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["alloc", "survive G0", "Gen 1 / 2", "dump the root"])
            + note(x, y + h - 24, w, "Heap still high after traffic falls = retained refs, not just churn.", kind="warn")
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Finalizer as cleanup",
            [
                "Wait for GC to close",
                "streams and DB handles.",
                "Timing is not a contract.",
            ],
            "Deterministic dispose",
            [
                "using / await using",
                "Finalizers only for owned",
                "unmanaged resources.",
            ],
        )

    def p4(x, y, w, h):
        return table(
            x, y, w,
            ["Symptom", "Look at", "Fix class"],
            [
                ("High alloc rate", "counters / traces", "reduce churn"),
                ("Heap after GC", "roots / dumps", "drop a retainer"),
                ("Handles / native", "undisposed objects", "using / IDisposable"),
            ],
            header_fill=TBL[0],
            h=h,
        )

    def p5(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("LOH  ≥ ~85KB", "arrays, big strings — separate heap"),
                ("Gen 2  long-lived", "caches, statics, captured this"),
                ("Gen 0  ephemeral", "per-request objects should die here"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Separate three causes",
            footer_left_code(
                ["# allocation rate vs heap after GC", "# vs handle / native counts"],
                ["using var stream = Open();", "// not: wait for the finalizer"],
            ),
            [
                "Split churn, rooted retention, and leaked handles",
                "IDisposable is prompt cleanup — GC is not",
            ],
            [
                "Blame GC without a dump or counter",
                "Use a finalizer as normal resource cleanup",
            ],
            [
                ("Generations", "survive → promote", "long refs age objects"),
                ("LOH", "large alloc path", "pauses + fragmentation"),
                ("Dispose", "using / IAsyncDisposable", "not GC timing"),
                ("Evidence", "counters + dumps", "churn vs root vs handle"),
            ],
            third="Interview",
        )

    return svg(
        "CLR Memory Management",
        "Dotnet · D05  ·  Churn vs roots vs undisposed — prove which one",
        [
            panel(s[0], 1, "Where objects live", "Gen 0 is cheap. Gen 2 and LOH are not.", p1),
            panel(s[1], 2, "Promotion is a root story", "Traffic down, heap still up → something still holds it.", p2),
            panel(s[2], 3, "The interview trap", "GC is not your connection closer.", p3),
            panel(s[3], 4, "Three diagnoses", "Rate, retained heap, handles — different fixes.", p4),
            panel(s[4], 5, "Heap layers you name", "Ephemeral work should not become Gen 2.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Evidence first. Dispose is deterministic.", p6),
        ],
    )


def d06():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 8, "await frees the worker — .Result does not", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 36, w, ["request", "await I/O", "thread free", "resume"])
            + note(x, y + h - 24, w, "Compiler builds a state machine. Blocking holds the thread the continuation needs.", kind="star")
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Block the async call",
            [
                "var result = client",
                "  .GetStringAsync(url).Result;",
                "Starves workers under load.",
            ],
            "Async all the way",
            [
                "var result = await client",
                "  .GetStringAsync(url, ct);",
                "Pass the request token down.",
            ],
        )

    def p3(x, y, w, h):
        return table(
            x, y, w,
            ["Signal", "Means", "You must"],
            [
                ("CancellationToken", "cooperative stop", "pass it; check it"),
                ("Timeout", "time budget expired", "distinct from cancel"),
                ("WhenAll", "parallel I/O", "handle Aggregate / first fail"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p4(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "public async Task<string> GetAsync(",
                "    string url, CancellationToken ct)",
                "{",
                "    using var cts = CancellationTokenSource",
                "        .CreateLinkedTokenSource(ct);",
                "    cts.CancelAfter(TimeSpan.FromSeconds(5));",
                "    return await _http.GetStringAsync(url, cts.Token);",
                "}",
            ],
            title="token + timeout, still await",
        )

    def p5(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("HTTP in", "Kestrel worker"),
                (".Result", "worker stuck"),
                ("await", "worker free"),
            ],
            "continues later",
            "thread-pool starve",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Call chain",
            footer_left_code(
                ["await client.GetStringAsync(url, ct);", "// never .Result / .Wait()"],
                ["await Task.WhenAll(a, b);", "// then inspect faults deliberately"],
            ),
            [
                "Keep the chain async; pass CancellationToken",
                "Name timeout vs cancel vs dependency failure",
            ],
            [
                "Block on .Result because 'it is simpler'",
                "Fire WhenAll and ignore which task faulted",
            ],
            [
                ("State machine", "async method rewrite", "suspend at await"),
                ("No block", "await, not .Result", "workers stay free"),
                ("Cancel", "CancellationToken", "cooperative, not kill"),
                ("Timeout", "CTS.CancelAfter / Polly", "separate from cancel"),
            ],
            third="Interview",
        )

    return svg(
        "Async Await Mechanics",
        "Dotnet · D06  ·  Async all the way — never .Result on the request path",
        [
            panel(s[0], 1, "What await actually does", "Suspend, free the thread, resume on completion.", p1),
            panel(s[1], 2, "The interview trap", ".Result holds the worker the continuation needs.", p2),
            panel(s[2], 3, "Cancel vs timeout vs WhenAll", "Three different failure shapes — name each.", p3),
            panel(s[3], 4, "A method you can defend", "Linked token, explicit budget, still await.", p4),
            panel(s[4], 5, "Why load made it stall", "Blocked workers cannot run the continuation.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Async chain + token + timeout.", p6),
        ],
    )


def d07():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w,
            ["Need", "Pick", "Not"],
            [
                ("I/O composition", "Task / async", "new Thread per call"),
                ("CPU fan-out", "bounded Parallel / TPL", "unbounded Task.Run storm"),
                ("Affinity / loop", "dedicated Thread", "thread-pool for blocking forever"),
            ],
            header_fill=TBL[2],
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Race on ++",
            [
                "Parallel.For(0, 1000,",
                "    _ => count++);",
                "Read-modify-write is not atomic.",
            ],
            "Atomic increment",
            [
                "Parallel.For(0, 1000,",
                "    _ => Interlocked.Increment(ref count));",
                "lock if the invariant is multi-step.",
            ],
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "int count = 0;",
                "Parallel.For(0, 1000,",
                "    _ => Interlocked.Increment(ref count));",
                "Console.WriteLine(count);",
            ],
            "1000   — without Interlocked you will not always get 1000",
            title="shared counter",
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.12, y, w * 0.76,
            ["I/O? → async Task", "Independent CPU? → bounded Parallel", "Shared invariant? → Interlocked / lock"],
            fill="#ede9fe",
            ink="#5b21b6",
            h=h,
        )

    def p5(x, y, w, h):
        return hub(x, y, w, h, "share little", ["Task", "Thread", "Parallel", "Interlocked"])

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Three scenarios",
            footer_left_code(
                ["await http.GetAsync(url, ct);", "// Task — I/O, not new Thread"],
                ["Interlocked.Increment(ref n);", "// lock { multi-step invariant }"],
            ),
            [
                "Pick Task vs Thread vs Parallel with a reason",
                "Minimize shared state; Interlocked vs lock by invariant",
            ],
            [
                "count++ inside Parallel.For",
                "new Thread for every HTTP call",
            ],
            [
                ("Task", "async work + pool", "compose I/O"),
                ("Thread", "affinity / long block", "rare on APIs"),
                ("Parallel", "bounded CPU fan-out", "not fake-sync I/O"),
                ("Interlocked", "simple shared counter", "lock for multi-step"),
            ],
            third="Interview",
        )

    return svg(
        "Threading and TPL",
        "Dotnet · D07  ·  Task for I/O. Parallel for CPU. Interlocked for ++.",
        [
            panel(s[0], 1, "Pick the construct", "Three scenario types — one reason each.", p1),
            panel(s[1], 2, "The interview trap", "++ is a race. Interlocked or lock.", p2),
            panel(s[2], 3, "A counter that adds up", "1000 increments must yield 1000.", p3),
            panel(s[3], 4, "Decision order", "I/O, then CPU, then the shared invariant.", p4),
            panel(s[4], 5, "Share as little as possible", "Name the four tools; prefer isolation.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Right construct + why the counter was wrong.", p6),
        ],
    )


def d08():
    s = slots()

    def p1(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Producers", "write async"),
                ("Bounded channel", "capacity N"),
                ("Workers", "read / complete"),
            ],
            "drain on stop",
            "wait / drop / reject",
        )

    def p2(x, y, w, h):
        return table(
            x, y, w,
            ["At capacity", "Means", "You say"],
            [
                ("Wait", "writer blocks / awaits", "backpressure on producer"),
                ("Drop", "newest or oldest lost", "must be explicit + metric"),
                ("Reject", "write fails / exception", "caller retries or 429"),
            ],
            header_fill="#ffedd5",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Unbounded queue",
            [
                "Queue every item forever.",
                "Spike becomes an OOM.",
                "Overload stays invisible.",
            ],
            "Bounded + policy",
            [
                "Measured capacity.",
                "Wait, reject, or drop — named.",
                "Overload is a signal.",
            ],
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["Complete the writer", "Readers drain remaining items", "Propagate terminal error, do not swallow"],
            fill="#dcfce7",
            ink="#166534",
            h=h,
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("capacity", "#2563eb", "how much memory you will hold"),
                ("writers", "#7c3aed", "single vs multi — Channel options"),
                ("failure", "#dc2626", "retry vs quarantine, still complete"),
                ("shutdown", "#15803d", "complete + drain within budget"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Name four numbers",
            footer_left_code(
                ["var ch = Channel.CreateBounded<Job>(n);", "await ch.Writer.WriteAsync(job, ct);"],
                ["ch.Writer.Complete(errorOrNull);", "await foreach (var j in ch.Reader.ReadAllAsync())"],
            ),
            [
                "Capacity, writer-at-full, worker count, drain on stop",
                "Failed items retry or quarantine — completion still signals",
            ],
            [
                "Hide overload in an unbounded queue",
                "Kill the process with items still in memory, no Complete",
            ],
            [
                ("Channel", "System.Threading.Channels", "async producer/consumer"),
                ("Bounded", "CreateBounded + FullMode", "wait / drop / reject"),
                ("Complete", "Writer.Complete", "readers drain then stop"),
                ("Collection", "ConcurrentQueue", "when sync access fits"),
            ],
            third="Interview",
        )

    return svg(
        "Channels and Backpressure",
        "Dotnet · D08  ·  Bounded capacity makes overload explicit",
        [
            panel(s[0], 1, "The flow you built", "Producers, a cap, workers, and a full-channel policy.", p1),
            panel(s[1], 2, "What 'full' does", "Wait, drop, or reject — pick one and measure it.", p2),
            panel(s[2], 3, "The interview trap", "Unbounded queues turn spikes into outages.", p3),
            panel(s[3], 4, "Shutdown is part of the design", "Complete the writer. Drain. Propagate errors.", p4),
            panel(s[4], 5, "Four things you recite", "Capacity, writers, failure, shutdown.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Bounded channel + named full-mode.", p6),
        ],
    )


def d09():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w,
            ["Thing", "Is", "Raises / runs"],
            [
                ("Delegate", "typed method reference", "you invoke it"),
                ("Event", "restricted multicast", "only the declaring type"),
                ("Expression", "code as a tree", "provider inspects nodes"),
            ],
            header_fill="#f3e8ff",
            h=h,
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "Same lambda, two destinies", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["x => x.Active", "Func runs", "Expression tree", "SQL"])
            + note(x, y + h - 24, w, "IQueryable gets a tree. An arbitrary C# method may not translate.", kind="star")
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Local method as SQL",
            [
                "query.Where(x =>",
                "    MyLocalCheck(x.Name))",
                "Often client-eval or throw.",
            ],
            "Provider-shaped tree",
            [
                "query.Where(x => x.Name.StartsWith(\"A\"))",
                "or ToList() then local filter",
                "if you meant in-memory.",
            ],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "Func<int, int> square = x => x * x;",
                "Action<int> print = value => Console.WriteLine(value);",
                "print(square(5));",
            ],
            "25",
            title="delegate runs; expression would be data",
        )

    def p5(x, y, w, h):
        return hub(x, y, w, h, "lambda", ["Func", "event", "Expression", "IQueryable"])

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Two sentences",
            footer_left_code(
                ["Func<int,int> square = x => x * x;", "button.Click += OnClick;  // event"],
                ["Expression<Func<T,bool>> pred = ...;", "// IQueryable inspects the tree"],
            ),
            [
                "Delegate = run. Event = controlled publish.",
                "IQueryable translates trees — not every method",
            ],
            [
                "Treat every C# method as SQL-translatable",
                "Public event field anyone can invoke",
            ],
            [
                ("Delegate", "Func / Action", "typed callback"),
                ("Event", "event EventHandler", "only owner raises"),
                ("Expression", "Expression<Func<>>", "tree, not IL yet"),
                ("Provider", "IQueryable.Where", "supported nodes only"),
            ],
            third="Interview",
        )

    return svg(
        "Delegates Events Expressions",
        "Dotnet · D09  ·  A lambda can run, or it can be data for SQL",
        [
            panel(s[0], 1, "Three types you unmix", "Delegate runs. Event restricts raise. Expression is a tree.", p1),
            panel(s[1], 2, "Executable vs inspectable", "Func compiles. Expression lets EF look at the nodes.", p2),
            panel(s[2], 3, "The interview trap", "MyLocalCheck inside Where is not a SQL function.", p3),
            panel(s[3], 4, "A delegate you can run", "Func computes. Action prints. That is execution.", p4),
            panel(s[4], 5, "One lambda, four homes", "Know which home you handed it to.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Run vs tree vs event publication.", p6),
        ],
    )


def d10():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["[Audit] is only metadata", "Scanner / filter / serializer reads it", "Framework invokes the real behavior"],
            fill="#dbeafe",
            ink="#1e40af",
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w,
            ["Piece", "Does", "Does not"],
            [
                ("Attribute", "store metadata", "run itself"),
                ("Reflection", "read / invoke members", "replace a hot-path API"),
                ("Cache", "reuse lookup results", "scan every request blindly"),
            ],
            header_fill=TBL[3],
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Attribute executes itself",
            [
                "[Audit] automatically",
                "runs auditing.",
                "Metadata is passive.",
            ],
            "A component must act",
            [
                "A filter provider discovers",
                "[Audit] and invokes audit.",
                "Name who scans, and when.",
            ],
        )

    def p4(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "[AttributeUsage(AttributeTargets.Method)]",
                "public sealed class AuditAttribute : Attribute { }",
                "",
                "// somewhere at startup or first use:",
                "var attrs = method.GetCustomAttributes",
                "    <AuditAttribute>(inherit: true);",
            ],
            title="discover, then act — cache the result",
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("startup scan", "#16a34a", "MVC filters, DI, source generators"),
                ("first use", "#2563eb", "lazy cache per type"),
                ("every call", "#dc2626", "unconstrained GetCustomAttributes"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Name the scanner",
            footer_left_code(
                ["[HttpGet] [Authorize] [Audit]", "// none of these run alone"],
                ["GetCustomAttributes<T>()", "// cache — not on the hot path"],
            ),
            [
                "Who discovers the attribute, when, and what is cached",
                "Reflection is a tool for frameworks, not business loops",
            ],
            [
                "Assume [Audit] executes itself",
                "Scan every request with no cache",
            ],
            [
                ("Attribute", "[Authorize] / [HttpGet]", "passive metadata"),
                ("Reflection", "GetCustomAttributes", "framework reads it"),
                ("Action", "filter / serializer / DI", "turns metadata into policy"),
                ("Cost", "cache lookups", "no hot-path scan"),
            ],
            third="Interview",
        )

    return svg(
        "Reflection and Attributes",
        "Dotnet · D10  ·  Attributes are data. A scanner must act on them.",
        [
            panel(s[0], 1, "Metadata is not behavior", "Something must discover [Audit] and invoke work.", p1),
            panel(s[1], 2, "Three pieces", "Attribute, reflection, cache — different jobs.", p2),
            panel(s[2], 3, "The interview trap", "[Audit] does nothing until a component reads it.", p3),
            panel(s[3], 4, "Discovery looks like this", "GetCustomAttributes, then build policy once.", p4),
            panel(s[4], 5, "When the scan happens", "Startup or first use — never unconstrained per call.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Name the scanner and the cache.", p6),
        ],
    )


def d11():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w,
            ["Type", "Lives", "Use"],
            [
                ("Span<T>", "stack-only view", "sync parse / slice"),
                ("Memory<T>", "heap-storable view", "across await"),
                ("string", "immutable alloc", "when you must own text"),
            ],
            header_fill="#dcfce7",
            last_green=True,
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Optimize from intuition",
            [
                "Rewrite all strings as spans",
                "before measuring.",
                "Readability dies; maybe no win.",
            ],
            "Measure the hot path",
            [
                "Profile first.",
                "Benchmark one representative case.",
                "Then slice that proven path.",
            ],
        )

    def p3(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "ReadOnlySpan<char> line = buffer;",
                "int comma = line.IndexOf(',');",
                "var field = line[..comma];  // no new string",
                "// across await: Memory<byte> instead",
            ],
            title="slice the buffer you already have",
        )

    def p4(x, y, w, h):
        return (
            t(x, y + 8, "Smallest change that you can prove", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["profile", "isolate", "benchmark", "alloc diag"])
            + note(x, y + h - 24, w, "Report time and allocations. Span must still parse correctly.", kind="ok")
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "> dotnet run -c Release --project Parser.Bench",
                "Method        Mean     Alloc",
                "Substring     420 ns   168 B",
                "SpanSlice      38 ns     0 B",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Order of work",
            footer_left_code(
                ["# 1 profile  2 isolate hot path", "# 3 BenchmarkDotNet + allocs"],
                ["ReadOnlySpan<char> field = line[..n];", "// Memory<T> if it must outlive await"],
            ),
            [
                "Profile, then benchmark the smallest honest change",
                "Span for sync slices; Memory across async",
            ],
            [
                "Rewrite the codebase as spans from a hunch",
                "Quote microseconds without allocation numbers",
            ],
            [
                ("Span", "stack-only view", "sync parse/slice"),
                ("Memory", "heap-storable view", "cross await"),
                ("Alloc", "hot path only", "readability still counts"),
                ("Proof", "BenchmarkDotNet", "time + Gen0/alloc"),
            ],
            third="Interview",
        )

    return svg(
        "Allocation Aware C#",
        "Dotnet · D11  ·  Profile first. Span slices buffers — it does not guess.",
        [
            panel(s[0], 1, "Span vs Memory vs string", "Stack view, await-safe view, or a new allocation.", p1),
            panel(s[1], 2, "The interview trap", "Intuition is not a benchmark.", p2),
            panel(s[2], 3, "A cheaper parser", "IndexOf + slice — no substring per field.", p3),
            panel(s[3], 4, "The measured loop", "Profile → isolate → benchmark → allocs.", p4),
            panel(s[4], 5, "What you put on the slide", "Mean and allocated bytes, same input.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Evidence, then Span on that path.", p6),
        ],
    )


def d12():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Inventory projects, NuGet, Windows-only APIs", "Modernize hosting, config, auth", "Validate + staged rollout with rollback"],
            fill="#ffedd5",
            ink="#9a3412",
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Retarget and ship",
            [
                "Only change TargetFramework.",
                "Declare the migration done.",
                "Runtime is where it actually breaks.",
            ],
            "Treat it as a program",
            [
                "Inventory first.",
                "Test seams for auth, config, hosting.",
                "Staged deploy + telemetry + rollback.",
            ],
        )

    def p3(x, y, w, h):
        return table(
            x, y, w,
            ["Area", "What actually breaks"],
            [
                ("Dependencies", "unsupported packages, Windows-only P/Invoke"),
                ("Hosting", "IIS modules vs Kestrel / generic host"),
                ("Auth / config", "web.config, old Identity, machineKey"),
                ("Ops", "deployment, health, serialization, glob"),
            ],
            header_fill=TBL[4],
            h=h,
        )

    def p4(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Rollout  telemetry + rollback", "big-bang TFM switch is not a plan"),
                ("Validate  auth, JSON, culture, HTTP", "production-like, not only unit tests"),
                ("Modernize  host / config / packages", "replace what Framework no longer has"),
                ("Inventory  the real graph", "TFM edit is the smallest line"),
            ],
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Map every project and NuGet — who is Windows-only.",
                "Move configuration off web.config assumptions.",
                "Prove authentication and deployment in a prod-like slot.",
                "Keep a rollback path; watch error rates after cutover.",
            ],
            color="#ea580c",
            max_w=48,
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Not a csproj edit",
            footer_left_code(
                ["# inventory packages + Windows APIs", "# then hosting / config / auth"],
                ["# staged slot + telemetry", "# rollback path before cutover"],
            ),
            [
                "Inventory dependencies before changing TFM",
                "Validate hosting, auth, config, and rollout",
            ],
            [
                "Retarget and declare success",
                "Skip runtime checks because it compiled",
            ],
            [
                ("Inventory", "csproj + NuGet graph", "Windows-only first"),
                ("Host", "Generic Host / Kestrel", "IIS module gaps"),
                ("Config", "IConfiguration / Options", "not web.config alone"),
                ("Rollout", "slots + telemetry", "never big-bang only"),
            ],
            third="Interview",
        )

    return svg(
        "Modern .NET Migration",
        "Dotnet · D12  ·  TFM is the smallest part — deps, host, auth, rollout",
        [
            panel(s[0], 1, "The real sequence", "Inventory, modernize, validate, roll out.", p1),
            panel(s[1], 2, "The interview trap", "Changing TargetFramework is not the migration.", p2),
            panel(s[2], 3, "Where it actually breaks", "Packages, hosting, auth, ops — not the SDK version.", p3),
            panel(s[3], 4, "TFM sits at the bottom", "Operations and compatibility sit on top.", p4),
            panel(s[4], 5, "What you can say you did", "Graph, config, auth proof, rollback.", p5),
            panel(s[5], 6, "Recite, trap & C#", "A program, not a project-file edit.", p6),
        ],
    )


def d13():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("counters", "#2563eb", "live CPU, alloc, GC, exceptions, pool"),
                ("trace", "#7c3aed", "time + stacks — what is hot or blocked"),
                ("dump", "#dc2626", "snapshot: heap, roots, threads, locks"),
            ],
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "Least disruptive evidence that tests the hypothesis", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 36, w, ["symptom", "hypothesis", "counters", "trace / dump"])
            + note(x, y + h - 24, w, "CPU high, logs quiet → counters first, then a focused trace.", kind="star")
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Collect everything",
            [
                "Take large dumps repeatedly",
                "in production.",
                "No question. High cost.",
            ],
            "Question, then tool",
            [
                "Form a hypothesis.",
                "Counters, then trace or dump",
                "with a known ops cost.",
            ],
        )

    def p4(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "$ dotnet-counters monitor -p 4120",
                "cpu-usage  91%   alloc-rate  420 MB/s",
                "$ dotnet-trace collect -p 4120 --duration 00:00:20",
                "# then: dump only if heap / deadlock is the question",
            ],
        )

    def p5(x, y, w, h):
        return table(
            x, y, w,
            ["Question", "Tool"],
            [
                ("Is alloc/GC/CPU the fire?", "dotnet-counters"),
                ("Which stacks are hot?", "dotnet-trace / speedoscope"),
                ("Who holds the object / lock?", "dump + SOS / dotnet-dump"),
            ],
            header_fill=TBL[2],
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Evidence loop",
            footer_left_code(
                ["dotnet-counters monitor -p PID", "# CPU / alloc / GC / threadpool"],
                ["dotnet-trace collect -p PID", "# then dump only for heap/locks"],
            ),
            [
                "Hypothesis → cheapest signal → before/after number",
                "Name what the trace or dump ruled in or out",
            ],
            [
                "Dump production in a loop with no question",
                "Tune from logs that never showed the CPU",
            ],
            [
                ("Counters", "dotnet-counters", "live rates / gauges"),
                ("Trace", "dotnet-trace", "stacks over time"),
                ("Dump", "dotnet-dump / SOS", "heap, roots, locks"),
                ("Method", "hypothesis first", "measure the fix"),
            ],
            third="Interview",
        )

    return svg(
        "Runtime Diagnostics Tools",
        "Dotnet · D13  ·  Hypothesis first — counters, then trace or dump",
        [
            panel(s[0], 1, "Three tools, three jobs", "Live rates, time-based stacks, then a snapshot.", p1),
            panel(s[1], 2, "How you actually start", "Symptom → hypothesis → least painful evidence.", p2),
            panel(s[2], 3, "The interview trap", "A dump is not a personality. It answers a question.", p3),
            panel(s[3], 4, "Commands you can type", "Monitor first. Trace with a duration. Dump last.", p4),
            panel(s[4], 5, "Match tool to question", "CPU vs stacks vs who roots the object.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Evidence in, hypothesis out, post-fix number.", p6),
        ],
    )


def d14():
    s = slots()

    def p1(x, y, w, h):
        return hub(x, y, w, h, "restore", ["direct", "transitive", "pin", "lock file"])

    def p2(x, y, w, h):
        return table(
            x, y, w,
            ["You see", "Means"],
            [
                ("Direct reference", "your csproj asked for it"),
                ("Transitive", "something you use asked for it"),
                ("Conflict / NU1605", "constraints cannot all be true"),
                ("Pin", "direct version to constrain a transitive"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Ignore NU1605",
            [
                "Suppress the warning and ship.",
                "Runtime loads a different bitness",
                "or a breaking transitive.",
            ],
            "Trace the path",
            [
                "Who requested each version.",
                "Align families or pin on purpose.",
                "Verify runtime assets.",
            ],
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["nuget restore resolves the graph", "project.assets.json is the truth", "runtime loads the chosen assets"],
            fill="#dbeafe",
            ink="#1e40af",
            h=h,
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "$ dotnet nuget why Newtonsoft.Json",
                "  Project.Api -> PackageA 13.0.1",
                "  Project.Api -> PackageB -> Newtonsoft.Json 12.0.3",
                "# then align or add a documented pin",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Graph, not hope",
            footer_left_code(
                ["dotnet nuget why Package.Name", "# who pulled this version?"],
                ["# Directory.Packages.props / lock", "# pin only with an owner"],
            ),
            [
                "Inspect the resolved graph and assets file",
                "Pin only when you own the upgrade story",
            ],
            [
                "Suppress NU1605 and ship",
                "Bump a package without checking transitives",
            ],
            [
                ("Graph", "restore + assets.json", "direct + transitive"),
                ("Conflict", "NU1605 / binding", "incompatible constraints"),
                ("Pin", "direct PackageReference", "document ownership"),
                ("Repeat", "CPM + lock file", "same graph on CI"),
            ],
            third="Interview",
        )

    return svg(
        "NuGet Dependency Resolution",
        "Dotnet · D14  ·  The resolved graph is the truth — not your csproj alone",
        [
            panel(s[0], 1, "Restore is a graph", "Direct, transitive, pin, lock — four nouns.", p1),
            panel(s[1], 2, "Words you unmix", "Who asked, who conflicted, who you pinned.", p2),
            panel(s[2], 3, "The interview trap", "A warning is a load failure waiting to happen.", p3),
            panel(s[3], 4, "Where the answer lives", "assets.json, then what the runtime actually loads.", p4),
            panel(s[4], 5, "Trace one package", "nuget why shows the path you must explain.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Path, alignment, verified assets.", p6),
        ],
    )


def d15():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            ["Exception handler (wraps everything)", "Routing selects endpoint + metadata", "Authn → Authz → endpoint / MVC filters"],
            fill="#dbeafe",
            ink="#1e40af",
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w,
            ["Layer", "Runs", "Sees"],
            [
                ("Middleware", "in then unwind out", "the whole server pipeline"),
                ("Routing", "match + metadata", "endpoint for later mw"),
                ("Filters", "MVC / endpoint stages", "not Kestrel itself"),
            ],
            header_fill=TBL[0],
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Handler too late",
            [
                "Register exception mw",
                "after MapControllers.",
                "Downstream faults escape.",
            ],
            "Wrap the pipeline",
            [
                "Exception handling early.",
                "UseAuthorization after routing",
                "so endpoint metadata exists.",
            ],
        )

    def p4(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Kestrel", "HTTP"),
                ("Middleware in", "order registered"),
                ("Endpoint", "your action"),
            ],
            "unwind out",
            "filters around action",
        )

    def p5(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Map / endpoint", "your code + MVC filters"),
                ("UseAuthorization", "needs endpoint metadata"),
                ("UseAuthentication", "sets User"),
                ("UseRouting + exception mw", "match first; errors wrap all"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Trace one request",
            footer_left_code(
                ["app.UseExceptionHandler();", "app.UseRouting();"],
                ["app.UseAuthentication();", "app.UseAuthorization();", "app.MapControllers();"],
            ),
            [
                "Trace Kestrel → exception → route → authn/z → action",
                "Authorization after routing so [Authorize] metadata exists",
            ],
            [
                "Place exception handling after endpoints",
                "Authorize before routing and wonder why it is open",
            ],
            [
                ("Middleware", "UseX() order", "in, then reverse out"),
                ("Routing", "UseRouting / Map", "endpoint metadata"),
                ("Filters", "IActionFilter etc.", "around the action"),
                ("Order", "exception → route → auth", "deliberate, not default luck"),
            ],
            third="Interview",
        )

    return svg(
        "ASP.NET Core Pipeline",
        "Dotnet · D15  ·  Order is a dependency: routing before authorization",
        [
            panel(s[0], 1, "How a request travels", "Exception wrap, then route, then identity, then the action.", p1),
            panel(s[1], 2, "Middleware vs filters", "Pipeline vs MVC stages — do not mix the nouns.", p2),
            panel(s[2], 3, "The interview trap", "Late exception mw and early authz both fail for different reasons.", p3),
            panel(s[3], 4, "In, then unwind out", "Registration order in; reverse on the way out.", p4),
            panel(s[4], 5, "Why [Authorize] was a no-op", "Metadata exists only after routing selected the endpoint.", p5),
            panel(s[5], 6, "Recite, trap & C#", "One order you can draw without stalling.", p6),
        ],
    )


def d16():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Transient", "#16a34a", "new instance every resolve — stateless"),
                ("Scoped", "#2563eb", "one per request / explicit work scope"),
                ("Singleton", "#1e3a5f", "one for the process — must be thread-safe"),
                ("Captive", "#dc2626", "singleton holding scoped — bug"),
            ],
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "DbContext in a singleton",
            [
                "SingletonWorker(AppDbContext db)",
                "One context lives for the app.",
                "Cross-request state + threading.",
            ],
            "Scope per unit of work",
            [
                "Inject IServiceScopeFactory.",
                "CreateScope() per job.",
                "Resolve DbContext inside it.",
            ],
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["BackgroundService is a singleton", "CreateScope for this item", "Resolve scoped services; dispose scope"],
            fill="#fee2e2",
            ink="#b91c1c",
            h=h,
        )

    def p4(x, y, w, h):
        return table(
            x, y, w,
            ["Lifetime", "From"],
            [
                ("Transient", "no state, cheap construct"),
                ("Scoped", "per-request or per-job unit of work"),
                ("Singleton", "shared, thread-safe, no scoped deps"),
            ],
            header_fill=TBL[1],
            h=h,
        )

    def p5(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Captive  singleton → scoped", "the short-lived object is trapped"),
                ("Singleton  process", "safe deps only"),
                ("Scoped  request / job", "DbContext lives here"),
                ("Transient  each resolve", "no captured inner scope"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Worker pattern",
            footer_left_code(
                ["public Worker(IServiceScopeFactory f)", "{ _f = f; }"],
                ["using var scope = _f.CreateScope();", "var db = scope.ServiceProvider", "    .GetRequiredService<AppDbContext>();"],
            ),
            [
                "Choose lifetime from state and concurrency",
                "Singleton workers create a scope per unit of work",
            ],
            [
                "Inject DbContext into a singleton",
                "Make everything Singleton 'for performance'",
            ],
            [
                ("Transient", "AddTransient", "new each resolve"),
                ("Scoped", "AddScoped / HTTP scope", "one DbContext per request"),
                ("Singleton", "AddSingleton", "thread-safe, no scoped deps"),
                ("Captive", "scoped inside singleton", "CreateScope per job"),
            ],
            third="Interview",
        )

    return svg(
        "DI Lifetimes and Captivity",
        "Dotnet · D16  ·  A singleton must not keep a scoped DbContext",
        [
            panel(s[0], 1, "Four words, one is a bug", "Transient, scoped, singleton — captive is the trap.", p1),
            panel(s[1], 2, "The interview trap", "Worker(AppDbContext) captures a request object forever.", p2),
            panel(s[2], 3, "How a hosted service does work", "The service is singleton. The job gets a scope.", p3),
            panel(s[3], 4, "Choose from ownership", "State and threading, not habit.", p4),
            panel(s[4], 5, "Longer must not hold shorter", "That nesting is the captivity rule.", p5),
            panel(s[5], 6, "Recite, trap & C#", "IServiceScopeFactory per unit of work.", p6),
        ],
    )


def d17():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w,
            ["Piece", "Client sees"],
            [
                ("Binding", "route / query / body → model"),
                ("Validation", "field errors at the boundary"),
                ("Versioning", "compatibility + retirement policy"),
                ("ProblemDetails", "stable type, status, trace id"),
            ],
            header_fill="#ffe4e6",
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Arbitrary error strings",
            [
                "return BadRequest(ex.Message);",
                "Shape changes per action.",
                "May leak internals.",
            ],
            "One error contract",
            [
                "Documented ProblemDetails.",
                "Safe detail + trace ID.",
                "Validation and 500 share a shape.",
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Success and error are one design", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["bind", "validate", "handler", "contract"])
            + note(x, y + h - 24, w, "Normalize validation centrally. Map domain exceptions to documented statuses.", kind="ok")
        )

    def p4(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "{",
                '  "type": "https://api/errors/order-closed",',
                '  "title": "Order closed",',
                '  "status": 409,',
                '  "traceId": "00-abc-01"',
                "}",
            ],
            title="machine-readable — no stack in the body",
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("400 validation", "#ea580c", "field-level, safe, same envelope"),
                ("409 / 422 domain", "#2563eb", "documented type URI"),
                ("500 unexpected", "#dc2626", "trace id, log once, hide internals"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Contract pair",
            footer_left_code(
                ["return TypedResults.Problem(", "    statusCode: 409, title: \"Order closed\");"],
                ["// validation → 400 ProblemDetails", "// never return ex.Message as the API"],
            ),
            [
                "Design 2xx and error shapes together",
                "Trace ID for support — no internals in the body",
            ],
            [
                "return BadRequest(ex.Message)",
                "A new JSON error shape per controller",
            ],
            [
                ("Binding", "FromRoute / body", "inputs become models"),
                ("Validation", "DataAnnotations / Fluent", "boundary 400"),
                ("Version", "URL / header policy", "retire old contracts"),
                ("ProblemDetails", "RFC 7807 shape", "stable for clients"),
            ],
            third="Interview",
        )

    return svg(
        "Reliable Web API Contracts",
        "Dotnet · D17  ·  One ProblemDetails envelope — success and errors together",
        [
            panel(s[0], 1, "Four pieces of the contract", "Bind, validate, version, ProblemDetails.", p1),
            panel(s[1], 2, "The interview trap", "ex.Message is not an API. It is a leak.", p2),
            panel(s[2], 3, "How a call is shaped", "Invalid input never reaches the domain as a surprise.", p3),
            panel(s[3], 4, "What the client parses", "type, title, status, traceId — always.", p4),
            panel(s[4], 5, "Three statuses you map", "Validation, domain conflict, unexpected.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Envelope + documented statuses + trace id.", p6),
        ],
    )


def d18():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w,
            ["Choice", "When"],
            [
                ("Tracking", "you will mutate and SaveChanges"),
                ("AsNoTracking", "read-only page / API projection"),
                ("Project / Include", "shape in one round trip"),
                ("Lazy in a loop", "hidden N+1 — almost never"),
            ],
            header_fill="#dcfce7",
            last_green=True,
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Lazy-load inside a loop",
            [
                "foreach (var o in orders)",
                "    Use(o.Customer.Name);",
                "1 + N queries.",
            ],
            "One shaped query",
            [
                "Select new { o.Id, o.Customer.Name }",
                "or Include when you must",
                "materialize the graph.",
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Prove N+1 with command count, then reshape", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 40, w, ["orders SQL", "customer 1", "customer 2", "customer N"])
            + note(x, y + h - 24, w, "Logs or MiniProfiler: one SELECT, then one per row.", kind="warn")
        )

    def p4(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "var rows = await db.Orders.AsNoTracking()",
                "    .Select(o => new OrderRow(",
                "        o.Id, o.Customer.Name, o.Total))",
                "    .ToListAsync(ct);",
            ],
            title="projection — SQL JOIN, no tracker",
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("1 query", "#16a34a", "projected page — the goal"),
                ("1 + Include graph", "#2563eb", "OK when you update the graph"),
                ("1 + N lazy", "#dc2626", "the bug you prove with SQL"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Prove, then reshape",
            footer_left_code(
                ["// SQL log: 1 orders + N customers", "// = N+1"],
                [".AsNoTracking().Select(o => new {", "    o.Id, o.Customer.Name })"],
            ),
            [
                "Prove N+1 with traces, then project or Include on purpose",
                "Tracking is for updates, not every read",
            ],
            [
                "Lazy-load inside a loop",
                "AsNoTracking on an entity you then mutate",
            ],
            [
                ("Track", "default on Save path", "needed to mutate"),
                ("No track", "AsNoTracking", "read-only cheaper"),
                ("Load", "Select / Include", "query count vs payload"),
                ("N+1", "per-row SQL", "reshape the query"),
            ],
            third="Interview",
        )

    return svg(
        "EF Core Query Behavior",
        "Dotnet · D18  ·  Tracking is for writes. N+1 is a measured query count.",
        [
            panel(s[0], 1, "Four loading choices", "Track, don't, project, or accidentally N+1.", p1),
            panel(s[1], 2, "The interview trap", "Customer.Name in a loop is another round trip.", p2),
            panel(s[2], 3, "What N+1 looks like", "One list query, then one query per row.", p3),
            panel(s[3], 4, "The reshape", "Project the DTO. One SQL. No tracker.", p4),
            panel(s[4], 5, "Count the commands", "1 is the goal. 1+N is the bug.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Evidence, then projection.", p6),
        ],
    )


def d19():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 6, "Code + PKCE, then bearer validation", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 28, w, ["SPA", "IdP", "code", "tokens", "API"])
            + note(x, y + h - 24, w, "Decode ≠ trust. Signature, iss, aud, exp still run on the API.", kind="warn")
        )

    def p2(x, y, w, h):
        return table(
            x, y, w,
            ["Noun", "Job"],
            [
                ("Identity", "local users, credentials, account flows"),
                ("OAuth2", "delegate access — defined flows"),
                ("OIDC", "authentication + identity claims on OAuth2"),
                ("JWT checks", "sig, issuer, audience, lifetime, roles"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Trust decoded claims",
            [
                "Read payload roles",
                "without signature validation.",
                "Anyone can mint a JSON blob.",
            ],
            "Validate the bearer",
            [
                "JwtBearer: authority, audience,",
                "signing keys, lifetime.",
                "Then [Authorize] still decides.",
            ],
        )

    def p4(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Login", "redirect / PKCE"),
                ("Tokens", "id + access + refresh"),
                ("API", "JwtBearer"),
            ],
            "Angular Bearer",
            "refresh hidden",
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Trace redirect, code exchange, issuance, API validation.",
                "Name expiry and how refresh is stored (not localStorage).",
                "Authentication is identity. Authorization is still [Authorize].",
                "If the IdP was Entra or IdentityServer, say that — not Cognito.",
            ],
            color="#4f46e5",
            max_w=52,
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "API must check",
            footer_left_code(
                ["AddAuthentication().AddJwtBearer(o => {", "  o.Authority = issuer;", "  o.Audience = clientId; }"],
                ["[Authorize(Roles = \"admin\")]", "// identity ≠ permission"],
            ),
            [
                "Draw login → tokens → bearer validation → expiry",
                "Authn names the user; authz still gates the action",
            ],
            [
                "Trust Base64 claims with no signature check",
                "Call OIDC 'we used JWT' with no issuer",
            ],
            [
                ("Identity", "ASP.NET Identity", "local accounts if you had them"),
                ("OAuth2", "code + PKCE", "delegate access"),
                ("OIDC", "id token + claims", "who logged in"),
                ("JWT", "JwtBearer options", "sig / iss / aud / exp"),
            ],
            third="Interview",
        )

    return svg(
        "Authentication Flow Design",
        "Dotnet · D19  ·  A JWT is trusted only after sig, iss, aud, and exp",
        [
            panel(s[0], 1, "The path you draw", "Browser, IdP, code, tokens, API — then stop.", p1),
            panel(s[1], 2, "Four nouns", "Identity, OAuth2, OIDC, validation — unmix them.", p2),
            panel(s[2], 3, "The interview trap", "jwt.io is not your authorization middleware.", p3),
            panel(s[3], 4, "Where each token goes", "Access on the API. Refresh stays hidden.", p4),
            panel(s[4], 5, "What you recite end to end", "Redirect, PKCE, validation, expiry, authz.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Authority + audience, then [Authorize].", p6),
        ],
    )


def d20():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["appsettings.json (base)", "appsettings.{Env}.json", "environment / vault — last wins"],
            fill="#dbeafe",
            ink="#1e40af",
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w,
            ["Inject", "When"],
            [
                ("IOptions<T>", "singleton-safe snapshot at start"),
                ("IOptionsSnapshot<T>", "scoped — per request, may reload"),
                ("IOptionsMonitor<T>", "singleton + change notifications"),
            ],
            header_fill="#fef3c7",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Commit production secrets",
            [
                "Passwords in appsettings.json.",
                "They land in git and images.",
            ],
            "Inject at runtime",
            [
                "Vault / env / secret store.",
                "Never log the value.",
            ],
        )

    def p4(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Secrets  vault / env", "never source, images, or client config"),
                ("Validate  Fail fast", "block boot if required keys missing"),
                ("Bind  typed Options", "one class per feature"),
                ("Providers  last wins", "JSON < env < command line"),
            ],
        )

    def p5(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "services.AddOptions<SmtpOptions>()",
                "    .Bind(config.GetSection(\"Smtp\"))",
                "    .ValidateDataAnnotations()",
                "    .ValidateOnStart();",
            ],
            title="invalid config fails the deployment, not the first email",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Typed + secret-free",
            footer_left_code(
                ["IOptions<SmtpOptions> opt", "// Snapshot / Monitor by lifetime"],
                ["# secrets: env / KeyVault", "# never appsettings.json or logs"],
            ),
            [
                "Typed options + startup validation",
                "Pick IOptions / Snapshot / Monitor from lifetime",
            ],
            [
                "Store passwords in appsettings.json",
                "IConfiguration[\" magickey\"] sprinkled in services",
            ],
            [
                ("Providers", "JSON + env + argv", "last wins"),
                ("Options", "IOptions<T>", "typed feature settings"),
                ("Validate", "ValidateOnStart", "bad config ≠ boot"),
                ("Secrets", "vault / env", "never git or logs"),
            ],
            third="Interview",
        )

    return svg(
        "Configuration and Options",
        "Dotnet · D20  ·  Typed options. Secrets never in source.",
        [
            panel(s[0], 1, "Precedence is a stack", "JSON, then environment, then command line.", p1),
            panel(s[1], 2, "Three options interfaces", "Start snapshot, per-request, or monitor reloads.", p2),
            panel(s[2], 3, "The interview trap", "appsettings.json is not a secret store.", p3),
            panel(s[3], 4, "How the pieces layer", "Providers, bind, validate, then secrets.", p4),
            panel(s[4], 5, "Fail the boot, not the user", "ValidateOnStart blocks a bad deployment.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Options + vault — never committed secrets.", p6),
        ],
    )


def d21():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w,
            ["Cache", "Share", "Cost"],
            [
                ("IMemoryCache", "this process only", "fast; replica-blind"),
                ("Distributed", "all instances", "network + serialize"),
                ("None", "source of truth", "when consistency forbids cache"),
            ],
            header_fill=TBL[0],
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Cache forever",
            [
                "No expiry, no invalidation.",
                "Stale becomes a second truth",
                "with no owner.",
            ],
            "Bound staleness",
            [
                "TTL, versioned keys,",
                "or explicit removal.",
                "Name outage behavior too.",
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Many misses at once = stampede", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["TTL hits 0", "N replicas miss", "N DB hits", "jitter / lock"])
            + note(x, y + h - 24, w, "Coalesce refresh or add jitter so expiry is not synchronized.", kind="warn")
        )

    def p4(x, y, w, h):
        return hub(x, y, w, h, "entry", ["key shape", "TTL", "invalidate", "stampede"])

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("what", "#2563eb", "one expensive read you measured"),
                ("key", "#7c3aed", "tenant + id + version"),
                ("TTL / event", "#ea580c", "staleness budget + invalidation"),
                ("miss storm", "#dc2626", "singleflight / jitter / lock"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Design, then cache",
            footer_left_code(
                ["_cache.Set(key, dto, ttl);", "// IMemoryCache = this replica"],
                ["await _dist.RemoveAsync(key);", "// or version the key on write"],
            ),
            [
                "Cache only a measured expensive read",
                "Name key, TTL, invalidation, size, stampede, outage",
            ],
            [
                "Cache forever with no owner",
                "IMemoryCache and expect other replicas to see it",
            ],
            [
                ("Memory", "IMemoryCache", "process-local"),
                ("Distributed", "IDistributedCache / Redis", "shared + serialize"),
                ("Invalidate", "TTL / Remove / version", "bound staleness"),
                ("Stampede", "lock / jitter", "one refresh, not N"),
            ],
            third="Interview",
        )

    return svg(
        "Caching and Invalidation",
        "Dotnet · D21  ·  A cache is a second truth — budget staleness on purpose",
        [
            panel(s[0], 1, "Local vs distributed vs none", "Replicas do not share IMemoryCache.", p1),
            panel(s[1], 2, "The interview trap", "No TTL is not a strategy.", p2),
            panel(s[2], 3, "Expiry can stampede", "Aligned TTLs turn one miss into a DB incident.", p3),
            panel(s[3], 4, "Four fields of the design", "Key, TTL, invalidation, stampede protection.", p4),
            panel(s[4], 5, "Say it in this order", "What, key, staleness, miss behavior.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Measured read + bounded staleness.", p6),
        ],
    )


def d22():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Request enqueues durable work", "BackgroundService consumes with CT", "Ack / checkpoint only after success"],
            fill="#dcfce7",
            ink="#166534",
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Fire and forget",
            [
                "_ = ProcessOrderAsync(order);",
                "Deploy kills the task.",
                "No retry, no ack.",
            ],
            "Supervised consumer",
            [
                "Enqueue durable work.",
                "Hosted worker owns retry,",
                "poison, and shutdown drain.",
            ],
        )

    def p3(x, y, w, h):
        return table(
            x, y, w,
            ["Moment", "You designed"],
            [
                ("Mid-item crash", "idempotent retry from checkpoint"),
                ("Poison message", "bounded retries then quarantine"),
                ("SIGTERM / stop", "cancel, drain, persist in budget"),
            ],
            header_fill=TBL[5],
            h=h,
        )

    def p4(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("HTTP", "202 + id"),
                ("Queue", "durable"),
                ("Worker", "scope + CT"),
            ],
            "success ack",
            "retry / DLQ",
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Work is durable or it is not — say which.",
                "Create a DI scope per item; observe cancellation.",
                "Retry only safe, idempotent operations.",
                "Shutdown: stop accepting, drain or persist, then exit.",
            ],
            color="#15803d",
            max_w=50,
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Owned by the host",
            footer_left_code(
                ["protected override async Task ExecuteAsync(", "    CancellationToken stoppingToken)"],
                ["// enqueue from the API", "// never _ = ProcessAsync(order);"],
            ),
            [
                "Explain crash mid-item: ack, retry, poison",
                "Worker creates scopes and honors shutdown CT",
            ],
            [
                "Start unobserved request work with _ =",
                "Ignore cancellation and die mid-write",
            ],
            [
                ("Hosted", "BackgroundService", "CT from the host"),
                ("Queue", "Channel / SB / SQS", "latency ≠ work"),
                ("Failure", "idempotent retry", "poison after N"),
                ("Stop", "stoppingToken", "drain in the budget"),
            ],
            third="Interview",
        )

    return svg(
        "Reliable Background Work",
        "Dotnet · D22  ·  Durable queue + hosted consumer — not fire-and-forget",
        [
            panel(s[0], 1, "Request is not the worker", "Enqueue, consume with a token, ack after success.", p1),
            panel(s[1], 2, "The interview trap", "_ = ProcessAsync dies on deploy with no trace.", p2),
            panel(s[2], 3, "Failure is a designed path", "Crash, poison, shutdown — three answers.", p3),
            panel(s[3], 4, "HTTP returns; work continues", "202 to the client. Worker owns the rest.", p4),
            panel(s[4], 5, "What you say about a crash", "Durable, scoped, cancelled, idempotent.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Hosted service, not an unobserved task.", p6),
        ],
    )


def d23():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("E2E  few", "real user path, expensive"),
                ("Integration  HTTP / DB seam", "WebApplicationFactory"),
                ("Unit  business rules", "fast, no infrastructure"),
            ],
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Mock the implementation",
            [
                "Verify every internal",
                "method call.",
                "Refactor breaks tests; bugs hide.",
            ],
            "Assert observable behavior",
            [
                "Status + contract + data.",
                "Mock only external boundaries",
                "or true nondeterminism.",
            ],
        )

    def p3(x, y, w, h):
        return table(
            x, y, w,
            ["Layer", "Proves"],
            [
                ("Unit", "rules, mapping, branching"),
                ("Double", "boundary you do not own"),
                ("Integration", "routing, DI, mw, JSON, DB"),
                ("Factory", "the app over real HTTP"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p4(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "public class ApiTests : IClassFixture<WebApplicationFactory<Program>>",
                "{",
                "    [Fact]",
                "    public async Task Order_returns_409_when_closed()",
                "    {",
                "        var c = _factory.CreateClient();",
                "        var r = await c.PostAsJsonAsync(\"/orders\", body);",
                "        Assert.Equal(HttpStatusCode.Conflict, r.StatusCode);",
                "    }",
                "}",
            ],
            title="HTTP in, contract out — isolated data",
        )

    def p5(x, y, w, h):
        return (
            t(x, y + 8, "The unit test that lied", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["HTTP", "routing", "DI", "serialize"])
            + note(x, y + h - 24, w, "Controller unit tests can pass while routing and JSON are broken.", kind="warn")
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "One real HTTP test",
            footer_left_code(
                ["var client = factory.CreateClient();", "var res = await client.PostAsJsonAsync(...);"],
                ["Assert.Equal(409, (int)res.StatusCode);", "// + ProblemDetails type"],
            ),
            [
                "Unit for rules; integration for seams; few E2E",
                "WebApplicationFactory: HTTP, isolated data, status + contract",
            ],
            [
                "Mock every internal collaborator",
                "Ship with only controller tests and no HTTP",
            ],
            [
                ("Unit", "xUnit facts", "deterministic rules"),
                ("Double", "Moq / NSubstitute", "external boundary only"),
                ("Integration", "Testcontainers / SQL", "components that must agree"),
                ("Factory", "WebApplicationFactory", "real pipeline over HTTP"),
            ],
            third="Interview",
        )

    return svg(
        "Layered .NET Testing",
        "Dotnet · D23  ·  Unit the rules. HTTP-test the pipeline. Mock the edge.",
        [
            panel(s[0], 1, "Three layers, different jobs", "Fast rules, then seams, then a few real paths.", p1),
            panel(s[1], 2, "The interview trap", "Verifying internals locks the design and misses bugs.", p2),
            panel(s[2], 3, "What each layer is for", "If routing can break it, a unit test will not see it.", p3),
            panel(s[3], 4, "An integration test you can defend", "POST, isolated data, assert status and body.", p4),
            panel(s[4], 5, "Why the controller test passed", "The lie lived in routing, DI, and serialization.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Observable behavior + one Factory test.", p6),
        ],
    )


def d24():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("logs", "#64748b", "why THIS request — structured + scope"),
                ("metrics", "#2563eb", "how many hurt — rate, error, duration"),
                ("traces", "#4f46e5", "which hop was slow — one path"),
                ("health", "#15803d", "liveness vs readiness — cheap checks"),
            ],
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "One ID ties the three signals", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["request", "trace", "span / SQL", "structured log"])
            + note(x, y + h - 24, w, "Alert names the symptom. Trace + log explain this correlation ID.", kind="star")
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Log only prose",
            [
                "logger.LogInformation(",
                "    $\"Order {id} failed\");",
                "Cannot filter or correlate.",
            ],
            "Structured properties",
            [
                "logger.LogInformation(",
                "    \"Order {OrderId} failed\", id);",
                "OrderId is a field, not text.",
            ],
        )

    def p4(x, y, w, h):
        return table(
            x, y, w,
            ["Check", "Means", "Must be"],
            [
                ("Liveness", "process should be restarted", "cheap, no deps"),
                ("Readiness", "ready for traffic", "deps you actually need"),
            ],
            header_fill="#dcfce7",
            last_green=True,
            h=h,
        )

    def p5(x, y, w, h):
        return hub(x, y, w, h, "corr-id", ["log", "metric", "trace", "alert"])

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Three signals + health",
            footer_left_code(
                ['logger.LogInformation("Order {OrderId} failed", id);', "// never $\"Order {id}\""],
                ["# dashboards: RPS / errors / p95", "# health ≠ telemetry"],
            ),
            [
                "Name SLIs, dashboards, and one alert you would add",
                "Correlate logs, metrics, traces with one ID",
            ],
            [
                "Log interpolated strings only",
                "Treat /health as a substitute for metrics",
            ],
            [
                ("Logs", "ILogger + scopes", "fields, not secrets"),
                ("Metrics", "meters / OTel", "rate error duration"),
                ("Traces", "Activity / OTel", "hop-by-hop path"),
                ("Health", "liveness / ready", "orchestrator, not APM"),
            ],
            third="Interview",
        )

    return svg(
        "Logs Metrics and Traces",
        "Dotnet · D24  ·  One correlation ID — structured logs, not prose",
        [
            panel(s[0], 1, "Four signals", "Logs explain. Metrics count. Traces locate. Health is cheap.", p1),
            panel(s[1], 2, "How an alert becomes a story", "Trace id on the span, the SQL, and the error log.", p2),
            panel(s[2], 3, "The interview trap", "Interpolation is a sentence. Templates are fields.", p3),
            panel(s[3], 4, "Liveness is not readiness", "Restart vs traffic — different questions.", p4),
            panel(s[4], 5, "The id in the middle", "Logs, metrics, traces, and the alert share it.", p5),
            panel(s[5], 6, "Recite, trap & C#", "Structured ILogger + OTel + health split.", p6),
        ],
    )


BUILDERS = [
    ("D01", "C# Type System", d01),
    ("D02", "LINQ execution internals", d02),
    ("D03", "Generics and variance", d03),
    ("D04", "Exception handling strategy", d04),
    ("D05", "CLR memory management", d05),
    ("D06", "Async/await mechanics", d06),
    ("D07", "Threading and TPL", d07),
    ("D08", "Channels and backpressure", d08),
    ("D09", "Delegates events expressions", d09),
    ("D10", "Reflection and attributes", d10),
    ("D11", "Allocation-aware C#", d11),
    ("D12", "Modern .NET migration", d12),
    ("D13", "Runtime diagnostics tools", d13),
    ("D14", "NuGet dependency resolution", d14),
    ("D15", "ASP.NET Core pipeline", d15),
    ("D16", "DI lifetimes and captivity", d16),
    ("D17", "Reliable web API contracts", d17),
    ("D18", "EF Core query behavior", d18),
    ("D19", "Authentication flow design", d19),
    ("D20", "Configuration and options", d20),
    ("D21", "Caching and invalidation", d21),
    ("D22", "Reliable background work", d22),
    ("D23", "Layered .NET testing", d23),
    ("D24", "Logs metrics and traces", d24),
]
