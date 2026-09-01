/*
  Run this ONCE in SSMS as the login that can create databases (user1 / sysadmin).
  Server: .\sqlexpress

  Cursor's Windows login is not dbcreator — it cannot create MyDB.
  After this succeeds, run:
    ClientInterview/sql/01_mydb_schema_seed.sql
    ClientInterview/sql/02_mydb_tune_steps.sql
*/
IF DB_ID(N'MyDB') IS NULL
BEGIN
    CREATE DATABASE [MyDB];
    PRINT 'Created MyDB.';
END
ELSE
    PRINT 'MyDB already exists.';
GO
