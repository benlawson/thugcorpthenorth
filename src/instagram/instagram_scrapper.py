
# coding: utf-8


import urllib3
import json
import datetime
import time
from pprint import pprint
from firebase import firebase

firebase = firebase.FirebaseApplication('https://boiling-fire-6168.firebaseio.com/', None)

def send_data(response):
    query = {}
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


http = urllib3.PoolManager()

while True:
    response = http.request('GET', "https://api.instagram.com/v1/media/search?lat=43.653226&lng=-79.383184&distance=500000&access_token=15936371.e012851.5d851e6e8e0446b2bf66ecb70da6a9d5").data
    info = json.loads(response)['data']
    for x in range(len(response)):
        if info[x]['location'] != None:
            send_data(info)
