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

    # Group of enrolled
    group_enrolled = enrolled.reset_index() \
        .groupby("EnrolledCount") \
        .agg("count")

    # Group of approved
    group_approved = approved.reset_index() \
        .groupby("ApproveCount") \
        .agg("count")

    # Display results
    displayStats("Enrolled", enrolled[["EnrolledCount"]])
    displayStats("Approved", approved[["ApproveCount"]])

    # Plot graphs
    def prepareForPlot(values, max_len):
        ret = []

        cur_index = 0
        while cur_index < len(values):
            if values[cur_index][0] > len(ret):
                ret.append(0)
                continue

            ret.append(values[cur_index][1])
            cur_index += 1

        while len(ret) < max_len:
            ret.append(0)

        return ret

    group_enrolled = prepareForPlot(group_enrolled.reset_index().values, 13)
    group_approved = prepareForPlot(group_approved.reset_index().values, 13)

    fig, p1 = pyplot.subplots()

    p1.plot(range(13), group_enrolled)
    p1.plot(range(13), group_approved)

    p2 = p1.twinx()

    p2.boxplot([enrolled[["EnrolledCount"]].values,
                    approved[["ApproveCount"]].values
        ], vert=False)


    util.makeDir(output_dir)
    fig.tight_layout()
    pyplot.savefig(os.path.join(output_dir, "plot"))
