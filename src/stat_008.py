#!/usr/bin/env python3

# =============================================================================
# Get number of enrolled courses and approved courses per student
# =============================================================================

import os

import numpy as np
import pandas as pd
from matplotlib import pyplot


import data
import util


output_dir = util.outputDirName(8)


def displayStats(label, series):
    print(label)
    print("\tMin %d" % (series.min()))
    print("\tMax %d" % (series.max()))
    print("\tMean %.02f" % (series.values.mean()))
    print("\tMedian %.02f" % (np.median(series.values)))
    print("\tTotal %d" % (len(series)))


if __name__ == "__main__":
    # Load data
    df = data.load(data.Results)[["StudentsNumber", "Results"]]

    # Number of enrolled courses
    enrolled = df.groupby("StudentsNumber") \
        .agg("count") \
        .rename(columns={"Results": "EnrolledCount"})

    # Number of approved courses
    approved = df \
        .loc[lambda x: x["Results"] == "Aprovado"] \
        .groupby("StudentsNumber") \
        .agg("count") \
        .rename(columns={"Results": "ApproveCount"})

    displayStats("Enrolled", enrolled[["EnrolledCount"]])
    displayStats("Approved", approved[["ApproveCount"]])

    pyplot.boxplot([enrolled[["EnrolledCount"]].values,
                    approved[["ApproveCount"]].values
        ], vert=False)

    util.makeDir(output_dir)
    pyplot.savefig(os.path.join(output_dir, "plot"))
