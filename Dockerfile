# Production image
FROM python:3.7-slim

ADD . /task-tracker
WORKDIR /task-tracker

RUN apt-get clean \
    && apt-get -y update
RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential
RUN pip install -r requirements.txt

ENTRYPOINT ["uwsgi", "uwsgi.ini"]
