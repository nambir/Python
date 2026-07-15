# Python Training Project Setup

Use this guide when you clone this repository on a new laptop.

## 1. Install Required Software

Install these first:

- **Git**: https://git-scm.com/downloads
- **Python 3.12+**: https://www.python.org/downloads/
- **Cursor or VS Code**

During Python installation on Windows, select:

```text
Add Python to PATH
```

Verify installation:

```powershell
python --version
pip --version
git --version
```

## 2. Clone the Repository

```powershell
cd D:\
git clone https://github.com/nambir/Python.git
cd D:\Python
```

If you cloned somewhere else, open that folder in Cursor.

## 3. Create and Activate Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

After activation, your terminal should show `(.venv)`.

## 4. Install Dependencies

Install practice/test dependencies:

```powershell
pip install -r Projects\requirements.txt
```

Install audio generation dependency:

```powershell
pip install edge-tts
```

## 5. Open the Training Deck

Open this file in a browser:

```text
PythonTraining.html
```

You can double-click it, or from PowerShell:

```powershell
start PythonTraining.html
```

Use:

- **Left / Right arrows**: move between slides
- **Home**: go to navigation
- **A**: play/pause current slide audio
- **Audio button**: play/pause current slide audio

## 6. Rebuild the HTML Deck

If you edit slide content or generator files, rebuild:

```powershell
python build_training.py
```

This regenerates:

```text
PythonTraining.html
```

Do not hand-edit `PythonTraining.html` if you can update the source generator instead.

## 7. Generate MP3 Audio Files

The deck uses HTML5 audio files from:

```text
audio/slide-00.mp3
audio/slide-01.mp3
...
audio/slide-30.mp3
```

If audio files are missing, run:

```powershell
python generate_audio.py
```

Generate one slide only:

```powershell
python generate_audio.py 3
```

Narration text is in:

```text
slide_narrations.py
```

## 8. Run Practice Files

Examples:

```powershell
python Projects\01_datatypes.py
python Projects\04_flow_control.py
python Projects\20_async.py
```

Run unit tests:

```powershell
pytest Projects\test_17_unit_testing.py -v
```

## 9. Important Files

| File | Purpose |
|------|---------|
| `PythonTraining.html` | Main training deck |
| `build_training.py` | Generates the HTML deck |
| `training_meta.py` | Slide definitions/interview text |
| `training_beginner.py` | Beginner steps and Q&A |
| `slide_glossary.py` | Glossary tables |
| `slide_scenarios.py` | Scenario tables |
| `slide_keyword_deepdives.py` | Keyword deep-dive boxes |
| `slide_narrations.py` | Audio narration text |
| `generate_audio.py` | Generates MP3 narration files |
| `Projects/` | Practice files |
| `Python-Set2/` | Larger real project examples |

## 10. GitHub Push Checklist

Before pushing:

```powershell
git status
```

Make sure secrets are not included:

- Do not commit `.env`
- Do not commit API keys
- Do not commit virtual environment folders like `.venv/`

The root `.gitignore` is already set up for this.

Typical first push:

```powershell
git add .
git commit -m "Initial Python training project"
git branch -M main
git remote add origin https://github.com/nambir/Python.git
git push -u origin main
```

## 11. Troubleshooting

### `python` is not recognized

Reinstall Python and select **Add Python to PATH**, or try:

```powershell
py --version
py -m venv .venv
```

### Audio says MP3 missing

Run:

```powershell
pip install edge-tts
python generate_audio.py
```

Then refresh `PythonTraining.html`.

### Tests fail because pytest is missing

Run:

```powershell
pip install -r Projects\requirements.txt
```

### Virtual environment activation is blocked

Run PowerShell as normal user and allow local scripts:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\activate
```
