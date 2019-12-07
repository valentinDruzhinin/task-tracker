# Production image
FROM python:3.7-slim

ADD . /task-tracker
WORKDIR /task-tracker
COPY nginx/uwsgi.ini nginx/build.sh ./
COPY nginx/nginx.conf /etc/nginx
RUN rm -rf prod_build

RUN apt-get clean \
    && apt-get -y update
RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential
RUN pip install -r requirements.txt
RUN make upgrade

RUN chmod +x "./build.sh"
ENTRYPOINT ["./build.sh"]
