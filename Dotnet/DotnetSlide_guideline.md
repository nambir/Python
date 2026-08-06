# Dotnet Slide Guideline

Use this for every curriculum slide in `Dotnet/`.  
**Do not hand-edit** `Dotnet/DotnetTraining.html` — edit sources, then:

```powershell
cd D:\Sangeetha/Python
python Dotnet/build_dotnet_training.py
```

Open: `http://localhost:8765/Dotnet/DotnetTraining.html`

---

## Source files (one job each)

| File | Purpose |
|------|---------|
| `dotnet_meta.py` | Definition (`_def`) + interview script + skill id |
| `dotnet_flowcharts.py` | Decision flowchart (YES → stop / NO → down) |
| `dotnet_diagrams.py` | Memory / timeline / compare pictures |
| `dotnet_beginner.py` | Step-by-step + interview Q&A |
| `dotnet_content.py` | Learn body (mistakes, quiz, big picture) + right-panel `code(..., expected=...)` |
| `build_dotnet_training.py` | Generator |

Shared: `training_deck.py`, `slide_io.io_split`, `slide_code.code`, CSS from `build_training.py`.

---

## Slide template (order on the page)

1. **Header** — title + short subtitle (plain text from definition)  
2. **Definition** — Slide-2 style (see below)  
3. **Decision flowchart** — kid-friendly YES/NO  
4. **Diagram** — picture that makes the idea click faster  
5. **Step-by-step** — beginner steps with INPUT \| OUTPUT  
6. **Learn body** — tables, mistakes, quiz, takeaways  
7. **Interview Q&A**  
8. **Practice** checklist  
9. **Right panel** — C# code editor + expected OUTPUT + SharpLab  

---

## Definition style (prefer Slide 2)

**Pattern:** one story sentence first, then 3–5 bold-labeled bullets.

```python
"definition": _def(
    # Intro = the whole idea in one breath (why it exists)
    "By default a method is <b>synchronous</b> — it holds the thread until it finishes. "
    "Add the <code>async</code> keyword so the method can <b>release the thread</b> "
    "while waiting; when the result is ready, work <b>resumes</b>.",
    [
        "<b>Normal method:</b> …",
        "<b>Make it async:</b> …",
        "<b>Why:</b> …",
        "<b>Not:</b> …",   # common misconception
    ],
),
```

**Rules**

- Start from **what the learner already knows** (default / sync / normal), then the new keyword.  
- Bold the few words that carry meaning (`synchronous`, `release the thread`, `resumes`).  
- Put keywords in `<code>…</code>`.  
- Avoid dumping jargon first (no “state machine” until after the basic story).  
- Interview blurb = same story, spoken aloud in 3–4 sentences.

**Slide 1 should match this voice** (value vs reference as a story, not only a taxonomy list).

---

## INPUT \| OUTPUT (critical)

Always use `io_split(code, out_map)` from `slide_io`.

### Alignment rule

**Every console line’s result must sit on the same row as that `Console.WriteLine(...)`.**

```python
io_split(
    "int a = 10;\n"
    "int b = a;     // copy the value\n"
    "b = 99;\n"
    "Console.WriteLine(a);  // 10\n"          # line 4
    "\n"
    "var list1 = new List<int> { 1, 2 };\n"
    "var list2 = list1;   // copy REFERENCE\n"
    "list2.Add(3);\n"
    "Console.WriteLine(list1.Count);  // 3",  # line 9
    {4: "10", 9: "3"},
    out_label="# OUTPUT (same line as each WriteLine)",
)
```

### How to build `out_map`

1. Number lines **1-based** in the exact string you pass (after `\n` split).  
2. Put the printed value only on the WriteLine line — leave other lines blank in OUTPUT.  
3. Prefer a trailing comment `// 10` on the WriteLine for teaching.  
4. Do **not** put outputs on declaration lines.  
5. After edits, re-count lines (blank lines count).

### Label

Use:

```text
# OUTPUT (same line as each WriteLine)
```

(not “print” — this is C#).

### Step body recipe

1. One or two sentences (bold key terms).  
2. `io_split(...)` with aligned outputs.  
3. Optional `<p class="step-result"><b>Takeaway:</b> …</p>`.

---

## Flowchart

- Start box = learner goal in plain words.  
- Each question: **YES** → answer tile (stop); **NO** → go down.  
- End with a one-line fallback / “remember”.  
- Keep 3 questions max.

---

## Diagrams

Prefer pictures that answer “where is the data?” or “what happens over time?”:

| Topic | Good diagram |
|-------|----------------|
| Value vs reference | Stack vs heap side-by-side (arrows for references) |
| Boxing | Short flow: stack → heap → unbox |
| async/await | Cycle: Run → await (release) → Ready → Resume |
| Struct vs class | Compare columns |

Useful references (ideas only — rewrite in our style, don’t paste copyrighted UI):

- [Microsoft — Value types](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/value-types)  
- [Microsoft — Reference types](https://learn.microsoft.com/dotnet/csharp/language-reference/keywords/reference-types)  
- [Microsoft — async overview](https://learn.microsoft.com/dotnet/csharp/asynchronous-programming/)  
- [SharpLab](https://sharplab.io/) — live Run for demos  

---

## Quiz

```html
<div class="quiz-q"><b>Q1.</b> …?
  <details class="quiz-ans"><summary>Show answer</summary>
    <div class="quiz-reveal"><code>answer</code> &mdash; short why.</div>
  </details>
</div>
```

- Multi-line sample code → use `<div class="step-pre">` with **one statement per line**.  
- Keep answers short; lead with the answer in `<code>`.

---

## Right-panel code (`code(...)`)

- Prefer **runnable** top-level samples (`Console.WriteLine`).  
- Pass `expected="..."` so OUTPUT shows under the editor.  
- Expected lines must match what SharpLab would print (order matters).

```python
code(
    """int x = 1;\nConsole.WriteLine(x);""",
    expected="1",
)
```

---

## Checklist before merge

- [ ] Definition uses Slide-2 story style (`_def` intro + bullets)  
- [ ] Flowchart + diagram present  
- [ ] Every `io_split` WriteLine has matching `out_map` line  
- [ ] Quiz answers use `quiz-reveal` + `&mdash;`  
- [ ] Right panel has `expected=` for demos  
- [ ] `python Dotnet/build_dotnet_training.py` succeeded  
- [ ] Hard-refresh browser (not stale `file://`)  

---

## Skill matrix link

Map each slide to a CSV id (`D01`, `D06`, …) in `dotnet_meta.py` (`skill_id` / `area`).
