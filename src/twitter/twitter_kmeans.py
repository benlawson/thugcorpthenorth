__author__ = 'Bill'

import pandas as pd

import json
exec(open("/Users/Bill/GitHub/thugcorpthenorth/kmeans.py").read())

with open('boiling-fire-6168-data-export.json') as json_data:
    data = json.load(json_data)

df = pd.DataFrame.from_dict(data)

data_labels,data_cluster_centers,data_num_each_cluster = kmeansData(df=df.transpose(),plotFlag=True)
print(data_labels)
print(data_cluster_centers)
print(data_num_each_cluster)