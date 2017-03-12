#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================


import data
import tasks
import util


if __name__ == "__main__":
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
