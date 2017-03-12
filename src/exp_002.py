#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================

import os

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.model_selection import KFold

import data
import util


def execute(model):
    # Get dataset and make the necessary numpy arrays
    features, _ = data.dat_001()

    # Create folds for training and testing
    kf = KFold(n_splits=10)
    kf.get_n_splits(features)

    # Try different number of clusters
    for cluster_number in range(2, 10):
        print("Number of Clusters: %s" % (cluster_number))

        # Train and test with different folds
        for train_index, test_index in kf.split(features):
            kmeans = KMeans(n_clusters=cluster_number, random_state=0)
            kmeans.fit(features[train_index])

            # And get it's silhouette score
            m = metrics.silhouette_score(
                features[train_index],
                kmeans.labels_)

            print("\t%0.2f" % (m))


if __name__ == "__main__":
    print("K-Means")
    execute("kmeans")
