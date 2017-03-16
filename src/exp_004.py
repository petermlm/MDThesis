#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================


import data
import tasks


if __name__ == "__main__":
    for i in range(2, 7):
        print("K-Means, %s" % (i))
        tasks.unsupervised(data.dat_002(approvedJoin=False), i)
