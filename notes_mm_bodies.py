"""MindMap slide bodies for datatype concepts (kid-friendly + memory)."""

from __future__ import annotations

from notes_mm_helpers import card, cheat, grid, memory, ops, p, sec, trap, what_two


def body_numbers() -> str:
    return (
        sec(
            "1. What is a number?",
            what_two(
                '<span class="kv">age<span class="arrow">&rarr;</span>25</span>'
                '<span class="kv">price<span class="arrow">&rarr;</span>9.5</span>'
                '<span class="kv">big<span class="arrow">&rarr;</span>10**100</span>',
                "<h4>Remember</h4>"
                '<p class="line"><strong>int</strong> &rarr; whole number</p>'
                '<p class="line"><strong>float</strong> &rarr; with a dot</p>',
                "Unlimited int size",
            ),
        )
        + sec(
            "2. Everyday operations",
            ops(
                [
                    ("new", "NEW", "Make", "n=25"),
                    ("add", "+", "Add", "n+1"),
                    ("chg", "//", "Floor /", "7//2 &rarr; 3"),
                    ("read", "/", "True /", "7/2 &rarr; 3.5"),
                    ("del", "**", "Power", "2**10"),
                ]
            ),
        )
        + sec(
            "3. Quick rules",
            grid(
                card("int vs float", "<code>3</code> is int. <code>3.0</code> is float.<br><code>/</code> always gives float in Python 3."),
                card("bool is a number too", "<code>True == 1</code>, <code>False == 0</code><br>But prefer real <code>bool</code> for yes/no."),
            ),
        )
        + memory(
            "Every number is an object. Bigger ints need more bytes.<br>"
            "<code>sys.getsizeof(1)</code> &lt; <code>sys.getsizeof(10**100)</code><br>"
            "Do not memorize exact bytes — they change by Python version.",
            "<b>Python int has no fixed 32/64-bit box</b> — it grows with the value (unlike C# <code>int</code>).<br>"
            "Interview: compare with <code>sys.getsizeof</code>; say sizes vary by build.<br>"
            "Float is fixed-width (IEEE) — big ints stay exact; floats can round.",
        )
        + sec(
            "4. Cheat sheet",
            cheat(
                [
                    ("int", "Whole count", "<code>age = 25</code>"),
                    ("float", "With decimal", "<code>price = 9.5</code>"),
                    ("/", "True divide", "<code>7/2 &rarr; 3.5</code>"),
                    ("//", "Floor divide", "<code>7//2 &rarr; 3</code>"),
                    ("sizeof", "Shallow bytes", "<code>sys.getsizeof(n)</code>"),
                ]
            ),
        )
    )


def body_strings() -> str:
    return (
        sec(
            "1. What is a string?",
            what_two(
                '<span class="kv">"H"<span class="arrow">&rarr;</span>0</span>'
                '<span class="kv">"i"<span class="arrow">&rarr;</span>1</span>'
                '<span class="kv">"!"<span class="arrow">&rarr;</span>2</span>',
                "<h4>Remember</h4>"
                '<p class="line"><strong>str</strong> &rarr; text in quotes</p>'
                '<p class="line"><strong>Index</strong> &rarr; seat number</p>',
                "Immutable text",
            ),
        )
        + sec(
            "2. Everyday operations",
            ops(
                [
                    ("new", "NEW", "Create", 's="Hi"'),
                    ("read", "&#128065;", "Read", "s[0]"),
                    ("add", "+", "Join", 's+"!"'),
                    ("chg", "f", "f-string", 'f"Hi {n}"'),
                    ("del", "[:]", "Slice", "s[0:2]"),
                ]
            ),
        )
        + sec(
            "3. Quick rules",
            grid(
                card("Cannot change one letter", '<code>s[0] = "X"</code> &rarr; error<br>Make a new string instead.'),
                card("Quotes", "<code>'hi'</code> or <code>\"hi\"</code><br>Triple quotes for long text."),
            ),
        )
        + trap("<b>Watch out:</b> Strings cannot change in place. <code>s = s + \"!\"</code> makes a <b>new</b> string.")
        + memory(
            "Longer text uses more memory.<br>"
            "<code>sys.getsizeof(\"A\")</code> &lt; <code>sys.getsizeof(\"Hello\")</code><br>"
            "Empty <code>\"\"</code> still costs some bytes (object header).",
            "Strings are <b>immutable</b> &amp; often interned for small literals.<br>"
            "Building with many <code>+</code> in a loop can be slow — prefer <code>''.join(parts)</code>.<br>"
            "Interview: <code>getsizeof</code> is shallow; shared interned strings may look small.",
        )
        + sec(
            "4. Cheat sheet",
            cheat(
                [
                    ("Create", "Text box", '<code>s = "Hi"</code>'),
                    ("Index", "One letter", "<code>s[0]</code>"),
                    ("Slice", "A piece", "<code>s[1:3]</code>"),
                    ("f-string", "Fill blanks", '<code>f"Hi {name}"</code>'),
                    ("Join", "Glue list", '<code>"".join(parts)</code>'),
                ]
            ),
        )
    )


def body_bool_none() -> str:
    return (
        sec(
            "1. What are Bool &amp; None?",
            what_two(
                '<span class="kv">yes<span class="arrow">&rarr;</span>True</span>'
                '<span class="kv">no<span class="arrow">&rarr;</span>False</span>'
                '<span class="kv">empty<span class="arrow">&rarr;</span>None</span>',
                "<h4>Remember</h4>"
                '<p class="line"><strong>bool</strong> &rarr; yes / no</p>'
                '<p class="line"><strong>None</strong> &rarr; nothing here</p>',
                "Use is for None",
            ),
        )
        + sec(
            "2. Everyday checks",
            ops(
                [
                    ("new", "T/F", "Make", "ok=True"),
                    ("read", "if", "If true", "if ok:"),
                    ("add", "not", "Flip", "not ok"),
                    ("chg", "and", "Both", "a and b"),
                    ("del", "is", "None?", "x is None"),
                ]
            ),
        )
        + sec(
            "3. Truthy / falsy (kid rule)",
            grid(
                card("Falsy (count as no)", "<code>False</code>, <code>0</code>, <code>0.0</code>, <code>\"\"</code>, <code>[]</code>, <code>{}</code>, <code>set()</code>, <code>None</code>"),
                card("Truthy (count as yes)", "Almost everything else — non-empty text, lists, numbers ≠ 0."),
            ),
        )
        + trap("<b>Watch out:</b> Use <code>x is None</code>, not <code>x == None</code>. Use <code>is</code> for identity; <code>==</code> for value.")
        + memory(
            "<code>True</code>/<code>False</code> are tiny shared objects (bool is a subclass of int).<br>"
            "<code>None</code> is one shared singleton — everyone points to the same nothing.",
            "Interview: <code>bool</code> is a subclass of <code>int</code> (<code>True == 1</code>).<br>"
            "<code>None</code> is a singleton — identity check with <code>is</code>.<br>"
            "Falsy containers still exist in memory; they just test false in <code>if</code>.",
        )
        + sec(
            "4. Cheat sheet",
            cheat(
                [
                    ("True/False", "Yes / no", "<code>ok = True</code>"),
                    ("None", "Missing value", "<code>x = None</code>"),
                    ("is None", "Same nothing?", "<code>x is None</code>"),
                    ("Truthy test", "If box has stuff", "<code>if items:</code>"),
                ]
            ),
        )
    )


def body_list() -> str:
    return (
        sec(
            "1. What is a List?",
            what_two(
                '<span class="kv">0<span class="arrow">&rarr;</span>"red"</span>'
                '<span class="kv">1<span class="arrow">&rarr;</span>"blue"</span>'
                '<span class="kv">2<span class="arrow">&rarr;</span>"green"</span>',
                "<h4>Remember</h4>"
                '<p class="line"><strong>List</strong> &rarr; row of seats</p>'
                '<p class="line"><strong>Index</strong> &rarr; seat number</p>',
                "Mutable · ordered",
            ),
        )
        + sec(
            "2. Everyday operations",
            ops(
                [
                    ("new", "NEW", "Create", 'a=["red"]'),
                    ("read", "&#128065;", "Read", "a[0]"),
                    ("add", "+", "Append", 'a.append("x")'),
                    ("chg", "&#9998;", "Change", 'a[0]="y"'),
                    ("del", "&#10005;", "Delete", "del a[0]"),
                ]
            ),
        )
        + sec(
            "3. Copy vs same box",
            grid(
                card("Alias (same box)", "<code>b = a</code><br>Change <code>b</code> &rarr; <code>a</code> changes too."),
                card("Copy (new box)", "<code>b = a.copy()</code> or <code>a[:]</code><br>Safe separate list."),
            ),
        )
        + trap("<b>Watch out:</b> <code>b = a</code> does not copy. Both names point to one list.")
        + memory(
            "Lists keep <b>extra empty seats</b> ready for append (over-allocation).<br>"
            "Size jumps in steps — not +1 byte each time you append.<br>"
            "<code>sys.getsizeof([])</code> &gt; <code>sys.getsizeof(())</code> (list shell is heavier).",
            "Interview: CPython over-allocates (~grow factor) so append is usually amortized O(1).<br>"
            "<code>getsizeof(list)</code> is <b>shallow</b> — does not include nested objects.<br>"
            "Prefer generators/<code>range</code> when you only need to walk huge data.",
        )
        + sec(
            "4. Cheat sheet",
            cheat(
                [
                    ("Create", "Row of seats", "<code>a = [1, 2]</code>"),
                    ("Append", "Add at end", "<code>a.append(3)</code>"),
                    ("Slice", "Take a piece", "<code>a[1:3]</code>"),
                    ("Copy", "New row", "<code>a.copy()</code>"),
                    ("sizeof", "Shell bytes", "<code>sys.getsizeof(a)</code>"),
                ]
            ),
        )
    )


def body_tuple() -> str:
    return (
        sec(
            "1. What is a Tuple?",
            what_two(
                '<span class="kv">0<span class="arrow">&rarr;</span>12.97</span>'
                '<span class="kv">1<span class="arrow">&rarr;</span>80.22</span>',
                "<h4>Remember</h4>"
                '<p class="line"><strong>Tuple</strong> &rarr; fixed record</p>'
                '<p class="line"><strong>()</strong> &rarr; cannot change</p>',
                "Immutable · ordered",
            ),
        )
        + sec(
            "2. Everyday operations",
            ops(
                [
                    ("new", "NEW", "Create", "t=(1,2)"),
                    ("read", "&#128065;", "Read", "t[0]"),
                    ("add", ",", "Unpack", "a,b=t"),
                    ("chg", "()", "One item", "t=(1,)"),
                    ("del", "key", "Dict key", "d[t]=1"),
                ]
            ),
        )
        + sec(
            "3. When to use",
            grid(
                card("Good for", "GPS <code>(lat, lng)</code>, RGB, <code>return ok, data</code>, dict keys."),
                card("Not for", "Growing carts / logs — use a <b>list</b> instead."),
            ),
        )
        + trap("<b>Watch out:</b> <code>(1)</code> is just number 1. One-item tuple needs a comma: <code>(1,)</code>.")
        + memory(
            "Tuples are usually <b>leaner</b> than lists — no append buffer.<br>"
            "<code>sys.getsizeof((1,2,3))</code> often &lt; same list.<br>"
            "Fixed size &rarr; less bookkeeping.",
            "Interview: tuple is immutable &amp; hashable (if items are) &rarr; safe dict key.<br>"
            "Often slightly faster to iterate fixed data; less memory than list.<br>"
            "Nested mutable item (e.g. list inside) can still change — hash with care.",
        )
        + sec(
            "4. Cheat sheet",
            cheat(
                [
                    ("Create", "Fixed record", "<code>t = (1, 2)</code>"),
                    ("One item", "Need comma", "<code>t = (1,)</code>"),
                    ("Unpack", "Split out", "<code>a, b = t</code>"),
                    ("Dict key", "Safe label", "<code>d[(1,2)] = \"x\"</code>"),
                ]
            ),
        )
    )


def body_set() -> str:
    return (
        sec(
            "1. What is a Set?",
            what_two(
                '<span class="kv">"red"<span class="arrow">&rarr;</span>in</span>'
                '<span class="kv">"blue"<span class="arrow">&rarr;</span>in</span>'
                '<span class="kv">"red"<span class="arrow">&rarr;</span>dup gone</span>',
                "<h4>Remember</h4>"
                '<p class="line"><strong>Set</strong> &rarr; bag of unique tags</p>'
                '<p class="line"><strong>No order</strong> &rarr; no seat numbers</p>',
                "Unique · mutable",
            ),
        )
        + sec(
            "2. Everyday operations",
            ops(
                [
                    ("new", "NEW", "Create", 's={"a","b"}'),
                    ("add", "+", "Add", 's.add("c")'),
                    ("read", "in", "Ask", '"a" in s'),
                    ("del", "&#10005;", "Remove", 's.discard("a")'),
                    ("chg", "fs", "Frozen", "frozenset(s)"),
                ]
            ),
        )
        + sec(
            "3. Set vs frozenset",
            grid(
                card("set", "Can add/remove.<br>Empty: <code>set()</code> — not <code>{}</code>."),
                card("frozenset", "Cannot change.<br>OK as <b>dict key</b>."),
            ),
        )
        + trap("<b>Watch out:</b> <code>{}</code> is an empty <b>dict</b>. Empty set is <code>set()</code>.")
        + memory(
            "Sets use a hash table — fast <code>in</code>, but extra memory overhead.<br>"
            "Empty set shell is often larger than empty list/tuple.<br>"
            "Duplicates are not stored twice.",
            "Interview: average O(1) membership via hashing.<br>"
            "Items must be hashable (immutable).<br>"
            "<code>frozenset</code> when you need a set-like dict key.",
        )
        + sec(
            "4. Cheat sheet",
            cheat(
                [
                    ("Create", "Unique bag", '<code>s = {"a", "b"}</code>'),
                    ("Empty", "Not {}", "<code>s = set()</code>"),
                    ("in", "Fast ask", '<code>"a" in s</code>'),
                    ("frozenset", "Fixed set", "<code>frozenset(s)</code>"),
                ]
            ),
        )
    )


def body_dict() -> str:
    """Existing Dict tools guide + memory section."""
    return """
<div class="mm-sec">
  <h3>1. What is a Dictionary?</h3>
  <div class="dict-what">
    <div class="dict-panel">
      <div class="dict-viz">
        <span class="kv">"red"<span class="arrow">&rarr;</span>3</span>
        <span class="kv">"blue"<span class="arrow">&rarr;</span>5</span>
        <span class="kv">"green"<span class="arrow">&rarr;</span>2</span>
      </div>
    </div>
    <div class="dict-panel dict-remember">
      <h4>Remember</h4>
      <p class="line"><strong>Key</strong> &rarr; label on the box</p>
      <p class="line"><strong>Value</strong> &rarr; item inside the box</p>
      <span class="dict-tag">Immutable Keys</span>
    </div>
  </div>
</div>

<div class="mm-sec">
  <h3>2. Everyday Operations</h3>
  <div class="ops-row">
    <div class="op-card">
      <div class="op-ico new">NEW</div>
      <div class="op-name">Create</div>
      <span class="op-code">d={"red":3}</span>
    </div>
    <div class="op-card">
      <div class="op-ico read">&#128065;</div>
      <div class="op-name">Read</div>
      <span class="op-code">d["red"]</span>
    </div>
    <div class="op-card">
      <div class="op-ico add">+</div>
      <div class="op-name">Add</div>
      <span class="op-code">d["blue"]=1</span>
    </div>
    <div class="op-card">
      <div class="op-ico chg">&#9998;</div>
      <div class="op-name">Change</div>
      <span class="op-code">d["red"]=5</span>
    </div>
    <div class="op-card">
      <div class="op-ico del">&#10005;</div>
      <div class="op-name">Delete</div>
      <span class="op-code">del d["red"]</span>
    </div>
  </div>
</div>

<div class="mm-sec">
  <h3>3. See what is inside</h3>
  <div class="mm-grid">
    <div class="mm-card">
      <b>Empty dict</b>
      <code>d = {}</code> or <code>d = dict()</code><br>
      Tip: <code>{}</code> is a dict. Empty set is <code>set()</code>.
    </div>
    <div class="mm-card">
      <b>Walk the boxes</b>
      <code>d.keys()</code> &mdash; labels<br>
      <code>d.values()</code> &mdash; insides<br>
      <code>d.items()</code> &mdash; both together
    </div>
  </div>
</div>

<div class="mm-sec">
  <h3>4. Label rules</h3>
  <p>
    A label must <b>stay the same</b> forever (immutable).
    Good labels: <code>str</code>, <code>int</code>, <code>tuple</code>.
    Bad labels: <code>list</code>, <code>dict</code>, <code>set</code> (they can change).
  </p>
</div>

<div class="mm-sec">
  <h3>5. Safe ways to look</h3>
  <div class="mm-grid">
    <div class="mm-card">
      <b>Ask: is the label there?</b>
      <code>"red" in box</code> &rarr; <code>True</code> / <code>False</code><br>
      Does <b>not</b> create a new box.
    </div>
    <div class="mm-card">
      <b>Ask gently with a backup</b>
      <code>box.get("yellow", 0)</code><br>
      If missing, you get <code>0</code> — no crash.
    </div>
  </div>
  <p style="margin-top:8px">
    <b>Careful:</b> <code>box["yellow"]</code> crashes with <code>KeyError</code> if that label is missing.
  </p>
</div>

<div class="mm-sec">
  <h3>6. Extra helpers</h3>
  <div class="mm-grid">
    <div class="mm-card">
      <b>defaultdict — auto groups</b>
      New group starts empty when you need it.<br>
      Like: fruits into baskets by color.<br>
      <code>groups[color].append(fruit)</code>
    </div>
    <div class="mm-card">
      <b>ChainMap — two boxes</b>
      Check your box first, then a backup box.<br>
      First answer wins.<br>
      <code>ChainMap(Dict1, Dict2)</code>
    </div>
  </div>
</div>

<div class="mm-sec">
  <h3>7. Which tool? (pick one)</h3>
  <p>Read from the top. When the answer is YES, stop.</p>
  <div class="dt-legend">
    <span><i class="dt-dot q"></i> Ask yourself</span>
    <span><i class="dt-dot plain"></i> plain dict</span>
    <span><i class="dt-dot peek"></i> key check</span>
    <span><i class="dt-dot dd" style="background:#16a34a"></i> defaultdict</span>
    <span><i class="dt-dot layer"></i> ChainMap</span>
  </div>

  <div class="dt-tree">
    <div class="dt-start">
      I want to store things by name
      <small>Start with normal dict. Use helpers only when you need them.</small>
    </div>

    <div class="dt-row">
      <div class="dt-q"><span class="dt-sit">Do you only want to ask<br>&ldquo;is this box there?&rdquo;</span>
        <em>Do not make a new empty box by accident</em></div>
      <div class="dt-a">
        <div class="pick"><span class="tag tag-key">Use</span> <code>"k" in d</code> or <code>d.get("k")</code></div>
        <div>Just peek. Safe for every dict.</div>
        <div class="why">YES &rarr; done. NO &rarr; go down.</div>
      </div>
    </div>

    <div class="dt-row">
      <div class="dt-q"><span class="dt-sit">Are you sorting things<br>into groups in a loop?</span>
        <em>Like: put each fruit into a basket by color</em></div>
      <div class="dt-a">
        <div class="pick"><span class="tag tag-dd">Use</span> <code>defaultdict(list)</code></div>
        <div>Empty group appears by itself. Then add the item.</div>
        <div><code>groups[dept].append(name)</code></div>
        <div class="why">YES &rarr; done. NO &rarr; go down.</div>
      </div>
    </div>

    <div class="dt-row">
      <div class="dt-q"><span class="dt-sit">Do you have two boxes<br>(yours first, then a backup)?</span>
        <em>Check yours first; use backup only if missing</em></div>
      <div class="dt-a">
        <div class="pick"><span class="tag tag-cm">Use</span> <code>ChainMap(Dict1, Dict2)</code></div>
        <div>Look in Dict1 first. If missing, look in Dict2.</div>
        <div><code>CombinedDict["color"]</code></div>
        <div class="why">YES &rarr; done. NO &rarr; go down.</div>
      </div>
    </div>

    <div class="dt-row">
      <div class="dt-q"><span class="dt-sit">None of those?</span>
        <em>You put each thing in yourself</em></div>
      <div class="dt-a">
        <div class="pick"><span class="tag tag-dict">Use</span> plain <code>dict</code> / <code>{}</code></div>
        <div>Normal boxes. Everyday choice.</div>
        <div><code>d["a"] = 1</code></div>
        <div class="why">Start here for most work.</div>
      </div>
    </div>
  </div>

  <div class="fc-wrap">
    <p class="fc-label">Same path — flowchart view</p>
    <div class="fc">
      <div class="fc-start">I want to store things by name
        <small>Start with normal dict. Use helpers only when you need them.</small>
      </div>
      <div class="fc-arrow"></div>

      <div class="fc-node">
        <div class="fc-q-box">Only ask &ldquo;is this box there?&rdquo;</div>
        <div class="fc-branch">
          <div class="fc-spacer"></div>
          <div class="fc-mid"><div class="fc-arrow tall"></div><span class="fc-arrow-lbl">NO</span></div>
          <div class="fc-yes">
            <span class="fc-side yes">YES</span>
            <div class="fc-h right"></div>
            <div class="fc-use key"><b>Use key check</b><code>"k" in d</code><code>d.get("k")</code></div>
          </div>
        </div>
      </div>

      <div class="fc-node">
        <div class="fc-q-box">Sorting into groups in a loop?</div>
        <div class="fc-branch">
          <div class="fc-spacer"></div>
          <div class="fc-mid"><div class="fc-arrow tall"></div><span class="fc-arrow-lbl">NO</span></div>
          <div class="fc-yes">
            <span class="fc-side yes">YES</span>
            <div class="fc-h right"></div>
            <div class="fc-use dd"><b>Use defaultdict</b><code>defaultdict(list)</code></div>
          </div>
        </div>
      </div>

      <div class="fc-node">
        <div class="fc-q-box">Two boxes (yours + backup)?</div>
        <div class="fc-branch">
          <div class="fc-spacer"></div>
          <div class="fc-mid"><div class="fc-arrow tall"></div><span class="fc-arrow-lbl">NO</span></div>
          <div class="fc-yes">
            <span class="fc-side yes">YES</span>
            <div class="fc-h right"></div>
            <div class="fc-use cm"><b>Use ChainMap</b><code>ChainMap(D1, D2)</code></div>
          </div>
        </div>
      </div>

      <div class="fc-arrow"></div>
      <div class="fc-use dict fc-end"><b>Use plain dict</b><code>d = {}</code> / <code>d["a"] = 1</code><span>Everyday choice</span></div>
    </div>
  </div>
</div>

<div class="mm-sec">
  <h3>8. Four choices (quick look)</h3>
  <div class="ninode">
    <div class="ninode-card dict">
      <div class="role">Normal</div>
      <h4>plain dict</h4>
      You make every box.<br>
      Simple and common.<br>
      <code>d = {"a": 1}</code>
    </div>
    <div class="ninode-card key">
      <div class="role">Just ask</div>
      <h4>key check</h4>
      &ldquo;Is it there?&rdquo;<br>
      Do not create it.<br>
      <code>"k" in d</code>
    </div>
    <div class="ninode-card dd">
      <div class="role">Auto groups</div>
      <h4>defaultdict</h4>
      New group starts empty<br>when you need it.<br>
      <code>groups[k].append(v)</code>
    </div>
    <div class="ninode-card cm">
      <div class="role">Two boxes</div>
      <h4>ChainMap</h4>
      Check box 1, then box 2.<br>
      First answer wins.<br>
      <code>ChainMap(D1, D2)</code>
    </div>
  </div>
</div>

<div class="dt-trap">
  <b>Watch out:</b> With <code>defaultdict</code>, writing
  <code>if myDict["ghost"]:</code> can <b>make</b> a new empty box named
  <code>ghost</code>. To only ask, write <code>if "ghost" in myDict:</code>.
</div>
""" + memory(
        "Dict is a hash table: fast lookup, but overhead for buckets.<br>"
        "Keys and values are separate objects — <code>getsizeof(d)</code> is shallow.<br>"
        "More keys &rarr; more memory (table may resize).",
        "Interview: average O(1) get/set via hashing; keys must be hashable.<br>"
        "Insertion order preserved (3.7+).<br>"
        "Compare tools: plain dict vs defaultdict vs ChainMap (no full merge copy).",
    ) + sec(
        "9. Full cheat sheet",
        cheat(
            [
                ("Make dict", "Start boxes", '<code>d = {"a": 1}</code>'),
                ("Read", "Open one", '<code>d["a"]</code>'),
                ("Safe ask", "Is label there?", '<code>"a" in d</code>'),
                ("Safe get", "Backup value", '<code>d.get("z", 0)</code>'),
                ("sizeof", "Shallow bytes", "<code>sys.getsizeof(d)</code>"),
            ]
        ),
    )


def body_which_collection() -> str:
    return (
        sec(
            "1. Pick a collection",
            p("Ask from the top. Stop at the first YES."),
        )
        + """
<div class="dt-tree">
  <div class="dt-start">I need to hold many values
    <small>list · tuple · set · dict</small>
  </div>
  <div class="dt-row">
    <div class="dt-q"><span class="dt-sit">Need label &rarr; value<br>lookup by name?</span>
      <em>Like: color &rarr; count</em></div>
    <div class="dt-a">
      <div class="pick"><span class="tag tag-dict">Use</span> <code>dict</code></div>
      <div class="why">YES &rarr; done. NO &rarr; go down.</div>
    </div>
  </div>
  <div class="dt-row">
    <div class="dt-q"><span class="dt-sit">Only unique tags?<br>Fast &ldquo;is it in?&rdquo;</span>
      <em>Duplicates should vanish</em></div>
    <div class="dt-a">
      <div class="pick"><span class="tag tag-dd">Use</span> <code>set</code> / <code>frozenset</code></div>
      <div class="why">YES &rarr; done. NO &rarr; go down.</div>
    </div>
  </div>
  <div class="dt-row">
    <div class="dt-q"><span class="dt-sit">Fixed record that<br>must not change?</span>
      <em>GPS, return pair, dict key</em></div>
    <div class="dt-a">
      <div class="pick"><span class="tag tag-cm">Use</span> <code>tuple</code></div>
      <div class="why">YES &rarr; done. NO &rarr; go down.</div>
    </div>
  </div>
  <div class="dt-row">
    <div class="dt-q"><span class="dt-sit">Growing ordered list?</span>
      <em>Cart, log, scores</em></div>
    <div class="dt-a">
      <div class="pick"><span class="tag tag-key">Use</span> <code>list</code></div>
      <div class="why">Everyday default.</div>
    </div>
  </div>
</div>

<div class="fc-wrap">
  <p class="fc-label">Flowchart view</p>
  <div class="fc">
    <div class="fc-start">Hold many values<small>pick one collection</small></div>
    <div class="fc-arrow"></div>
    <div class="fc-node">
      <div class="fc-q-box">Need key &rarr; value by name?</div>
      <div class="fc-branch">
        <div class="fc-spacer"></div>
        <div class="fc-mid"><div class="fc-arrow tall"></div><span class="fc-arrow-lbl">NO</span></div>
        <div class="fc-yes"><span class="fc-side yes">YES</span><div class="fc-h right"></div>
          <div class="fc-use dict"><b>Use dict</b><code>{"a": 1}</code></div></div>
      </div>
    </div>
    <div class="fc-node">
      <div class="fc-q-box">Only unique tags?</div>
      <div class="fc-branch">
        <div class="fc-spacer"></div>
        <div class="fc-mid"><div class="fc-arrow tall"></div><span class="fc-arrow-lbl">NO</span></div>
        <div class="fc-yes"><span class="fc-side yes">YES</span><div class="fc-h right"></div>
          <div class="fc-use dd"><b>Use set</b><code>{"a","b"}</code></div></div>
      </div>
    </div>
    <div class="fc-node">
      <div class="fc-q-box">Fixed, must not change?</div>
      <div class="fc-branch">
        <div class="fc-spacer"></div>
        <div class="fc-mid"><div class="fc-arrow tall"></div><span class="fc-arrow-lbl">NO</span></div>
        <div class="fc-yes"><span class="fc-side yes">YES</span><div class="fc-h right"></div>
          <div class="fc-use cm"><b>Use tuple</b><code>(1, 2)</code></div></div>
      </div>
    </div>
    <div class="fc-arrow"></div>
    <div class="fc-use key fc-end"><b>Use list</b><code>[1, 2, 3]</code><span>Everyday ordered bag</span></div>
  </div>
</div>
"""
        + memory(
            "Rough shell cost (varies): empty tuple often lightest; list next; dict/set heavier (hash tables).<br>"
            "Pick by <b>job</b> first — then think about memory.",
            "Interview: list = ordered mutable; tuple = fixed/hashable; set = unique/hash; dict = mapping.<br>"
            "Mention over-allocation (list) and hash overhead (set/dict).<br>"
            "For huge streams prefer generators over materializing a list.",
        )
    )


def body_mutable() -> str:
    return (
        sec(
            "1. Can it change?",
            p("Mutable = you can change the inside. Immutable = make a new one instead."),
        )
        + sec(
            "2. Table",
            """
<table class="data-tbl">
<tr><th>Type</th><th>Mutable?</th><th>Dict key?</th></tr>
<tr><td>int, float, str, bool</td><td>No</td><td>Yes</td></tr>
<tr><td>tuple, frozenset</td><td>No</td><td>Yes*</td></tr>
<tr><td>list, dict, set</td><td>Yes</td><td>No</td></tr>
</table>
<p style="font-size:12px;color:#64748b">* tuple/frozenset only if their items are hashable too.</p>
""",
        )
        + sec(
            "3. Kid picture",
            grid(
                card("Immutable", "Sealed box. To change, buy a new box.<br><code>s = s + \"!\"</code>"),
                card("Mutable", "Open box. Swap what is inside.<br><code>a.append(1)</code>"),
            ),
        )
        + trap("<b>Watch out:</b> Dict keys need a stable hash. Mutable keys are blocked so the locker number cannot move.")
        + memory(
            "Immutables can be shared safely (same object reused).<br>"
            "Mutables shared by alias (<code>b=a</code>) surprise you when one side changes.",
            "Interview: hashability requires immutability for reliable dict/set use.<br>"
            "Identity (<code>is</code>) vs equality (<code>==</code>) matters more with mutables.<br>"
            "Copy mutables when you need isolation (<code>copy</code> / <code>deepcopy</code>).",
        )
    )


def body_collections() -> str:
    return (
        sec(
            "1. Extra dict / sequence tools",
            p("From <code>collections</code> — helpers on top of normal types."),
        )
        + sec(
            "2. Quick cards",
            """
<div class="ninode" style="grid-template-columns:repeat(3,1fr)">
  <div class="ninode-card dd"><div class="role">Count</div><h4>Counter</h4>Tally how many.<br><code>Counter(words)</code></div>
  <div class="ninode-card dict"><div class="role">Auto</div><h4>defaultdict</h4>Missing key makes default.<br><code>defaultdict(list)</code></div>
  <div class="ninode-card cm"><div class="role">Layers</div><h4>ChainMap</h4>Look in map1 then map2.<br><code>ChainMap(D1,D2)</code></div>
  <div class="ninode-card key"><div class="role">Queue</div><h4>deque</h4>Fast both ends.<br><code>deque(maxlen=n)</code></div>
  <div class="ninode-card dict"><div class="role">Record</div><h4>namedtuple</h4>Tuple with names.<br><code>Point(x,y)</code></div>
  <div class="ninode-card cm"><div class="role">Order+</div><h4>OrderedDict</h4>Extra order helpers.<br>(dict keeps order 3.7+)</div>
</div>
""",
        )
        + sec(
            "3. Which helper?",
            """
<div class="dt-tree">
  <div class="dt-start">Need a collections helper?</div>
  <div class="dt-row">
    <div class="dt-q"><span class="dt-sit">Count items?</span><em>word frequency</em></div>
    <div class="dt-a"><div class="pick"><span class="tag tag-dd">Use</span> Counter</div></div>
  </div>
  <div class="dt-row">
    <div class="dt-q"><span class="dt-sit">Group in a loop?</span><em>auto empty list</em></div>
    <div class="dt-a"><div class="pick"><span class="tag tag-dict">Use</span> defaultdict</div></div>
  </div>
  <div class="dt-row">
    <div class="dt-q"><span class="dt-sit">Fast left &amp; right ends?</span><em>queue / buffer</em></div>
    <div class="dt-a"><div class="pick"><span class="tag tag-key">Use</span> deque</div></div>
  </div>
  <div class="dt-row">
    <div class="dt-q"><span class="dt-sit">Light named record?</span><em>x,y fields</em></div>
    <div class="dt-a"><div class="pick"><span class="tag tag-cm">Use</span> namedtuple</div></div>
  </div>
</div>
""",
        )
        + memory(
            "These are still Python objects — same shallow <code>getsizeof</code> idea.<br>"
            "<code>deque</code> is great for queues; list <code>pop(0)</code> is slow (O(n)).<br>"
            "<code>ChainMap</code> does not copy — it views layers.",
            "Interview: Counter is a dict subclass; defaultdict factory runs on missing key.<br>"
            "deque: O(1) append/pop both ends; optional <code>maxlen</code> ring buffer.<br>"
            "namedtuple: immutable, lighter than a full class; OrderedDict less needed post-3.7.",
        )
    )


def body_comprehensions() -> str:
    return (
        sec(
            "1. What is a comprehension?",
            p("A short way to build a list / set / dict (or a lazy generator) in one line."),
        )
        + sec(
            "2. Four shapes",
            grid(
                card("List", "<code>[n*n for n in nums]</code><br>Builds all results now."),
                card("Set", "<code>{n%2 for n in nums}</code><br>Unique results."),
                card("Dict", "<code>{n: n*n for n in nums}</code><br>Key &rarr; value."),
                card("Generator", "<code>(n*n for n in nums)</code><br>One at a time — lazy."),
            ),
        )
        + sec(
            "3. Kid rule",
            grid(
                card("Good", "Build a new collection from an old one."),
                card("Bad", "Print / write files inside a comprehension — use a normal <code>for</code> loop."),
            ),
        )
        + trap("<b>Watch out:</b> List comps keep <b>everything</b> in memory. Huge data? Use a generator expression.")
        + memory(
            "List/set/dict comps allocate the whole result up front.<br>"
            "Generator expression stores almost nothing — computes on demand.<br>"
            "<code>sys.getsizeof(list(...))</code> &gt;&gt; <code>sys.getsizeof((... for ...))</code>.",
            "Interview: comps are syntactic sugar over loops; prefer clarity if nested deep.<br>"
            "Memory: O(n) for list comp vs O(1) extra for generator when streaming.<br>"
            "Do not use comps for side effects.",
        )
        + sec(
            "4. Cheat sheet",
            cheat(
                [
                    ("List comp", "Build list", "<code>[x for x in a if x&gt;0]</code>"),
                    ("Set comp", "Build set", "<code>{x for x in a}</code>"),
                    ("Dict comp", "Build dict", "<code>{k:v for k,v in pairs}</code>"),
                    ("Gen exp", "Lazy stream", "<code>(x for x in a)</code>"),
                ]
            ),
        )
    )
