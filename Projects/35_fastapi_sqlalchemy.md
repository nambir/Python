# Slide 35 — FastAPI + SQLAlchemy

## Install
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

## Recommended folder layout
```
my-api/
  app/
    main.py           # FastAPI app, include routers
    api/routes/       # HTTP handlers (thin)
    schemas/          # Pydantic models
    models/           # SQLAlchemy ORM
    services/         # business logic
    db.py             # engine, SessionLocal, get_db
  tests/
  pyproject.toml
```

## Layer rules
| Layer | Job |
|-------|-----|
| routes | Parse HTTP, call service, return schema |
| schemas | Validate JSON in/out |
| models | Map tables — no API exposure |
| services | Transactions, rules, orchestration |
| `get_db` | One session per request via `Depends` |

## Run (after implementing `app/main.py`)
```bash
uvicorn app.main:app --reload
```

## C# mapping
- FastAPI ≈ ASP.NET Core Web API
- Pydantic ≈ DTO + DataAnnotations
- SQLAlchemy Session ≈ EF Core DbContext
- `Depends(get_db)` ≈ scoped DI
