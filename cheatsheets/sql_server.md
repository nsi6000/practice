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

select @@version;
