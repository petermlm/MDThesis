#!/usr/bin/env python3

import sys

import data
import tasks
import util


if __name__ == "__main__":
    limit = None
    classes_op = None

    if len(sys.argv) == 1:
        model = "tree"

    elif len(sys.argv) in [3, 4]:
        model = sys.argv[1]

        if sys.argv[2] in ["2", "4", "6"]:
            classes_op = sys.argv[2]

        if len(sys.argv) == 4:
            limit = int(sys.argv[3])

    else:
        print("Usage:")
        print("\texp_003a.py")
        print("\texp_003a.py [tree | bayesian] [original | 2 | 4 | 6] {limit}")
        exit(1)

    df = data.dat_002(classes=classes_op, approvedJoin=False)
    clf, accuracy = tasks.supervised(df, model)

    # Display True Positives
    util.title("Correctly classified")
    util.printByCondition(lambda _, c, p: c == p[0], df, clf, limit)

    # Display True Negatives
    util.title("Incorrectly Classified")
    util.printByCondition(lambda _, c, p: c != p[0], df, clf, limit)
