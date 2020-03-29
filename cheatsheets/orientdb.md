# OrientDB
https://orientdb.com/docs/last/index.html

* bin/server.sh //run the server.
* bin/dserver.sh //run the server decentralized.
* bin/console.sh //run the console.
* default port: 2480.
* ACID-compliant. Supports transactions.


# Commands

* SELECT * FROM Person WHERE name LIKE 'Luk%' ORDER BY @rid DESC SKIP 5 LIMIT 10
* INSERT INTO Person (name, surname) VALUES ('Jay', 'Miner')
* INSERT INTO Person CONTENT {"name":"Jay", "surname":"Miner"}
* INSERT INTO Person FROM SELECT * FROM People
* UPDATE Person SET name = 'Luka' WHERE name IS NULL
* DELETE FROM Person WHERE name = 'Luka'
* CREATE FUNCTION <function_name> <function_javascript_code>
	* CREATE FUNCTION test "return a+b;" PARAMETERS [a,b]
* CREATE FUNCTION <function_name> <function_sql_code> LANGUAGE SQL

# Concepts

* Document
* Vertex
* Edge
* Record ID
* Class
* Abstract Class
* Cluster
* Function
* Relationship
* Links
	* There are no relational JOINs in OrientDB. It uses the "dot notation".
* SB-Tree Index
* Hash Index
* Auto Sharding Index
* Lucene Full Text Index
* Lucene Spatial Index

