# Kafka


## KSQLDB:
* create stream
* data-gen
* stream manipulation/transformation
* KSQL tables
* KSQL joins
* pull queries
* KSQL Connect with Postgresql
* CSV / JSON / Nested JSON (->) / AVRO.
* Rekeying a table
* Repartitioning a stream
* Merging streams (CSAS + INSERT into stream 1)
* Windowing (Tumbling, Hopping, Session)
* Geospatial
* Create and Use UDF/UDAF (Jar file + publish on Ext/ + list functions;)
* EXPLAIN PLAN
* Test-runner: inputs-outputs-KSQL script. + | grep '>>>'.




## Kafka Streams:
* Kafka Stream 101 - WordCount app
* Kafka Stream 102 - FavoriteColour app
* Kafka Stream 103 - BankBalance app
* Kafka Stream Topology
* Build and deploy FatJar of Kafka Stream
* KStreams (all INSERTs) (for topic that's compacted, transactional)
* KTables (all UPSERTs) (for aggregations, "database table"-like)
* Stateless (multiply by 2) vs Stateful (word count).
* Operation		for KStream		for KTable		affect Key		affect Value
* Stateless
* =========
* MapValues			X				X				-				X
* Map					X				-				X				X
* Filter/FilterNot	X				X				-				-
* FlatMapValues		X				-				-				?
* FlatMap				X				-				X				?
* Branch				X				?				?				?
* SelectKey			X				?				X				-
* Read a topic as a KStream, KTable or GlobalKTable. (builder.stream/table/globalTable)
* To vs Through operations (write to a topic)
* Log Compaction (keep current data, deletes old data.) (--config cleanup.policy=compact)
* Transforming a "KStream to a KTable" (2 ways: groupBy + Aggregation, stream.to() + builder.table().) and "KTable to a KStream" (table.toStream()).
* 
* Stateful
* ========
* GroupBy				X				X				X				?	=> generates a KGroupedStream/KGroupedTable.
* Aggregate
* Reduce
* Peek
* Transform/TransformValues
* 
* => Stateful Transformations diagram in Confluent's documentation.
* 
* Exactly Once Semantics. (thanks to idempotency and transactions.)
* 	(ProducerConfig.ACKS_CONFIG = "all", ENABLE_IDEMPOTENCE_CONFIG, "true")
* 	config.put(StreamsConfig.PROCESSING_GUARANTEE_CONFIG, StreamsConfig.EXACTLY_ONCE);
* 
* Kafka Streams JOINs. (INNER, LEFT, OUTER.)
* JOINs Co-partitioning of data.




## Kafka Connect:
* Kafka Connect Architecture (with Sources, Sinks, Kafka Connect Workers.)
* Tasks are executed by workers and composed of the Connector + the User Configuration.
* Use Landoop Dockerfile Compose with the Landoop UI.
* Get logs from Kafka.
* Use the FileStream Source Connector.
* Standalone mode:
* 	Edit the worker.properties file.
* 	Edit the <your-porject>.properties file.
* 	> create a topic -rf 1 -partitions 3
* 	> connect-standalone worker.properties file-stream-demo-standalone.propreties
* 	> => see "INFO Connector Created" in the logs.
* 	> Edit the file with some text.
* 	> Save it.
* 	> Read the topic and see your text added.
* Cluster mode:
* 	Edit the worker.properties file.
* 	Edit the <your-porject>.properties file.
* 	> create a topic -rf 1 -partitions 3
* 	> Open the Kafka Connect UI in Landoop UI.
* 	> Add <your-project>.properties via the Kafka Connect UI. > Add & Validate button.
* 	> create file.
* 	> edit file.
* 	> see the changes in the topic.
* 
* Find Kafka Connectors:			confluent.io/hub/
* 	confluent-hub install <connector-name>


## Kafka Schema Registry:
* Avro vs CSV vs JSON (pros - cons)
* 3 ways to Generate an Avro:
* 	Generic Record (not good because no type safety and runtime error.)
* 	Specific Record (maven import which generate Java code and methods from the Avro (eg. getAge). Good because it provides type safety and compile time error.)
* 	Reflection (from a POJO)
* 4 types of Schema Evolution
* 	Backward
* 	Forward
* 	Full
* 	Breaking
* 6 Best Practices for Avro
* 	add/remove fields with defaults. => ALWAYS give default values.
* 	don't change ENUMs.
* 	don't change data type.
* 	don't change name/rename fields, use Aliases instead.
* 	never delete a required field.
* 	make your primary key required.
* When reading with an old schema, Avro IGNORES new fields.
