# apcupsd-influxdb-exporter

Build an x86_64 or ARM compatible Docker image that will output commonly used UPS device statistics to an influxdb database using an included version of the 
[APCUPSd](http://www.apcupsd.org/) 
tool. Dockerfiles included for both intel and ARM (RaspberryPi or comparable) chipsets.

## How to build
Building the image is straight forward:
* Git clone this repo
* `docker build -t apcupsd-influxdb-exporter  .`

## Environment Variables
These are all the available environment variables, along with some example values, and a description.

| Environment Varialbe | Example Value | Description |
| -------------------- | ------------- | ----------- |
| WATTS |  1500 | if your ups doesn't have NOMPOWER, set this to be the rated max power, if you do have  NOMPOWER, don't set this variable |
| APCUPSD_HOST |  192.168.1.100 | host running apcupsd |
| INFLUXDB_HOST |  192.168.1.101 | host running influxdb |
| HOSTNAME |  unraid | host you want to show up in influxdb, optional defaults to apcupsd-influxdb-exporter |
| INFLUXDB_DATABASE |  apcupsd | db name for influxdb. optional, defaults to apcupsd |
| INFLUXDB_USER | myuser | optional, defaults to empty |
| INFLUXDB_PASSWORD | pass | optional, defaults to empty |
| INFLUXDB_PORT |  8086 | optional, defaults to 8086 |
| VERBOSE | true | if anything but true docker logging will show no output

## How to Use

### Run docker container directly
```bash
docker run --rm  -d --name="apcupsd-influxdb-exporter" \
    -e "WATTS=600" \
    -e "HOSTNAME=unraid" \
    -e "INFLUXDB_HOST=10.0.1.11" \
    -e "APCUPSD_HOST=10.0.1.11" \
    -t bgulla/apcupsd-influxdb-exporter
```
Note: if your UPS does not include the NOMPOWER metric, you will need to include the WATTS environment variable in order to compute the live-power consumption 
metric.

### Run from docker-compose
```bash
version: '3'
services:
  apcupsd-influxdb-exporter:
    image: bgulla/apcupsd-influxdb-exporter
    container_name: apcupsd-influxdb-exporter
    restart: always
    environment:
      WATTS: 1500
      APCUPSD_HOST: 10.0.1.11
      INFLUXDB_HOST: 10.0.1.11
      HOSTNAME: unraid
```

If you want to debug the apcaccess output or the send to influxdb, set the environment variable "VERBOSE" to "true"
