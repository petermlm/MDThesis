#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================

import os

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold

import data
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
    execute("tree", "binary")

    print("Decision Tree Classifier, Grades Classes 2 by 2")
    execute("tree", "2")

    print("Decision Tree Classifier, Grades Classes 4 by 4")
    execute("tree", "4")

    print("Bayesian Network, Binary Class")
    execute("bayesian", "binary")

    print("Bayesian Network, Grades Classes 2 by 2")
    execute("bayesian", "2")

    print("Bayesian Network, Grades Classes 4 by 4")
    execute("bayesian", "4")
