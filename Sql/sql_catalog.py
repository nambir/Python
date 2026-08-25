"""SQL Server interview catalog — ClientInterviewExpectations.pdf §§15–19."""

from interview_track import skill_entry as _entry

AREA_TITLES = {
    "S1": "S1 — Query fundamentals",
    "S2": "S2 — Performance & indexes",
    "S3": "S3 — Transactions & production",
}

SKILLS = [
    _entry(
        "S01",
        "S1",
        "Joins",
        "INNER, LEFT, OUTER, when rows multiply, how a missing ON clause explodes rows",
        "Draws one reporting query from the project and names the join type",
        ["INNER", "LEFT", "Multiplication", "ON vs WHERE"],
        "A join combines rows from two tables on a key. INNER keeps matches only. "
        "LEFT keeps every left row and nulls on the right. A missing or wrong key <b>multiplies</b> rows.",
        [
            ("INNER JOIN", "Only rows that match on both sides — active devices with a customer."),
            ("LEFT JOIN", "All orders, even with no shipment yet."),
            ("Multiplication", "Joining to a child with many rows duplicates the parent — SUM then double-counts unless you aggregate first."),
            ("Filter trap", "Putting a right-table filter in WHERE after LEFT JOIN turns it into an INNER JOIN."),
        ],
        "I pick INNER when both sides must exist, LEFT when the report must show gaps. If numbers look doubled I check for a one-to-many join before I blame the index.",
        (
            "WHERE on the right of a LEFT JOIN",
            "LEFT JOIN Shipment s ON s.OrderId = o.Id WHERE s.Status = 'Shipped'",
            "LEFT JOIN Shipment s ON s.OrderId = o.Id AND s.Status = 'Shipped'",
        ),
        code_src="""SELECT o.Id, s.ShippedAt
FROM dbo.Orders o
LEFT JOIN dbo.Shipment s
  ON s.OrderId = o.Id AND s.Status = N'Shipped';""",
        expected="LEFT JOIN keeps orders without a shipment.",
    ),
    _entry(
        "S02",
        "S1",
        "Subquery vs CTE",
        "When a subquery is enough, when a CTE is clearer, derived tables",
        "Rewrites one nested subquery as a named CTE they could explain",
        ["Subquery", "CTE", "Exists", "Derived"],
        "A subquery is a query inside another. A <b>CTE</b> (WITH name AS (...)) names that result so the outer query reads like steps. "
        "EXISTS often beats IN + DISTINCT for existence checks.",
        [
            ("Subquery", "Scalar or IN list — fine when short."),
            ("CTE", "Reusable named step, easier to test and to add a second consumer in the same batch."),
            ("EXISTS", "Stop at the first match — good for “has any payment”."),
            ("Not magic", "A CTE is not automatically faster. The optimizer may treat it like a subquery."),
        ],
        "I use a CTE when the interview query has two or three steps (filter devices, then join latest heartbeat). I use EXISTS when I only care that a child row exists.",
        (
            "IN (SELECT DISTINCT ...)",
            "WHERE CustomerId IN (SELECT DISTINCT CustomerId FROM Orders)",
            "WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.Id)",
        ),
        code_src="""WITH LatestBeat AS (
  SELECT DeviceId, MAX(SeenAt) AS SeenAt
  FROM dbo.Heartbeat
  GROUP BY DeviceId
)
SELECT d.Id, b.SeenAt
FROM dbo.Device d
LEFT JOIN LatestBeat b ON b.DeviceId = d.Id;""",
        expected="Named step, then join.",
    ),
    _entry(
        "S03",
        "S1",
        "Temp Table vs Table Variable",
        "When #temp gets statistics and a table variable does not, scope, recompiles",
        "Chooses #temp for a large intermediate set they would inspect in a slow SP",
        ["#temp", "@table", "Stats", "Scope"],
        "#temp tables live in tempdb, can have indexes, and the optimizer often has statistics. "
        "Table variables are lighter for tiny lists but the optimizer may assume one row.",
        [
            ("#temp", "Better for larger intermediate results, indexes, and statistics."),
            ("@table var", "Good for a handful of ids; can underestimate rows on bigger sets."),
            ("Scope", "#temp is session/batch; ##global is rare and dangerous. Table vars die at the end of the batch/module."),
            ("Interview", "If a slow SP stuffed 100k rows in a table variable, I would switch to #temp and look at the plan."),
        ],
        "For a few lookup ids I use a table variable. For a working set I will filter then join, I use #temp so the next statement gets a real row estimate.",
        (
            "100k rows in a table variable",
            "DECLARE @x TABLE (Id int); INSERT @x SELECT Id FROM Big;",
            "SELECT Id INTO #x FROM Big WHERE ...; CREATE INDEX IX ON #x(Id);",
        ),
        code_src="""SELECT d.Id
INTO #Active
FROM dbo.Device d
WHERE d.IsActive = 1;
CREATE CLUSTERED INDEX IX_Active ON #Active(Id);""",
        expected="#temp + index when the set is not tiny.",
    ),
    _entry(
        "S04",
        "S1",
        "Stored Procedures",
        "Why SPs, parameters, error handling, SET NOCOUNT, injection",
        "Explains one production SP they touched and how it is called from EF",
        ["Parameters", "TRY/CATCH", "NOCOUNT", "FromSql"],
        "A stored procedure is a named batch on SQL Server. Use parameters — never concatenate user input. "
        "TRY/CATCH + transaction when multiple writes must succeed together.",
        [
            ("Parameters", "Typed inputs; plans can be reused (watch parameter sniffing on S09)."),
            ("TRY/CATCH", "CATCH, rollback, RAISERROR/THROW with a safe message."),
            ("NOCOUNT ON", "Stops extra DONE_IN_PROC traffic that can confuse some clients."),
            ("EF", "FromSqlInterpolated / ExecuteSql — still parameterized."),
        ],
        "I keep set-based work in an SP when the logic is already proven in SQL. From C# I pass parameters. I do not hide every query in an SP just because the DBA prefers it.",
        (
            "String concat from C#",
            "\"EXEC GetOrders \" + customerId",
            "EXEC dbo.GetOrders @CustomerId = @p",
        ),
        code_src="""CREATE PROCEDURE dbo.GetOpenOrders
  @CustomerId uniqueidentifier
AS
BEGIN
  SET NOCOUNT ON;
  SELECT o.Id, o.Status
  FROM dbo.Orders o
  WHERE o.CustomerId = @CustomerId AND o.Status = N'Open';
END""",
        expected="Parameterized SP, NOCOUNT ON.",
    ),
    _entry(
        "S05",
        "S1",
        "Functions",
        "Scalar vs table-valued, why scalar UDFs in a WHERE can destroy performance",
        "Avoids wrapping a column in a scalar function in a hot WHERE",
        ["Scalar", "Inline TVF", "sargability", "Computed"],
        "Functions encapsulate expressions. A scalar UDF called per row in WHERE often blocks parallelism and indexes. "
        "Inline table-valued functions expand like a view and are usually safer.",
        [
            ("Scalar UDF", "Easy to write, expensive in filters — prefer inline TVF or computed column."),
            ("Inline TVF", "RETURNS TABLE AS RETURN SELECT ... — optimizer can expand it."),
            ("Multi-statement TVF", "Like a table var inside — estimates can be poor."),
            ("Interview", "If the slow plan shows a UDF in a predicate, I inline or rewrite."),
        ],
        "I do not put dbo.fnNormalize(Name) in a WHERE on a million-row table. I persist a normalized column or use an inline TVF.",
        (
            "Scalar UDF in WHERE",
            "WHERE dbo.Trim(Name) = @name",
            "WHERE Name = @name  -- or a persisted computed column",
        ),
        code_src="""CREATE FUNCTION dbo.ActiveDevices()
RETURNS TABLE
AS RETURN
  SELECT Id, Name FROM dbo.Device WHERE IsActive = 1;""",
        expected="Inline TVF, not a per-row scalar in WHERE.",
    ),
    _entry(
        "S06",
        "S2",
        "Indexes: Clustered, Nonclustered, PK",
        "Clustered vs nonclustered vs primary key; when indexes help and hurt; VARCHAR keys",
        "States whether the PK is clustered in their DB and why a second index exists",
        ["Clustered", "Nonclustered", "PK", "Write cost"],
        "A <b>clustered</b> index <b>is</b> the table order (one per table). A <b>nonclustered</b> index is a separate B-tree with pointers. "
        "A primary key is a constraint; by default it is clustered, but it does not have to be.",
        [
            ("Clustered", "Choose a key that grows and is used in lots of range/lookups (often the PK)."),
            ("Nonclustered", "Supports filters/joins that are not the clustered key. INCLUDE covering columns to avoid lookups."),
            ("PK vs clustered", "PK = uniqueness. Clustered = storage order. They often coincide; they are not the same word."),
            ("Hurt", "Every write maintains indexes. Wide VARCHAR keys and duplicate indexes slow inserts."),
        ],
        "I ask: what is the clustered key? If they filter by CustomerId all day, a nonclustered index on CustomerId INCLUDE Status may help. I do not index every column.",
        (
            "Index every VARCHAR",
            "CREATE INDEX IX_Notes ON T(Notes);",
            "Index selective keys; consider full-text for long text; watch write cost.",
        ),
        code_src="""-- PK clustered on Id (common)
ALTER TABLE dbo.Orders ADD CONSTRAINT PK_Orders PRIMARY KEY CLUSTERED (Id);
-- lookup by customer
CREATE NONCLUSTERED INDEX IX_Orders_Customer
  ON dbo.Orders(CustomerId) INCLUDE (Status, Total);""",
        expected="PK ≠ clustered always, but say what yours is.",
    ),
    _entry(
        "S07",
        "S1",
        "Views",
        "What a view is, indexed views, not a magic performance button",
        "Explains one view used as a stable contract for a screen or report",
        ["View", "Indexed view", "Security", "Contract"],
        "A view is a stored SELECT. It can hide joins for a reporting contract. "
        "It does not automatically make queries fast. An indexed (materialized) view has strict rules.",
        [
            ("Abstraction", "Give Angular/API a stable shape when tables change underneath."),
            ("Indexed view", "Persisted, extra writes; only when the same aggregate is hit constantly."),
            ("Permissions", "GRANT SELECT on the view without granting base tables."),
            ("Trap", "SELECT * FROM vw JOIN ... that re-joins the same tables again."),
        ],
        "We used a view for the device list DTO so the API did not copy five joins. I would not claim the view made it fast until I saw the plan.",
        (
            "Views are always faster",
            "Put everything in a view for performance.",
            "View = contract. Speed comes from the plan and indexes.",
        ),
        code_src="""CREATE VIEW dbo.vwDeviceList
AS
SELECT d.Id, d.Name, c.Name AS Customer
FROM dbo.Device d
JOIN dbo.Customer c ON c.Id = d.CustomerId;""",
        expected="Stable shape, not a free index.",
    ),
    _entry(
        "S08",
        "S3",
        "Transactions: Commit and Rollback",
        "BEGIN TRAN, COMMIT, ROLLBACK, TRY/CATCH, one unit of work",
        "Names two writes that must commit together in their project",
        ["BEGIN TRAN", "COMMIT", "ROLLBACK", "Savepoint"],
        "A transaction is all-or-nothing. Wallet debit and outbox insert must commit together. "
        "If the second write fails, ROLLBACK both.",
        [
            ("Commit", "Make the changes durable and visible per isolation level."),
            ("Rollback", "Undo the whole unit. Call it in CATCH after a failure."),
            ("EF", "SaveChanges is one transaction by default; ITransaction for explicit boundaries."),
            ("Microservices", "This SQL transaction cannot include another service’s database — that is a saga (Dotnet D65)."),
        ],
        "Inside one SQL Server database I wrap related writes in a transaction. Across services I do not pretend one ROLLBACK undoes payment and inventory.",
        (
            "Catch and still commit",
            "BEGIN TRAN; ... CATCH; COMMIT;",
            "BEGIN TRAN; TRY ... COMMIT; CATCH ROLLBACK; THROW;",
        ),
        code_src="""BEGIN TRAN;
BEGIN TRY
  UPDATE dbo.Wallet SET Balance -= @amt WHERE Id = @id;
  INSERT dbo.Outbox (WalletId, Type) VALUES (@id, N'Debited');
  COMMIT;
END TRY
BEGIN CATCH
  ROLLBACK;
  THROW;
END CATCH""",
        expected="Two writes, one commit or full rollback.",
    ),
    _entry(
        "S09",
        "S2",
        "Slow Stored Procedure Playbook",
        "Production SP is slow: plan, indexes, scans, stats, blocking, parameter sniffing, measure after",
        "Lists a ordered checklist they would actually run",
        ["Actual plan", "Scan vs seek", "Stats", "Sniffing"],
        "Interviewers ask: “Production stored procedure is slow. What will you do?” "
        "Do not start with “add an index.” Reproduce, capture the actual plan, check waits, then change, then measure.",
        [
            ("Reproduce", "Same parameters, similar data volume, in a copy of prod if you can."),
            ("Plan", "Actual execution plan: scans, lookups, spills, underestimated rows."),
            ("Indexes / stats", "Missing index hints are clues, not orders. UPDATE STATISTICS if they are stale."),
            ("Blocking / sniffing", "sp_whoisactive; parameter sniffing → OPTIMIZE FOR / local vars / recompile as last resorts."),
            ("After", "Compare duration, CPU, logical reads. Do not ship a guess."),
        ],
        "I start with “show me the actual plan and the parameters.” Then I check blocking. Then I look at scans on large tables. An index is a hypothesis I prove with before/after reads.",
        (
            "Add an index immediately",
            "CREATE INDEX on every column in the WHERE.",
            "Reproduce → actual plan → waits → one change → measure.",
        ),
        code_src="""-- Checklist (say it):
-- 1 reproduce with real params
-- 2 actual plan + SET STATISTICS IO, TIME
-- 3 blocking / deadlocks
-- 4 stats and sargable predicates
-- 5 one index or rewrite
-- 6 compare logical reads""",
        expected="Plan first, index second, numbers after.",
    ),
    _entry(
        "S10",
        "S2",
        "Scans, Seeks, and Parameter Sniffing",
        "Table scan vs index seek, lookups, sniffed plan reuse",
        "Explains one sniffing story: a plan for a rare parameter reused for a common one",
        ["Seek", "Scan", "Lookup", "Sniffing"],
        "A seek jumps to a key. A scan reads a large portion of the table/index. "
        "Parameter sniffing: SQL Server caches a plan from the first parameter and reuses it for others.",
        [
            ("Seek", "Good when the predicate is selective and sargable (not wrapped in a function)."),
            ("Scan", "OK for small tables or when most rows qualify; painful on large tables."),
            ("Lookup", "Nonclustered seek then clustered lookup — INCLUDE columns to cover."),
            ("Sniffing", "First call with CustomerId that has 3 rows vs one that has 3 million."),
        ],
        "If a report is fast for one customer and slow for another with the same SP, I suspect sniffing or data skew. I look at the cached plan’s estimated vs actual rows.",
        (
            "Always recompile",
            "OPTION (RECOMPILE) on every call",
            "Use recompile or OPTIMIZE FOR only after proving sniffing.",
        ),
        code_src="""-- sargable
WHERE CreatedAt >= @from AND CreatedAt < @to
-- not sargable
WHERE YEAR(CreatedAt) = 2026""",
        expected="Sargable range; sniffing is a cached-plan story.",
    ),
    _entry(
        "S11",
        "S3",
        "Isolation Levels and Deadlocks",
        "READ COMMITTED, SNAPSHOT, blocking vs deadlocks, row versioning",
        "Picks an isolation level for a report vs a wallet debit",
        ["READ COMMITTED", "SNAPSHOT", "Blocking", "Deadlock"],
        "Isolation decides what you see under concurrency. Higher isolation reduces anomalies and can increase blocking. "
        "READ_COMMITTED_SNAPSHOT uses row versions to reduce reader/writer blocking. A deadlock is a cycle; SQL picks a victim.",
        [
            ("READ COMMITTED", "Default; can still block. Good starting point."),
            ("SNAPSHOT / RCSI", "Readers don’t block writers as much; tempdb version store cost."),
            ("SERIALIZABLE", "Range locks; rare for OLTP APIs."),
            ("Deadlock", "Capture graph, make access order consistent, keep transactions short, index to seek."),
        ],
        "Wallet debit stays short and default isolation unless we proved otherwise. A long report might use SNAPSHOT so it does not hold locks on hot tables. Deadlocks: I show the graph and the two procedures’ lock order.",
        (
            "NOLOCK everywhere",
            "WITH (NOLOCK) on every SELECT",
            "NOLOCK can skip/duplicate rows. Prefer RCSI or a real snapshot if dirty reads are unacceptable.",
        ),
        code_src="""SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRAN;
UPDATE dbo.Wallet SET Balance -= @amt WHERE Id = @id;
COMMIT;""",
        expected="Short transaction; NOLOCK is not a performance strategy.",
    ),
    _entry(
        "S12",
        "S3",
        "DB Deploy and Rollback",
        "Migrations, expand/contract, rollback scripts, production data changes",
        "Explains how a column add is safer than a rename, and how they roll back",
        ["Expand", "Contract", "Rollback", "Data fix"],
        "Schema changes go DEV → QA → Prod with the app. Prefer additive changes (new nullable column) over breaking renames. "
        "A rollback script is a first-class artifact, not an afterthought.",
        [
            ("Expand/contract", "Add new column and dual-write, deploy app, then drop old column later."),
            ("Migrations", "EF migrations or SQL scripts in CI — same files the team reviews."),
            ("Data changes", "Back up / script a reversible UPDATE; never a one-way DELETE without a copy."),
            ("Failure", "If the app cannot start, roll forward with a fix or roll back the package and the last script."),
        ],
        "I do not rename a live column in one deploy. I add, dual-read, switch the app, then remove. Rollback is the reverse script plus the previous app package.",
        (
            "Rename in prod in one shot",
            "EXEC sp_rename 'Orders.Amt', 'Amount'",
            "Add Amount, backfill, switch app, drop Amt in a later release.",
        ),
        code_src="""-- expand
ALTER TABLE dbo.Orders ADD Amount decimal(18,2) NULL;
UPDATE dbo.Orders SET Amount = Amt WHERE Amount IS NULL;
-- later contract: ALTER TABLE dbo.Orders DROP COLUMN Amt;""",
        expected="Additive first; rollback script stored with the migration.",
    ),
    _entry(
        "S13",
        "S3",
        "Replicas and Database-per-Service",
        "Primary/secondary, read replicas, why one SQL transaction cannot span microservices",
        "States who owns the database for a service they worked on",
        ["Primary", "Replica", "DB per service", "No shared writes"],
        "A primary takes writes. Replicas serve reads with lag. "
        "Database-per-service means Order DB is not joined to Payment DB in one SQL statement — that is a coupling trap.",
        [
            ("Primary / secondary", "Failover pair; secondary may be read-only."),
            ("Read replica", "Scale reporting; accept replication delay."),
            ("DB per service", "Each service owns its schema. Cross-service data via API or events."),
            ("Shared DB", "Two services writing the same tables is a distributed monolith."),
        ],
        "Device service owned Device DB. Reporting could read a replica if lag was acceptable. I would not JOIN across another team’s database from my SP.",
        (
            "One database for all microservices",
            "All services share CompanyDb and join freely.",
            "Service owns its DB; others consume APIs or events.",
        ),
        code_src="""-- Device service
-- dbo.Device lives here only
-- Payment data arrives as PaymentCaptured event, not a cross-DB JOIN""",
        expected="Own your schema; replicas for reads; events for others.",
    ),
    _entry(
        "S14",
        "S3",
        "SQL Five-Question Drill",
        "What / Where / Why / How / Problem for joins, indexes, and a slow-SP story",
        "Answers all five for one index they added or would add",
        ["What", "Where", "Why", "How", "Problem"],
        "Practice the five questions on one join, one index, and the slow-SP playbook.",
        [
            ("Index", "What: nonclustered on CustomerId INCLUDE Status. Where: Orders. Why: list page scanned. How: CREATE INDEX. Problem: p95 dropped (use a real number if you have one)."),
            ("Join", "Name INNER vs LEFT for a report you shipped."),
            ("Slow SP", "Walk S09 without jumping to “add index.”"),
            ("Honesty", "If you only read plans in QA, say that — still use the playbook."),
        ],
        "Index drill: What — covering index on Orders(CustomerId). Where — customer order list. Why — clustered PK seek + lookup per row. How — INCLUDE Status, Total. Problem — logical reads dropped and the list page stopped timing out.",
        (
            "I know SQL",
            "I am strong in SQL.",
            "Five sentences for the index, five for the slow SP.",
        ),
        code_src="""-- Say aloud:
-- What / Where / Why / How / Problem — that index
-- Reproduce → plan → change → measure — that SP""",
        expected="Two drills with a number if you have one.",
    ),
]

assert len(SKILLS) == 14
assert [s["id"] for s in SKILLS] == [f"S{i:02d}" for i in range(1, 15)]
