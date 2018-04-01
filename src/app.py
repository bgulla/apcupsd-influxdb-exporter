#!/usr/bin/python
import os
import platform
import time
from influxdb import InfluxDBClient
from apcaccess import status as apc


# Try to pull the hostname
HOSTNAME = platform.node()
try:
  HOSTNAME = os.environ['HOSTNAME']
except:
  pass

# Run APCACCESS
#os.system('apcaccess > .apcupsd_output.txt')

# Debug

# Send to influxdb

dbname = os.environ['INFLUXDB_DATABASE']
user = ""
password =""
port = os.environ['INFLUXDB_PORT']
host = os.environ['INFLUXDB_HOST']
client = InfluxDBClient(host, port, user, password, dbname)

client.create_database(dbname)


#print ups

while True:
  ups = apc.parse(apc.get(host="localhost"), strip_units=True)
  if os.environ['WATTS']:
    ups['NOMPOWER'] = os.environ['WATTS']
  watts = float(float(ups['NOMPOWER']) * float(0.01 *float(ups['LOADPCT'])))
  json_body =  [
                      {
                          'measurement': 'APC-NEW',
                          'fields': {
                              'WATTS' : float(watts),
                              'LOADPCT' : float(ups['LOADPCT']),
                              'NOMPOWER' : float(ups['NOMPOWER'])
                          },
                          'tags': {
                              'host': HOSTNAME
                          }
                      }
                  ]
  print json_body
  print client.write_points(json_body)
  time.sleep(5)
