#!/usr/bin/env python3

import sys

import data
import tasks


def getObjects(df, kmeans, cluster, limit):
    count = 0

    for i in df[0]:
        res_cluster = kmeans.predict([i])

        if cluster == res_cluster:
            sys.stdout.write("[");
            for j in i[:-1]:
                sys.stdout.write("%.02f, " % (j));
            sys.stdout.write("%.02f]\n" % (i[-1]));

            count += 1

        if count == limit:
            return


if __name__ == "__main__":
    limit = 50

    if len(sys.argv) == 1:
        clusters_num = 2
    elif len(sys.argv) in [2, 3]:
        clusters_num = int(sys.argv[1])

        if len(sys.argv) == 3:
            limit = int(sys.argv[2])
    else:
        print("Usage:")
        print("\texp_004a.py")
        print("\texp_004a.py clusters_num {limit}")

    df = data.dat_002(approvedJoin=False)
    (kmeans, silhouette) = tasks.unsupervised(df, clusters_num)

    for i in range(clusters_num):
        print("Cluster %d" %(i))
        getObjects(df, kmeans, i, limit)
