#!/usr/bin/python
import os
import time

from apcaccess import status as apc
from influxdb import InfluxDBClient


dbname = os.getenv('INFLUXDB_DATABASE', 'apcupsd')
user = os.getenv('INFLUXDB_USER')
password = os.getenv('INFLUXDB_PASSWORD')
port = os.getenv('INFLUXDB_PORT', 8086)
host = os.getenv('INFLUXDB_HOST', '10.0.1.9')
interval = float(os.getenv('INTERVAL', 5))
client = InfluxDBClient(host, port, user, password, dbname)

client.create_database(dbname)

while True:
    ups = apc.parse(apc.get(host=os.getenv('APCUPSD_HOST', 'localhost')), strip_units=True)

    watts = float(os.getenv('WATTS', ups.get('NOMPOWER', 0.0))) * 0.01 * float(ups.get('LOADPCT', 0.0))
    json_body = [
        {
            'measurement': 'apcaccess_status',
            'fields': {
                'WATTS': watts,
                'STATUS': ups.get('STATUS'),
                'LOADPCT': float(ups.get('LOADPCT', 0.0)),
                'BCHARGE': float(ups.get('BCHARGE', 0.0)),
                'TONBATT': float(ups.get('TONBATT', 0.0)),
                'TIMELEFT': float(ups.get('TIMELEFT', 0.0)),
                'NOMPOWER': float(ups.get('NOMPOWER', 0.0)),
                'CUMONBATT': float(ups.get('CUMONBATT', 0.0)),
                'BATTV': float(ups.get('BATTV', 0.0)),
                'OUTPUTV': float(ups.get('OUTPUTV', 0.0)),
                'ITEMP': float(ups.get('ITEMP', 0.0)),
            },
            'tags': {
                'host': os.getenv('HOSTNAME', ups.get('HOSTNAME', 'apcupsd-influxdb-exporter')),
                'serial': ups.get('SERIALNO', None),
            }
        }
    ]

    if os.getenv('VERBOSE', 'false').lower() == 'true':
        print(json_body)
        print(client.write_points(json_body))
    else:
        client.write_points(json_body)
    time.sleep(interval)
