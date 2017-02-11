#!/usr/bin/env python3

# =============================================================================
# Mean of activities per week. It falls. Write this conclusion

"""
The mean of the activities per week drops. But the number of courses which end
drops with it.

Is the number of activities is consistent along the semester? Or does it drop?

Make further experiments.
"""

# =============================================================================


import numpy as np
import pandas
from matplotlib import pyplot


import data


def numberOfActs(alunos_moodle_data):
    # Get maximum of weeks
    max_weeks = alunos_moodle_data["Week"].max()

    # Select only useful columns for this experience
    orig_cols = alunos_moodle_data[[
        "CourseCodeMoodle",
        "Week",
        "NumberOfActivitiesPerWeek"
    ]]

    # Group by course code and week number, having the total number of
    # activities for that week and for that course.
    group = orig_cols.groupby(["CourseCodeMoodle", "Week"], as_index=False).agg("sum")
    group_sum = group.groupby(by="Week").agg("sum")
    sum_values = group_sum["NumberOfActivitiesPerWeek"].values.tolist()

    pyplot.plot(range(len(sum_values)), np.array(sum_values))
    pyplot.show()


def weeks(alunos_moodle_data):
    # Get maximum of weeks
    max_weeks = alunos_moodle_data["Week"].max()

    # Select only useful columns for this experience
    orig_cols = alunos_moodle_data[[
        "CourseCodeMoodle",
        "Week"
    ]]

    # Number of courses with activities until this point
    group = orig_cols.groupby(["CourseCodeMoodle"], as_index=False).agg("max")

    counts = group.groupby(["Week"]).count()

    max_week_per_course = []
    for i in range(max_weeks+1):
        if i in counts.index:
            max_week_per_course.append(counts.loc[i].values[0])
        else:
            max_week_per_course.append(0)

    # Reverse acc
    rev_acc = []
    acc = 0
    for i in max_week_per_course[::-1]:
        acc += i
        rev_acc.insert(0, acc)

    fig, p1 = pyplot.subplots()
    p1.bar(range(max_weeks+1), rev_acc, width=1.0, facecolor='red', edgecolor='red')
    p2 = p1.twinx()
    p2.bar(range(max_weeks+1), max_week_per_course, width=1.0, facecolor='black', edgecolor='black')

    fig.tight_layout()
    pyplot.show()


if __name__ == "__main__":
    # Load data
    df = data.load(data.MoodleLogs)

    numberOfActs(df)
    pyplot.clf()
    weeks(df)
