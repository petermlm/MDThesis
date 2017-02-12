#!/usr/bin/env python3

# =============================================================================
# This experiment plots the number of courses for each possible number of
# credits in a bars chart.
# =============================================================================

import os

import numpy as np
import pandas
from matplotlib import pyplot

import data
import util


output_dir = util.outputDirName(1)

if __name__ == "__main__":
    df = data.load(data.CoursesGeneral)

    groups = df.groupby("Credits").agg("count")

    print(groups["CourseName"])

    courses = groups.index.tolist()
    counts = groups["CourseName"].values.tolist()

    util.makeDir(output_dir)

    pyplot.bar(courses, counts)
    pyplot.title("Number of Courses Grouped by Credits")
    pyplot.savefig(os.path.join(output_dir, "counts"))
