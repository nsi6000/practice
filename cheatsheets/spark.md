# Spark
* https://spark.apache.org/
* docker run -it --name spark_dev -p 8080:8080 -p 7077:7077 bde2020/spark-master:3.0.0-hadoop3.2 bash
```sh
/spark/bin/spark-shell -i test.scala
/spark/bin/spark-shell
:help
:load test.scala
val cars = sc.read.schema("").csv("abc.csv")
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

