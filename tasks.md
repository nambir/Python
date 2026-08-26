# Interview decks — task list

Source: `ClientInterviewExpectations.pdf` (29 pages). Pattern: edit catalog → run `build_*_training.py` → generated HTML. Do **not** hand-edit HTML.

---

## Visual guides — match Python PNG quality

Contract: `visual_guide_requirements.md` (written from every Python `images/slide-*.png`).
Shared drawing primitives: `poster_lib.py` (fill-height, visible arrow shafts, 13px body, 3-col footer).

- [x] Requirements written from Python posters (3+2+1, unique diagrams, 3-col C# footer)
- [x] AWS W01–W16 hand-authored (`AWS/aws_posters.py`)
- [x] Angular A01–A14 hand-authored (`Angular/angular_posters.py`)
- [x] SQL S01–S14 hand-authored (`Sql/sql_posters.py`)
- [x] .NET D01–D72 hand-authored (`Dotnet/dotnet_posters_p1.py`–`p3.py`)

Python PNGs are the quality bar — do not regenerate Python posters from this engine.

Rebuild:

```powershell
python Angular/build_angular_training.py
python Sql/build_sql_training.py
python AWS/build_aws_training.py
python Dotnet/build_dotnet_training.py
```

Hard-refresh SVGs (`Ctrl+F5`).

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
