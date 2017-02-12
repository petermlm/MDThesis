#!/usr/bin/env python3

# =============================================================================
# Number of active courses vs total number of activities
# =============================================================================

import os

import numpy as np
import pandas
from matplotlib import pyplot


import data
import util


output_dir = util.outputDirName(6)


def numberOfActs(df):
    # Select only useful columns for this experience
    orig_cols = df[[
        "CourseCodeMoodle",
        "Week",
        "NumberOfActivitiesPerWeek"
    ]]

    # Group by course code and week number, having the total number of
    # activities for that week and for that course.
    group = orig_cols.groupby(["CourseCodeMoodle", "Week"], as_index=False).agg("sum")
    group_sum = group.groupby(by="Week").agg("sum")
    sum_values = group_sum["NumberOfActivitiesPerWeek"].values.tolist()

    return np.array(sum_values)


def weeks(max_weeks, df):
    # Select only useful columns for this experience
    orig_cols = df[[
        "CourseCodeMoodle",
        "Week"
    ]]

    # Get maximum of weeks
    max_weeks = df["Week"].max()

    # Number of courses with activities until this point
    group = orig_cols.groupby(["CourseCodeMoodle"], as_index=False).agg("max")

    counts = group.groupby(["Week"]).count()

    max_week_per_course = [
        counts.loc[i].values[0]
        if i in counts.index else 0
        for i in range(max_weeks+1)]

    # Reverse accumulated
    rev_acc = []
    acc = 0
    for i in max_week_per_course[::-1]:
        acc += i
        rev_acc.insert(0, acc)

    return np.array(rev_acc)


if __name__ == "__main__":
    # Load data
    df = data.load(data.MoodleLogs)

    # Get maximum of weeks
    max_weeks = df["Week"].max()

    # Get values for plots
    number_acts = numberOfActs(df)
    weeks = weeks(max_weeks, df)

    # Plot
    fig, p1 = pyplot.subplots()
    p1.bar(range(max_weeks+1), weeks, width=1.0, facecolor="lightgray", edgecolor="lightgray")
    p2 = p1.twinx()
    p2.plot(range(max_weeks+1), number_acts)

    util.makeDir(output_dir)

    fig.tight_layout()
    pyplot.title("Active Courses vs Number of Activities")
    pyplot.savefig(os.path.join(output_dir, "plot"))
