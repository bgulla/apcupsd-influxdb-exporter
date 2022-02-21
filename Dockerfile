FROM python:2-alpine
MAINTAINER Brandon <brandon.gulla@gmail.com>

RUN apk add --no-cache tzdata

COPY ./apcupsd-influxdb-exporter.py /apcupsd-influxdb-exporter.py
RUN pip install apcaccess influxdb

CMD ["python", "/apcupsd-influxdb-exporter.py"]
