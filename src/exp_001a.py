#!/usr/bin/env python3

import sys

import data
import tasks
import util


if __name__ == "__main__":
    limit = 100

    if len(sys.argv) == 1:
        model = "tree"

    elif len(sys.argv) in [2, 3]:
        model = sys.argv[1]

        if len(sys.argv) == 3:
            limit = int(sys.argv[2])

    else:
        print("Usage:")
        print("\texp_001a.py")
        print("\texp_001a.py [tree | bayesian] {limit}")

    df = data.dat_001("binary")
    clf, accuracy = tasks.supervised(df, model)

    # Display True Positives
    util.title("True Positives")
    util.printByCondition(lambda _, c, p: c and p[0], df, clf, limit)

    # Display True Negatives
    util.title("True Negatives")
    util.printByCondition(lambda _, c, p: not c and not p[0], df, clf, limit)

    # Display False Positives
    util.title("False Positives")
    util.printByCondition(lambda _, c, p: c != p[0] and p[0], df, clf)

    # Display False Negatives
    util.title("False Negatives")
    util.printByCondition(lambda _, c, p: c != p[0] and not p[0], df, clf)
