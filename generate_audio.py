"""Generate MP3 narration files for PythonTraining.html (0.75x speed via edge-tts)."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("Install edge-tts: pip install edge-tts")
    sys.exit(1)

from slide_narrations import NARRATIONS

VOICE = "en-IN-NeerjaNeural"  # clear Indian English; fallback: en-US-AriaNeural
RATE = "-25%"  # ~0.75x speed
OUT_DIR = Path(__file__).parent / "audio"


async def generate_one(slide_id: int, text: str, out_path: Path) -> None:
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(str(out_path))
    print(f"  OK slide-{slide_id:02d}.mp3 ({out_path.stat().st_size // 1024} KB)")


async def main(slides: list[int] | None = None) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    targets = slides if slides else sorted(int(k) for k in NARRATIONS.keys())
    print(f"Generating {len(targets)} audio files -> {OUT_DIR}")
    print(f"Voice: {VOICE}  Rate: {RATE} (~0.75x)")
    for sid in targets:
        text = NARRATIONS.get(sid) or NARRATIONS.get(str(sid))
        if not text:
            print(f"  SKIP slide-{sid:02d} (no narration)")
            continue
        out_path = OUT_DIR / f"slide-{sid:02d}.mp3"
        await generate_one(sid, text, out_path)
    print("Done. Open PythonTraining.html and press A to play current slide.")


if __name__ == "__main__":
    ids = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else None
    asyncio.run(main(ids))
