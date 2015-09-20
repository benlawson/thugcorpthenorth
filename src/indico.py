__author__ = 'Bill'
# from __future__ import absolute_import
# from __future__ import print_function

import json
import pandas as pd
import numpy as np
import os
import indicoio
import geo_results
from pprint import pprint
def tweetCategory(getDF=False,insta=False):
    '''

    :return: (text_classAndSenti,text_list)
        text_classAndSenti (selected samples,2): (:,0)=1 indicates that this tweets 1) is related to food 2) is positive.
                                                (:,0)=0 otherwise
        text_list: original lists of tweets
    '''
    FOOD=["beer","cooking","general_food","vegan","vegetarian","wine","nutrition"]
    if insta:
        os.system('curl "https://boiling-fire-6168.firebaseio.com/instagram_data.json?print=pretty" > instagram/instagram_data_cat.json')
        with open('instagram/instagram_data_cat.json') as json_data:
            data = json.load(json_data)
    else:
        os.system('curl "https://boiling-fire-6168.firebaseio.com/twitter_data.json?print=pretty" > twitter/twitter_data_cat.json')
        with open('twitter/twitter_data_cat.json') as json_data:
            data = json.load(json_data)
    # JSON -> list of texts
    df = pd.DataFrame.from_dict(data)
    df = df.transpose()
    # print("dfInfo",df.info())
    if insta:
        lat = df['coordinate_2']
        lng = df['coordinate_1']
    else:
        lat = df['coordinate_1']
        lng = df['coordinate_2']
    in_toronto = []
    for idx,x  in enumerate(lat):
        in_toronto = in_toronto + [geo_results.is_in_circle(geo_results.TORONTO.latitude, geo_results.TORONTO.longitude, geo_results.radius, lng[idx], lat[idx])]
    # print in_toronto
    df['in_toronto'] = in_toronto
    df = df[df['in_toronto'] == 1]
    # print("DF:  ")
    # print df
    # dicard insta without text
    if insta:
        df = df[df['text'].notnull()]
        text_list =df['text'].values.tolist()
    else:
        text_list = df['text'].values.tolist()
    print(df.shape)

    # Get topics
    indicoio.config.api_key = 'dfd155c0984bed63c78aef5ce44763bf'
    topics = indicoio.text_tags(text_list,top_n = 5)

    def topIncluded(topics,cat):
        # test if at least one element in topics is in cat
        for i in topics:
            if i in cat:
                return True
        return False

    # get sentiment analysis
    text_classAndSenti = np.zeros((len(text_list),2))
    text_classAndSenti[:,1] = indicoio.sentiment(text_list)

    # put text into classes (Food is 1; otherwise, 0)
    for i,t in enumerate(topics):
        top_topics = t.keys()
        if topIncluded(top_topics,FOOD) and text_classAndSenti[i,1]>0.5:
            text_classAndSenti[i,0] = 1
        else:
            text_classAndSenti[i,1] = 0 # clear sentiment info of non-food tweets

    if getDF:
        return text_classAndSenti,text_list,df
    else:
        return text_classAndSenti,text_list

def filtered_clusters(insta=False):
    if insta:
        print("****INSTAGRAM****")
    k = 3 # set k here
    classAndSenti,text_list,df = tweetCategory(getDF=True,insta=insta)

    text_list = np.asarray(text_list) # convert to numpy array

    # get indexes of the selected/unselcted rows
    selected_index = (classAndSenti[:,0]==1).nonzero()
    unselected_index = (classAndSenti[:,0]==0).nonzero()
    # get the selected text
    selected_text = np.asarray(text_list[selected_index])
    df = df.drop(df.index[unselected_index])
    exec(open("kmeans.py").read())
    data_labels,data_cluster_centers,data_num_each_cluster = kmeansData(k=k,df=df,plotFlag=False)
    cluster_info = []
    for i in xrange(k):
        singleCluster = {}
        singleCluster['no'] = i
        cen = data_cluster_centers[i]
        if insta:
            singleCluster['lat'] = cen[0]
            singleCluster['lon'] = cen[1]
        else:
            singleCluster['lat'] = cen[1]
            singleCluster['lon'] = cen[0]
        singleCluster['size'] = data_num_each_cluster[i,0]

        singleCluster['content'] = selected_text[data_labels==i]
        cluster_info.append(singleCluster)

    pprint(cluster_info)
    return cluster_info

if __name__=='__main__':
    cluster_info = filtered_clusters(insta=True)
    print(cluster_info[0]['content'].shape)
