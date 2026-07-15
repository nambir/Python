"""Generate PythonBasics.html slide deck."""
from pathlib import Path
from slide_meta import SLIDE_META

OUTPUT = Path(__file__).parent / "PythonBasics.html"
TOTAL_SLIDES = 48

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { height: 100%; overflow: hidden; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #fff; color: #1a1a2e; }

.slide { display: none; width: 100%; height: 100vh; padding: 30px 50px 60px 50px; overflow-y: auto; position: relative; }
.slide.active { display: block; }

.slide-hdr { margin-bottom: 16px; }
.slide-meta { font-size: 10px; color: #999; letter-spacing: 1.5px; text-transform: uppercase; }
.slide-title { font-size: 28px; font-weight: 700; color: #1a1a2e; border-bottom: 3px solid #0066cc; padding-bottom: 6px; display: inline-block; }
.slide-sub { font-size: 14px; color: #555; margin-top: 3px; }

h3 { font-size: 16px; color: #0066cc; margin: 14px 0 6px 0; }
h4 { font-size: 14px; color: #333; margin: 10px 0 4px 0; }
p { font-size: 13px; margin-bottom: 6px; line-height: 1.5; }
ul { margin-left: 18px; margin-bottom: 8px; }
li { font-size: 12px; margin-bottom: 2px; line-height: 1.4; }
code { font-family: Consolas, 'Cascadia Mono', monospace; font-size: 12px; background: #f0f7ff; padding: 1px 4px; border-radius: 3px; color: #0000FF; }

.nav-bar { position: fixed; bottom: 0; left: 0; right: 0; height: 44px; background: #f0f0f0; border-top: 1px solid #ccc; display: flex; align-items: center; justify-content: space-between; padding: 0 50px; z-index: 999; }
.nav-bar button { padding: 6px 20px; font-size: 13px; font-weight: 600; border: none; border-radius: 4px; cursor: pointer; }
.nav-bar .btn-prev { background: #666; color: #fff; }
.nav-bar .btn-prev:hover { background: #444; }
.nav-bar .btn-next { background: #0066cc; color: #fff; }
.nav-bar .btn-next:hover { background: #004499; }
.nav-bar .btn-nav { background: #28a745; color: #fff; }
.nav-bar .btn-nav:hover { background: #1e7e34; }
.nav-bar .slide-info { font-size: 12px; color: #555; }

table, .ref-table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 12px; }
th { background: #0066cc; color: #fff; padding: 6px 10px; text-align: left; font-size: 11px; }
td { padding: 5px 10px; border-bottom: 1px solid #e8e8e8; }
tr:nth-child(even) { background: #f8fafc; }

.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 8px 0; }
.card { background: #fff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px; border-left: 3px solid #0066cc; }
.card-g { border-left-color: #28a745; }
.card-o { border-left-color: #f39c12; }
.card-p { border-left-color: #6f42c1; }
.card-r { border-left-color: #dc3545; }

.tip { background: #fff8e6; border-left: 3px solid #f39c12; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.challenge { background: #e8f5e9; border-left: 3px solid #28a745; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.callout { background: #f0f7ff; border-left: 3px solid #0066cc; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.def-box { background: #f8fafc; border: 1px solid #e2e8f0; border-left: 3px solid #333; border-radius: 6px; padding: 10px; margin: 8px 0; font-size: 12px; line-height: 1.5; }
.interview-box { background: #e8f5e9; border-left: 3px solid #28a745; padding: 8px 12px; border-radius: 4px; margin: 8px 0; font-size: 12px; }
.interview-box p { margin: 6px 0 0; line-height: 1.5; color: #1b5e20; font-style: italic; font-size: 12px; }

.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
.slide-layout { display: flex; flex-direction: column; gap: 12px; }
.explain-top { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
.explain-left h3:first-of-type, .explain-right h3:first-of-type { margin-top: 0; }
.practice-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.practice-bottom { grid-column: 1; }
.practice-panel { background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; padding: 14px; }
.practice-panel h3 { margin-top: 0; }
.checklist { list-style: none; margin: 8px 0 0 0; padding: 0; }
.checklist li { padding: 3px 0; font-size: 12px; }
.checklist li::before { content: "\\2610  "; color: #0066cc; }
.file-link { display: inline-block; margin-top: 8px; padding: 5px 12px; background: #0066cc; color: #fff; text-decoration: none; border-radius: 4px; font-size: 11px; font-weight: 600; }
.file-link:hover { background: #004499; }
.run-cmd { font-family: Consolas, monospace; background: #2d2d2d; color: #dcdcdc; padding: 8px 12px; border-radius: 4px; font-size: 11px; margin-top: 8px; display: block; }

pre.code { background: #fafafa; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 12px; overflow-x: auto; font-family: Consolas, 'Cascadia Mono', monospace; font-size: 12px; line-height: 1.45; margin: 8px 0; }
.kw { color: #0000FF; } .str { color: #A31515; } .cmt { color: #008000; }
.num { color: #098658; } .fn { color: #795E26; } .typ { color: #267F99; }

.nav-content { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: calc(100vh - 44px); padding: 20px; }
.nav-content h1 { font-size: 38px; color: #1a1a2e; margin-bottom: 4px; }
.nav-content .sub { font-size: 17px; color: #0066cc; margin-bottom: 4px; }
.nav-content .org { font-size: 13px; color: #666; margin-bottom: 30px; }
.nav-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; max-width: 900px; width: 100%; }
.nav-section { background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; padding: 14px; text-align: center; max-height: 420px; overflow-y: auto; }
.nav-section h3 { font-size: 13px; color: #1a1a2e; margin-bottom: 8px; border-bottom: 2px solid #0066cc; padding-bottom: 4px; }
.nav-section a { display: block; padding: 3px 0; color: #0066cc; text-decoration: none; font-size: 12px; cursor: pointer; text-align: left; }
.nav-section a:hover { text-decoration: underline; }

.qa-item { margin-bottom: 10px; font-size: 12px; }
.qa-item strong { color: #0066cc; display: block; margin-bottom: 3px; }

.tree-mockup { background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; padding: 12px 14px; margin: 8px 0; font-family: Consolas, 'Cascadia Mono', monospace; font-size: 11px; line-height: 1.55; overflow-x: auto; }
.tree-mockup .t-row { display: flex; align-items: baseline; flex-wrap: wrap; gap: 4px; padding: 1px 0; }
.tree-mockup .t-indent-1 { padding-left: 16px; }
.tree-mockup .t-indent-2 { padding-left: 32px; }
.tree-mockup .t-indent-3 { padding-left: 48px; }
.tree-mockup .t-indent-4 { padding-left: 64px; }
.tree-mockup .t-folder { color: #0066cc; font-weight: 700; }
.tree-mockup .t-file { color: #1a1a2e; }
.tree-mockup .t-config { color: #6f42c1; }
.tree-mockup .t-test { color: #28a745; font-weight: 600; }
.tree-mockup .t-note { color: #888; font-style: italic; font-family: 'Segoe UI', sans-serif; font-size: 10px; }
.tree-legend { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-top: 8px; font-size: 11px; }
.tree-legend span { display: flex; align-items: center; gap: 6px; }
.tree-legend .dot { width: 10px; height: 10px; border-radius: 2px; flex-shrink: 0; }
.dot-blue { background: #0066cc; } .dot-green { background: #28a745; }
.dot-purple { background: #6f42c1; } .dot-orange { background: #f39c12; }
.wireframe-compare { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 8px 0; }
.wireframe-box { border: 2px dashed #b3d4fc; border-radius: 8px; padding: 10px; background: #fff; }
.project-map { width: 100%; font-size: 11px; }
.project-map td:first-child { font-weight: 600; color: #0066cc; white-space: nowrap; }

@media (max-width: 700px) {
  .slide { padding: 20px 16px 60px; }
  .two-col, .cards, .nav-grid, .wireframe-compare, .tree-legend, .explain-top, .practice-row { grid-template-columns: 1fr; }
  .practice-bottom { grid-column: auto; }
  .nav-bar { padding: 0 16px; }
}
"""

JS = """
let current = 0;
const slideOrder = [0];
for (let i = 2; i <= """ + str(TOTAL_SLIDES) + """; i++) slideOrder.push(i);
const totalTopics = """ + str(TOTAL_SLIDES) + """;

function showSlide(n) {
  if (!slideOrder.includes(n)) return;
  document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
  const el = document.getElementById('slide-' + n);
  if (el) {
    el.classList.add('active');
    current = n;
    el.scrollTop = 0;
    const info = document.getElementById('slideInfo');
    if (info) info.textContent = n === 0 ? 'Navigation' : 'Slide ' + n + ' of ' + totalTopics;
  }
}

function goSlide(n) { showSlide(n); }

function nextSlide() {
  const idx = slideOrder.indexOf(current);
  if (idx < slideOrder.length - 1) showSlide(slideOrder[idx + 1]);
}

function prevSlide() {
  const idx = slideOrder.indexOf(current);
  if (idx > 0) showSlide(slideOrder[idx - 1]);
}

document.addEventListener('keydown', function(e) {
  if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
  if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
  if (e.key === 'Home') { e.preventDefault(); showSlide(0); }
});

function highlightAll() {
  const keywords = new Set(['False','True','None','and','as','assert','async','await','break',
    'class','continue','def','del','elif','else','except','finally','for','from','global',
    'if','import','in','is','lambda','nonlocal','not','or','pass','raise','return','try',
    'while','with','yield','self','print','len','range','type','int','str','float','bool',
    'list','dict','set','tuple','super','open','enum','isinstance']);
  document.querySelectorAll('pre.code').forEach(pre => {
    let html = pre.innerHTML;
    html = html.replace(/(#.*)$/gm, '<span class="cmt">$1</span>');
    html = html.replace(/(&quot;[^&]*?&quot;|'[^']*?')/g, '<span class="str">$1</span>');
    html = html.replace(/\\b(\\d+\\.?\\d*)\\b/g, '<span class="num">$1</span>');
    keywords.forEach(kw => {
      const re = new RegExp('\\\\b' + kw + '\\\\b', 'g');
      html = html.replace(re, '<span class="kw">' + kw + '</span>');
    });
    pre.innerHTML = html;
  });
}
document.addEventListener('DOMContentLoaded', () => { showSlide(0); highlightAll(); });
"""

NAV_BAR = """
<div class="nav-bar">
  <button class="btn-prev" onclick="prevSlide()">&larr; Prev</button>
  <button class="btn-nav" onclick="goSlide(0)">&#9776; Navigation</button>
  <span class="slide-info" id="slideInfo">Navigation</span>
  <button class="btn-next" onclick="nextSlide()">Next &rarr;</button>
</div>
"""

MODULE_MAP = {
    range(2, 17): "Python Basics",
    range(17, 21): "Python Basics · OOP",
    range(21, 27): "Python Basics",
    range(27, 32): "API · FastAPI",
    range(32, 37): "UI · Streamlit & Tkinter",
    range(37, 42): "Real Projects · Structure",
    range(42, 48): "Python-Set2 · Real Projects",
    range(48, 49): "Appendix",
}

def module_for(n):
    for r, name in MODULE_MAP.items():
        if n in r:
            return name
    return "Python"

def slide_subtitle(n):
    meta = SLIDE_META.get(n)
    if not meta:
        return ""
    d = meta["definition"]
    dot = d.find(".")
    return d[: dot + 1] if dot > 0 else d[:90]

def slide_hdr(n, title):
    mod = module_for(n)
    sub = slide_subtitle(n)
    return f'''<div class="slide-hdr">
  <div class="slide-meta">Slide {n} of {TOTAL_SLIDES} &middot; {mod}</div>
  <div class="slide-title">{title}</div>
  <div class="slide-sub">{sub}</div>
</div>'''

def code_block(text):
    return f'<pre class="code">{text}</pre>'

def tree_row(indent, icon, name, cls, note=""):
    note_html = f'<span class="t-note">— {note}</span>' if note else ""
    return f'<div class="t-row t-indent-{indent}"><span class="{cls}">{icon} {name}</span>{note_html}</div>'

def tree_mockup(rows_html, legend=True):
    leg = ""
    if legend:
        leg = '''<div class="tree-legend">
<span><span class="dot dot-blue"></span> Source / app code</span>
<span><span class="dot dot-green"></span> Tests</span>
<span><span class="dot dot-purple"></span> Config / env</span>
<span><span class="dot dot-orange"></span> Docs / scripts</span>
</div>'''
    return f'<div class="tree-mockup">{rows_html}{leg}</div>'

def topic_intro(n):
    meta = SLIDE_META.get(n)
    if not meta:
        return ""
    return (
        f'<h3>Definition</h3><p>{meta["definition"]}</p>'
        f'<div class="interview-box"><b>How to explain in interview:</b>'
        f'<p>&ldquo;{meta["interview"]}&rdquo;</p></div>'
    )

def learn_practice_slide(n, title, learn_html, practice_html):
    intro = topic_intro(n)
    return f'''<div class="slide" id="slide-{n}">
{slide_hdr(n, title)}
<div class="slide-layout">
  <div class="explain-top">
    <div class="explain-left">{intro}</div>
    <div class="explain-right">{learn_html}</div>
  </div>
  <div class="practice-row">
    <div class="practice-bottom practice-panel">
      <h3>Practice</h3>
      {practice_html}
    </div>
  </div>
</div>
</div>'''

SLIDES = []

# Content slides data: (num, title, learn, practice)
content = [
(2, "Welcome & Setup", '''
<p>Welcome! You know C# — Python will feel familiar yet simpler in syntax.</p>
<ul>
  <li>Install Python 3.11+ from <strong>python.org</strong></li>
  <li>Use VS Code or Cursor with Python extension</li>
  <li>Run scripts: <code>python filename.py</code></li>
  <li>REPL: type <code>python</code> in terminal</li>
</ul>
<div class="callout"><strong>Coming from C#?</strong> No semicolons, no curly braces, indentation matters. Python uses dynamic typing — no <code>int x = 5;</code> declaration needed.</div>
<div class="tip"><strong>Interview tip:</strong> Python is interpreted, dynamically typed, and strongly typed (no implicit string+int).</div>
''', '''
<h4>Setup Checklist</h4>
<ul class="checklist">
  <li>Install Python and verify: python --version</li>
  <li>Create folder d:\\Sangeetha\\Python\\Projects</li>
  <li>Open PythonBasics.html in browser</li>
  <li>Run first script on Slide 3</li>
</ul>
'''),

(3, "Hello World & Running Code", '''
<ul>
  <li><code>print()</code> = C# <code>Console.WriteLine()</code></li>
  <li>Scripts run top-to-bottom</li>
  <li><code>if __name__ == "__main__":</code> guards entry point</li>
</ul>
''' + code_block('''print("Hello, Python!")
name = "Alex"
print(f"Hi, {name}!")

if __name__ == "__main__":
    print("Script entry point")''') + '''
<div class="callout"><strong>Coming from C#?</strong> C# needs <code>static void Main()</code>. Python runs the file directly; the <code>__name__</code> guard is optional but professional.</div>
''', '''
<h4>Exercise: Hello World</h4>
<ul class="checklist">
  <li>Print "Hello, Python!"</li>
  <li>Print your name on line 2</li>
  <li>Print result of 2 + 3</li>
</ul>
<a class="file-link" href="Projects/03_hello_world.py">Projects/03_hello_world.py</a>
<span class="run-cmd">python Projects/03_hello_world.py</span>
'''),

(4, "Variables & Types", '''
<ul>
  <li>Assign with <code>x = 10</code> — no type keyword</li>
  <li><code>type(x)</code> checks runtime type</li>
  <li>Variables are references to objects</li>
</ul>
''' + code_block('''age = 25
price = 9.99
name = "Riya"
is_active = True
print(type(age))   # &lt;class 'int'&gt;''') + '''
<div class="callout"><strong>Coming from C#?</strong> C#: <code>int age = 25;</code> Python: <code>age = 25</code>. Types are checked at runtime, not compile time.</div>
<div class="tip"><strong>Interview tip:</strong> Python is dynamically typed but strongly typed — <code>"5" + 5</code> raises TypeError.</div>
''', '''
<h4>Exercise: Variables</h4>
<ul class="checklist">
  <li>Create int, float, str, bool variables</li>
  <li>Print type() of each</li>
  <li>Reassign age to a string — observe type change</li>
</ul>
<a class="file-link" href="Projects/04_variables.py">Projects/04_variables.py</a>
'''),

(5, "Strings", '''
<ul>
  <li>Immutable sequence of characters</li>
  <li>f-strings: <code>f"Hello {name}"</code></li>
  <li>Slicing: <code>s[0:3]</code>, <code>s[-1]</code></li>
  <li>Methods: .upper(), .split(), .replace()</li>
</ul>
''' + code_block('''text = "Python"
print(text[0:3])       # Pyt
print(f"Learn {text}!") # Learn Python!
print(len(text))''') + '''
<div class="callout"><strong>Coming from C#?</strong> C# has <code>$"Hello {name}"</code>. Python f-strings work the same way: <code>f"Hello {name}"</code>.</div>
''', '''
<h4>Exercise: Strings</h4>
<ul class="checklist">
  <li>Slice first 6 and last 4 chars</li>
  <li>Use an f-string greeting</li>
  <li>Call .upper() and .replace()</li>
</ul>
<a class="file-link" href="Projects/05_strings.py">Projects/05_strings.py</a>
'''),

(6, "Numbers & Math", '''
<ul>
  <li><code>/</code> always float division</li>
  <li><code>//</code> floor division, <code>%</code> modulo</li>
  <li><code>**</code> exponent, <code>divmod(a,b)</code></li>
</ul>
''' + code_block('''a, b = 17, 5
print(a / b)    # 3.4
print(a // b)   # 3
print(a % b)    # 2
print(a ** 2)   # 289''') + '''
<div class="callout"><strong>Coming from C#?</strong> C# <code>17 / 5</code> is 3 (int div). Python 3 <code>17 / 5</code> is 3.4. Use <code>//</code> for integer division.</div>
''', '''
<h4>Exercise: Numbers</h4>
<ul class="checklist">
  <li>Print /, //, %, ** for 17 and 5</li>
  <li>Use divmod()</li>
  <li>Round pi to 2 decimals</li>
</ul>
<a class="file-link" href="Projects/06_numbers.py">Projects/06_numbers.py</a>
'''),

(7, "Booleans & None", '''
<ul>
  <li><code>None</code> = C# <code>null</code></li>
  <li>Use <code>is None</code>, not <code>== None</code></li>
  <li>Truthiness: empty = False, non-empty = True</li>
</ul>
''' + code_block('''x = None
if x is None:
    print("No value")

print(bool(""))    # False
print(bool("hi"))  # True
print(bool(0))     # False''') + '''
<div class="tip"><strong>Interview trap:</strong> <code>bool("False")</code> is <code>True</code> — non-empty strings are truthy!</div>
''', '''
<h4>Exercise: Booleans</h4>
<ul class="checklist">
  <li>Print bool() of 8 different values</li>
  <li>Check None with "is"</li>
  <li>Predict bool("False") before running</li>
</ul>
<a class="file-link" href="Projects/07_booleans_none.py">Projects/07_booleans_none.py</a>
'''),

(8, "if / elif / else", '''
<ul>
  <li>No parentheses required (but allowed)</li>
  <li>Colon <code>:</code> + indented block</li>
  <li>Ternary: <code>x if cond else y</code></li>
</ul>
''' + code_block('''score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
status = "pass" if score >= 60 else "fail"''') + '''
<div class="callout"><strong>Coming from C#?</strong> C# uses <code>{ }</code> blocks. Python uses indentation (4 spaces standard). Mixing tabs/spaces causes errors.</div>
''', '''
<h4>Exercise: Conditionals</h4>
<ul class="checklist">
  <li>Assign letter grade from score</li>
  <li>Use ternary for pass/fail</li>
  <li>Check if score is 70–89</li>
</ul>
<a class="file-link" href="Projects/08_conditionals.py">Projects/08_conditionals.py</a>
'''),

(9, "Loops: for", '''
<ul>
  <li><code>for item in collection:</code> = C# foreach</li>
  <li><code>range(5)</code> → 0,1,2,3,4</li>
  <li><code>enumerate()</code> gives index + value</li>
</ul>
''' + code_block('''for i in range(1, 6):
    print(i * i)

fruits = ["apple", "banana"]
for i, f in enumerate(fruits):
    print(i, f)''') + '''
<div class="callout"><strong>Coming from C#?</strong> <code>foreach (var x in list)</code> → <code>for x in list:</code>. No index unless you use <code>enumerate</code>.</div>
''', '''
<h4>Exercise: for loops</h4>
<ul class="checklist">
  <li>enumerate() over fruits list</li>
  <li>Print squares 1–5 with range</li>
  <li>Sum a list manually</li>
</ul>
<a class="file-link" href="Projects/09_for_loops.py">Projects/09_for_loops.py</a>
'''),

(10, "Loops: while, break, continue", '''
<ul>
  <li><code>while condition:</code> same idea as C#</li>
  <li><code>break</code> exits loop, <code>continue</code> skips iteration</li>
  <li>Python loops can have <code>else</code> (runs if no break)</li>
</ul>
''' + code_block('''n = 5
while n > 0:
    print(n)
    n -= 1

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)''') + '''
<div class="callout"><strong>Coming from C#?</strong> No <code>i++</code> — use <code>i += 1</code>. No <code>--</code> operator either.</div>
''', '''
<h4>Exercise: while loops</h4>
<ul class="checklist">
  <li>Countdown 5 to 1 with while</li>
  <li>Skip multiples of 3 with continue</li>
  <li>Find first number &gt; 50 with break</li>
</ul>
<a class="file-link" href="Projects/10_while_loops.py">Projects/10_while_loops.py</a>
'''),

(11, "Lists", '''
<ul>
  <li>Mutable, ordered — like <code>List&lt;T&gt;</code></li>
  <li>append, insert, pop, sort, reverse</li>
  <li>Slicing creates new list: <code>nums[1:3]</code></li>
</ul>
''' + code_block('''nums = [10, 20, 30]
nums.append(40)
nums.insert(0, 5)
print(nums[1:3])
print(nums[::-1])  # reverse''') + '''
<div class="tip"><strong>Interview tip:</strong> Lists are mutable. Slicing returns a copy — safe to modify.</div>
''', '''
<h4>Exercise: Lists</h4>
<ul class="checklist">
  <li>append, insert, pop operations</li>
  <li>Slice middle elements</li>
  <li>Reverse with [::-1]</li>
</ul>
<a class="file-link" href="Projects/11_lists.py">Projects/11_lists.py</a>
'''),

(12, "Tuples & Sets", '''
<ul>
  <li><strong>Tuple</strong> — immutable, ordered: <code>(1, 2, 3)</code></li>
  <li><strong>Set</strong> — unique, unordered: <code>{1, 2, 3}</code></li>
  <li>Sets support union <code>|</code>, intersection <code>&</code></li>
</ul>
''' + code_block('''coords = (10, 20, 30)
x, y, z = coords          # unpacking

unique = set([1,2,2,3])
a, b = {1,2,3}, {3,4,5}
print(a | b)  # union''') + '''
<div class="callout"><strong>Coming from C#?</strong> C# ValueTuple is similar. Python tuples are lightweight and hashable (can be dict keys).</div>
''', '''
<h4>Exercise: Tuples & Sets</h4>
<ul class="checklist">
  <li>Unpack a 3-value tuple</li>
  <li>Remove duplicates with set()</li>
  <li>Union and intersection of two sets</li>
</ul>
<a class="file-link" href="Projects/12_tuples_sets.py">Projects/12_tuples_sets.py</a>
'''),

(13, "Dictionaries", '''
<ul>
  <li>Key-value pairs — like <code>Dictionary&lt;K,V&gt;</code></li>
  <li><code>.get(key, default)</code> safe lookup</li>
  <li>Dict comprehension: <code>{k: v for ...}</code></li>
</ul>
''' + code_block('''student = {"name": "Riya", "age": 22}
student["city"] = "Chennai"
grade = student.get("grade", "N/A")

squares = {n: n*n for n in range(1, 6)}''') + '''
<div class="tip"><strong>Interview tip:</strong> Keys must be hashable (str, int, tuple — not list).</div>
''', '''
<h4>Exercise: Dictionaries</h4>
<ul class="checklist">
  <li>Add a new key to student dict</li>
  <li>Safe .get() with default</li>
  <li>Dict comprehension for squares</li>
</ul>
<a class="file-link" href="Projects/13_dictionaries.py">Projects/13_dictionaries.py</a>
'''),

(14, "Functions", '''
<ul>
  <li><code>def name(params):</code> — no access modifiers</li>
  <li>Default args: <code>def f(x, y=10)</code></li>
  <li><code>*args</code> tuple, <code>**kwargs</code> dict</li>
</ul>
''' + code_block('''def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

def add_all(*args):
    return sum(args)

print(greet("Sam"))
print(add_all(1, 2, 3))''') + '''
<div class="tip"><strong>Interview trap:</strong> Never use mutable default args like <code>def f(x, lst=[])</code> — shared across calls!</div>
''', '''
<h4>Exercise: Functions</h4>
<ul class="checklist">
  <li>Write greet() with default greeting</li>
  <li>Write add_all(*args)</li>
  <li>Fix mutable default arg bug</li>
</ul>
<a class="file-link" href="Projects/14_functions.py">Projects/14_functions.py</a>
'''),

(15, "Lambda, map, filter", '''
<ul>
  <li><code>lambda x: x * 2</code> — anonymous one-liner</li>
  <li><code>map(fn, iterable)</code> — transform each</li>
  <li><code>filter(fn, iterable)</code> — keep matches</li>
</ul>
''' + code_block('''nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2==0, nums))

pairs = [("amy",1), ("bob",3)]
pairs.sort(key=lambda p: p[1])''') + '''
<div class="callout"><strong>Coming from C#?</strong> Similar to LINQ <code>.Select()</code> and <code>.Where()</code>. List comprehensions are often preferred in Python.</div>
''', '''
<h4>Exercise: Lambda & map</h4>
<ul class="checklist">
  <li>Double nums with map</li>
  <li>Filter evens only</li>
  <li>Sort pairs by second element</li>
</ul>
<a class="file-link" href="Projects/15_lambda_map_filter.py">Projects/15_lambda_map_filter.py</a>
'''),

(16, "Comprehensions", '''
<ul>
  <li>List: <code>[x*2 for x in nums if x%2==0]</code></li>
  <li>Set: <code>{c for c in chars}</code></li>
  <li>Dict: <code>{w: len(w) for w in words}</code></li>
</ul>
''' + code_block('''squares = [n*n for n in range(1,11) if n%2==0]
letters = {w[0] for w in ["python","code"]}
lengths = {w: len(w) for w in words}''') + '''
<div class="tip"><strong>Interview tip:</strong> Comprehensions are idiomatic Python — faster to write and often faster to run than map/filter.</div>
''', '''
<h4>Exercise: Comprehensions</h4>
<ul class="checklist">
  <li>Even squares list comp</li>
  <li>Set comp for first letters</li>
  <li>Dict comp for word lengths</li>
</ul>
<a class="file-link" href="Projects/16_comprehensions.py">Projects/16_comprehensions.py</a>
'''),

(17, "OOP — Four Pillars Overview", '''
<p>Object-Oriented Programming (OOP) groups <b>data</b> and <b>behavior</b> into objects. Python supports all four pillars — slightly differently from C#.</p>
<table>
<tr><th>Pillar</th><th>Meaning</th><th>Python</th><th>C#</th><th>Slide</th></tr>
<tr><td><b>Encapsulation</b></td><td>Hide internal data; expose methods</td><td><code>_private</code> convention, <code>@property</code></td><td><code>private</code>, properties</td><td>18</td></tr>
<tr><td><b>Inheritance</b></td><td>Reuse parent class code</td><td><code>class Dog(Animal)</code></td><td><code>class Dog : Animal</code></td><td>19</td></tr>
<tr><td><b>Polymorphism</b></td><td>Same method, different behavior</td><td>Override methods; duck typing</td><td><code>override</code>, interfaces</td><td>19</td></tr>
<tr><td><b>Abstraction</b></td><td>Hide complexity; show essentials</td><td><code>ABC</code>, abstract methods, duck typing</td><td><code>abstract</code>, interfaces</td><td>20</td></tr>
</table>
<div class="callout"><b>Interview answer:</b> &ldquo;Python is object-oriented — everything is an object, even integers and functions. I use classes for encapsulation, inheritance with super(), polymorphism by overriding methods, and abstraction with ABC or duck typing.&rdquo;</div>
''', '''
<h4>OOP self-check</h4>
<ul class="checklist">
  <li>Name all 4 OOP pillars from memory</li>
  <li>Match each pillar to slides 18, 19, 20</li>
  <li>Explain one C# vs Python OOP difference</li>
</ul>
<div class="tip">Next 3 slides deep-dive each pillar with code practice.</div>
'''),

(18, "OOP — Classes, Objects & Encapsulation", '''
<ul>
  <li><b>Class</b> = blueprint; <b>object</b> = instance created from class</li>
  <li><code>self</code> = C# <code>this</code> (must be explicit first parameter)</li>
  <li><b>Encapsulation:</b> bundle data + methods; hide internals with <code>_name</code> convention</li>
  <li><code>@property</code> = controlled getter (like C# property get/set)</li>
</ul>
''' + code_block('''class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0          # "private" by convention

    def deposit(self, amount):
        self._balance += amount

    @property
    def balance(self):
        return self._balance

acct = BankAccount("Riya")
acct.deposit(100)
print(acct.balance)  # 100 — no direct _balance access''') + '''
<div class="callout"><b>Coming from C#?</b> No <code>public/private</code> keywords. Use <code>_</code> prefix for internal use; <code>__</code> (dunder) for name mangling (rare).</div>
''', '''
<h4>Exercise: Encapsulation</h4>
<ul class="checklist">
  <li>Build Person with __init__ and introduce()</li>
  <li>Add "private" <code>_age</code> with a method to read it</li>
  <li>Create 2 instances and call introduce()</li>
</ul>
<a class="file-link" href="Projects/17_classes.py">Projects/17_classes.py</a>
'''),

(19, "OOP — Inheritance & Polymorphism", '''
<ul>
  <li><b>Inheritance:</b> <code>class Dog(Animal):</code> reuses parent code</li>
  <li><code>super().__init__()</code> calls parent constructor</li>
  <li><b>Polymorphism:</b> override <code>speak()</code> — same call, different output per type</li>
  <li><b>Duck typing:</b> &ldquo;if it walks and quacks like a duck…&rdquo; — no interface required</li>
</ul>
''' + code_block('''class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

for pet in [Dog(), Cat()]:      # polymorphism
    print(pet.speak())''') + '''
<div class="tip"><b>Interview tip:</b> Python supports <b>multiple inheritance</b>. Know MRO (Method Resolution Order). C# uses single inheritance + interfaces instead.</div>
''', '''
<h4>Exercise: Inheritance & Polymorphism</h4>
<ul class="checklist">
  <li>Dog extends Animal, override speak() → "Woof!"</li>
  <li>Use super().__init__(name) in Dog</li>
  <li>Loop a list of animals — print each speak()</li>
</ul>
<a class="file-link" href="Projects/18_inheritance.py">Projects/18_inheritance.py</a>
'''),

(20, "OOP — Abstraction & Magic Methods", '''
<ul>
  <li><b>Abstraction:</b> hide implementation — use <code>ABC</code> + <code>@abstractmethod</code> (like C# abstract class)</li>
  <li><b>Duck typing:</b> any object with the right methods works — no formal interface</li>
  <li><b>Magic methods:</b> <code>__str__</code>, <code>__repr__</code>, <code>__eq__</code> (like ToString, Equals)</li>
</ul>
''' + code_block('''from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return f"Book: {self.title}"''') + '''
<div class="callout"><b>Coming from C#?</b> C# <code>interface IShape</code> → Python <code>ABC</code> or duck typing. <code>__str__</code> ≈ <code>ToString()</code>, <code>__eq__</code> ≈ <code>Equals()</code>.</div>
''', '''
<h4>Exercise: Abstraction & Magic Methods</h4>
<ul class="checklist">
  <li>Implement __str__ and __repr__ on Book</li>
  <li>Implement __eq__ comparing title</li>
  <li>Optional: create Shape ABC with Circle subclass</li>
</ul>
<a class="file-link" href="Projects/19_magic_methods.py">Projects/19_magic_methods.py</a>
'''),

(21, "Modules & Imports", '''
<ul>
  <li><code>import math</code> — whole module</li>
  <li><code>from utils import add</code> — specific names</li>
  <li><code>__name__ == "__main__"</code> when run directly</li>
</ul>
''' + code_block('''import math
from my_utils import add, greet

print(math.sqrt(16))
print(greet("Dev"))
print(__name__)  # __main__ if direct''') + '''
<div class="callout"><strong>Coming from C#?</strong> <code>using System;</code> → <code>import os</code>. Python modules are just .py files.</div>
''', '''
<h4>Exercise: Modules</h4>
<ul class="checklist">
  <li>Import from my_utils.py</li>
  <li>Import math, print sqrt(144)</li>
  <li>Print __name__ when run directly</li>
</ul>
<a class="file-link" href="Projects/20_modules/main.py">Projects/20_modules/main.py</a>
<span class="run-cmd">python Projects/20_modules/main.py</span>
'''),

(22, "File I/O", '''
<ul>
  <li><code>open(path, "r")</code> read, <code>"w"</code> write, <code>"a"</code> append</li>
  <li><code>with open(...) as f:</code> auto-closes file</li>
  <li>Always specify <code>encoding="utf-8"</code></li>
</ul>
''' + code_block('''with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello\\n")
    f.write("Python\\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())''') + '''
<div class="callout"><strong>Coming from C#?</strong> Like <code>using (var reader = ...)</code>. Python <code>with</code> is a context manager — same idea.</div>
''', '''
<h4>Exercise: File I/O</h4>
<ul class="checklist">
  <li>Write 3 lines to a file</li>
  <li>Read back with line numbers</li>
  <li>Append a 4th line</li>
</ul>
<a class="file-link" href="Projects/21_file_io.py">Projects/21_file_io.py</a>
'''),

(23, "Exceptions", '''
<ul>
  <li><code>try / except / finally</code> = C# try/catch/finally</li>
  <li>Catch specific: <code>except ValueError:</code></li>
  <li><code>raise</code> to throw exceptions</li>
</ul>
''' + code_block('''try:
    n = int("abc")
except ValueError:
    print("Invalid number")

def set_age(age):
    if age < 0:
        raise ValueError("Negative age")
    return age''') + '''
<div class="tip"><strong>Interview tip:</strong> Catch specific exceptions, not bare <code>except:</code>. Use <code>finally</code> for cleanup.</div>
''', '''
<h4>Exercise: Exceptions</h4>
<ul class="checklist">
  <li>try/except converting strings to int</li>
  <li>Raise ValueError for negative age</li>
  <li>Create custom TooSmallError class</li>
</ul>
<a class="file-link" href="Projects/22_exceptions.py">Projects/22_exceptions.py</a>
'''),

(24, "Common Stdlib", '''
<ul>
  <li><code>os</code> — paths, environment, cwd</li>
  <li><code>json</code> — serialize/deserialize</li>
  <li><code>datetime</code> — dates and timedelta</li>
</ul>
''' + code_block('''import json, os
from datetime import datetime, timedelta

data = {"lang": "Python"}
js = json.dumps(data)
restored = json.loads(js)
print(os.getcwd())
print(datetime.now() + timedelta(days=7))''') + '''
<div class="callout"><strong>Coming from C#?</strong> <code>System.Text.Json</code> → <code>json</code>. <code>DateTime</code> → <code>datetime</code>.</div>
''', '''
<h4>Exercise: Stdlib</h4>
<ul class="checklist">
  <li>Print current working directory</li>
  <li>JSON serialize and parse a dict</li>
  <li>Print date 7 days from today</li>
</ul>
<a class="file-link" href="Projects/23_stdlib_demo.py">Projects/23_stdlib_demo.py</a>
'''),

(25, "Top Interview Patterns", '''
<ul>
  <li>Reverse string / list</li>
  <li>Character frequency count</li>
  <li>FizzBuzz (classic warm-up)</li>
  <li>Two-sum with hash map</li>
</ul>
''' + code_block('''def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        need = target - v
        if need in seen:
            return [seen[need], i]
        seen[v] = i
    return []''') + '''
<div class="tip"><strong>Interview tip:</strong> Dict lookup is O(1) — use it for frequency and two-sum patterns.</div>
''', '''
<h4>Exercise: Patterns</h4>
<ul class="checklist">
  <li>Reverse a string manually</li>
  <li>Count char frequency in a string</li>
  <li>Implement FizzBuzz 1–15</li>
  <li>Implement two_sum()</li>
</ul>
<a class="file-link" href="Projects/24_interview_patterns.py">Projects/24_interview_patterns.py</a>
'''),

(26, "Mock Interview Q&A", '''
<div class="qa-item"><strong>Q: List vs Tuple?</strong> List is mutable, tuple is immutable. Tuples can be dict keys.</div>
<div class="qa-item"><strong>Q: == vs is?</strong> == compares values, is compares identity (same object in memory).</div>
<div class="qa-item"><strong>Q: Mutable default argument?</strong> Default values evaluated once. Use None instead of [].</div>
<div class="qa-item"><strong>Q: What is GIL?</strong> Global Interpreter Lock — one thread executes Python bytecode at a time. Matters for CPU-bound threading.</div>
<div class="qa-item"><strong>Q: *args and **kwargs?</strong> Collect extra positional (*tuple) and keyword (**dict) arguments.</div>
''', '''
<h4>Self-Test (answer aloud)</h4>
<ul class="checklist">
  <li>Explain list vs tuple in 30 seconds</li>
  <li>Explain == vs is with example</li>
  <li>Describe the mutable default trap</li>
  <li>What is a context manager?</li>
  <li>How does for-loop else work?</li>
</ul>
<div class="tip"><strong>Tip:</strong> Practice explaining out loud — interviews test communication too.</div>
'''),

# API Module
(27, "HTTP & REST Basics", '''
<ul>
  <li>REST uses HTTP verbs: GET, POST, PUT, DELETE</li>
  <li>Status codes: 200 OK, 201 Created, 404 Not Found, 500 Error</li>
  <li>JSON is the standard data format for APIs</li>
</ul>
''' + code_block('''import requests

r = requests.get("https://api.example.com/users/1")
print(r.status_code)
data = r.json()
print(data["name"])

r = requests.post(url, json={"name": "Alex"})''') + '''
<div class="callout"><strong>Coming from C#?</strong> Like calling APIs with <code>HttpClient</code>. <code>requests</code> is the most popular HTTP library.</div>
''', '''
<h4>Exercise: HTTP Requests</h4>
<ul class="checklist">
  <li>GET a post from JSONPlaceholder</li>
  <li>Print status_code and title</li>
  <li>POST a new item with json=</li>
</ul>
<a class="file-link" href="Projects/26_http_requests.py">Projects/26_http_requests.py</a>
<span class="run-cmd">pip install requests &amp;&amp; python Projects/26_http_requests.py</span>
'''),

(28, "FastAPI — Hello API", '''
<ul>
  <li>FastAPI = modern Python web framework (like ASP.NET Web API)</li>
  <li>Decorator routes: <code>@app.get("/path")</code></li>
  <li>Auto-generates Swagger docs at /docs</li>
</ul>
''' + code_block('''from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting": f"Hello, {name}!"}''') + '''
<div class="callout"><strong>Coming from C#?</strong> <code>[HttpGet("users/{id}")]</code> → <code>@app.get("/users/{id}")</code>. Returns dict → auto JSON.</div>
''', '''
<h4>Exercise: Hello API</h4>
<ul class="checklist">
  <li>Create GET /hello/{name}</li>
  <li>Add GET /health endpoint</li>
  <li>Test in browser at /docs</li>
</ul>
<a class="file-link" href="Projects/27_fastapi_hello/main.py">Projects/27_fastapi_hello/main.py</a>
<span class="run-cmd">cd Projects/27_fastapi_hello &amp;&amp; uvicorn main:app --reload</span>
'''),

(29, "FastAPI — POST & Validation", '''
<ul>
  <li>Pydantic models validate request bodies (like DTOs)</li>
  <li>Type hints drive validation and docs</li>
  <li>Invalid data returns 422 automatically</li>
</ul>
''' + code_block('''from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=2)
    email: str
    age: int = Field(ge=0, le=120)

@app.post("/users")
def create_user(user: User):
    return {"user": user}''') + '''
<div class="callout"><strong>Coming from C#?</strong> Pydantic models ≈ C# record/DTO classes with DataAnnotations validation.</div>
''', '''
<h4>Exercise: POST API</h4>
<ul class="checklist">
  <li>Define User model with validation</li>
  <li>POST /users creates a user</li>
  <li>GET /users lists all users</li>
</ul>
<a class="file-link" href="Projects/28_fastapi_post/main.py">Projects/28_fastapi_post/main.py</a>
<span class="run-cmd">cd Projects/28_fastapi_post &amp;&amp; uvicorn main:app --reload</span>
'''),

(30, "FastAPI — CRUD Mini API", '''
<ul>
  <li>CRUD = Create, Read, Update, Delete</li>
  <li>PUT updates, DELETE removes, POST creates</li>
  <li>HTTPException for 404 errors</li>
</ul>
''' + code_block('''from fastapi import HTTPException

@app.post("/todos", status_code=201)
def create_todo(todo: Todo):
    ...

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    raise HTTPException(404, "Not found")''') + '''
<div class="tip"><strong>Interview tip:</strong> Know REST conventions — nouns for resources, verbs via HTTP methods, proper status codes.</div>
''', '''
<h4>Exercise: Todo CRUD</h4>
<ul class="checklist">
  <li>Implement full CRUD for todos</li>
  <li>Test all endpoints in Swagger /docs</li>
  <li>Return 404 for missing items</li>
</ul>
<a class="file-link" href="Projects/29_fastapi_crud/main.py">Projects/29_fastapi_crud/main.py</a>
<span class="run-cmd">cd Projects/29_fastapi_crud &amp;&amp; uvicorn main:app --reload</span>
'''),

(31, "API Interview Q&A", '''
<div class="qa-item"><strong>Q: REST vs GraphQL?</strong> REST uses fixed endpoints per resource. GraphQL uses one endpoint with client-defined queries.</div>
<div class="qa-item"><strong>Q: Idempotent methods?</strong> GET, PUT, DELETE are idempotent. POST is not (creates new each time).</div>
<div class="qa-item"><strong>Q: 401 vs 403?</strong> 401 = not authenticated. 403 = authenticated but not authorized.</div>
<div class="qa-item"><strong>Q: Design a URL shortener API?</strong> POST /links {url} → {short_code}, GET /{code} → redirect.</div>
<div class="qa-item"><strong>Q: async in FastAPI?</strong> Use async def for I/O-bound work. Sync def is fine for CPU-light CRUD.</div>
''', '''
<h4>Design Challenge</h4>
<ul class="checklist">
  <li>Sketch endpoints for a Book Store API</li>
  <li>Choose status codes for each operation</li>
  <li>Define request/response JSON shapes</li>
  <li>Explain how you'd add pagination</li>
</ul>
'''),

# UI Module
(32, "UI Options in Python", '''
<table class="ref-table">
<tr><th>Approach</th><th>Library</th><th>C# Parallel</th><th>Best For</th></tr>
<tr><td>Web UI (quick)</td><td>Streamlit</td><td>Blazor/Razor</td><td>Dashboards, prototypes</td></tr>
<tr><td>Desktop UI</td><td>Tkinter</td><td>WinForms/WPF</td><td>Simple desktop apps</td></tr>
<tr><td>Web UI (full)</td><td>Flask + HTML</td><td>ASP.NET MVC</td><td>Custom web apps</td></tr>
<tr><td>API backend</td><td>FastAPI</td><td>ASP.NET Web API</td><td>REST services</td></tr>
</table>
<div class="callout"><strong>Coming from C#?</strong> You likely used WinForms/WPF or Blazor. In Python interviews, Streamlit + FastAPI is a powerful combo to demo quickly.</div>
''', '''
<h4>Choose Your Path</h4>
<ul class="checklist">
  <li>Slides 32–33: Streamlit (web UI)</li>
  <li>Slide 34: Tkinter (desktop)</li>
  <li>Slide 35: Full-stack capstone</li>
</ul>
<span class="run-cmd">pip install -r Projects/requirements-ui.txt</span>
'''),

(33, "Streamlit — First App", '''
<ul>
  <li>Pure Python — no HTML/CSS/JS needed</li>
  <li><code>st.title()</code>, <code>st.button()</code>, <code>st.text_input()</code></li>
  <li>Runs as local web app in browser</li>
</ul>
''' + code_block('''import streamlit as st

st.title("My App")
name = st.text_input("Your name")
if st.button("Say Hello"):
    st.success(f"Hello, {name}!")

age = st.slider("Age", 18, 60, 25)''') + '''
<div class="callout"><strong>Coming from C#?</strong> Like building a Blazor page but with zero markup — every widget is a Python function call.</div>
''', '''
<h4>Exercise: Streamlit App</h4>
<ul class="checklist">
  <li>Add text_input for name</li>
  <li>Button shows greeting</li>
  <li>Slider for age 18–60</li>
</ul>
<a class="file-link" href="Projects/32_streamlit_app.py">Projects/32_streamlit_app.py</a>
<span class="run-cmd">streamlit run Projects/32_streamlit_app.py</span>
'''),

(34, "Streamlit — Call Your API", '''
<ul>
  <li>UI layer calls REST API with requests</li>
  <li>Form submits POST, button triggers refresh</li>
  <li>Separate frontend (Streamlit) from backend (FastAPI)</li>
</ul>
''' + code_block('''import requests, streamlit as st

API = "http://127.0.0.1:8000"
todos = requests.get(f"{API}/todos").json()

with st.form("add"):
    title = st.text_input("Todo")
    if st.form_submit_button("Add"):
        requests.post(f"{API}/todos",
            json={"title": title})''') + '''
<div class="tip"><strong>Interview tip:</strong> Decoupling UI and API shows you understand architecture — same as Angular/React + .NET API.</div>
''', '''
<h4>Exercise: API Client UI</h4>
<ul class="checklist">
  <li>Start Todo API (slide 29)</li>
  <li>Display todos from GET /todos</li>
  <li>Form to add new todo via POST</li>
</ul>
<a class="file-link" href="Projects/33_streamlit_api_client/app.py">Projects/33_streamlit_api_client/app.py</a>
<span class="run-cmd">streamlit run Projects/33_streamlit_api_client/app.py</span>
'''),

(35, "Tkinter — Desktop UI", '''
<ul>
  <li>Built into Python (no pip install on Windows)</li>
  <li>Window, widgets, event loop pattern</li>
  <li><code>root.mainloop()</code> starts the app</li>
</ul>
''' + code_block('''import tkinter as tk

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, font=("Consolas", 18))
display.pack()

def on_click(char):
    display.insert(tk.END, char)

tk.Button(root, text="7",
    command=lambda: on_click("7")).pack()
root.mainloop()''') + '''
<div class="callout"><strong>Coming from C#?</strong> Very similar to WinForms — drag-less code UI. Button click = event handler / command callback.</div>
''', '''
<h4>Exercise: Calculator</h4>
<ul class="checklist">
  <li>Build 4x4 button grid</li>
  <li>Display shows input/output</li>
  <li>= evaluates expression</li>
</ul>
<a class="file-link" href="Projects/34_tkinter_calc.py">Projects/34_tkinter_calc.py</a>
<span class="run-cmd">python Projects/34_tkinter_calc.py</span>
'''),

(36, "Full-Stack Capstone Project", '''
<p>Combine everything: <strong>FastAPI backend</strong> + <strong>Streamlit frontend</strong> = Todo app.</p>
<ul>
  <li>API on port 8001 with CRUD + toggle</li>
  <li>UI displays, adds, toggles, deletes todos</li>
  <li>Two terminals — one for each service</li>
</ul>
''' + code_block('''# Terminal 1 (api folder):
# uvicorn main:app --reload --port 8001

# Terminal 2 (ui folder):
# streamlit run app.py''') + '''
<div class="tip"><strong>Interview tip:</strong> Walk through this project end-to-end. It demonstrates Python basics, API design, and UI — a complete story.</div>
''', '''
<h4>Capstone: Build & Demo</h4>
<ul class="checklist">
  <li>Start API on port 8001</li>
  <li>Start Streamlit UI</li>
  <li>Add 3 todos, toggle one, delete one</li>
  <li>Explain architecture to a friend</li>
</ul>
<a class="file-link" href="Projects/35_mini_project/api/main.py">Projects/35_mini_project/api/</a>
<a class="file-link" href="Projects/35_mini_project/ui/app.py">Projects/35_mini_project/ui/</a>
'''),

# Module 4 — Real Project Structure
(37, "Why Real Project Structure?", '''
<p>In interviews, employers expect you to explain <b>how a real Python project is organized</b> — not just single <code>.py</code> files.</p>
<ul>
  <li><b>Separation of concerns</b> — routes, business logic, data, config stay separate</li>
  <li><b>Team collaboration</b> — everyone knows where to add code</li>
  <li><b>Testability</b> — tests mirror app structure in <code>tests/</code></li>
  <li><b>Deployability</b> — config via <code>.env</code>, dependencies in <code>requirements.txt</code></li>
</ul>
<div class="callout"><b>Coming from C#?</b> Python <code>app/api/routes/</code> ≈ C# <code>Controllers/</code>. <code>services/</code> ≈ business layer. <code>schemas/</code> ≈ DTOs. <code>models/</code> ≈ EF entities.</div>
<div class="wireframe-compare">
  <div class="wireframe-box"><h4>Learning (this course)</h4><p style="font-size:11px;text-align:center">One file per topic<br><code>03_hello_world.py</code></p></div>
  <div class="wireframe-box"><h4>Real job project</h4><p style="font-size:11px;text-align:center">Folders by responsibility<br><code>app/api/routes/todos.py</code></p></div>
</div>
''', '''
<h4>Interview warm-up</h4>
<ul class="checklist">
  <li>Explain difference: script vs structured project</li>
  <li>Name 4 folders in a real API project</li>
  <li>Why keep tests in a separate <code>tests/</code> folder?</li>
</ul>
<div class="tip">Next slides show wireframe trees — study them like an architecture diagram.</div>
'''),

(38, "Learning Project Structure (Wireframe)", '''
<p>Your <code>Projects/</code> folder follows a <b>numbered learning layout</b> — great for practice, not for production.</p>
''' + tree_mockup(
    tree_row(0, "📁", "Python/", "t-folder", "root workspace") +
    tree_row(1, "📁", "Projects/", "t-folder", "all practice exercises") +
    tree_row(2, "📄", "03_hello_world.py", "t-file", "single-topic script") +
    tree_row(2, "📄", "14_functions.py", "t-file", "single-topic script") +
    tree_row(2, "📁", "27_fastapi_hello/", "t-folder", "small multi-file demo") +
    tree_row(3, "📄", "main.py", "t-file", "entry point only") +
    tree_row(2, "📁", "35_mini_project/", "t-folder", "mini full-stack") +
    tree_row(3, "📁", "api/", "t-folder", "backend") +
    tree_row(4, "📄", "main.py", "t-file", "FastAPI app") +
    tree_row(3, "📁", "ui/", "t-folder", "frontend") +
    tree_row(4, "📄", "app.py", "t-file", "Streamlit UI") +
    tree_row(1, "📄", "PythonBasics.html", "t-file", "slide deck") +
    tree_row(1, "📄", "build_deck.py", "t-file", "regenerate slides")
) + '''
<table>
<tr><th>Pattern</th><th>Purpose</th><th>When to use</th></tr>
<tr><td><code>NN_topic.py</code></td><td>One concept per file</td><td>Learning, interviews practice</td></tr>
<tr><td><code>topic/main.py</code></td><td>Mini app in subfolder</td><td>API/UI demos</td></tr>
<tr><td><code>api/ + ui/</code></td><td>Split backend & frontend</td><td>Capstone projects</td></tr>
</table>
''', '''
<h4>Map your current folder</h4>
<ul class="checklist">
  <li>Open <code>Projects/</code> in File Explorer</li>
  <li>Find 3 single-file exercises (slides 3–24)</li>
  <li>Find 2 folder-based projects (27, 35)</li>
  <li>Draw this tree on paper from memory</li>
</ul>
<a class="file-link" href="Projects/">Open Projects/</a>
'''),

(39, "FastAPI Production Structure (Wireframe)", '''
<p>Industry-standard FastAPI projects group code by <b>responsibility</b> (layered) or by <b>feature</b> (domain). Below is the most common interview answer — <b>layered structure</b>.</p>
''' + tree_mockup(
    tree_row(0, "📁", "todo-api/", "t-folder", "project root") +
    tree_row(1, "📁", "app/", "t-folder", "all application source") +
    tree_row(2, "📄", "main.py", "t-file", "creates FastAPI app, mounts routers") +
    tree_row(2, "📁", "api/", "t-folder", "HTTP layer (like Controllers)") +
    tree_row(3, "📁", "routes/", "t-folder", "endpoint files") +
    tree_row(4, "📄", "todos.py", "t-file", "@router.get/post — thin handlers") +
    tree_row(2, "📁", "schemas/", "t-folder", "Pydantic DTOs (request/response)") +
    tree_row(3, "📄", "todo.py", "t-file", "TodoCreate, TodoResponse models") +
    tree_row(2, "📁", "services/", "t-folder", "business logic") +
    tree_row(3, "📄", "todo_service.py", "t-file", "create, list, delete rules") +
    tree_row(2, "📁", "models/", "t-folder", "database table classes (SQLAlchemy)") +
    tree_row(3, "📄", "todo.py", "t-file", "Todo table definition") +
    tree_row(2, "📁", "core/", "t-folder", "settings, security, logging") +
    tree_row(3, "📄", "config.py", "t-file", "reads .env variables") +
    tree_row(1, "📁", "tests/", "t-test", "pytest tests mirror app/") +
    tree_row(2, "📄", "test_todos.py", "t-test", "API endpoint tests") +
    tree_row(1, "📄", "requirements.txt", "t-config", "pip dependencies") +
    tree_row(1, "📄", ".env.example", "t-config", "sample secrets (no real keys)") +
    tree_row(1, "📄", "README.md", "t-file", "how to run the project") +
    tree_row(1, "📄", ".gitignore", "t-config", "ignore .env, __pycache__")
) + '''
<div class="tip"><b>Interview answer:</b> &ldquo;Routes stay thin — they validate input and call services. Services hold business rules. Models talk to the database. Schemas define API contracts.&rdquo;</div>
''', '''
<h4>Explore template</h4>
<ul class="checklist">
  <li>Open <code>Projects/real_project_template/</code></li>
  <li>Read each file's header comment (purpose)</li>
  <li>Trace: route → service → schema flow</li>
  <li>Run: <code>uvicorn app.main:app --reload</code></li>
</ul>
<a class="file-link" href="Projects/real_project_template/">real_project_template/</a>
<span class="run-cmd">cd Projects/real_project_template && uvicorn app.main:app --reload</span>
'''),

(40, "Full-Stack Monorepo Structure (Wireframe)", '''
<p>When API + UI + scripts live in <b>one repository</b> (monorepo), folders are split by <b>deployable service</b>.</p>
''' + tree_mockup(
    tree_row(0, "📁", "my-todo-product/", "t-folder", "one git repo") +
    tree_row(1, "📁", "backend/", "t-folder", "FastAPI service (deploy to server)") +
    tree_row(2, "📁", "app/", "t-folder", "same layered structure as slide 39") +
    tree_row(2, "📄", "requirements.txt", "t-config", "fastapi, uvicorn, pydantic") +
    tree_row(2, "📄", "Dockerfile", "t-config", "container image for API") +
    tree_row(1, "📁", "frontend/", "t-folder", "Streamlit or React UI") +
    tree_row(2, "📄", "app.py", "t-file", "calls backend via HTTP") +
    tree_row(2, "📄", "requirements.txt", "t-config", "streamlit, requests") +
    tree_row(1, "📁", "shared/", "t-folder", "optional shared constants/types") +
    tree_row(1, "📁", "docs/", "t-folder", "architecture diagrams, API notes") +
    tree_row(2, "📄", "architecture.md", "t-file", "wireframe & data flow") +
    tree_row(1, "📁", "scripts/", "t-folder", "dev helpers") +
    tree_row(2, "📄", "run_dev.ps1", "t-file", "start API + UI together") +
    tree_row(1, "📄", "docker-compose.yml", "t-config", "run all services locally") +
    tree_row(1, "📄", ".env.example", "t-config", "API_URL, DB connection")
) + '''
<div class="callout"><b>Data flow wireframe:</b><br>
<code>Browser → frontend/app.py → HTTP → backend/app/api/routes → service → DB</code><br>
Each box maps to a folder. Interviewers love when you draw this left-to-right.</div>
''', '''
<h4>Compare to your capstone</h4>
<ul class="checklist">
  <li>Open <code>Projects/35_mini_project/</code></li>
  <li>Relabel <code>api/</code> as <code>backend/</code> mentally</li>
  <li>Relabel <code>ui/</code> as <code>frontend/</code></li>
  <li>Draw the data-flow arrow diagram on paper</li>
</ul>
<a class="file-link" href="Projects/35_mini_project/">35_mini_project/</a>
'''),

(41, "Create a Real Project — Step by Step", '''
<h3>Step-by-step (do once before interview)</h3>
<table>
<tr><th>Step</th><th>Action</th><th>File / Folder</th></tr>
<tr><td>1</td><td>Create project root</td><td><code>mkdir my-api && cd my-api</code></td></tr>
<tr><td>2</td><td>Add dependency list</td><td><code>requirements.txt</code></td></tr>
<tr><td>3</td><td>Add environment template</td><td><code>.env.example</code> (never commit real .env)</td></tr>
<tr><td>4</td><td>Create app package</td><td><code>app/__init__.py</code></td></tr>
<tr><td>5</td><td>Entry point</td><td><code>app/main.py</code> — FastAPI()</td></tr>
<tr><td>6</td><td>Routes (thin)</td><td><code>app/api/routes/todos.py</code></td></tr>
<tr><td>7</td><td>DTOs</td><td><code>app/schemas/todo.py</code></td></tr>
<tr><td>8</td><td>Business logic</td><td><code>app/services/todo_service.py</code></td></tr>
<tr><td>9</td><td>Tests</td><td><code>tests/test_todos.py</code></td></tr>
<tr><td>10</td><td>Document how to run</td><td><code>README.md</code></td></tr>
</table>
''' + code_block('''# app/main.py — entry point
from fastapi import FastAPI
from app.api.routes import todos

app = FastAPI(title="My API")
app.include_router(todos.router, prefix="/todos")

# Run: uvicorn app.main:app --reload''') + '''
<div class="challenge"><b>Interview Q: &ldquo;Walk me through your project structure.&rdquo;</b><br>
Start at root → app/ → explain each subfolder purpose → show main.py → one route file → mention tests/ and .env.</div>
''', '''
<h4>Hands-on: scaffold from template</h4>
<ul class="checklist">
  <li>Copy <code>real_project_template/</code> to <code>my-first-api/</code></li>
  <li>Rename project in README.md</li>
  <li>Add one new endpoint in routes/todos.py</li>
  <li>Explain each folder aloud in 2 minutes</li>
</ul>
<span class="run-cmd">xcopy /E /I Projects\\real_project_template Projects\\my-first-api</span>
<a class="file-link" href="Projects/real_project_template/README.md">Template README</a>
'''),

# Module 5 — Python-Set2 Real Projects
(42, "Python-Set2 — Portfolio Overview", '''
<p><b>Python-Set2</b> is your real project library — six top-level areas that map directly to this deck.</p>
<table class="project-map">
<tr><th>Folder</th><th>What it teaches</th><th>Deck slides</th></tr>
<tr><td>pythonBasics/</td><td>OOP, collections, loops, modules, exceptions, pytest</td><td>09–14, 17–20, 22–24</td></tr>
<tr><td>google-python-exercises/</td><td>File I/O, regex, string parsing</td><td>21, 23</td></tr>
<tr><td>pandas/</td><td>Jupyter, DataFrames, CSV analysis</td><td>25 (stdlib) + data roles</td></tr>
<tr><td>djangobasics/</td><td>Django MVC, templates, JWT API</td><td>27–31 (compare to FastAPI)</td></tr>
<tr><td>DjangoRestBasics/</td><td>Django REST Framework serializers</td><td>27–29 (REST patterns)</td></tr>
<tr><td>Pipecat-Project/</td><td>Voice AI, WebRTC, FastAPI + Pipecat</td><td>27–31, 42–47</td></tr>
</table>
''' + tree_mockup(
    tree_row(0, "📁", "Python-Set2/", "t-folder", "your portfolio root") +
    tree_row(1, "📁", "pythonBasics/", "t-folder", "7 topic modules") +
    tree_row(1, "📁", "google-python-exercises/", "t-folder", "4 classic exercises") +
    tree_row(1, "📁", "pandas/", "t-folder", "Jupyter + CSV") +
    tree_row(1, "📁", "djangobasics/meeting_planner/", "t-folder", "Django + JWT") +
    tree_row(1, "📁", "DjangoRestBasics/inventory/", "t-folder", "DRF REST API") +
    tree_row(1, "📁", "Pipecat-Project/", "t-folder", "Voice AI POCs")
) + '''
<div class="callout"><strong>Interview angle:</strong> &ldquo;I have a structured portfolio — basics in pythonBasics/, web APIs in Django and FastAPI-style projects, data in pandas notebooks, and a voice-AI POC with Pipecat.&rdquo;</div>
''', '''
<h4>Explore the portfolio</h4>
<ul class="checklist">
  <li>Open <code>Python-Set2/</code> in VS Code / Cursor</li>
  <li>Pick one folder per week — basics → exercises → Django → Pipecat</li>
  <li>For each project, write a 2-minute verbal walkthrough</li>
</ul>
<a class="file-link" href="Python-Set2/">Python-Set2 root</a>
'''),

(43, "pythonBasics — Topic Modules", '''
<p>Seven self-contained modules — each folder is a mini-project with runnable examples.</p>
<table class="project-map">
<tr><th>Module</th><th>Topics</th><th>Maps to slide</th></tr>
<tr><td>MyClass</td><td>classes, __init__, inheritance, properties</td><td>17–20 OOP</td></tr>
<tr><td>MyCollections</td><td>list, dict, set, tuple, comprehensions</td><td>11–13</td></tr>
<tr><td>MyLoops</td><td>for, while, range, enumerate</td><td>09–10</td></tr>
<tr><td>MyModules</td><td>import, packages, __name__</td><td>21</td></tr>
<tr><td>MyExceptionHandling</td><td>try/except, raise, custom errors</td><td>23</td></tr>
<tr><td>MyDebug</td><td>pdb, logging, breakpoints</td><td>24</td></tr>
<tr><td>MyUnitTesting</td><td>unittest / pytest patterns</td><td>24</td></tr>
</table>
''' + tree_mockup(
    tree_row(0, "📁", "pythonBasics/", "t-folder") +
    tree_row(1, "📁", "MyClass/", "t-folder", "OOP demos") +
    tree_row(1, "📁", "MyCollections/", "t-folder", "list, dict, set") +
    tree_row(1, "📁", "MyLoops/", "t-folder", "iteration") +
    tree_row(1, "📁", "MyModules/", "t-folder", "imports") +
    tree_row(1, "📁", "MyExceptionHandling/", "t-folder", "errors") +
    tree_row(1, "📁", "MyDebug/", "t-folder", "debugging") +
    tree_row(1, "📁", "MyUnitTesting/", "t-green", "tests")
) + '''
<div class="challenge"><b>Interview Q:</b> &ldquo;Show me OOP in Python.&rdquo;<br>
Open <code>MyClass/</code> — explain class vs instance, <code>self</code>, and one inheritance example aloud.</div>
''', '''
<h4>Practice: one module per day</h4>
<ul class="checklist">
  <li>Run scripts in MyClass/ — explain each class</li>
  <li>Complete MyCollections/ exercises</li>
  <li>Write one pytest in MyUnitTesting/</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/MyClass/">MyClass</a>
<a class="file-link" href="Python-Set2/pythonBasics/MyUnitTesting/">MyUnitTesting</a>
'''),

(44, "Google Exercises &amp; Pandas Data", '''
<h3>google-python-exercises/</h3>
<p>Classic Google Python exercises — file manipulation, regex, and string parsing (interview favorites).</p>
<table class="project-map">
<tr><th>Exercise</th><th>Skill</th></tr>
<tr><td>basic/</td><td>Lists, strings, logic puzzles</td></tr>
<tr><td>babynames/</td><td>Regex, file parsing, dict counting</td></tr>
<tr><td>copyspecial/</td><td>os, shutil, file system traversal</td></tr>
<tr><td>logpuzzle/</td><td>HTTP, image stitching, algorithms</td></tr>
</table>
<h3>pandas/</h3>
<p>Jupyter notebooks for real-world CSV analysis — Titanic survival and FIFA stats.</p>
<ul>
<li><b>MyJupyterBasics.ipynb</b> — DataFrame intro, read_csv, head(), describe()</li>
<li><b>Pandas_TitanicData.ipynb</b> — filtering, groupby, missing values</li>
<li><b>Pandas_FIFAData.ipynb</b> — sorting, aggregation, visualization hooks</li>
</ul>
<div class="callout"><strong>C# parallel:</strong> pandas DataFrames ≈ LINQ on in-memory tables; Jupyter ≈ interactive C# script / LINQPad.</div>
''', '''
<h4>Run exercises</h4>
<ul class="checklist">
  <li>Complete babynames/ — practice regex aloud</li>
  <li>Open Pandas_TitanicData.ipynb in Jupyter</li>
  <li>Explain one groupby result in plain English</li>
</ul>
<span class="run-cmd">jupyter notebook Python-Set2/pandas/Pandas_TitanicData.ipynb</span>
<a class="file-link" href="Python-Set2/google-python-exercises/babynames/">babynames</a>
<a class="file-link" href="Python-Set2/pandas/Pandas_TitanicData.ipynb">Titanic notebook</a>
'''),

(45, "Django &amp; Django REST Projects", '''
<p>Two full web projects — compare to FastAPI slides 27–31. Django uses <b>MVT</b> (Model-View-Template); DRF adds REST serializers.</p>
<h3>djangobasics/meeting_planner/</h3>
''' + tree_mockup(
    tree_row(0, "📁", "meeting_planner/", "t-folder", "Django 4 project") +
    tree_row(1, "📄", "manage.py", "t-file", "entry point") +
    tree_row(1, "📁", "meeting/", "t-folder", "models, views, templates") +
    tree_row(1, "📁", "myauth/", "t-folder", "login / auth views") +
    tree_row(1, "📁", "meetingapi_simplejwt/", "t-folder", "JWT REST API") +
    tree_row(1, "📁", "mywebsite/", "t-folder", "static + welcome pages"),
    legend=False
) + '''
<h3>DjangoRestBasics/inventory/</h3>
''' + tree_mockup(
    tree_row(0, "📁", "inventory/", "t-folder", "DRF multi-app API") +
    tree_row(1, "📁", "drink/", "t-folder", "Model + Serializer + ViewSet") +
    tree_row(1, "📁", "merchant/", "t-folder", "nested resources") +
    tree_row(1, "📁", "supplier/", "t-folder", "CRUD endpoints") +
    tree_row(1, "📁", "core/", "t-folder", "shared models"),
    legend=False
) + '''
<div class="challenge"><b>Interview Q:</b> &ldquo;Django vs FastAPI?&rdquo;<br>
Django = batteries-included (ORM, admin, auth, templates). FastAPI = lean async API with Pydantic. Both expose REST — Django via DRF, FastAPI natively.</div>
''', '''
<h4>Run Django projects</h4>
<ul class="checklist">
  <li>cd meeting_planner → python manage.py runserver</li>
  <li>Explore meeting/models.py and migrations/</li>
  <li>Compare drink/serializers.py to FastAPI Pydantic schemas</li>
</ul>
<span class="run-cmd">cd Python-Set2/djangobasics/meeting_planner && python manage.py runserver</span>
<a class="file-link" href="Python-Set2/djangobasics/meeting_planner/meeting/models.py">Meeting models</a>
<a class="file-link" href="Python-Set2/DjangoRestBasics/inventory/drink/serializers.py">DRF serializers</a>
'''),

(46, "Pipecat — Voice AI POCs", '''
<p><b>Pipecat-Project/</b> demonstrates real-time voice pipelines: STT → LLM → TTS over WebRTC, built in phases.</p>
<table class="project-map">
<tr><th>POC folder</th><th>Purpose</th></tr>
<tr><td>pipecat-quickstart</td><td>Official Pipecat clone — cloud STT/LLM/TTS</td></tr>
<tr><td>pipecat-voice-phase1</td><td>Local STT/LLM/TTS services + simple UI</td></tr>
<tr><td>pipecat-voice-phase2</td><td>Full Pipecat framework pipeline (step 1–8)</td></tr>
<tr><td>voice-bouncer</td><td>IVR-style voice auth demo (member ID, zip)</td></tr>
<tr><td>Pipecat-Learning/</td><td>HTML tutorials + PipecatLearning.html</td></tr>
</table>
''' + tree_mockup(
    tree_row(0, "📁", "Pipecat-Project/POC/", "t-folder") +
    tree_row(1, "📁", "pipecat-quickstart/", "t-folder", "cloud services") +
    tree_row(1, "📁", "pipecat-voice-phase1/", "t-folder", "local services") +
    tree_row(1, "📁", "pipecat-voice-phase2/", "t-folder", "full pipeline") +
    tree_row(1, "📁", "voice-bouncer/", "t-folder", "voice auth IVR") +
    tree_row(1, "📁", "Pipecat-Learning/", "t-file", "learning HTML")
) + '''
<div class="callout"><strong>Architecture:</strong> FastAPI backend + Pipecat processors + WebRTC client — same layered thinking as slides 37–41, but for streaming audio instead of JSON REST.</div>
''', '''
<h4>Voice AI practice</h4>
<ul class="checklist">
  <li>Read POC/Readme.md for phase overview</li>
  <li>Run voice-bouncer step1_greeting.py</li>
  <li>Open PipeCatLearningContent/PipecatAI.html</li>
</ul>
<a class="file-link" href="Python-Set2/Pipecat-Project/POC/Readme.md">POC Readme</a>
<a class="file-link" href="Python-Set2/Pipecat-Project/POC/voice-bouncer/README.md">voice-bouncer</a>
<a class="file-link" href="Python-Set2/Pipecat-Project/PipeCatLearningContent/PipecatAI.html">PipecatAI guide</a>
'''),

(47, "Python-Set2 — Learning Path &amp; Interview Map", '''
<h3>Suggested study order</h3>
<table>
<tr><th>Week</th><th>Focus</th><th>Folder</th></tr>
<tr><td>1</td><td>Core Python</td><td>pythonBasics/ + google-python-exercises/basic/</td></tr>
<tr><td>2</td><td>OOP + tests</td><td>MyClass/ + MyUnitTesting/</td></tr>
<tr><td>3</td><td>Data</td><td>pandas/ notebooks</td></tr>
<tr><td>4</td><td>Web APIs</td><td>meeting_planner/ + inventory/ + Projects/ FastAPI</td></tr>
<tr><td>5</td><td>Voice AI</td><td>Pipecat-Project/POC/ (phase1 → phase2)</td></tr>
</table>
<h3>What to say in interviews</h3>
<ul>
<li><b>Basics:</b> &ldquo;I practiced in pythonBasics/ — seven modules covering OOP through pytest.&rdquo;</li>
<li><b>APIs:</b> &ldquo;I built REST with Django REST Framework and FastAPI — I know serializers vs Pydantic.&rdquo;</li>
<li><b>Data:</b> &ldquo;I analyzed Titanic and FIFA datasets in Jupyter with pandas.&rdquo;</li>
<li><b>Advanced:</b> &ldquo;I prototyped a voice pipeline with Pipecat — STT, LLM, TTS over WebRTC.&rdquo;</li>
</ul>
<div class="callout"><strong>Tip:</strong> Keep 2–3 projects demo-ready. Depth on one project beats listing ten you barely ran.</div>
''', '''
<h4>Final Set2 checklist</h4>
<ul class="checklist">
  <li>Ran at least one script from each top-level folder</li>
  <li>Can draw meeting_planner app structure from memory</li>
  <li>Explained Pipecat STT→LLM→TTS flow in 60 seconds</li>
  <li>Linked Set2 work to deck slides during mock interview</li>
</ul>
<a class="file-link" href="Python-Set2/pythonBasics/">pythonBasics</a>
<a class="file-link" href="Python-Set2/Pipecat-Project/">Pipecat-Project</a>
'''),

# Appendix
(48, "C# vs Python Quick Reference", '''
<table class="ref-table">
<tr><th>Concept</th><th>C#</th><th>Python</th></tr>
<tr><td>Print</td><td>Console.WriteLine()</td><td>print()</td></tr>
<tr><td>Variable</td><td>int x = 5;</td><td>x = 5</td></tr>
<tr><td>Foreach</td><td>foreach (var i in list)</td><td>for i in list:</td></tr>
<tr><td>Class</td><td>class Person { }</td><td>class Person:</td></tr>
<tr><td>Constructor</td><td>public Person() { }</td><td>def __init__(self):</td></tr>
<tr><td>Null</td><td>null</td><td>None</td></tr>
<tr><td>Interface</td><td>interface IRepo { }</td><td>ABC or duck typing</td></tr>
<tr><td>Namespace</td><td>using System;</td><td>import module</td></tr>
<tr><td>Web API</td><td>[HttpGet] controller</td><td>@app.get() FastAPI</td></tr>
<tr><td>UI</td><td>WinForms / Blazor</td><td>Tkinter / Streamlit</td></tr>
<tr><td>Exceptions</td><td>try/catch</td><td>try/except</td></tr>
<tr><td>String format</td><td>$"Hello {name}"</td><td>f"Hello {name}"</td></tr>
</table>
<div class="callout"><strong>You made it!</strong> 48 slides — basics, OOP, API, UI, project structure, and Python-Set2 real projects. Review slides 17–20, 42–47, and 37–41 before your interview. Good luck!</div>
''', '''
<h4>Final Checklist</h4>
<ul class="checklist">
  <li>Completed all Projects/ exercises</li>
  <li>Ran FastAPI and Streamlit apps</li>
  <li>Can explain 5 oral Q&A answers</li>
  <li>Built the capstone todo project</li>
  <li>Reviewed this cheat sheet</li>
</ul>
'''),
]

def nav_link(num, title):
    return f'<a onclick="goSlide({num})">{num}. {title}</a>'

def build_index(slides):
    by_num = {n: t for n, t, _, _ in slides}
    def links(start, end):
        return "".join(nav_link(n, by_num[n]) for n in range(start, end + 1))
    return f'''<div class="slide active" id="slide-0">
<div class="nav-content">
  <h1>Python Basics</h1>
  <div class="sub">Interview Prep &middot; For C# Developers</div>
  <div class="org">Click a topic below to jump to that slide</div>
  <div class="nav-grid">
    <div class="nav-section">
      <h3>Module 1 — Python Basics</h3>
      {links(2, 14)}
    </div>
    <div class="nav-section">
      <h3>Python Basics (continued)</h3>
      {links(15, 16)}
    </div>
    <div class="nav-section">
      <h3>OOP — Object-Oriented Programming</h3>
      {links(17, 20)}
    </div>
    <div class="nav-section">
      <h3>Python Basics (modules &amp; more)</h3>
      {links(21, 26)}
    </div>
    <div class="nav-section">
      <h3>Module 2 — API (FastAPI)</h3>
      {links(26, 30)}
    </div>
    <div class="nav-section">
      <h3>Module 3 — UI (Streamlit &amp; Tkinter)</h3>
      {links(31, 35)}
    </div>
    <div class="nav-section">
      <h3>Module 4 — Real Project Structure</h3>
      {links(37, 41)}
    </div>
    <div class="nav-section">
      <h3>Module 5 — Python-Set2 Real Projects</h3>
      {links(42, 47)}
    </div>
    <div class="nav-section">
      <h3>Appendix</h3>
      {nav_link(48, by_num[48])}
    </div>
  </div>
</div>
</div>'''

SLIDES.append(build_index(content))

for num, title, learn, practice in content:
    SLIDES.append(learn_practice_slide(num, title, learn, practice))

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Python Basics — Interview Prep</title>
<style>{CSS}</style>
</head>
<body>
{"".join(SLIDES)}
{NAV_BAR}
<script>{JS}</script>
</body>
</html>
'''

OUTPUT.write_text(html, encoding="utf-8")
print(f"Generated {OUTPUT} ({len(html):,} bytes, {len(SLIDES)} slides)")
