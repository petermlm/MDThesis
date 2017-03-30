#!/usr/bin/env python3

import sys

import data
import tasks


def doAll():
    print("Decision Tree Classifier, Original Classes")
    tasks.supervised(data.dat_002(approvedJoin=False), "tree")

    print("Decision Tree Classifier, 2 Classes")
    tasks.supervised(data.dat_002(classes="2", approvedJoin=False), "tree")

    print("Decision Tree Classifier, 4 Classes")
    tasks.supervised(data.dat_002(classes="4", approvedJoin=False), "tree")

    print("Decision Tree Classifier, 6 Classes")
    tasks.supervised(data.dat_002(classes="6", approvedJoin=False), "tree")

    print("Bayesian Network, Original Classes")
    tasks.supervised(data.dat_002(approvedJoin=False), "bayesian")

    print("Bayesian Network, 2 Classes")
    tasks.supervised(data.dat_002(classes="2", approvedJoin=False), "bayesian")

    print("Bayesian Network, 4 Classes")
    tasks.supervised(data.dat_002(classes="4", approvedJoin=False), "bayesian")

    print("Bayesian Network, 6 Classes")
    tasks.supervised(data.dat_002(classes="6", approvedJoin=False), "bayesian")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        doAll()

    elif len(sys.argv) == 3:
        classes_op = None

        if sys.argv[2] in ["2", "4", "6"]:
            classes_op = sys.argv[2]

        df = data.dat_002(classes=classes_op, approvedJoin=False)
        tasks.supervised(df, sys.argv[1])

    else:
        print("Usage:")
        print("\texp_003.py")
        print("\texp_003.py [tree | bayesian] [original | 2 | 4 | 6]")
        exit(1)
