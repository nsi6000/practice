# SQL Server
* [Internals](https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-guides?view=sql-server-ver15)
  - [Ghost cleanup process](https://docs.microsoft.com/en-us/sql/relational-databases/ghost-record-cleanup-process-guide?view=sql-server-ver15)
  - [Page and Extents Architecture](https://docs.microsoft.com/en-us/sql/relational-databases/pages-and-extents-architecture-guide?view=sql-server-ver15)
  - [Transaction Logs Architecture](https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide?view=sql-server-ver15)
  - [Transaction Locking](https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver15)
  - [Index Architecture](https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver15)
  - [Latch contention](https://docs.microsoft.com/en-us/sql/relational-databases/diagnose-resolve-latch-contention?view=sql-server-ver15)
  - [Spinlock contention](https://docs.microsoft.com/en-us/sql/relational-databases/diagnose-resolve-spinlock-contention?view=sql-server-ver15)
  - [Thread and Task Architecture](https://docs.microsoft.com/en-us/sql/relational-databases/thread-and-task-architecture-guide?view=sql-server-ver15)
  - [Query processing](https://docs.microsoft.com/en-us/sql/relational-databases/query-processing-architecture-guide?view=sql-server-ver15)
  - [Memory Management](https://docs.microsoft.com/en-us/sql/relational-databases/memory-management-architecture-guide?view=sql-server-ver15)
* install, update & configure SQL Server.
	- [DTA (Database Tuning Advisor)](https://docs.microsoft.com/en-us/sql/tools/dta/dta-utility?view=sql-server-ver15)
	- Propreties and sp_configure.
* Encryption, Access, permissions and auditing.
	- Manage users, roles and permissions.
	- RLS (row-level security) and DDM (dynamic data masking).
	- CLE(cell-level encryption), TDE and compression.
	- Manage an audit and audit log.
	- Accounts, Server Roles, Database Roles and permissions (GRANT/DENY).
	- Certificate Based Logins.
	- Auditing and Policies.
* Backup, Restore and DB Integrity.
  - [Overview of Backup & Restore](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver15)
	- Backups: full, differential, file, filegroup, partial, transaction log, tail-log, copy-only.
	- Recovery models: simple, full, bulked logged.
	- transaction log backups.
  - Tail-Log Backups.
	- Backup-Restore vs Attach-Detach DB. (.DACPAC, .BACPAC)
	- DB Recovery without Backup (dbcc checkdb ( repair_allow_data_loss))
	- [FileGroup/Page restore](https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-files-and-filegroups-sql-server?view=sql-server-ver15)
* Monitoring, Indexes and Statistics.
	- Data Collector
	- Resource Governor and PerfMon.
	- DMVs and SQL Profiler.	
	- [Extended Events](https://docs.microsoft.com/en-us/sql/relational-databases/extended-events/quick-start-extended-events-in-sql-server?view=sql-server-ver15)
	- Traces and Trace Flags (dbcc traceon, dbcc traceoff, dbcc tracestatus)
	- Execution Plans
	- Policy-based Management.
	- Configure Database Mail.
	- Index types, Index Fragmentation, manage CSI.
	- Fill Factor. Index Statistics, reorganize and Rebuild (if more than 30% fragmentation)(WITH Online=ON, FILLFACTOR=80). AUS (Auto-Update Statistics)
	- Filtered Indexes. (for optimization) (WHERE city = 'London')
	- find Missing/unused indexes (sys.dm_db_index_usage_stats -> user_seeks = good; user_scans, lookups and updates are bad.)
	- Partitioning. (create filegroups, partition function, parition scheme, modify table using partition scheme.)
	- Compression.
	- Concurrency.
* HA & DR (High Availability and Disaster Recovery).
	- [Log Shipping](https://docs.microsoft.com/en-us/sql/database-engine/database-mirroring/database-mirroring-and-log-shipping-sql-server?view=sql-server-ver15)
	- AOAG (AlwaysOn Availability Groups)
	- Failover Cluster Instances
	- SQL Server Cluster.

## Misc
Types of Databases.
FTI, FTS and CSI. FILETABLE.
Troubleshouting:
	sys.messages
	dbcc checkalloc, checktable, checkcatalog, checkdb.
	dbcc shrinkfile(<file>,<number>);
	dbcc shrinkdatabase(<db_name>,<number>);

SINGLE_USER mode vs MULTI_USER mode

Transaction Logs
Change Tracking and CDC
Temporal Tables

https://www.sqlshack.com/various-techniques-to-audit-sql-server-databases/

* SQL Server Locking:
	- Live Locking: shared locks prevent another process to acquire exclusive locks.
	- Dead Locking: two processes competes for the same resource.
	- Blocking: the second connection is blocked.

```t-sql
select @@version;

sp_configure;
sp_configure 'clr_enabled', 1;
RECONFIGURE;

sp_configure 'show advanced options', 1;
RECONFIGURE;

sp_configure 'affinity I/O mask', 1;
RECONFIGURE;
ALTER SERVER CONFIGURATION SET PROCESS AFFINITY CPU=0;

SELECT
 Name
,Size
,Size/128 as Size_MB
,FILEPROPERTY(Name, 'SpaceUsed')/128 as Used_MB
FROM dbo.sysfiles;

GRANT ALTER ANY DATABASE TO MailAdmin WITH GRANT OPTION;
DENY CONNECT SQL TO MailAdmin;

Certificate Based Logins (CBLs):
CREATE MASTER KEY ENCRYPTION BY PASSWORD='MyPassword01';
CREATE CERTIFICATE MyCert WITH SUBJECT='This is my cert', EXPIRY_DATE='2030-01-01';
BACKUP CERTIFICATE MyCert
	TO FILE='C:\data\MyCert.cer' WITH PRIVATE KEY (
	FILE=':\data\MyCert.key',
	ENCRYPTION BY PASSWORD='AnotherPassword02'
	);
.

TDE:
OPEN MASTER KEY DECRYPTION BY PASSWORD='NewPassword03';
CREATE CERTIFICATE CertTDE WITH SUBJECT='Certificate for TDE';
BACKUP CERTIFICATE CertTDE
	TO FILE='C:\data\CertTDE.cer' WITH PRIVATE KEY (
	FILE=':\data\CertTDE.key',
	ENCRYPTION BY PASSWORD='AnotherPassword02'
	);
.
CREATE DATABASE ENCRYPTION KEY WITH ALGORITHM=AES_256 ENCRYPTION BY SERVER CERTIFICATE CertTDE;
ALTER DATABASE MyTestDB SET ENCRYPTION ON;
SELECT
 DB_NAME(DATABASE_ID) as DB
,ENCRYPTION_STATE
,ENCRYPTOR_TYPE
FROM SYS.DM_DATABASE_ENCRYPTION_KEYS;

COMPRESSION:
sp_estimate_data_compression_savings 'SalesLT', 'SalesOrderDetail', null, null, 'ROW';
sp_estimate_data_compression_savings 'SalesLT', 'SalesOrderDetail', null, null, 'PAGE';
ALTER TABLE SalesLT.SalesOrderDetail REBUILD PARTITION=ALL WITH (DATA_COMPRESSION=PAGE);

FULL-TEXT INDEXING:
???
SELECT * FROM SalesLT.ProductDescription WHERE CONTAINS(Description, 'mountain or wheel');
SELECT * FROM SalesLT.ProductDescription WHERE CONTAINS(Description, 'NEAR(mountain, frame), 2');
SELECT * FROM sys.fulltext_document_types;
sp_fulltext_service 'load_os_resources', 1;
	=> RESTART SERVER.
SELECT * FROM sys.fulltext_document_types; //new document types loaded.

ALTER DATABASE MyTestDB SET_FILESTREAM(NON_TRANSACTED_ACCESS=Full, DIRECTORY_NAME=N'Files');
ALTER DATABASE MyTestDB ADD FILEGROUP FGFiles CONTAINS FILESTREAM;
ALTER DATABASE MyTestDB ADD FILE (Name='Files', Filename='C:\Files') TO FILEGROUP FGFiles;
CREATE TABLE Documents AS FILETABLE WITH (FILETABLE_DIRECTORY='Documents',FILETABLE_COLLATE_FILENAME=database_default);
SELECT * FROM Documents;

SELECT * FROM SYS.DM_EXEC_SESSIONS S INNER JOIN SYS.DM_RESOURCE_GOVERNOR_WORKLOAD_GROUPS G ON G.GROUP_ID = S.GROUP_ID;
SELECT * FROM SYS.MESSAGES;
SELECT * FROM SYS.DM_OS_WAIT_STATS;
SELECT
 SUM(Pages_KB) as Total_Pages
,SUM(Virtual_memory_reserved_kb) as Total_Reserved
,SUM(Virtual_Memory_Commited_kb) as Total_Commited
FROM SYS.DM_OS_MEMORY_CLERKS;
SELECT * FROM SYS.DM_OS_MEMORY_CACHE_COUNTERS MCC INNER JOIN SYS.DM_OS_MEMORY_CACHE_CLOCK_HANDS MCCH ON MCC.CACHE_ADDRESS = MCCH.CACHE_ADDRESS;

DBCC CHECKDB(MyDatabaseName);
DBCC TRACEON(3226,-1);
DBCC TRACEOFF(3226,-1);

RECOVER WITHOUT BACKUP:
ALTER DATABASE MyDatabaseName SET EMERGENCY;
ALTER DATABASE MyDatabaseName SET SINGLE_USER;
DBCC CHECKDB(MyDatabaseName, REPAIR_ALLOW_DATA_LOSS);
```

