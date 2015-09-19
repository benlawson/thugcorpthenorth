
# coding: utf-8

import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
import datetime


#def save_to_db(payload):

def send_data(response):
    query = []
    try:
        query.append(response.coordinates['coordinates'][0])
        query.append(response.coordinates['coordinates'][1])
        query.append(str(response.created_at))
        query.append(response.id)
        query.append(response.text)

        payload = [str(x.encode('ascii', 'ignore')).replace("\"","\'").replace('u\'','').replace('None','0') if type(x) is unicode or type(x) is str else str(x).replace("\"","\'").replace('u\'','') for x in query ]
        #payload = str(query)
        #print payload
        save_to_db(payload)
        return "good"
    except:
        return "error"


#need to have a file keys.txt with the Twitter API keys/info
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

with open('keys.txt','r') as f:
    consumer_key = f.readline().strip()
    consumer_secret = f.readline().strip()
    access_token = f.readline().strip()
    access_token_secret = f.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search,q="",count=2000, geocode="43.7182412,-79.378058,5mi").items():
    print tweet.text
    print send_data(tweet)

