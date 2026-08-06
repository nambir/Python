"""Handcrafted rich slides that override catalog-generated bodies (D01, D06)."""

from __future__ import annotations

from slide_code import code
from slide_diagrams import compare, cycle, flow
from slide_io import io_split
from training_meta import _def

# --- Diagrams (shared helpers) ---


def _memory_picture() -> str:
    return """
<h3>Picture — where the data lives</h3>
<p class="fc-kid-hint">Value types keep the bits <b>in the variable</b>. Reference types keep a <b>pointer</b>; the object is on the heap.</p>
<div class="cdiag cdiag-compare" style="align-items:stretch">
  <div class="cdiag-compare-col" style="background:#eff6ff;border:1.5px solid #93c5fd;border-radius:8px;padding:10px 12px">
    <h4 style="color:#1d4ed8;margin:0 0 8px">Value type — <code>int a = 10</code></h4>
    <div style="font-family:Consolas,monospace;font-size:12px;line-height:1.6;background:#fff;border-radius:6px;padding:8px 10px;border:1px solid #bfdbfe">
      <b>STACK / inline</b><br>
      ┌─────────────┐<br>
      │  a  │  10   │  ← value lives here<br>
      └─────────────┘<br>
      ┌─────────────┐<br>
      │  b  │  10   │  ← copy of 10<br>
      └─────────────┘<br>
      <span style="color:#166534">b = 99 → only b changes</span>
    </div>
  </div>
  <div class="cdiag-compare-vs">vs</div>
  <div class="cdiag-compare-col" style="background:#fdf2f8;border:1.5px solid #f9a8d4;border-radius:8px;padding:10px 12px">
    <h4 style="color:#9d174d;margin:0 0 8px">Reference type — <code>var r = new[]&#123;1,2&#125;</code></h4>
    <div style="font-family:Consolas,monospace;font-size:12px;line-height:1.6;background:#fff;border-radius:6px;padding:8px 10px;border:1px solid #fbcfe8">
      <b>STACK</b> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>HEAP</b><br>
      ┌──────┐ &nbsp;&nbsp;&nbsp; ┌──────────┐<br>
      │ r1 ●─┼───────▶│ [1, 2]   │<br>
      └──────┘ &nbsp;&nbsp;&nbsp; └──────────┘<br>
      ┌──────┐ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;▲<br>
      │ r2 ●─┼───────────────┘  same object<br>
      └──────┘<br>
      <span style="color:#9d174d">r2[0]=99 → r1 also sees 99</span>
    </div>
  </div>
</div>
<p class="flow-note"><b>One-line memory:</b> value = copy the number · reference = copy the arrow (both arrows can point at one box).</p>
"""


def _boxing_flow() -> str:
    return flow(
        "Boxing in one glance",
        [
            ("value on stack", "int n = 7"),
            ("box → heap", "object o = n"),
            ("unbox back", "int m = (int)o"),
        ],
        note="Boxing allocates. Prefer List&lt;int&gt; over old ArrayList of ints.",
    )


def _async_cycle() -> str:
    return cycle(
        "async/await timeline (easy mental model)",
        [
            ("1. Run", "method starts on a thread"),
            ("2. await", "release the thread — wait for I/O"),
            ("3. Ready", "Task completes (result arrived)"),
            ("4. Resume", "continue after await"),
        ],
        note="Not “new OS thread per call” — just don’t hold the thread while waiting.",
    )


RICH: dict[str, dict] = {
    "D01": {
        "title": "C# Type System",
        "meta": {
            "definition": _def(
                "By default you think of a variable as “holding data.” In C# that is only true for "
                "<b>value types</b>. A <b>reference type</b> variable holds an <b>arrow</b> to an object "
                "on the heap — so two variables can point at the same box.",
                [
                    "<b>Value types:</b> <code>int</code>, <code>bool</code>, <code>struct</code>, "
                    "<code>enum</code> — assignment <b>copies</b> the bits.",
                    "<b>Reference types:</b> <code>class</code>, arrays, <code>delegate</code> — "
                    "assignment copies the <b>reference</b> (same object).",
                    "<b>Boxing:</b> wrapping a value in <code>object</code> moves it to the heap — "
                    "allocation; avoid in hot loops.",
                    "<b>struct vs class:</b> small immutable value → <code>struct</code>; "
                    "identity / inheritance / large mutable state → <code>class</code>.",
                ],
            ),
            "interview": (
                "Value types copy on assign; reference types copy the pointer so both names can "
                "see the same object. Boxing puts a value on the heap as object — I avoid it on "
                "hot paths and prefer generics. I pick struct for small immutable values like "
                "Point or Money, and class when I need identity or inheritance."
            ),
            "skill_id": "D01",
            "area": "D1 — C# Core",
        },
        "learn": """
<p>Skill matrix <b>D01</b> — value vs reference types, boxing, struct vs class.</p>
<h3>Quick reference</h3>
<table class="data-tbl">
<tr><th>Kind</th><th>Examples</th><th>Stored as</th></tr>
<tr><td>Value</td><td><code>int</code>, <code>bool</code>, <code>struct</code>, <code>enum</code></td><td>Inline / stack</td></tr>
<tr><td>Reference</td><td><code>class</code>, <code>string</code>, arrays</td><td>Reference → heap object</td></tr>
</table>
<h3>Common mistakes</h3>
<div class="mistake-box"><span class="mistake-title">&#10060; Mistake 1 &mdash; assuming assignment always copies data</span>
<span class="mistake-desc">For reference types, <code>=</code> copies the <b>reference</b>, not the object.</span>
<div class="mc-row"><div class="mc-col mc-bad"><span class="mc-lbl">&#10060; Bug</span><div class="step-pre">var a = new List&lt;int&gt; { 1 };
var b = a;
b.Add(2);
// a now has 2 items — surprise!</div></div>
<div class="mc-col mc-good"><span class="mc-lbl">&#10004; Fix</span><div class="step-pre">var b = new List&lt;int&gt;(a);  // new list
// or a.ToList()</div></div></div></div>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> <code>this</code> in a method refers to?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">The <b>current instance</b> (the object the method was called on). Same idea as Python <code>self</code> &mdash; C# passes it automatically; use <code>this.Name</code> when you need to be explicit.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What is <code>a</code> after this?
<div class="step-pre">int a = 10;
int b = a;
b = 99;</div>
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><code>10</code> &mdash; value types copy the value. Changing <code>b</code> does not change <code>a</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> What is boxing?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Wrapping a value type in <code>object</code> (or an interface) on the <b>heap</b> &mdash; allocation + copy. Prefer generics like <code>List&lt;int&gt;</code> to avoid it.</div>
    </details>
  </div>
</div>
"""
        + code(
            """// Runnable demo — value vs reference + boxing
// (top-level statements — paste into SharpLab and Run)

int x = 1, y = x;
y = 5;
Console.WriteLine($"value copy: x={x}, y={y}");

var r1 = new[] { 1, 2 };
var r2 = r1;          // same array
r2[0] = 99;
Console.WriteLine($"reference: r1[0]={r1[0]}, r2[0]={r2[0]}");

int n = 7;
object o = n;         // boxing
int m = (int)o;       // unboxing
Console.WriteLine($"boxed then unboxed: {m}");""",
            expected=(
                "value copy: x=1, y=5\n"
                "reference: r1[0]=99, r2[0]=99\n"
                "boxed then unboxed: 7"
            ),
        ),
        "practice": """
<ul class="checklist">
  <li>Explain value vs reference with one list example</li>
  <li>Name one boxing scenario and how to avoid it</li>
  <li>Pick struct vs class for a Money / Point type</li>
</ul>
<a class="file-link" href="Skill_Depth_Matrix_I25054_Sangeetha_Rajendiran_9.csv">Skill matrix CSV</a>
""",
        "beginner": {
            "steps": [
                {
                    "title": "Step 1 — Value type vs reference type",
                    "body": (
                        "A <b>value type</b> variable holds the bits of the value itself. "
                        "A <b>reference type</b> variable holds a pointer to an object on the heap."
                        + io_split(
                            "int a = 10;\n"
                            "int b = a;     // copy the value\n"
                            "b = 99;\n"
                            "Console.WriteLine(a);  // 10\n"
                            "\n"
                            "var list1 = new List<int> { 1, 2 };\n"
                            "var list2 = list1;   // copy REFERENCE\n"
                            "list2.Add(3);\n"
                            "Console.WriteLine(list1.Count);  // 3",
                            {4: "10", 9: "3"},
                        )
                        + '<p class="step-result"><b>Takeaway:</b> value = copy the number · '
                        "reference = copy the arrow (both can point at one box).</p>"
                    ),
                },
                {
                    "title": "Step 2 — Boxing and unboxing",
                    "body": (
                        "<b>Boxing</b> stores a value type inside an <code>object</code> on the heap. "
                        "It allocates and copies — fine occasionally, expensive in a hot loop."
                        + io_split(
                            "int n = 42;\n"
                            "object boxed = n;        // boxing — heap alloc\n"
                            "int back = (int)boxed;   // unboxing\n"
                            "Console.WriteLine(back);",
                            {4: "42"},
                        )
                        + '<p class="step-result"><b>Level-3 answer:</b> name a place boxing hurt '
                        "performance (e.g. <code>ArrayList</code> of ints) and what you changed "
                        "(prefer <code>List&lt;int&gt;</code>).</p>"
                    ),
                },
                {
                    "title": "Step 3 — struct vs class",
                    "body": (
                        "Use <code>struct</code> for small, immutable, logical-value data; "
                        "<code>class</code> when you need identity, inheritance, or large mutable state."
                        + io_split(
                            "readonly struct Money\n"
                            "{\n"
                            "    public decimal Amount { get; }\n"
                            "    public string Currency { get; }\n"
                            "    public Money(decimal amount, string currency) =>\n"
                            "        (Amount, Currency) = (amount, currency);\n"
                            "}\n"
                            "\n"
                            "var fee = new Money(9.99m, \"USD\");\n"
                            "var copy = fee;   // value copy\n"
                            "Console.WriteLine(copy.Amount);\n"
                            "\n"
                            "class Order { public int Id { get; set; } }\n"
                            "var o1 = new Order { Id = 1 };\n"
                            "var o2 = o1;      // same object\n"
                            "o2.Id = 99;\n"
                            "Console.WriteLine(o1.Id);  // 99 — shared",
                            {11: "9.99", 17: "99"},
                        )
                        + '<p class="step-result"><b>Takeaway:</b> when unsure, start with '
                        "<code>class</code>; switch to <code>struct</code> only when value semantics are clear.</p>"
                    ),
                },
            ],
            "interview_qa": [
                {
                    "q": "What is boxing?",
                    "a": "Converting a value type to <code>object</code> or an interface it implements — "
                    "allocates on the heap and copies the value. Unboxing casts back and copies again.",
                },
                {
                    "q": "When would you choose struct over class?",
                    "a": "Small immutable value semantics (coordinates, money amount+currency), "
                    "no inheritance needed, want stack allocation / fewer heap objects.",
                },
            ],
        },
        "flow": (
            "I need to model this data in C#",
            "Pick value type, reference type, struct, or class",
            [
                (
                    "Is it small, fixed, and logically a value (Point, Money, Date)?",
                    "Use struct",
                    "Copied by value — no identity. Stack-friendly, immutable is best.",
                    ["readonly struct Point", "readonly struct Money"],
                    "key",
                ),
                (
                    "Do you need inheritance, identity, or large mutable state?",
                    "Use class",
                    "Reference type — variable holds a pointer to one object on the heap.",
                    ["class Order", "class Customer"],
                    "dd",
                ),
                (
                    "Are value types going into object or non-generic collections?",
                    "Watch boxing",
                    "Value → object allocates on heap. Prefer generics: List<int> not ArrayList.",
                    ["List<int>", "avoid ArrayList"],
                    "cm",
                ),
            ],
            "Default",
            "When unsure, start with class — switch to struct only when value semantics are clear.",
            ["class by default"],
        ),
        "diagram": (
            _memory_picture()
            + compare(
                "Quick pick",
                (
                    "Use value / struct when…",
                    [
                        "Small fixed data (Point, Money)",
                        "Copying is OK / wanted",
                        "No inheritance needed",
                    ],
                ),
                (
                    "Use class when…",
                    [
                        "Identity / mutable state",
                        "Inheritance or large object",
                        "Many references should share one instance",
                    ],
                ),
                note="When unsure → start with class.",
            )
            + _boxing_flow()
        ),
    },
    "D06": {
        "title": "Async / Await",
        "meta": {
            "definition": _def(
                "By default a method is <b>synchronous</b> — it holds the thread until it finishes. "
                "Add the <code>async</code> keyword so the method can <b>release the thread</b> "
                "while waiting; when the result is ready, work <b>resumes</b> (often on a thread-pool thread).",
                [
                    "<b>Normal method:</b> sync — thread stays busy until the method returns.",
                    "<b>Make it async:</b> put <code>async</code> on the method and use "
                    "<code>await</code> where you wait (HTTP, DB, file).",
                    "<b>Why:</b> <code>await</code> frees the thread during the wait so other work "
                    "can run; when the Task completes, the method continues after <code>await</code>.",
                    "<b>Not a new OS thread per call</b> — it is about not blocking while waiting.",
                ],
            ),
            "interview": (
                "Methods are sync by default. I add async so the method can await I/O and release "
                "the thread while waiting; when the Task completes, execution resumes. I never block "
                "with .Result or .Wait() — I await end-to-end and pass CancellationToken."
            ),
            "skill_id": "D06",
            "area": "D1 — C# Core",
        },
        "learn": """
<p>Skill matrix <b>D06</b> — start from basics: sync method → <code>async</code> keyword → release thread → resume.</p>
<h3>Big picture</h3>
<table class="data-tbl">
<tr><th>Step</th><th>What happens</th></tr>
<tr><td>1. Sync method (default)</td><td>Thread stays busy until the method finishes</td></tr>
<tr><td>2. Add <code>async</code></td><td>Method may use <code>await</code>; return type is <code>Task</code> / <code>Task&lt;T&gt;</code></td></tr>
<tr><td>3. Hit <code>await</code></td><td><b>Release</b> the thread while waiting for I/O</td></tr>
<tr><td>4. Result ready</td><td>Method <b>resumes</b> after <code>await</code> (takes a thread again)</td></tr>
</table>
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> Are methods async by default?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No — methods are <b>sync</b> by default. You add the <code>async</code> keyword to allow <code>await</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> What does <code>await</code> do to the thread?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">It <b>releases</b> the thread while waiting. When the Task completes, the method continues after <code>await</code>.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Does <code>async</code> create a new OS thread every call?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">No — it is about not blocking while waiting, not spawning a thread per call.</div>
    </details>
  </div>
</div>
"""
        + code(
            """// Runnable demo — sync wait vs async await
// Paste into SharpLab and Run

using System.Diagnostics;

// SYNC style — blocks the thread while "waiting"
string FetchSync()
{
    // Simulate slow work that holds the thread
    Thread.Sleep(300);
    return "sync-done";
}

// ASYNC — await releases the thread during the wait
async Task<string> FetchAsync()
{
    await Task.Delay(300);   // wait without blocking this thread
    return "async-done";
}

var sw = Stopwatch.StartNew();
Console.WriteLine(FetchSync());
Console.WriteLine($"sync waited {sw.ElapsedMilliseconds} ms (thread held)");

sw.Restart();
Console.WriteLine(await FetchAsync());
Console.WriteLine($"async waited {sw.ElapsedMilliseconds} ms (thread released during Delay)");""",
            expected=(
                "sync-done\n"
                "sync waited ~300 ms (thread held)\n"
                "async-done\n"
                "async waited ~300 ms (thread released during Delay)"
            ),
        ),
        "practice": """
<ul class="checklist">
  <li>Convert one sync method to <code>async Task</code> with <code>await</code></li>
  <li>Explain: release thread at await → resume when result ready</li>
  <li>Find and remove one <code>.Result</code> / <code>.Wait()</code></li>
</ul>
""",
        "beginner": {
            "steps": [
                {
                    "title": "Step 1 — Normal methods are sync",
                    "body": (
                        "By default a method is <b>synchronous</b>. The thread that calls it "
                        "<b>stays busy</b> until the method returns — even if it is only waiting."
                        + io_split(
                            "// SYNC — no async keyword; thread held while waiting\n"
                            "string FetchSync()\n"
                            "{\n"
                            "    Thread.Sleep(200);          // blocks this thread\n"
                            "    return \"sync-done\";\n"
                            "}\n"
                            "\n"
                            "Console.WriteLine(FetchSync());",
                            {8: "sync-done"},
                        )
                        + '<p class="step-result"><b>Problem:</b> while waiting, that thread cannot '
                        "do other useful work.</p>"
                    ),
                },
                {
                    "title": "Step 2 — Add <code>async</code> to make the method async",
                    "body": (
                        "To wait without blocking, add the <code>async</code> keyword and use "
                        "<code>await</code>. Return type becomes <code>Task</code> / "
                        "<code>Task&lt;T&gt;</code>."
                        + io_split(
                            "// ASYNC — keyword async + await\n"
                            "async Task<string> FetchAsync()\n"
                            "{\n"
                            "    await Task.Delay(200);      // release thread while waiting\n"
                            "    return \"async-done\";\n"
                            "}\n"
                            "\n"
                            "Console.WriteLine(await FetchAsync());",
                            {8: "async-done"},
                        )
                        + "<table class=\"data-tbl\" style=\"margin:6px 0;font-size:12px\">"
                        "<tr><th>Part</th><th>Meaning</th></tr>"
                        "<tr><td><code>async</code></td>"
                        "<td>This method may use <code>await</code></td></tr>"
                        "<tr><td><code>await</code></td>"
                        "<td>Wait here — but <b>release the thread</b> while waiting</td></tr>"
                        "<tr><td><code>Task&lt;string&gt;</code></td>"
                        "<td>Promise of a string later</td></tr>"
                        "</table>"
                    ),
                },
                {
                    "title": "Step 3 — Release thread → result ready → resume",
                    "body": (
                        "That is the whole point of <code>async</code>/<code>await</code>:"
                        "<ol style=\"margin:6px 0 8px 18px;font-size:12px;line-height:1.55\">"
                        "<li>Method runs until it hits <code>await</code>.</li>"
                        "<li><b>Release:</b> thread is free while I/O / delay runs.</li>"
                        "<li><b>Result ready:</b> Task completes.</li>"
                        "<li><b>Resume:</b> continue after <code>await</code>.</li>"
                        "</ol>"
                        + io_split(
                            "Console.WriteLine(\"1 before await\");\n"
                            "await Task.Delay(50);\n"
                            "Console.WriteLine(\"2 after resume\");",
                            {1: "1 before await", 3: "2 after resume"},
                        )
                        + '<p class="step-result"><b>Remember:</b> <code>async</code> does <b>not</b> '
                        "mean “new OS thread per call.” It means “don’t hold the thread while waiting.”</p>"
                    ),
                },
                {
                    "title": "Step 4 — Do not block with <code>.Result</code> / <code>.Wait()</code>",
                    "body": (
                        "If you mark a method <code>async</code> then block with "
                        "<code>.Result</code>, you undo the benefit — and can deadlock."
                        '<div class="mc-row">'
                        '<div class="mc-col mc-bad"><span class="mc-lbl">Bad — blocks again</span>'
                        '<div class="step-pre">var data = FetchAsync().Result;  // holds thread</div></div>'
                        '<div class="mc-col mc-good"><span class="mc-lbl">Good — await through</span>'
                        '<div class="step-pre">var data = await FetchAsync();   // releases</div></div>'
                        "</div>"
                    ),
                },
            ],
            "interview_qa": [
                {
                    "q": "How do you turn a sync method into async?",
                    "a": "Add the <code>async</code> keyword, change the return type to "
                    "<code>Task</code> / <code>Task&lt;T&gt;</code>, and <code>await</code> "
                    "async APIs instead of blocking.",
                },
                {
                    "q": "What does async do to the thread?",
                    "a": "At <code>await</code>, the method releases the thread while waiting. "
                    "When the Task completes, execution resumes after the await.",
                },
                {
                    "q": "Why avoid .Result?",
                    "a": "It blocks the thread again and can cause deadlocks or thread-pool "
                    "starvation. Prefer <code>await</code> end-to-end.",
                },
            ],
        },
        "flow": (
            "My method needs to wait (HTTP / DB / file)",
            "Start from sync — then add async when waiting would block",
            [
                (
                    "Is the method still normal (no async keyword)?",
                    "It is sync",
                    "Thread stays busy until the method returns — even while waiting.",
                    ["string Fetch(...)", "thread blocked"],
                    "key",
                ),
                (
                    "Do you need to wait without holding the thread?",
                    "Add async + await",
                    "async allows await. await releases the thread; resumes when the result is ready.",
                    ["async Task<T>", "await GetAsync()"],
                    "dd",
                ),
                (
                    "Are you calling .Result or .Wait() on a Task?",
                    "Stop — use await",
                    "Blocking undoes the benefit and can deadlock.",
                    ["await FetchAsync()", "never .Result"],
                    "cm",
                ),
            ],
            "Flow to remember",
            "run → await (release thread) → result ready → resume after await",
            ["release → complete → resume"],
        ),
        "diagram": (
            _async_cycle()
            + compare(
                "Sync vs async at await",
                (
                    "Sync (.Result / Sleep)",
                    [
                        "Thread sits idle while waiting",
                        "Other work cannot use that thread",
                        "Can deadlock under load",
                    ],
                ),
                (
                    "async + await",
                    [
                        "Thread is free during the wait",
                        "Other requests can run",
                        "Resume when result is ready",
                    ],
                ),
                note="Add the async keyword → use await → release → resume.",
            )
        ),
    },
}
