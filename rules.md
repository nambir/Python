# Python Training Deck — Authoring Rules

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
