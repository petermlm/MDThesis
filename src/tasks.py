from sklearn import tree
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.cluster import KMeans
from sklearn.model_selection import KFold


def supervised(data, model):
    # Get dataset and make the necessary numpy arrays
    features, classes = data

    # Create folds for training and testing
    kf = KFold(n_splits=10)
    kf.get_n_splits(features)

    # Train and test with different folds
    for train_index, test_index in kf.split(features):
        # Fit
        if model == "tree":
            clf = tree.DecisionTreeClassifier()
        elif model == "bayesian":
            clf = MultinomialNB()

        clf.fit(features[train_index], classes[train_index])

        # And get it's accuracy
        m = metrics.accuracy_score(
            classes[test_index],
            clf.predict(features[test_index]))

        print("\t%0.2f" % (m))


def unsupervised(data):
    # Get dataset and make the necessary numpy arrays
    features, _ = data

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
