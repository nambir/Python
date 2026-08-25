# Interview decks — task list

Source: `ClientInterviewExpectations.pdf` (29 pages). Pattern: edit catalog → run `build_*_training.py` → generated HTML. Do **not** hand-edit HTML.

---

## Visual guides — Python Logging standard

Python posters (`images/slide-22-logging.png`, Threading & GIL, …) are the quality bar:

- White dense infographic, numbered color panels
- **Each panel is a different visual** (compare table, level bars, code + sample line, architecture flow, good vs bad code, practice + C#)
- Topic-specific diagrams — not the same 4 pastel boxes on every slide

Engine: `track_poster_engine.py` + `track_poster_plans.py`. Output: SVG in each track `images/`.

### Shared engine

- [x] Logging-style 3×2 / 2×3 / hero+panel chrome
- [x] Widgets: table, levels, code+output, flow, good/bad code, triple, checklist, stack, nested, join, metrics, decision
- [x] Unique 6-widget mix per slide id (hero diagram from `HERO`)
- [x] Rebuild all four HTML decks

### Angular (A01–A14)

- [x] A01–A14 posters generated

### SQL (S01–S14)

- [x] S01–S14 posters generated (S01 uses a join diagram)

### AWS (W01–W16)

- [x] W01–W16 posters generated

### .NET (D01–D72)

- [x] D01–D24
- [x] D25–D48
- [x] D49–D72 (including PDF-gap D61–D72)

Rebuild:

```powershell
python Dotnet/build_dotnet_training.py
python Angular/build_angular_training.py
python Sql/build_sql_training.py
python AWS/build_aws_training.py
```

Hard-refresh SVGs in the browser (`Ctrl+F5`) after rebuild.

## Track 0 — Shared

- [x] Write this `tasks.md`
- [x] Shared builder `interview_track.py`
- [x] Visual posters wired under Definition
- [x] Playground support for TypeScript / SQL / Dockerfile
- [x] Float-window JS for posters

## Track 1 — Dotnet

- [x] D61–D72 PDF gaps

## Track 2–4 — Angular / Sql / AWS

- [x] Folders, catalogs, builders, HTML decks
