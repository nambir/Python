"""Hand-authored SQL visual guides S01–S14.

Meets visual_guide_requirements.md (Python 3+2+1 chrome). Not the shared stencil.
Panel 6 is always footer3(..., third="T-SQL") — Concept | C# | T-SQL for that slide.
"""

from __future__ import annotations

from pathlib import Path

from poster_lib import (
    INK,
    MUTED,
    arrow,
    bullets,
    code_out,
    flow_h,
    flow_v,
    footer3,
    footer_left_code,
    hub,
    log_bars,
    ml,
    note,
    panel,
    pipe_split,
    slots,
    stack,
    svg,
    t,
    table,
    terminal,
    vs_boxes,
    write_posters,
)


def _join_picture(x, y, w, h):
    """Two labeled tables plus a LEFT JOIN result — not a bullet list."""
    gap = 36
    th = min(92, (h - gap) * 0.46)
    tw = (w - 12) / 2
    left = table(
        x, y, tw, ["Orders.Id", "Cust"],
        [("1", "Alice"), ("2", "Bob")],
        header_fill="#dbeafe", h=th,
    )
    right = table(
        x + tw + 12, y, tw, ["Ship.OrderId", "Status"],
        [("1", "Shipped"), ("2", "(none)")],
        header_fill="#ffedd5", h=th,
    )
    ax1, ax2 = x + tw / 2, x + tw + 12 + tw / 2
    shafts = (
        arrow(ax1, y + th, ax1, y + th + gap)
        + arrow(ax2, y + th, ax2, y + th + gap)
        + t(
            x + w / 2, y + th + 22,
            "ON o.Id = s.OrderId",
            size=11, fill=MUTED, weight=700, anchor="middle",
        )
    )
    result = table(
        x, y + th + gap, w, ["Id", "Cust", "Status"],
        [("1", "Alice", "Shipped"), ("2", "Bob", "NULL  ← LEFT keeps")],
        header_fill="#dcfce7", last_green=True, h=h - th - gap,
    )
    return left + right + shafts + result


def s01():
    s = slots()

    def p1(x, y, w, h):
        return _join_picture(x, y, w, h)

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Kind", "Keeps", "Watch"],
            [
                ("INNER", "matches only", "orphan left row gone"),
                ("LEFT", "every left row", "NULLs on the right"),
                ("1:N child", "parent × children", "SUM double-counts"),
                ("Missing ON", "every combo", "row explosion"),
            ],
            header_fill="#dbeafe", h=h,
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Orders", "left table"),
                ("ON OrderId", "match key"),
                ("Match?", "row exists?"),
            ],
            "INNER drop",
            "LEFT keep NULL",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "WHERE on the right",
            [
                "LEFT JOIN Shipment s ON s.OrderId = o.Id",
                "WHERE s.Status = 'Shipped'",
                "NULLs fail the WHERE",
                "The LEFT JOIN became INNER",
            ],
            "Filter in ON",
            [
                "LEFT JOIN Shipment s",
                "ON s.OrderId = o.Id",
                "AND s.Status = 'Shipped'",
                "Orders with no shipment stay",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "SELECT o.Id, s.ShippedAt",
                "FROM dbo.Orders o",
                "LEFT JOIN dbo.Shipment s",
                "  ON s.OrderId = o.Id",
                " AND s.Status = N'Shipped';",
            ],
            "LEFT JOIN keeps orders without a shipment.",
            title="right-side filter lives in ON",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- trap: WHERE on right of LEFT",
                    "WHERE s.Status = N'Shipped'",
                ],
                [
                    "-- keep the LEFT: filter in ON",
                    "ON s.OrderId = o.Id",
                    "AND s.Status = N'Shipped'",
                ],
            ),
            [
                "INNER when both sides must exist",
                "LEFT when the report must show gaps",
                "If SUM doubled, check 1:N before indexes",
            ],
            [
                "WHERE on the right of a LEFT JOIN",
                "A missing ON clause",
                "Blame the index for multiplied rows",
            ],
            [
                ("INNER", "Join / Include required nav", "INNER JOIN"),
                ("LEFT", "GroupJoin + DefaultIfEmpty", "LEFT JOIN"),
                ("Right filter", "Where after join → inner", "AND in the ON clause"),
                ("1:N SUM", "GroupBy before join", "aggregate, then join"),
            ],
            third="T-SQL",
        )

    return svg(
        "Joins",
        "SQL · S01  ·  INNER vs LEFT — multiplication and the WHERE trap",
        [
            panel(s[0], 1, "Draw the join", "Two tables plus the LEFT result — Bob stays with NULL.", p1),
            panel(s[1], 2, "Which rows survive", "INNER drops gaps. 1:N multiplies the parent.", p2),
            panel(s[2], 3, "How a row is kept", "No match: INNER drops it. LEFT keeps a NULL.", p3),
            panel(s[3], 4, "The interview trap", "WHERE on the right of a LEFT JOIN is an INNER JOIN.", p4),
            panel(s[4], 5, "Say this in T-SQL", "Put the right-table predicate in ON, not WHERE.", p5),
            panel(s[5], 6, "Practice & C# comparison", "EF Where after a left join has the same trap.", p6),
        ],
    )


def s02():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Shape", "Use when", "Not"],
            [
                ("Subquery", "short scalar / IN", "a three-step story"),
                ("CTE", "named steps, two consumers", "a speed button"),
                ("EXISTS", "“has any child”", "you need the child columns"),
                ("Derived", "FROM (SELECT…) t", "clearer than a CTE here"),
            ],
            header_fill="#dbeafe", h=h,
        )

    def p2(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            [
                "WITH LatestBeat AS (…)",
                "GROUP BY DeviceId",
                "LEFT JOIN to Device",
            ],
            h=h,
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Filter", "active devices"),
                ("Name it", "WITH LatestBeat"),
                ("Join", "to Device"),
            ],
            "outer SELECT",
            "2nd consumer",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "IN + DISTINCT",
            [
                "WHERE CustomerId IN (",
                "  SELECT DISTINCT CustomerId",
                "  FROM Orders)",
                "Builds a list; does not stop early",
            ],
            "EXISTS",
            [
                "WHERE EXISTS (SELECT 1",
                "  FROM Orders o",
                "  WHERE o.CustomerId = c.Id)",
                "Stops at the first match",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "WITH LatestBeat AS (",
                "  SELECT DeviceId, MAX(SeenAt) AS SeenAt",
                "  FROM dbo.Heartbeat",
                "  GROUP BY DeviceId)",
                "SELECT d.Id, b.SeenAt",
                "FROM dbo.Device d",
                "LEFT JOIN LatestBeat b ON b.DeviceId = d.Id;",
            ],
            "Named step, then join — not automatically faster.",
            title="CTE is a name, not a hint",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- existence, not a list",
                    "WHERE EXISTS (SELECT 1 FROM Orders o",
                    "  WHERE o.CustomerId = c.Id)",
                ],
                [
                    "-- CTE when there are steps",
                    "WITH LatestBeat AS (...)",
                    "SELECT ... JOIN LatestBeat",
                ],
            ),
            [
                "CTE for two or three named steps",
                "EXISTS when you only need “any row”",
                "Say the optimizer may inline the CTE",
            ],
            [
                "IN (SELECT DISTINCT …) for existence",
                "“CTE is faster” with no plan",
            ],
            [
                ("Named step", "two IQueryable vars", "WITH cte AS (...)"),
                ("Exists", "Any()", "EXISTS (SELECT 1 …)"),
                ("Contains list", "Contains(ids)", "IN (SELECT …)"),
                ("Not magic", "same SQL either way", "CTE ≠ faster"),
            ],
            third="T-SQL",
        )

    return svg(
        "Subquery vs CTE vs EXISTS",
        "SQL · S02  ·  Name the step; EXISTS for “any”; CTE is not a hint",
        [
            panel(s[0], 1, "Pick the shape", "A CTE names a step. EXISTS stops at the first match.", p1),
            panel(s[1], 2, "Read it as steps", "Filter, name the aggregate, then join.", p2),
            panel(s[2], 3, "Why name it", "A CTE can feed the outer query and a second consumer.", p3),
            panel(s[3], 4, "The interview trap", "IN + DISTINCT builds a list. EXISTS can stop early.", p4),
            panel(s[4], 5, "Latest heartbeat", "WITH LatestBeat, then LEFT JOIN — still check the plan.", p5),
            panel(s[5], 6, "Practice & C# comparison", "Any() is EXISTS. A second IQueryable is a CTE.", p6),
        ],
    )


def s03():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Store", "Stats", "Use"],
            [
                ("#temp", "usually yes", "working set, indexes"),
                ("@table var", "often 1-row guess", "a handful of ids"),
                ("##global", "shared / dangerous", "almost never"),
                ("100k in @x", "underestimate", "switch to #temp"),
            ],
            header_fill="#dcfce7", h=h,
        )

    def p2(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("@table var", "#dc2626", "optimizer often assumes 1 row"),
                ("100k stuffed in @x", "#ea580c", "nested loop on a huge set"),
                ("tiny id list", "#2563eb", "table variable is fine"),
                ("#temp + stats", "#16a34a", "next statement gets a real estimate"),
            ],
        )

    def p3(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "> DECLARE @x TABLE (Id int);",
                "> INSERT @x SELECT Id FROM Big;",
                "-- 100,000 rows loaded",
                "-- Estimate: 1 row",
                "-- Join: nested loop disaster",
                "> SELECT Id INTO #x FROM Big WHERE ...;",
                "> CREATE INDEX IX ON #x(Id);",
                "-- next statement sees real stats",
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "100k in a table var",
            [
                "DECLARE @x TABLE (Id int);",
                "INSERT @x SELECT Id FROM Big;",
                "Optimizer may assume 1 row",
                "The join plan is then a guess",
            ],
            "#temp + index",
            [
                "SELECT Id INTO #x FROM Big WHERE ...",
                "CREATE INDEX IX ON #x(Id);",
                "Statistics on the working set",
                "Inspect that in a slow SP",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "SELECT d.Id",
                "INTO #Active",
                "FROM dbo.Device d",
                "WHERE d.IsActive = 1;",
                "CREATE CLUSTERED INDEX IX_Active",
                "  ON #Active(Id);",
            ],
            "#temp + index when the set is not tiny.",
            title="working set in tempdb",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- too big for @table",
                    "DECLARE @x TABLE (Id int);",
                    "INSERT @x SELECT Id FROM Big;",
                ],
                [
                    "-- working set",
                    "SELECT Id INTO #x FROM Big WHERE ...;",
                    "CREATE INDEX IX ON #x(Id);",
                ],
            ),
            [
                "Table var for a handful of ids",
                "#temp when the next join needs stats",
                "Say tempdb + scope in one sentence",
            ],
            [
                "100k rows in a table variable",
                "##global “just in case”",
            ],
            [
                ("Tiny list", "List<int> / HashSet", "@table variable"),
                ("Working set", "no EF analog — FromSql", "#temp + index"),
                ("Stats", "IQueryable sees SQL stats", "#temp has stats; @x often not"),
                ("Scope", "local variable", "#temp batch; @x module"),
            ],
            third="T-SQL",
        )

    return svg(
        "Temp Table vs Table Variable",
        "SQL · S03  ·  #temp gets statistics; @table may assume one row",
        [
            panel(s[0], 1, "Pick the store", "#temp for a working set. @table for a handful of ids.", p1),
            panel(s[1], 2, "What the optimizer sees", "A table variable often looks like one row.", p2),
            panel(s[2], 3, "The 100k session", "Load Big into @x and the join estimate collapses.", p3),
            panel(s[3], 4, "The interview trap", "100k rows in a table variable — switch to #temp.", p4),
            panel(s[4], 5, "Working set in T-SQL", "SELECT INTO #Active, then index the key you join on.", p5),
            panel(s[5], 6, "Practice & C# comparison", "EF has no #temp. FromSql plus a temp table is the move.", p6),
        ],
    )


def s04():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("CREATE PROC", "named batch on SQL Server"),
                ("Parameters", "typed — never concatenate"),
                ("TRY / CATCH", "rollback + THROW"),
                ("SET NOCOUNT ON", "less DONE_IN_PROC noise"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Piece", "Why", "Watch"],
            [
                ("Parameters", "plan reuse", "sniffing — S10"),
                ("TRY/CATCH", "one unit of work", "ROLLBACK then THROW"),
                ("NOCOUNT ON", "client traffic", "some stacks count rows"),
                ("FromSql", "call from EF", "still parameterized"),
            ],
            header_fill="#ede9fe", h=h,
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("C# param", "FromSqlInterpolated"),
                ("SP", "typed @CustomerId"),
                ("NOCOUNT", "no extra chatter"),
            ],
            "result set",
            "CATCH THROW",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "String concat",
            [
                '"EXEC GetOrders " + customerId',
                "Injection + no plan reuse",
                "Types are a string accident",
                "Never from Angular either",
            ],
            "A real parameter",
            [
                "EXEC dbo.GetOrders @CustomerId = @p",
                "FromSqlInterpolated($\"… {id}\")",
                "Typed input, reusable plan",
                "Still watch sniffing (S10)",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "CREATE PROCEDURE dbo.GetOpenOrders",
                "  @CustomerId uniqueidentifier",
                "AS",
                "BEGIN",
                "  SET NOCOUNT ON;",
                "  SELECT o.Id, o.Status FROM dbo.Orders o",
                "  WHERE o.CustomerId = @CustomerId",
                "    AND o.Status = N'Open';",
                "END",
            ],
            "Parameterized SP, NOCOUNT ON.",
            title="set-based work, typed input",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- never",
                    "\"EXEC GetOrders \" + customerId",
                ],
                [
                    "-- from EF",
                    "FromSqlInterpolated(",
                    "  $\"EXEC dbo.GetOpenOrders {id}\")",
                ],
            ),
            [
                "Parameters from C# — always",
                "TRY/CATCH when two writes must pair",
                "NOCOUNT ON unless a client needs counts",
            ],
            [
                "String-concat an EXEC",
                "Hide every SELECT in an SP “because DBA”",
            ],
            [
                ("Call SP", "FromSqlInterpolated", "EXEC dbo.Name @p"),
                ("Nonquery", "ExecuteSqlInterpolated", "EXEC … no result"),
                ("Errors", "SqlException", "THROW in CATCH"),
                ("NOCOUNT", "no C# switch", "SET NOCOUNT ON"),
            ],
            third="T-SQL",
        )

    return svg(
        "Stored Procedures",
        "SQL · S04  ·  Parameters, TRY/CATCH, NOCOUNT, FromSql — never concat",
        [
            panel(s[0], 1, "What an SP is", "A named batch: parameters, body, CATCH, NOCOUNT.", p1),
            panel(s[1], 2, "Four pieces to name", "Typed inputs. Rollback then THROW. FromSql still uses parameters.", p2),
            panel(s[2], 3, "How C# reaches it", "Interpolated FromSql → typed @param → rows or THROW.", p3),
            panel(s[3], 4, "The interview trap", "Concatenating EXEC from C# is injection, not a call.", p4),
            panel(s[4], 5, "A production shape", "GetOpenOrders: NOCOUNT ON and a typed uniqueidentifier.", p5),
            panel(s[5], 6, "Practice & C# comparison", "FromSqlInterpolated is the EF door. Keep it parameterized.", p6),
        ],
    )


def s05():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Kind", "Expands?", "Hot WHERE"],
            [
                ("Scalar UDF", "no — per row", "kills plans"),
                ("Inline TVF", "yes, like a view", "usually safe"),
                ("Multi-stmt TVF", "no — like @table", "bad estimates"),
                ("Computed col", "persisted + index", "prefer this"),
            ],
            header_fill="#ffedd5", h=h,
        )

    def p2(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("scalar UDF in WHERE", "#dc2626", "per row; blocks parallelism"),
                ("multi-statement TVF", "#ea580c", "table-var estimates inside"),
                ("inline TVF", "#16a34a", "optimizer can expand it"),
                ("persisted computed", "#2563eb", "index the normalized column"),
            ],
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            [
                "Find UDF in the predicate",
                "Inline TVF or persist column",
                "Re-check the actual plan",
            ],
            h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Scalar UDF in WHERE",
            [
                "WHERE dbo.Trim(Name) = @name",
                "Index on Name cannot seek",
                "Often serial, row by row",
                "Easy to write, expensive to run",
            ],
            "Sargable / inline",
            [
                "WHERE Name = @name",
                "Or a persisted computed column",
                "Inline TVF expands like a view",
                "Rewrite if the plan shows a UDF",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "CREATE FUNCTION dbo.ActiveDevices()",
                "RETURNS TABLE",
                "AS RETURN",
                "  SELECT Id, Name",
                "  FROM dbo.Device",
                "  WHERE IsActive = 1;",
            ],
            "Inline TVF, not a per-row scalar in WHERE.",
            title="RETURNS TABLE AS RETURN",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- kills a seek",
                    "WHERE dbo.Trim(Name) = @name",
                ],
                [
                    "-- inline TVF",
                    "CREATE FUNCTION dbo.ActiveDevices()",
                    "RETURNS TABLE AS RETURN SELECT ...",
                ],
            ),
            [
                "Keep scalars out of hot predicates",
                "Prefer inline TVF over multi-statement",
                "Persist a normalized column if you filter it",
            ],
            [
                "dbo.fnX(column) in a million-row WHERE",
                "Assume a function is “free encapsulation”",
            ],
            [
                ("Predicate", "Where(x => x.Name == n)", "WHERE Name = @n"),
                ("Client eval", "AsEnumerable then Where", "scalar UDF per row"),
                ("TVF", "FromSql to the function", "inline RETURNS TABLE"),
                ("Computed", "HasComputedColumnSql", "persisted + indexed"),
            ],
            third="T-SQL",
        )

    return svg(
        "Functions",
        "SQL · S05  ·  Scalar UDF in WHERE kills; inline TVF can expand",
        [
            panel(s[0], 1, "Four function shapes", "Scalar in a filter is the expensive one.", p1),
            panel(s[1], 2, "Cost you will see", "Per-row UDF blocks parallelism. Inline TVF expands.", p2),
            panel(s[2], 3, "Rewrite path", "Find it in the predicate, inline or persist, re-measure.", p3),
            panel(s[3], 4, "The interview trap", "dbo.Trim(Name) in WHERE is not sargable.", p4),
            panel(s[4], 5, "Inline TVF", "RETURNS TABLE AS RETURN — optimizer can expand it.", p5),
            panel(s[5], 6, "Practice & C# comparison", "LINQ on IQueryable stays sargable. AsEnumerable does not.", p6),
        ],
    )


def s06():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Clustered", "the table order — one per table"),
                ("Nonclustered", "separate B-tree + pointer"),
                ("Lookups", "key → clustered row unless covered"),
                ("Writes", "every index is maintained"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Word", "Means", "Often"],
            [
                ("Clustered", "storage order", "the PK, not always"),
                ("Nonclustered", "extra B-tree", "CustomerId + INCLUDE"),
                ("PK", "uniqueness", "clustered by default"),
                ("Hurt", "write cost", "wide VARCHAR keys"),
            ],
            header_fill="#e0e7ff", h=h,
        )

    def p3(x, y, w, h):
        return hub(
            x, y, w, h, "PK ≠ clustered",
            ["Uniqueness", "Storage order", "Often same key", "Say what yours is"],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Index every VARCHAR",
            [
                "CREATE INDEX IX_Notes ON T(Notes);",
                "Low selectivity, high write cost",
                "Duplicates of the clustered key",
                "Long text is a full-text problem",
            ],
            "Selective + covering",
            [
                "Index keys you filter and join",
                "INCLUDE Status, Total to cover",
                "PK = uniqueness, not “the index”",
                "Watch insert cost on every extra tree",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "ALTER TABLE dbo.Orders ADD CONSTRAINT",
                "  PK_Orders PRIMARY KEY CLUSTERED (Id);",
                "CREATE NONCLUSTERED INDEX IX_Orders_Customer",
                "  ON dbo.Orders(CustomerId)",
                "  INCLUDE (Status, Total);",
            ],
            "PK ≠ clustered always — say what yours is.",
            title="covering lookup by customer",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- uniqueness, often clustered",
                    "PRIMARY KEY CLUSTERED (Id)",
                ],
                [
                    "-- the list-page index",
                    "ON dbo.Orders(CustomerId)",
                    "INCLUDE (Status, Total)",
                ],
            ),
            [
                "Name the clustered key first",
                "INCLUDE to avoid lookups",
                "Do not index every column",
            ],
            [
                "Index every VARCHAR",
                "“PK is clustered” without checking",
            ],
            [
                ("Clustered", "PK convention in EF", "one clustered index"),
                ("Extra index", "HasIndex + Include", "NONCLUSTERED + INCLUDE"),
                ("PK", "HasKey", "PRIMARY KEY — uniqueness"),
                ("Write cost", "SaveChanges slower", "every index maintained"),
            ],
            third="T-SQL",
        )

    return svg(
        "Indexes: Clustered, Nonclustered, PK",
        "SQL · S06  ·  Clustered is the table; PK is uniqueness; they often coincide",
        [
            panel(s[0], 1, "What the trees are", "One clustered order. Nonclustered is a separate B-tree.", p1),
            panel(s[1], 2, "Three words, three jobs", "PK ≠ clustered. INCLUDE covers so you skip lookups.", p2),
            panel(s[2], 3, "Say it in the interview", "Uniqueness vs storage order — name what your DB uses.", p3),
            panel(s[3], 4, "The interview trap", "An index on Notes is write cost, not a list-page win.", p4),
            panel(s[4], 5, "A covering pattern", "PK on Id, nonclustered CustomerId INCLUDE Status, Total.", p5),
            panel(s[5], 6, "Practice & C# comparison", "HasIndex().Include() is CREATE INDEX … INCLUDE.", p6),
        ],
    )


def s07():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Base tables", "Device + Customer"),
                ("VIEW SELECT", "stored query, stable shape"),
                ("API / Angular", "DTO contract"),
                ("Plan still matters", "not a free index"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Kind", "Gives you", "Cost"],
            [
                ("View", "stable contract", "same plan as the SELECT"),
                ("Indexed view", "persisted aggregate", "extra writes; strict rules"),
                ("GRANT SELECT", "hide base tables", "not a performance knob"),
                ("Re-join trap", "join the view + bases", "double the same joins"),
            ],
            header_fill="#fef9c3", h=h,
        )

    def p3(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("Device", "base table"),
                ("JOIN Cust", "hidden in view"),
                ("vwDeviceList", "stable shape"),
            ],
            "API DTO",
            "Angular screen",
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Views are faster",
            [
                "Put everything in a view",
                "“for performance”",
                "No plan, no index story",
                "SELECT * FROM vw JOIN bases again",
            ],
            "View = contract",
            [
                "Stable shape when tables move",
                "Speed comes from the plan",
                "Indexed view only for a hot aggregate",
                "Do not re-join the same tables",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "CREATE VIEW dbo.vwDeviceList",
                "AS",
                "SELECT d.Id, d.Name, c.Name AS Customer",
                "FROM dbo.Device d",
                "JOIN dbo.Customer c",
                "  ON c.Id = d.CustomerId;",
            ],
            "Stable shape, not a free index.",
            title="contract for the device list",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- contract, not a hint",
                    "CREATE VIEW dbo.vwDeviceList AS",
                    "SELECT d.Id, d.Name, c.Name AS Customer ...",
                ],
                [
                    "-- trap",
                    "SELECT * FROM vwDeviceList v",
                    "JOIN dbo.Device d ON d.Id = v.Id",
                ],
            ),
            [
                "Call the view a contract for a screen",
                "Prove speed with a plan, not the word view",
                "Indexed view only when the aggregate is constant",
            ],
            [
                "“Views are always faster”",
                "Re-join the view to the same bases",
            ],
            [
                ("Contract", "DTO / projection", "VIEW SELECT list"),
                ("Hide joins", "IQueryable Select", "view hides Device+Cust"),
                ("Materialize", "ToList cache", "indexed view"),
                ("Speed", "the SQL plan", "not CREATE VIEW"),
            ],
            third="T-SQL",
        )

    return svg(
        "Views",
        "SQL · S07  ·  A view is a contract — not a free performance button",
        [
            panel(s[0], 1, "What sits under the screen", "Tables → view → DTO. The plan is still the SELECT.", p1),
            panel(s[1], 2, "View vs indexed view", "Indexed views persist work. Ordinary views do not.", p2),
            panel(s[2], 3, "How the contract travels", "Joins stay in the view. API and Angular see one shape.", p3),
            panel(s[3], 4, "The interview trap", "A view is not faster until the plan says so.", p4),
            panel(s[4], 5, "Device list DTO", "vwDeviceList so the API does not copy five joins.", p5),
            panel(s[5], 6, "Practice & C# comparison", "A DTO projection is the C# cousin of a view contract.", p6),
        ],
    )


def s08():
    s = slots()

    def p1(x, y, w, h):
        return (
            t(x, y + 10, "Inside one SQL Server database", size=11, fill=MUTED, weight=700)
            + flow_h(x, y + 28, w, ["BEGIN TRAN", "Wallet", "Outbox", "COMMIT"])
            + note(x, y + 92, w, "CATCH → ROLLBACK both, then THROW. Never COMMIT in CATCH.", kind="ok")
            + note(x, y + 122, w, "Payment service’s database is a saga — not this TRAN.", kind="warn")
            + ml(
                x, y + 158,
                ["EF SaveChanges is one transaction by default.", "ITransaction when you need an explicit boundary."],
                size=13, fill=INK, weight=500,
            )
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Move", "Does", "Boundary"],
            [
                ("COMMIT", "durable + visible", "this database"),
                ("ROLLBACK", "undo the unit", "CATCH after failure"),
                ("SaveChanges", "one TRAN", "one DbContext"),
                ("Two services", "cannot share", "saga / outbox (D65)"),
            ],
            header_fill="#dcfce7", h=h,
        )

    def p3(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Wallet debit", "must succeed"),
                ("Outbox insert", "same unit"),
                ("COMMIT both", "or ROLLBACK both"),
                ("Other service DB", "not in this TRAN"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "CATCH then COMMIT",
            [
                "BEGIN TRAN; ...",
                "CATCH; COMMIT;",
                "Failed write still lands",
                "The unit of work is a lie",
            ],
            "CATCH ROLLBACK THROW",
            [
                "BEGIN TRAN; BEGIN TRY",
                "  … COMMIT;",
                "CATCH ROLLBACK; THROW;",
                "All-or-nothing, error bubbles up",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "BEGIN TRAN;",
                "BEGIN TRY",
                "  UPDATE dbo.Wallet SET Balance -= @amt",
                "    WHERE Id = @id;",
                "  INSERT dbo.Outbox (WalletId, Type)",
                "    VALUES (@id, N'Debited');",
                "  COMMIT;",
                "END TRY",
                "BEGIN CATCH",
                "  ROLLBACK; THROW;",
                "END CATCH",
            ],
            "Two writes, one commit or full rollback.",
            title="wallet + outbox",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- unit of work",
                    "BEGIN TRAN; BEGIN TRY",
                    "  UPDATE ...; INSERT ...; COMMIT;",
                ],
                [
                    "-- failure",
                    "BEGIN CATCH",
                    "  ROLLBACK; THROW;",
                    "END CATCH",
                ],
            ),
            [
                "Name two writes that must pair",
                "ROLLBACK in CATCH, then THROW",
                "Say a SQL TRAN cannot span services",
            ],
            [
                "COMMIT inside CATCH",
                "One ROLLBACK “undoes payment and inventory”",
            ],
            [
                ("One DB", "SaveChanges / ITransaction", "BEGIN TRAN … COMMIT"),
                ("Two writes", "same context.SaveChanges", "Wallet + Outbox"),
                ("Failure", "catch, transaction.Rollback", "CATCH ROLLBACK THROW"),
                ("Two services", "saga / outbox pattern", "cannot share this TRAN"),
            ],
            third="T-SQL",
        )

    return svg(
        "Transactions: Commit and Rollback",
        "SQL · S08  ·  All-or-nothing in one database — not across microservices",
        [
            panel(s[0], 1, "The happy path", "BEGIN TRAN, two writes, COMMIT — CATCH rolls both back.", p1),
            panel(s[1], 2, "Where the boundary is", "SaveChanges is one TRAN. Another service is a saga.", p2),
            panel(s[2], 3, "One unit of work", "Wallet and outbox commit together or not at all.", p3),
            panel(s[3], 4, "The interview trap", "COMMIT in CATCH keeps the failed unit.", p4),
            panel(s[4], 5, "Wallet + outbox", "Two writes, one COMMIT, or ROLLBACK and THROW.", p5),
            panel(s[5], 6, "Practice & C# comparison", "ITransaction maps to BEGIN TRAN. A saga does not.", p6),
        ],
    )


def s09():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.04, y, w * 0.92,
            [
                "1 Reproduce real params",
                "2 Actual plan + IO",
                "3 Waits / blocking",
                "4 One change",
                "5 Measure reads / CPU",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("reproduce", "#1e3a5f", "same params, similar volume"),
                ("actual plan", "#1d4ed8", "scans, lookups, spills, rows"),
                ("waits / blocking", "#ea580c", "sp_whoisactive before guessing"),
                ("one change + measure", "#16a34a", "duration, CPU, logical reads"),
            ],
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Look at", "Clue", "Not an order"],
            [
                ("Actual plan", "scan vs seek", "estimated-only plan"),
                ("Missing index", "hypothesis", "create all of them"),
                ("Stats", "stale rows", "skip UPDATE STATISTICS"),
                ("Sniffing", "3 vs 3M rows", "RECOMPILE first"),
            ],
            header_fill="#ffedd5", h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Add an index first",
            [
                "CREATE INDEX on every WHERE",
                "No params, no actual plan",
                "No before/after reads",
                "Ship a guess",
            ],
            "Playbook",
            [
                "Reproduce → actual plan",
                "Waits, then one change",
                "Measure logical reads",
                "An index is a hypothesis",
            ],
        )

    def p5(x, y, w, h):
        return terminal(
            x, y, w, h,
            [
                "> SET STATISTICS IO, TIME ON;",
                "> EXEC dbo.GetOpenOrders @CustomerId = '…';",
                "Table 'Orders'. Scan count 1, logical reads 48210",
                "CPU time = 940 ms, elapsed time = 2100 ms",
                "> -- after one change — same params",
                "Table 'Orders'. Scan count 1, logical reads 128",
                "CPU time = 15 ms, elapsed time = 22 ms",
            ],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- say this order",
                    "-- 1 reproduce with real params",
                    "-- 2 actual plan + STATISTICS IO, TIME",
                    "-- 3 blocking / deadlocks",
                ],
                [
                    "-- 4 stats and sargable predicates",
                    "-- 5 one index or rewrite",
                    "-- 6 compare logical reads",
                ],
            ),
            [
                "Start with the actual plan and the parameters",
                "Treat missing-index hints as clues",
                "Prove the change with before/after reads",
            ],
            [
                "Add an index immediately",
                "Ship without measuring",
            ],
            [
                ("Reproduce", "same payload in QA", "same @params on a copy"),
                ("Plan", "MiniProfiler / ToQueryString", "actual execution plan"),
                ("IO", "log duration", "SET STATISTICS IO, TIME"),
                ("Blocking", "whois / Insights", "sp_whoisactive"),
            ],
            third="T-SQL",
        )

    return svg(
        "Slow Stored Procedure Playbook",
        "SQL · S09  ·  Reproduce → actual plan → waits → one change → measure",
        [
            panel(s[0], 1, "Say this order", "Five steps. An index is step four, not step one.", p1),
            panel(s[1], 2, "What you collect", "Plan, waits, then one change with numbers after.", p2),
            panel(s[2], 3, "Clues, not orders", "Missing-index hints are hypotheses. Sniffing is S10.", p3),
            panel(s[3], 4, "The interview trap", "Do not start with CREATE INDEX on every column.", p4),
            panel(s[4], 5, "Measure like this", "STATISTICS IO/TIME before and after the same params.", p5),
            panel(s[5], 6, "Practice & C# comparison", "MiniProfiler is not an actual plan. Still measure both.", p6),
        ],
    )


def s10():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Shape", "Means", "When"],
            [
                ("Seek", "jump to a key", "selective + sargable"),
                ("Scan", "read a lot", "small table or most rows"),
                ("Lookup", "NC → clustered", "INCLUDE to cover"),
                ("Sniffing", "first @p cached", "3 rows vs 3 million"),
            ],
            header_fill="#dbeafe", h=h,
        )

    def p2(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("First call", "3-row customer"),
                ("Cache plan", "nested loops"),
                ("Reuse", "next @CustomerId"),
            ],
            "still 3 rows",
            "3M row scan",
        )

    def p3(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("seek", "#16a34a", "selective + sargable key"),
                ("scan", "#ea580c", "OK small; pain on large"),
                ("lookup", "#2563eb", "INCLUDE columns to cover"),
                ("sniffing", "#dc2626", "3-row plan reused for 3M"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Always RECOMPILE",
            [
                "OPTION (RECOMPILE) on every call",
                "CPU tax on a busy SP",
                "Hides the real sniffing story",
                "A slogan, not a diagnosis",
            ],
            "Prove sniffing first",
            [
                "Estimated vs actual rows",
                "Fast customer vs slow customer",
                "Then OPTIMIZE FOR / local var",
                "RECOMPILE as a last resort",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "-- sargable — can seek",
                "WHERE CreatedAt >= @from",
                "  AND CreatedAt < @to",
                "-- not sargable — often a scan",
                "WHERE YEAR(CreatedAt) = 2026",
            ],
            "Sargable range; sniffing is a cached-plan story.",
            title="do not wrap the indexed column",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- sargable",
                    "WHERE CreatedAt >= @from",
                    "  AND CreatedAt < @to",
                ],
                [
                    "-- not sargable",
                    "WHERE YEAR(CreatedAt) = 2026",
                ],
            ),
            [
                "Seek when the predicate is selective and bare",
                "Same SP fast/slow by customer → sniffing or skew",
                "INCLUDE to kill lookups",
            ],
            [
                "OPTION (RECOMPILE) on every call",
                "YEAR(column) on an indexed date",
            ],
            [
                ("Seek", "Where on indexed key", "sargable predicate"),
                ("Scan", "client filter / AsEnumerable", "YEAR(CreatedAt)"),
                ("Cover", "Select only indexed cols", "INCLUDE (Status)"),
                ("Sniff", "same compiled query", "cached plan from first @p"),
            ],
            third="T-SQL",
        )

    return svg(
        "Scans, Seeks, and Parameter Sniffing",
        "SQL · S10  ·  Sargable seeks; sniffing is a cached plan for the wrong @p",
        [
            panel(s[0], 1, "Four words to keep straight", "Seek jumps. Scan reads. Lookup follows. Sniffing reuses.", p1),
            panel(s[1], 2, "How sniffing happens", "A 3-row plan is reused for the 3-million-row customer.", p2),
            panel(s[2], 3, "What hurts", "A scan on a large table. A sniffed nested loop on 3M rows.", p3),
            panel(s[3], 4, "The interview trap", "RECOMPILE everywhere is not a sniffing strategy.", p4),
            panel(s[4], 5, "Keep it sargable", "Range on CreatedAt can seek. YEAR(CreatedAt) often cannot.", p5),
            panel(s[5], 6, "Practice & C# comparison", "IQueryable keeps the column bare. AsEnumerable does not.", p6),
        ],
    )


def s11():
    s = slots()

    def p1(x, y, w, h):
        return table(
            x, y, w, ["Level", "Readers", "Use"],
            [
                ("READ COMMITTED", "can block", "default OLTP start"),
                ("RCSI / SNAPSHOT", "row versions", "less reader/writer block"),
                ("SERIALIZABLE", "range locks", "rare for APIs"),
                ("NOLOCK", "dirty / skip / dup", "not a strategy"),
            ],
            header_fill="#e0e7ff", h=h,
        )

    def p2(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("READ COMMITTED", "#2563eb", "default; writers can still block"),
                ("RCSI / SNAPSHOT", "#16a34a", "readers skip writer locks"),
                ("SERIALIZABLE", "#ea580c", "range locks; rare for OLTP"),
                ("NOLOCK", "#dc2626", "skip or duplicate rows"),
            ],
        )

    def p3(x, y, w, h):
        return hub(
            x, y, w, h, "Deadlock",
            ["SP A Wallet", "SP B Outbox", "Victim chosen", "Fix lock order"],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "NOLOCK everywhere",
            [
                "WITH (NOLOCK) on every SELECT",
                "Can skip or duplicate rows",
                "Dirty reads look like speed",
                "Not a performance strategy",
            ],
            "A real isolation choice",
            [
                "Short debit: READ COMMITTED",
                "Long report: SNAPSHOT / RCSI",
                "Keep transactions short",
                "Consistent access order + seeks",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "SET TRANSACTION ISOLATION LEVEL",
                "  READ COMMITTED;",
                "BEGIN TRAN;",
                "UPDATE dbo.Wallet",
                "  SET Balance -= @amt",
                "  WHERE Id = @id;",
                "COMMIT;",
            ],
            "Short transaction; NOLOCK is not a performance strategy.",
            title="wallet debit stays brief",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- short OLTP",
                    "SET TRANSACTION ISOLATION LEVEL",
                    "  READ COMMITTED;",
                ],
                [
                    "-- report without blocking writers",
                    "SET TRANSACTION ISOLATION LEVEL",
                    "  SNAPSHOT;",
                ],
            ),
            [
                "Pick isolation for debit vs report",
                "Deadlock: graph, then lock order, then length",
                "RCSI costs version store in tempdb",
            ],
            [
                "NOLOCK on every SELECT",
                "SERIALIZABLE for a busy API by default",
            ],
            [
                ("Default", "ReadCommitted", "READ COMMITTED"),
                ("Snapshot", "Snapshot / RCSI", "row versions in tempdb"),
                ("NOLOCK", "no EF equivalent you want", "dirty / skip / dup"),
                ("Deadlock", "retry / short scope", "victim + consistent order"),
            ],
            third="T-SQL",
        )

    return svg(
        "Isolation Levels and Deadlocks",
        "SQL · S11  ·  Isolation is a choice; NOLOCK is not a strategy",
        [
            panel(s[0], 1, "What you see under load", "Higher isolation, fewer anomalies, more blocking.", p1),
            panel(s[1], 2, "Cost of each choice", "RCSI helps readers. NOLOCK can skip or duplicate.", p2),
            panel(s[2], 3, "A deadlock is a cycle", "Capture the graph. Same lock order. Keep TRAN short.", p3),
            panel(s[3], 4, "The interview trap", "WITH (NOLOCK) is not how you make reports fast.", p4),
            panel(s[4], 5, "Wallet stays short", "READ COMMITTED, one UPDATE, COMMIT.", p5),
            panel(s[5], 6, "Practice & C# comparison", "IsolationLevel on the transaction. There is no good NOLOCK API.", p6),
        ],
    )


def s12():
    s = slots()

    def p1(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            [
                "Add Amount NULL",
                "Backfill from Amt",
                "App reads Amount",
                "Later DROP Amt",
            ],
            h=h,
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Change", "Safer?", "Rollback"],
            [
                ("Add nullable col", "yes — expand", "DROP COLUMN"),
                ("Rename in place", "no — breaks app", "another rename"),
                ("Data UPDATE", "copy first", "reverse UPDATE"),
                ("DELETE rows", "keep a copy", "restore from copy"),
            ],
            header_fill="#dcfce7", h=h,
        )

    def p3(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("DEV", "script + app together"),
                ("QA", "run the rollback once"),
                ("Prod expand", "nullable column + backfill"),
                ("Later contract", "drop the old column"),
            ],
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "Rename in one shot",
            [
                "EXEC sp_rename 'Orders.Amt', 'Amount'",
                "App and DB change together",
                "No dual-read window",
                "Rollback is another breaking rename",
            ],
            "Expand / contract",
            [
                "Add Amount, backfill Amt",
                "Switch the app, then drop Amt",
                "Rollback = reverse script + old package",
                "Additive first, delete later",
            ],
        )

    def p5(x, y, w, h):
        return code_out(
            x, y, w, h,
            [
                "-- expand",
                "ALTER TABLE dbo.Orders",
                "  ADD Amount decimal(18,2) NULL;",
                "UPDATE dbo.Orders",
                "  SET Amount = Amt WHERE Amount IS NULL;",
                "-- later contract:",
                "-- ALTER TABLE dbo.Orders DROP COLUMN Amt;",
            ],
            "Additive first; rollback script stored with the migration.",
            title="Amount beside Amt",
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- expand",
                    "ALTER TABLE dbo.Orders",
                    "  ADD Amount decimal(18,2) NULL;",
                ],
                [
                    "-- rollback artifact",
                    "-- DROP COLUMN Amount;",
                    "-- restore previous app package",
                ],
            ),
            [
                "Add, dual-read, switch app, then drop",
                "Keep a reverse script with the migration",
                "Back up before a one-way DELETE",
            ],
            [
                "sp_rename in the same release as the app",
                "A rollback plan that is “restore the VM” only",
            ],
            [
                ("Add column", "Add-migration nullable", "ALTER TABLE ADD"),
                ("Rename", "avoid in one deploy", "expand/contract, not sp_rename"),
                ("Data fix", "SQL script in CI", "reversible UPDATE"),
                ("Rollback", "previous package", "reverse script + old app"),
            ],
            third="T-SQL",
        )

    return svg(
        "DB Deploy and Rollback",
        "SQL · S12  ·  Expand/contract — additive first; rollback is a first-class script",
        [
            panel(s[0], 1, "Four releases, not one", "Add Amount, backfill, switch the app, drop Amt later.", p1),
            panel(s[1], 2, "Which change is reversible", "A nullable add rolls back. A live rename does not.", p2),
            panel(s[2], 3, "Same files through Prod", "DEV → QA → Prod with the app. Practice the rollback in QA.", p3),
            panel(s[3], 4, "The interview trap", "sp_rename of a live column in one shot breaks the app.", p4),
            panel(s[4], 5, "The expand script", "ADD Amount NULL, backfill from Amt, drop Amt next release.", p5),
            panel(s[5], 6, "Practice & C# comparison", "An EF migration is still expand/contract, not a sneaky rename.", p6),
        ],
    )


def s13():
    s = slots()

    def p1(x, y, w, h):
        return stack(
            x, y, w, h,
            [
                ("Primary", "all writes"),
                ("Secondary", "failover pair"),
                ("Read replica", "reporting + lag"),
                ("Other service", "API or event — not JOIN"),
            ],
        )

    def p2(x, y, w, h):
        return pipe_split(
            x, y, w, h,
            [
                ("API write", "Device service"),
                ("Primary", "Device DB"),
                ("Replica", "lag OK?"),
            ],
            "reporting",
            "events out",
        )

    def p3(x, y, w, h):
        return table(
            x, y, w, ["Pattern", "Owns writes", "Cross data"],
            [
                ("DB per service", "that service", "API or events"),
                ("Shared CompanyDb", "everyone", "JOIN anything"),
                ("Read replica", "still primary", "stale OK for reports"),
                ("Cross-DB JOIN", "hidden coupling", "distributed monolith"),
            ],
            header_fill="#ede9fe", h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "One CompanyDb",
            [
                "All services share CompanyDb",
                "JOIN Order to Payment in one SP",
                "Two teams writing the same tables",
                "A distributed monolith",
            ],
            "Service owns its DB",
            [
                "Device DB lives with Device service",
                "Payment arrives as an event",
                "Replicas for reads, accept lag",
                "No cross-database JOIN",
            ],
        )

    def p5(x, y, w, h):
        return hub(
            x, y, w, h, "Device DB",
            ["Device service", "Read replica", "Payment event", "No cross-DB JOIN"],
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Useful lines",
            footer_left_code(
                [
                    "-- Device service",
                    "-- dbo.Device lives here only",
                ],
                [
                    "-- not this",
                    "-- JOIN PaymentDb.dbo.Pay p",
                    "--   ON p.DeviceId = d.Id",
                ],
            ),
            [
                "Name who owns the database you touched",
                "Replicas for reads if lag is acceptable",
                "Other teams’ data via API or events",
            ],
            [
                "One database for all microservices",
                "Cross-DB JOIN “just this once”",
            ],
            [
                ("Owns schema", "one DbContext per service", "tables in that DB only"),
                ("Reads", "read replica connection", "async replica, accept lag"),
                ("Other domain", "HTTP / message", "event, not cross-DB JOIN"),
                ("Shared writes", "distributed monolith", "two services, one table"),
            ],
            third="T-SQL",
        )

    return svg(
        "Replicas and Database-per-Service",
        "SQL · S13  ·  Primary writes; replicas lag; no cross-database JOIN",
        [
            panel(s[0], 1, "Four roles", "Writes hit primary. Reports may hit a replica. Others get events.", p1),
            panel(s[1], 2, "Where a write goes", "Service → primary. Replica is for reads. Events leave the boundary.", p2),
            panel(s[2], 3, "Ownership vs sharing", "A shared CompanyDb plus JOINs is a distributed monolith.", p3),
            panel(s[3], 4, "The interview trap", "Microservices that JOIN across databases are one database.", p4),
            panel(s[4], 5, "Device owns Device", "PaymentCaptured is an event. It is not a JOIN to Payment DB.", p5),
            panel(s[5], 6, "Practice & C# comparison", "One DbContext per service. No second catalog in FromSql.", p6),
        ],
    )


def s14():
    s = slots()

    def p1(x, y, w, h):
        return log_bars(
            x, y, w, h,
            [
                ("What", "#1e3a5f", "covering index on Orders(CustomerId)"),
                ("Where", "#1d4ed8", "customer order list page"),
                ("Why", "#7c3aed", "PK seek + lookup per row"),
                ("How", "#ea580c", "INCLUDE Status, Total"),
                ("Problem", "#16a34a", "logical reads dropped; p95 recovered"),
            ],
        )

    def p2(x, y, w, h):
        return table(
            x, y, w, ["Q", "Index answer"],
            [
                ("What", "NC on CustomerId INCLUDE Status, Total"),
                ("Where", "Orders — customer list page"),
                ("Why", "clustered PK + lookup per row"),
                ("How", "CREATE INDEX … INCLUDE"),
                ("Problem", "a real number: reads / p95"),
            ],
            header_fill="#dbeafe", h=h,
        )

    def p3(x, y, w, h):
        return flow_v(
            x + w * 0.06, y, w * 0.88,
            [
                "Reproduce with prod params",
                "Actual plan — not estimated",
                "Waits and blocking",
                "One change",
                "Compare logical reads",
            ],
            h=h,
        )

    def p4(x, y, w, h):
        return vs_boxes(
            x, y, w, h,
            "I know SQL",
            [
                "I am strong in SQL.",
                "No index. No join type.",
                "No slow-SP order.",
                "No number.",
            ],
            "Five sentences each",
            [
                "Index: What/Where/Why/How/Problem",
                "Join: INNER vs LEFT on a report",
                "Slow SP: S09, not “add index”",
                "A real number if you have one",
            ],
        )

    def p5(x, y, w, h):
        return bullets(
            x, y,
            [
                "Join: name INNER vs LEFT for a report you shipped",
                "If numbers doubled, you checked 1:N before the index",
                "Slow SP: walk S09 without jumping to CREATE INDEX",
                "If you only read plans in QA, say that — still use the playbook",
            ],
            max_w=48,
            h=h,
        )

    def p6(x, y, w, h):
        return footer3(
            x, y, w, h, "Say aloud",
            footer_left_code(
                [
                    "-- index drill",
                    "-- What / Where / Why / How / Problem",
                    "-- covering Orders(CustomerId)",
                ],
                [
                    "-- slow SP drill",
                    "-- Reproduce → plan → change → measure",
                    "-- not “add an index” first",
                ],
            ),
            [
                "Two drills without stalling",
                "A number if you have one (reads / p95)",
                "Honesty about QA-only plans",
            ],
            [
                "I know SQL",
                "Five empty slogans",
            ],
            [
                ("What", "HasIndex on CustomerId", "NONCLUSTERED + INCLUDE"),
                ("Where", "the list endpoint", "Orders customer page"),
                ("How", "migration HasIndex", "CREATE INDEX … INCLUDE"),
                ("Problem", "p95 / timeout gone", "logical reads dropped"),
            ],
            third="T-SQL",
        )

    return svg(
        "SQL Five-Question Drill",
        "SQL · S14  ·  Five sentences for the index, five for the slow SP",
        [
            panel(s[0], 1, "The five questions", "What / Where / Why / How / Problem — then a number.", p1),
            panel(s[1], 2, "Worked example: that index", "Covering CustomerId on the order list. Say the lookups.", p2),
            panel(s[2], 3, "Worked example: that SP", "S09 out loud. Index is a hypothesis you measure.", p3),
            panel(s[3], 4, "The interview trap", "“I know SQL” is not an answer. Two drills are.", p4),
            panel(s[4], 5, "Join + honesty", "Name INNER vs LEFT. If you only saw QA plans, say so.", p5),
            panel(s[5], 6, "Recite, trap & C#", "HasIndex is the C# sentence. CREATE INDEX is the T-SQL one.", p6),
        ],
    )


BUILDERS = [
    ("S01", "Joins", s01),
    ("S02", "Subquery vs CTE vs EXISTS", s02),
    ("S03", "Temp Table vs Table Variable", s03),
    ("S04", "Stored Procedures", s04),
    ("S05", "Functions", s05),
    ("S06", "Indexes Clustered Nonclustered PK", s06),
    ("S07", "Views", s07),
    ("S08", "Transactions Commit and Rollback", s08),
    ("S09", "Slow Stored Procedure Playbook", s09),
    ("S10", "Scans Seeks and Parameter Sniffing", s10),
    ("S11", "Isolation Levels and Deadlocks", s11),
    ("S12", "DB Deploy and Rollback", s12),
    ("S13", "Replicas and Database-per-Service", s13),
    ("S14", "SQL Five-Question Drill", s14),
]


def write_sql_posters(images_dir: Path) -> dict[int, tuple[str, str, int]]:
    if len(BUILDERS) != 14:
        raise RuntimeError(f"expected 14 SQL posters, got {len(BUILDERS)}")
    return write_posters(images_dir, BUILDERS)
