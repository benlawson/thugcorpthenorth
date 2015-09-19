# coding: utf-8


import json
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import datetime
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

with open('twitter_keys.txt','r') as f:
    consumer_key = f.readline().strip()
    consumer_secret = f.readline().strip()
    access_token = f.readline().strip()
    access_token_secret = f.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
stream = Stream(auth, l)


# In[15]:

#This line filter Twitter Streams to capture tweets that fallinto the bounding box of Boston
stream.filter(locations=[-71.190426,42.273561,-70.922514,42.444548], async=True)
