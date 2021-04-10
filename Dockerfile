FROM python:3.9.4

ENV PYTHONUNBUFFERED 1
RUN apt-get -y update
RUN mkdir /srv/docker-server

ADD . /srv/docker-server
WORKDIR /srv/docker-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
