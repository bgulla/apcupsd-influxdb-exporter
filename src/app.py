#!/usr/bin/python
import os
import platform
import time
from influxdb import InfluxDBClient
from apcaccess import status as apc


# Try to pull the hostname
HOSTNAME = platform.node()
try:
  HOSTNAME = os.getenv('HOSTNAME', 'meatwad')
except:
  pass

# Run APCACCESS
#os.system('apcaccess > .apcupsd_output.txt')

# Debug

# Send to influxdb

dbname = os.getenv('INFLUXDB_DATABASE', 'upsnew')
user = ""
password =""
port = os.getenv('INFLUXDB_PORT', 8086)
host = os.getenv('INFLUXDB_HOST', '10.0.1.11')
client = InfluxDBClient(host, port, user, password, dbname)

client.create_database(dbname)


print "Hostname: ", HOSTNAME
print "database name: ", dbname
print "db host:", host
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
                              'BCHARGE' : float(ups['BCHARGE']),
                              'TONBATT' : float(ups['TONBATT']),
                              'TIMELEFT' : float(ups['TIMELEFT']),
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
