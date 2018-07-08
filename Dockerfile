FROM python:2.7.15-alpine3.7
#FROM jfloff/alpine-python
MAINTAINER Brandon <hey@brandongulla.com>

RUN apk add --no-cache apcupsd jq curl supervisor busybox bash
COPY ./conf/requirements.txt /requirements.txt
COPY ./conf/apcupsd.conf /
COPY ./src/app.py /
RUN pip install -r /requirements.txt
COPY ./conf/supervisord.conf /supervisord.conf

CMD ["supervisord", "-n", "-c","/supervisord.conf"]
