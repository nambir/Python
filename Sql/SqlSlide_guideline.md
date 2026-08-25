# SQL Slide Guideline

Use this for every curriculum slide in `Sql/`.  
**Do not hand-edit** `Sql/SqlTraining.html` — edit sources, then:

```powershell
cd D:\Sangeetha\Python
python Sql/build_sql_training.py
```

---

## Source files

| File | Purpose |
|------|---------|
| `sql_catalog.py` | Skills S01–S14 (PDF §§15–19) |
| `sql_assemble.py` | Builds meta / content / beginner / flows |
| `sql_flowcharts.py` | YES→right / NO→down |
| `build_sql_training.py` | Generator + SVG visual posters |

Shared: `interview_track.py`, `track_visual_guides.py`, `training_deck.py`.

Slow-SP answers start with **reproduce + actual plan**, not “add an index.”
A SQL transaction does **not** span independently deployed microservices.
