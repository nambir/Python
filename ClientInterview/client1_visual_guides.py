"""Visual guides for Client1.html — same thumbnail + window pattern as PythonTraining.

Posters live in Client1-Images/ (unique 1536×1024 infographics, not the shared stencil).
"""

from __future__ import annotations

from slide_visual_guides import _guide_block


def make_client1_visual_guide_fn(mapping: dict[int, tuple[str, str, int]]):
    def visual_guide_for(n: int) -> str:
        entry = mapping.get(n)
        if not entry:
            return ""
        return _guide_block(f"vguide-{n}", *entry)

    return visual_guide_for
