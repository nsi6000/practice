# Data Storage Principles

* [Kimball Dimensional Techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/)
* Database
* Database types: relational, wcs, document, graph, key-value, search,...
* RDBMS vs NoSQL
* Row store vs Column store
* [Datastore](https://en.wikipedia.org/wiki/Data_store)
* "Columns are not fields. Rows are not records. Tables are not files." - Joe Celko.
* [Data warehouse](https://en.wikipedia.org/wiki/Data_warehouse) (definition + criteria)
* Corporate Information Factory (CIF) (Inmon 1999)
* [ODS](https://en.wikipedia.org/wiki/Operational_data_store)
* ODS characteristics:
  - Subject-oriented.
  - Integrated data.
  - Current (little to no history).
  - Volatility (data change frequently).
  - Detailed (low granularity).
* ODS Types:
  - Class 1: no aggregation/transformation on data.
  - Class 2: 30 minutes to 1 hour for update.
  - Class 3: loaded in batches. (daily basis)
  - Class 4: data come from operational systems and data warehouse.
  - Class 5: heavy aggregation/transformation on data. (slow and complex)
* [SCDs (8)](https://en.wikipedia.org/wiki/Slowly_changing_dimension)
  - [SCD0](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-0): no change, original only.
  - [SCD1](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-1): overwrite, last version, current only.
  - [SCD2](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-2): history (eff_from + eff_to + current_fl), add new row.
  - [SCD3](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-3): previous-current. no history. add new attribute.
  - [SCD4](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-4-mini-dimension): history table, add mini-dimension. (SCD1+SCD2)
  - [SCD5](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-5): SCD4+1: mini-dimension + type 1 outrigger.
  - [SCD6](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-6): SCD1+2+3 + from-to-current_fl. (SCD3 with history)
  - [SCD7](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-7): dual type 1 and type 2 dimensions.
* Normalization (11)
  - 0NF
  - 1NF
  - 2NF
  - 3NF
  - EKNF
  - BCNF
  - 4NF
  - ETNF
  - 5NF
  - DKNF
  - 6NF
* [Edgar F. Codd's 12 rules](https://en.wikipedia.org/wiki/Codd%27s_12_rules)
* Kimball (+ load patterns)
  - [Fact](https://en.wikipedia.org/wiki/Data_warehouse#Facts)
  - [Dimension](https://en.wikipedia.org/wiki/Dimension_(data_warehouse))
  - [Measure](https://en.wikipedia.org/wiki/Measure_(data_warehouse))
* Inmon (+ load patterns)
* [DV2.0](https://en.wikipedia.org/wiki/Data_vault_modeling) (+ load patterns)
* Anchor Modeling (+ load patterns)
* Star Schema (+ load patterns)
* Snowflake Schema (+ load patterns)
* [ACID](https://en.wikipedia.org/wiki/ACID)
* [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem)
* [Armstrong's axioms](https://en.wikipedia.org/wiki/Armstrong%27s_axioms)
* [Functional Dependency](https://en.wikipedia.org/wiki/Functional_dependency)
* [13 Base relations of James F. Allen's Interval Algebra in 1983](https://en.wikipedia.org/wiki/Allen%27s_interval_algebra#Relations)
* SQL Standards (ANSI 86 -> 16)
* DML, DCL, DDL, TCL.
* Conceptual Data Model
* Logical Data Model
* Physical Data Model
* Data Type Coercion (table of type casting)
* Joe Celko's Nested Set Model
* [SQL Server SQL Query Processing Order](https://blog.sqlauthority.com/2009/04/06/sql-server-logical-query-processing-phases-order-of-statement-execution/)
  - FROM
  - ON
  - OUTER
  - WHERE
  - GROUP BY
  - CUBE | ROLLUP
  - HAVING
  - SELECT
  - DISTINCT
  - ORDER BY
  - TOP
* COALESCE vs ISNULL.
* [MERGE](https://en.wikipedia.org/wiki/Merge_(SQL))
* Stored Procedure (SP) vs User-defined Function (UDF).
* Replication (propagate the logs) vs Duplication (copy data).
* Centralized vs Decentralized vs Distributed network.
* Vertical partitioning vs Horizontal partitioning vs Sharding.
* OLTP vs OLAP.
* [SQL JOINs](https://www.mssqltips.com/sqlservertip/1667/sql-server-join-example/) (INNER, LEFT, RIGHT, FULL, CROSS, SELF, SEMI, ANTI SEMI, STAR, CROSS APPLY, OUTER APPLY, INNER APPLY.)
![SQL Joins Picture](https://upload.wikimedia.org/wikipedia/commons/9/9d/SQL_Joins.svg)
* [SQL JOIN HINTS](https://www.mssqltips.com/sqlservertip/2917/sql-server-join-hints/)
  - [NESTED LOOP JOIN (NLJ)](https://en.wikipedia.org/wiki/Nested_loop_join) (efficient for small table on left side of join)
  - [HASH JOIN](https://en.wikipedia.org/wiki/Hash_join) (better than LOOP JOIN on large datasets but requires an equi-join)
  - REMOTE JOIN (efficient for geographically distant datasets. Only for INNER JOINs.)
  - [SORT-MERGE JOIN (SMJ)](https://en.wikipedia.org/wiki/Sort-merge_join) (efficient for well-indexed table. No memory reallocation and good for parallel execution.)
  - [SYMMETRIC HASH JOIN (SHJ)](https://en.wikipedia.org/wiki/Symmetric_hash_join)
  - [BLOCK NESTED LOOP (BNL)](https://en.wikipedia.org/wiki/Block_nested_loop)
* MySQL Straight_JOIN (forces to read the tables in the order listed in the query).
* Keys
  - Primary Key
  - Foreign Key
  - Natural Key
  - Durable Key
  - Business Key
  - Surrogate Key
  - Smart Key
  - Hash Key
  - Composite Key
  - Candidate Key
  - Alternate Key
  - Unique Key
  - Super Key
  - ...
* Early-Arriving Fact (EAF)
* Late-Arriving Dimension (LAD) (dummy values: "-1" for IDs and NULLs for attributes)
* [Block Range Indexes (BRIN)](https://en.wikipedia.org/wiki/Block_Range_Index)
* [Distributed Hash Tables (DHTs)](https://en.wikipedia.org/wiki/Distributed_hash_table) (e.g. Cassandra, Riak, Voldemort.)
* Index types:
  - Clustered (CI)
  - Non-Clustered (NCI)
  - Unique (UI)
  - Filtered (FI)
  - Columnstore (CSI)
  - Hash
  - Memory-optimized Non-Clustered
* [Data Lineage](https://en.wikipedia.org/wiki/Data_lineage)
* What is considered as a "large" table?
  - It's relative. (think 1 bit clustered indexed column table vs 50 varchar(max) columns with lots of un-indexed queries)
  - How many columns, what data types?
  - How many indexes?
  - What is the actual size of the table? (i.e. number of pages. see sys.dm_db_partition_stats)
  - What are the queries run against it?
  - In-memory indexes or clustered index scans?
  - How much memory on the machine?
  - This is why SQL Server doesn't document a maximum of rows.
