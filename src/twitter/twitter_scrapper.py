
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
    query["coordinate_1"] = response.coordinates['coordinates'][0]
    query["coordinate_2"] = response.coordinates['coordinates'][1]
    query["created_at"] = str(response.created_at)
    query["id"] = response.id
    query["text"] = response.text
    result = firebase.post('/twitter_data', query)
    print result


#need to have a file keys.txt with the Twitter API keys/info
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

with open('twitter_keys.txt','r') as f:
    consumer_key = f.readline().strip()
    consumer_secret = f.readline().strip()
    access_token = f.readline().strip()
    access_token_secret = f.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,q="",count=1000000, geocode="43.653226,-79.383184,400mi").items():
    if tweet.coordinates != None:
        send_data(tweet)



