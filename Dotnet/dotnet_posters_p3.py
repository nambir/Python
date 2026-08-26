"""Hand-authored .NET visual guides D49–D72.

Meets visual_guide_requirements.md (Python 3+2+1 chrome). Quality bar: AWS W03/W04.
"""

from __future__ import annotations

from poster_lib import (
    INK,
    MUTED,
    NAVY,
    TBL,
    bullets,
    code_box,
    code_out,
    flow_h,
    flow_v,
    footer3,
    hub,
    levels,
    log_bars,
    ml,
    note,
    panel,
    pipe_split,
    rect,
    slots,
    stack,
    svg,
    t,
    table,
    terminal,
    vs_boxes,
    wrap,
)


def _footer_left_code(lines_a, lines_b):
    def draw(x, y, w, h):
        hh = (h - 8) / 2
        return code_box(x, y, w - 8, hh - 4, lines_a) + code_box(x, y + hh, w - 8, hh - 4, lines_b)

    return draw


def _tri(x, y, w, h, cols):
    cw = (w - 16) / 3
    parts = []
    for i, (title, sub, fill, ink) in enumerate(cols):
        bx = x + i * (cw + 8)
        parts.append(rect(bx, y, cw, h, fill=fill, stroke=ink, rx=10))
        parts.append(t(bx + 8, y + 24, title, size=14, fill=ink, weight=800))
        parts.append(ml(bx + 8, y + 48, wrap(sub, max(10, int(cw / 8)), 6), size=12, fill=INK))
    return "".join(parts)


def d49():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Failure", "Control", "Outcome"],
            [
                ("Transient", "Bounded retry + jitter", "Later recovery"),
                ("Duplicate", "Idempotency record", "One logical effect"),
                ("Poison", "DLQ + alert + replay", "Flow stays up"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 6, "Same transaction, then publish", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 28, w, ["Order write", "Outbox row", "Publisher", "Bus"])
            + note(x, y + h - 24, w, "Outbox = atomic change + intent to publish.", kind="star")
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Outbox", "publisher"),
                ("Topic", "at-least-once"),
                ("Consumer", "idempotent"),
            ],
            "Inventory",
            "Notify / DLQ",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Retry forever",
            [
                "Poison loops forever",
                "Duplicates apply twice",
                "No owner for replay",
            ],
            "Fail safely",
            [
                "Backoff with a hard cap",
                "Ignore known message IDs",
                "DLQ + alert + runbook",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "if (await _seen.Exists(msg.Id)) return;",
                "await _inventory.Reserve(msg);",
                "await _seen.Mark(msg.Id);",
                "// after N failures → DLQ",
            ],
            "at-least-once  →  one logical reserve",
            title="idempotent consumer",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            _footer_left_code(
                ["// outbox in the same SaveChanges", "// then a publisher drains it"],
                ["// consumer: id check → work", "// poison: DLQ + alert + replay"],
            ),
            [
                "Draw the real path including failure",
                "Name dedupe and the DLQ owner",
                "Say why outbox beats publish-after-commit hope",
            ],
            ["Infinite retries on poison", "Assume exactly-once delivery"],
            [
                ("Outbox", "same DbContext txn", "atomic intent to publish"),
                ("Idempotent", "processed message id", "duplicates are normal"),
                ("DLQ", "IErrorHandler / SQS DLQ", "alert, fix, replay"),
                ("Pub/sub", "MassTransit / SNS", "independent reactions"),
            ],
            third="Interview",
        )

    return svg(
        "Make Messaging Fail Safely",
        ".NET · D49  ·  Duplicates, delays, and poison are normal — design for them",
        [
            panel(s[0], 1, "Three failure controls", "Retry, dedupe, quarantine — one outcome each.", p1),
            panel(s[1], 2, "How an order event is born", "Write the outbox in the same transaction.", p2),
            panel(s[2], 3, "How a message travels", "At-least-once bus. Independent consumers.", p3),
            panel(s[3], 4, "The interview trap", "Unbounded retries are not reliability.", p4),
            panel(s[4], 5, "Idempotent handler", "Same message id must be a no-op.", p5),
            panel(s[5], 6, "Practice & interview lines", "Path, failure states, replay.", p6),
        ],
    )


def d50():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Timeout", "#1d4ed8", "stop before the caller budget dies"),
                ("Circuit", "#b91c1c", "pause a predictably failing hop"),
                ("Bulkhead", "#7c3aed", "one dep cannot take all threads"),
                ("Degrade", "#15803d", "page without personalization"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Failure mode", "Pattern", "Result"],
            [
                ("Slow dependency", "Timeout", "Latency stays bounded"),
                ("Repeated failure", "Circuit breaker", "Load is shed"),
                ("Pool exhaustion", "Bulkhead", "Other features live"),
            ],
            header_fill="#dcfce7",
            h=h,
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.12, y, w * 0.76,
            ["Closed — calls flow", "Open — fail fast", "Half-open — probe", "Closed again or trip"],
            h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Retry everything",
            [
                "Retries with no budget",
                "Amplify a dying dependency",
                "Total page failure",
            ],
            "Bound the damage",
            [
                "Timeout inside the budget",
                "Circuit during sustained fail",
                "Safe reduced page",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "http.Timeout = TimeSpan.FromMs(250);",
                "// Polly: CircuitBreaker + bulkhead",
                "try { return await recs.Get(); }",
                "catch { return catalog.WithoutRecs(); }",
            ],
            "slow recs → catalog still renders",
            title="catalog survives recommendations",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say this",
            _footer_left_code(
                ["// timeout < caller budget", "// circuit on sustained fail"],
                ["// bulkhead = own pool", "// fallback = reduced page"],
            ),
            [
                "Name three failure modes you survive",
                "Map each to a control",
                "Say the degraded response",
            ],
            ["Retry without a budget", "Resilience = more retries"],
            [
                ("Timeout", "HttpClient.Timeout", "caller's p95 budget"),
                ("Circuit", "Polly CircuitBreaker", "protect both sides"),
                ("Bulkhead", "dedicated Semaphore", "isolate the slow hop"),
                ("Fallback", "reduced DTO", "safe, not empty 500"),
            ],
            third="Interview",
        )

    return svg(
        "Contain Failures by Design",
        ".NET · D50  ·  Resilience is bounding damage — not retrying everything",
        [
            panel(s[0], 1, "Four controls", "Timeout, break, isolate, degrade.", p1),
            panel(s[1], 2, "Mode → pattern → result", "Each failure has a named control.", p2),
            panel(s[2], 3, "Circuit states", "Closed, open, half-open — then decide.", p3),
            panel(s[3], 4, "The interview trap", "Retries without a budget amplify outages.", p4),
            panel(s[4], 5, "Catalog without recs", "Fall back inside the request budget.", p5),
            panel(s[5], 6, "Practice & interview lines", "Survive slow, fail, and exhaustion.", p6),
        ],
    )


def d51():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["NFR", "Target", "Verify"],
            [
                ("Availability", "99.95% / month", "success-ratio SLI"),
                ("Latency", "p95 < 400 ms", "histogram"),
                ("Throughput", "250 RPS sustained", "load + prod"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("SLI", "#1e3a5f", "the signal you actually measure"),
                ("SLO", "#2563eb", "the target + window you promised"),
                ("Error budget", "#dc2626", "allowed unreliability left"),
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Checkout — recite the numbers", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 32, w, ["99.95%", "p95 400ms", "250 RPS", "2× burst"])
            + note(x, y + h - 24, w, "Averages hide the slow users. Use percentiles.", kind="star")
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Must be fast",
            [
                "The API must be fast.",
                "No percentile, no window.",
                "No way to verify.",
            ],
            "Named SLO",
            [
                "p95 < 400 ms checkout",
                "eligible requests / month",
                "dashboard + load test",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "// SLO: 99.95% success, monthly",
                "// SLI: 2xx/3xx of eligible POSTs",
                "// alert: error-budget burn rate",
                "// load: 250 RPS, 500 burst",
            ],
            "signal + target + scope + window",
            title="turn the NFR into a sentence",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Recite three",
            _footer_left_code(
                ["// availability 99.95% monthly", "// p95 checkout < 400 ms"],
                ["// 250 RPS sustained", "// 2× burst, load-tested"],
            ),
            [
                "State three real targets",
                "Name the measurement window",
                "Say how each was verified",
            ],
            ["The API must be fast", "Quote four nines with no SLI"],
            [
                ("SLI", "meter / histogram", "what you measure"),
                ("SLO", "alert rule + window", "what you promise"),
                ("p95", "Stopwatch / OTel", "not the average"),
                ("Budget", "burn-rate alert", "allowed unreliability"),
            ],
            third="Interview",
        )

    return svg(
        "Turn NFRs Into Numbers",
        ".NET · D51  ·  Signal, target, scope, window — or it is not an NFR",
        [
            panel(s[0], 1, "Three targets you can say", "Availability, p95, throughput — with proof.", p1),
            panel(s[1], 2, "SLI → SLO → budget", "A number without a signal is a slogan.", p2),
            panel(s[2], 3, "Checkout numbers", "Percentile, window, sustained and burst.", p3),
            panel(s[3], 4, "The interview trap", "Fast is not a requirement.", p4),
            panel(s[4], 5, "Write the SLO sentence", "Eligible requests, monthly, verified.", p5),
            panel(s[5], 6, "Practice & interview lines", "Three numbers and how you checked them.", p6),
        ],
    )


def d52():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Input", "Assumption", "Derived"],
            [
                ("Daily users", "120,000", "demand base"),
                ("Peak share", "20% in one hour", "~40 RPS"),
                ("Safe / instance", "25 RPS", "3 instances + margin"),
            ],
            header_fill="#ffedd5",
            h=h,
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["120k users × 6 calls / day", "20% in one peak hour", "÷ 3600 → ~40 RPS", "40 / 25 → 2 + spare = 3"],
            fill="#ffedd5",
            ink="#9a3412",
            h=h,
        )

    def p3(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("API instances", "you sized these first"),
                ("DB connections", "often the next wall"),
                ("Queue / downstream", "throughput you did not own"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "False precision",
            [
                "We need 37.4 instances.",
                "Guesses stated as facts.",
                "No downstream check.",
            ],
            "Defensible range",
            [
                "Assumptions out loud",
                "Safe RPS, not max RPS",
                "Then verify DB + queue",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "users = 120_000",
                "peak = users * 6 * 0.20 / 3600",
                "# ≈ 40 RPS before burst",
                "n = ceil(40 / 25) + 1  # = 3",
            ],
            "then check pool size and queue RPS",
            title="users → RPS → instances",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Live arithmetic",
            _footer_left_code(
                ["// users × actions / interval", "// apply peak factor"],
                ["// ÷ safe RPS / instance", "// + headroom, then DB"],
            ),
            [
                "Estimate users to peak RPS live",
                "State every assumption",
                "Name the next bottleneck",
            ],
            ["Present guesses as exact", "Scale instances and ignore SQL"],
            [
                ("Demand", "active users × calls", "say the interval"),
                ("Safe RPS", "load-test ceiling − margin", "not the spike max"),
                ("Headroom", "n+1 / AZ failure", "redundancy first"),
                ("Next wall", "SqlConnection pool", "always check downstream"),
            ],
            third="Interview",
        )

    return svg(
        "Estimate Capacity Before Scaling",
        ".NET · D52  ·  Users → RPS → instances — then the database",
        [
            panel(s[0], 1, "Inputs you must say", "Demand, peak share, safe instance RPS.", p1),
            panel(s[1], 2, "How users become RPS", "Do the arithmetic out loud.", p2),
            panel(s[2], 3, "What you check next", "Instances are not the only limit.", p3),
            panel(s[3], 4, "The interview trap", "Guesses presented as exact are worse than a range.", p4),
            panel(s[4], 5, "The napkin math", "Then verify connections and queues.", p5),
            panel(s[5], 6, "Practice & interview lines", "Assumptions visible, range defensible.", p6),
        ],
    )


def d53():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Risk", "Control", "Proof"],
            [
                ("Broken access", "resource policy", "negative tests"),
                ("Injection", "parameterized SQL", "SAST + tests"),
                ("Misconfig", "hardened templates", "config scan"),
                ("Data leak", "encrypt + redact", "log audit"),
            ],
            header_fill="#fee2e2",
            h=h,
        )

    def p2(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Authorize", "#b91c1c", "object + action on the server"),
                ("Validate", "#1d4ed8", "parameters, not string concat"),
                ("Protect", "#15803d", "encrypt, minimize, redact"),
                ("Manage", "#475569", "vault + rotate — never logs"),
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "A request through your controls", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 32, w, ["JWT", "[Authorize]", "param SQL", "vault"])
            + note(x, y + h - 24, w, "Encryption is not enough — minimize and audit too.", kind="warn")
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "OWASP list",
            [
                "We follow OWASP Top 10.",
                "No code, no test, no owner.",
            ],
            "Mapped controls",
            [
                "This threat → this policy",
                "This test proves it",
                "Secrets from managed ID",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "[Authorize(Policy = \"OrderOwner\")]",
                "await _db.Orders.FromSqlInterpolated(",
                "  $\"EXEC GetOrder {id}\");",
                "// secret: KeyVault, not appsettings",
            ],
            "resource authz + parameterized SP + vault",
            title="three controls in one path",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Map three risks",
            _footer_left_code(
                ["// broken access → policy", "// injection → parameters"],
                ["// secrets → vault + MI", "// never in logs or SPA"],
            ),
            [
                "Map three OWASP risks to your code",
                "Explain secret rotation",
                "Name a verification test each",
            ],
            ["Recite OWASP categories only", "Store secrets in appsettings.json"],
            [
                ("Authz", "[Authorize] policy", "server, every action"),
                ("SQL", "FromSqlInterpolated", "never concatenate"),
                ("Secrets", "KeyVault / MI", "rotate and redact"),
                ("PII", "AES + log redaction", "minimize first"),
            ],
            third="Interview",
        )

    return svg(
        "Map Threats to Controls",
        ".NET · D53  ·  A named threat, a control in YOUR path, a test",
        [
            panel(s[0], 1, "Four risks, four proofs", "Policy, parameters, templates, redaction.", p1),
            panel(s[1], 2, "Four verbs", "Authorize, validate, protect, manage.", p2),
            panel(s[2], 3, "How a request is guarded", "JWT is not authorization by itself.", p3),
            panel(s[3], 4, "The interview trap", "A checklist is not architecture.", p4),
            panel(s[4], 5, "Controls in the code", "Owner policy, parameterized SP, vault.", p5),
            panel(s[5], 6, "Practice & interview lines", "Threat → control → verification.", p6),
        ],
    )


def d54():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("Traces", "#4f46e5", "which hop is slow for THIS user"),
                ("Metrics", "#2563eb", "how many users are hurting now"),
                ("Logs", "#64748b", "why this request failed — no secrets"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Signal", "Question", "Example"],
            [
                ("Logs", "Why this fail?", "structured error"),
                ("Metrics", "How many hurt?", "error ratio / p95"),
                ("Traces", "Which hop?", "SQL span ms"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("RPS + errors", "#2563eb", "filterable by version"),
                ("p50 / p95 / p99", "#16a34a", "user latency, not avg"),
                ("Dependency health", "#ea580c", "recs / SQL / queue"),
                ("Oldest queued msg", "#dc2626", "depth can hide stuck"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Page every 500",
            [
                "Every exception pages.",
                "On-call tunes it out.",
                "Real SLO burn is missed.",
            ],
            "Actionable alert",
            [
                "Sustained SLO burn",
                "Known response path",
                "Add oldest-message next",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "_log.LogError(ex,",
                "  \"Checkout {OrderId} {TraceId}\",",
                "  id, Activity.Current?.Id);",
            ],
            "fields search; trace id joins the span",
            title="structured — never a secret",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Dashboard you built",
            _footer_left_code(
                ["// rate, errors, p50/p95/p99", "// deps + queue depth"],
                ["// page on SLO burn", "// tomorrow: oldest message"],
            ),
            [
                "Describe one dashboard you built",
                "Explain one alert threshold",
                "Name one missing signal",
            ],
            ["We have logging", "Page on every isolated error"],
            [
                ("Logs", "ILogger + Serilog", "why THIS request"),
                ("Metrics", "OTel meters", "how many hurt"),
                ("Traces", "Activity / OTel", "which hop"),
                ("Alert", "burn-rate rule", "user impact"),
            ],
            third="Interview",
        )

    return svg(
        "Observe What Users Experience",
        ".NET · D54  ·  Start from user questions — then the smallest signals",
        [
            panel(s[0], 1, "Three signals", "This request. How many. Which hop.", p1),
            panel(s[1], 2, "Question each signal answers", "Pick the glass that matches the question.", p2),
            panel(s[2], 3, "Dashboard tiles", "Version filters. Oldest message hides in depth.", p3),
            panel(s[3], 4, "The interview trap", "Noise is not observability.", p4),
            panel(s[4], 5, "A log line you can defend", "Structured fields and a trace id.", p5),
            panel(s[5], 6, "Practice & interview lines", "One dashboard, one alert, one gap.", p6),
        ],
    )


def d55():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Choice", "Gain", "Accepted cost"],
            [
                ("Async search index", "fast reads", "up to 2 min stale"),
                ("Strong write path", "correct stock", "higher latency"),
                ("More instances", "less saturation", "higher cost"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "The sentence they want", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 32, w, ["Constraint", "Options", "Accept X", "Gain Y"])
            + note(x, y + h - 24, w, "Name the trigger that would reverse the choice.", kind="star")
        )

    def p3(x, y, w, h):
        return _tri(
            x, y, w, h,
            [
                ("Stale OK", "discovery search can lag two minutes", "#eff6ff", "#1e40af"),
                ("Stock not", "inventory stays strongly consistent", "#f0fdf4", "#166534"),
                ("If stock in search", "do not serve it from the index", "#fef3c7", "#854d0e"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Always best",
            [
                "Microservices are always right.",
                "No constraint, no cost.",
            ],
            "Tied to Z",
            [
                "We accepted X to gain Y",
                "under constraint Z.",
                "If Z changes, we revisit.",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "// accepted: ≤2 min stale search",
                "// gained: isolate search from SQL",
                "// reverse if: stock in that payload",
                "// then: strong path for inventory",
            ],
            "we accepted X to gain Y under Z",
            title="tradeoff as one breath",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Frame it",
            _footer_left_code(
                ["// accepted 2 min stale search", "// gained latency + isolation"],
                ["// reverse: stock in that read", "// keep inventory strongly consistent"],
            ),
            [
                "Prepare one accepted-X-to-gain-Y",
                "Name two alternatives",
                "Change one constraint and adapt",
            ],
            ["Call one architecture always best", "Skip the downside"],
            [
                ("CAP in practice", "partition → pick", "avail vs strong write"),
                ("Staleness", "eventual index", "say the bound"),
                ("Cost", "instance count", "tied to saturation"),
                ("Revisit", "ADR status", "when Z changes"),
            ],
            third="Interview",
        )

    return svg(
        "Explain Architecture Tradeoffs Clearly",
        ".NET · D55  ·  We accepted X to gain Y — and we know what would reverse it",
        [
            panel(s[0], 1, "Choice / gain / cost", "Every option has a named downside.", p1),
            panel(s[1], 2, "How to frame a decision", "Constraint, options, accept, gain.", p2),
            panel(s[2], 3, "Search vs inventory", "Stale discovery is fine; stock is not.", p3),
            panel(s[3], 4, "The interview trap", "Always-best is not a tradeoff.", p4),
            panel(s[4], 5, "Say it in one breath", "X, Y, Z, and the reverse trigger.", p5),
            panel(s[5], 6, "Practice & interview lines", "Adapt when the constraint changes.", p6),
        ],
    )


def d56():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Section", "Answers", "Evidence"],
            [
                ("Context", "Why act now?", "failure + demand"),
                ("Options", "What else?", "same criteria"),
                ("Decision", "What we accept", "costs + owners"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.12, y, w * 0.76,
            ["Proposal: async invoices", "Challenge: delivery + support", "Evidence: outbox + DLQ", "ADR records the why"],
            fill="#ede9fe",
            ink="#5b21b6",
            h=h,
        )

    def p3(x, y, w, h):
        return bullets(
            x, y,
            [
                "Outbox for publish intent",
                "Idempotent consumer",
                "DLQ ownership named",
                "Reconciliation metric",
            ],
            color="#7c3aed",
            max_w=36,
            h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Decision theater",
            [
                "Only the preferred option.",
                "No objection recorded.",
                "Looks unanimous.",
            ],
            "Survived review",
            [
                "Credible alternatives",
                "Strongest objection replayed",
                "What evidence changed",
            ],
        )

    def p5(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "# ADR-014 async invoices",
                "Status: Accepted",
                "Context: sync timeouts at peak",
                "Decision: outbox + worker",
                "Rejected: bigger timeout",
                "Consequences: DLQ owner = billing",
            ],
            title="the record they can reopen",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Replay the debate",
            _footer_left_code(
                ["// objected: delivery guarantees", "// we added outbox + idempotent"],
                ["// objected: supportability", "// DLQ owner + recon metric"],
            ),
            [
                "Pick one challenged design",
                "Replay the strongest objection",
                "Say what changed and why",
            ],
            ["Document only the winner", "No alternatives, no consequences"],
            [
                ("ADR", "docs/adr/*.md", "context + choice"),
                ("Options", "same scorecard", "not a straw man"),
                ("Challenge", "review notes", "replay the debate"),
                ("Supersede", "new ADR", "when architecture moves"),
            ],
            third="Interview",
        )

    return svg(
        "Defend Designs With Evidence",
        ".NET · D56  ·  Assumptions reviewable before code makes them expensive",
        [
            panel(s[0], 1, "What an ADR must answer", "Why now, what else, what we accept.", p1),
            panel(s[1], 2, "Invoice design survived review", "Challenge changed the design.", p2),
            panel(s[2], 3, "What we added after pushback", "Outbox, idempotency, DLQ, metric.", p3),
            panel(s[3], 4, "The interview trap", "A preferred option is not a design review.", p4),
            panel(s[4], 5, "The record", "Status, rejected option, named owner.", p5),
            panel(s[5], 6, "Practice & interview lines", "Replay objections; show what changed.", p6),
        ],
    )


def d57():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["STAR", "Time", "Focus"],
            [
                ("Situation + task", "25 s", "stakes + ownership"),
                ("Action", "70 s", "your choices"),
                ("Result", "25 s", "numbers + learning"),
            ],
            header_fill="#dcfce7",
            last_green=True,
            h=h,
        )

    def p2(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("S + T  25s", "#64748b", "only the stakes"),
                ("Action  70s", "#16a34a", "decisions you made"),
                ("Result  25s", "#2563eb", "p95 2.4s → 380ms"),
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Claims intake — two minutes", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 32, w, ["Timeouts", "I owned API", "Queue docs", "3× volume"])
            + note(x, y + h - 24, w, "I, not we — then credit the team.", kind="star")
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Team-only story",
            [
                "We rebuilt the API.",
                "No ownership, no choice.",
                "Follow-ups stall.",
            ],
            "I + the team",
            [
                "I profiled the path",
                "I moved docs to a queue",
                "Team shipped the rest",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "// I owned claims intake API",
                "// profiled → idempotent queue",
                "// p95 2.4s → 380ms",
                "// volume ×3 with SLO boards",
            ],
            "two minutes, then take questions",
            title="one project STAR",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Ready stories",
            _footer_left_code(
                ["// story 1: intake latency", "// story 2: auth / tokens"],
                ["// story 3: a failure you owned", "// five follow-ups each"],
            ),
            [
                "Three two-minute STARs",
                "Replace vague we with I + credit",
                "Five follow-ups per story",
            ],
            ["We throughout", "Spend the two minutes on situation"],
            [
                ("S", "one sentence stakes", "not the company history"),
                ("T", "I owned X", "success criteria"),
                ("A", "choices + tradeoffs", "most of the time"),
                ("R", "a number", "and what you learned"),
            ],
            third="Interview",
        )

    return svg(
        "Tell Your Project Story",
        ".NET · D57  ·  Two minutes, I not we, numbers in the result",
        [
            panel(s[0], 1, "Clock the STAR", "Action gets most of the two minutes.", p1),
            panel(s[1], 2, "Where the seconds go", "25 / 70 / 25 — then stop.", p2),
            panel(s[2], 3, "Claims intake in one line", "Timeouts → queue → 380 ms at 3× volume.", p3),
            panel(s[3], 4, "The interview trap", "A team slogan hides your judgment.", p4),
            panel(s[4], 5, "The story as notes", "Ownership, action, measured result.", p5),
            panel(s[5], 6, "Practice & interview lines", "Two or three distinct stories.", p6),
        ],
    )


def d58():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Beat", "Strong", "Weak"],
            [
                ("Own", "names your gap", "blames another team"),
                ("Recover", "users first", "looking right"),
                ("Learn", "changes system", "I'll be careful"),
            ],
            header_fill="#fee2e2",
            h=h,
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["I skipped a load test", "Pool exhausted at peak", "I led rollback", "Gate + alert + canary"],
            fill="#fee2e2",
            ink="#b91c1c",
            h=h,
        )

    def p3(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Perf gate", "#1d4ed8", "load test in the pipeline"),
                ("Pool alert", "#ea580c", "saturation before users"),
                ("Canary", "#16a34a", "small % then promote"),
                ("Runbook", "#475569", "rollback is a step, not a hero"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Safe fake",
            [
                "I care too much.",
                "I work too hard.",
                "No incident, no change.",
            ],
            "Real gap",
            [
                "I approved without load",
                "Bounded user impact",
                "Four durable controls",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "// gap: config change, no load test",
                "// impact: SqlConnection pool empty",
                "// recover: rollback + communicate",
                "// after: gate, alert, canary, runbook",
            ],
            "own the omission — then the system change",
            title="one sentence of ownership",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Landing the story",
            _footer_left_code(
                ["// I approved X without Y", "// users: connection timeouts"],
                ["// I rolled back, then", "// gate + alert + canary"],
            ),
            [
                "Choose a real production failure",
                "State your gap in one sentence",
                "List technical and process changes",
            ],
            ["Blame another team", "Promise to be more careful"],
            [
                ("Own", "I skipped the test", "not 'the process failed'"),
                ("Recover", "rollback first", "protect users"),
                ("Learn", "why safeguards missed", "root, not heroics"),
                ("Change", "gate / alert / canary", "verified later"),
            ],
            third="Interview",
        )

    return svg(
        "Own Failure and Improve",
        ".NET · D58  ·  Specific gap, contained impact, durable prevention",
        [
            panel(s[0], 1, "Strong vs weak beats", "Ownership, recovery, system change.", p1),
            panel(s[1], 2, "The pool story", "Skip test → exhaust → rollback → gates.", p2),
            panel(s[2], 3, "What actually changed", "A promise is not a control.", p3),
            panel(s[3], 4, "The interview trap", "Perfectionism is not a failure story.", p4),
            panel(s[4], 5, "Say the gap once", "Then recovery and verified change.", p5),
            panel(s[5], 6, "Practice & interview lines", "Honest, bounded, durable.", p6),
        ],
    )


def d59():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Option", "Why considered", "Why it lost"],
            [
                ("PostgreSQL", "tx + reporting", "selected"),
                ("Document store", "flexible docs", "weak relational"),
                ("Event-only", "full history", "ops cost too high"),
            ],
            header_fill="#dbeafe",
            last_green=True,
            h=h,
        )

    def p2(x, y, w, h):
        return flow_h(x, y + 40, w, ["Constraint", "3 options", "Criteria", "Pick + trigger"])

    def p3(x, y, w, h):
        return bullets(
            x, y,
            [
                "Transactions were non-negotiable",
                "Relational reporting was real",
                "Team already operated Postgres",
                "Accepted: schema migrations",
            ],
            color="#2563eb",
            max_w=34,
            h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Predetermined",
            [
                "We always use Postgres.",
                "Alternatives listed after.",
            ],
            "Compared live",
            [
                "Criteria from the problem",
                "Two losers with reasons",
                "Revisit: partition / read model",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "// chose Postgres for orders",
                "// rejected document + event-only",
                "// validated with load tests",
                "// revisit: partition or read model",
            ],
            "advantage AND accepted downside",
            title="decision in four lines",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Criteria first",
            _footer_left_code(
                ["// goals, risk, cost, ops", "// two credible losers"],
                ["// load-test the winner", "// write the revisit trigger"],
            ),
            [
                "One consequential decision",
                "Two rejected alternatives",
                "Criteria, outcome, revisit",
            ],
            ["List alternatives after deciding", "Skip the accepted downside"],
            [
                ("Constraint", "tx + reporting", "say non-negotiables"),
                ("Loser 1", "document store", "why it almost won"),
                ("Loser 2", "event-only", "ops cost"),
                ("Trigger", "read model later", "when scale changes"),
            ],
            third="Interview",
        )

    return svg(
        "Tell a Decision Story",
        ".NET · D59  ·  Constraints and evidence eliminated credible alternatives",
        [
            panel(s[0], 1, "Three options on the table", "Why each was real — why two lost.", p1),
            panel(s[1], 2, "How judgment looks", "Constraint → options → criteria → trigger.", p2),
            panel(s[2], 3, "Why Postgres won", "Transactions, reporting, operating skill.", p3),
            panel(s[3], 4, "The interview trap", "A predetermined choice is not judgment.", p4),
            panel(s[4], 5, "The decision card", "Winner, losers, proof, revisit.", p5),
            panel(s[5], 6, "Practice & interview lines", "Usually two or three credible options.", p6),
        ],
    )


def d60():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Metric", "Before", "After"],
            [
                ("p95 latency", "1.8 s", "420 ms"),
                ("Compute cost", "baseline", "28% lower"),
                ("Tickets / mo", "90", "15"),
            ],
            header_fill="#dcfce7",
            last_green=True,
            h=h,
        )

    def p2(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("420 ms p95", "#16a34a", "from 1.8 s at 600 RPS"),
                ("−28% compute", "#2563eb", "same peak, fewer boxes"),
                ("15 tickets", "#7c3aed", "timeouts were 90 / month"),
            ],
        )

    def p3(x, y, w, h):
        return flow_h(x, y + 40, w, ["Baseline", "Change", "Scale", "Meaning"])

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Number-free",
            [
                "Performance improved a lot.",
                "No baseline, no window.",
            ],
            "Two numbers",
            [
                "Technical: p95 1.8s→420ms",
                "Business: 90→15 tickets",
                "At 600 RPS peak",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "// p95 checkout 1.8s → 420ms",
                "// peak 600 RPS",
                "// compute −28%",
                "// timeout tickets 90 → 15 / mo",
            ],
            "baseline + result + scale + meaning",
            title="say two numbers without prompting",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Put numbers on STAR",
            _footer_left_code(
                ["// technical: latency / RPS", "// business: cost / tickets"],
                ["// window: peak month", "// credit: what I vs team did"],
            ),
            [
                "Two real numbers on every STAR",
                "Record source and window",
                "Connect to user or cost impact",
            ],
            ["Significantly improved", "Claim a team metric as only yours"],
            [
                ("Baseline", "1.8 s p95", "no magnitude without it"),
                ("Scale", "600 RPS", "the load it survived"),
                ("Cost", "−28%", " infra meaning"),
                ("User", "90→15 tickets", "support meaning"),
            ],
            third="Interview",
        )

    return svg(
        "Prove Impact With Numbers",
        ".NET · D60  ·  Baseline, change, scale, business meaning — unprompted",
        [
            panel(s[0], 1, "Before / after", "Latency, cost, tickets — same story.", p1),
            panel(s[1], 2, "Three numbers, one breath", "Technical + cost + user.", p2),
            panel(s[2], 3, "How a number earns meaning", "Start, change, load, why it mattered.", p3),
            panel(s[3], 4, "The interview trap", "Improved is not evidence.", p4),
            panel(s[4], 5, "The impact card", "Two number types, one window.", p5),
            panel(s[5], 6, "Practice & interview lines", "Do not overclaim causation.", p6),
        ],
    )


def d61():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Four pillars",
            [
                "OOP is encapsulation,",
                "inheritance, polymorphism.",
                "No project, no keyword.",
            ],
            "A scenario",
            [
                "Two device stacks",
                "IDeviceAdapter contract",
                "sealed Tas / Tasnx",
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["They say", "You say from the project"],
            [
                ("interface vs abstract", "IDeviceAdapter — no forced base"),
                ("sealed", "TasAdapter cannot be subclassed"),
                ("private ctor", "HubOptions.FromConfig only"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 6, "Problem first, then the keyword", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 28, w, ["Two hubs", "IDeviceAdapter", "Tas", "Tasnx"])
            + note(x, y + h - 24, w, "Abstract would lock one inheritance tree.", kind="star")
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "public interface IDeviceAdapter {",
                "  Task SendAsync(string g, object p);",
                "}",
                "public sealed class TasAdapter : …",
            ],
            "abstraction + polymorphism + sealed",
            title="contract, then sealed impls",
        )

    def p5(x, y, w, h):
        return table(
            x, y, w, ["Keyword", "Interview use"],
            [
                ("this / base", "ctor chaining — current vs parent"),
                ("static", "type-level, no instance"),
                ("var vs dynamic", "inference vs skipped checks"),
                ("record", "value equality for DTOs"),
            ],
            header_fill="#f3e8ff",
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Start from the problem",
            _footer_left_code(
                ["// two adapters, no common base", "// extract IDeviceAdapter"],
                ["// sealed impls + factory", "// private ctor if creation gated"],
            ),
            [
                "Answer the keyword they used",
                "Give the project scenario first",
                "Name sealed / private ctor if true",
            ],
            ["Recite the four pillars", "Define without a scenario"],
            [
                ("Abstraction", "interface contract", "callers ignore Tas vs Tasnx"),
                ("Sealed", "sealed class Adapter", "no further inheritance"),
                ("Factory", "private ctor + FromConfig", "control creation"),
                ("Record", "record OrderDto", "value-like DTO equality"),
            ],
            third="Interview",
        )

    return svg(
        "OOP Principles Pack",
        ".NET · D61  ·  A project scenario — not a four-pillars recitation",
        [
            panel(s[0], 1, "They want a story", "Keyword in, scenario out.", p1),
            panel(s[1], 2, "Map the keyword", "Interface vs abstract is the usual trap.", p2),
            panel(s[2], 3, "Two adapters, one contract", "No forced base class.", p3),
            panel(s[3], 4, "The code they hear", "Interface + two sealed implementations.", p4),
            panel(s[4], 5, "Other keywords, same rule", "this/base, static, var, records — with use.", p5),
            panel(s[5], 6, "Practice & interview lines", "Problem, then the language tool.", p6),
        ],
    )


def d62():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Growing if/else",
            [
                "if (hub == Tas) …",
                "else if (hub == Tasnx)",
                "Next vendor = another if.",
            ],
            "New class",
            [
                "IHubForwarder",
                "TasnxForwarder added",
                "ForwardMiddleware closed",
            ],
        )

    def p2(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("OCP", "#1d4ed8", "new class, not a new if"),
                ("DIP", "#7c3aed", "policy depends on IHubForwarder"),
                ("LSP", "#15803d", "no NotImplementedException"),
                ("SRP / ISP", "#ea580c", "split fat interfaces"),
            ],
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["Problem: second SignalR stack", "Extract IHubForwarder", "Add TasnxForwarder", "Old middleware not rewritten"],
            fill="#dbeafe",
            ink="#1e40af",
            h=h,
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "public interface IHubForwarder {",
                "  Task ForwardAsync(HttpContext c);",
                "}",
                "// Bluefin later = another class",
            ],
            "new class, same interface — OCP + DIP",
            title="the change story",
        )

    def p5(x, y, w, h):
        return table(
            x, y, w, ["Letter", "Fail they catch", "Your line"],
            [
                ("LSP", "throw in override", "honor the contract"),
                ("ISP", "one fat interface", "IRead vs IWrite"),
                ("SRP", "god service", "one reason to change"),
            ],
            header_fill="#ffedd5",
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Problem / class / next",
            _footer_left_code(
                ["// problem: second hub stack", "// class: TasnxForwarder"],
                ["// closed: ForwardMiddleware", "// next: another adapter class"],
            ),
            [
                "Problem, class that changed, next variant",
                "Say the old code was not rewritten",
                "Name DIP: depend on the interface",
            ],
            ["Quote OCP with no story", "Add a vendor with another if"],
            [
                ("OCP", "new IHubForwarder impl", "not if/else"),
                ("DIP", "ctor IHubForwarder", "not TasnxForwarder"),
                ("LSP", "no NIEX in override", "callers keep working"),
                ("ISP", "split read/write", "callers unused methods"),
            ],
            third="Interview",
        )

    return svg(
        "SOLID With a Change Story",
        ".NET · D62  ·  New class behind an interface — not a growing if/else",
        [
            panel(s[0], 1, "The OCP picture", "Next variant is a type, not a branch.", p1),
            panel(s[1], 2, "Five letters, one job each", "OCP and DIP carry the story.", p2),
            panel(s[2], 3, "TASNX hub change", "Extract, add class, leave middleware closed.", p3),
            panel(s[3], 4, "The code of the story", "Bluefin = another class later.", p4),
            panel(s[4], 5, "The other letters", "LSP, ISP, SRP — still with a fail they catch.", p5),
            panel(s[5], 6, "Practice & interview lines", "Problem, class, next adapter.", p6),
        ],
    )


def d63():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Repo per DbSet",
            [
                "Orders => _db.Orders",
                "No query reused",
                "Looks enterprise",
            ],
            "Thin + UoW",
            [
                "GetOpenByCustomerAsync",
                "DbContext IS the UoW",
                "One SaveChanges",
            ],
        )

    def p2(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Use case / handler", "debit wallet + outbox row"),
                ("IWalletRepository", "GetTrackedAsync — reused query"),
                ("AppDbContext : IUnitOfWork", "SaveChanges = one transaction"),
            ],
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["GetTracked wallet", "wallet.Debit(amount)", "Outbox.Add(debited)", "SaveChangesAsync once"],
            fill="#dcfce7",
            ink="#166534",
            h=h,
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Add a repo when", "Skip when"],
            [
                ("Query is reused", "One-off CRUD"),
                ("Domain must not see EF", "Handler already is the app"),
                ("Tests need a fake", "Wrapping every DbSet"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "var w = await _wallets.GetTracked(id);",
                "w.Debit(amount);",
                "_db.Outbox.Add(new Outbox(w.Id));",
                "await _uow.SaveChangesAsync(ct);",
            ],
            "debit + outbox in one transaction",
            title="DbContext is the unit of work",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say the overlap",
            _footer_left_code(
                ["// DbContext already is UoW", "// SaveChanges = the commit"],
                ["// repo = intention, not DbSet", "// wallet + outbox together"],
            ),
            [
                "Call DbContext the unit of work",
                "Repo only for reused queries",
                "One SaveChanges per use case",
            ],
            ["Repository per table", "Split a business txn across SaveChanges"],
            [
                ("UoW", "DbContext.SaveChanges", "several changes, one commit"),
                ("Repo", "GetActiveAsync()", "hides Include/Where"),
                ("Without", "SQL in every handler", "tests cannot fake"),
                ("Outbox", "same SaveChanges", "atomic with the debit"),
            ],
            third="Interview",
        )

    return svg(
        "Repository and Unit of Work",
        ".NET · D63  ·  DbContext already is the unit of work",
        [
            panel(s[0], 1, "The extra-type trap", "A pass-through DbSet is not a repository.", p1),
            panel(s[1], 2, "Where each type sits", "Handler, thin repo, context as UoW.", p2),
            panel(s[2], 3, "One business transaction", "Debit and outbox commit together.", p3),
            panel(s[3], 4, "When the extra type is worth it", "Reuse, domain boundary, test seam.", p4),
            panel(s[4], 5, "The use-case shape", "Mutate, add outbox, one SaveChanges.", p5),
            panel(s[5], 6, "Practice & interview lines", "Not enterprise theater.", p6),
        ],
    )


def d64():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "MediatR = CQRS",
            [
                "We use MediatR",
                "so we have CQRS.",
                "Dispatcher ≠ model split.",
            ],
            "Two models",
            [
                "Write: Order aggregate",
                "Read: OrderListView",
                "Split only when pain is real",
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Side", "Job", "Shape"],
            [
                ("Command", "mutate + persist", "CreateOrder"),
                ("Query", "return a screen", "OrderListItem DTO"),
                ("Why split", "list crushed writes", "denormalized read"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Command", "invariants"),
                ("SaveChanges", "write schema"),
                ("Event", "optional"),
            ],
            "Write aggregate",
            "List view / SQL",
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "public record CreateOrder(Guid Id);",
                "public record OrderListItem(",
                "  Guid Id, string Status);",
                "// read: OrderListView, not graph",
            ],
            "two models, one reason: list vs write",
            title="command vs read DTO",
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "CRUD one table → do not split",
                "Same EF entity + filter → no CQRS",
                "Say we did not need it if true",
                "Pain = list joins crushing writes",
            ],
            color="#7c3aed",
            max_w=36,
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Exact scenario",
            _footer_left_code(
                ["// write: Order invariants", "// read: denormalized list"],
                ["// MediatR = dispatcher only", "// skip if CRUD is enough"],
            ),
            [
                "Give the scenario that justified the split",
                "Or say you did not need CQRS",
                "Never equate it with MediatR",
            ],
            ["We have MediatR so we have CQRS", "Split a one-table CRUD module"],
            [
                ("CQRS", "two models", "not IRequest<>"),
                ("Command", "CreateOrder handler", "mutate + persist"),
                ("Query", "list DTO / view", "no write graph"),
                ("When not", "simple EF filters", "say so honestly"),
            ],
            third="Interview",
        )

    return svg(
        "CQRS — Exact Scenario",
        ".NET · D64  ·  Command/write vs query/read — MediatR is not CQRS",
        [
            panel(s[0], 1, "The naming trap", "A dispatcher is not a model split.", p1),
            panel(s[1], 2, "Two sides", "Strict writes. Flattened reads.", p2),
            panel(s[2], 3, "How the split looks", "Write schema vs list projection.", p3),
            panel(s[3], 4, "Two records, two jobs", "Command in; list DTO out.", p4),
            panel(s[4], 5, "When you refuse CQRS", "Honesty beats a pattern name.", p5),
            panel(s[5], 6, "Practice & interview lines", "Exact pain, or we did not split.", p6),
        ],
    )


def d65():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Distributed rollback",
            [
                "Shipment fails →",
                "rollback three DBs",
                "in one SQL transaction.",
            ],
            "Compensate",
            [
                "ShipmentFailed event",
                "Payment refunds (idempotent)",
                "Inventory releases hold",
            ],
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 6, "Happy path — each service commits locally", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 32, w, ["Order", "Pay", "Reserve", "Ship"])
            + note(x, y + h - 24, w, "No BEGIN TRAN across independently deployed services.", kind="warn")
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Reserve fails after pay", "InventoryReserveFailed", "Payment RefundAsync", "Must be idempotent"],
            fill="#ffedd5",
            ink="#9a3412",
            h=h,
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Style", "Who decides", "You name"],
            [
                ("Choreography", "each service reacts", "events you published"),
                ("Orchestration", "one coordinator", "the worker you owned"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "try { await ReserveAsync(id); }",
                "catch {",
                "  await bus.Publish(",
                "    new ReserveFailed(id)); }",
                "// payment: RefundAsync — idempotent",
            ],
            "compensation event, not DTC",
            title="later-step failure",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Walk a failure",
            _footer_left_code(
                ["// pay committed locally", "// reserve fails → event"],
                ["// refund handler idempotent", "// inventory releases hold"],
            ),
            [
                "Walk a later-step failure",
                "Name the compensating event",
                "Say which style you used",
            ],
            ["Claim a distributed SQL rollback", "Skip idempotency on refund"],
            [
                ("No DTC", "one commit / service", "cannot span DBs"),
                ("Compensate", "RefundRequested", "more events, not undo SQL"),
                ("Idempotent", "refund key = order id", "retries will happen"),
                ("Style", "choreo vs orchestrator", "name yours"),
            ],
            third="Interview",
        )

    return svg(
        "Saga and Compensating Actions",
        ".NET · D65  ·  No distributed SQL rollback — compensate with events",
        [
            panel(s[0], 1, "The DTC trap", "Three services do not share a transaction.", p1),
            panel(s[1], 2, "Happy path", "Order → pay → reserve → ship, local commits.", p2),
            panel(s[2], 3, "Reserve fails after pay", "Refund and release — more messages.", p3),
            panel(s[3], 4, "Choreography vs orchestration", "Name which you actually ran.", p4),
            panel(s[4], 5, "The compensation trigger", "Publish failure; refund must be idempotent.", p5),
            panel(s[5], 6, "Practice & interview lines", "Later-step failure, named event.", p6),
        ],
    )


def d66():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Approach", "Starts from", "When"],
            [
                ("Code First", "classes + migrations", "new service you own"),
                ("Database First", "existing schema", "legacy SQL Server"),
                ("Fluent API", "OnModelCreating", "keys, precision, delete"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "b.Entity<Wallet>(e => {",
                "  e.HasKey(x => x.Id);",
                "  e.Property(x => x.Balance)",
                "    .HasPrecision(18, 2);",
                "});",
            ],
            title="Fluent — keep entities clean",
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "String concat",
            [
                'ExecuteSqlRaw("exec " + id)',
                "Injection + broken tracking",
            ],
            "Interpolated + no track",
            [
                "FromSqlInterpolated($\"EXEC …\")",
                "AsNoTracking for reads",
            ],
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["OnModelCreating mappings", "FromSqlInterpolated EXEC", "AsNoTracking for lists", "Txn if paired with writes"],
            fill="#ffedd5",
            ink="#9a3412",
            h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "var rows = await _db.Set<OrderRow>()",
                "  .FromSqlInterpolated(",
                "    $\"EXEC dbo.GetOpenOrders {id}\")",
                "  .AsNoTracking().ToListAsync();",
            ],
            "parameterized SP — never concatenated",
            title="call the procedure on purpose",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Name the approach",
            _footer_left_code(
                ["// brownfield: database-first", "// Fluent for conversions"],
                ["// SP: FromSqlInterpolated", "// AsNoTracking on reads"],
            ),
            [
                "Name Code First vs Database First",
                "Show one Fluent mapping",
                "Call SPs parameterized",
            ],
            ["Concatenate SQL into ExecuteSqlRaw", "Hide all C# in stored procedures"],
            [
                ("Code First", "migrations", "you own the schema"),
                ("DB First", "scaffold / map", "legacy you cannot rewrite"),
                ("Fluent", "OnModelCreating", "composite keys, precision"),
                ("SP", "FromSqlInterpolated", "AsNoTracking lists"),
            ],
            third="Interview",
        )

    return svg(
        "EF Mapping: Code First, Fluent API, SPs",
        ".NET · D66  ·  Name the approach — parameterized SPs, not string concat",
        [
            panel(s[0], 1, "Three mapping choices", "Code First, Database First, Fluent.", p1),
            panel(s[1], 2, "Fluent that does not clutter entities", "Keys, precision, restrict delete.", p2),
            panel(s[2], 3, "The SP trap", "Concatenation is injection.", p3),
            panel(s[3], 4, "How an SP is invoked", "Map, parameterize, don't track lists.", p4),
            panel(s[4], 5, "The call they want", "FromSqlInterpolated + AsNoTracking.", p5),
            panel(s[5], 6, "Practice & interview lines", "SPs for proven set-based SQL only.", p6),
        ],
    )


def d67():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Bytes on the bus",
            [
                "FileReceived { Bytes = … }",
                "Kills retries and memory",
                "Hops Gateway → A → queue → B",
            ],
            "Store then publish",
            [
                "Upload stream to S3",
                "FileReady { Bucket, Key, Sha }",
                "Consumer pulls what it needs",
            ],
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 6, "Firmware / invoice PDF", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 28, w, ["Stream", "S3 key", "SQL meta", "Event"])
            + note(x, y + h - 24, w, "The queue never carried the file.", kind="star")
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("PUT object", "stream"),
                ("FileMeta", "SQL"),
                ("FileReady", "id + uri"),
            ],
            "202 + job id",
            "Worker pulls object",
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Limit", "If you put the file there"],
            [
                ("Broker payload", "publish fails / truncates"),
                ("API Gateway", "timeout / payload cap"),
                ("Retry", "re-sends 200 MB"),
            ],
            header_fill="#fee2e2",
            h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "await _storage.PutAsync(b, key, stream);",
                "_db.Files.Add(new FileMeta(key, sha));",
                "await _uow.SaveChangesAsync();",
                "await _bus.Publish(new FileReady(…));",
            ],
            "Accepted({ jobId }) — not the bytes",
            title="store, persist, publish location",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "The pattern",
            _footer_left_code(
                ["// stream to object storage", "// metadata in SQL"],
                ["// event: bucket, key, sha, size", "// 202 + job id to Angular"],
            ),
            [
                "Store object then publish location",
                "Do not load a 200 MB byte[]",
                "Process off the request thread",
            ],
            ["Put the file on the event", "Hop the blob through every service"],
            [
                ("Upload", "stream to S3", "not byte[] in Kestrel"),
                ("Meta", "FileMeta row", "checksum + size"),
                ("Event", "FileReady key", "reference only"),
                ("HTTP", "202 Accepted", "job id for polling"),
            ],
            third="Interview",
        )

    return svg(
        "Large Payload and Object References",
        ".NET · D67  ·  Store the object — publish the location, not the bytes",
        [
            panel(s[0], 1, "Bus vs reference", "A 200 MB file does not belong on the message.", p1),
            panel(s[1], 2, "The path", "Stream → storage → SQL → small event.", p2),
            panel(s[2], 3, "Async processing", "202 to the UI; worker pulls the object.", p3),
            panel(s[3], 4, "Why the bus dies", "Payload caps, timeouts, retry amplification.", p4),
            panel(s[4], 5, "The four lines", "Put, persist, publish, Accepted.", p5),
            panel(s[5], 6, "Practice & interview lines", "Location and checksum on the event.", p6),
        ],
    )


def d68():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["If you used", "Say this", "Do not say"],
            [
                ("Cognito", "issuer + audience", "invent IdentityServer"),
                ("Entra / AAD", "tenant + app id", "invent a user pool"),
                ("IdentityServer", "authority + client", "claim Cognito"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Login", "SPA / hosted UI"),
                ("IdP", "issues JWTs"),
                ("API", "JwtBearer"),
            ],
            "Angular Bearer",
            "task IAM ≠ user",
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "IAM as login",
            [
                "Users log in with",
                "IAM access keys",
                "from Angular.",
            ],
            "IdP then JWT",
            [
                "Users authenticate at IdP",
                "API validates JWT",
                "IAM is for ECS → S3",
            ],
        )

    def p4(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("SSO", "#1d4ed8", "one login, several apps, same IdP"),
                ("IdentityServer / OIDC", "#7c3aed", "issues tokens; API is bearer"),
                ("Cognito", "#16a34a", "user pool — same issuer/aud story"),
                ("IAM", "#475569", "task role, not the SPA password"),
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                ".AddJwtBearer(o => {",
                "  o.Authority = cfg[\"Auth:Authority\"];",
                "  o.Audience = cfg[\"Auth:Audience\"];",
                "  o.TokenValidationParameters",
                "    .ValidateLifetime = true;",
                "});",
            ],
            "iss + aud + exp — name the real IdP",
            title="API trusts the IdP",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Name the real IdP",
            _footer_left_code(
                ["// used Cognito → issuer URL", "// used Entra → tenant"],
                ["// API: JwtBearer checks", "// IAM: task role to S3"],
            ),
            [
                "Draw login → IdP → tokens → API",
                "Name the product you actually ran",
                "Keep IAM off the SPA login story",
            ],
            ["Invent IdentityServer", "IAM access keys from Angular"],
            [
                ("IdP", "AddJwtBearer Authority", "Cognito / Entra / IS"),
                ("SSO", "same IdP session", "several apps"),
                ("JWT", "iss + aud + exp", "roles still in claims"),
                ("IAM", "ECS task role", "not the user's password"),
            ],
            third="Interview",
        )

    return svg(
        "SSO, IdentityServer, Cognito Awareness",
        ".NET · D68  ·  Name the real IdP — IAM is not the SPA login",
        [
            panel(s[0], 1, "Name the real IdP", "Inventing Cognito is worse than naming Entra.", p1),
            panel(s[1], 2, "How a login travels", "IdP issues tokens. API validates. IAM is compute.", p2),
            panel(s[2], 3, "The IAM mix-up", "Humans use the IdP. Tasks assume a role.", p3),
            panel(s[3], 4, "Four words, four jobs", "SSO, OIDC, Cognito, IAM — unmixed.", p4),
            panel(s[4], 5, "What the API checks", "Authority, audience, lifetime.", p5),
            panel(s[5], 6, "Practice & interview lines", "Same JWT story, honest product name.", p6),
        ],
    )


def d69():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("1–4  business, users, Angular, auth", "#1e3a5f", "who and how they sign in"),
                ("5–8  gateway, YOUR APIs, REST/events, DB", "#2563eb", "two services deep"),
                ("9–12 AWS, deploy, monitor, I built X", "#16a34a", "finish on contribution"),
            ],
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Ten microservices",
            [
                "We have ten services",
                "on AWS.",
                "Cannot draw any.",
            ],
            "Two you owned",
            [
                "Device API: REST + EF",
                "Notify worker: queue",
                "I built TAS middleware",
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "The spine of the six minutes", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 32, w, ["Angular", "Gateway", "My API", "SQL", "Event"])
            + note(x, y + h - 24, w, "Then Docker/ECS and one dashboard. Stop.", kind="star")
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Service", "What I can draw"],
            [
                ("Device API", "REST, EF, owner DB"),
                ("Notify worker", "queue, idempotent, DLQ"),
                ("My contribution", "TAS bridge middleware"),
            ],
            header_fill="#dcfce7",
            h=h,
        )

    def p5(x, y, w, h):
        return code_box(
            x, y, w, h,
            [
                "// 6 minutes, out loud:",
                "// 1 business  2 users  3 Angular  4 auth",
                "// 5 gateway   6 my two services",
                "// 7 REST vs events  8 SQL ownership",
                "// 9 AWS  10 deploy  11 monitor",
                "// 12 I built …",
            ],
            title="twelve beats — two services deep",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Rehearse the clock",
            _footer_left_code(
                ["// start: who the user is", "// middle: the API I owned"],
                ["// event I published", "// end: I built X — not we"],
            ),
            [
                "Time a 5–7 minute walk",
                "Two or three services you owned",
                "Finish on personal contribution",
            ],
            ["Dump ten microservice names", "Skip beat 12 — your work"],
            [
                ("Spine", "Angular→GW→API→SQL", "then one event"),
                ("Depth", "two services", "not a catalog"),
                ("AWS", "only what you used", "honest platform vs you"),
                ("Beat 12", "I designed / built", "not we"),
            ],
            third="Interview",
        )

    return svg(
        "Architecture 5–7 Minute Talk",
        ".NET · D69  ·  Twelve beats — two services you owned, then I built X",
        [
            panel(s[0], 1, "Twelve beats in three bands", "Users and auth, your APIs, then you.", p1),
            panel(s[1], 2, "The catalog trap", "Names you cannot explain will be pulled.", p2),
            panel(s[2], 3, "The drawing", "One path through the service you owned.", p3),
            panel(s[3], 4, "Two services deep", "Device API and Notify — plus contribution.", p4),
            panel(s[4], 5, "The rehearsal card", "Cover all twelve. Do not dump names.", p5),
            panel(s[5], 6, "Practice & interview lines", "Timed walk, I not we.", p6),
        ],
    )


def d70():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Events for GetById",
            [
                "Everything is event-driven",
                "including status reads.",
                "UI is waiting.",
            ],
            "Pick with a reason",
            [
                "Waiting user = REST",
                "Fan-out after commit = event",
                "Event carries an id + URI",
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Need", "Choose", "Failure mode"],
            [
                ("Answer now", "REST", "timeouts + retries"),
                ("Many reactors", "event", "at-least-once + DLQ"),
                ("Spike buffer", "queue", "depth + oldest msg"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 6, "Same device, two shapes", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 28, w, ["GET status", "REST now", "inventory write", "DeviceUpdated"])
            + note(x, y + h - 24, w, "Event: id + URI — never a 20 MB package.", kind="star")
        )

    def p4(x, y, w, h):
        return hub(
            x, y, w, h,
            "commit",
            ["Notify", "Report", "Analytics", "REST UI"],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "[HttpGet(\"{id}\")]",
                "public Task<DeviceDto> Get(Guid id)",
                "  => _repo.GetAsync(id);",
                "await _bus.Publish(new DeviceUpdated(id));",
            ],
            "waiting user = REST; fan-out = event + ref",
            title="two verbs, two reasons",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Choose out loud",
            _footer_left_code(
                ["// live command: REST", "// UI needs the answer"],
                ["// inventory changed: event", "// id + URI, not the package"],
            ),
            [
                "Pick REST or events with a reason",
                "Never put a large blob on the event",
                "Name retry vs idempotent+DLQ",
            ],
            ["Make GetById event-driven", "Put the file on the message"],
            [
                ("REST", "HttpGet DeviceDto", "user is waiting"),
                ("Event", "DeviceUpdated(id)", "temporal decoupling"),
                ("Retry REST", "HttpClient policy", "bounded"),
                ("Retry event", "idempotent + DLQ", "at-least-once"),
            ],
            third="Interview",
        )

    return svg(
        "Events vs REST and Event Size",
        ".NET · D70  ·  Waiting user = REST. Fan-out after commit = event with a reference",
        [
            panel(s[0], 1, "The everything-events trap", "GetById stays request/response.", p1),
            panel(s[1], 2, "When each wins", "Now vs many consumers vs buffer.", p2),
            panel(s[2], 3, "One device, two paths", "Live status REST; inventory event.", p3),
            panel(s[3], 4, "Fan-out after commit", "UI can still GET. Others subscribe.", p4),
            panel(s[4], 5, "The two snippets", "GET returns. Publish carries an id.", p5),
            panel(s[5], 6, "Practice & interview lines", "Same size rule as D67.", p6),
        ],
    )


def d71():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "ex.ToString()",
            [
                "return 500, ex.Message",
                "SQL and stacks in Angular",
                "No trace to find the log",
            ],
            "ProblemDetails",
            [
                "Stable error contract",
                "Log exception server-side",
                "X-Trace-Id on the way out",
            ],
        )

    def p2(x, y, w, h):
        return (
            t(x, y + 8, "On the way in — registration order", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 32, w, ["Exception mw", "Auth", "Endpoint"])
            + note(x, y + h - 24, w, "Register exception handling first so it wraps the rest.", kind="star")
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.10, y, w * 0.80,
            ["await next() — action runs", "pipeline unwinds", "add X-Trace-Id header", "log + ProblemDetails on throw"],
            fill="#ede9fe",
            ink="#5b21b6",
            h=h,
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Piece", "Goes to Angular", "Stays on server"],
            [
                ("title / status", "yes — ProblemDetails", "—"),
                ("trace id", "header + body", "same id in logs"),
                ("stack / SQL", "never", "ILogger"),
            ],
            header_fill="#f3e8ff",
            h=h,
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "var trace = ctx.TraceIdentifier;",
                "ctx.Response.Headers[\"X-Trace-Id\"] = trace;",
                "try { await next(); }",
                "catch (Exception ex) {",
                "  _log.LogError(ex, \"{Trace}\", trace);",
                "  await WriteProblem(ctx, trace); }",
            ],
            "middleware runs after the controller too",
            title="unwind is how the header is added",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Contract + correlation",
            _footer_left_code(
                ["// UseExceptionHandler first", "// ProblemDetails + trace"],
                ["// Angular: 401 → login", "// 5xx → friendly + trace id"],
            ),
            [
                "Show middleware that logs a trace id",
                "Return ProblemDetails, not ex.Message",
                "Say the pipeline unwinds after the action",
            ],
            ["return StatusCode(500, ex.ToString())", "Leak SQL to the SPA"],
            [
                ("In", "exception mw first", "wraps auth + endpoint"),
                ("Out", "after await next()", "headers + timing"),
                ("Body", "ProblemDetails", "title + trace"),
                ("Angular", "interceptor", "same trace for support"),
            ],
            third="Interview",
        )

    return svg(
        "Global Exceptions and Correlation",
        ".NET · D71  ·  ProblemDetails + trace id — middleware still runs on the way out",
        [
            panel(s[0], 1, "The leak trap", "Stacks belong in logs, not the SPA.", p1),
            panel(s[1], 2, "On the way in", "Exception middleware registered first.", p2),
            panel(s[2], 3, "On the way out", "After the controller, the pipeline unwinds.", p3),
            panel(s[3], 4, "The error contract", "Stable body. Same id in logs.", p4),
            panel(s[4], 5, "The middleware", "Header always; ProblemDetails on throw.", p5),
            panel(s[5], 6, "Practice & interview lines", "Trace id on every response.", p6),
        ],
    )


def d72():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("What", "#1e3a5f", "one sentence a skeptic trusts"),
                ("Where", "#2563eb", "Program.cs / class / pipeline"),
                ("Why", "#16a34a", "the alternative you rejected"),
                ("How", "#7c3aed", "two implementation details"),
                ("Problem", "#dc2626", "latency, incident, or coupling"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Q", "DI"],
            [
                ("What", "invert creation; swap impls"),
                ("Where", "Program.cs + DeviceService ctor"),
                ("Why", "new SqlRepo() blocked tests"),
                ("How", "AddScoped<IDevice, Device>"),
                ("Problem", "caught captive DbContext"),
            ],
            header_fill=TBL[1],
            h=h,
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Q", "JWT"],
            [
                ("What", "bearer proof of identity"),
                ("Where", "AddJwtBearer + [Authorize]"),
                ("Why", "not cookies on a public API"),
                ("How", "iss + aud + exp"),
                ("Problem", "401 from wrong audience"),
            ],
            header_fill=TBL[0],
            h=h,
        )

    def p4(x, y, w, h):
        return table(
            x, y, w, ["Q", "EF Core"],
            [
                ("What", "change tracker + SQL"),
                ("Where", "AppDbContext in Device API"),
                ("Why", "not raw ADO for this domain"),
                ("How", "AsNoTracking lists; SaveChanges"),
                ("Problem", "N+1 until Include/split query"),
            ],
            header_fill=TBL[4],
            h=h,
        )

    def p5(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Best practice",
            [
                "We used DI because",
                "it is best practice.",
                "Where and How empty.",
            ],
            "Five sentences",
            [
                "What / Where / Why",
                "How / Problem",
                "Then stop.",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say aloud",
            _footer_left_code(
                ["// What / Where / Why / How / Problem", "// — DI"],
                ["// What / Where / Why / How / Problem", "// — JWT  then EF"],
            ),
            [
                "All five for DI, JWT, EF",
                "One AWS service if it is on the resume",
                "If a blank exists, drop the topic",
            ],
            ["Skip Where and How", "Best practice with no problem"],
            [
                ("What", "one trusted sentence", "not a slogan"),
                ("Where", "a type name", "in YOUR drawing"),
                ("How", "lifetime / iss+aud", "two details"),
                ("Problem", "a number or incident", "why it existed"),
            ],
            third="Interview",
        )

    return svg(
        "Five-Question Drill",
        ".NET · D72  ·  What / Where / Why / How / Problem — then stop",
        [
            panel(s[0], 1, "The five questions", "Every resume box gets these five.", p1),
            panel(s[1], 2, "Worked example: DI", "Do this out loud without stalling.", p2),
            panel(s[2], 3, "Worked example: JWT", "Issuer, audience, 401 you actually saw.", p3),
            panel(s[3], 4, "Worked example: EF", "Where the context lives and the N+1.", p4),
            panel(s[4], 5, "The interview trap", "Best practice is not an answer.", p5),
            panel(s[5], 6, "Practice & interview lines", "Five sentences. If any is empty, cut it.", p6),
        ],
    )


BUILDERS = [
    ("D49", "Make Messaging Fail Safely", d49),
    ("D50", "Contain Failures by Design", d50),
    ("D51", "Turn NFRs Into Numbers", d51),
    ("D52", "Estimate Capacity Before Scaling", d52),
    ("D53", "Map Threats to Controls", d53),
    ("D54", "Observe What Users Experience", d54),
    ("D55", "Explain Architecture Tradeoffs Clearly", d55),
    ("D56", "Defend Designs With Evidence", d56),
    ("D57", "Tell Your Project Story", d57),
    ("D58", "Own Failure and Improve", d58),
    ("D59", "Tell a Decision Story", d59),
    ("D60", "Prove Impact With Numbers", d60),
    ("D61", "OOP Principles Pack", d61),
    ("D62", "SOLID With a Change Story", d62),
    ("D63", "Repository and Unit of Work", d63),
    ("D64", "CQRS Exact Scenario", d64),
    ("D65", "Saga Compensating Actions", d65),
    ("D66", "EF Mapping Code First Fluent API SPs", d66),
    ("D67", "Large Payload and Object References", d67),
    ("D68", "SSO IdentityServer Cognito Awareness", d68),
    ("D69", "Architecture 5-7 Minute Talk", d69),
    ("D70", "Events vs REST and Event Size", d70),
    ("D71", "Global Exceptions and Correlation", d71),
    ("D72", "Five-Question Drill", d72),
]
