import geo_results
from yelpapi import YelpAPI
from uberpy import Uber
import math, os, json
#yelp api setup
with open('yelp.txt','r') as f:
        consumer_key = f.readline().strip()
        consumer_secret = f.readline().strip()
        token = f.readline().strip()
        token_secret = f.readline().strip()

yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)

with open('uber.txt','r') as f:
        client_id = f.readline().strip()
        server_token = f.readline().strip()
        secret= f.readline().strip()
uber = Uber(client_id, server_token, secret)

def uberize(latitude, longitude):
    total = []
    times = uber.get_time_estimate(latitude, longitude)
    for x in (times['times']):
        total.append(x['estimate'])
    return sum(total)/float(len(total))

def client_choice(latitude, longitude, dis, theme=None):
    '''takes in clients options and returns top 20 resturants as a list with meta information like the Yelp Rating and the average wait time for an Uber'''
    geo =  "{0}, {1}".format(latitude, longitude)
    search_results  = yelp_api.search_query(term='{0}'.format(theme), ll=geo, sort=2, radius_filter=dis, offset=0)['businesses'] #sort=2 returns the highest rated locations
    search_results = search_results +  yelp_api.search_query(term='{0}'.format(theme), ll=geo, sort=2, radius_filter=dis, offset=20)['businesses'] #index begin at 20
    #parse the response
    locations = [] #store parsed businesses
    for idx, e in enumerate(search_results):
       location = {}
       lat = e['location']['coordinate']['latitude']
       lng = e['location']['coordinate']['longitude']
       uber_time = uberize(lat, lng)
       location['name'] = e['name']
       location['latitude'] = lat
       location['longitude'] =  lng
       location['yelp_rating'] = e['rating']
       location['uber_time'] =  uber_time
       locations.append(location)
    return locations
def retrive(suffix=''):
    os.system('curl "https://boiling-fire-6168.firebaseio.com{0}.json?print=pretty" >> temp.txt'.format(suffix)) #get data from database
    with open('temp.txt') as f:
        return json.load(f)

def prepare_clusters():
    import pandas as pd
    import json
    import os
    import numpy as np
     
    x = retrive('/twitter_data')
    x = x + retrive('/instagram_data')
    df = pd.DataFrame.from_dict(data)
    df = df.transpose()
    df = df.dropna()
    
    labels,centriods,c_size = kmeansData(k=8, df=df,plotFlag=False)    
    return cenriods, c_size
def distance(lat1, lng1, lat2, lng2):
    d1 = lat1-lat2
    d2 = lng1 - lng2
    return math.sqrt((d1*d1) +( d2*d2) )
def compare_clusers(locations, centriods, c_size):
    clusters = zip(centriods, c_size)
    sort = sorted(clusters, key=lambda x: x[1], reverse=True)
    sort = filter(lambda x: x[1] > 50)
    matches = [] # used to match clusters to yelp locations
    closest_match = 1000000
    for idx, clust in enumerate(clusters):
        for pt in locations:
           similarity = distance(clust[0][0], clust[0][1], pt[0][0], pt[0][1])
           if similarity < closest_match:
               closest_match = similarity
               matches[idx] = pt 
        locations.pop(locations.index(matches[idx]))   
    for place in matches[:3]:
       ##TODO     
    return matches[:3], clusters[:3]

