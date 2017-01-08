#!/usr/bin/python

import sys
import requests
import json

stop = 'Reading'
apiKey = 'XXXXX'

predictionsByStopUrl = 'http://realtime.mbta.com/developer/api/v2/predictionsbystop?stop='+stop+'&api_key='+apiKey+'&format=json'

r = requests.get(predictionsByStopUrl)

if r.status_code != 200:
    print 'API Call failed: ' + str(r.status_code) + ' ' + r.text
    sys.exit(1)

d = json.loads(r.text)

for mode in d['mode']:
    if mode['mode_name'] == 'Commuter Rail':
        for route in mode['route']:
            print "Route: " + route['route_name']
            for direction in route['direction']:
                print "Direction: " + direction['direction_name']
                for trip in direction['trip']:
                    pre_away = int(trip['pre_away'])
                    m, s = divmod(pre_away, 60)
                    print 'Train to ' + trip['trip_headsign'] + ' predicted in ' + str(m) + ' min '



