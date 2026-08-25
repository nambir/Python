# Interview decks — task list

Source: `ClientInterviewExpectations.pdf` (29 pages). Pattern: edit catalog → run `build_*_training.py` → generated HTML. Do **not** hand-edit HTML.

---

## Visual guides — unique layout per slide

White/light page. **Do not** reuse one 6-panel grid for every topic.

Each slide is assigned a layout in `track_visual_flows.py` (`LAYOUT_BY_ID`): hero flow, VS split, loop, layers, timeline, fork, cards, before/after, swimlane, STAR story, code + callouts, five-question drill, nested containment, hub, zigzag, matrix.

- [x] Unique page layouts (not a shared 6-panel stencil)
- [x] Per-slide process boxes in `FLOW_BY_ID`
- [x] Rebuild Dotnet, Angular, Sql, AWS posters

---

## Track 0 — Shared

- [x] Write this `tasks.md`
- [x] Shared builder `interview_track.py`
- [x] Visual posters wired under Definition
- [x] Playground support for TypeScript / SQL / Dockerfile
- [x] Float-window JS for posters

## Track 1 — Dotnet

- [x] D61–D72 PDF gaps
- [x] Visual guide on all Dotnet slides (upgrade to Threading style — see above)

## Track 2–4 — Angular / Sql / AWS

- [x] Folders, catalogs, builders, HTML decks
- [x] Visual guide on every slide (upgrade to Threading style — see above)

Rebuild:

```powershell
python Dotnet/build_dotnet_training.py
python Angular/build_angular_training.py
python Sql/build_sql_training.py
python AWS/build_aws_training.py
```
