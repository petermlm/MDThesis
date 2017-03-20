import os
import math


import pandas as pd
from sklearn import preprocessing


data_root = "../../Data/Processed"

CoursesEntriesOverview = os.path.join(data_root, "CoursesEntriesOverview.csv")
CoursesGeneral         = os.path.join(data_root, "CoursesGeneral.csv")
CoursesNoMoodle        = os.path.join(data_root, "CoursesNoMoodle.csv")
CoursesStudents        = os.path.join(data_root, "CoursesStudents.csv")
MoodleLogs             = os.path.join(data_root, "MoodleLogs.csv")
MoodleUsers            = os.path.join(data_root, "MoodleUsers.csv")
Results                = os.path.join(data_root, "Results.csv")
Students               = os.path.join(data_root, "Students.csv")
Profile                = os.path.join(data_root, "Profile.csv")


def load(sheet):
    return pd.read_csv(sheet)


def prepare_dat_001(classes):
    df_stu = load(Students)
    df_cge = load(CoursesGeneral)
    df_log = load(MoodleLogs)
    df_res = load(Results)

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
    def mapClasses(x):
        if classes == "binary":
            if x >= 10 and x <= 20:
                return True
            return False

        elif classes == "2":
            if x >= 10 and x < 12:
                return "10-12"
            elif x >= 12 and x < 14:
                return "12-14"
            elif x >= 14 and x < 16:
                return "14-16"
            elif x >= 16 and x < 18:
                return "16-18"
            elif x >= 18 and x <= 20:
                return "18-20"
            else:
                return "failed"

        elif classes == "4":
            if x >= 10 and x < 14:
                return "10-14"
            elif x >= 14 and x < 18:
                return "14-18"
            elif x >= 18 and x <= 20:
                return "18-20"
            else:
                return "failed"

    if classes == "binary":
        df_final["Grade"] = df_final["Grade"].map(mapClasses)
        df_final.rename(columns={"Grade": "Approved"}, inplace=True)
    else:
        df_final["Grade"] = df_final["Grade"].map(mapClasses)
        df_final.rename(columns={"Grade": "GradeClass"}, inplace=True)

    return df_final.drop(["StudentsNumber"], axis=1)


def dat_001(classes=None):
    # Parse arguments
    arguments = ["binary", "2", "4"]

    if classes is None:
        classes = "binary"
    else:
        if classes not in arguments:
            raise Exception("Argument no in " + str(arguments))

    df = prepare_dat_001(classes)

    def encode(values):
        le = preprocessing.LabelEncoder()
        le.fit(values)
        return le.transform(values)

    def removeNan(value):
        return "none" if type(value) != str else value

    def replaceNan(value):
        return 0 if pd.isnull(value) else value

    # Encode the labels to ints
    df["StudentType"]     = encode(df["StudentType"])
    df["CourseCodeSiiue"] = encode(df["CourseCodeSiiue"])
    df["Semester"]        = encode(df["Semester"].map(removeNan))
    df["Season"]          = encode(df["Season"].map(removeNan))

    # Clean missing numbers from counts
    df["TotalActsOnCourse"] = df["TotalActsOnCourse"].map(replaceNan)
    df["CActsOnCourse"] = df["CActsOnCourse"].map(replaceNan)
    df["RActsOnCourse"] = df["RActsOnCourse"].map(replaceNan)
    df["UActsOnCourse"] = df["UActsOnCourse"].map(replaceNan)
    df["DActsOnCourse"] = df["DActsOnCourse"].map(replaceNan)

    if classes == "binary":
        class_name = "Approved"
    else:
        class_name = "GradeClass"

    return (
        df.drop([class_name], axis=1).values,
        df[[class_name]].values)


def prepare_dat_002():
    df_stu = load(Students)
    df_log = load(MoodleLogs)
    df_res = load(Results)

    # Remove parts of datasets that are not needed
    df_res = df_res[["StudentsNumber", "Grade"]]

    df_log = df_log[[
        "CRUD",
        "NumberOfActivitiesPerWeek",
        "StudentsNumber"]]

    # Replace some values
    def mapBinary(x):
        if x >= 10 and x <= 20:
            return True
        return False

    df_res["Grade"] = df_res["Grade"].map(mapBinary)

    def removeNan(value):
        return 0 if type(value) != float else value

    df_log["StudentsNumber"] = df_log["StudentsNumber"].map(removeNan)

    # Group number of enrolled courses by student
    df_enrolled_courses = df_res \
        .groupby("StudentsNumber") \
        .agg("count") \
        .reset_index()

    df_enrolled_courses.rename(columns={"Grade": "EnrolledCourses"}, inplace=True)

    # Group number of approved courses by student
    df_approved_courses = df_res \
        .loc[lambda df: df["Grade"] == True] \
        .groupby("StudentsNumber") \
        .agg("count") \
        .reset_index()

    df_approved_courses.rename(columns={"Grade": "ApprovedCourses"}, inplace=True)

    # Get logs per student
    df_acts_all = df_log \
        .loc[lambda df: df["StudentsNumber"] != 0] \
        .groupby(["StudentsNumber"]) \
        .agg("sum") \
        .reset_index()

    df_acts_c = df_log \
        .loc[lambda df: df["StudentsNumber"] != 0] \
        .loc[lambda df: df["CRUD"] == "c"] \
        .groupby(["StudentsNumber"]) \
        .agg("sum") \
        .reset_index()

    df_acts_r = df_log \
        .loc[lambda df: df["StudentsNumber"] != 0] \
        .loc[lambda df: df["CRUD"] == "r"] \
        .groupby(["StudentsNumber"]) \
        .agg("sum") \
        .reset_index()

    df_acts_u = df_log \
        .loc[lambda df: df["StudentsNumber"] != 0] \
        .loc[lambda df: df["CRUD"] == "u"] \
        .groupby(["StudentsNumber"]) \
        .agg("sum") \
        .reset_index()

    df_acts_d = df_log \
        .loc[lambda df: df["StudentsNumber"] != 0] \
        .loc[lambda df: df["CRUD"] == "d"] \
        .groupby(["StudentsNumber"]) \
        .agg("sum") \
        .reset_index()

    df_acts_all.rename(columns={"NumberOfActivitiesPerWeek": "ActSumAll"}, inplace=True)
    df_acts_c.rename(columns={"NumberOfActivitiesPerWeek": "ActSumC"}, inplace=True)
    df_acts_r.rename(columns={"NumberOfActivitiesPerWeek": "ActSumR"}, inplace=True)
    df_acts_u.rename(columns={"NumberOfActivitiesPerWeek": "ActSumU"}, inplace=True)
    df_acts_d.rename(columns={"NumberOfActivitiesPerWeek": "ActSumD"}, inplace=True)

    # Merge everything
    df_merged = pd.merge(df_enrolled_courses, df_approved_courses, how="left") \
        .merge(df_acts_all, how="left") \
        .merge(df_acts_c, how="left") \
        .merge(df_acts_r, how="left") \
        .merge(df_acts_u, how="left") \
        .merge(df_acts_d, how="left")

    def removeNanFloat(value):
        return 0 if pd.isnull(value) else value

    df_merged["ApprovedCourses"] = df_merged["ApprovedCourses"].map(removeNanFloat)
    df_merged["ActSumAll"] = df_merged["ActSumAll"].map(removeNanFloat)
    df_merged["ActSumC"] = df_merged["ActSumC"].map(removeNanFloat)
    df_merged["ActSumR"] = df_merged["ActSumR"].map(removeNanFloat)
    df_merged["ActSumU"] = df_merged["ActSumU"].map(removeNanFloat)
    df_merged["ActSumD"] = df_merged["ActSumD"].map(removeNanFloat)

    return df_merged.drop(["StudentsNumber"], axis=1)


def dat_002(classes=None, approvedJoin=False):
    # Parse arguments
    arguments = [None, "2", "4", "6"]

    if classes is not None and classes not in arguments:
        raise Exception("Argument no in " + str(arguments))

    df = prepare_dat_002()

    def mapClasses(x):
        if x == 12:
            x = 11
        iclass = 13 // int(classes)
        return x // math.floor(iclass)

    if classes is not None:
        df["ApprovedCourses"] = df["ApprovedCourses"].map(mapClasses)

    # Approved field will be just another features. There will be no class
    if approvedJoin:
        return (df.values, None)

    # Approved field will be the class of the dataset
    else:
        return (
            df.drop(["ApprovedCourses"], axis=1).values,
            df[["ApprovedCourses"]].values)


def prepare_dat_003(classes):
    df_stu = load(Students)
    df_cge = load(CoursesGeneral)
    df_pro = load(Profile)
    df_res = load(Results)

    # Drop unnecessary fields from datasets
    df_stu = df_stu[["StudentsNumber", "StudentsId"]]
    df_cge = df_cge[["CourseId", "CourseCodeSiiue"]]
    df_pro = df_pro.drop(["Results"], axis=1)

    # Join Profile with Students and with Courses General to get other students
    # and courses id's
    df_pro_ids = df_pro.merge(df_stu, how="left")
    df_pro_ids = df_pro_ids.merge(df_cge, how="left")

    # Join results
    df_all = df_pro_ids.merge(df_res, how="left")

    # Keep only useful fields
    df_final = df_all[[
            "CourseCodeSiiue",
            "NumberOfResources",
            "NumberOfActivities",
            "NumberOfViews",
            "NumberOfSubmissions",
            "Grade"]].copy()

    # Map the class
    def mapClasses(x):
        if classes == "binary":
            if x >= 10 and x <= 20:
                return True
            return False

        elif classes == "2":
            if x >= 10 and x < 12:
                return "10-12"
            elif x >= 12 and x < 14:
                return "12-14"
            elif x >= 14 and x < 16:
                return "14-16"
            elif x >= 16 and x < 18:
                return "16-18"
            elif x >= 18 and x <= 20:
                return "18-20"
            else:
                return "failed"

        elif classes == "4":
            if x >= 10 and x < 14:
                return "10-14"
            elif x >= 14 and x < 18:
                return "14-18"
            elif x >= 18 and x <= 20:
                return "18-20"
            else:
                return "failed"

    if classes == "binary":
        df_final["Grade"] = df_final["Grade"].map(mapClasses)
        df_final.rename(columns={"Grade": "Approved"}, inplace=True)
    else:
        df_final["Grade"] = df_final["Grade"].map(mapClasses)
        df_final.rename(columns={"Grade": "GradeClass"}, inplace=True)

    return df_final


def dat_003(classes=None):
    # Parse arguments
    arguments = ["binary", "2", "4"]

    if classes is None:
        classes = "binary"
    else:
        if classes not in arguments:
            raise Exception("Argument no in " + str(arguments))

    df = prepare_dat_003(classes)

    def encode(values):
        le = preprocessing.LabelEncoder()
        le.fit(values)
        return le.transform(values)

    df["CourseCodeSiiue"] = encode(df["CourseCodeSiiue"])

    if classes == "binary":
        class_name = "Approved"
    else:
        class_name = "GradeClass"

    return (
        df.drop([class_name], axis=1).values,
        df[[class_name]].values)
