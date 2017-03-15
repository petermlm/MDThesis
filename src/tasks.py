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
    best_clf = None
    best_accuracy = 0

    for train_index, test_index in kf.split(features):
        # Fit
        if model == "tree":
            clf = tree.DecisionTreeClassifier()
        elif model == "bayesian":
            clf = MultinomialNB()

        clf.fit(features[train_index], classes[train_index])

        # And get it's accuracy
        accuracy = metrics.accuracy_score(
            classes[test_index],
            clf.predict(features[test_index]))

        # Keep best
        if accuracy > best_accuracy:
            best_clf = clf
            best_accuracy = accuracy

        print("\t%0.2f" % (accuracy))

    return (best_clf, best_accuracy)


def unsupervised(data, cluster_number):
    # Get dataset and make the necessary numpy arrays
    features, _ = data

    # Create folds for training and testing
    kf = KFold(n_splits=10)
    kf.get_n_splits(features)

    # Train and test with different folds
    best_kmeans = None
    best_silhouette = 0

    for train_index, test_index in kf.split(features):
        kmeans = KMeans(n_clusters=cluster_number, random_state=0)
        kmeans.fit(features[train_index])

        # And get it's silhouette score
        silhouette = metrics.silhouette_score(
            features[train_index],
            kmeans.labels_)

        # Keep best
        if silhouette > best_silhouette:
            best_kmeans = kmeans
            best_silhouette = silhouette

        print("\t%0.2f" % (silhouette))

    return (best_kmeans, best_silhouette)
