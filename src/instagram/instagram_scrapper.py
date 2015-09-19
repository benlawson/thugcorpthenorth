
# coding: utf-8


import urllib3
import json
import datetime
import time

#def save_to_db(payload, table):
#pls implement

def send_data(response):
    entries = ['caption','created_time', 'id', 'location', 'link' ]
    query = []
    for x in entries:
        if 'location' in x:
            query.append(response[x]['latitude'])
            query.append(response[x]['longitude'])
            try:
                query.append(response[x]['id'])
                query.append(response[x]['name'])
            except: 
                query.append(0)
                query.append(0)
        elif 'caption' in x:
            try:
                query.append(response[x]['text'])
            except:
                query.append(0)
        elif 'id' in x and not('has' in x) and not('in' in x):
            both_id = response[x]
            ids = both_id.split('_')
            query.append(both_id)
            query.append(int(ids[0]))
            query.append(int(ids[1]))

        elif 'create' in x:
            query.append(str(datetime.datetime.fromtimestamp(int(response['created_time'])/1.0)))
        else:
            if response[x] == False:
                query.append(0)
            else:     
                query.append(response[x])
x = 2000
while (x):
    http = urllib3.PoolManager()
    response = http.request('GET', "https://api.instagram.com/v1/media/search?lat=42.360066&lng=-71.05793952&distance=5000&access_token=15936371.e012851.5d851e6e8e0446b2bf66ecb70da6a9d5").data
    info = json.loads(response)['data']
    send_data(info)
    x = x - 1
