#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================


import sys


import data
import tasks


def doAll():
    print("Decision Tree Classifier, Binary Class")
    tasks.supervised(data.dat_003("binary"), "tree")

    print("Decision Tree Classifier, Grades Classes 2 by 2")
    tasks.supervised(data.dat_003("2"), "tree")

    print("Decision Tree Classifier, Grades Classes 4 by 4")
    tasks.supervised(data.dat_003("4"), "tree")

    print("Bayesian Network, Binary Class")
    tasks.supervised(data.dat_003("binary"), "bayesian")

    print("Bayesian Network, Grades Classes 2 by 2")
    tasks.supervised(data.dat_003("2"), "bayesian")

    print("Bayesian Network, Grades Classes 4 by 4")
    tasks.supervised(data.dat_003("4"), "bayesian")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        doAll()

    elif len(sys.argv) == 3:
        tasks.supervised(data.dat_003(sys.argv[2]), sys.argv[1])

    else:
        print("Usage:")
        print("\texp_005.py")
        print("\texp_005.py [tree | bayesian] [binary | 2 | 4]")
        exit(1)
