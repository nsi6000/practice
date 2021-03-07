FROM debian:buster
#docker image build -t nsi6000:latest .
#docker run -it --name nsi6000 nsi6000 bash

WORKDIR /github

COPY . /local

#Tools
RUN apt-get update
RUN apt-get install -y bash
RUN apt-get install -y vim
RUN apt-get install -y git
RUN apt-get install -y wget

#Clone git repos
RUN git clone https://github.com/nsi6000/practice.git
RUN git clone https://github.com/nsi6000/stacks.git

#C
RUN apt-get install -y gcc #compile linux kernel.
RUN apt-get install -y libc-dev #required to compile with GCC.
RUN apt-get install -y binutils #compile linux kernel.
RUN apt-get install -y make #compile linux kernel.
RUN apt-get install -y gdb
RUN apt-get install -y cppcheck #cppcheck <file>|<path>
RUN apt-get install -y indent #indent -kr|-linux <file>

#Python
RUN apt-get install -y python3
RUN apt-get install -y python3-pip #pip
RUN pip3 install Faker #faker
RUN pip3 install pylint #Linter
RUN pip3 install pytest
RUN pip3 install flake8 #Linter

#Ports
EXPOSE 5000
EXPOSE 4040

# Define environment variable
ENV NAME World

# Run app.py when the container launches
#CMD ["python", "app.py"]


#Spark
ENV SPARK_VERSION=3.0.2
ENV HADOOP_VERSION=3.2

RUN apt-get install -y openjdk-11-jre
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark
RUN rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz


#wget https://downloads.apache.org/cassandra/3.11.10/apache-cassandra-3.11.10-bin.tar.gz
#tar -xvzf apache-cassandra-3.11.10-bin.tar.gz
#rm apache-cassandra-3.11.10-bin.tar.gz
#
#wget https://dist.neo4j.org/deb/neo4j_4.2.3_all.deb
#dpkg -i neo4j_4.2.3_all.deb
#
#wget https://s3.us-east-2.amazonaws.com/orientdb3/releases/3.1.9/orientdb-3.1.9.tar.gz
#tar -xvzf orientdb-3.1.9.tar.gz
#rm orientdb-3.1.9.tar.gz
#orientdb-3.1.9/bin/dserver.sh
