"""Handcrafted rich slides that override catalog-generated bodies (D01, D06)."""

from __future__ import annotations

from slide_code import code
from slide_diagrams import compare, cycle, flow
from slide_io import io_split
from training_meta import _def


def _before_after(before: str, after: str, *, before_lbl: str = "Before", after_lbl: str = "After") -> str:
    """Side-by-side comparison used on every subtopic."""
    return (
        '<div class="mc-row">'
        f'<div class="mc-col mc-bad"><span class="mc-lbl">&#10060; {before_lbl}</span>'
        f'<div class="step-pre">{before}</div></div>'
        f'<div class="mc-col mc-good"><span class="mc-lbl">&#10004; {after_lbl}</span>'
        f'<div class="step-pre">{after}</div></div>'
        "</div>"
    )


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
        "subtopics": [
            "Value vs reference",
            "Boxing (SqlParameter)",
            "struct vs class (DTO)",
            "nullable value types",
        ],
        "meta": {
            "definition": _def(
                "In C#, a variable does not always “hold the object.” "
                "<b>Value types</b> (simple/primitive data like <code>int</code>, <code>bool</code>, "
                "<code>DateTime</code>, small <code>struct</code>s) store their bits "
                "<b>directly in the variable</b>. "
                "<b>Reference types</b> (<code>class</code> DTOs, <code>string</code>, "
                "<code>List&lt;T&gt;</code>) store the <b>starting address</b> (an arrow) of a "
                "heap object — so two variables can point at the same box.",
                [
                    "<b>Value types:</b> <code>int</code>, <code>bool</code>, <code>DateTime</code>, "
                    "<code>struct</code> — assignment <b>copies</b> the bits (independent copies).",
                    "<b>Reference types:</b> <code>class</code> DTOs, <code>string</code>, "
                    "<code>List&lt;T&gt;</code> — assignment copies the <b>address/reference</b> "
                    "(same object).",
                    "<b>Boxing:</b> putting a value into <code>object</code> (or untyped SQL param) "
                    "allocates on the heap — avoid on busy schedule/payment APIs.",
                    "<b>struct vs class:</b> small immutable value → <code>struct</code>; "
                    "shared mutable appointment/patient DTO across layers → <code>class</code>.",
                ],
            ),
            "interview": (
                "In my API Data Access I map SqlDataReader rows into class DTOs because appointments "
                "are mutated and shared Controller → DA → response. For SQL I use typed SqlParameter "
                "(SqlDbType.Int / DateTime) so int/DateTime are not boxed as object on busy paths. "
                "I pick struct only for small immutable values; classes for identity and shared mutation."
            ),
            "skill_id": "D01",
            "area": "D1 — C# Core",
        },
        "learn": (
            """
<p>Skill matrix <b>D01</b> — value vs reference, boxing, struct vs class.
<span style="color:#64748b">(Project angle from MyDotnet: SqlParameter + appointment DTOs.)</span></p>
<div class="callout"><b>Level-3 bar:</b> name a place boxing or struct vs class affected performance.</div>

<h3>Quick reference</h3>
<table class="data-tbl">
<tr><th>Kind</th><th>Examples in my API</th><th>Assignment does…</th></tr>
<tr><td>Value</td><td><code>int</code> PatientId, <code>DateTime</code>, <code>bool</code></td><td>Copies the bits</td></tr>
<tr><td>Reference</td><td><code>ScheduleAppointmentDto</code>, <code>string</code>, <code>List&lt;T&gt;</code></td><td>Copies the arrow (same object)</td></tr>
</table>

<h3>1. Value vs reference — full example</h3>
<p><b>What it means:</b> a value-type variable <b>is</b> the data.
A reference-type variable holds a <b>pointer</b> to one heap object — so two names can share one DTO.</p>
<p><b>Why it matters in my project:</b> Controller, DA, and API response all touch the same
<code>ScheduleAppointmentDto</code> instance. If it were a struct, each layer would get a <b>copy</b>
and updates would not travel together.</p>
"""
            + _before_after(
                "// BEFORE — think “= always copies data”\n"
                "var a = new List&lt;int&gt; { 1 };\n"
                "var b = a;      // looks like a copy…\n"
                "b.Add(2);\n"
                "// surprise: a also has 2 items\n"
                "Console.WriteLine(a.Count);  // 2",
                "// AFTER — know reference shares the object\n"
                "var a = new List&lt;int&gt; { 1 };\n"
                "var b = new List&lt;int&gt;(a);  // real copy\n"
                "b.Add(2);\n"
                "Console.WriteLine(a.Count);  // 1\n"
                "Console.WriteLine(b.Count);  // 2",
            )
            + """
<p class="step-result"><b>Takeaway:</b> value = copy the number · reference = copy the arrow.</p>

<h3>2. Boxing — full example (SqlParameter)</h3>
<p><b>What it means:</b> boxing wraps a value type in an <code>object</code> on the <b>heap</b>
(allocation + copy). Unboxing casts it back.</p>
<p><b>Why it matters in my project:</b> if you pass <code>int</code>/<code>DateTime</code> as plain
<code>object</code> into SQL parameters, .NET boxes them on every call. On busy schedule/payment APIs
that is extra GC pressure. Typed <code>SqlParameter</code> + <code>SqlDbType</code> is the fix we use in DA.</p>
"""
            + _before_after(
                "// BEFORE — API takes object → boxes the int\n"
                "int patientId = 42;\n"
                "cmd.Parameters.Add(\"@PatientId\", patientId);\n"
                "// Add(string, object) → int becomes object (heap)",
                "// AFTER — typed SqlParameter + SqlDbType\n"
                "int patientId = 42;\n"
                "cmd.Parameters.Add(\n"
                "  new SqlParameter(\"@PatientId\", SqlDbType.Int)\n"
                "  { Value = patientId });\n"
                "// SQL type is Int — not a bare object bag",
            )
            + """
<div class="keyword-box">
<b>How typed <code>SqlParameter</code> avoids the boxing trap</b>
<ol style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li><b>Boxing trigger:</b> a value type (<code>int</code>, <code>DateTime</code>) must live inside something typed as
<code>object</code> → CLR allocates a heap box and copies the bits.</li>
<li><b>Before (bad path):</b> <code>Parameters.Add("@PatientId", patientId)</code> uses an overload that takes
<code>object</code>. Your <code>int</code> is therefore boxed on <b>every</b> call before it even reaches SQL.</li>
<li><b>After (good path):</b> create the parameter with an explicit SQL type first —
<code>new SqlParameter("@PatientId", SqlDbType.Int)</code>. ADO.NET already knows “this is an Int column,”
so you are not stuffing a mystery <code>object</code> into the collection.</li>
<li><b>What you gain:</b> no untyped object-add boxing on the hot DA path; correct SQL type
(<code>Int</code> / <code>DateTime</code>) instead of <code>AddWithValue</code> guessing; less GC pressure on busy
schedule/payment APIs.</li>
<li><b>Same idea elsewhere:</b> prefer <code>List&lt;int&gt;</code> over <code>List&lt;object&gt;</code> —
generics keep the value as <code>int</code> and never box.</li>
</ol>
<p style="margin:8px 0 0;font-size:12px"><b>Picture of the call:</b></p>
<div class="step-pre" style="font-size:11px">BEFORE:  int patientId  ──box──▶  object  ──▶  Parameters.Add(name, object)
AFTER:   int patientId  ──▶  SqlParameter(SqlDbType.Int)  ──▶  SQL INT (typed)</div>
</div>
<p class="step-result"><b>Level-3 line:</b> “I avoid boxing on SqlParameter hot paths by using SqlDbType — I never pass int/DateTime as plain object into Add.”</p>

<h3>3. struct vs class — full example (DTO choice)</h3>
<p><b>What it means:</b> <code>struct</code> = value semantics (copied).
<code>class</code> = reference semantics (shared identity, mutation, inheritance).</p>
<p><b>Why it matters in my project:</b> appointments/patients are mapped from <code>SqlDataReader</code>
into <b>class</b> DTOs — mutated and passed across Controller → DA → API response.
A struct would copy at each hop and break shared updates / nullability patterns.</p>
"""
            + _before_after(
                "// BEFORE — struct DTO (wrong for shared mutation)\n"
                "public struct ScheduleAppointmentDto {\n"
                "  public int AppointmentId { get; set; }\n"
                "  public string PatientName { get; set; }\n"
                "}\n"
                "// each layer gets a COPY — updates may not stick",
                "// AFTER — class DTO (correct for our layers)\n"
                "public class ScheduleAppointmentDto {\n"
                "  public int AppointmentId { get; set; }\n"
                "  public string PatientName { get; set; }\n"
                "}\n"
                "// same instance shared Controller → DA → Ok(dto)",
            )
            + """
<table class="data-tbl">
<tr><th>Choose</th><th>When</th><th>Project example</th></tr>
<tr><td><code>class</code></td><td>Shared mutation, nullability, across layers</td><td><code>ScheduleAppointmentDto</code></td></tr>
<tr><td><code>struct</code></td><td>Small immutable value, copy is OK</td><td><code>Point</code>, <code>Money</code> amount</td></tr>
</table>

<h3>4. Nullable value types — short example</h3>
<p><b>What it means:</b> <code>int?</code> / <code>DateTime?</code> can be “no value” without using a reference type.
Useful for optional SQL columns (appointment end time may be null).</p>
"""
            + _before_after(
                "// BEFORE — magic 0 / MinValue as “missing”\n"
                "DateTime end = DateTime.MinValue;\n"
                "if (end == DateTime.MinValue) { /* missing? */ }",
                "// AFTER — nullable value type\n"
                "DateTime? end = reader[\"EndTime\"] as DateTime?;\n"
                "if (end is null) { /* truly missing */ }\n"
                "else { Use(end.Value); }",
            )
            + """
<h3>Self-check quiz</h3>
<div class="quiz-box">
  <div class="quiz-q"><b>Q1.</b> After <code>var b = a</code> where <code>a</code> is a class DTO, do both names share one object?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal"><b>Yes</b> — reference types copy the arrow. That is why we use <code>class</code> DTOs across Controller → DA → response.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q2.</b> How do you avoid boxing <code>int patientId</code> into a SQL parameter?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">Use typed <code>SqlParameter("@PatientId", SqlDbType.Int) { Value = patientId }</code> — not an untyped <code>object</code> add.</div>
    </details>
  </div>
  <div class="quiz-q"><b>Q3.</b> Why not make <code>ScheduleAppointmentDto</code> a struct?
    <details class="quiz-ans"><summary>Show answer</summary>
      <div class="quiz-reveal">It is mutated and shared across layers. A struct would <b>copy</b> at each hop — updates would not travel together. Prefer class for identity / shared mutation.</div>
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
            )
        ),
        "practice": """
<ul class="checklist">
  <li>Explain value vs reference with a list / DTO example (before vs after copy)</li>
  <li>Show typed <code>SqlParameter</code> vs boxing into <code>object</code></li>
  <li>Defend class DTO vs struct for appointments/patients across layers</li>
  <li>Use <code>DateTime?</code> for an optional SQL column instead of MinValue</li>
</ul>
<a class="file-link" href="Skill_Depth_Matrix_I25054_Sangeetha_Rajendiran_9.csv">Skill matrix CSV</a>
· <a class="file-link" href="MyDotnet.md">MyDotnet answers (D01)</a>
""",
        "beginner": {
            "steps": [
                {
                    "title": "Step 1 — Value vs reference (with before/after)",
                    "body": (
                        "<p>A <b>value type</b> variable holds the bits. A <b>reference type</b> holds an arrow "
                        "to one heap object — two variables can share the same DTO/list.</p>"
                        + _before_after(
                            "int a = 10;\nint b = a;  // COPY value\nb = 99;\n// a is still 10",
                            "var list1 = new List&lt;int&gt; { 1, 2 };\n"
                            "var list2 = list1;  // COPY arrow\n"
                            "list2.Add(3);\n"
                            "// list1.Count is 3 — same list",
                            before_lbl="Value type",
                            after_lbl="Reference type",
                        )
                        + io_split(
                            "int a = 10;\n"
                            "int b = a;\n"
                            "b = 99;\n"
                            "Console.WriteLine(a);  // 10\n"
                            "\n"
                            "var list1 = new List<int> { 1, 2 };\n"
                            "var list2 = list1;\n"
                            "list2.Add(3);\n"
                            "Console.WriteLine(list1.Count);  // 3",
                            {4: "10", 9: "3"},
                        )
                        + '<p class="step-result"><b>Takeaway:</b> value = copy the number · '
                        "reference = copy the arrow.</p>"
                    ),
                },
                {
                    "title": "Step 2 — Boxing on SQL parameters (before/after)",
                    "body": (
                        "<p><b>Boxing</b> = store a value type inside <code>object</code> on the heap (allocates). "
                        "On hot API paths we avoid the untyped parameter API.</p>"
                        + _before_after(
                            "// BEFORE — Add takes object → boxes int\n"
                            "int patientId = 42;\n"
                            "cmd.Parameters.Add(\"@PatientId\", patientId);\n"
                            "// int → object (heap alloc every call)",
                            "// AFTER — typed SqlParameter + SqlDbType\n"
                            "int patientId = 42;\n"
                            "cmd.Parameters.Add(\n"
                            "  new SqlParameter(\"@PatientId\", SqlDbType.Int)\n"
                            "  { Value = patientId });\n"
                            "// SQL type declared as Int up front",
                        )
                        + """
<div class="keyword-box">
<b>How this avoids the boxing problem</b>
<ol style="margin:6px 0 0 18px;font-size:12px;line-height:1.55">
<li><b>Trigger:</b> anytime an <code>int</code> must become <code>object</code>, the CLR boxes it (heap copy).</li>
<li><b>Before:</b> <code>Add(name, patientId)</code> expects <code>object</code> → <code>patientId</code> is boxed
on every SQL call in schedule/payment DA.</li>
<li><b>After:</b> build <code>SqlParameter(..., SqlDbType.Int)</code> first. You tell ADO.NET “this is SQL Int,”
instead of handing a bare <code>object</code> into the collection.</li>
<li><b>Why it matters:</b> less GC pressure on busy APIs + correct SQL type (no AddWithValue guessing).</li>
</ol>
<div class="step-pre" style="font-size:11px;margin-top:6px">BEFORE: int ──box──▶ object ──▶ Add(name, object)
AFTER:  int ──▶ SqlParameter(SqlDbType.Int) ──▶ SQL INT</div>
</div>
"""
                        + io_split(
                            "int n = 42;\n"
                            "object boxed = n;        // boxing\n"
                            "int back = (int)boxed;   // unboxing\n"
                            "Console.WriteLine(back);",
                            {4: "42"},
                        )
                        + '<p class="step-result"><b>Project line:</b> typed SqlDbType on schedule/payment '
                        "parameter binding = avoid object-add boxing on the hot path.</p>"
                    ),
                },
                {
                    "title": "Step 3 — struct vs class for DTOs (before/after)",
                    "body": (
                        "<p>Use <code>class</code> when the same appointment/patient object is passed and "
                        "updated across Controller → DA → API response. Use <code>struct</code> only for "
                        "small immutable values.</p>"
                        + _before_after(
                            "public struct ScheduleAppointmentDto { ... }\n"
                            "// each layer gets a COPY",
                            "public class ScheduleAppointmentDto {\n"
                            "  public int AppointmentId { get; set; }\n"
                            "  public string PatientName { get; set; }\n"
                            "}\n"
                            "// shared instance across layers",
                        )
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
                            "var copy = fee;\n"
                            "Console.WriteLine(copy.Amount);\n"
                            "\n"
                            "class Order { public int Id { get; set; } }\n"
                            "var o1 = new Order { Id = 1 };\n"
                            "var o2 = o1;\n"
                            "o2.Id = 99;\n"
                            "Console.WriteLine(o1.Id);  // 99",
                            {11: "9.99", 17: "99"},
                        )
                        + '<p class="step-result"><b>Takeaway:</b> DTO across layers → '
                        "<code>class</code>; tiny immutable value → <code>struct</code>.</p>"
                    ),
                },
                {
                    "title": "Step 4 — Nullable value types (before/after)",
                    "body": (
                        "<p>Optional SQL columns should use <code>int?</code> / <code>DateTime?</code>, "
                        "not magic zeros or <code>MinValue</code>.</p>"
                        + _before_after(
                            "DateTime end = DateTime.MinValue; // “missing?”",
                            "DateTime? end = reader[\"EndTime\"] as DateTime?;\n"
                            "if (end is null) { /* missing */ }",
                        )
                        + '<p class="step-result"><b>Takeaway:</b> <code>?</code> on value types = '
                        "true missing without a reference type.</p>"
                    ),
                },
            ],
            "interview_qa": [
                {
                    "q": "Where did boxing or struct vs class matter in your project?",
                    "a": "Typed <code>SqlParameter</code> (<code>SqlDbType.Int</code>/<code>DateTime</code>) "
                    "avoids boxing ints/dates as <code>object</code> on busy APIs. Appointment/patient "
                    "DTOs are <code>class</code> because they are mutated and shared across layers — "
                    "a struct would copy and break shared updates.",
                },
                {
                    "q": "What is boxing?",
                    "a": "Converting a value type to <code>object</code> (or an interface) — allocates on "
                    "the heap and copies the value. Prefer generics and typed parameters.",
                },
                {
                    "q": "When would you choose struct over class?",
                    "a": "Small immutable value semantics (Point, Money) with no shared mutation. "
                    "For DTOs across Controller → DA → response, use class.",
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
                    "Do you need shared mutation across Controller → DA → API?",
                    "Use class DTO",
                    "Reference type — one object shared across layers (ScheduleAppointmentDto).",
                    ["class ScheduleAppointmentDto", "class PatientDto"],
                    "dd",
                ),
                (
                    "Are value types going into object / untyped SQL params?",
                    "Avoid boxing",
                    "Use SqlDbType + generics (List<int>), not object / ArrayList.",
                    ["SqlParameter + SqlDbType.Int", "List<int>"],
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
                "Quick pick (project)",
                (
                    "Use value / struct when…",
                    [
                        "Small fixed data (Point, Money)",
                        "Copying is OK / wanted",
                        "No shared mutation across layers",
                    ],
                ),
                (
                    "Use class when…",
                    [
                        "DTO shared Controller → DA → Ok()",
                        "Nullability + mutable fields",
                        "Appointment / patient identity",
                    ],
                ),
                note="My project: class DTOs + typed SqlParameter (avoid boxing).",
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

# D57–D60 STAR / failure / decision / impact stories (from DOCX + MyDotnet)
from Dotnet.dotnet_stories_rich import STORIES_RICH  # noqa: E402

RICH.update(STORIES_RICH)
