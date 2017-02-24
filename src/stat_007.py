#!/usr/bin/env python3

# =============================================================================
# Get number of students per course and number of approved students per course
# =============================================================================

import os

import numpy as np
import pandas
from matplotlib import pyplot


import data
import util


output_dir = util.outputDirName(6)


if __name__ == "__main__":
    # Load data
    df = data.load(data.Results)[[
        "CourseCodeSiiue",
        "StudentsNumber",
        "Grade"]]

    # Number of students per course
    g1 = df.groupby("CourseCodeSiiue") \
        .agg("count") \
        .sort("StudentsNumber", ascending=False)

    # Number of approved students per course
    g2 = df \
        .loc[lambda x: (x["Grade"] >= 10) & (x["Grade"] <= 20)] \
        .groupby("CourseCodeSiiue").agg("count") \
        .sort("StudentsNumber", ascending=False)

    print(g1)
    print(g2)

    g1_values = g1[["StudentsNumber"]].values.flatten()
    g2_values = g2[["StudentsNumber"]].values.flatten()

    pyplot.bar(range(len(g1_values)), g1_values, width=1.0, facecolor="lightgray", edgecolor="lightgray")
    pyplot.bar(range(len(g2_values)), g2_values, width=1.0, facecolor="blue", edgecolor="blue")

    pyplot.show()
