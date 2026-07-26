# Python Training & Review — Authoring Rules

Use these rules when creating or updating:

- **Training** slides → `PythonTraining.html` (beginner steps, code, interview Q&A)
- **Review** questions → `PythonReview.html` (kid-friendly model answers, MyAnswer, deep dives)
- **Cross-updates** — when Review teaches something new, mirror it on the related Training topic

Goal: **every explanation should be understandable by a beginner**, with matching examples; regenerate HTML from sources (never hand-edit generated files).

---

## Training deck

Use these rules when creating or updating slides in `PythonTraining.html`.
Goal: **every slide should be explainable by a beginner**, step by step, with matching code and interview Q&A.

---

## 1. File map (what lives where)

| File | Purpose |
|------|---------|
| `build_training.py` | Generator — layout, CSS, `CONTENT` tuples, calls `python build_training.py` |
| `training_meta.py` | Short **Definition** paragraph per slide (1–30) |
| `training_beginner.py` | **Step-by-step** explanations + **Interview Q&A** per slide |
| `slide_glossary.py` | "Key terms explained" table (Term \| Meaning \| Example) |
| `slide_keyword_deepdives.py` | **Python keywords — deeper look** blocks (pass-style) per slide |
| `slide_scenarios.py` | "When to use which" scenario tables |
| `Projects/*.py` | Runnable practice files linked from each slide |
| `PythonTraining.html` | **Generated output — do not edit by hand** |

Regenerate after any source change:

```powershell
python D:\Sangeetha\Python\build_training.py
```

---

## 2. Slide layout (left panel)

Order on every topic slide:

1. **Definition** — one short paragraph (`training_meta.py`)
2. **Step-by-step (beginner)** — numbered steps (`training_beginner.py`)
3. **Key terms explained** — glossary table (`slide_glossary.py`)
4. **When to use which** — scenario table (`slide_scenarios.py`, where applicable)
5. **Topic-specific tables** — e.g. immutable works/fails (`CONTENT` in `build_training.py`)
6. **Interview — questions & answers** — Q&A pairs (`training_beginner.py`)
7. **Practice** — checklist + `Projects/` links

Right panel: **code only** — VS2022-style highlighted Python.

---

## 3. Step-by-step rules (beginner voice)

Each slide must have **4–6 steps** in `training_beginner.py`:

- **Step 1** — Start with the simplest real-world idea ("what is this?").
- **Step 2** — Show the smallest working example.
- **Step 3** — Explain one common mistake or "why it works this way".
- **Step 4** — Contrast with something they already know (list vs tuple, C# vs Python).
- **Step 5+** — Alternatives, when to use, or interview one-liner.

Writing style:

- Use **plain English** — no jargon without defining it in the same sentence.
- One idea per step — if you need "and also", split into two steps.
- Use **concrete examples** (shopping cart, GPS, phone book) before abstract terms.
- Put code snippets in backticks in the text: `` `t[0] = 5` ``.
- Say **what happens** when code runs: "You get `TypeError`" not just "it's wrong".

---

## 4. Interview Q&A rules

Each slide must have **2–4 Q&A pairs** in `training_beginner.py`:

```python
"interview_qa": [
    {"q": "Short interview question?", "a": "Beginner-friendly answer in 2–4 sentences."},
]
```

Rules:

- **Q** = what an interviewer actually asks (not "explain tuple").
- **A** = first person ("I use…") or direct teaching voice — complete sentences.
- Include **one example** or **one error message** in at least one answer per slide.
- For technical slides, include: *what it is*, *when to use*, *common trap*.

Do **not** use a single long quoted paragraph anymore — use structured Q&A.

---

## 5. Code panel rules (right side)

Code in `CONTENT` must mirror the steps on the left:

```python
# ── STEP 1: What is a dict key? ──
grid = {}
grid[(1, 2)] = "treasure"

# ── STEP 2: Why list fails ──
# grid[[1, 2]] = "x"    # TypeError: unhashable type: 'list'
```

Rules:

- Section headers: `# ── STEP N: short title ──` matching left-panel steps.
- Comment out lines that **fail on purpose**; add `# WHY: ...` on the next line.
- Runnable code first; failing examples commented with expected error.
- Keep one concept per section — max ~15 lines per section.
- Sync with `Projects/NN_topic.py` — same examples, runnable with `python Projects/...`.

---

## 6. Glossary rules (`slide_glossary.py`)

For each important term on the slide:

| Column | Content |
|--------|---------|
| Term | Bold concept name |
| Meaning | Beginner definition + **Works** / **Does NOT work** / **Why** where relevant |
| Example | One-line code |

Immutable-style depth is the **target** for hard concepts (hashable, GIL, decorator, etc.).

---

## 7. Scenario table rules (`slide_scenarios.py`)

Three columns: **Situation** | **Use** | **Reason**

Example: "Fixed GPS coordinate" → **tuple** → "Immutable — cannot change by mistake"

---

## 8. Practice section rules

- 3–4 checklist items — hands-on, tied to step numbers.
- Link to `Projects/` file(s) from `SLIDE_PROJECT_FILES` in `build_training.py`.
- Include `run-cmd` when a script exists: `python Projects/01_datatypes.py`

---

## 9. Slide numbering (30 topics)

| # | Topic |
|---|--------|
| 1 | What is Python? |
| 2 | Setup & Run on Windows |
| 3 | Python Datatypes |
| 4 | Your Training Workspace |
| 5 | Operators |
| 6 | Flow Control |
| 7 | Comprehensions |
| 8 | Functions |
| 9 | Built-in Functions |
| 10 | OOP |
| 11 | Decorators |
| 12 | Descriptors |
| 13 | Generators |
| 14 | Type Hints |
| 15 | File Operations |
| 16 | Exceptions |
| 17 | Regular Expressions |
| 18 | Collections |
| 19 | Unit Testing |
| 20 | Threading |
| 21 | Context Managers |
| 22 | Async |
| 23 | venv |
| 24–29 | Python-Set2 projects |
| 30 | C# vs Python appendix |

---

## 9. CSV curriculum alignment (`csv_curriculum.py`)

Source file: `Python Training 2026 Batch 2.csv` — 20 core topics.

| CSV # | Deck slide | Topic |
|-------|------------|--------|
| 1 | 3 | Python Datatypes (incl. frozenset) |
| 2 | 5 | Operators |
| … | … | … |
| 20 | 23 | Virtual Environment |

Every CSV sub-topic must appear as at least one **Step N** in `training_beginner.py` for that slide.
Check coverage: `csv_curriculum.py` → `CSV_TOPICS` dict.

---

## 10. Migration checklist (per slide)

When upgrading an existing slide to beginner format:

- [ ] Add/update `steps` in `training_beginner.py`
- [ ] Add/update `interview_qa` in `training_beginner.py`
- [ ] Align `CONTENT` code sections with `# ── STEP N ──` headers
- [ ] Update `Projects/*.py` to match
- [ ] Expand glossary rows for confusing terms
- [ ] Run `python build_training.py` and spot-check in browser

**Gold-standard reference:** Slide 3 (Python Datatypes) — 10-step sequence:

1. Primitive types → 2. Collections table → 3. List vs tuple → 4. Dictionary → 5. Dict key → 6. Keys must not change → 7. List key error → 8. Dict key error → 9. Tuple solution → 10. Summary table.

Do **not** introduce "hashable" in step 1 — build up to it in step 6 as "keys must not change".

---

## 11. What we already have vs what to expand

**Already in repo:**

- All 30 slide titles, definitions, code blocks, glossary, scenarios
- `Projects/` practice files for slides 1–22
- Python-Set2 links for slides 24–29
- VS2022 code panel, left/right layout, navigation

**Expand per slide (this ruleset):**

- Beginner step-by-step in `training_beginner.py`
- Interview Q&A (replacing single paragraph)
- Code section headers aligned to steps
- Deeper glossary for tricky terms (like Immutable on slide 3)

---

## 12. Do not

- Edit `PythonTraining.html` directly — always regenerate.
- Use one giant interview paragraph — use Q&A.
- Add jargon without a beginner sentence first.
- Commit secrets (`.env`, API keys) in `Projects/` or slides.

---

## 13. Python Review deck (kid-friendly + MyAnswer)

Use these rules when updating `PythonReview.html` / practice questions.

### File map

| File | Purpose |
|------|---------|
| `python_review_content.py` | Question bank (prompt, stub, deep dive, `my_answer`, interview Q&A) |
| `python_review_kid_answers.py` | **Kid-friendly HTML** for every question’s **Model answer / approach** |
| `python_review_algorithms.py` | Algorithm steps for coding solutions |
| `PythonReview/*.py` | Official solution scripts |
| `build_python_review.py` | Generator — layout, CSS, playground, split divider |
| `PythonReview.html` | **Generated — do not edit by hand** |

Regenerate:

```powershell
python D:\Sangeetha\Python\build_python_review.py
```

### Left panel order (Review slides)

1. Learning notes / question + learning intent  
2. **Model answer / approach** (kid-friendly)  
3. **Base concepts you need** — explanation + `# INPUT` / `# OUTPUT` (`python_review_concept_examples.py`)  
4. Deeper understanding  
5. Interview Q&A  
6. MyAnswer (if any)  
7. Practice link  

### Base concepts you need

- Lives in `python_review_concept_examples.py` (`CONCEPT_EXAMPLES`).
- Each concept shows: short explanation + `# INPUT` / `# OUTPUT` mini example.
- Rendered below Model answer / approach on every Review slide.

### Model answer / approach (required style)

- Source of truth: `python_review_kid_answers.py` → `KID_ANSWERS[id]` (applied in the builder).
- Rendered in a **white** `.model-answer` box (green left border).
- Writing style:
  - Simple analogy first (waiting-room seats, filing cabinet, traffic light).
  - Short paragraphs / newlines — one idea per `<p>`.
  - **Bold** important words; `code` for APIs.
  - For new tools/syntax (`deque`, `Decimal`, `:=`, `*args`, `get` vs `[]`, generators): add a tiny **example** (`<div class="step-pre">`) + a small **comparison table** when helpful.
  - Parenthetical meanings: bold **inside** parens, e.g. `deque (<b>double-ended queue</b>)`.
- Do **not** leave only jargon (“over-allocated contiguous arrays…”) in the model answer.

### MyAnswer (learner code)

- Store in `python_review_content.py` as `'my_answer': '...'` (one attempt) or `'my_answer': ['...', '...']` (MyAnswer 1, MyAnswer 2, …).
- Appears on the **left**, below Interview Q&A, as a runnable playground.
- Keep the learner’s code mostly as they wrote it (format lightly if needed).
- Official solution stays on the **right**.

### Deeper understanding

- Use **tables** for memory / performance / when-to-use comparisons (same spirit as Q1.2 / Q1.4).
- Correct inaccurate claims (e.g. Python `int` is **not** fixed 4 bytes — ~28 for `12345` on 64-bit CPython).

---

## 14. Cross-update: Review ↔ Training (required)

When a Review explanation introduces or clarifies a concept, **also update the matching Training slide** if that topic already exists (or clearly belongs there).

| Review idea | Typical Training home |
|-------------|------------------------|
| int/str memory, list growth, list vs ArrayList, deque | Slide **Python Datatypes** (`build_training.py` CONTENT + callouts) |
| `is` vs `==` | Operators / identity section |
| `*args` / `**kwargs`, mutable default | Functions slide |
| `yield` / generators | Comprehensions + Generators slides |
| Walrus `:=` | Flow / beginner steps (`training_beginner.py`) |
| C# Comparison popups | `slide_csharp_popups.py` → rebuild training |

Checklist when changing a Review Q:

1. Update kid model answer (`python_review_kid_answers.py`) and/or deep dive (`python_review_content.py`).
2. If the learner provided code → set `my_answer`.
3. Mirror the teaching (callout / table / mini example) on the related **Training** slide.
4. Run **both** generators when both decks changed:

```powershell
python D:\Sangeetha\Python\build_python_review.py
python D:\Sangeetha\Python\build_training.py
```

5. Spot-check in browser (`http://127.0.0.1:8765/...` preferred over `file://` for playground).

---

## 15. Serve locally

```powershell
cd D:\Sangeetha\Python
python -m http.server 8765 --bind 127.0.0.1
```

- Training: `http://127.0.0.1:8765/PythonTraining.html`
- Review: `http://127.0.0.1:8765/PythonReview.html`

If port 8765 fails (“Connection was reset”), kill stale listeners and restart the server.
