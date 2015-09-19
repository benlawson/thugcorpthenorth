__author__ = 'Bill'

import pandas as pd
import json
from get_twitter_data import retrive 
instagram_data = retrive('instagram_data')
twitter_data = retrive('twitter_data')

exec(open("../../kmeans.py").read())

df = pd.DataFrame.from_dict(instagram_data)

data_labels,data_cluster_centers,data_num_each_cluster = kmeansData(df=df.transpose(),plotFlag=False)
print(data_labels)
print(data_cluster_centers)
print(data_num_each_cluster)
