#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================


import data
import tasks
import util


def execute(model, classes_arg):
    # Get dataset and make the necessary numpy arrays
    features, classes = data.dat_001(classes=classes_arg)

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


if __name__ == "__main__":
    print("Decision Tree Classifier, Binary Class")
    tasks.supervised(data.dat_001("binary"), "tree")

    print("Decision Tree Classifier, Grades Classes 2 by 2")
    tasks.supervised(data.dat_001("2"), "tree")

    print("Decision Tree Classifier, Grades Classes 4 by 4")
    tasks.supervised(data.dat_001("4"), "tree")

    print("Bayesian Network, Binary Class")
    tasks.supervised(data.dat_001("binary"), "bayesian")

    print("Bayesian Network, Grades Classes 2 by 2")
    tasks.supervised(data.dat_001("2"), "bayesian")

    print("Bayesian Network, Grades Classes 4 by 4")
    tasks.supervised(data.dat_001("4"), "bayesian")
