# Redpanda

curl -1sLf 'https://packages.vectorized.io/nzc4ZYQK3WRGd9sy/redpanda/cfg/setup/bash.deb.sh' | sudo -E bash
sudo apt install redpanda -y
sudo systemctl start redpanda
sudo systemctl status redpanda
rpk topic create twitch_chat
rpk topic produce twitch_chat
> Hello
> World
CTRL+C
rpk topic consume twitch_chat
rpk topic list
rpk topic list --detailed
*********
rpk topic produce --help
rpk topic consume --help
rpk topic create song_plays song_likes --partitions 6 --replicas 1
rpk topic describe song_plays
rpk topic alter-config song_plays --set retention.ms=259200000
rpk topic describe song_plays -c #limit output to only the configuration.
rpk topic add-partitions song_plays -n6
rpk topic describe song_plays -s #limit output to only the partition count.
rpk topic produce song_likes --format "%k|%v\n"
rpk topic consume song_likes --offset 1
rpk topic consume song_likes --offset start
rpk topic consume song_likes --offset end
rpk topic consume song_likes --offset start --format "%k\n"
rpk topic consume song_likes --offset start --num 1 #consume a specific number of records.
rpk topic consume song_likes --partitions 4 #consume data from a particular partition.
*** Consumer Groups
rpk topic consume song_likes --offset start --num 1 --group groupA
rpk topic consume song_likes --offset start --num 1 --group groupB
rpk group list
rpk group describe groupA
rpk topic consume song_likes --group groupA
rpk group seek groupA --to start
rpk group seek groupA --to start --topics song_likes
rpk group delete groupB
#rpk group seek groupA --to $(date --date 'now - 5 minutes')
rpk topic delete song_likes
rpk topic delete --regex "^song.*"

#Java Client
java --version
mvn --version
rpk topic create greetings --partitions 4 --replicas 1
export REDPANDA_BROKERS="127.0.0.1:9092"
mvn archetype:generate \
    -DgroupId=com.example \
    -DartifactId=java-tutorial \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DarchetypeVersion=1.4 \
    -DinteractiveMode=false
cd java-tutorial/
Add in pom.xml:
<dependencies>
    <dependency>
      <groupId>org.apache.kafka</groupId>
      <artifactId>kafka-clients</artifactId>
      <version>3.2.0</version>
    </dependency>
    <!-- other dependencies -->
</dependencies>
mvn clean #test the pom.xml file is correct.
mvn package
=> copy ProducerExample.java from Github.
mvn package && mvn exec:java -Dexec.mainClass="com.example.ProducerExample"
==> if Java NullPointerException, check that the Environment is correctly set.
==> Should see "Produced record: Hello World" in the build output.
=> copy ConsumerExample.java from Github.
mvn package && mvn exec:java -Dexec.mainClass="com.example.ConsumerExample"
==> Should see "Consumed record: Hello World" in the build output.
CTRL+C

Python Client:
==============
python3 --version
pip3 --version
mkdir python-tutorial && cd python-tutorial
sudo apt install python3.8-venv
python3 -m venv .
source bin/activate
pip3 install kafka-python
nano producer.py
=> copy producer.py from Github repo.
python3 producer.py
=> "Successfully produced message to topic: greetings"
rpk topic consume greetings --offset start
nano consumer.py
=> copy consumer.py from Github repo.
python3 consumer.py
=> "Consumed record: Hello World!"
CTRL+C


