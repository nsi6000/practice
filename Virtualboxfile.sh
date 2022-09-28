# Virtual Box Setup
# debian-10.8.0-i386-netinst.iso
su
apt-get update
apt-get install -y bash vim git wget gcc
git clone https://github.com/nsi6000/practice.git

## Python
apt-get install -y python3 python3-pip
python3
	print("Hello Python")
	quit()
pip3 install apache-airflow
pip3 install pandas
pip3 install numpy

## Java Scala Spark
apt-get install -y openjdk-11-jre
export SPARK_VERSION=3.0.2
export HADOOP_VERSION=3.2
wget https://archive.apache.org/dist/spark/spark-3.0.2/spark-3.0.2-bin-hadoop3.2.tgz
mkdir spark
cd spark
tar -xzvf spark-3.0.2-bin-hadoop3.2.tgz
./spark-3.0.2-bin-hadoop3.2/bin/spark-shell
	println("Hello spark!")
	:q
apt-get install -y scala
scala
	println("Hello Scala!")
	:q

## Java
apt-get install -y openjdk-11-jdk
vim helloworld.java
´´´java
class HelloWorld {
	public static void main(String[] args){
		System.out.println("Hello Java!");
	}
}
´´´
javac helloworld.java
java HelloWorld


## Check versions
python3 --version
pip3 --version
pip3 list | grep numpy
pip3 list | grep pandas
java --version
scala -version #single-dash
spark-shell --version


wget https://neo4j.com/artifact.php?name=neo4j-community-4.2.4-unix.tar.gz
tar -xzvf artifact.php\?name\=neo4j-community-4.2.4-unix.tar.gz
neo4j-community-4.2.4/bin/neo4j start





# NEW
* ssh -i <path-to-key>.pem <user>@<IP-address>

sudo apt-get update
sudo apt-get install
	python3
	vim
	git
	wget
	scala
	python3-pip
	openjdk-11-jre
	redis
	maven
pip3 install
	autopep8
	pytest
	Faker
	bandit
	vulture
	pyspark
	pyflink
	cassandra-driver
	confluent-kafka
	redis
	<postgres ???>
	<akka ???>
pip3 list

autoflake
isort
pyformat
pylint
pycodestyle
black
docstrings + sphinx
pipenv + poetry
behave


scalafmt
scalafix
scalastyle
scalatest	unit testing
scalamock	mocking
scalacheck	property based testing
scalactic.org
JUnit
TestNG



=> pre-commit.org

VERSIONS:
=========
python3 --version
java -version
scala -version
pip3 --version
git --version
vim --version
wget --version
redis-server --version
~/sbt/sbt/bin/sbt version
mvn --version

cassandra version
kafka version
spark version
flink version
postgres version
akka version
redpanda version


+ KSLDB.
+ Confluent Schema Registry.


## Maven basics:
mvn clean install
mvn clean install -DskipTests
mvn -X clean install
mvn help:effective-pom -Doutput=filename.xml
mvn dependency:tree
mvn archetype:generate

multi-module mavenproject (<modules><module>)

+ run unit tests
+ compile / test / build / ... ?



## MICROK8S
* sudo snap install microk8s --classic
* microk8s enable dns dashboard storage
* microk8s disable dns dashboard storage
* microk8s enable istio
* sudo microk8s status
* sudo microk8s kubectl create deployment microbot --image=dontrebootme/microbot:v1
* sudo microk8s kubectl scale deployment microbot --replicas=2
* sudo microk8s kubectl expose deployment microbot --type=NodePort --port=80 --name=microbot-service
* sudo microk8s kubectl get all --all-namespaces
* microk8s status: Provides an overview of the MicroK8s state (running / not running) as well as the set of enabled addons
* microk8s enable: Enables an addon
* microk8s disable: Disables an addon
* microk8s kubectl: Interact with kubernetes
* microk8s config: Shows the kubernetes config file
* microk8s istioctl: Interact with the istio services; needs the istio addon to be enabled
* microk8s inspect: Performs a quick inspection of the MicroK8s intallation
* microk8s reset: Resets the infrastructure to a clean state
* microk8s stop: Stops all kubernetes services
* microk8s start: Starts MicroK8s after it is being stopped

## SBT+AKKA
mkdir sbt
wget https://github.com/sbt/sbt/releases/download/v1.7.1/sbt-1.7.1.tgz
tar xzvf
~/sbt/sbt/bin/sbt new sbt/scala-seed.g8
	....
	Minimum Scala build.
	name [My Something Project]: hello
	Template applied in ./hello
cd hello

../sbt
(takes some time...)
sbt:hello> help
CTRL+D or exit


add to build.sbt file, at the end.
	val AkkaVersion = "2.5.13"
	libraryDependencies += "com.typesafe.akka" %% "akka-actor" % AkkaVersion
sbt compile
	[success]


vim src/main/scala/example/Hello.scala
	package example
	object Hello extends App {
		println("Hello World")
	}
scalac example/Hello.scala
scala example.Hello
> Hello World


vim src/main/scala/example/Hello.scala
	package example
	import akka.actor.{Actor, ActorSystem, Props}
	object Hello extends App {
		class SimpleActor extends Actor {
			override def receive: Receive = {
				case message => println(s"I received the message: $message")
			}
		}
		val system = ActorSystem("AkkaTest")
		val actor = system.actorOf(Props[SimpleActor], "simpleActor")
		actor ! "hello 1"
	}
~/sbt/sbt/bin/sbt run

rm -R akkaTest target

## SPARK
wget https://archive.apache.org/dist/spark/spark-3.0.2/spark-3.0.2-bin-hadoop3.2.tgz
bin/spark-shell
> :help
> println("test")
vim spark.scala
	println("test2")
vim spark.scala
	val myDF = spark.read.option("inferSchema", "true").option("header", "true").csv("/home/azureuser/test.csv")
	myDF.show()
bin/spark-shell < spark.scala
OR
bin/spark-shell
> :load /home/azureuser/spark.scala
> myDF.select("quantity","name").show()
> myDF.select("quantity","name").filter(col("name") === "B").show()
> myDF.select("quantity","name").filter(col("name") =!= "B" and col("quantity") > 5).show()
> myDF.select("name").distinct().show()
> myDF.select(count("*")).show()
> myDF.select(countDistinct("name")).show()
> myDF.select(sum(col("quantity"))).show()
> myDF.select(avg(col("quantity"))).show()
> myDF.groupBy(col("name")).sum("quantity").show()
> myDF.groupBy(col("name")).agg(sum("quantity").as("TotalSum")).orderBy(col("TotalSum").desc_nulls_last).show()
> val newDF = spark.createDataFrame(Seq(("A","Alice"),("B","Bob"),("C","Charlie")))
> newDF.show()
> val myResult = myDF.join(newDF, myDF.col("name") === newDF.col("_1"), "inner")
> myResult.show()
> val finalDF = myResult.select(col("_2").as("Name"), col("quantity").as("Quantity"))
> finalDF.orderBy(col("Quantity").desc).show() //or sort instead of orderBy.

Streaming: (open second terminal screen)
> import org.apache.spark.sql.DataFrame
> val lines: DataFrame = spark.readStream.format("socket").option("host", "localhost").option("port", 12345).load()
> lines.writeStream.format("console").outputMode("append").start().awaitTermination()

## POSTGRESQL
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql.service
sudo -i -u postgres
psql
	OR   sudo -u postgres psql
select 1;
CTRL-D
CTRL-D (to get back to azureuser)

## KAFKA
wget https://dlcdn.apache.org/kafka/3.2.0/kafka_2.13-3.2.0.tgz
tar xzvf
bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties &
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
> write some stuff
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
CTRL-C
ps
pkill <java1>
pkill <java2>


bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2 --topic word-count-input
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2 --topic word-count-output
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
git clone https://github.com/simplesteph/kafka-streams-course.git
mvn validate
mvn package
	https://mvnrepository.com/
java -jar target/word-count-....jar
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic word-count-input
> hello world
> hello test
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic word-count-output --from-beginning --formatter kafka.tools.DefaultMessageFormatter --property print.key=true --property print.value=true --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer --property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer

## FLINK
wget https://dlcdn.apache.org/flink/flink-1.15.1/flink-1.15.1-bin-scala_2.12.tgz
tar xzvf
./bin/start-cluster.sh
./bin/flink run examples/streaming/WordCount.jar
tail log/flink-*-taskexecutor-*.out
./bin/stop-cluster.sh


## CASSANDRA
wget https://dlcdn.apache.org/cassandra/4.0.4/apache-cassandra-4.0.4-bin.tar.gz
sha256sum <file> / md5sum
tar xvzf
./bin/cassandra &
./bin/cqlsh
show version;
show host;
CTRL-D



## TODO:
* airflow
* flask
* django
* neo4j + driver
* mysql/mariadb + dr
* monetdb + driver
* mongodb + dr
* influxdb + driver + TICK
* ELK
* memcached
* Drill
* Druid
* Beam
* Storm
* Heron
* Twister2
* Nemo

* ruby
* perl
* php
* golang
* rust
* gcc / clang-llvm
* haskell


+ CICD (github actions / gitlab)




