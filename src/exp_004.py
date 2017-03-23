#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================


import data
import tasks


if __name__ == "__main__":
    print("Original Classes")
    for i in range(2, 7):
        print("K-Means, %s" % (i))
        tasks.unsupervised(data.dat_002(approvedJoin=True), "kmeans", i)

    print("2 Classes")
    for i in range(2, 7):
        print("K-Means, %s" % (i))
        tasks.unsupervised(data.dat_002(classes="2", approvedJoin=True), "kmeans", i)

    print("4 Classes")
    for i in range(2, 7):
        print("K-Means, %s" % (i))
        tasks.unsupervised(data.dat_002(classes="4", approvedJoin=True), "kmeans", i)

    print("6 Classes")
    for i in range(2, 7):
        print("K-Means, %s" % (i))
        tasks.unsupervised(data.dat_002(classes="6", approvedJoin=True), "kmeans", i)

    # Results are terrible
    # for i in range(2, 7):
    #     print("Affinity Propagation, %s" % (i))
    #     tasks.unsupervised(data.dat_002(approvedJoin=False), "affinity", i)
