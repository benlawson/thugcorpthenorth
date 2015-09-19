
# coding: utf-8


import urllib3
import json
import datetime
import time
from pprint import pprint
from firebase import firebase

firebase = firebase.FirebaseApplication('https://boiling-fire-6168.firebaseio.com/', None)

def send_data(response):
    # pprint(response)
    print(response[1]['created_time'])
    query = {}
    for x in range(len(response)):
        query["coordinate_1"] = response[x]['location']['latitude']
        query["coordinate_2"] = response[x]['location']['longitude']
        query["created_at"] = datetime.datetime.fromtimestamp(int(response[x]['created_time'])).strftime('%Y-%m-%d %H:%M:%S')
        query["id"] = response[x]['id']

        if 'caption' in response[x]:
            if response[x]['caption'] != None:
                if 'text' in response[x]['caption']:
                    query["text"] = response[x]['caption']['text']

        query["img"] = response[x]['images']['standard_resolution']

        if 'videos' in response[x]:
            query["video"] = response[x]['videos']['standard_resolution']
        result = firebase.post('/instagram_data', query)

 
for x in range(1000):
    http = urllib3.PoolManager()
    response = http.request('GET', "https://api.instagram.com/v1/media/search?lat=42.360066&lng=-71.05793952&distance=5000&access_token=15936371.e012851.5d851e6e8e0446b2bf66ecb70da6a9d5").data
    info = json.loads(response)['data']
    send_data(info)
