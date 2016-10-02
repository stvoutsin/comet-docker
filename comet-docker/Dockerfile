FROM ubuntu:14.04
MAINTAINER Stelios Voutsinas <stv@roe.a.uk>

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y curl
RUN apt-get install -y nano
RUN apt-get install -y python
RUN apt-get install -y python python-dev python-distribute python-pip python-virtualenv libxml2-dev libxslt1-dev libxml2-dev lib32z1-dev
RUN apt-get install -y git 
# https://github.com/docker/docker/issues/9299
ENV TERM xterm

