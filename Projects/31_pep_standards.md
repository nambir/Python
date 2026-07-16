# Slide 31 — PEP Standards

## Run once in REPL
```python
import this   # PEP 20 — Zen of Python
```

## PEP checklist
| PEP | Topic |
|-----|-------|
| 8 | Style — snake_case, 4 spaces, import order |
| 257 | Docstrings on public modules/functions |
| 484/585 | Type hints — `list[int]` in 3.9+ |
| 440 | Version strings for packages |
| 621 | `[project]` in `pyproject.toml` |

## Practice
1. Rename one script's functions to `snake_case`.
2. Add a one-line docstring to each `def`.
3. Run `ruff check .` or `flake8` if installed.
