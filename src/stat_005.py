#!/usr/bin/env python3

# =============================================================================
# Plot total number of activities per week and mean number of activities per
# course per week. Both plots are in the same graph.
# =============================================================================


import os

import numpy as np
import pandas
from matplotlib import pyplot


import data
import util


output_dir = util.outputDirName(5)


if __name__ == "__main__":
    # Load data
    df = data.load(data.MoodleLogs)

    # Get maximum of weeks
    max_weeks = df["Week"].max()

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
    group_mean = group.groupby(by="Week").agg("mean")

    sum_values = np.array(group_sum["NumberOfActivitiesPerWeek"].values.tolist())
    mean_values = np.array(group_mean["NumberOfActivitiesPerWeek"].values.tolist())

    fig, p1 = pyplot.subplots()
    p1.plot(range(max_weeks+1), sum_values)
    p2 = p1.twinx()
    p2.plot(range(max_weeks+1), mean_values, color="red")

    util.makeDir(output_dir)

    fig.tight_layout()
    pyplot.title("Active Courses vs Number of Activities")
    pyplot.savefig(os.path.join(output_dir, "plot"))
