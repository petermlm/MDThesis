#!/usr/bin/env python3

# =============================================================================
# TODO
# =============================================================================


import data
import tasks


if __name__ == "__main__":
    for i in range(2, 6):
        print("K-Means, %s" % (i))
        tasks.unsupervised(data.dat_001(), i)
