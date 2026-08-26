"""Python-poster chrome data: unique banners, architecture nodes, Gantt/hub/lock."""

from __future__ import annotations

from track_poster_plans import COMPARE_EXTRA, HERO, LEVEL_SETS

INKS = ["#3b82f6", "#16a34a", "#4f46e5", "#7c3aed", "#ea580c", "#e11d48"]
PILLS = ["#dbeafe", "#dcfce7", "#ede9fe", "#f3e8ff", "#ffedd5", "#ffe4e6"]
PILL_TX = ["#1e40af", "#166534", "#5b21b6", "#6b21a8", "#9a3412", "#9f1239"]

BANNER: dict[tuple[str, int], str] = {
    ("W15", 1): "Draw two paths. Only name boxes you can defend.",
    ("W15", 2): "Sync for the user click. Events for work that can wait.",
    ("W15", 3): "A service laundry list is the fail. A drawing is the pass.",
    ("W15", 4): "Git → image → task definition → service. Rollback is previous revision.",
    ("W15", 5): "Logs = this request. Metrics = how many hurt. Traces = which hop.",
    ("W15", 6): "Two paths, four deploy words, three signals.",
    ("A05", 2): "XSS can read both stores. Prefer memory or HttpOnly.",
    ("A05", 3): "Refresh token does not belong in either store.",
    ("W07", 2): "Task definition is the recipe. Service keeps N healthy.",
    ("D16", 2): "A singleton must not capture a scoped DbContext.",
    ("D06", 1): "Sync waits idle. Async uses the wait time for other work.",
    ("D06", 2): "await pauses this method. It does not start a new thread by itself.",
    ("D06", 3): "At each await the thread is free for another request.",
    ("D06", 4): "Async is for waiting, not for heavy CPU.",
    ("D06", 5): "Async wins on threads: one pool, thousands of waits.",
    ("S01", 1): "INNER drops unmatched left rows. LEFT keeps them as NULL.",
    ("S01", 2): "WHERE on the right of a LEFT JOIN turns it into INNER.",
    ("A05", 1): "DOM storage is readable by XSS. Name the store and the risk.",
    ("A04", 1): "Access token on every API. Refresh token only against /token.",
    ("A06", 1): "Clone the request, add Bearer, refresh once on 401.",
    ("W07", 1): "Task definition = recipe. Task = running copy. Service = keep N healthy.",
    ("W12", 1): "Lambda for short events. ECS for the long-lived API.",
    ("D15", 1): "Exception handler must wrap the rest or it never sees the throw.",
    ("D16", 1): "A singleton must not capture a scoped DbContext.",
    ("D39", 1): "Reproduce → isolate → prove → regression test.",
}


def hero_kind(sid: str) -> str:
    k = HERO.get(sid, "arch")
    if sid in GANTT:
        return "gantt"
    if sid in HUB and k == "flow":
        return "hub"
    if sid in JOIN_IDS:
        return "join"
    if extra_levels(sid):
        return "levels"
    if extra_compare(sid):
        return "table"
    if k == "flow":
        return "arch"
    return k


def extra_compare(sid: str):
    return COMPARE_EXTRA.get(sid)


def extra_levels(sid: str):
    return LEVEL_SETS.get(sid)


ARCH: dict[str, list[tuple[str, str]]] = {
    "W15": [("Angular SPA", "browser"), ("API Gateway", "JWT + route"), ("ECS .NET", "tasks + ALB"), ("SQL", "+ traces")],
    "W01": [("Angular", "HTTPS"), ("API Gateway", "auth + throttle"), (".NET API", "ECS"), ("SQL", "data")],
    "W07": [("Git / CI", "build image"), ("ECR", "tagged image"), ("Task def", "CPU, env, role"), ("Service+ALB", "desired count")],
    "W05": [("Dockerfile", "recipe"), ("Image", "filesystem"), ("ECR", "registry"), ("Container", "running")],
    "W14": [("PR checks", "build/test"), ("Image :sha", "immutable"), ("ECR", "push"), ("ECS rolling", "rollback = prev")],
    "A04": [("Login form", "credentials"), ("Token API", "access+refresh"), ("Interceptor", "Bearer"), (".NET [Authorize]", "validates")],
    "A06": [("Clone HttpReq", "headers"), ("Add Bearer", "access token"), ("401?", "refresh once"), ("Retry / logout", "never loop")],
    "A01": [("constructor", "DI only"), ("ngOnInit", "Inputs ready"), ("View", "template bound"), ("ngOnDestroy", "unsubscribe")],
    "A07": [("URL", "router"), ("CanActivate", "hide the route"), ("Component", "renders"), ("API", "still authorizes")],
    "D15": [("HTTP in", "Kestrel"), ("AuthZ", "after routing"), ("Action", "your code"), ("Unwind", "exception mw")],
    "D19": [("Login", "credentials"), ("Issue JWT", "API"), ("Validate", "each call"), ("Refresh", "new access")],
    "D65": [("Order", "command"), ("Payment", "remote"), ("Inventory", "remote"), ("Ship / undo", "compensate")],
    "D71": [("Middleware in", "next()"), ("Action", "throws"), ("Unwind catch", "on the way out"), ("ProblemDetails", "+ trace id")],
    "D43": [("Build", "compile"), ("Test gate", "fail closed"), ("Same artifact", "no rebuild"), ("Deploy", "rollback")],
    "S09": [("Reproduce", "same params"), ("Actual plan", "not estimated"), ("One change", "index or rewrite"), ("Measure", "before/after")],
    "D39": [("Reproduce", "same input"), ("Isolate", "one dependency"), ("Prove", "failing test"), ("Lock", "regression")],
    "D40": [("Map", "callers + data"), ("Characterize", "tests first"), ("Small diff", "blast radius"), ("Rollout", "flag / canary")],
    "W13": [("App emit", "OTel"), ("Logs", "this request"), ("Metrics", "how many"), ("Traces", "which hop")],
}

LANE2: dict[str, list[str]] = {
    "W15": ["API event", "queue", "worker ECS", "SQL"],
}

GANTT: dict[str, dict] = {
    "D06": {
        "jobs": ["SQL 1", "SQL 2", "HTTP"],
        "sync_s": 3,
        "async_s": 1,
        "sync_name": "Sync (.Result / one by one)",
        "async_name": "await (overlaps waits)",
    },
    "A09": {
        "jobs": ["HTTP A", "HTTP B", "HTTP C"],
        "sync_s": 3,
        "async_s": 1,
        "sync_name": "nested subscribe (wait chain)",
        "async_name": "forkJoin / combineLatest",
    },
    "W10": {
        "jobs": ["Task 1", "Task 2", "Task 3"],
        "sync_s": 3,
        "async_s": 1,
        "sync_name": "One fat instance",
        "async_name": "N tasks behind ALB",
    },
}

HUB: dict[str, dict] = {
    "D06": {"center": "await", "sats": ["Req A", "Req B", "Req C", "Req D"]},
    "A09": {"center": "subscribe", "sats": ["map", "catchError", "UI", "unsub"]},
    "D21": {"center": "cache", "sats": ["miss", "load", "set", "drop"]},
}

LOCK: dict[str, dict] = {
    "D06": {"io": "HTTP / SQL waits — async helps", "cpu": "tight loop / image resize — thread frozen"},
    "D07": {"io": "I/O → Task / async", "cpu": "CPU → Parallel; lock shared memory"},
    "W12": {"io": "S3 event → Lambda (short)", "cpu": "Device API / WebSocket → stay on ECS"},
    "A08": {"io": "CanActivate only hides a URL", "cpu": "[Authorize] on the API is the real gate"},
}

JOIN_IDS = {"S01", "D27"}

MESSY: dict[str, list[str]] = {
    "W15": ["EC2", "S3", "RDS", "SQS", "SNS", "Lambda", "EKS", "CloudFront", "Cognito", "WAF"],
}

FOOTER_CODE: dict[str, tuple[list[str], list[str]]] = {
    "W15": (
        ["# user click", "SPA → APIGW → ECS API → SQL"],
        ["# work that can wait", "API → event → worker → SQL"],
    ),
    "D06": (
        ["# many waits", "await Task.WhenAll(a, b, c);"],
        ["# CPU off the request", "await Task.Run(() => Work());"],
    ),
    "A05": (
        ["// session only", "sessionStorage.setItem(k, v)"],
        ["// never the refresh token", "// memory or HttpOnly cookie"],
    ),
    "S01": (
        ["-- INNER: unmatched left gone", "FROM Orders o JOIN Ship s ON o.Id = s.OrderId"],
        ["-- LEFT: 102 stays as NULL", "FROM Orders o LEFT JOIN Ship s ON o.Id = s.OrderId"],
    ),
    "A09": (
        ["// overlap HTTP", "forkJoin([a$, b$, c$])"],
        ["// chain", "a$.pipe(switchMap(() => b$))"],
    ),
}

PICK_ROWS: dict[str, list[tuple[str, str, str]]] = {
    "aws": [
        ("cloud", "User click", "SPA → APIGW → ECS → SQL"),
        ("chip", "Work that can wait", "event → worker → SQL"),
        ("blocks", "Interview", "Two paths, not a catalog"),
    ],
    "dotnet": [
        ("cloud", "Many I/O waits", "async + Task.WhenAll"),
        ("chip", "Heavy Python-like CPU", "Task.Run / Parallel"),
        ("blocks", "Blocking library", "off the request thread"),
    ],
    "angular": [
        ("cloud", "Many HTTP waits", "forkJoin / async pipe"),
        ("chip", "UI thread work", "keep it off change detect"),
        ("blocks", "Tokens", "access on API; refresh hidden"),
    ],
    "sql": [
        ("cloud", "Match both sides", "INNER JOIN"),
        ("chip", "Keep the gaps", "LEFT JOIN; filter in ON"),
        ("blocks", "Prove it", "actual plan + SET STATISTICS IO"),
    ],
}
