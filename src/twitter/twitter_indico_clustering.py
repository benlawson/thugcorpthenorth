import numpy as np
import json
import pandas as pd
import numpy as np
import indicoio
import os
from pprint import pprint
def indicoClustering():
    '''

    :return: list of k dictionaries. keys: center location, ie (cor1,cor2); values (# of elements in each category, tweets)
    '''
    k = 3 # set k here
    exec(open("twitter_indico.py").read())
    classAndSenti,text_list,df = tweetCategory(getDF=True)

    text_list = np.asarray(text_list) # convert to numpy array
    selected_index = (classAndSenti[:,0]==1).nonzero()
    selected_text = text_list[selected_index]


    # get indexes of the selected/unselcted rows
    selected_index = (classAndSenti[:,0]==1).nonzero()
    unselected_index = (classAndSenti[:,0]==0).nonzero()
    # get the selected text
    selected_text = np.asarray(text_list[selected_index])

    df = df.drop(df.index[unselected_index])

    exec(open("../../kmeans.py").read())

    data_labels,data_cluster_centers,data_num_each_cluster = kmeansData(k=k,df=df,plotFlag=False)
    cluster_info = {}
    for i in xrange(k):
        cen = data_cluster_centers[i]
        cluster_info[(cen[0],cen[1])] = (data_num_each_cluster[i,0],selected_text[data_labels==i])
    #pprint(cluster_info)
    return cluster_info

if __name__=='__main__':
    indicoClustering()