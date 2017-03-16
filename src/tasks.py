from sklearn import tree
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
from sklearn.model_selection import KFold


def supervised(data, model):
    # Get dataset and make the necessary numpy arrays
    features, classes = data

    # Create folds for training and testing
    kf = KFold(n_splits=10)
    kf.get_n_splits(features)

    # Train and test with different folds
    best_clf = None
    max_accuracy = 0
    min_accuracy = 0
    sum_accuracy = 0

    for train_index, test_index in kf.split(features):
        # Fit
        if model == "tree":
            clf = tree.DecisionTreeClassifier()
        elif model == "bayesian":
            clf = MultinomialNB()
        else:
            raise Exception("Model %s doesn't exist" % (model))

        clf.fit(features[train_index], classes[train_index])

        # And get it's accuracy
        accuracy = metrics.accuracy_score(
            classes[test_index],
            clf.predict(features[test_index]))

        # Keep info
        if best_clf is None:
            best_clf = clf
            max_accuracy = accuracy
            min_accuracy = accuracy

        elif accuracy > max_accuracy:
            best_clf = clf
            max_accuracy = accuracy

        elif accuracy < min_accuracy:
            min_accuracy = accuracy

        sum_accuracy += accuracy

        print("\t%0.2f" % (accuracy))

    print("%0.2f, %0.2f, %0.2f" % (max_accuracy, min_accuracy, sum_accuracy / 10))

    return (best_clf, max_accuracy)


def unsupervised(data, model, cluster_number):
    # Get dataset and make the necessary numpy arrays
    features, _ = data

    # Create folds for training and testing
    kf = KFold(n_splits=10)
    kf.get_n_splits(features)

    # Train and test with different folds
    best_clf = None
    max_silhouette = 0
    min_silhouette = 0
    sum_silhouette = 0

    for train_index, test_index in kf.split(features):
        # Fit
        if model == "kmeans":
            clf = KMeans(n_clusters=cluster_number, random_state=0)
        elif model == "affinity":
            clf = AffinityPropagation()
        else:
            raise Exception("Model %s doesn't exist" % (model))

        clf.fit(features[train_index])

        # And get it's silhouette score
        silhouette = metrics.silhouette_score(
            features[train_index],
            clf.labels_)

        # Keep info
        if best_clf is None:
            best_clf = clf
            max_silhouette = silhouette
            min_silhouette = silhouette

        elif silhouette > max_silhouette:
            best_clf = clf
            max_silhouette = silhouette

        elif silhouette < min_silhouette:
            best_clf = clf
            min_silhouette = silhouette

        sum_silhouette += silhouette

        print("\t%0.2f" % (silhouette))

    print("%0.2f, %0.2f, %0.2f" % (max_silhouette, min_silhouette, sum_silhouette / 10))

    return (best_clf, max_silhouette)
