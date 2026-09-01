/*
  Client1 lab — RDC_MetricS.dbo.A_employees1 execution plan
  Run this in the SSMS window that already opened the database (title bar: user1).

  Server:   .\sqlexpress
  Database: RDC_MetricS

  Login that works:
    Use the same SSMS connection you already have (user1).
    If that is Windows Authentication: Connect → Windows Auth → .\sqlexpress
    If that is SQL Authentication:     Connect → SQL Server Auth → user1 + password

  sqlcmd (only if THAT login is a Windows account mapped to the DB):
    sqlcmd -S .\sqlexpress -E -d RDC_MetricS

  This file does not SELECT NIC, passport, or fingerprint.
*/

USE [RDC_MetricS];
GO

/* ---------- 0) Prove you are in the right database ---------- */
SELECT
    @@SERVERNAME AS server_name,
    DB_NAME()    AS database_name,
    SUSER_SNAME() AS login_name,
    SYSTEM_USER   AS system_user;
GO

/* ---------- 1) PROBLEM query (matches your screenshot) ----------
   SSMS: Query → Include Actual Execution Plan  (Ctrl+M)
   Then run this batch.

   Plan you already saw:
     Query 1  USE [RDC_MetricS]     cost 0%
     Query 2  SELECT … A_employees1  cost 100%
              Table Scan on [A_employees1]  cost 100%

   Table Scan (not Clustered Index Scan) = heap: no clustered index.
   No WHERE = you asked for every row, so a scan is expected even after an index.
*/
SELECT
    [EmpID],
    [FullName (English)],
    [Status]
FROM [dbo].[A_employees1];
GO

/* ---------- 2) Read the plan (say this) ----------
   - Two queries in one batch: USE is free; the SELECT is the whole cost.
   - Fat arrow = many rows / wide rows moving.
   - Table Scan = read the heap row-by-row. No B-tree to seek.
   - Messages "(1 row affected)" is not the plan. Open the Execution Plan tab.
*/

/* ---------- 3) Diagnose indexes (run after the SELECT) ---------- */
SELECT
    i.name AS index_name,
    i.type_desc,
    i.is_unique,
    i.is_primary_key
FROM sys.indexes AS i
WHERE i.object_id = OBJECT_ID(N'dbo.A_employees1')
ORDER BY i.index_id;

-- Heap check: HEAP means no clustered index
SELECT
    t.name AS table_name,
    i.type_desc
FROM sys.tables AS t
JOIN sys.indexes AS i ON i.object_id = t.object_id AND i.index_id IN (0, 1)
WHERE t.name = N'A_employees1';

SELECT
    SUM(row_count) AS approx_rows
FROM sys.dm_db_partition_stats
WHERE object_id = OBJECT_ID(N'dbo.A_employees1')
  AND index_id IN (0, 1);
GO

/* ---------- 4) The lookup they actually need ----------
   If this is STILL a Table Scan, the missing clustered index is the real bug.
*/
DECLARE @id INT = 1;  -- pick a real EmpID from your table

SELECT
    [EmpID],
    [FullName (English)],
    [Status]
FROM [dbo].[A_employees1]
WHERE [EmpID] = @id;
GO

/* ---------- 5) FIX — clustered on EmpID (run once, after you check duplicates) ---------- */
-- Do not create UNIQUE if EmpID has duplicates (A_employees1 looks like a copy).
SELECT [EmpID], COUNT(*) AS cnt
FROM [dbo].[A_employees1]
GROUP BY [EmpID]
HAVING COUNT(*) > 1;

-- If that returns no rows, EmpID is unique — use UNIQUE CLUSTERED:
/*
CREATE UNIQUE CLUSTERED INDEX CX_A_employees1_EmpID
ON [dbo].[A_employees1]([EmpID]);
*/

-- If duplicates exist, clustered still helps seeks on EmpID (not unique):
/*
CREATE CLUSTERED INDEX CX_A_employees1_EmpID
ON [dbo].[A_employees1]([EmpID]);
*/
GO

/* ---------- 6) RETEST — same lookup, expect Clustered Index Seek ---------- */
DECLARE @id2 INT = 1;

SELECT
    [EmpID],
    [FullName (English)],
    [Status]
FROM [dbo].[A_employees1]
WHERE [EmpID] = @id2;
GO

/* ---------- 7) Optional — filter by Status (nonclustered from the WHERE) ----------
   Only after clustered exists. INCLUDE covers the SELECT list (no key lookup).
*/
/*
CREATE NONCLUSTERED INDEX IX_A_employees1_Status
ON [dbo].[A_employees1]([Status])
INCLUDE ([FullName (English)]);

SELECT [EmpID], [FullName (English)], [Status]
FROM [dbo].[A_employees1]
WHERE [Status] = N'Active';   -- use a Status value that exists
*/
GO

/* ---------- 8) Isolation (C14) — not a speed-up ----------
   NOLOCK is a dirty read, not a Table Scan fix.
   Default is Read Committed. Snapshot/RCSI if readers block writers.
*/
-- SET TRANSACTION ISOLATION LEVEL SNAPSHOT;
-- SELECT … WITH (NOLOCK)  -- do not use this as a performance habit
GO
