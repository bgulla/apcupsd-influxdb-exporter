# apcupsd-influxdb-exporter
Exposes GPIO sensor data via JSON REST endpoint. This repo builds an x86_64 or ARM compatible Docker image that will output commonly used UPS device statistics to 
an influxdb database. 

## How to build
Building the image is straight forward:

* Git clone this repo
* `docker build -t apcupsd-influxdb-exporter`

## Telegraf/InfluxDB (+Grafana) Plugin
![Grafana is awesome](https://github.com/bgulla/apcupsd-influxdb-exporter/raw/master/img/watts.png?raw=true)
Graphs are awesome, and I am am a huge fan of InfluxDB + Grafana.
