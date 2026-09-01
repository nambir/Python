/*
  MyDB — step-by-step execution plan lab (C21).
  Prerequisite: 01_mydb_schema_seed.sql

  SSMS: USE MyDB, then Query → Include Actual Execution Plan (Ctrl+M) before each SELECT.
  One change per step. Do not run the whole file as one batch if you want a clean plan per query —
  highlight one step at a time.

  Expected operators (typical on 50k-row heap; your % may differ):
    Step 0 before: Table Scan on Orders
    Step 0 after:  Clustered Index Scan (filter is not OrderId)
    Step 1 after:  Index Seek on IX_Orders_Customer_Status
    Step 2:        SELECT * or narrow INCLUDE → Nested Loops + Key Lookup
    Step 2b:       key = CustomerId only → Status residual on Key Lookup
    Step 3 before: YEAR() residual on Orders; OrderLine scan often ~50%
    Step 3 after:  date range (query first), then optional (Status, CreatedUtc)
    Step 4 before: implicit convert warning
    Step 4 after:  matching types
    Step 5:        OR vs UNION ALL

  Demo filter: CustomerId = 42 AND Status = 'Closed' (shows rows).
  'Open' for customer 42 is often 0 rows — the operator still matters.
*/
SET NOCOUNT ON;
USE [MyDB];
GO

-- Optional: prove seed (heap Indexes folder empty on Orders)
SELECT TOP (2) * FROM dbo.Customer;
SELECT TOP (2) * FROM dbo.OrderLine;
SELECT TOP (2) * FROM dbo.Orders;
SELECT TOP (2) * FROM dbo.Product;
GO

/* ========== STEP 0 — heap Table Scan ==========
   Why heap: seed created dbo.Orders with columns only — no clustered PK.
   Heap = unordered pages. WHERE CustomerId / Status has nothing to Seek.
   Expect: Table Scan 100%. Hover: Object = dbo.Orders (no index). Predicate = residual WHERE.
   Output List = SELECT columns. Rows Read ≈ 50,000 vs Actual Rows — both matter.
*/
-- Ctrl+M, run this SELECT only:
SELECT o.OrderId, o.CustomerId, o.Status, o.Total, o.CreatedUtc
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
  AND o.Status = 'Closed';
GO

-- Fix 0: clustered PK (the table’s order). Filter is still not OrderId.
-- Ctrl+M: Query 1 = IF NOT EXISTS (ignore). Query 2 = Table Scan heap → Sort → Index Insert CX_Orders.
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'CX_Orders' AND object_id = OBJECT_ID(N'dbo.Orders'))
    CREATE UNIQUE CLUSTERED INDEX CX_Orders ON dbo.Orders (OrderId);
GO

-- Ctrl+M, same SELECT — expect Clustered Index Scan (or scan + residual), not Seek on CustomerId.
-- Object = CX_Orders. Rows Read still ~50,000. Predicate still residual.
SELECT o.OrderId, o.CustomerId, o.Status, o.Total, o.CreatedUtc
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
  AND o.Status = 'Closed';
GO

/* ========== STEP 1 — nonclustered from the WHERE ==========
   KEY (CustomerId, Status) = WHERE — find matching rows (book index).
   INCLUDE (Total, CreatedUtc) = SELECT — return values without going back to the table.
   Ctrl+M on CREATE: Scan CX → Sort by NCI keys → Index Insert.
   Then same SELECT: Index Seek, Rows Read ≈ matching rows (not 50,000).
*/
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'IX_Orders_Customer_Status' AND object_id = OBJECT_ID(N'dbo.Orders'))
    CREATE NONCLUSTERED INDEX IX_Orders_Customer_Status
    ON dbo.Orders (CustomerId, Status)
    INCLUDE (Total, CreatedUtc);
GO

-- Ctrl+M — expect Index Seek on IX_Orders_Customer_Status
SELECT o.OrderId, o.CustomerId, o.Status, o.Total, o.CreatedUtc
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
  AND o.Status = 'Closed';
GO

/* ========== STEP 2 — Key Lookup ==========
   Covering NCI from step 1 + this SELECT * → extra columns not in the leaf
   → Nested Loops (physical) / Inner Join (logical) → Key Lookup.
   Hover Key Lookup: Number of Executions. Many + hot query → INCLUDE.
   A few lookups → covering can cost more on writes. Not every lookup is bad.
*/
SELECT *
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
  AND o.Status = 'Closed';
GO

-- Fix 2: list only columns in the key / INCLUDE / OrderId → Seek only
SELECT o.OrderId, o.CustomerId, o.Status, o.Total, o.CreatedUtc
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
  AND o.Status = 'Closed';
GO

/* --- Optional 2a (your image 7): INCLUDE (Total) only, SELECT still wants CreatedUtc ---
DROP INDEX IX_Orders_Customer_Status ON dbo.Orders;
CREATE NONCLUSTERED INDEX IX_Orders_Customer_Status
  ON dbo.Orders (CustomerId, Status) INCLUDE (Total);
-- same SELECT as Fix 2 → Key Lookup Output List = CreatedUtc, ~96%
*/

/* --- Optional 2b (your image 8): key = CustomerId only, no Status, no CreatedUtc ---
DROP INDEX IX_Orders_Customer_Status ON dbo.Orders;
CREATE NONCLUSTERED INDEX IX_Orders_Customer_Status
  ON dbo.Orders (CustomerId) INCLUDE (Total);
-- same SELECT → Seek Predicates = CustomerId only (e.g. 25 rows).
-- Key Lookup Predicate = Status = 'Closed' (e.g. 25 read → 19 kept, 6 dropped).
-- Recreate the covering index when done:
-- DROP INDEX IX_Orders_Customer_Status ON dbo.Orders;
-- CREATE NONCLUSTERED INDEX IX_Orders_Customer_Status
--   ON dbo.Orders (CustomerId, Status) INCLUDE (Total, CreatedUtc);
*/

/* ========== STEP 3 — join + SARGable date ==========
   Hover: 49% OrderLine CI Scan (150k). Orders Predicate = YEAR() residual.
   Merge Join = both sides sorted. Missing index is a hint — rewrite the query first.
   GOOD range = same year. Same actual rows. OrderLine still ~50% until you change the count.
   Then create (Status, CreatedUtc) and run GOOD again — expect Orders Seek/range, not only a new hint.
*/
-- BAD: function on the column → cannot seek CreatedUtc
SELECT c.Name, o.OrderId, o.Total, COUNT_BIG(*) AS line_count
FROM dbo.Orders AS o
JOIN dbo.Customer AS c ON c.CustomerId = o.CustomerId
JOIN dbo.OrderLine AS l ON l.OrderId = o.OrderId
WHERE o.Status = 'Open'
  AND YEAR(o.CreatedUtc) = YEAR(SYSUTCDATETIME())
GROUP BY c.Name, o.OrderId, o.Total;
GO

-- GOOD: range on the column
DECLARE @from DATETIME2(0) = DATEFROMPARTS(YEAR(SYSUTCDATETIME()), 1, 1);
DECLARE @to   DATETIME2(0) = DATEADD(YEAR, 1, @from);

SELECT c.Name, o.OrderId, o.Total, COUNT_BIG(*) AS line_count
FROM dbo.Orders AS o
JOIN dbo.Customer AS c ON c.CustomerId = o.CustomerId
JOIN dbo.OrderLine AS l ON l.OrderId = o.OrderId
WHERE o.Status = 'Open'
  AND o.CreatedUtc >= @from
  AND o.CreatedUtc < @to
GROUP BY c.Name, o.OrderId, o.Total;
GO

-- After GOOD still scans Orders: this is the index the missing-index hint asked for
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE name = N'IX_Orders_Status_Created' AND object_id = OBJECT_ID(N'dbo.Orders'))
    CREATE NONCLUSTERED INDEX IX_Orders_Status_Created
    ON dbo.Orders (Status, CreatedUtc)
    INCLUDE (CustomerId, Total);
GO

-- Ctrl+M — same GOOD SELECT again. Hover Orders: Seek/range on (Status, CreatedUtc), not YEAR.
DECLARE @from2 DATETIME2(0) = DATEFROMPARTS(YEAR(SYSUTCDATETIME()), 1, 1);
DECLARE @to2   DATETIME2(0) = DATEADD(YEAR, 1, @from2);

SELECT c.Name, o.OrderId, o.Total, COUNT_BIG(*) AS line_count
FROM dbo.Orders AS o
JOIN dbo.Customer AS c ON c.CustomerId = o.CustomerId
JOIN dbo.OrderLine AS l ON l.OrderId = o.OrderId
WHERE o.Status = 'Open'
  AND o.CreatedUtc >= @from2
  AND o.CreatedUtc < @to2
GROUP BY c.Name, o.OrderId, o.Total;
GO

/* ========== STEP 4 — implicit convert ========== */
-- BAD: Status is varchar, literal is int → convert warning, often scan
SELECT o.OrderId, o.Status
FROM dbo.Orders AS o
WHERE o.Status = 1;
GO

-- GOOD: same type
SELECT o.OrderId, o.Status
FROM dbo.Orders AS o
WHERE o.Status = 'Open';
GO

/* ========== STEP 5 — rewrite, not another index ==========
   OR on two columns often prevents a single seek. Two seeks + UNION ALL can win.
*/
SELECT o.OrderId, o.CustomerId, o.Status
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
   OR o.Status = 'Hold';
GO

SELECT o.OrderId, o.CustomerId, o.Status
FROM dbo.Orders AS o
WHERE o.CustomerId = 42
UNION ALL
SELECT o.OrderId, o.CustomerId, o.Status
FROM dbo.Orders AS o
WHERE o.Status = 'Hold'
  AND o.CustomerId <> 42;  -- avoid dupes if a row matches both
GO

PRINT 'Lab done. Heap Table Scan → CX → NCI Seek. Key = WHERE, INCLUDE = SELECT. Key Lookup: check executions. YEAR() → date range, then index. Types match. UNION ALL if OR wrecks the Seek.';
GO
