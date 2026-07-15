# Slide 21 — Virtual Environment Guide

## Create a venv in Projects

```powershell
cd D:\Sangeetha\Python\Projects
python -m venv .venv
.venv\Scripts\activate
pip install pytest
pytest test_17_unit_testing.py -v
pip freeze > requirements.txt
```

## Why use venv?

- Isolates packages per project (like NuGet per solution)
- Avoids breaking system Python
- `requirements.txt` records exact versions for teammates

## Deactivate

```powershell
deactivate
```
