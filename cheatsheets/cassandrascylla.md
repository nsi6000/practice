# Cassandra / ScyllaDB
## Websites
* <https://github.com/apache/cassandra>
* <https://github.com/scylladb/scylla>
* <https://github.com/rishinair21/awesome-cassandra>
* <https://www.datastax.com/>
* <https://www.scylladb.com/>

## Commands
* abc

## Concepts
* Keyspace ~= schema
* Table
* Partition
* PK = Primary Key = partition key + clustering columns (CCs).
* Partition Key
  *	The Partition Key cannot be undefined.
  *	There can be multiple columns as Partition Key.
* CC = Clustering Columns = how Cassandra sorts data within each partition.
  *	CC values are stored sorted.
  *	The CCs can be undefined.
  *	There can be multiple columns as CC.
  *	If there is more than one column as CCs, the order of these columns defines the clustering order.
* Collections = multi-valued columns. (Data type:= set<text> || list<text> || map<timestamp, text>)
* UDTs = user-defined type.
* COUNTER data type = store a 64-bit signed inter that can increment or decrement with UPDATE statement.
* UDFs = user-defined functions.
* UDAs = user-defined aggregates.
* Data Modeling := CDM + AccessPatterns + LDM + PDM. Know your data, know your queries.
* CDM -> ERM := Entities(Strong vs Weak) + Relationships(Cardinality := 1:1, 1:N, M:N.) + Attributes.
* LDM -> (Artem) Chebotko Diagram.
* Nesting Data := CCs + Collections + UDTs.
* Cassandra joins on Write (and not on Read) and therefore generates Data Duplication.
* 5 Mapping Rules:
  *	1) Entities and Relationships.
  *	2) Equality search attributes.
  *	3) Inequality Search attributes.
  *	4) Ordering attributes.
  *	5) Key attributes.
* Loading Data Methods:
  *	1) COPY FROM/TO command.
  *	2) SSTable Loader. (cmd: sstableloader)
  *	3) DSE Bulk Loader. (cmd: dsbulk)
* Batch Log as Write Technique. (BEGIN BATCH ... APPLY BATCH;)
* Compare and Set (CAS) as a Lightweight Transaction (LWT) Technique. (INSERT/UPDATE/DELETE ... IF NOT EXISTS.)
* SI = Secondary Index
  *	Uses cases: indexing.
  *	In ScyllaDB, SI is built on MV.
* MV = Materialized View
  *	Uses cases: different sort ordering, indexing, denormalization and filtering.
  *	Updates on MVs are always async.
  *	A PK of a MV must contain all columns from the PK of the base table.
  *	A PK of a MV can contain at most one other column.
  *	WHERE filtering should be on columns not part of the base table's PK.
* Split with an Artificial Column
* Split with an Artificial Bucket (manually set: max interactions of 1000. -> even size partitions.)
* Split vertically the table.
* Safe Data Model Changes:
  * Execute one CREATE/DROP statement at a time.
  * Allow time to propagate through the cluster.
  * Verify completion via nodetool describecluster.
  * Then perform the next CREATE/DROP command.
* A Partitioner hashes the partition key values to create a partition token.
* You can't change your PK without redoing the Data Model.
* Unlike RDBMS, there is no incremental value in Cassandra as it is a difficult thing to implement in a Distributed Database.
* Every query should have a Partition Key. Otherwis you do a random search on the cluster.
* SELECT * FROM Users; is a very bad query since it triggers a Random Scan on the cluster.
* A Node runs on a server or VM, on cloud or on premises. Don't run it on a SAN/NAS! Max 2 to 4 Tb of data per Node.
*	bin/nodetool
    - help
    - info
    - status
    - stopdaemon
    - getendpoints
    - flush
*	A Node has 4 statuses:	Joining.	Leaving.	Up.		Down.
* The Ring is Cassandra's Cluster.
* Token Range: set of values within the Node. It is a BigInt (2e63).
* Coordinator: ...
* Partitioner: responsible for Token Value distribution within the Ring.
* TokenAwarePolicy: The Driver is locally aware of the Token Range and suppress the need for the Coordinator.
* VNode: a virtual node. If num_tokens is greater than 1 in cassandra.yaml, you use VNodes. By default, you have 128 VNodes per Node. (256 in ScyllaDB)
* Gossip: spreading of informations within the Ring between Nodes in a Polynomial fashion. Initiated every second. Picks 1 to 3 Nodes to gossip with.
  *	It's the Inter-node Communication Protocol. Decentralized, no SPOF.
  *	SYN -> ACK -> ACK2.
* Cluster Metadata:
*	Endpoint (EP) State:
  *	Heartbeat (HB) State: generation:HeartbeatNumber (100:20)
    *	generation=5
    *	version=22
    *	Application State:
  *	STATUS=BOOTSTRAP|NORMAL|LEAVING|LEFT|REMOVING|REMOVED|???
    *	DC=west
    *	RACK=rack1
    *	SCHEMA=2d2c...
    *	LOAD=100.0
    *	SEVERITY=0.75
    *	...
* Snitch: declare a Node's rack and DC. Multiple Types:
  *	SimpleSnitch: hardcoded rack1, DC1.
  *	PropertyFileSnitch: get topology from cassandra-topology.properties file. Must maintain and each Node and keep them in sync.
  *	GossipingPropertyFileSnitch: No need to copy properties like in PFS. cassandra-rackdc.properties file.
  *	Cloud-based Snitches: specific Snitches for each vendors. (AWS, GCP, Rackspace,...)
  *	Dynamic Snitch: Turned on by default. Maintains a pulse on Node's performance. Layered on top of your actual Snitches.
*	=> ALL NODES MUST HAVE THE SAME SNITCHES! Otherwise you'll have an inconsistent state.
* Partition Summary: stores byte offsets into the partition index.
* Key Cache: stores the byte offset of the most recently accessed records.
* Hinted Handoff: replay of missing data if a machine is down when it goes back up. Default time: 3 hours.
 * Careful with CL=ANY, reply success while Nodes don't have (yet) the data. (hinted handoff)
 * Even more dangerous, if the Hint window expires before the Node come back to life, the Coordinator will delete your write.
* Consistency Level:
	- consistency per query.
	- ALL, QUORUM (50%+, for RF=3, it's 2.) | LOCAL_QUORUM (use only local DC to minimize latency), ONE | LOCAL_ONE.
	- How many replicas do I need to hear that R/W before that R/W is considered successful.
* The Write Path: writes -> any node (coordinator) -> commit log (append-only, immutable, stored sequentially, on HDD.) -> memtable (stored by partition key, on RAM.) -flushed to disk + delete the commit log (not needed anymore)-> sstable (immutable file on disk, sorted by partition key).
  * Every write gets a timestamp.
* Tombstone: delete is a special type of write.
* sstable compaction: merging of sstables and keep only last timestamp.
* The Read Path: query any server -> contact node with the requested key -> on each node, data is pulled from sstable and merged.
  * IF CL = ALL, perform a read_repair.
  * If CL < ALL, perform read_repair_chance in the background.
* Read Repair: compare all Nodes data/checksum. If they don't match, send back the latest data on each node based on latest timestamp.
* RF = Replication Factor = RF is set per keyspace.
* (Master-Slave) Replication: data is replicated asyncroniously. -> Replication lag.
* Sharding. (no joins, no aggregations.)
* Master failover.
* Hash Ring:
	- no MSR. No Replica Sets.
	- no ZooKeeper.
	- RF=N servers.

## ScyllaDB specifics
* Scylla has a ring type architecture
* It’s a distributed, highly available, high performance, low maintenance, highly scalable NoSQL database
* In Scylla all nodes are created equal, there are no master/slave nodes
* Data is automatically distributed and replicated on the cluster according to the replication strategy
* Scylla supports multiple data centers
* Scylla transparently partitions data by using the hash values of keys
* Large partitions are best avoided. They can be tracked using the system.large_partitions table.



