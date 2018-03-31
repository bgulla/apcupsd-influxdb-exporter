# apcupsd-influxdb-exporter
Build an x86_64 or ARM compatible Docker image that will output commonly used UPS device statistics to an influxdb database.

## How to build
Building the image is straight forward:
* Git clone this repo
* `docker build -t apcupsd-influxdb-exporter`

## Running
```bash
docker run --rm  -d --name="apcupsd" \
  --privileged --restart=always \
  -e "HOSTNAME=newguy" -e "WATTS=600" \
  -t bgulla/apcupsd-influxdb-exporter
```

## Telegraf/InfluxDB (+Grafana) Plugin
![Grafana is awesome](https://github.com/bgulla/apcupsd-influxdb-exporter/raw/master/img/watts.png?raw=true)
Graphs are awesome, and I am am a huge fan of InfluxDB + Grafana.
