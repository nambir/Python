"""Hand-authored .NET visual guides — D25–D48.

Meets visual_guide_requirements.md (Python 3+2+1 chrome). Not the shared stencil.
"""

from __future__ import annotations

from poster_lib import (
    INK,
    MUTED,
    NAVY,
    TBL,
    arrow,
    bullets,
    code_box,
    code_out,
    flow_h,
    flow_v,
    footer3,
    footer_left_code,
    gantt,
    hub,
    levels,
    lock,
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


def d25():
    s = slots()

    def p1(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [("Deliver", "at-least-once"), ("Process", "side effect"), ("Commit", "durable write")],
            "Ack broker",
            "Redeliver / DLQ",
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Control", "When", "Rule"],
            [
                ("Ack", "after durable success", "never ack on crash-risk"),
                ("Retry", "transient only", "limit + backoff"),
                ("DLQ", "poison / exhausted", "alert + replay runbook"),
                ("Idempotency", "every redelivery", "stable message id"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Exactly-once end to end",
            [
                "Apply the side effect on every delivery.",
                "Crash before ack duplicates payment.",
                "Broker promise ≠ business effect.",
            ],
            "Idempotent at-least-once",
            [
                "Deduplicate on message id.",
                "Ack only after durable success.",
                "Redelivery is normal, not a bug.",
            ],
        )

    def p4(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("1  Deliver", "#1d4ed8", "queue / bus hands the message"),
                ("2  Process", "#15803d", "write the business effect"),
                ("3  Crash window", "#c2410c", "commit done, ack not yet"),
                ("4  Redeliver", "#7c3aed", "same id must be a no-op"),
                ("5  DLQ", "#be123c", "poison isolated with a reason"),
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "if (await seen.ExistsAsync(msg.Id))",
                "    { await ack(); return; }",
                "await db.SavePaymentAsync(msg);",
                "await seen.RecordAsync(msg.Id);",
                "await ack();",
            ],
            "redelivery of msg.Id → already processed → ack",
            title="ack after both writes",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Failure path",
            lambda x, y, w, h: table(
                x, y, w, ["Step", "If it fails"],
                [
                    ("Process", "retry transient"),
                    ("Commit", "no ack — redeliver"),
                    ("Ack", "broker may retry"),
                    ("Exhausted", "DLQ + alert"),
                    ("Replay", "idempotent handler"),
                ],
                header_fill="#ffe4e6",
                h=h,
            ),
            [
                "Name retry, DLQ, and idempotency",
                "Ack only after durable success",
                "Poison messages have a replay runbook",
            ],
            ["Assume exactly-once end to end", "Ack before the write commits"],
            [
                ("Ack", "Complete after SaveChanges", "Say when you ack"),
                ("Retry", "Polly on transient", "Transient ≠ validation"),
                ("DLQ", "error queue + alert", "Name the quarantine"),
                ("Idempotent", "processed-id table", "Same id, one effect"),
            ],
            third="Interview",
        )

    return svg(
        "Reliable Message Consumers",
        "Dotnet · D25  ·  At-least-once delivery needs idempotent effects",
        [
            panel(s[0], 1, "Commit then ack", "Redelivery is normal. Ack is a promise you finished.", p1),
            panel(s[1], 2, "Four consumer controls", "Ack, retry, DLQ, and a stable message id.", p2),
            panel(s[2], 3, "The interview trap", "Brokers retry. Your side effect must not.", p3),
            panel(s[3], 4, "The crash window", "Commit without ack is the duplicate payment.", p4),
            panel(s[4], 5, "Idempotent handler", "Seen-id first. Write. Record. Then ack.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Walk delivery → DLQ without stalling.", p6),
        ],
    )


def d26():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Load balancer / ingress", "health + TLS at the edge"),
                ("IIS or reverse proxy", "optional — forwards to Kestrel"),
                ("Kestrel", "the ASP.NET Core web server"),
                ("App + external state", "DB, blob, cache — not local disk"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Piece", "Job", "Scale note"],
            [
                ("Kestrel", "app HTTP", "one process per replica"),
                ("Proxy / IIS", "TLS, edge policy", "not your session store"),
                ("Container", "immutable artifact", "probes + limits"),
                ("Replicas", "stateless copies", "shared state outside"),
            ],
            header_fill="#dcfce7",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "State on local disk",
            [
                "Each replica writes uploads locally.",
                "Scale-out loses files mid-request.",
                "Sticky sessions hide the bug.",
            ],
            "External durable store",
            [
                "Blob / SQL / Redis for shared state.",
                "Any healthy replica can serve.",
                "Scale from measured bottlenecks.",
            ],
        )

    def p4(x, y, w, h):
        return (
            t(x, y + 8, "Draw this topology, then justify replica count", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["LB", "Kestrel × N", "SQL", "Blob"])
            + note(x, y + h - 28, w, "Adding replicas only helps after local state is gone.", kind="star")
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "$ kubectl get pods  # or docker ps / IIS sites",
                "READY  2/2   /health/live  +  /health/ready",
                "HPA  cpu=68%  replicas=4  max=8",
                "# scale signal: latency / queue — not hope",
                "ERR  replica-3  writes to /app/uploads",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say the topology",
            footer_left_code(
                ["# LB → proxy? → Kestrel", "# probes: live vs ready"],
                ["# state: SQL / blob / cache", "# never the container FS"],
            ),
            [
                "Draw LB, Kestrel, dependencies, probes",
                "Name the autoscaling signal",
                "Externalize session and files",
            ],
            ["Store required state on local disk", "Assume more replicas fix SQL"],
            [
                ("Server", "Kestrel", "Name the process"),
                ("Proxy", "IIS / nginx / YARP", "TLS is not the app"),
                ("Health", "IHealthChecks", "Live ≠ ready"),
                ("Scale", "replicas + HPA", "Justify from a bottleneck"),
            ],
            third="Interview",
        )

    return svg(
        "Hosting and Scaling",
        "Dotnet · D26  ·  Replicas help only after state leaves the process",
        [
            panel(s[0], 1, "Where the process sits", "Kestrel is the app server. The rest is topology.", p1),
            panel(s[1], 2, "Four hosting pieces", "Proxy, container, and replicas are not the same job.", p2),
            panel(s[2], 3, "The interview trap", "Local disk is a single-instance design.", p3),
            panel(s[3], 4, "A topology you can draw", "LB, N Kestrels, SQL, blob — then replica count.", p4),
            panel(s[4], 5, "Probes and scale signals", "Ready gates traffic. CPU is one signal, not the story.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Topology first, then the scaling decision.", p6),
        ],
    )


def d27():
    s = slots()

    def p1(x, y, w, h):
        bw = (w - 40) / 3
        boxes = [
            ("Customer", "c.Id", "#dbeafe", "#1e40af"),
            ("Orders", "o.CustomerId", "#dcfce7", "#166534"),
            ("OrderLine", "l.OrderId", "#ffedd5", "#9a3412"),
        ]
        parts = []
        by = y + 8
        bh = h * 0.52
        for i, (name, key, fill, ink) in enumerate(boxes):
            bx = x + i * (bw + 20)
            parts.append(rect(bx, by, bw, bh, fill=fill, stroke=ink, rx=10))
            parts.append(t(bx + bw / 2, by + 28, name, size=14, fill=ink, weight=800, anchor="middle"))
            parts.append(t(bx + bw / 2, by + 52, key, size=12, fill=INK, weight=600, anchor="middle"))
            if i < 2:
                parts.append(arrow(bx + bw + 2, by + bh / 2, bx + bw + 18, by + bh / 2))
        parts.append(note(x, y + h - 26, w, "State the grain before the second JOIN — lines multiply orders.", kind="warn"))
        return "".join(parts)

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Form", "Rows", "Use"],
            [
                ("INNER JOIN", "matches only", "required relationship"),
                ("LEFT JOIN", "keep left", "optional child"),
                ("GROUP BY", "collapse groups", "one row per grain"),
                ("WINDOW", "keep rows", "rank / running total"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "SELECT c.Id, SUM(l.Amount) AS Spend,",
                " RANK() OVER (ORDER BY SUM(l.Amount) DESC)",
                "FROM Customer c",
                "JOIN Orders o ON o.CustomerId = c.Id",
                "JOIN OrderLine l ON l.OrderId = o.Id",
                "GROUP BY c.Id",
            ],
            "grain = one row per customer — sum lines, then rank",
            title="three tables + one window",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Join at the wrong grain",
            [
                "SUM(o.Total) after joining lines.",
                "Order total repeats per line.",
                "Counts look 'almost right'.",
            ],
            "Aggregate at the grain",
            [
                "Sum line amounts (or pre-agg orders).",
                "Then join / window at customer.",
                "Verify row counts after each join.",
            ],
        )

    def p5(x, y, w, h):
        return table(
            x, y, w, ["GROUP BY", "WINDOW"],
            [
                ("Collapses rows", "Keeps each row"),
                ("One total per group", "Rank / lag / running"),
                ("Need a group key", "PARTITION BY optional"),
                ("Report totals", "Compare siblings"),
            ],
            header_fill=TBL[2],
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say the grain",
            footer_left_code(
                ["-- grain: one row / customer", "JOIN orders, then lines"],
                ["-- window: RANK() OVER", "-- not an extra self-join"],
            ),
            [
                "Name grain before the joins",
                "Write a 3-table join live",
                "Window for rank / previous row",
            ],
            ["Join at the wrong grain", "GROUP BY every selected column by habit"],
            [
                ("Join", "LINQ Join / EF Include", "Keys, not 'just join'"),
                ("Group", "GroupBy", "Collapse vs keep rows"),
                ("Window", "raw SQL RANK/LAG", "Name one you used"),
                ("Grain", "Select grain first", "Count rows after JOIN"),
            ],
            third="Interview",
        )

    return svg(
        "SQL Joins and Windows",
        "Dotnet · D27  ·  Grain first, then join, then window without collapsing",
        [
            panel(s[0], 1, "Three tables, two keys", "Customers → orders → lines. Grain is the trap.", p1),
            panel(s[1], 2, "Pick the SQL form", "Join preserves. Group collapses. Window keeps rows.", p2),
            panel(s[2], 3, "A 3-table report", "Sum at the line grain, rank customers.", p3),
            panel(s[3], 4, "The interview trap", "Joining lines multiplies order totals.", p4),
            panel(s[4], 5, "GROUP BY vs WINDOW", "Totals collapse. Rankings keep context.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Grain, join, aggregate, then a window you used.", p6),
        ],
    )


def d28():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Equality first: TenantId = @id", "Range / sort next: CreatedAt", "Optional INCLUDE covering cols"],
            fill="#dbeafe", ink="#1e40af", h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Idea", "Remember", "Cost"],
            [
                ("B-tree", "ordered lookup", "storage + writes"),
                ("Order", "equality then range", "wrong lead = unused"),
                ("Covering", "INCLUDE avoids lookup", "fatter index"),
                ("Write tax", "every INSERT/UPDATE", "drop unused twins"),
            ],
            header_fill="#ffedd5",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Index every filter",
            [
                "ix_a (TenantId)",
                "ix_b (CreatedAt)",
                "Optimizer may pick one.",
            ],
            "One composite for the query",
            [
                "(TenantId, CreatedAt)",
                "Equality + timeline sort.",
                "Confirm in the actual plan.",
            ],
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "CREATE INDEX ix_orders_tenant_time",
                "  ON Orders (TenantId, CreatedAt)",
                "  INCLUDE (Status, Total);",
                "-- WHERE TenantId = @id",
                "-- ORDER BY CreatedAt DESC",
            ],
            "seek TenantId, range CreatedAt, no key lookup",
            title="column order matches the query",
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Read win", "#16a34a", "tenant timeline goes from scan to seek"),
                ("Write tax", "#ea580c", "every insert maintains the key"),
                ("INCLUDE bloat", "#7c3aed", "covering helps reads, fattens writes"),
                ("Twin indexes", "#dc2626", "unused overlap — drop after proof"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Name the query",
            footer_left_code(
                ["# query + predicates + order", "# old plan → new key order"],
                ["# measured duration / reads", "# write cost you accepted"],
            ),
            [
                "Name the query and key order",
                "Explain why the leading column",
                "Quantify write cost",
            ],
            ["Index every filter separately", "Add INCLUDE columns by default"],
            [
                ("Index", "[Index] / SQL CREATE", "Trade reads vs writes"),
                ("Order", "composite key order", "Equality then range"),
                ("Cover", "INCLUDE columns", "Only if lookups hurt"),
                ("Proof", "actual plan", "Before/after reads"),
            ],
            third="Interview",
        )

    return svg(
        "Composite Index Design",
        "Dotnet · D28  ·  Leading column matches equality; order is the design",
        [
            panel(s[0], 1, "Column order is the design", "Equality, then range/sort, then INCLUDE.", p1),
            panel(s[1], 2, "What an index costs", "Faster qualifying reads. Paid on every write.", p2),
            panel(s[2], 3, "The interview trap", "Two single-column indexes are not a composite.", p3),
            panel(s[3], 4, "A real key you can name", "Tenant timeline: (TenantId, CreatedAt).", p4),
            panel(s[4], 5, "Read win vs write tax", "Keep it only if the plan and writes still work.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Query, order, old plan, measured result.", p6),
        ],
    )


def d29():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Operators", "#1d4ed8", "joins, sorts, spills, lookups"),
                ("Estimates", "#7c3aed", "est vs actual row gaps"),
                ("Access", "#ea580c", "scan vs seek is not a moral"),
                ("Measure", "#15803d", "duration, reads, rows, waits"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Look at", "Question", "Trap"],
            [
                ("Actual rows", "what really flowed?", "trusting estimate only"),
                ("Join type", "why nested loops?", "cardinality lie"),
                ("Predicates", "sargable?", "function on the column"),
                ("Before/after", "one change", "changing three things"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Scan means add an index",
            [
                "EXPLAIN says Scan — so index it.",
                "Tiny table: scan is cheaper.",
                "Guessing the key wastes writes.",
            ],
            "Read the actual plan first",
            [
                "Table size, rows consumed.",
                "Estimates vs actuals.",
                "Then one controlled change.",
            ],
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            ["Exact query + real parameters", "Actual plan (not estimated)", "One change: stats / rewrite / index", "Measure duration and logical reads"],
            fill="#dcfce7", ink="#166534", h=h,
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "SET STATISTICS IO, TIME ON;",
                "-- before: Clustered Scan  1.2M rows",
                "-- Nested Loops  est 12  actual 180k",
                "UPDATE STATISTICS Orders;",
                "-- after: Hash Join  210ms  8k reads",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Before / after",
            lambda x, y, w, h: table(
                x, y, w, ["Signal", "Capture"],
                [
                    ("Duration", "client + server"),
                    ("Reads", "logical I/O"),
                    ("Rows", "actual vs est"),
                    ("Waits", "lock / io / cpu"),
                    ("Plan", "screenshot / XML"),
                ],
                header_fill="#f3e8ff",
                h=h,
            ),
            [
                "Walk a real slow query",
                "Show actual vs estimated rows",
                "One change, then remeasure",
            ],
            ["Treat every scan as the problem", "Tune from estimated cost alone"],
            [
                ("Plan", "SSMS live query", "Operators + flow"),
                ("Stats", "UPDATE STATISTICS", "Est vs actual gap"),
                ("EF", "ToQueryString()", "Same SQL you tuned"),
                ("Proof", "before/after ms", "Not a prettier shape"),
            ],
            third="Interview",
        )

    return svg(
        "Reading Query Plans",
        "Dotnet · D29  ·  Actual rows beat a prettier estimated shape",
        [
            panel(s[0], 1, "What to read in a plan", "Operators, estimates, access path, then numbers.", p1),
            panel(s[1], 2, "Four questions", "A scan is not automatically wrong.", p2),
            panel(s[2], 3, "The interview trap", "Do not index because EXPLAIN said Scan.", p3),
            panel(s[3], 4, "Fix loop", "Real params → actual plan → one change → measure.", p4),
            panel(s[4], 5, "A before/after you can tell", "Cardinality lie, then stats, then a hash join.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Duration and reads, not plan cosmetics.", p6),
        ],
    )


def d30():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x + w / 2, y + 18, "Keep the lock window tiny", size=13, fill=NAVY, weight=800, anchor="middle")
            + lock(x + w / 2, y + 48)
            + flow_h(x, y + 92, w, ["BEGIN", "update rows", "COMMIT"])
            + note(x, y + h - 26, w, "No HTTP, no email, no 'just one more call' inside the transaction.", kind="warn")
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Idea", "Protects", "Watch"],
            [
                ("Transaction", "all-or-nothing", "length = lock time"),
                ("Isolation", "what others see", "anomalies vs blocking"),
                ("Lock", "row / page / table", "order + duration"),
                ("Deadlock", "cycle of waits", "victim + retry + order"),
            ],
            header_fill="#fee2e2",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Hold TX across HTTP",
            [
                "BEGIN; update; call API; COMMIT;",
                "Remote slowness holds locks.",
                "Deadlocks and timeouts follow.",
            ],
            "Short TX + outbox",
            [
                "Commit the DB work first.",
                "Coordinate the API via outbox.",
                "Retry the remote separately.",
            ],
        )

    def p4(x, y, w, h):
        hw = (w - 56) / 2
        by = y + 8
        bh = h * 0.42
        return (
            rect(x, by, hw, bh, fill="#fee2e2", stroke="#dc2626", rx=8)
            + t(x + hw / 2, by + 28, "Tx A", size=14, fill="#b91c1c", weight=800, anchor="middle")
            + t(x + hw / 2, by + 52, "holds Row 1, waits Row 2", size=12, fill=INK, weight=500, anchor="middle")
            + rect(x + hw + 56, by, hw, bh, fill="#ffedd5", stroke="#ea580c", rx=8)
            + t(x + hw + 56 + hw / 2, by + 28, "Tx B", size=14, fill="#9a3412", weight=800, anchor="middle")
            + t(x + hw + 56 + hw / 2, by + 52, "holds Row 2, waits Row 1", size=12, fill=INK, weight=500, anchor="middle")
            + arrow(x + hw + 4, by + bh / 2, x + hw + 52, by + bh / 2, "#dc2626")
            + t(x + w / 2, by + bh + 28, "Cycle → engine picks a victim", size=13, fill=NAVY, weight=700, anchor="middle")
            + note(x, y + h - 26, w, "Retry the victim. Then normalize access order and shorten TX.", kind="star")
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "UPDATE Stock SET Qty = Qty - 1",
                " WHERE Sku = @sku AND Qty >= 1;",
                "-- rows==0 → sold out, no oversell",
                "// or: rowversion WHERE Version=@v",
            ],
            "two readers cannot both decrement the last unit",
            title="atomic statement beats two reads",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Name the anomaly",
            footer_left_code(
                ["# lost update / oversell", "# dirty / nonrepeatable?"],
                ["# pick: atomic SQL,", "# rowversion, or isolation"],
            ),
            [
                "Name the concurrency bug first",
                "Keep transactions short",
                "Deadlock: order + retry victim",
            ],
            ["Hold a transaction across remote I/O", "Raise isolation as the first fix"],
            [
                ("TX", "BEGIN / SaveChanges", "Commit or rollback"),
                ("Isolation", "ReadCommitted+", "Name the anomaly"),
                ("Optimistic", "rowversion", "Conflict → retry"),
                ("Deadlock", "1205 victim", "Order + short TX"),
            ],
            third="Interview",
        )

    return svg(
        "Transactions Locks Deadlocks",
        "Dotnet · D30  ·  Name the anomaly, then a short atomic fix",
        [
            panel(s[0], 1, "Locks last as long as the TX", "No remote I/O inside BEGIN…COMMIT.", p1),
            panel(s[1], 2, "Four concurrency words", "Atomicity, isolation, locks, deadlock victim.", p2),
            panel(s[2], 3, "The interview trap", "An HTTP call is not a database operation.", p3),
            panel(s[3], 4, "A deadlock is a wait cycle", "Victim retry is recovery. Order is the fix.", p4),
            panel(s[4], 5, "One atomic write", "Last-unit oversell dies in a single UPDATE.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Anomaly first, then isolation or SQL.", p6),
        ],
    )


def d31():
    s = slots()

    def p1(x, y, w, h):
        hw = (w - 12) / 2
        return (
            rect(x, y, hw, h, fill="#dbeafe", stroke="#2563eb", rx=10)
            + t(x + hw / 2, y + 24, "Write model", size=14, fill="#1e40af", weight=800, anchor="middle")
            + ml(x + 10, y + 52, wrap("Each fact once. Keys and checks own the invariants.", 18, 6), size=13, fill=INK)
            + rect(x + hw + 12, y, hw, h, fill="#ffedd5", stroke="#ea580c", rx=10)
            + t(x + hw + 12 + hw / 2, y + 24, "Read model", size=14, fill="#9a3412", weight=800, anchor="middle")
            + ml(x + hw + 22, y + 52, wrap("Deliberate copies for a measured query — with an owner.", 18, 6), size=13, fill=INK)
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Choice", "Wins", "Pays"],
            [
                ("Normalize", "no update anomalies", "more joins"),
                ("Denormalize", "cheap hot reads", "sync + lag"),
                ("Constraints", "DB enforces rules", "migration care"),
                ("Ownership", "one source of truth", "must name it"),
            ],
            header_fill="#dcfce7",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Copy with no owner",
            [
                "CustomerName in five tables.",
                "No update policy, no lag budget.",
                "Repair is 'we noticed'.",
            ],
            "Document the copy",
            [
                "Source of truth named.",
                "Sync mechanism + lag.",
                "Repair path exists.",
            ],
        )

    def p4(x, y, w, h):
        return (
            t(x, y + 6, "If you denormalize, say this path out loud", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 36, w, ["Source", "Sync job", "Copy", "Repair"])
            + note(x, y + h - 26, w, "Lag budget is a number — not 'eventually'.", kind="star")
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Entities and invariants first",
                "Access patterns and growth",
                "What you denormalized and why",
                "Who updates the duplicate",
            ],
            color="#7c3aed",
            max_w=42,
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Defend the schema",
            footer_left_code(
                ["# fact stored once?", "# copy: who writes it?"],
                ["# lag budget: 30s / 5m", "# FK / unique / check"],
            ),
            [
                "Show write vs read models",
                "Name duplicated facts + owner",
                "Constraints that protect invariants",
            ],
            ["Duplicate without ownership", "Denormalize because joins are 'slow'"],
            [
                ("OLTP", "normalized tables", "Integrity first"),
                ("Read copy", "projection table", "Name the owner"),
                ("FK", "[ForeignKey] / SQL", "Enforce at the DB"),
                ("Lag", "event / job", "A number, not hope"),
            ],
            third="Interview",
        )

    return svg(
        "Schema Design Tradeoffs",
        "Dotnet · D31  ·  Duplicate only with an owner, lag budget, and repair",
        [
            panel(s[0], 1, "Two models, two jobs", "Writes keep facts once. Reads may copy on purpose.", p1),
            panel(s[1], 2, "The tradeoff table", "Joins vs sync. Constraints vs operational cost.", p2),
            panel(s[2], 3, "The interview trap", "A copied name without an owner is drift.", p3),
            panel(s[3], 4, "Sync is a designed path", "Source → job → copy → repair.", p4),
            panel(s[4], 5, "How to defend it", "Invariants, access, copy, owner — in that order.", p5),
            panel(s[5], 6, "Practice & C# comparison", "What you denormalized, and why it was worth it.", p6),
        ],
    )


def d32():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Tool", "Best at", "Breaks when"],
            [
                ("EF / ORM", "ordinary CRUD", "million tracked rows"),
                ("Native SQL", "set-based / hints", "string-built queries"),
                ("Bulk / batch", "volume updates", "unbounded batches"),
                ("SPs", "stable hot paths", "hidden app logic"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Load every row",
            [
                "foreach (var row in db.Rows)",
                "  row.Flag = true;",
                "SaveChanges();  // N entities",
            ],
            "Set-based update",
            [
                "UPDATE … SET Flag=1 WHERE …",
                "or ExecuteUpdate / bulk API",
                "One round trip, no tracker.",
            ],
        )

    def p3(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "await db.Rows.Where(r => r.Open)",
                "  .ExecuteUpdateAsync(s =>",
                "    s.SetProperty(r => r.Flag, true));",
                "-- parameterized, no tracker",
            ],
            "1 statement  vs  1M tracked entities",
            title="bypass when volume is proven",
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Correctness + generated SQL", "Measure round trips and duration", "Bypass only the hot set-based path", "Keep SQL parameterized and tested"],
            fill="#ede9fe", ink="#5b21b6", h=h,
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("ORM default", "#16a34a", "mapping, tracking, maintainable"),
                ("Profiler", "#2563eb", "see the SQL EF actually sent"),
                ("Volume", "#ea580c", "set-based or bounded batches"),
                ("Isolation", "#7c3aed", "keep vendor SQL in one place"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Quantify the bypass",
            footer_left_code(
                ["# before: N round trips", "# allocs + duration"],
                ["# after: 1 set-based SQL", "# extra test / dialect cost"],
            ),
            [
                "Say where you bypassed EF",
                "Numbers: trips, ms, rows",
                "Parameterize and isolate SQL",
            ],
            ["Load every row to update it", "Raw SQL concatenated with values"],
            [
                ("CRUD", "EF SaveChanges", "Stay on the ORM"),
                ("Volume", "ExecuteUpdate", "Set-based on purpose"),
                ("SQL", "FromSql / Dapper", "Parameterized always"),
                ("Bulk", "staging + MERGE", "Bounded batches"),
            ],
            third="Interview",
        )

    return svg(
        "ORM or Native SQL",
        "Dotnet · D32  ·  Bypass the ORM for a measured set-based hot path",
        [
            panel(s[0], 1, "Pick the tool from volume", "EF for ordinary work. SQL when the set is huge.", p1),
            panel(s[1], 2, "The interview trap", "A million tracked entities is not a batch.", p2),
            panel(s[2], 3, "One statement", "ExecuteUpdate (or bulk) — no change tracker.", p3),
            panel(s[3], 4, "Decide with a profiler", "See generated SQL, then isolate the bypass.", p4),
            panel(s[4], 5, "What you still owe", "Parameters, transactions, tests, one folder.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Where you left EF, and what it bought.", p6),
        ],
    )


def d33():
    s = slots()

    def p1(x, y, w, h):
        return hub(x, y, w, h, "Pool", ["borrow", "query", "return", "waiters"])

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Symptom", "Looks like", "Often is"],
            [
                ("Timeout", "DB is down", "pool wait, DB idle"),
                ("Leak", "slow growth", "missing Dispose"),
                ("Long TX", "held handle", "HTTP inside using"),
                ("Too many", "Max Pool Size", "replicas × pool"),
            ],
            header_fill="#ffedd5",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Double Max Pool Size",
            [
                "Timeouts → raise the cap.",
                "DB still has no capacity.",
                "Leaks just fail later.",
            ],
            "Measure hold time first",
            [
                "Open late, close early.",
                "Fix leaks and long TX.",
                "Size from DB + replicas.",
            ],
        )

    def p4(x, y, w, h):
        return gantt(
            x, y, w, h,
            ["query", "HTTP", "query"],
            "Held for the HTTP call",
            "Open late / close early",
            "pool empty",
            "healthy",
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "Timeout expired. The timeout period",
                "elapsed prior to obtaining a connection",
                "from the pool.",
                "-- SQL: sessions sleeping, app waiting",
                "-- fix: dispose, then size, then cap",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Size from capacity",
            lambda x, y, w, h: table(
                x, y, w, ["Input", "Use"],
                [
                    ("DB max sessions", "hard ceiling"),
                    ("Replica count", "multiply pools"),
                    ("Hold time", "concurrency math"),
                    ("Waiters", "exhaustion signal"),
                    ("Leaks", "fix before tuning"),
                ],
                header_fill="#ffe4e6",
                h=h,
            ),
            [
                "Correlate pool waits with DB sessions",
                "Dispose connections every path",
                "Raise pool only if DB has room",
            ],
            ["Increase pool size first", "Hold a connection across HTTP"],
            [
                ("Borrow", "SqlConnection using", "Close returns to pool"),
                ("EF", "DbContext scope", "Short lifetime"),
                ("Cap", "Max Pool Size", "Last knob, not first"),
                ("Math", "replicas × pool", "Must fit the DB"),
            ],
            third="Interview",
        )

    return svg(
        "Connection Pool Sizing",
        "Dotnet · D33  ·  Timeouts while the database looks idle are pool waits",
        [
            panel(s[0], 1, "A pool is a toolbox", "Open/close usually borrow and return.", p1),
            panel(s[1], 2, "Exhaustion disguises itself", "Idle SQL + app timeouts = held handles.", p2),
            panel(s[2], 3, "The interview trap", "Raising Max Pool Size hides leaks.", p3),
            panel(s[3], 4, "Hold time is the real size", "An HTTP call inside using starves waiters.", p4),
            panel(s[4], 5, "The error you must recognize", "Pool timeout is not 'SQL is down'.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Leaks and TX length before the cap.", p6),
        ],
    )


def d34():
    s = slots()

    def p1(x, y, w, h):
        cw = (w - 16) / 3
        cards = [
            ("Document", "aggregate as a unit", "#dbeafe", "#1e40af"),
            ("Key-value", "lookup by id", "#dcfce7", "#166534"),
            ("Columnar", "sparse / scan-heavy", "#ffedd5", "#9a3412"),
        ]
        parts = []
        for i, (title, cap, fill, ink) in enumerate(cards):
            bx = x + i * (cw + 8)
            parts.append(rect(bx, y, cw, h, fill=fill, stroke=ink, rx=10))
            parts.append(t(bx + cw / 2, y + 32, title, size=14, fill=ink, weight=800, anchor="middle"))
            parts.append(ml(bx + 10, y + 64, wrap(cap, 12, 5), size=13, fill=INK))
        return "".join(parts)

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Need", "SQL", "NoSQL"],
            [
                ("Relations + TX", "natural", "painful / limited"),
                ("One-key session", "possible", "KV / cache fit"),
                ("Flexible shape", "migrations", "document fit"),
                ("Consistency", "strong default", "must choose"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Choose by trend",
            [
                "Use NoSQL because it scales.",
                "Fashion is not an access pattern.",
                "Financial posting needs invariants.",
            ],
            "Choose by access pattern",
            [
                "Queries, partition key, volume.",
                "TX boundary + conflict rules.",
                "Ops maturity on the failure path.",
            ],
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Queries and writes first", "Partition key and growth", "Transaction + consistency need", "Ops: backup, query, failure"],
            fill="#dcfce7", ink="#166534", h=h,
        )

    def p5(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Session / cache lookup", "key-value — short-lived value"),
                ("Product catalog aggregate", "document — read/write as a unit"),
                ("Ledger / posting", "relational — constraints + TX"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Start from the query",
            footer_left_code(
                ["# access: key? aggregate?", "# join-heavy? analytic scan?"],
                ["# consistency: strong / eventual", "# who handles conflicts?"],
            ),
            [
                "Justify SQL vs NoSQL from a query",
                "Name partition key and TX needs",
                "Include operational failure cost",
            ],
            ["Choose by trend", "Say 'scale' with no access pattern"],
            [
                ("Document", "Cosmos / Mongo", "Aggregate-shaped"),
                ("KV", "Redis / Dynamo", "Direct key lookup"),
                ("SQL", "EF + constraints", "Relations + TX"),
                ("Consistency", "rowversion / TX", "Say the guarantee"),
            ],
            third="Interview",
        )

    return svg(
        "Choosing NoSQL Models",
        "Dotnet · D34  ·  Access pattern and consistency choose the store",
        [
            panel(s[0], 1, "Three models, three jobs", "Document, key-value, columnar are not synonyms.", p1),
            panel(s[1], 2, "SQL still wins some fights", "Relations and multi-row TX are not fashion.", p2),
            panel(s[2], 3, "The interview trap", "'It must scale' is not a data model.", p3),
            panel(s[3], 4, "Decision order", "Query → key → TX → ops — then the product.", p4),
            panel(s[4], 5, "Worked pair on one system", "Sessions in KV. Money in SQL.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Pattern, partition, consistency, failure.", p6),
        ],
    )


def d35():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 6, "Zero-downtime rename is two releases", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 40, w, ["Expand", "Backfill", "Switch", "Contract"])
            + note(x, y + h - 26, w, "Old code must still run against the expanded schema.", kind="star")
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Rename in one release",
            [
                "ALTER … RENAME COLUMN Name",
                "Deploy app in the same cut.",
                "Rolling deploy breaks mid-way.",
            ],
            "Expand then contract",
            [
                "Add DisplayName, dual-write.",
                "Switch readers, then drop Name.",
                "Each step is reversible.",
            ],
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Discipline", "Rule", "Failure"],
            [
                ("Versioned", "ordered, once", "drifted environments"),
                ("Review", "lock + duration", "prod blocking DDL"),
                ("Expand-contract", "compat first", "big-bang rename"),
                ("Rollback", "forward-fix often", "lossy DOWN script"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p4(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "$ dotnet ef migrations add AddDisplayName",
                "# CI applies to prod-like data",
                "# history table records version",
                "# long backfill ≠ blocking DDL",
                "ERR  rename + app in one release",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "-- release 1: expand",
                "ALTER TABLE Customer",
                "  ADD DisplayName nvarchar(200) NULL;",
                "-- dual-write + backfill",
                "-- release 2: switch reads, then drop",
            ],
            "old app still reads Name until contract",
            title="compatible first",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Rollback story",
            footer_left_code(
                ["# additive: DOWN may work", "# data move: snapshot / fix"],
                ["# never: drop then hope", "# app compat per step"],
            ),
            [
                "Versioned scripts in source control",
                "Expand-contract for live columns",
                "Separate long backfills from DDL",
            ],
            ["Rename a live column in one release", "Trust DOWN scripts for data loss"],
            [
                ("Tool", "EF migrations", "Once, ordered"),
                ("Expand", "add nullable col", "Old code still runs"),
                ("Backfill", "batched UPDATE", "Not in the lock"),
                ("Contract", "drop later", "After old app gone"),
            ],
            third="Interview",
        )

    return svg(
        "Team Schema Migrations",
        "Dotnet · D35  ·  Expand, backfill, switch, contract — never one-cut rename",
        [
            panel(s[0], 1, "Four steps, two releases", "Compatibility is the migration, not the ALTER.", p1),
            panel(s[1], 2, "The interview trap", "A live rename is a rolling-deploy outage.", p2),
            panel(s[2], 3, "Team discipline", "Review locks, duration, and rollback honesty.", p3),
            panel(s[3], 4, "Pipeline evidence", "Prod-like apply + recorded version.", p4),
            panel(s[4], 5, "Expand SQL you can recite", "Add nullable, dual-write, then drop.", p5),
            panel(s[5], 6, "Practice & C# comparison", "A rollback or forward-fix you actually used.", p6),
        ],
    )


def d36():
    s = slots()

    def p1(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Materialize everything",
            [
                "var rows = await q.ToListAsync();",
                "return rows;  // unbounded",
                "First byte waits for last row.",
            ],
            "Bound or stream",
            [
                "Hard page / keyset limit.",
                "IAsyncEnumerable batches.",
                "Cancel when the client leaves.",
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Pattern", "For", "Watch"],
            [
                ("Offset page", "tiny stable lists", "drift + deep cost"),
                ("Keyset / cursor", "deep changing data", "need a stable order"),
                ("Stream batches", "exports", "connection + cancel"),
                ("Archive", "cold history", "retention policy"),
            ],
            header_fill="#dcfce7",
            h=h,
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Keyset: next page starts after last key", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 44, w, ["page 1", "last Id", "WHERE Id > last", "page 2"])
            + note(x, y + h - 26, w, "Offset SKIP 100000 rescans. Cursors do not.", kind="star")
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "await foreach (var row in query",
                "  .AsNoTracking()",
                "  .AsAsyncEnumerable())",
                "{ await write(row, ct); }",
            ],
            "bounded buffer + cancellation — no OOM list",
            title="stream, do not ToList",
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("OOM list", "#dc2626", "unbounded ToList before first byte"),
                ("Slow client", "#ea580c", "buffer grows without backpressure"),
                ("Tracker", "#7c3aed", "AsNoTracking on read-only export"),
                ("Huge file", "#15803d", "async job → object storage URL"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Endpoint contract",
            footer_left_code(
                ["# interactive: keyset + limit", "# order must be deterministic"],
                ["# export: stream or blob job", "# AsNoTracking + cancel"],
            ),
            [
                "Hard page limit on APIs",
                "Keyset for deep result sets",
                "Stream exports with cancellation",
            ],
            ["Materialize an unlimited query", "Offset pagination on a live feed"],
            [
                ("Page", "Skip/Take", "Prefer keyset"),
                ("Stream", "IAsyncEnumerable", "Bound in-flight"),
                ("EF", "AsNoTracking", "Exports are reads"),
                ("Huge", "blob + notify", "Not one HTTP body"),
            ],
            third="Interview",
        )

    return svg(
        "Large Data Result Patterns",
        "Dotnet · D36  ·  Bound the page or stream — never ToList the world",
        [
            panel(s[0], 1, "The interview trap", "An unbounded list is an OOM waiting.", p1),
            panel(s[1], 2, "Four result patterns", "Cursor, stream, limit, archive — pick for the job.", p2),
            panel(s[2], 3, "Keyset pagination", "WHERE Id > last beats SKIP 100000.", p3),
            panel(s[3], 4, "Streaming export", "AsNoTracking + cancel, first byte early.", p4),
            panel(s[4], 5, "How memory actually dies", "Tracker, buffers, and one giant HTTP body.", p5),
            panel(s[5], 6, "Practice & C# comparison", "The endpoint that stopped OOMing.", p6),
        ],
    )


def d37():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Clarify input, constraints, output", "Baseline then a better structure", "State time and space unprompted", "Empty, duplicate, boundary cases"],
            fill="#dbeafe", ink="#1e40af", h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Signal", "Good evidence", "Why"],
            [
                ("Constraints", "n drives the design", "skips needless cleverness"),
                ("Structure", "why a hash map", "access pattern match"),
                ("Complexity", "O(n) time, O(n) space", "cost is explicit"),
                ("Edges", "four tests aloud", "sample is not done"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Silent coding",
            [
                "Starts typing immediately.",
                "Nested loops 'for now'.",
                "Stops when the sample passes.",
            ],
            "Clarify, outline, then code",
            [
                "Restate + constraints first.",
                "Baseline, then optimize.",
                "Edges + complexity out loud.",
            ],
        )

    def p4(x, y, w, h):
        return gantt(
            x, y, w, h,
            ["clarify", "baseline", "code"],
            "Type the whole 30 minutes",
            "Plan then implement",
            "stuck",
            "on time",
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "// membership / counts → HashSet",
                "// Dictionary<TKey, TVal>",
                "if (!seen.Add(x)) return true;",
                "// nested scan is O(n²) — say so",
            ],
            "O(n) time  O(n) space  — say it before they ask",
            title="match the access pattern",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "30-minute loop",
            footer_left_code(
                ["# restate + constraints", "# brute force, then better"],
                ["# code + four edges", "# time and space aloud"],
            ),
            [
                "Restate before typing",
                "Name the structure and why",
                "Complexity without being asked",
            ],
            ["Silent coding from the first second", "Stop when the sample passes"],
            [
                ("Lookup", "Dictionary / HashSet", "Why hashing fits"),
                ("Scan", "array / span", "When O(n) is enough"),
                ("Nested", "avoidable O(n²)", "Call it out"),
                ("Proof", "edge cases", "Empty / dup / bound"),
            ],
            third="Interview",
        )

    return svg(
        "Algorithms Under Time Pressure",
        "Dotnet · D37  ·  Clarify, baseline, code, then complexity unprompted",
        [
            panel(s[0], 1, "Four steps before cleverness", "Constraints pick the structure, not habit.", p1),
            panel(s[1], 2, "What they score", "Access pattern, Big-O, and edges.", p2),
            panel(s[2], 3, "The interview trap", "Typing is not a plan.", p3),
            panel(s[3], 4, "Spend the 30 minutes", "Clarify and baseline still finish on time.", p4),
            panel(s[4], 5, "Hashing is a sentence", "Membership → set. Then say O(n)/O(n).", p5),
            panel(s[5], 6, "Practice & C# comparison", "One medium problem, four tests, complexity.", p6),
        ],
    )


def d38():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Phase", "What to say", "What to do"],
            [
                ("Clarify", "null or empty?", "record assumptions"),
                ("Plan", "dictionary for lookup", "sketch steps"),
                ("Implement", "why this branch", "small increments"),
                ("Verify", "now duplicates", "trace or run tests"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [("Clarify", "inputs"), ("Plan", "algorithm"), ("Code", "increments")],
            "Trace sample",
            "Fix in the open",
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Ten silent minutes",
            [
                "Codes without a word.",
                "Interviewer cannot help.",
                "Hides the bugfix.",
            ],
            "Narrate decisions",
            [
                "Assumptions and tradeoffs.",
                "Not every keystroke.",
                "Show the failing case, then fix.",
            ],
        )

    def p4(x, y, w, h):
        return bullets(
            x, y,
            [
                "May the list be unsorted?",
                "Should duplicates count twice?",
                "What should null return?",
                "I will test empty next",
            ],
            color="#4f46e5",
            max_w=40,
            h=h,
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "> empty  → []",
                "> one item  → [x]",
                "> duplicates  → keep / drop? (ask)",
                "> null  → throw or empty? (ask)",
                "# declare done only after this list",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "The short loop",
            footer_left_code(
                ["# clarify → plan", "# implement → verify"],
                ["# error: show evidence", "# fix, rerun the case"],
            ),
            [
                "Ask focused questions first",
                "Narrate choices, not keys",
                "Test before declaring done",
            ],
            ["Narrate every keystroke", "Hide the defect and keep typing"],
            [
                ("Clarify", "questions first", "Assumptions on paper"),
                ("Plan", "name the structure", "Before the first line"),
                ("Verify", "xUnit / trace", "Edges, then complexity"),
                ("Mistake", "say the evidence", "Fix in the open"),
            ],
            third="Interview",
        )

    return svg(
        "Think Aloud Live Coding",
        "Dotnet · D38  ·  Reasoning is scored — narrate choices, then verify",
        [
            panel(s[0], 1, "Four phases to say aloud", "Clarify, plan, implement, verify.", p1),
            panel(s[1], 2, "The live-coding loop", "If it breaks, show the evidence and rerun.", p2),
            panel(s[2], 3, "The interview trap", "Silence wastes the only person who can help.", p3),
            panel(s[3], 4, "Questions that count", "Null, empty, duplicates — not small talk.", p4),
            panel(s[4], 5, "Done means tested", "Trace the sample and the edges.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Record 25 minutes. End with tests.", p6),
        ],
    )


def d39():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 8, "A hard-bug story is a timeline, not a punchline", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 44, w, ["Reproduce", "Isolate", "Fix", "Prove"])
            + note(x, y + h - 26, w, "The fix is step 3. Interviewers want 1, 2, and 4.", kind="star")
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Step", "Evidence", "Deliverable"],
            [
                ("Reproduce", "same input fails", "minimal case"),
                ("Isolate", "one variable flips it", "confirmed cause"),
                ("Fix", "root cause, not mask", "small diff"),
                ("Prove", "test + prod signal", "it cannot return"),
            ],
            header_fill="#dcfce7",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Fix-only story",
            [
                "Jumps to the code change.",
                "No rejected hypotheses.",
                "No regression test.",
            ],
            "Experiments first",
            [
                "Reliable reproduction.",
                "Two hypotheses you killed.",
                "Test + dashboard proof.",
            ],
        )

    def p4(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("H1  bad data", "#64748b", "ruled out — same payload works elsewhere"),
                ("H2  race", "#ea580c", "ruled out — single-thread still fails"),
                ("H3  stale cache", "#16a34a", "confirmed — bypass cache succeeds"),
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "[Fact]",
                "public async Task StaleConfig_IsEvicted()",
                "{",
                "  // arrange failing payload",
                "  // act update + read",
                "  // assert fresh value",
                "}",
            ],
            "regression test + error-rate back to baseline",
            title="prove prevention, not just the patch",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Tell the timeline",
            footer_left_code(
                ["# first reliable repro", "# H1 H2 killed how"],
                ["# the confirming test", "# prod metric restored"],
            ),
            [
                "Minimal failing case first",
                "Name two rejected hypotheses",
                "Regression test + runtime proof",
            ],
            ["Jump directly to the code change", "Ship a mask without a test"],
            [
                ("Repro", "failing test first", "Same input always"),
                ("Isolate", "one variable", "Cause vs correlation"),
                ("Fix", "small root-cause diff", "Not a shotgun"),
                ("Prove", "xUnit + metric", "Prevention evidence"),
            ],
            third="Interview",
        )

    return svg(
        "Prove the Bug Fix",
        "Dotnet · D39  ·  Reproduce, isolate, fix, then prove it cannot return",
        [
            panel(s[0], 1, "Four words, in order", "The patch is not the story.", p1),
            panel(s[1], 2, "Evidence at each step", "A hypothesis dies by experiment.", p2),
            panel(s[2], 3, "The interview trap", "A clever fix with no isolation is luck.", p3),
            panel(s[3], 4, "Kill hypotheses", "Change one variable. Keep the losers in the story.", p4),
            panel(s[4], 5, "Proof is a test plus a signal", "Green CI and a recovered dashboard.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Five-step timeline, two rejects, one test.", p6),
        ],
    )


def d40():
    s = slots()

    def p1(x, y, w, h):
        return hub(x, y, w, h, "change", ["callers", "tests", "data", "deps"])

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Risk", "Control", "Evidence"],
            [
                ("Unknown behavior", "characterization test", "current contract locked"),
                ("Wide impact", "caller map", "blast radius named"),
                ("Bad release", "flag / canary", "rollback path"),
                ("Rewrite itch", "smallest coherent diff", "reviewable PR"),
            ],
            header_fill="#ffedd5",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Rewrite first",
            [
                "Replace code you do not own.",
                "Behavior was never captured.",
                "Blast radius is 'the module'.",
            ],
            "Characterize, then slice",
            [
                "Tests lock today's behavior.",
                "Smallest coherent change.",
                "Staged rollout + rollback.",
            ],
        )

    def p4(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Trace entry → data → callers", "Add characterization tests", "Smallest coherent diff", "Canary + rollback signal"],
            fill="#dcfce7", ink="#166534", h=h,
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Who owns this path today?",
                "Which tests already pin it?",
                "Which consumers break if we lie?",
                "What metric says roll back?",
            ],
            color="#ea580c",
            max_w=44,
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Safe-change script",
            footer_left_code(
                ["# map: HTTP → SQL → events", "# tests that already exist"],
                ["# characterization gaps", "# flag / canary / metric"],
            ),
            [
                "Trace the request before editing",
                "Lock behavior with tests",
                "Name blast radius and rollback",
            ],
            ["Replace unfamiliar code first", "A large rewrite with no tests"],
            [
                ("Map", "call graph / logs", "Entry to side effects"),
                ("Lock", "characterization", "Behavior before change"),
                ("Diff", "small PR", "Easy to revert"),
                ("Ship", "flag / canary", "Watch one signal"),
            ],
            third="Interview",
        )

    return svg(
        "Change Unfamiliar Code Safely",
        "Dotnet · D40  ·  Tests and blast radius are the map — not a rewrite",
        [
            panel(s[0], 1, "Blast radius first", "Callers, data, deps, tests — then the edit.", p1),
            panel(s[1], 2, "Risk to control", "Unknown behavior is the default risk.", p2),
            panel(s[2], 3, "The interview trap", "Rewriting is not understanding.", p3),
            panel(s[3], 4, "The safe sequence", "Map, lock, smallest diff, staged ship.", p4),
            panel(s[4], 5, "Questions before the first edit", "Owner, tests, consumers, rollback metric.", p5),
            panel(s[5], 6, "Practice & C# comparison", "A change you did not originally write.", p6),
        ],
    )


def d41():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Blocker", "#b91c1c", "auth bypass — fix before merge"),
                ("Design", "#1d4ed8", "sync cross-service call — discuss"),
                ("Suggestion", "#15803d", "rename for the domain"),
                ("Nit", "#64748b", "formatting — do not lead with this"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Type", "Example", "Action"],
            [
                ("Blocker", "authorization hole", "must fix"),
                ("Design", "invert this dependency?", "evidence talk"),
                ("Question", "what happens on retry?", "clarify"),
                ("Nit", "brace style", "optional / tooling"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Style-only review",
            [
                "Comments only on formatting.",
                "Missed the coupled HTTP call.",
                "Author learns nothing durable.",
            ],
            "Design that changed",
            [
                "Sync call coupled two SLAs.",
                "Switched to idempotent event.",
                "Named the operational tradeoff.",
            ],
        )

    def p4(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [("PR intent", "why + tests"), ("Review", "risk first"), ("Decision", "recorded")],
            "Merge",
            "Change design",
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "// before: await pricing.GetAsync(id)",
                "// inside the checkout command",
                "// after: publish OrderPriced",
                "// consumer is idempotent on orderId",
            ],
            "availability no longer couples both services",
            title="a review that changed the design",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "The story to keep",
            footer_left_code(
                ["# before: sync HTTP", "# risk: shared latency"],
                ["# after: event + idempotency", "# what we accepted"],
            ),
            [
                "Label blocker vs suggestion",
                "Lead with correctness and contracts",
                "Keep one design-changing example",
            ],
            ["Style-only review", "Vague 'please refactor this'"],
            [
                ("PR", "small + intent", "Tests in the body"),
                ("Blocker", "must-fix comment", "Severity labeled"),
                ("Design", "coupling / SLA", "Evidence, not taste"),
                ("Respond", "decide + record", "Respect + data"),
            ],
            third="Interview",
        )

    return svg(
        "Reviews That Improve Design",
        "Dotnet · D41  ·  A useful review changes a risk, not a brace",
        [
            panel(s[0], 1, "Severity first", "Blockers before nits — or the author cannot prioritize.", p1),
            panel(s[1], 2, "Four comment types", "Label them so merge rules are obvious.", p2),
            panel(s[2], 3, "The interview trap", "Formatting is not a design review.", p3),
            panel(s[3], 4, "From comment to decision", "Intent, risk, recorded outcome.", p4),
            panel(s[4], 5, "One story that landed", "Sync call became an idempotent event.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Before, after, and the risk you removed.", p6),
        ],
    )


def d42():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Pattern", "Use when", "Safety"],
            [
                ("Extract method", "intent is buried", "unit tests"),
                ("Introduce interface", "dep blocks change", "contract tests"),
                ("Strangler", "large component", "incremental route"),
                ("Feature flag", "behavior cut-over", "instant revert"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Big-bang cleanup",
            [
                "Rewrite mixed with the deadline.",
                "No seam, no reversible slice.",
                "QA cannot isolate the risk.",
            ],
            "Tested seams, small slices",
            [
                "Tie the refactor to delivery.",
                "Tests first, then move structure.",
                "Each slice can ship alone.",
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Deadline-safe order", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 44, w, ["Need", "Tests", "Seam", "Slice"])
            + note(x, y + h - 26, w, "If it cannot ship independently, it is still a rewrite.", kind="warn")
        )

    def p4(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Checkout workflow", "stays stable — tests pin it"),
                ("IPaymentProvider seam", "new vendor without branching core"),
                ("Adapter A → Adapter B", "flagged, one provider at a time"),
            ],
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Name the delivery the refactor unblocked",
                "Characterization tests before moving",
                "Measure defects and latency after",
                "Keep a flag until the old path is cold",
            ],
            color="#7c3aed",
            max_w=46,
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "De-risk the slice",
            footer_left_code(
                ["# extract IPaymentProvider", "# characterization tests"],
                ["# migrate one adapter", "# flag off = old path"],
            ),
            [
                "Tie refactor to a delivery need",
                "Seam + tests before the move",
                "Reversible slices only",
            ],
            ["Mix a rewrite with urgent delivery", "Refactor with no safety net"],
            [
                ("Seam", "interface + adapter", "Core stays testable"),
                ("Tests", "characterization", "Behavior preserved"),
                ("Slice", "one provider", "Ships alone"),
                ("Flag", "IFeatureManager", "Revert without deploy"),
            ],
            third="Interview",
        )

    return svg(
        "Refactor Without Missing Deadlines",
        "Dotnet · D42  ·  Seams and slices — not a rewrite on the critical path",
        [
            panel(s[0], 1, "Patterns with a safety net", "Extract, interface, strangler, flag.", p1),
            panel(s[1], 2, "The interview trap", "A cleanup that cannot ship is a rewrite.", p2),
            panel(s[2], 3, "Order under pressure", "Need → tests → seam → slice.", p3),
            panel(s[3], 4, "Payment-provider story", "Core workflow never branched per vendor.", p4),
            panel(s[4], 5, "How you de-risked it", "Tests, one adapter, a flag, a metric.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Name the refactor and the reverse path.", p6),
        ],
    )


def d43():
    s = slots()

    def p1(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [("Build", "once"), ("Test + scan", "gates"), ("Publish", "immutable")],
            "Promote same SHA",
            "Rollback previous",
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Stage", "Gate", "Failure means"],
            [
                ("Build", "warnings policy", "does not compile clean"),
                ("Test", "required suites", "behavior unproven"),
                ("Contract", "consumer checks", "breaking API"),
                ("Deploy", "health check", "new version unhealthy"),
            ],
            header_fill="#dcfce7",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Rebuild per environment",
            [
                "Staging built again for prod.",
                "You shipped untested bits.",
                "'It worked in QA' is luck.",
            ],
            "One artifact, promoted",
            [
                "Build once, version it.",
                "Same SHA through envs.",
                "Rollback = previous artifact.",
            ],
        )

    def p4(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "PR  restore + build + unit + contract",
                "CI  publish device-api:abc123",
                "QA  deploy abc123  health=pass",
                "PROD promote abc123  (no rebuild)",
                "FAIL contract tests — merge blocked",
            ],
        )

    def p5(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("Must fail the build", "#dc2626", "broken tests, vuln gate, compile"),
                ("Should fail the PR", "#ea580c", "contract drift caught late once"),
                ("Deploy gate", "#1d4ed8", "health / smoke on the same SHA"),
                ("Rollback", "#15803d", "previous artifact, not a hotfix rewrite"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "The gate you added",
            footer_left_code(
                ["# contract tests on PR", "# after a staging surprise"],
                ["# same image abc123", "# QA → prod promote"],
            ),
            [
                "Draw your real pipeline",
                "Name a gate you added or fixed",
                "Promote one immutable artifact",
            ],
            ["Rebuild a different artifact per stage", "Green build with no required tests"],
            [
                ("CI", "dotnet test", "Fail closed"),
                ("Artifact", "container SHA", "Never rebuild"),
                ("Gate", "Pact / contract", "Shift-left breakages"),
                ("CD", "health + rollback", "Previous SHA"),
            ],
            third="Interview",
        )

    return svg(
        "Build Trustworthy Delivery Pipelines",
        "Dotnet · D43  ·  Build once, gate hard, promote the same artifact",
        [
            panel(s[0], 1, "Commit to production path", "Same SHA is the whole point of CD.", p1),
            panel(s[1], 2, "Gates have meaning", "A red build is a quality standard, not a nuisance.", p2),
            panel(s[2], 3, "The interview trap", "A second build is a second untested product.", p3),
            panel(s[3], 4, "A pipeline you can recite", "PR gates, publish SHA, promote, rollback.", p4),
            panel(s[4], 5, "What should go red", "Tests, vulns, contracts, unhealthy deploy.", p5),
            panel(s[5], 6, "Practice & C# comparison", "The gate that stopped a staging surprise.", p6),
        ],
    )


def d44():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.08, y, w * 0.84,
            ["Detect: user impact + severity", "Correlate: metrics, logs, traces, change", "Mitigate: rollback / flag / degrade", "Prevent: fix + detect + runbook"],
            fill="#fee2e2", ink="#9f1239", h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Signal", "Answers", "Example"],
            [
                ("Metric", "how widespread?", "errors by endpoint"),
                ("Log", "what context?", "order + correlation id"),
                ("Trace", "where was time?", "slow pricing span"),
                ("Change", "what shipped?", "release abc123"),
            ],
            header_fill="#ffe4e6",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Debug while it burns",
            [
                "Keeps investigating as impact grows.",
                "Users wait on your curiosity.",
                "No mitigation owner.",
            ],
            "Restore first",
            [
                "Safest reversible action.",
                "Preserve evidence.",
                "Then root cause and prevent.",
            ],
        )

    def p4(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("T+0  alert", "#dc2626", "checkout latency + error rate"),
                ("T+4  trace", "#1d4ed8", "time in downstream pricing"),
                ("T+8  rollback", "#15803d", "service restored"),
                ("T+1d prevent", "#7c3aed", "timeout, fallback, load test"),
            ],
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "error_rate{route=checkout}  0.2% → 8%",
                "trace  span=pricing  p99=2100ms",
                "change  release abc123  4 min ago",
                "action  rollback abc122  # mitigate",
                "follow  timeout + dashboard + test",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Close the incident",
            footer_left_code(
                ["# impact + severity", "# mitigate (rollback)"],
                ["# cause (pricing span)", "# prevent + owner"],
            ),
            [
                "Restore users before the autopsy",
                "Correlate three signals + the change",
                "Leave a prevention metric",
            ],
            ["Debug before mitigation", "Close with no owner or follow-up"],
            [
                ("Detect", "alert / SLO", "User impact first"),
                ("Logs", "ILogger + corr id", "Context per request"),
                ("Trace", "Activity / OTel", "Which hop"),
                ("Mitigate", "rollback / flag", "Reversible first"),
            ],
            third="Interview",
        )

    return svg(
        "Lead Production Incident Recovery",
        "Dotnet · D44  ·  Restore service, then prove the cause and prevent it",
        [
            panel(s[0], 1, "Four incident moves", "Detect, correlate, mitigate, prevent.", p1),
            panel(s[1], 2, "Each signal answers one question", "Metrics spread, logs context, traces the hop.", p2),
            panel(s[2], 3, "The interview trap", "Investigation is not mitigation.", p3),
            panel(s[3], 4, "A timeline you can walk", "Alert → trace → rollback → prevention.", p4),
            panel(s[4], 5, "Evidence, not vibes", "Rate, span, change, action.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Minute-by-minute, then the follow-up.", p6),
        ],
    )


def d45():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Concern", "Decision", "Client impact"],
            [
                ("Retries", "idempotency key", "no duplicate order"),
                ("Growth", "cursor pagination", "stable bounded reads"),
                ("Errors", "ProblemDetails", "typed handling"),
                ("Evolve", "additive first", "old clients keep working"),
            ],
            header_fill="#dbeafe",
            h=h,
        )

    def p2(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Rename a live field",
            [
                "Remove or rename Total.",
                "Change 200 to 201 quietly.",
                "Mobile builds break in the wild.",
            ],
            "Additive or versioned",
            [
                "Add fields; keep old ones.",
                "Version only when semantics change.",
                "Say what would break clients.",
            ],
        )

    def p3(x, y, w, h):
        return (
            t(x, y + 8, "Same key, same order — even on retry", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 44, w, ["Client", "Idempotency-Key", "create", "replay"])
            + note(x, y + h - 26, w, "Replay returns the original result, not a second order.", kind="star")
        )

    def p4(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "return Problem(",
                "  type: \"https://…/conflict\",",
                "  title: \"Duplicate order\",",
                "  status: 409,",
                "  extensions: { [\"traceId\"] = id });",
            ],
            "clients branch on type/status — not on prose",
            title="stable error contract",
        )

    def p5(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Compatible", "add optional fields, new endpoints"),
                ("Versioned break", "new route or media type"),
                ("Never silent", "no type/status/semantic surprise"),
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Defend one API",
            footer_left_code(
                ["# POST /orders + Idempotency-Key", "# cursor, not offset"],
                ["# ProblemDetails + trace id", "# additive fields only"],
            ),
            [
                "Idempotent writes for retries",
                "Cursor pagination for growth",
                "Typed errors + trace ids",
            ],
            ["Rename or remove a response field", "Offset pagination on a live feed"],
            [
                ("Idempotent", "key header + store", "Same effect twice"),
                ("Page", "cursor / next", "Not SKIP N"),
                ("Error", "ProblemDetails", "Machine-readable"),
                ("Version", "add or /v2", "Never silent break"),
            ],
            third="Interview",
        )

    return svg(
        "Design Durable API Contracts",
        "Dotnet · D45  ·  Retries, growth, and errors are designed — not accidents",
        [
            panel(s[0], 1, "Four contract promises", "Idempotency, pagination, errors, evolution.", p1),
            panel(s[1], 2, "The interview trap", "A renamed field is a broken mobile build.", p2),
            panel(s[2], 3, "Idempotent create", "The key is the client’s retry handle.", p3),
            panel(s[3], 4, "Errors clients can switch on", "Type, status, trace — not a sentence.", p4),
            panel(s[4], 5, "How contracts evolve", "Additive first. Version only a real break.", p5),
            panel(s[5], 6, "Practice & C# comparison", "An API you owned, and what would break it.", p6),
        ],
    )


def d46():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("API / controllers", "HTTP in — no business policy"),
                ("Application", "use cases + transaction boundary"),
                ("Domain", "rules and invariants"),
                ("Infrastructure", "EF, HTTP clients, queues"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Boundary", "Owns", "Must not own"],
            [
                ("API", "HTTP mapping", "pricing rules"),
                ("Application", "orchestration", "SQL dialect"),
                ("Domain", "invariants", "DbContext"),
                ("Infra", "adapters", "use-case flow"),
            ],
            header_fill="#ede9fe",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Controller hits SQL",
            [
                "Action queries DbContext.",
                "HTTP and schema change together.",
                "Rules are untestable without SQL.",
            ],
            "Controller → use case",
            [
                "HTTP maps to an application call.",
                "Domain has no EF reference.",
                "Infra implements ports.",
            ],
        )

    def p4(x, y, w, h):
        return hub(x, y, w, h, "domain", ["API", "app", "EF", "queue"])

    def p5(x, y, w, h):
        return (
            t(x, y + 8, "Dependencies point inward", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 44, w, ["Controller", "Use case", "IPort", "EF adapter"])
            + note(x, y + h - 26, w, "A vendor swap stays in the adapter. Tests stay on the domain.", kind="star")
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Justify each box",
            footer_left_code(
                ["# sketch four boxes", "# arrows toward domain"],
                ["# change: swap SQL", "# change: new transport"],
            ),
            [
                "Sketch the service in four boxes",
                "Arrows toward stable policy",
                "A change scenario per boundary",
            ],
            ["Controller queries the database", "Domain project references EF"],
            [
                ("API", "Controller", "Transport only"),
                ("App", "IRequestHandler", "TX boundary"),
                ("Domain", "entity / service", "No DbContext"),
                ("Infra", "repo / client", "Implements ports"),
            ],
            third="Interview",
        )

    return svg(
        "Draw Boundaries That Last",
        "Dotnet · D46  ·  Policy inward, adapters at the edge",
        [
            panel(s[0], 1, "Four layers, four jobs", "HTTP, use case, rules, adapters.", p1),
            panel(s[1], 2, "Ownership table", "A boundary is what it must not own.", p2),
            panel(s[2], 3, "The interview trap", "A controller with a DbContext is not a domain.", p3),
            panel(s[3], 4, "Domain in the middle", "Everything else plugs in.", p4),
            panel(s[4], 5, "Arrow direction", "Controller → use case → port → adapter.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Swap SQL or HTTP without rewriting rules.", p6),
        ],
    )


def d47():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 8, "Any healthy instance can take the next request", size=12, fill=NAVY, weight=800)
            + flow_h(x, y + 44, w, ["LB", "api-1", "api-2", "api-3"])
            + note(x, y + h - 26, w, "Sticky sessions are a scale-out tax. Shared state lives outside.", kind="warn")
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Mechanism", "Benefit", "Limit"],
            [
                ("Stateless handler", "swap instances", "external state latency"),
                ("Load balancer", "spread + health", "bad probes lie"),
                ("Autoscaling", "elastic N", "downstream saturates"),
                ("Idempotent retry", "any replica", "needs an id"),
            ],
            header_fill="#dcfce7",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Just add instances",
            [
                "CPU was fine; SQL was not.",
                "Pools × replicas exhaust DB.",
                "In-memory session still sticky.",
            ],
            "Model the whole path",
            [
                "Externalize session/workflow.",
                "Bound pools and query cost.",
                "Scale on a real saturation signal.",
            ],
        )

    def p4(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("In-memory session", "#dc2626", "affinity — instances are not equal"),
                ("CPU scale-out", "#16a34a", "helps until a shared limit"),
                ("DB connections", "#ea580c", "replicas × pool is the ceiling"),
                ("Idempotent handler", "#1d4ed8", "LB retry can hit another replica"),
            ],
        )

    def p5(x, y, w, h):
        return hub(x, y, w, h, "SQL", ["api-1", "api-2", "api-3", "pool cap"])

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "What blocked scale",
            footer_left_code(
                ["# local: session / files", "# shared: SQL / Redis"],
                ["# signal: CPU vs p99 vs pool", "# first bottleneck named"],
            ),
            [
                "No required local state",
                "Health checks the LB trusts",
                "Name the first shared bottleneck",
            ],
            ["Add instances without checking SQL", "Sticky sessions as the architecture"],
            [
                ("State", "Redis / SQL / blob", "Not in-process"),
                ("LB", "IHealthChecks", "Ready = in rotation"),
                ("Scale", "HPA / replicas", "Demand + saturation"),
                ("Retry", "idempotent action", "Any instance is fine"),
            ],
            third="Interview",
        )

    return svg(
        "Scale Stateless Services Horizontally",
        "Dotnet · D47  ·  Instances are interchangeable — until a shared limit",
        [
            panel(s[0], 1, "Interchangeable replicas", "The load balancer must not care which one.", p1),
            panel(s[1], 2, "Scale-out toolkit", "Stateless, healthy, elastic, idempotent.", p2),
            panel(s[2], 3, "The interview trap", "More Kestrels will not enlarge the database.", p3),
            panel(s[3], 4, "What actually blocks N", "Session memory, then connection pools.", p4),
            panel(s[4], 5, "The shared hub", "Every replica still shares SQL — size that.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Local state, first bottleneck, one signal.", p6),
        ],
    )


def d48():
    s = slots()

    def p1(x, y, w, h):
        return levels(
            x, y, w, h,
            [
                ("Browser / CDN", "#1e3a5f", "public, coarse, far from origin"),
                ("IMemoryCache", "#2563eb", "per process — not shared"),
                ("Distributed (Redis)", "#7c3aed", "shared, network + serialize"),
                ("Origin (SQL / API)", "#15803d", "source of truth"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Policy", "Best fit", "Tradeoff"],
            [
                ("TTL only", "bounded staleness OK", "updates wait for expiry"),
                ("Event eviction", "hot keys must move", "events can drop"),
                ("Cache-aside", "read-heavy", "first request pays miss"),
                ("TTL + event", "recovery + freshness", "two mechanisms"),
            ],
            header_fill="#ffedd5",
            h=h,
        )

    def p3(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Cache forever",
            [
                "No TTL, no invalidation.",
                "Wrong price served for days.",
                "Outage of cache = outage of app.",
            ],
            "Freshness policy",
            [
                "TTL from tolerated staleness.",
                "Events evict hot keys.",
                "Origin fallback when cache dies.",
            ],
        )

    def p4(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [("Lookup", "key"), ("Miss", "single-flight"), ("Load origin", "then set")],
            "Hit: return",
            "Stampede: one loader",
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "if (!_cache.TryGetValue(key, out var v))",
                "{",
                "  v = await origin.GetAsync(id);",
                "  _cache.Set(key, v, ttl: 10m);",
                "}",
                "// update event: Remove(key)",
            ],
            "10m TTL recovers missed events; event evicts hot keys",
            title="cache-aside + TTL + eviction",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Defend one cached value",
            footer_left_code(
                ["# what: product config", "# why: read-heavy, 10m OK"],
                ["# event: Remove on update", "# miss: single-flight"],
            ),
            [
                "Name what was cached and why",
                "TTL number + event eviction",
                "Stampede and cache-down behavior",
            ],
            ["Cache with no expiry or invalidation", "Let a Redis outage take the site down"],
            [
                ("Local", "IMemoryCache", "Per replica"),
                ("Shared", "IDistributedCache", "Redis / NCache"),
                ("TTL", "MemoryCacheEntryOptions", "Staleness budget"),
                ("Stampede", "lock / GetOrCreate", "One origin load"),
            ],
            third="Interview",
        )

    return svg(
        "Cache Without Serving Surprises",
        "Dotnet · D48  ·  Every fast read needs a freshness and failure policy",
        [
            panel(s[0], 1, "Layers of copies", "Browser, memory, Redis, origin — say which.", p1),
            panel(s[1], 2, "TTL vs event vs both", "Missed events are why TTL still exists.", p2),
            panel(s[2], 3, "The interview trap", "A cache without expiry is a second, lying database.", p3),
            panel(s[3], 4, "Miss path", "Single-flight load, then set — no stampede.", p4),
            panel(s[4], 5, "Cache-aside you can recite", "TryGet, load, Set 10m, event Remove.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Value, TTL, invalidation, outage behavior.", p6),
        ],
    )


BUILDERS = [
    ("D25", "Reliable Message Consumers", d25),
    ("D26", "Hosting and Scaling", d26),
    ("D27", "SQL Joins and Windows", d27),
    ("D28", "Composite Index Design", d28),
    ("D29", "Reading Query Plans", d29),
    ("D30", "Transactions Locks Deadlocks", d30),
    ("D31", "Schema Design Tradeoffs", d31),
    ("D32", "ORM or Native SQL", d32),
    ("D33", "Connection Pool Sizing", d33),
    ("D34", "Choosing NoSQL Models", d34),
    ("D35", "Team Schema Migrations", d35),
    ("D36", "Large Data Result Patterns", d36),
    ("D37", "Algorithms Under Time Pressure", d37),
    ("D38", "Think Aloud Live Coding", d38),
    ("D39", "Prove the Bug Fix", d39),
    ("D40", "Change Unfamiliar Code Safely", d40),
    ("D41", "Reviews That Improve Design", d41),
    ("D42", "Refactor Without Missing Deadlines", d42),
    ("D43", "Build Trustworthy Delivery Pipelines", d43),
    ("D44", "Lead Production Incident Recovery", d44),
    ("D45", "Design Durable API Contracts", d45),
    ("D46", "Draw Boundaries That Last", d46),
    ("D47", "Scale Stateless Services Horizontally", d47),
    ("D48", "Cache Without Serving Surprises", d48),
]
