__author__ = 'Bill'
def kmeansData(k=3,fname=None,plotFlag=False):
    '''
    @input:
            k: number of categories
            fname: input filename
            plotFlag: whether you wanna use matplot to plot the data or not

    @return: (label,data_cluster_centers,data_num_each_cluster)
            label: array of type (samples,1)
            data_cluster_centers: the center point of each category. (k,1)
            data_num_each_cluster: (,1)

    '''
    import pandas as pd
    import numpy as np
    df = pd.DataFrame.from_csv(fname)

    # modify columns
    df.columns = [u'id', u'lat', u'lng', u'loca', u'color', u'timestamp']
    df.drop(['color'],inplace=True,axis=1)
    df.drop(['loca'],inplace=True,axis=1)
    ll_arr = np.asarray(zip(df['id'],df['lat'],df['lng']),dtype = 'float64')

    # kmeans
    from sklearn.preprocessing import StandardScaler
    from sklearn import cluster

    stdScaler = StandardScaler()
    ll_arr_std = stdScaler.fit_transform(ll_arr[:,1:])

    k_means = cluster.KMeans(n_clusters=k)
    k_means.fit_predict(ll_arr_std)

    # extract kmeans results
    data_labels = k_means.labels_
    data_cluster_centers = k_means.cluster_centers_
    data_cluster_centers = stdScaler.inverse_transform(k_means.cluster_centers_)

    n_clusters = len(data_cluster_centers)

    # compute no. of elements in each category
    data_num_each_cluster = np.zeros((n_clusters,1))
    for i in xrange(n_clusters):
        data_num_each_cluster[i,0] = (data_labels == i).sum()

    # plot the data
    if plotFlag:
        import matplotlib.pyplot as plt
        %matplotlib inline
        fig = plt.figure(figsize=(8, 3))
        fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)
        colors = ['#4EACC5', '#FF9C34', '#4E9A06','#00FFFF']

        # KMeans
        ax = fig.add_subplot(1, 3, 1)
        for k, col in zip(range(n_clusters), colors):
            my_members = data_labels == k
            cluster_center = data_cluster_centers[k]
            ax.plot(ll_arr[my_members, 0], ll_arr[my_members, 1], 'w',
                    markerfacecolor=col, marker='.')
            ax.plot(data_cluster_centers[0], data_cluster_centers[1], 'o', markerfacecolor=col,
                    markeredgecolor='k', markersize=6)
        ax.set_title('KMeans')
        ax.set_xticks(())
        ax.set_yticks(())


    return (data_labels,data_cluster_centers,data_num_each_cluster)