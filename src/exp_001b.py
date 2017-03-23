#!/usr/bin/env python3

import sys

import data
import tasks
import util


if __name__ == "__main__":
    limit = None

    if len(sys.argv) == 1:
        model = "tree"
        classes = "2"

    elif len(sys.argv) in [3, 4]:
        model = sys.argv[1]
        classes = sys.argv[2]

        if len(sys.argv) == 4:
            limit = int(sys.argv[2])

    else:
        print("Usage:")
        print("\texp_001a.py")
        print("\texp_001a.py [tree | bayesian] [2 | 4] {limit}")
        exit(1)

    df = data.dat_001(classes)
    clf, accuracy = tasks.supervised(df, model)

    # Display True Positives
    util.title("Correctly classified")
    util.printByCondition(lambda _, c, p: c == p[0], df, clf, limit)

    # Display True Negatives
    util.title("Incorrectly Classified")
    util.printByCondition(lambda _, c, p: c != p[0], df, clf, limit)
