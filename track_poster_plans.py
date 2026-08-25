"""Per-slide poster plans — which visual widgets go in which panels.

Python Logging quality: six numbered color panels, each a different visual,
not six copies of the same 4-box flow.
"""

from __future__ import annotations

# First panel is the "hero" diagram for that topic.
HERO: dict[str, str] = {
    "A01": "flow",
    "A02": "flow",
    "A03": "nested",
    "A04": "flow",
    "A05": "table",
    "A06": "flow",
    "A07": "flow",
    "A08": "decision",
    "A09": "flow",
    "A10": "flow",
    "A11": "table",
    "A12": "flow",
    "A13": "vs",
    "A14": "metrics",
    "S01": "join",
    "S02": "table",
    "S03": "table",
    "S04": "code",
    "S05": "table",
    "S06": "stack",
    "S07": "nested",
    "S08": "flow",
    "S09": "flow",
    "S10": "decision",
    "S11": "levels",
    "S12": "flow",
    "S13": "stack",
    "S14": "metrics",
    "W01": "flow",
    "W02": "table",
    "W03": "flow",
    "W04": "stack",
    "W05": "flow",
    "W06": "code",
    "W07": "stack",
    "W08": "decision",
    "W09": "table",
    "W10": "flow",
    "W11": "flow",
    "W12": "decision",
    "W13": "flow",
    "W14": "flow",
    "W15": "flow",
    "W16": "metrics",
    "D01": "table",
    "D02": "flow",
    "D03": "table",
    "D04": "vs",
    "D05": "levels",
    "D06": "flow",
    "D07": "decision",
    "D08": "nested",
    "D09": "flow",
    "D10": "table",
    "D11": "code",
    "D12": "flow",
    "D13": "metrics",
    "D14": "table",
    "D15": "flow",
    "D16": "levels",
    "D17": "table",
    "D18": "table",
    "D19": "flow",
    "D20": "nested",
    "D21": "flow",
    "D22": "flow",
    "D23": "stack",
    "D24": "flow",
    "D25": "flow",
    "D26": "stack",
    "D27": "join",
    "D28": "stack",
    "D29": "decision",
    "D30": "levels",
    "D31": "table",
    "D32": "decision",
    "D33": "nested",
    "D34": "table",
    "D35": "flow",
    "D36": "flow",
    "D37": "metrics",
    "D38": "flow",
    "D39": "flow",
    "D40": "flow",
    "D41": "vs",
    "D42": "flow",
    "D43": "flow",
    "D44": "flow",
    "D45": "table",
    "D46": "stack",
    "D47": "flow",
    "D48": "table",
    "D49": "flow",
    "D50": "vs",
    "D51": "metrics",
    "D52": "metrics",
    "D53": "flow",
    "D54": "flow",
    "D55": "table",
    "D56": "decision",
    "D57": "metrics",
    "D58": "vs",
    "D59": "decision",
    "D60": "metrics",
    "D61": "table",
    "D62": "flow",
    "D63": "nested",
    "D64": "table",
    "D65": "flow",
    "D66": "code",
    "D67": "flow",
    "D68": "flow",
    "D69": "metrics",
    "D70": "table",
    "D71": "flow",
    "D72": "metrics",
}

# 3x2 = Logging page. Other grids so neighbouring posters are not identical chrome.
GRID: dict[str, str] = {}

_GRIDS = ("3x2", "2x3", "hero_plus")


def grid_for(sid: str) -> str:
    if sid in GRID:
        return GRID[sid]
    n = int("".join(ch for ch in sid if ch.isdigit()) or "0")
    return _GRIDS[n % 3]


# Extra rows when the catalog table is the wrong shape for a Logging-style compare.
COMPARE_EXTRA: dict[str, list[tuple[str, str, str]]] = {
    "A05": [
        ("Criterion", "localStorage", "sessionStorage"),
        ("Survives tab close", "yes", "no"),
        ("Shared tabs", "yes", "no"),
        ("XSS can read", "yes", "yes"),
        ("Refresh token", "avoid", "avoid — memory/HttpOnly preferred"),
    ],
    "S01": [
        ("Criterion", "INNER JOIN", "LEFT JOIN"),
        ("Unmatched left row", "dropped", "kept, right side NULL"),
        ("Use when", "both sides must exist", "report must show gaps"),
        ("WHERE on right", "fine", "turns it into INNER — put filter in ON"),
    ],
    "S03": [
        ("Criterion", "#temp", "table variable"),
        ("Statistics", "yes", "often assumed 1 row"),
        ("Indexes", "yes", "limited"),
        ("Best for", "large intermediate", "tiny list"),
    ],
    "W02": [
        ("Criterion", "IAM user / access key", "Task role"),
        ("Who", "a person (or leftover secret)", "ECS / Lambda assumes"),
        ("Lifetime", "long-lived key risk", "temporary credentials"),
        ("In Angular", "never", "API uses the role, not the SPA"),
    ],
    "W12": [
        ("Criterion", "Lambda", "ECS API"),
        ("Shape", "short event", "request/response, long-lived"),
        ("Example", "S3 → thumbnail", "Device API"),
        ("Avoid", "20-minute report / WebSocket hub", "tiny cron that is cheaper as Lambda"),
    ],
    "D01": [
        ("Criterion", "Value type", "Reference type"),
        ("Stored", "bits in the variable", "arrow to the heap"),
        ("Copy", "copies the bits", "copies the arrow"),
        ("Examples", "int, bool, small struct", "class, string, List<T>"),
    ],
}

LEVEL_SETS: dict[str, list[tuple[str, str, str]]] = {
    "D05": [
        ("Gen 0", "#94a3b8", "short-lived objects"),
        ("Gen 1", "#3b82f6", "survived one collection"),
        ("Gen 2", "#1d4ed8", "long-lived"),
        ("LOH", "#dc2626", "large objects — expensive"),
    ],
    "D16": [
        ("Transient", "#86efac", "new instance every resolve"),
        ("Scoped", "#3b82f6", "one per HTTP request"),
        ("Singleton", "#1e3a5f", "one for the process"),
        ("Captive", "#dc2626", "singleton holding scoped — bug"),
    ],
    "S11": [
        ("Read uncommitted", "#fecaca", "dirty reads possible"),
        ("Read committed", "#fdba74", "SQL Server default"),
        ("Repeatable read", "#86efac", "row locks hold"),
        ("Serializable / SI", "#3b82f6", "narrower anomalies"),
    ],
    "A11": [
        ("Emulated", "#3b82f6", "default — unique attributes"),
        ("ShadowDom", "#7c3aed", "true shadow boundary"),
        ("None", "#dc2626", "styles leak globally"),
        ("::ng-deep", "#f97316", "avoid — piercing is a smell"),
    ],
}

# Panel titles when the widget name is too generic.
PANEL_TITLE: dict[tuple[str, str], str] = {
    ("A01", "flow"): "Lifecycle — order you must name",
    ("A06", "flow"): "How a request is cloned",
    ("A04", "flow"): "Login → token → API",
    ("S01", "join"): "What a join actually does",
    ("S09", "flow"): "Slow stored-proc playbook",
    ("W07", "stack"): "Recipe vs running vs keep-alive",
    ("W01", "flow"): "Your drawing, not a brochure",
    ("D15", "flow"): "How a request travels",
    ("D06", "flow"): "await frees the thread",
    ("D39", "flow"): "Prove the bug, then lock it",
    ("D40", "flow"): "Safe change on unfamiliar code",
    ("D65", "flow"): "Saga — then compensate",
    ("D71", "flow"): "In, then unwind out",
}

WIDGET_POOL = [
    "table",
    "levels",
    "code",
    "flow",
    "vs",
    "triple",
    "checklist",
    "stack",
    "nested",
    "join",
    "metrics",
    "decision",
]


def widgets_for(sid: str) -> list[str]:
    hero = HERO.get(sid, "flow")
    seed = sum(ord(c) * (i + 3) for i, c in enumerate(sid))
    pool = [w for w in WIDGET_POOL if w != hero]
    if not (sid.startswith("S") or sid in {"D27"}):
        pool = [w for w in pool if w != "join"]
    k = seed % len(pool)
    pool = pool[k:] + pool[:k]
    return [hero] + pool[:5]
