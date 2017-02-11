#!/usr/bin/env python3

# =============================================================================
# Plot activities of students over the semester.
#
# This experiment aims at making different plots in order to visualize the #
# activity of students over the semester. He pick the six courses with the most
# activities registered in the logs. We then plot those activities over the
# whole semester and see the relation between the overall number of activities,
# activities that are only Create activities, only Update, etc.
#
# It is noticeable that Read activities are disproportionally greater than the
# other activities, so Create, Update, and Delete activities are also plotted
# in their own graphs
# =============================================================================

import os

import numpy as np
import pandas
from matplotlib import pyplot

import data


output_dir = "exp_001_results"


def outputFileName(index, courses, plot_type):
    file_name = "fig_%d_%s_%s" % (index, courses, plot_type)
    return os.path.join(output_dir, file_name)


def takeGroup(df):
    return df.groupby(["CourseCodeMoodle", "Week"]).agg("sum")


def takeCRUD(df, crud):
    return df.loc[lambda df: df["CRUD"] == crud]


def plotCourse(index, course, groups):
    # Get this course's groups
    group_all = groups["all"].loc[course]
    group_C   = groups["C"].loc[course]
    group_R   = groups["R"].loc[course]
    group_U   = groups["U"].loc[course]
    group_D   = groups["D"].loc[course]

    # Get weeks
    weeks_all = np.array(group_all.index.get_level_values("Week").tolist())
    weeks_C = np.array(group_C.index.get_level_values("Week").tolist())
    weeks_R = np.array(group_R.index.get_level_values("Week").tolist())
    weeks_U = np.array(group_U.index.get_level_values("Week").tolist())
    weeks_D = np.array(group_D.index.get_level_values("Week").tolist())

    # Get number of activities
    act_all = np.array(group_all.values.tolist()).flatten()
    act_C = np.array(group_C.values.tolist()).flatten()
    act_R = np.array(group_R.values.tolist()).flatten()
    act_U = np.array(group_U.values.tolist()).flatten()
    act_D = np.array(group_D.values.tolist()).flatten()

    # Plot all and every crud
    plot_all = pyplot.plot(weeks_all, act_all)
    plot_C, = pyplot.plot(weeks_C, act_C)
    plot_R, = pyplot.plot(weeks_R, act_R)
    plot_U, = pyplot.plot(weeks_U, act_U)
    plot_D, = pyplot.plot(weeks_D, act_D)

    pyplot.title("%d - %s" % (index, course))
    pyplot.figlegend(
        (plot_all[0], plot_C, plot_R, plot_U, plot_D),
        ("All", "C", "R", "U", "D"),
        "upper right")

    pyplot.savefig(outputFileName(index, course, "all"));
    pyplot.clf()

    # Plot the C, U, and D only
    plot_C, = pyplot.plot(weeks_C, act_C)
    plot_U, = pyplot.plot(weeks_U, act_U)
    plot_D, = pyplot.plot(weeks_D, act_D)

    pyplot.title("%d - %s" % (index, course))
    pyplot.figlegend(
        (plot_C, plot_U, plot_D),
        ("C", "U", "D"),
        "upper right")

    pyplot.savefig(outputFileName(index, course, "cud"));
    pyplot.clf()


if __name__ == "__main__":
    # Load data
    df = data.load(data.MoodleLogs)

    # Select only useful columns for this experience
    df_redux = df[[
        "CourseCodeMoodle",
        "CRUD",
        "Week",
        "NumberOfActivitiesPerWeek"
    ]]

    # Get 6 most common courses
    courses_count = df_redux["CourseCodeMoodle"].value_counts()
    common_courses = courses_count.sort_values(ascending=False)[:6]

    # Group by course code and week number, having the total number of
    # activities for that week and for that course. Do this for every CRUD
    # activity and for specific CRUD activities
    groups = {
        "all": takeGroup(df_redux),
        "C":   takeGroup(takeCRUD(df_redux, "c")),
        "R":   takeGroup(takeCRUD(df_redux, "r")),
        "U":   takeGroup(takeCRUD(df_redux, "u")),
        "D":   takeGroup(takeCRUD(df_redux, "d"))
    }

    # Create the directory for the results if it doesn't exist
    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass

    # Get week number and activities number of a specific course
    for index, course in enumerate(common_courses.index.tolist()):
        plotCourse(index, course, groups)
