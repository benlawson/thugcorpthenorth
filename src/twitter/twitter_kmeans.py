__author__ = 'Bill'

import pandas as pd
import json
import os
from get_twitter_data import retrive 
from pprint import pprint
# twitter_data = retrive('twitter_data')
data = os.system('curl "https://boiling-fire-6168.firebaseio.com/.json?print=pretty"')

# data = json.loads(json.dumps(twitter_data))
pprint(data)
exec(open("../../kmeans.py").read())

df = pd.DataFrame.from_dict(data)

data_labels,data_cluster_centers,data_num_each_cluster = kmeansData(df=df.transpose(),plotFlag=False)
print(data_labels)
print(data_cluster_centers)
print(data_num_each_cluster)
