#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================


import data
import tasks


if __name__ == "__main__":
    for i in range(2, 6):
        print("K-Means, %s" % (i))
        tasks.unsupervised(data.dat_001(), "kmeans", i)

    # Does not get good results and is very slow
    # for i in range(2, 6):
    #     print("Affinity Propagation, %s" % (i))
    #     tasks.unsupervised(data.dat_001(), "affinity", i)
