FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential redis-server


COPY requirements.txt tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY . /keyvalue
WORKDIR /keyvalue

EXPOSE 6379

CMD ["redis-server", "--protected-mode no"]