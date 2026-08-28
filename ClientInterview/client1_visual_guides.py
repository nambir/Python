"""Visual guides for Client1.html — same thumbnail + window pattern as PythonTraining.

Posters live in Client1-Images/ (unique 1536×1024 infographics, not the shared stencil).
"""

from __future__ import annotations

from slide_visual_guides import _guide_block


def _guide(win_id: str, item: tuple) -> str:
    src, label, native_w = item[0], item[1], item[2]
    blurb = item[3] if len(item) > 3 else None
    return _guide_block(win_id, src, label, native_w, blurb)


def make_client1_visual_guide_fn(
    mapping: dict[int, tuple],
    extras: dict[int, list[tuple]] | None = None,
    prepend: dict[int, list[tuple]] | None = None,
):
    extras = extras or {}
    prepend = prepend or {}

    def visual_guide_for(n: int) -> str:
        blocks: list[str] = []
        k = 1
        for item in prepend.get(n, []):
            blocks.append(_guide(f"vguide-{n}-{k}", item))
            k += 1
        entry = mapping.get(n)
        if entry:
            blocks.append(_guide(f"vguide-{n}", entry))
            k += 1
        for extra in extras.get(n, []):
            blocks.append(_guide(f"vguide-{n}-{k}", extra))
            k += 1
        return "".join(blocks)

    return visual_guide_for
