__author__ = 'Bill'
# from __future__ import absolute_import
# from __future__ import print_function

import json
import pandas as pd
import numpy as np
import os
import indicoio
def tweetCategory(getDF=False):
    '''

    :return: (text_classAndSenti,text_list)
        text_classAndSenti (selected samples,2): (:,0)=1 indicates that this tweets 1) is related to food 2) is positive.
                                                (:,0)=0 otherwise
        text_list: original lists of tweets
    '''

    # os.system('curl "https://boiling-fire-6168.firebaseio.com/twitter_data.json?print=pretty" > twitter_data_cat.json')
    FOOD=["beer","cooking","general_food","vegan","vegetarian","wine","nutrition"]

    with open('twitter_data_cat.json') as json_data:
        data = json.load(json_data)
    # JSON -> list of texts
    df = pd.DataFrame.from_dict(data)
    df = df.transpose()
    text_list = df['text'].values.tolist()



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
        if topIncluded(top_topics,FOOD) and text_classAndSenti[i,1]>.5:
            text_classAndSenti[i,0] = 1
        else:
            text_classAndSenti[i,1] = 0 # clear sentiment info of non-food tweets


    if getDF:
        return text_classAndSenti,text_list,df
    else:
        return text_classAndSenti,text_list

if __name__=='__main__':
    classAndSenti,text_list = tweetCategory()
    text_list = np.asarray(text_list)
    selected_index = (classAndSenti[:,0]==1).nonzero()
    selected_text = text_list[selected_index]
