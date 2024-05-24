# Rename file to simply 'Dockerfile'.
# On Debian, apt-get install podman.
# podman build -t dev .
FROM debian:latest as codeforces

WORKDIR /home/

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y bash
RUN apt-get install -y vim
RUN apt-get install -y openjdk-17-jdk

COPY ./.vimrc .
