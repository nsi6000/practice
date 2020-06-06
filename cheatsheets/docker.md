# Docker
<https://docs.docker.com/>

* docker --version
* docker --help
* docker run hello-world
* docker pull <user_name>/<image_name>:<tag_name>
* docker image ls
* docker images
* docker ps
* docker ps -a
* docker rm -f <container_id>
* docker rmi <image_id>
* docker run (-d) (--rm) (-it) (--name <container_name>) (-p <port_number>:<port_number>) <image_name>:<tag_name>|<image_id>
* docker exec -it <container_name> <command>
* docker image inspect <image_name>:<tag_name>|<image_id>
* docker start (-i) <container_name>|<container_id>
* docker stop <container_name>|<container_id>
* docker-compose up
* docker-compose down
* docker network ls
* docker network create <network_name>
* docker volume ls
* docker volume create <volume_name>
* docker volume inspect <volume_name>
* docker image build (-t <image_name>:<tag_name>) .
* docker save <image_name> > <iamge_name>.tar //backup image.
* cat <image_name>.tar | docker load //restore image.


# Dockerfile

* FROM <image_name>:<tag_name>
* WORKDIR <path>
* COPY <from_path> <to_path>
* RUN <command>
* EXPOSE <port_number>
* [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
* [Builder Pattern / Multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/)


# Docker images

## Operating Systems
* alpine
* ubuntu
* debian
* debian:jessie
* debian:jessie-slim
* debian:sid
* debian:sid-slim
* debian:stable
* debian:stable-slim
* fedora
* fedora:30
* opensuse
* archlinux
* sourcemage
* mageia
* clearlinux
* sl
* sl:6
* crux
* kalilinux/kali
* kalilinux/kali-rolling

## Databases
* mongo
* cassandra
* scylladb/scylla
* puckel/docker-airflow
* prefecthq/prefect
* altibase/altibase
* couchbase
* postgres
* redis
* mysql
* mariadb
* crate
* percona
* neo4j
* rethinkdb
* arangodb
* orientdb
* monetdb/monetdb
* dgraph/dgraph
* cockroachdb/cockroach
* voltdb/voltdb-community
* apache/incubator-druid
* alluxio/alluxio-presto-sandbox //https://www.alluxio.io/blog/getting-started-with-the-alluxio-presto-sandbox/
* docker run -d -p 14022:22 -p 9000:9000 -p 14240:14240 --name tigergraph_dev --ulimit nofile=1000000:1000000 -v ~/data:/home/tigergraph/mydata -t docker.tigergraph.com/tigergraph-dev:latest //https://github.com/tigergraph/ecosys/tree/master/demos/guru_scripts/docker



## Programming languages
* python
* golang
* gcc
* hylang
* haskell
* julia
* fsharp
* node
* clojure
* erlang
* elixir
* openjdk
* rust
* mono
* swift
* r-base
* nimlang/nim
* crystallang/crystal



