import geo_results
from yelpapi import YelpAPI
from uberpy import Uber
import math, os, json
import numpy as np

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
    try:
        return sum(total)/float(len(total))
    except:
        return 0 

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
       location['business_id'] = e['id']
       location['uber_time'] =  uber_time
       locations.append(location)
    return locations
def retrive(suffix=''):
    os.system('curl "https://boiling-fire-6168.firebaseio.com{0}.json?print=pretty" >> temp.txt'.format(suffix)) #get data from database
    with open('temp.txt') as f:
        return json.load(f)

def distance(lat1, lng1, lat2, lng2):
    d1 = lat1-lat2
    d2 = lng1 - lng2
    return math.sqrt((d1*d1) +( d2*d2) )
def compare_clusters(locations, clusters):
    matches = [0]*len(clusters) # used to match clusters to yelp locations
    for idx, clust in enumerate(clusters):
        closest_match = 1000000
        for pt in locations:
           similarity = distance(clust['latitude'], clust['longitude'], pt['latitude'], pt['longitude'])
           if similarity < closest_match and pt not in matches:
               closest_match = similarity
               matches[idx] = pt
    ret = []
    for idx, place in enumerate(matches):
        place['cluster_size'] = clusters[idx]['size']
        place['content'] = clusters[idx]['content']
        place['blurb'] = yelp_api.business_query(place['business_id'])
        ret.append(place) 
    return ret 

