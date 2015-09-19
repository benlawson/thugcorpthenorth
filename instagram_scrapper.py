
# coding: utf-8


import MySQLdb
import urllib3
from bs4 import BeautifulSoup 
import json
import datetime
import time

def save_to_db(payload, table):
#pls implement

def send_data(response):
    #get tweet information
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
    payload = [str(x.encode('ascii', 'ignore')).replace("\"","\'").replace('u\'','').replace('True','1').replace('None','0') if type(x) is unicode or type(x) is str else str(x).replace("\"","\'").replace('u\'','') for x in query ]
    save_to_db(payload, 1)
    user_query = []
    for xy in response['user'].keys():
        user_query.append(response['user'][xy])
    return save_to_db(user_query, 2)

m = 1
while True:
    print "begin loop"
    http = urllib3.PoolManager()
    response = http.request('GET', "https://api.instagram.com/v1/media/search?lat=42.360066&lng=-71.05793952&distance=5000&MIN_TIMESTAMP=1432225371&access_token=15936371.e012851.5d851e6e8e0446b2bf66ecb70da6a9d5").data
    soup = BeautifulSoup(response)
    info = json.loads(soup.get_text())['data']
    hits = 0
    count = len(info)    
    for entry in range(count):
        try:
            hits = hits + send_data(info[entry])
        except:
            break
    sleepy = (count-hits+1)*m
    time.sleep(sleepy)
    
    if (hits < 2):
        m = m + 2
    elif (hits == 2 or (hits > 2 and hits < 6)):
        m = m + 1
    elif (hits > 15):
        m = 1



