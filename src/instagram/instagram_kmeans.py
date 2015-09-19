__author__ = 'Bill'

import pandas as pd
import json
import os
import numpy as np
from pprint import pprint
# twitter_data = retrive('twitter_data')

os.system('curl "https://boiling-fire-6168.firebaseio.com/instagram_data.json?print=pretty" > instagram_data.json')

exec(open("../../kmeans.py").read())

with open('instagram_data.json') as json_data:
    data = json.load(json_data)

df = pd.DataFrame.from_dict(data)
df = df.transpose()
df = df.dropna()
print(df)

data_labels,data_cluster_centers,data_num_each_cluster = kmeansData(df=df,plotFlag=False)
print(data_labels)
print(data_cluster_centers)
print(data_num_each_cluster)