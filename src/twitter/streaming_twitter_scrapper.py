# coding: utf-8


import json
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import MySQLdb
import datetime
import boto.rds


instances = conn.get_all_dbinstances("twitterdb")
database = instances[0]


:
#twitter account info
#consumer_key = 'LYSIAcY40RmPGcakF3uCtm3sK'
#consumer_secret = 'aT3BgeqcaWNvdeJlqYyY9y8XPtLgzmiQIor0nEqpaE6uLzOMJ1'
#access_token = '224805278-dZREnC1V50OnxXGJ4aWbWmMs08RrDFxFUZR9DssX'
#access_token_secret = 'EJXKcWm0jHT796wgWBCawV5xPrKBqMMHiMmKc6AQpEgjX'


#def save_to_db(payload, table):
  #pls implement 

def send_data(response):
    #get tweet information
    entries = ['coordinates', 'created_at','id', 'text', 'timestamp_ms', 'user']
    query = []
    for x in entries:
        if 'coordinates' in x:
            query.append(response[x]['coordinates'][1])
            query.append(response[x]['coordinates'][0])
        elif 'user' in x:
            query.append(response[x]['id'])
        elif 'created' in x:
            query.append(str(datetime.datetime.fromtimestamp(int(response['timestamp_ms'])/1000)))
        else:
            if response[x] == False:
                query.append(0)
            else:     
                query.append(response[x])
    payload = [str(x.encode('ascii', 'ignore')).replace("\"","\'").replace('u\'','').replace('True','1').replace('None','0') if type(x) is unicode or type(x) is str else str(x).replace("\"","\'").replace('u\'','') for x in query ]
    error = save_to_db(payload, "boston_tweets")        



#This is a listener handles received tweets.
class StandardListener(StreamListener):
    def on_data(self, data):
        response = json.loads(data)
        if not(response['coordinates'] == None):
            send_data(response)
    def on_error(self, status):
        print status    



#This handles Twitter authetification and the connection to Twitter Streaming API
l = StandardListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)


# In[15]:

#This line filter Twitter Streams to capture tweets that fallinto the bounding box of Boston
stream.filter(locations=[-71.190426,42.273561,-70.922514,42.444548], async=True)
