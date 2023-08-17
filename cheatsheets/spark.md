# Spark
* https://spark.apache.org/
* docker run -it --name spark_dev -p 8080:8080 -p 7077:7077 bde2020/spark-master:3.0.0-hadoop3.2 bash
```sh
/spark/bin/spark-shell -i test.scala
/spark/bin/spark-shell
:help
:load test.scala
import org.apache.spark.sql.SparkSession
val sc = SparkSession.builder().config("spark.master","local").getOrCreate()
val cars = sc.read.option("header","true").csv("abc.csv")
cars.write.format("csv").option("header","true").save("./cars.csv")
cars.write.format("json").save("./cars.json")
cars.write.save("./cars.parquet")
cars.show()
cars.take(3).foreach(println)
...
```

## Concepts
* Data Sources API
* Low Level APIs (Spark Core Execution Engine):
  - RDDs
  - DStreams
  - Distributed Variables
* High Levels APIs:
  - DataFrames
  - DataSets
  - SQL
  - Spark Streaming (DataFrames + DataSets)
  - MLlib (LinearRegression, LogisticRegression, KMeans, PCA)
  - GraphX
  - SparkR

![Spark API](https://databricks.com/wp-content/uploads/2016/06/Apache-Spark-Components-Diagram.gif)

* Event Time Windows
* Processing Time Windows
* Watermarking



## Spark basics:
* Spark Architecture
* spark session builder
* Data frames: group by, aggregates, missing data, dates and timestamps.
* data sources
* DF: columns+alias, expressions, aggregations, joins.
* Spark Data Types
* NULLs
* Data Sets
* Spark SQL
* RDDs

## Spark Streaming:
* Streaming data frames
* Streaming aggregations
* Streaming joins
* Streaming data sets
* DStreams
* DStreams transformations
* Integration with Kafka
* Integration with PostgreSQL
* Integration with Cassandra
* Event time windows
* Processing time windows
* Watermarking


## Spark 101
```scala
val email = sc.textFile("test.txt")
sc
val words = email.flapMap { line => line.split("\\s") }
words.take(5)
words.count

val words = "this is a test.".split(" ")
val wordsRDD = sc.parallelize(words)
//val wordsRDD = sc.parallelize(List("quick", "brown", "quick", "dog"))
//wordsRDD.countByValue
val wordLengths = wordsRDD.map { _.length }
wordLengths.collect

filteredWords.toDebugString

//Transformations (lazy) vs Actions (non-lazy -> execute)

words.persist // -> MEMORY_ONLY (default)

import org.apache.spark.storage.StorageLevel
words.persist(StorageLevel.MEMORY_AND_DISK)
```

