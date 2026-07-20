"""C# comparison popups — triggered from glossary / slide content."""

from __future__ import annotations

from collections.abc import Callable

from slide_code import vs_editor

_PY_HETERO = 'order = [101, "SHIPPED", ["Google", "Amazon"]]'

_CS_HETERO = """// Does NOT compile:
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

_CS_TUPLE = """// ValueTuple — fixed slots, each position has a type
var order = (101, "SHIPPED", new List<string> { "Google", "Amazon" });

// Named fields (same data, clearer to read)
var orderNamed = (Id: 101, Status: "SHIPPED", Vendors: new List<string> { "Google", "Amazon" });

Console.WriteLine(orderNamed.Id);       // 101
Console.WriteLine(orderNamed.Status);   // SHIPPED
Console.WriteLine(orderNamed.Vendors[0]); // Google"""

_CS_RECORD = """// record — named type with fixed fields (C# 9+)
public record Order(int Id, string Status, List<string> Vendors);

var order = new Order(
    101,
    "SHIPPED",
    new List<string> { "Google", "Amazon" }
);

Console.WriteLine(order.Id);        // 101
Console.WriteLine(order.Status);    // SHIPPED
Console.WriteLine(order.Vendors[0]); // Google

// Records compare by value, not reference:
var a = new Order(101, "SHIPPED", new() { "Google" });
var b = new Order(101, "SHIPPED", new() { "Google" });
Console.WriteLine(a == b);  // True"""


def csharp_compare_btn(popup_id: str, label: str = "C# Comparison") -> str:
    return (
        f'<button type="button" class="btn-csharp-pop" '
        f'onclick="openCsharpWin(\'{popup_id}\')" title="Open draggable C# comparison window">'
        f"{label}</button>"
    )


def _hetero_list_body() -> str:
    py_code = vs_editor(_PY_HETERO, lang="python", compact=True)
    cs_code = vs_editor(_CS_HETERO, lang="csharp", compact=True)
    tuple_code = vs_editor(_CS_TUPLE, lang="csharp", compact=True)
    record_code = vs_editor(_CS_RECORD, lang="csharp", compact=True)
    return f"""
<p>In <b>Python</b>, one <code>list</code> can hold mixed types naturally:</p>
{py_code}
<p>In <b>C#</b>, <code>List&lt;T&gt;</code> is strongly typed — you cannot mix types unless <code>T</code> is <code>object</code>:</p>
{cs_code}
<p><b>More idiomatic in C#:</b></p>
<table class="data-tbl csharp-pop-tbl">
<tr><th>Approach</th><th>What it is</th><th>When to use</th></tr>
<tr>
  <td><code>List&lt;object&gt;</code></td>
  <td>A growable list where every item is stored as <code>object</code>. You must <b>cast</b> when reading.</td>
  <td>Quick prototype or legacy code — avoid in new APIs.</td>
</tr>
<tr>
  <td><code>(int Id, string Status, List&lt;string&gt; Vendors)</code></td>
  <td><b>Yes — a ValueTuple.</b> A lightweight grouped value: fixed number of slots, each with a known type. Access by position (<code>Item1</code>) or by name (<code>Id</code>, <code>Status</code>).</td>
  <td>Return 2–4 related values from a method, local grouping, no need for a separate class.</td>
</tr>
<tr>
  <td><code>record Order(...)</code></td>
  <td><b>A record type</b> (C# 9+) — a named class-like type with immutable-style fields, value-based equality, and clear field names.</td>
  <td>Domain models, DTOs, API payloads — when the shape is reused across methods/classes.</td>
</tr>
</table>
<p><b>2. ValueTuple example</b> — closest to Python’s heterogeneous list for a single “record”:</p>
{tuple_code}
<p><b>3. Record example</b> — best when you want a reusable, named type:</p>
{record_code}
<p class="csharp-pop-note"><b>Bottom line:</b> Python’s <code>[101, "SHIPPED", [...]]</code> maps best to a <b>named ValueTuple</b> or a <b>record</b> in C# — not <code>List&lt;object&gt;</code>, unless you truly need a dynamic mixed bag.</p>
"""


_POPUP_BUILDERS: dict[str, tuple[str, Callable[[], str]]] = {
    "hetero-list": ("C# Comparison — Heterogeneous Lists", _hetero_list_body),
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
