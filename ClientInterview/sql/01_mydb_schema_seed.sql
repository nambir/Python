/*
  MyDB lab — schema + data for execution-plan tuning (C21).
  Prerequisite: 00_create_mydb.sql already ran (database MyDB exists).

  SSMS: connect as user1 (or whoever owns MyDB), then F5 this file.
  Server: .\sqlexpress

  Creates:
    Customer   ~2,000  clustered PK
    Product    ~200    clustered PK
    Orders     ~50,000 HEAP (no clustered index — you will add it in step 0)
    OrderLine  ~150,000 clustered PK (OrderId, LineNumber)
    Note: do not name a column LineNo — LINENO is a reserved keyword.
*/
SET NOCOUNT ON;
GO
USE [MyDB];
GO

IF OBJECT_ID(N'dbo.OrderLine', N'U') IS NOT NULL DROP TABLE dbo.OrderLine;
IF OBJECT_ID(N'dbo.Orders', N'U') IS NOT NULL DROP TABLE dbo.Orders;
IF OBJECT_ID(N'dbo.Product', N'U') IS NOT NULL DROP TABLE dbo.Product;
IF OBJECT_ID(N'dbo.Customer', N'U') IS NOT NULL DROP TABLE dbo.Customer;
GO

CREATE TABLE dbo.Customer
(
    CustomerId INT           NOT NULL,
    Name       NVARCHAR(80)  NOT NULL,
    City       NVARCHAR(40)  NOT NULL,
    CONSTRAINT PK_Customer PRIMARY KEY CLUSTERED (CustomerId)
);

CREATE TABLE dbo.Product
(
    ProductId INT           NOT NULL,
    Sku       NVARCHAR(20)  NOT NULL,
    Name      NVARCHAR(80)  NOT NULL,
    CONSTRAINT PK_Product PRIMARY KEY CLUSTERED (ProductId)
);

-- HEAP on purpose (Step 0 Table Scan).
-- Heap = no clustered index: no PRIMARY KEY CLUSTERED, no CREATE CLUSTERED INDEX.
-- Pages are unordered. A WHERE on CustomerId / Status cannot Seek until we add an index.
-- Customer / Product / OrderLine have clustered PKs so Object Explorer can contrast an empty Indexes folder on Orders.
CREATE TABLE dbo.Orders
(
    OrderId    INT           NOT NULL,
    CustomerId INT           NOT NULL,
    Status     VARCHAR(12)   NOT NULL,
    Total      MONEY         NOT NULL,
    CreatedUtc DATETIME2(0)  NOT NULL
);

CREATE TABLE dbo.OrderLine
(
    OrderId     INT    NOT NULL,
    LineNumber  INT    NOT NULL,
    ProductId   INT    NOT NULL,
    Qty         INT    NOT NULL,
    UnitPrice   MONEY  NOT NULL,
    CONSTRAINT PK_OrderLine PRIMARY KEY CLUSTERED (OrderId, LineNumber)
);
GO

;WITH n AS
(
    SELECT TOP (2000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_objects a
    CROSS JOIN sys.all_objects b
)
INSERT dbo.Customer (CustomerId, Name, City)
SELECT
    n,
    CONCAT(N'Customer ', n),
    CASE n % 5
        WHEN 0 THEN N'Chennai'
        WHEN 1 THEN N'Bengaluru'
        WHEN 2 THEN N'Hyderabad'
        WHEN 3 THEN N'Pune'
        ELSE N'Mumbai'
    END
FROM n;

;WITH n AS
(
    SELECT TOP (200) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_objects a
    CROSS JOIN sys.all_objects b
)
INSERT dbo.Product (ProductId, Sku, Name)
SELECT
    n,
    CONCAT(N'SKU', RIGHT(CONCAT(N'000', n), 4)),
    CONCAT(N'Product ', n)
FROM n;

;WITH n AS
(
    SELECT TOP (50000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_objects a
    CROSS JOIN sys.all_objects b
)
INSERT dbo.Orders (OrderId, CustomerId, Status, Total, CreatedUtc)
SELECT
    n,
    ((n - 1) % 2000) + 1,
    CASE n % 10
        WHEN 0 THEN 'Open'
        WHEN 1 THEN 'Hold'
        ELSE 'Closed'
    END,
    CAST((n % 90) + 10 AS MONEY),
    DATEADD(DAY, -(n % 400), SYSUTCDATETIME())
FROM n;

;WITH n AS
(
    SELECT TOP (150000) ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_objects a
    CROSS JOIN sys.all_objects b
)
INSERT dbo.OrderLine (OrderId, LineNumber, ProductId, Qty, UnitPrice)
SELECT
    ((n - 1) / 3) + 1,
    ((n - 1) % 3) + 1,
    ((n - 1) % 200) + 1,
    ((n - 1) % 5) + 1,
    CAST(((n % 40) + 5) AS MONEY)
FROM n
WHERE ((n - 1) / 3) + 1 <= 50000;
GO

ALTER TABLE dbo.Orders
    ADD CONSTRAINT FK_Orders_Customer
    FOREIGN KEY (CustomerId) REFERENCES dbo.Customer (CustomerId);

-- No FK OrderLine → Orders yet: Orders is a heap with no unique key until CX in step 0.

ALTER TABLE dbo.OrderLine
    ADD CONSTRAINT FK_OrderLine_Product
    FOREIGN KEY (ProductId) REFERENCES dbo.Product (ProductId);
GO

-- Orders is still a HEAP (index_id 0). Clustered comes in 02_mydb_tune_steps.sql
SELECT t.name AS table_name, i.type_desc, p.rows
FROM sys.tables AS t
JOIN sys.indexes AS i ON i.object_id = t.object_id AND i.index_id IN (0, 1)
JOIN sys.partitions AS p ON p.object_id = t.object_id AND p.index_id = i.index_id
ORDER BY t.name;

PRINT 'MyDB seed done. Orders should be HEAP. Next: 02_mydb_tune_steps.sql (Ctrl+M).';
GO
