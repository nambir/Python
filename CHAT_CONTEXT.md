# Training-deck chat context

Use this file when opening the repo on another machine, or starting a new Cursor chat. It is a compact record of the Python training-deck work and the Q&A that shaped Slide 20 (and related slides).

**Rebuild the deck:** `python build_training.py`  
**Output:** `PythonTraining.html` (35 curriculum slides + 11 notes slides)  
**Serve locally:** `python -m http.server 8123` then open `http://localhost:8123/PythonTraining.html#20`

---

## Repo map (what to edit)

| File | Role |
|---|---|
| `build_training.py` | Assembles HTML. Slide bodies, CSS, JS, `CONTENT` list. |
| `training_beginner.py` | Step-by-step bodies + interview Q&A keyed by slide number. |
| `training_meta.py` | Per-slide definition / interview one-liners. |
| `slide_visual_guides.py` | Poster mapping: `VISUAL_GUIDES` (one per slide) + `EXTRA_GUIDES` (extra posters below the main one). |
| `slide_diagrams.py`, `slide_keyword_deepdives.py`, `slide_csharp_popups.py`, `slide_real_life.py`, `slide_rich_diagrams.py` | Other slide extras. |
| `images/` | Visual-guide PNGs/JPGs. |

---

## Visual guides

Every slide 1–35 has a six-panel visual-guide poster in `images/`. Mapping is in `slide_visual_guides.py`.

- Slide 20 main poster: `images/slide-20-threading-gil.png` (1536×1024).
- Extra poster **below** the main one (user-supplied): `images/slide-20-threading-full.jpg`.
- Extra posters are stored in `EXTRA_GUIDES`, rendered after the main strip, each with its own thumbnail / new-tab / resizable window (`vguide-20` and `vguide-20-2`).
- Original `images/Threading.jpg` is unused by the mapping (safe to delete if not wanted).

To add another extra poster later:

```python
EXTRA_GUIDES: dict[int, list[tuple[str, str, int]]] = {
    20: [
        ("images/slide-20-threading-full.jpg",
         "Threading & GIL &mdash; Cores, Processes & Pools", 1536),
    ],
}
```

---

## Slide 20 — what was added in this conversation

### `__name__ == "__main__"` (Step 6)

**It is not only for `ProcessPoolExecutor`.** The guard asks: *am I the program being run, or am I being imported?* Pooling is the case where omitting it **crashes**.

Short 3-purpose note (in the step-by-step, under the comparison):

1. One file, two roles — importable module *and* runnable script.
2. Entry point — `main()`, argparse, `sys.argv` live in the guard.
3. Test-friendly imports — `pytest` imports your module to collect tests.

Full 8-purpose table lives in the **slide body** (before Common mistakes), in `build_training.py` under slide 20:

1. One file, two roles
2. Program entry point
3. Test-friendly imports
4. Multiprocessing / `ProcessPoolExecutor` (**mandatory** on Windows/macOS `spawn`)
5. Self-demo / smoke test
6. `python -m package` via `__main__.py`
7. Servers that import the app (uvicorn reloader/workers)
8. Frozen executables — `multiprocessing.freeze_support()` first inside the guard

**What `__name__` actually holds:**

| How the file is used | `__name__` | Guarded block runs? |
|---|---|---|
| `python job.py` | `"__main__"` | yes |
| `from module1 import add` | `"module1"` | no |
| re-imported in a multiprocessing child | `"__mp_main__"` (not `"job"`) | no |
| `python -m mypkg` (`__main__.py`) | `"__main__"` | yes |

**Without vs with the guard (measured on Windows / Python 3.12):**

- Without: child re-runs `ProcessPoolExecutor` during import → `RuntimeError` **in the child** (“bootstrapping phase”) → parent dies with `BrokenProcessPool`, exit code 1. Zero `[task]` lines.
- With: same three `[import]` prints (you + 2 workers). Guard does **not** stop the re-import; it stops re-running the **program body**. Tasks run, exit 0.

**“Children import defs only, then run `work()`”** means:

1. Parent pickles a **name** (`__mp_main__.work`), not the function body.
2. Windows `spawn` starts a fresh empty `python.exe`.
3. Child imports the file under `__mp_main__` — `import`/`def` run, guard is skipped.
4. Child looks up `work` and calls it.

Consequence: the target must be a **top-level `def`**. A `lambda` fails with `PicklingError: Can't pickle <function <lambda>>: attribute lookup <lambda> on __main__ failed`.

Purpose 1 is demonstrated with the real workspace files `Python-Set2/pythonBasics/MyModules/module1.py` + `index.py` (`from module1 import add`). Unguarded `print` at module level leaks into `python index.py` (prints `3` twice). Those demo files were **not** edited; only copies in a temp folder were run.

### Process / thread counts (Step 7)

Two rules:

1. Every launched command is **one process**, and a process starts with **one** `MainThread`. So 3 apps = 3 processes = 3 threads.
2. `ThreadPool` adds **threads inside** that process. `ProcessPool` adds **new processes**, each with its own `MainThread` and GIL.

Measured (one app, Python 3.12 Windows):

```
at start                 threads=1  ['MainThread']
inside ThreadPool(4)     threads=5  MainThread + 4 workers
after ThreadPool closed  threads=1
inside ProcessPool(4)    parent threads=3
                         ['MainThread', 'QueueFeederThread', 'Thread-1']
                         4 child processes, each threads=1 ['MainThread']
```

App2 with `ProcessPoolExecutor(4)` = **5 processes, 7 threads**: 4 children × 1 thread + parent 3 (MainThread + QueueFeederThread pickles args into the pipe + manager thread completes Futures).

`max_workers=4` is a **ceiling**, not a reservation. Submit 2 tasks to `ThreadPoolExecutor(4)` → 3 threads, not 5.

Task Manager shows processes (`python.exe` entries), not threads.

### `threading.Thread` vs `ThreadPoolExecutor` (Step 8)

Both are threads in **one process** — GIL rules identical. Difference is bookkeeping.

| | `threading.Thread` | `ThreadPoolExecutor` |
|---|---|---|
| Threads created | one per task | `max_workers`, reused |
| Result | no return — shared list/Queue | `return` → `future.result()` / `pool.map` |
| Order | finish order | `map` keeps input order |
| Errors | kill that thread; `join()` still returns | stored in Future, **re-raised** at `.result()` |
| Waiting | you `.join()` | `with` joins on exit |
| Best for | long-lived background service (`daemon=True`) | batches of short tasks with a result |

C#: `new Thread().Start()` vs `Task.Run` / `await Task.WhenAll`.

### `with` keyword — **belongs on Slide 26**, not as a new slide

`with` is the syntax for the **context manager** protocol. Slide 26 already owns `__enter__`/`__exit__`, `@contextmanager`, and the “return True swallows exceptions” mistake.

What `with expr as x:` does: evaluate `expr` → `__enter__()` → run body → `__exit__(exc_type, exc, tb)` always. Equivalent to `try/finally`.

Use cases: files, locks, pools (`shutdown(wait=True)` — why thread count drops to 1 after the block), sockets/DB, transactions, tempfile, pytest.raises / mock.patch, `contextlib.suppress` / `ExitStack`, `async with`.

Gotchas: resource is dead after the block (never `return f` from `with open`); `with` does **not** create a scope.

C#: `using` / `IDisposable`; `async with` = `await using`; `with lock:` = `lock (obj)`.

Slide 20 Step 7 already has a **short pointer** to Slide 26. The full use-case catalogue was **not yet added** to Slide 26 when this file was written — that is the next natural edit if continuing the work.

---

## How the HTML is built (so you don’t hunt)

`slide_hdr` → `topic_intro` (definition + visual guide + diagrams) → beginner `steps` from `training_beginner.py` → keyword deep-dives → rest of `CONTENT` learn HTML (mistakes, quiz) → interview box.

To change beginner steps, edit `BEGINNER_CONTENT[20]["steps"]` in `training_beginner.py`.  
To change the slide-body “Purposes of `__main__`” table, edit the string after slide 20’s `code(...)` in `build_training.py`.

Browsers cache `PythonTraining.html`; after rebuild use a query string (`?v=8#20`) or hard-refresh.

---

## Open follow-ups

- Add the full `with` explanation / use-case catalogue to **Slide 26**.
- Optionally add a one-line cross-ref on Slide 25 (`with open`) and Slide 35 (`using`).
- `images/Threading.jpg` is unused; delete if not needed.
