"""Narration scripts for PythonTraining.html — spoken at 0.75x via edge-tts MP3.

Narrations are composed from definition, glossary, real-life examples, diagrams,
step-by-step content, keyword deepdives, learn panels, code examples, scenarios,
practice checklists, and interview Q&A so audio covers every concept on the slide.
"""

from slide_narration_builder import compose_narration

NARRATION_0 = (
    "Welcome to Python Training 2026, Batch 2. This deck follows a four-week syllabus. "
    "Week 1 covers foundations: intro, setup, workspace, PEP standards, datatypes, typing, "
    "operators, flow control, comprehensions, functions, and built-in functions. "
    "Week 2 covers collections, memory management and garbage collection, Pydantic, "
    "object-oriented programming, descriptors, and generators. "
    "Week 3 covers decorators, exception handling, threading and the GIL, async and await, "
    "logging, unit testing, regular expressions, file operations, context managers, and "
    "virtual environments. Week 4 covers FastAPI with SQLAlchemy. "
    "Project slides cover the Python-Set2 portfolio: pythonBasics, Google exercises, Pandas, "
    "Django, Pipecat voice AI, and real project structure. "
    "The appendix slide compares C-sharp and Python. "
    "Use the navigation grid to jump to any slide. Press A to play or pause audio."
)

NARRATIONS: dict[int, str] = {0: NARRATION_0}
for slide_num in range(1, 36):
    NARRATIONS[slide_num] = compose_narration(slide_num)
