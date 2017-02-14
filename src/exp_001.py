#!/usr/bin/env python3

# =============================================================================
# TOOD
# =============================================================================

import os

import numpy as np
import pandas as pd
from matplotlib import pyplot

import data
import util


def makeDataset(approvedBinary=True):
    df_stu = data.load(data.Students)
    df_cge = data.load(data.CoursesGeneral)
    df_log = data.load(data.MoodleLogs)
    df_res = data.load(data.Results)

    # Join Students and results to obtain a dataset with an entry for each
    # student and actual result, set CourseCodeSiiue to be an index along with
    # StudentsNumber
    df_stu.set_index("StudentsNumber", inplace=True)
    df_res.set_index("StudentsNumber", inplace=True)
    df_stu_res = df_stu.join(df_res)

    df_stu_res.set_index("CourseCodeSiiue", inplace=True, append=True)
    df_stu_res = df_stu_res[["EnrollementCount", "StudentType", "Grade"]]

    # Get the logs and add CourseCodeSiiue to them. Then take only the useful
    # columns
    df_log = df_log.merge(
            df_cge[["CourseCodeMoodle", "CourseCodeSiiue"]],
            on = "CourseCodeMoodle",
            how = "left") \
        [["StudentsNumber",
          # "CourseCodeSiiue",
          "CourseCodeMoodle",
          "CRUD",
          "NumberOfActivitiesPerWeek"]]

    # Perform group-bys in order to get count of CRUD activities
    df_acts_all = df_log \
        .groupby(["StudentsNumber", "CourseCodeMoodle"]) \
        .agg("sum")

    df_acts_c = df_log \
        .loc[lambda df: df["CRUD"] == "c"] \
        .groupby(["StudentsNumber", "CourseCodeMoodle"]) \
        .agg("sum")

    df_acts_r = df_log \
        .loc[lambda df: df["CRUD"] == "r"] \
        .groupby(["StudentsNumber", "CourseCodeMoodle"]) \
        .agg("sum")

    df_acts_u = df_log \
        .loc[lambda df: df["CRUD"] == "u"] \
        .groupby(["StudentsNumber", "CourseCodeMoodle"]) \
        .agg("sum")

    df_acts_d = df_log \
        .loc[lambda df: df["CRUD"] == "d"] \
        .groupby(["StudentsNumber", "CourseCodeMoodle"]) \
        .agg("sum")

    df_acts_all.columns = ["TotalActsOnCourse"]
    df_acts_c.columns = ["CActsOnCourse"]
    df_acts_r.columns = ["RActsOnCourse"]
    df_acts_u.columns = ["UActsOnCourse"]
    df_acts_d.columns = ["DActsOnCourse"]

    df_acts_j = df_acts_all.join(df_acts_c)
    df_acts_j = df_acts_j.join(df_acts_r)
    df_acts_j = df_acts_j.join(df_acts_u)
    df_acts_j = df_acts_j.join(df_acts_d)

    # Change acts_j CourseCodeMoodle to use CourseCodeSiiue
    df_acts_j = pd.merge(
            df_acts_j.reset_index(),
            df_cge[["CourseCodeMoodle", "CourseCodeSiiue"]],
            on = "CourseCodeMoodle",
            how = "inner") \
        [["StudentsNumber",
          "CourseCodeSiiue",
          "TotalActsOnCourse",
          "CActsOnCourse",
          "RActsOnCourse",
          "UActsOnCourse",
          "DActsOnCourse"]] \
        .set_index(["StudentsNumber", "CourseCodeSiiue"])

    # Final dataset
    df_final = df_stu_res.join(df_acts_j)

    # Join course information to final dataset
    df_final = pd.merge(
            df_final.reset_index(),
            df_cge[["CourseCodeSiiue", "Semester", "Season"]].drop_duplicates(),
            on="CourseCodeSiiue",
            how="left")

    # Map the class
    def mapBinary(x):
        if x >= 10 and x <= 20:
            return True
        return False

    def mapClasses(x):
        pass # TODO

    if approvedBinary:
        df_final["Grade"] = df_final["Grade"].map(mapBinary)
        df_final.rename(columns={"Grade": "Approved"}, inplace=True)
    else:
        df_final["Grade"] = df_final["Grade"].map(mapClasses)
        df_final.rename(columns={"Grade": "GradeClass"}, inplace=True)

    return df_final


def BinaryClass():
    df = makeDataset(approvedBinary=True)


def GradeClass():
    df = makeDataset(approvedBinary=False)


if __name__ == "__main__":
    BinaryClass()
    GradeClass()
