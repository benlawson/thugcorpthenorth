__author__ = 'Bill'

import pandas as pd
import json
from firebase import firebase
app = firebase.FirebaseApplication('https://boiling-fire-6168.firebaseio.com/', None)
instagram_data = app.get('/instagram_data', None)
twitter_data = app.get('/twitter_data', None)

exec(open("../../kmeans.py").read())

df = pd.DataFrame.from_dict(data)

data_labels,data_cluster_centers,data_num_each_cluster = kmeansData(df=df.transpose(),plotFlag=False)
print(data_labels)
print(data_cluster_centers)
print(data_num_each_cluster)
