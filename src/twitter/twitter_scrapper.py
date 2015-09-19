
# coding: utf-8

import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
import datetime
import time
from firebase import firebase

firebase = firebase.FirebaseApplication('https://boiling-fire-6168.firebaseio.com/', None)

def send_data(response):
    query = {}
    try:
        query["source"] = "twitter"
        query["coordinate_1"] = response.coordinates['coordinates'][0]
        query["coordinate_2"] = response.coordinates['coordinates'][1]
        query["created_at"] = str(response.created_at)
        query["id"] = response.id
        query["text"] = response.text
        for x in query:
            print x
        result = firebase.post('/data', query)
        print result
        #print payload
        # save_to_db(payload)
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
