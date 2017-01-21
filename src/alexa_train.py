#!/usr/bin/python

import sys
#import requests
import json
import urllib2

stop = 'Reading'
apiKey = 'XXXXX'

predictionsByStopUrl = 'http://realtime.mbta.com/developer/api/v2/predictionsbystop?stop='+stop+'&api_key='+apiKey+'&format=json'

#r = requests.get(predictionsByStopUrl)
#if r.status_code != 200:
#    print 'API Call failed: ' + str(r.status_code) + ' ' + r.text
#    sys.exit(1)
#
#d = json.loads(r.text)

d = json.load(urllib2.urlopen(predictionsByStopUrl))

for mode in d['mode']:
    if mode['mode_name'] == 'Commuter Rail':
        for route in mode['route']:
            print "Route: " + route['route_name']
            p_text_list = []
            for direction in route['direction']:
                print "Direction: " + direction['direction_name']
                min_list = []
                for trip in direction['trip']:
                    pre_away = int(trip['pre_away'])
                    m, s = divmod(pre_away, 60)
                    print 'Train to ' + trip['trip_headsign'] + ' predicted in ' + str(m) + ' min '
                    min_list.append(str(m) + ' minutes')
                if len(min_list) == 0:
                    p_text_list.append('There is currently no train prediction for trains to ' + trip['trip_headsign'])
                else:
                    p_text_list.append('The next trains to ' + trip['trip_headsign'] + ' are in ' + ' and '.join(min_list))
            
print "Train predictions: "
for p_text in p_text_list:
    print p_text



